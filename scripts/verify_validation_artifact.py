#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any


VALIDATION_BOUNDARY_STATEMENT = (
    "This validation artifact supports deterministic reproducibility from "
    "archived validation inputs to archived outputs. Reconstruction from "
    "upstream NOAA archives is not claimed because upstream NOAA source URLs "
    "and checksums are not preserved within this artifact."
)
LEGACY_PRIMARY_DOI_PLACEHOLDERS = (
    "TODO_" + "BEFORE_DOI",
    "TO_BE_ADDED_" + "BEFORE_JOSS_SUBMISSION",
)

PRIMARY_ARCHIVE_BOUNDARY_STATEMENT = (
    "The primary DOI archive contains the canonical reproducibility boundary:\n\n"
    "archived inputs → deterministic NOAA-Spec processing → canonical cleaned outputs"
)

DOMAINS_SUPPLEMENT_STATEMENT = (
    "Domain outputs are convenience projections intended to improve interpretability "
    "for downstream workflows. They are derived from canonical cleaned outputs and "
    "are not required to reproduce NOAA-Spec's core deterministic cleaning behavior.\n\n"
    "Domain outputs are archived separately as supplementary artifacts and are "
    "outside the primary reproducibility claim."
)


REQUIRED_TOP_LEVEL_FILES = {
    "aggregate_quality_summary.json",
    "aggregate_quality_summary.md",
    "archive_manifest_primary.json",
    "checksums_primary.txt",
    "run_manifest.json",
    "selected_station_metadata.csv",
    "station_results.csv",
    "station_selection_manifest.csv",
    "strict_parse_summary_report.json",
    "strict_parse_summary_report.md",
    "strict_token_rejection_explanation.md",
    "summary.md",
}

