from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from scripts.verify_validation_artifact import (
    generate_selected_station_metadata,
    recompute_checksums_and_archive_manifest,
    verify_artifact,
    write_aggregate_quality_summary,
    write_strict_token_rejection_explanation,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_minimal_artifact(root: Path) -> None:
    for directory in ["raw_inputs", "canonical_cleaned", "quality_reports"]:
        (root / directory).mkdir(parents=True)

    station_rows = []
    selection_rows = []
    for index in range(100):
        station_id = f"{index:011d}"
        raw_path = root / "raw_inputs" / f"{station_id}.parquet"
        canonical_path = root / "canonical_cleaned" / f"{station_id}_cleaned.csv"
        quality_path = root / "quality_reports" / f"{station_id}_quality_report.json"
        raw_path.write_text(f"raw {station_id}\n", encoding="utf-8")
        canonical_path.write_text("STATION,DATE\n", encoding="utf-8")
        quality_path.write_text(
            json.dumps(
                {
                    "parse_error_rows": 0,
                    "strict_parse_summary": {
                        "skipped_encoded_columns": ["HL1"] if index == 0 else [],
                        "unsupported_identifier_columns": ["HL1"] if index == 0 else [],
                    },
                }
            )
            + "\n",
            encoding="utf-8",
        )
        station_rows.append(
            {
                "station_id": station_id,
                "status": "success",
                "input_rows": 1,
                "output_rows": 1,
                "runtime_seconds": 0.1,
                "archived_raw_input_path": f"raw_inputs/{station_id}.parquet",
                "raw_sha256": _sha256(raw_path),
                "canonical_output_path": f"canonical_cleaned/{station_id}_cleaned.csv",
                "canonical_output_sha256": _sha256(canonical_path),
                "quality_report_path": f"quality_reports/{station_id}_quality_report.json",
                "domain_outputs_generated": False,
                "warnings_count": 1 if index == 0 else 0,
                "error_type": "",
                "error_message": "",
            }
        )
        selection_rows.append(
            {
                "station_id": station_id,
                "selection_status": "selected",
                "file_size_bytes": raw_path.stat().st_size,
                "size_stratum": "q1",
                "raw_sha256": _sha256(raw_path),
            }
        )

    _write_csv(
        root / "station_results.csv",
        list(station_rows[0].keys()),
        station_rows,
    )
    _write_csv(
        root / "station_selection_manifest.csv",
        list(selection_rows[0].keys()),
        selection_rows,
    )
    (root / "strict_parse_summary_report.json").write_text(
        json.dumps(
            {
                "token_validation_rejections": {
                    "affected_station_count": 1,
                    "token_rejections_by_identifier": {"HL1": 1},
                    "token_rejections_by_identifier_part": {"HL1.part_1": 1},
                    "token_rejections_by_reason": {"token_width_mismatch": 1},
                    "top_affected_stations": [{"station_id": "00000000000", "token_rejection_count": 1}],
                    "total_token_rejection_count": 1,
                }
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (root / "run_manifest.json").write_text('{"build_id":"test-build"}\n', encoding="utf-8")
    for name in ["archive_manifest.json", "aggregate_quality_summary.json"]:
        (root / name).write_text("{}\n", encoding="utf-8")
    for name in [
        "aggregate_quality_summary.md",
        "strict_parse_summary_report.md",
        "strict_token_rejection_explanation.md",
        "summary.md",
        "selected_station_metadata.csv",
    ]:
        (root / name).write_text("placeholder\n", encoding="utf-8")

    checksum_lines = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != "checksums.txt":
            checksum_lines.append(f"{_sha256(path)}  {path.relative_to(root).as_posix()}")
    (root / "checksums.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")


def test_verify_validation_artifact_accepts_minimal_valid_fixture(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)

    assert verify_artifact(artifact) == []


def test_generate_selected_station_metadata_uses_manifest_and_results(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)

    metadata_path = generate_selected_station_metadata(artifact)
    rows = list(csv.DictReader(metadata_path.open(newline="", encoding="utf-8")))

    assert len(rows) == 100
    assert rows[0]["station_id"] == "00000000000"
    assert rows[0]["input_rows"] == "1"
    assert rows[0]["output_rows"] == "1"
    assert rows[0]["size_stratum"] == "q1"
    assert rows[0]["raw_input_sha256"]
    assert rows[0]["canonical_output_sha256"]


def test_write_aggregate_quality_summary_from_existing_reports(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)

    json_path, markdown_path = write_aggregate_quality_summary(artifact)
    payload = json.loads(json_path.read_text(encoding="utf-8"))

    assert markdown_path.exists()
    assert payload["total_stations"] == 100
    assert payload["successful_stations"] == 100
    assert payload["row_parity"] is True
    assert payload["total_warnings"] == 1
    assert payload["strict_token_rejection_total"] == 1
    assert payload["unsupported_identifiers"] == {"HL1": 1}


def test_write_strict_token_rejection_explanation_uses_actual_counts(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)
    write_aggregate_quality_summary(artifact)

    path = write_strict_token_rejection_explanation(artifact)
    text = path.read_text(encoding="utf-8")

    assert "Total strict token rejections: 1" in text
    assert "Affected stations: 1" in text
    assert "HL1: 1" in text
    assert "7.3M" not in text


def test_recompute_archive_manifest_classifies_domains_as_supplementary(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)
    for domain in [
        "clouds",
        "core_meteorology",
        "precipitation",
        "pressure_temperature",
        "quality_codes",
        "remarks",
        "visibility",
        "wind",
    ]:
        domain_dir = artifact / "domains" / domain
        domain_dir.mkdir(parents=True)
        for index in range(100):
            station_id = f"{index:011d}"
            (domain_dir / f"{station_id}_{domain}.csv").write_text("STATION,DATE\n", encoding="utf-8")

    manifest_path = recompute_checksums_and_archive_manifest(artifact)
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    domain_inventory = [
        entry for entry in payload["directory_inventory"] if entry["path"] == "domains"
    ]

    assert domain_inventory
    assert payload["build_id"] == "test-build"
    assert domain_inventory[0].get("supplementary_not_primary") is True
    assert "domains/" in payload["archive_content_classification"]["supplementary"]


def test_verify_artifact_treats_domains_as_optional_supplement(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    _write_minimal_artifact(artifact)

    assert verify_artifact(artifact, verify_hashes=False) == []
    failures = verify_artifact(artifact, verify_hashes=False, verify_domains=True)
    assert "missing supplementary domains directory" in failures