REQUIRED_DOMAINS_TOP_LEVEL_FILES = {
    "archive_manifest_domains.json",
    "checksums_domains.txt",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _now_utc_isoformat() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _artifact_build_id(artifact_root: Path) -> str:
    run_manifest = artifact_root / "run_manifest.json"
    if run_manifest.exists():
        try:
            return str(_read_json(run_manifest).get("build_id") or "")
        except json.JSONDecodeError:
            pass
    name = artifact_root.name
    return name.removeprefix("build_")


def verify_checksums(artifact_root: Path, checksum_filename: str) -> list[str]:
    failures: list[str] = []
    checksums_path = artifact_root / checksum_filename
    if not checksums_path.exists():
        return [f"missing {checksum_filename}"]

    for line_number, raw_line in enumerate(checksums_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            expected_hash, relative_path = line.split(maxsplit=1)
        except ValueError:
            failures.append(f"malformed {checksum_filename} line {line_number}: {raw_line!r}")
            continue

        target = artifact_root / relative_path
        if not target.exists():
            failures.append(f"checksum target missing: {relative_path}")
            continue
        actual_hash = _sha256(target)
        if actual_hash != expected_hash:
            failures.append(
                f"checksum mismatch for {relative_path}: expected {expected_hash}, got {actual_hash}"
            )
    return failures


def _verify_root(artifact_root: Path) -> list[str]:
    failures: list[str] = []
    if not artifact_root.exists():
        return [f"artifact path does not exist: {artifact_root}"]
    if not artifact_root.is_dir():
        return [f"artifact path is not a directory: {artifact_root}"]
    return failures


def verify_primary_artifact(
    artifact_root: Path,
    *,
    verify_hashes: bool = True,
) -> list[str]:
    artifact_root = artifact_root.resolve()
    failures: list[str] = _verify_root(artifact_root)
    if failures:
        return failures

    for name in sorted(REQUIRED_TOP_LEVEL_FILES):
        if not (artifact_root / name).exists():
            failures.append(f"missing required file: {name}")

    expected_counts = {
        "raw_inputs": ("*.parquet", 100),
        "canonical_cleaned": ("*_cleaned.csv", 100),
        "quality_reports": ("*_quality_report.json", 100),
    }
    for directory_name, (pattern, expected_count) in expected_counts.items():
        directory = artifact_root / directory_name
        if not directory.is_dir():
            failures.append(f"missing required directory: {directory_name}")
            continue
        actual_count = len(list(directory.glob(pattern)))
        if actual_count != expected_count:
            failures.append(f"{directory_name} contains {actual_count} {pattern} files, expected {expected_count}")

    station_results_path = artifact_root / "station_results.csv"
    if station_results_path.exists():
        station_results = _read_csv(station_results_path)
        if len(station_results) != 100:
            failures.append(f"station_results.csv has {len(station_results)} rows, expected 100")
        statuses = Counter(row.get("status", "") for row in station_results)
        if statuses != {"success": 100}:
            failures.append(f"station_results.csv statuses are {dict(statuses)}, expected {{'success': 100}}")

        input_total = sum(int(row.get("input_rows") or 0) for row in station_results)
        output_total = sum(int(row.get("output_rows") or 0) for row in station_results)
        if input_total != output_total:
            failures.append(f"summed input_rows ({input_total}) != summed output_rows ({output_total})")

    if verify_hashes:
        failures.extend(verify_checksums(artifact_root, "checksums_primary.txt"))

    manifest_path = artifact_root / "archive_manifest_primary.json"
    if manifest_path.exists():
        try:
            payload = _read_json(manifest_path)
            if payload.get("archive_type") != "primary":
                failures.append(
                    f"archive_manifest_primary.json archive_type is {payload.get('archive_type')!r}, expected 'primary'"
                )
            if payload.get("checksum_file") != "checksums_primary.txt":
                failures.append("archive_manifest_primary.json checksum_file is not checksums_primary.txt")
        except json.JSONDecodeError as exc:
            failures.append(f"archive_manifest_primary.json is not valid JSON: {exc}")

    return failures


def verify_domains_artifact(
    artifact_root: Path,
    *,
    verify_hashes: bool = True,
) -> list[str]:
    artifact_root = artifact_root.resolve()
    failures: list[str] = _verify_root(artifact_root)
    if failures:
        return failures

    for name in sorted(REQUIRED_DOMAINS_TOP_LEVEL_FILES):
        if not (artifact_root / name).exists():
            failures.append(f"missing required supplementary file: {name}")

    domain_root = artifact_root / "domains"
    expected_domains = {
        "clouds",
        "core_meteorology",
        "precipitation",
        "pressure_temperature",
        "quality_codes",
        "remarks",
        "visibility",
        "wind",
    }
    if not domain_root.is_dir():
        failures.append("missing supplementary domains directory")
    else:
        for domain in sorted(expected_domains):
            domain_dir = domain_root / domain
            if not domain_dir.is_dir():
                failures.append(f"missing supplementary domain directory: domains/{domain}")
                continue
            actual_count = len(list(domain_dir.glob(f"*_{domain}.csv")))
            if actual_count != 100:
                failures.append(
                    f"domains/{domain} contains {actual_count} *_{domain}.csv files, expected 100"
                )

    if verify_hashes:
        failures.extend(verify_checksums(artifact_root, "checksums_domains.txt"))

    manifest_path = artifact_root / "archive_manifest_domains.json"
    if manifest_path.exists():
        try:
            payload = _read_json(manifest_path)
            if payload.get("archive_type") != "supplementary_domains":
                failures.append(
                    "archive_manifest_domains.json archive_type is "
                    f"{payload.get('archive_type')!r}, expected 'supplementary_domains'"
                )
            if payload.get("checksum_file") != "checksums_domains.txt":
                failures.append("archive_manifest_domains.json checksum_file is not checksums_domains.txt")
        except json.JSONDecodeError as exc:
            failures.append(f"archive_manifest_domains.json is not valid JSON: {exc}")

    return failures


def verify_artifact(
    artifact_root: Path,
    *,
    verify_hashes: bool = True,
    verify_domains: bool = False,
    verify_all: bool = False,
) -> list[str]:
    if verify_all:
        return verify_primary_artifact(artifact_root, verify_hashes=verify_hashes) + verify_domains_artifact(
            artifact_root,
            verify_hashes=verify_hashes,
        )
    if verify_domains:
        return verify_domains_artifact(artifact_root, verify_hashes=verify_hashes)
    return verify_primary_artifact(artifact_root, verify_hashes=verify_hashes)


def _read_parquet_station_metadata(path: Path) -> dict[str, str]:
    try:
        import pandas as pd
    except ImportError:
        return {}

    try:
        columns = ["NAME", "LATITUDE", "LONGITUDE", "DATE"]
        frame = pd.read_parquet(path, columns=columns)
    except Exception:
        return {}

    if frame.empty:
        return {}

    first = frame.iloc[0]
    return {
        "station_name": "" if first.get("NAME") is None else str(first.get("NAME")),
        "latitude": "" if first.get("LATITUDE") is None else str(first.get("LATITUDE")),
        "longitude": "" if first.get("LONGITUDE") is None else str(first.get("LONGITUDE")),
        "min_date": "" if frame["DATE"].empty else str(frame["DATE"].min()),
        "max_date": "" if frame["DATE"].empty else str(frame["DATE"].max()),
    }


def generate_selected_station_metadata(artifact_root: Path) -> Path:
    selection_rows = {
        row["station_id"]: row
        for row in _read_csv(artifact_root / "station_selection_manifest.csv")
        if row.get("selection_status") == "selected"
    }
    result_rows = {row["station_id"]: row for row in _read_csv(artifact_root / "station_results.csv")}

    output_path = artifact_root / "selected_station_metadata.csv"
    fieldnames = [
        "station_id",
        "station_name",
        "latitude",
        "longitude",
        "min_date",
        "max_date",
        "input_rows",
        "output_rows",
        "raw_input_size_bytes",
        "size_stratum",
        "raw_input_sha256",
        "canonical_output_sha256",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for station_id in sorted(result_rows):
            result = result_rows[station_id]
            selection = selection_rows.get(station_id, {})
            raw_path = artifact_root / result.get("archived_raw_input_path", "")
            parquet_metadata = _read_parquet_station_metadata(raw_path) if raw_path.exists() else {}
            writer.writerow(
                {
                    "station_id": station_id,
                    "station_name": parquet_metadata.get("station_name", ""),
                    "latitude": parquet_metadata.get("latitude", ""),
                    "longitude": parquet_metadata.get("longitude", ""),
                    "min_date": parquet_metadata.get("min_date", ""),
                    "max_date": parquet_metadata.get("max_date", ""),
                    "input_rows": result.get("input_rows", ""),
                    "output_rows": result.get("output_rows", ""),
                    "raw_input_size_bytes": selection.get("file_size_bytes", ""),
                    "size_stratum": selection.get("size_stratum", ""),
                    "raw_input_sha256": result.get("raw_sha256", "") or selection.get("raw_sha256", ""),
                    "canonical_output_sha256": result.get("canonical_output_sha256", ""),
                }
            )
    return output_path


def build_aggregate_quality_summary(artifact_root: Path) -> dict[str, Any]:
    station_results = _read_csv(artifact_root / "station_results.csv")
    strict_summary = _read_json(artifact_root / "strict_parse_summary_report.json")
    token_summary = strict_summary.get("token_validation_rejections", {})

    warnings_by_station = Counter(
        {row["station_id"]: int(row.get("warnings_count") or 0) for row in station_results}
    )
    skipped_identifiers: Counter[str] = Counter()
    unsupported_identifiers: Counter[str] = Counter()
    parse_error_rows = 0
    for report_path in sorted((artifact_root / "quality_reports").glob("*_quality_report.json")):
        report = _read_json(report_path)
        parse_error_rows += int(report.get("parse_error_rows") or 0)
        strict = report.get("strict_parse_summary", {})
        skipped_identifiers.update(strict.get("skipped_encoded_columns", []))
        unsupported_identifiers.update(strict.get("unsupported_identifier_columns", []))

    total_input_rows = sum(int(row.get("input_rows") or 0) for row in station_results)
    total_output_rows = sum(int(row.get("output_rows") or 0) for row in station_results)
    successful_stations = sum(1 for row in station_results if row.get("status") == "success")

    return {
        "artifact_id": "aggregate_quality_summary",
        "schema_version": "1.0.0",
        "build_id": _artifact_build_id(artifact_root),
        "created_utc": _now_utc_isoformat(),
        "total_stations": len(station_results),
        "successful_stations": successful_stations,
        "failed_stations": sum(1 for row in station_results if row.get("status") == "failed"),
        "not_run_stations": sum(1 for row in station_results if row.get("status") == "not_run"),
        "total_input_rows": total_input_rows,
        "total_output_rows": total_output_rows,
        "row_parity": total_input_rows == total_output_rows,
        "total_warnings": sum(warnings_by_station.values()),
        "stations_with_warnings": sum(1 for count in warnings_by_station.values() if count > 0),
        "parse_error_rows": parse_error_rows,
        "strict_token_rejection_total": int(token_summary.get("total_token_rejection_count") or 0),
        "strict_token_rejections_by_identifier": token_summary.get("token_rejections_by_identifier", {}),
        "strict_token_rejections_by_reason": token_summary.get("token_rejections_by_reason", {}),
        "strict_token_rejections_by_identifier_part": token_summary.get(
            "token_rejections_by_identifier_part", {}
        ),
        "strict_token_affected_station_count": int(token_summary.get("affected_station_count") or 0),
        "unsupported_identifiers": dict(sorted(unsupported_identifiers.items())),
        "skipped_identifiers": dict(sorted(skipped_identifiers.items())),
        "top_affected_stations_by_warning_count": [
            {"station_id": station_id, "warnings_count": count}
            for station_id, count in warnings_by_station.most_common(10)
        ],
        "top_affected_stations_by_strict_rejection_count": token_summary.get("top_affected_stations", []),
    }


def write_aggregate_quality_summary(artifact_root: Path) -> tuple[Path, Path]:
    payload = build_aggregate_quality_summary(artifact_root)
    json_path = artifact_root / "aggregate_quality_summary.json"
    markdown_path = artifact_root / "aggregate_quality_summary.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Aggregate Quality Summary",
        "",
        f"- Total stations: {payload['total_stations']}",
        f"- Successful stations: {payload['successful_stations']}",
        f"- Total input rows: {payload['total_input_rows']}",
        f"- Total output rows: {payload['total_output_rows']}",
        f"- Row parity: {payload['row_parity']}",
        f"- Total warnings: {payload['total_warnings']}",
        f"- Stations with warnings: {payload['stations_with_warnings']}",
        f"- Parse error rows: {payload['parse_error_rows']}",
        f"- Strict token rejections: {payload['strict_token_rejection_total']}",
        f"- Strict token affected stations: {payload['strict_token_affected_station_count']}",
        "",
        "## Strict Token Rejections By Identifier",
        "",
    ]
    for identifier, count in payload["strict_token_rejections_by_identifier"].items():
        lines.append(f"- {identifier}: {count}")
    lines.extend(["", "## Unsupported Or Skipped Identifiers", ""])
    lines.append(f"- Unsupported identifiers: {payload['unsupported_identifiers']}")
    lines.append(f"- Skipped identifiers: {payload['skipped_identifiers']}")
    lines.extend(["", "## Top Affected Stations By Warning Count", ""])
    for station in payload["top_affected_stations_by_warning_count"]:
        lines.append(f"- {station['station_id']}: {station['warnings_count']}")
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, markdown_path


def write_strict_token_rejection_explanation(artifact_root: Path) -> Path:
    summary = build_aggregate_quality_summary(artifact_root)
    path = artifact_root / "strict_token_rejection_explanation.md"
    top_identifiers = summary["strict_token_rejections_by_identifier"]
    lines = [
        "# Strict Token Rejection Explanation",
        "",
        "Strict token rejections are diagnostics emitted when an optional encoded NOAA section is present but one or more parsed tokens do not match the declared token width or shape expected by the current rule table.",
        "",
        "These diagnostics are non-fatal. The validation workflow records them so reviewers can see where real-world optional-section payloads diverge from the strict token expectations, while still preserving station-level processing and row-level lineage.",
        "",
        "## Observed Counts",
        "",
        f"- Total strict token rejections: {summary['strict_token_rejection_total']}",
        f"- Affected stations: {summary['strict_token_affected_station_count']}",
        f"- Total input rows: {summary['total_input_rows']}",
        f"- Total output rows: {summary['total_output_rows']}",
        f"- Row parity preserved: {summary['row_parity']}",
        f"- Parse error rows: {summary['parse_error_rows']}",
        "",
        "## Dominant Identifiers",
        "",
    ]
    for identifier, count in top_identifiers.items():
        lines.append(f"- {identifier}: {count}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A strict token rejection does not mean a station failed, a row was dropped, or the canonical row count changed. In this validation bundle, all 100 stations succeeded and summed input rows equal summed output rows.",
            "",
            "Unsupported or malformed optional encoded sections are surfaced in per-station quality reports through fields such as `skipped_encoded_columns`, `unsupported_identifier_columns`, `malformed_identifier_columns`, and `token_rejection_examples`. The cleaner does not silently convert those diagnostics into a claim of decoded scientific correctness for the affected optional payloads.",
            "",
            "Reviewers should infer that the workflow observed optional-section irregularity and recorded it explicitly. Reviewers should not infer that the reported count represents row loss, station failure, or silent removal of observations.",
            "",
            "## Future Work",
            "",
            "- Review high-volume families such as CH1 and OD1 against NOAA documentation and representative raw examples.",
            "- Promote common optional-section divergences into documented rule-provenance decisions where appropriate.",
            "- Add aggregate field-completeness and nullification reports for the DOI artifact boundary.",
            "- Expand upstream-traceable fixtures for optional encoded families that dominate strict diagnostics.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def update_run_manifest(artifact_root: Path) -> Path:
    path = artifact_root / "run_manifest.json"
    payload = _read_json(path)
    payload["docker_image"] = payload.get("docker_image")
    payload["docker_image_id"] = payload.get("docker_image_id")
    payload["docker_image_digest"] = payload.get("docker_image_digest")
    payload["reproducibility_boundary"] = "archived-validation-inputs-to-canonical-outputs"
    payload["reproducibility_boundary_note"] = VALIDATION_BOUNDARY_STATEMENT
    payload["upstream_noaa_reconstruction_claimed"] = False
    payload["archived_input_format"] = "parquet"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def update_summary_markdown(artifact_root: Path) -> Path:
    path = artifact_root / "summary.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "The raw inputs are intended for DOI-backed archival before submission so the validation evidence can be inspected and rerun without relying on live NOAA availability.",
        VALIDATION_BOUNDARY_STATEMENT,
    )
    text = text.replace(
        "- Once DOI-backed archival is complete, reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.\n- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.",
        "- Reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.\n- Local rerun of this validation boundary requires the archived raw parquet input bundle.\n- " + VALIDATION_BOUNDARY_STATEMENT,
    )
    text = text.replace(
        "This artifact provides operational smoke validation for a stratified 100-station sample. It does not claim exhaustive validation of the full NOAA corpus. Semantic correctness is verified by tracked upstream-traceable fixtures, tests, and source-document-linked rule families. The selected raw inputs are archived with checksums so reviewers can inspect or rerun the workflow without depending on live NOAA availability once a DOI-backed archive exists.",
        "This artifact provides operational reproducibility evidence for a stratified 100-station sample. " + VALIDATION_BOUNDARY_STATEMENT,
    )
    for legacy_placeholder in LEGACY_PRIMARY_DOI_PLACEHOLDERS:
        text = text.replace(
            f"- DOI: {legacy_placeholder}\n- This bundle is intended for external archival before submission; until a DOI is inserted, the archive should be treated as planned.",
            "- Primary DOI: TODO_PRIMARY_DOI\n- The DOI placeholder must be replaced before final DOI freeze or JOSS submission.",
        )
    inventory_anchor = "- `archive_manifest_primary.json`"
    if "selected_station_metadata.csv" not in text:
        text = text.replace(
            inventory_anchor,
            "- `aggregate_quality_summary.json`\n- `aggregate_quality_summary.md`\n- `selected_station_metadata.csv`\n- `strict_token_rejection_explanation.md`\n" + inventory_anchor,
        )
    path.write_text(text, encoding="utf-8")
    return path


def recompute_checksums_and_archive_manifest(artifact_root: Path) -> Path:
    checksums_primary_path = artifact_root / "checksums_primary.txt"
    checksums_domains_path = artifact_root / "checksums_domains.txt"
    archive_manifest_primary_path = artifact_root / "archive_manifest_primary.json"
    archive_manifest_domains_path = artifact_root / "archive_manifest_domains.json"

    build_id = _artifact_build_id(artifact_root)

    primary_entries = [
        "raw_inputs",
        "canonical_cleaned",
        "quality_reports",
        "station_results.csv",
        "station_selection_manifest.csv",
        "selected_station_metadata.csv",
        "run_manifest.json",
        "archive_manifest_primary.json",
        "checksums_primary.txt",
        "summary.md",
        "aggregate_quality_summary.json",
        "aggregate_quality_summary.md",
        "strict_parse_summary_report.json",
        "strict_parse_summary_report.md",
        "strict_token_rejection_explanation.md",
    ]
    domain_entries = ["domains", "archive_manifest_domains.json", "checksums_domains.txt"]

    def existing_paths(entries: list[str]) -> list[Path]:
        paths: list[Path] = []
        for entry in entries:
            path = artifact_root / entry
            if path.is_file():
                paths.append(path)
            elif path.is_dir():
                paths.extend(sorted(item for item in path.rglob("*") if item.is_file()))
        return sorted(paths)

    def write_checksums(path: Path, files: list[Path]) -> None:
        lines = [
            f"{_sha256(file_path)}  {file_path.relative_to(artifact_root).as_posix()}"
            for file_path in files
            if file_path.resolve() != path.resolve()
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def directory_inventory(files: list[Path], archive_type: str) -> list[dict[str, Any]]:
        inventory = []
        directory_names = sorted(
            {path.relative_to(artifact_root).parts[0] for path in files if len(path.relative_to(artifact_root).parts) > 1}
        )
        for directory_name in directory_names:
            directory = artifact_root / directory_name
            directory_files = [path for path in files if path.is_relative_to(directory)]
            inventory.append(
                {
                    "archive_classification": archive_type,
                    "file_count": len(directory_files),
                    "path": directory_name,
                    "total_bytes": sum(path.stat().st_size for path in directory_files),
                }
            )
        return inventory

    for _ in range(5):
        primary_files = existing_paths(primary_entries)
        domain_files = existing_paths(domain_entries)
        primary_payload = {
            "archive_type": "primary",
            "artifact_name": "validation_100_station_primary",
            "artifact_root": str(artifact_root),
            "artifact_version": build_id,
            "build_id": build_id,
            "checksum_algorithm": "SHA256",
            "checksum_file": "checksums_primary.txt",
            "claim_scope": VALIDATION_BOUNDARY_STATEMENT,
            "directory_inventory": directory_inventory(primary_files, "primary"),
            "doi": "TODO_PRIMARY_DOI",
            "file_count": len(primary_files),
            "byte_count": sum(path.stat().st_size for path in primary_files),
            "generated_timestamp_utc": _now_utc_isoformat(),
            "git_sha": None,
            "git_tag": None,
            "manifest_file": "archive_manifest_primary.json",
            "top_level_files": sorted({path.relative_to(artifact_root).parts[0] for path in primary_files}),
            "total_bytes": sum(path.stat().st_size for path in primary_files),
            "total_files": len(primary_files),
        }
        domain_payload = {
            "archive_type": "supplementary_domains",
            "artifact_name": "validation_100_station_domains",
            "artifact_root": str(artifact_root),
            "artifact_version": build_id,
            "build_id": build_id,
            "checksum_algorithm": "SHA256",
            "checksum_file": "checksums_domains.txt",
            "claim_scope": DOMAINS_SUPPLEMENT_STATEMENT,
            "directory_inventory": directory_inventory(domain_files, "supplementary_domains"),
            "doi": "TODO_DOMAINS_DOI",
            "file_count": len(domain_files),
            "byte_count": sum(path.stat().st_size for path in domain_files),
            "generated_timestamp_utc": _now_utc_isoformat(),
            "git_sha": None,
            "git_tag": None,
            "manifest_file": "archive_manifest_domains.json",
            "top_level_files": sorted({path.relative_to(artifact_root).parts[0] for path in domain_files}),
            "total_bytes": sum(path.stat().st_size for path in domain_files),
            "total_files": len(domain_files),
        }
        archive_manifest_primary_path.write_text(
            json.dumps(primary_payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        archive_manifest_domains_path.write_text(
            json.dumps(domain_payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        write_checksums(checksums_primary_path, existing_paths(primary_entries))
        write_checksums(checksums_domains_path, existing_paths(["domains"]))

    # Final refresh includes the settled manifest/checksum file sizes.
    primary_files = existing_paths(primary_entries)
    domain_files = existing_paths(domain_entries)
    primary_payload["directory_inventory"] = directory_inventory(primary_files, "primary")
    primary_payload["file_count"] = primary_payload["total_files"] = len(primary_files)
    primary_payload["byte_count"] = primary_payload["total_bytes"] = sum(path.stat().st_size for path in primary_files)
    primary_payload["top_level_files"] = sorted({path.relative_to(artifact_root).parts[0] for path in primary_files})
    domain_payload["directory_inventory"] = directory_inventory(domain_files, "supplementary_domains")
    domain_payload["file_count"] = domain_payload["total_files"] = len(domain_files)
    domain_payload["byte_count"] = domain_payload["total_bytes"] = sum(path.stat().st_size for path in domain_files)
    domain_payload["top_level_files"] = sorted({path.relative_to(artifact_root).parts[0] for path in domain_files})
    archive_manifest_primary_path.write_text(
        json.dumps(primary_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    archive_manifest_domains_path.write_text(
        json.dumps(domain_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_checksums(checksums_primary_path, existing_paths(primary_entries))
    write_checksums(checksums_domains_path, existing_paths(["domains"]))
    return archive_manifest_primary_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify a NOAA-Spec 100-station validation artifact.")
    parser.add_argument("artifact_path", type=Path)
    parser.add_argument(
        "--skip-hashes",
        action="store_true",
        help="Run structural checks without hashing every file.",
    )
    parser.add_argument(
        "--verify-domains",
        action="store_true",
        help="Verify a supplementary domains archive instead of the primary archive.",
    )
    parser.add_argument(
        "--verify-all",
        action="store_true",
        help="Verify primary and supplementary domains contents in one combined build directory.",
    )
    args = parser.parse_args(argv)

    if args.verify_domains and args.verify_all:
        parser.error("--verify-domains and --verify-all are mutually exclusive")

    failures = verify_artifact(
        args.artifact_path,
        verify_hashes=not args.skip_hashes,
        verify_domains=args.verify_domains,
        verify_all=args.verify_all,
    )
    if failures:
        print("FAIL: validation artifact verification failed")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: validation artifact verification succeeded")
    print(f"Artifact directory: {args.artifact_path}")
    if (args.artifact_path / "domains").exists() and not (args.verify_domains or args.verify_all):
        print("Supplementary domains present; use --verify-all to validate them with the primary archive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
