"""Operational validation bundle workflow built on the existing deterministic cleaner."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any

import pandas as pd

from . import __version__
from .cleaning import clean_noaa_dataframe
from .deterministic_io import write_deterministic_csv
from .projections import project_domains

DEFAULT_VALIDATION_COUNT = 100
DEFAULT_VALIDATION_SEED = 20260430
STATION_CHUNKING_ROW_COUNT_THRESHOLD = 250_000
STATION_CHUNK_ROW_COUNT = 250_000
STATION_CHUNKING_THRESHOLD_ENV = "NOAA_STATION_CHUNKING_ROW_COUNT_THRESHOLD"
STATION_CHUNK_ROW_COUNT_ENV = "NOAA_STATION_CHUNK_ROW_COUNT"
DOCKER_IMAGE_ENV = "NOAA_SPEC_DOCKER_IMAGE"
DOCKER_IMAGE_ID_ENV = "NOAA_SPEC_DOCKER_IMAGE_ID"
DOCKER_IMAGE_DIGEST_ENV = "NOAA_SPEC_DOCKER_IMAGE_DIGEST"
PRIMARY_DOI_PLACEHOLDER = "TODO_PRIMARY_DOI"
DOMAINS_DOI_PLACEHOLDER = "TODO_DOMAINS_DOI"
REPRODUCIBILITY_BOUNDARY_ID = "archived-validation-inputs-to-canonical-outputs"
REPRODUCIBILITY_BOUNDARY_NOTE = (
    "This validation artifact supports deterministic reproducibility from "
    "archived validation inputs to archived outputs. Reconstruction from upstream "
    "NOAA archives is not claimed because upstream NOAA source URLs and checksums "
    "are not preserved within this artifact.\n\n"
    "The primary DOI archive contains the canonical reproducibility boundary:\n\n"
    "archived inputs → deterministic NOAA-Spec processing → canonical cleaned outputs\n\n"
    "Domain outputs are convenience projections intended to improve interpretability "
    "for downstream workflows. They are derived from canonical cleaned outputs and "
    "are not required to reproduce NOAA-Spec's core deterministic cleaning behavior.\n\n"
    "Domain outputs are archived separately as supplementary artifacts and are "
    "outside the primary reproducibility claim."
)
SUMMARY_OPERATIONAL_LANGUAGE = (
    "Small upstream-traceable fixtures verify semantic correctness. The "
    "100-station validation artifact is supplementary operational evidence that "
    "the same repository-controlled workflow runs successfully across a broader "
    "stratified sample."
)
SUMMARY_ARCHIVAL_LANGUAGE = (
    "This validation artifact supports deterministic reproducibility from "
    "archived validation inputs to archived outputs. Reconstruction from upstream "
    "NOAA archives is not claimed because upstream NOAA source URLs and checksums "
    "are not preserved within this artifact."
)
SUMMARY_NON_EXHAUSTIVE_LANGUAGE = (
    "This artifact does not prove correctness over the full NOAA corpus."
)
SUMMARY_SELECTION_LANGUAGE = (
    "The sample is deterministic and size-stratified, not manually selected for "
    "favorable outcomes."
)
STRICT_TOKEN_DIAGNOSTIC_LANGUAGE = (
    "Strict token-level validation rejections are observability signals. They identify "
    "optional-section payloads that did not match declared token-width expectations. "
    "They did not cause station-level failure or row loss in this validation run."
)
WORKER_RESULT_SCHEMA_VERSION = "validation-station-result-v1"


@dataclass(frozen=True)
class StationCandidate:
    station_id: str
    source_path: Path
    source_format: str
    file_size_bytes: int
    size_stratum: str | None
    selection_score: int


@dataclass(frozen=True)
class StationChunkPlan:
    chunk_index: int
    start_row: int
    end_row: int


def default_build_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def run_validation_workflow(
    *,
    source_root: Path,
    output_root: Path,
    count: int = DEFAULT_VALIDATION_COUNT,
    strategy: str = "size-stratified",
    seed: int = DEFAULT_VALIDATION_SEED,
    continue_on_error: bool = False,
    build_id: str | None = None,
    command: str | None = None,
    selected_by: str = "noaa-spec dev build-validation-bundle",
    emit_domains: bool = False,
) -> dict[str, Any]:
    if count <= 0:
        raise ValueError("count must be greater than zero")
    if strategy != "size-stratified":
        raise ValueError(f"Unsupported sampling strategy: {strategy}")

    source_root = source_root.resolve()
    if not source_root.exists():
        raise FileNotFoundError(f"Source root does not exist: {source_root}")

    resolved_build_id = build_id or default_build_id()
    output_root = output_root.resolve()
    raw_inputs_dir = output_root / "raw_inputs"
    canonical_dir = output_root / "canonical_cleaned"
    quality_dir = output_root / "quality_reports"
    domains_dir = output_root / "domains"
    for path in (output_root, raw_inputs_dir, canonical_dir, quality_dir):
        path.mkdir(parents=True, exist_ok=True)
    if emit_domains:
        domains_dir.mkdir(parents=True, exist_ok=True)

    command_text = command or _default_command(
        source_root=source_root,
        output_root=output_root,
        count=count,
        strategy=strategy,
        seed=seed,
        continue_on_error=continue_on_error,
        build_id=resolved_build_id,
        emit_domains=emit_domains,
        command_name=(
            selected_by.removeprefix("noaa-spec ").strip()
            if selected_by.startswith("noaa-spec ")
            else selected_by
        ),
    )

    scan_records = _scan_station_candidates(source_root=source_root, seed=seed)
    selected_candidates, selection_rows = _select_candidates(
        scan_records=scan_records,
        source_root=source_root,
        count=count,
        strategy=strategy,
        seed=seed,
        selected_by=selected_by,
    )
    copied_entries = _copy_selected_raw_inputs(
        selected_candidates=selected_candidates,
        raw_inputs_dir=raw_inputs_dir,
        source_root=source_root,
    )
    selection_rows = _merge_copied_metadata_into_selection_rows(
        selection_rows=selection_rows,
        copied_entries=copied_entries,
    )

    git_metadata = _git_metadata()
    run_manifest = {
        "build_id": resolved_build_id,
        "repo_commit_sha": git_metadata["repo_commit_sha"],
        "git_dirty_status": git_metadata["git_dirty_status"],
        "git_tag": git_metadata["git_tag"],
        "timestamp_utc": _now_utc_isoformat(),
        "command": command_text,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "package_version": __version__,
        "dependency_lock_hash": _dependency_lock_hash(),
        "docker_image": _env_or_none(DOCKER_IMAGE_ENV),
        "docker_image_id": _env_or_none(DOCKER_IMAGE_ID_ENV),
        "docker_image_digest": _env_or_none(DOCKER_IMAGE_DIGEST_ENV),
        "source_root": str(source_root),
        "output_root": str(output_root),
        "station_count_requested": count,
        "station_count_selected": len(selected_candidates),
        "sampling_strategy": strategy,
        "seed": seed,
        "domain_outputs_requested": emit_domains,
        "reproducibility_boundary": REPRODUCIBILITY_BOUNDARY_ID,
        "reproducibility_boundary_note": REPRODUCIBILITY_BOUNDARY_NOTE,
        "upstream_noaa_reconstruction_claimed": False,
    }

    results_rows: list[dict[str, Any]] = []
    total_runtime = 0.0
    total_input_rows = 0
    total_output_rows = 0
    failure_seen = False
    failed_station_id: str | None = None

    remaining_candidates: list[StationCandidate] = []
    for index, candidate in enumerate(selected_candidates):
        copied_entry = copied_entries[(candidate.station_id, str(candidate.source_path))]
        result = _process_station_candidate(
            candidate=candidate,
            copied_entry=copied_entry,
            canonical_dir=canonical_dir,
            quality_dir=quality_dir,
            domains_dir=domains_dir if emit_domains else None,
            output_root=output_root,
        )
        results_rows.append(result)
        total_runtime += float(result["runtime_seconds"] or 0.0)
        total_input_rows += int(result["input_rows"] or 0)
        total_output_rows += int(result["output_rows"] or 0)
        _update_selection_row_with_result(selection_rows, result)

        if result["status"] != "success":
            failure_seen = True
            failed_station_id = candidate.station_id
            remaining_candidates = selected_candidates[index + 1 :]
            break

    if failure_seen and continue_on_error:
        for candidate in remaining_candidates:
            copied_entry = copied_entries[(candidate.station_id, str(candidate.source_path))]
            result = _process_station_candidate(
                candidate=candidate,
                copied_entry=copied_entry,
                canonical_dir=canonical_dir,
                quality_dir=quality_dir,
                domains_dir=domains_dir if emit_domains else None,
                output_root=output_root,
            )
            results_rows.append(result)
            total_runtime += float(result["runtime_seconds"] or 0.0)
            total_input_rows += int(result["input_rows"] or 0)
            total_output_rows += int(result["output_rows"] or 0)
            _update_selection_row_with_result(selection_rows, result)
    elif failure_seen:
        for candidate in remaining_candidates:
            copied_entry = copied_entries[(candidate.station_id, str(candidate.source_path))]
            result = _not_run_result(
                candidate=candidate,
                copied_entry=copied_entry,
                output_root=output_root,
                prior_station_id=failed_station_id or "",
            )
            results_rows.append(result)
            _update_selection_row_with_result(selection_rows, result)

    selection_manifest_path = output_root / "station_selection_manifest.csv"
    selection_frame = pd.DataFrame(selection_rows, columns=_station_selection_columns())
    write_deterministic_csv(
        selection_frame,
        selection_manifest_path,
        sort_by=("selection_status", "selection_rank", "station_id", "source_path"),
    )

    station_results_path = output_root / "station_results.csv"
    station_results_frame = pd.DataFrame(results_rows, columns=_station_results_columns())
    write_deterministic_csv(
        station_results_frame,
        station_results_path,
        sort_by=("status", "station_id"),
        float_format="%.6f",
    )

    run_manifest_path = output_root / "run_manifest.json"
    _write_json(run_manifest_path, run_manifest)

    summary_path = output_root / "summary.md"
    bundle_strict_summary = _aggregate_bundle_strict_parse_summary(results_rows)
    _write_summary(
        summary_path=summary_path,
        run_manifest=run_manifest,
        selection_rows=selection_rows,
        results_rows=results_rows,
        total_input_rows=total_input_rows,
        total_output_rows=total_output_rows,
        total_runtime=total_runtime,
        bundle_strict_summary=bundle_strict_summary,
    )
    _write_strict_parse_summary_report(
        output_root=output_root,
        run_manifest=run_manifest,
        bundle_strict_summary=bundle_strict_summary,
    )
    selected_station_metadata_path = _write_selected_station_metadata(
        output_root=output_root,
        selection_rows=selection_rows,
        results_rows=results_rows,
    )
    aggregate_summary = _write_aggregate_quality_summary(
        output_root=output_root,
        run_manifest=run_manifest,
        results_rows=results_rows,
        total_runtime=total_runtime,
    )
    _write_strict_token_rejection_explanation(
        output_root=output_root,
        aggregate_summary=aggregate_summary,
    )

    checksums_primary_path = output_root / "checksums_primary.txt"
    checksums_domains_path = output_root / "checksums_domains.txt"
    archive_manifest_primary_path = output_root / "archive_manifest_primary.json"
    archive_manifest_domains_path = output_root / "archive_manifest_domains.json"
    _finalize_archive_manifests_and_checksums(
        archive_manifest_primary_path=archive_manifest_primary_path,
        archive_manifest_domains_path=archive_manifest_domains_path,
        checksums_primary_path=checksums_primary_path,
        checksums_domains_path=checksums_domains_path,
        output_root=output_root,
        run_manifest=run_manifest,
    )

    return {
        "build_id": resolved_build_id,
        "output_root": output_root,
        "station_selection_manifest": selection_manifest_path,
        "run_manifest": run_manifest_path,
        "station_results": station_results_path,
        "selected_station_metadata": selected_station_metadata_path,
        "summary": summary_path,
        "checksums_primary": checksums_primary_path,
        "checksums_domains": checksums_domains_path,
        "archive_manifest_primary": archive_manifest_primary_path,
        "archive_manifest_domains": archive_manifest_domains_path,
        "selected_station_count": len(selected_candidates),
        "failure_count": sum(1 for row in results_rows if row["status"] != "success"),
        "failed": failure_seen,
    }


def _default_command(
    *,
    source_root: Path,
    output_root: Path,
    count: int,
    strategy: str,
    seed: int,
    continue_on_error: bool,
    build_id: str,
    emit_domains: bool,
    command_name: str,
) -> str:
    parts = [
        "noaa-spec",
        *command_name.split(),
        "--input-root" if "validate-100-stations" in command_name else "--source-root",
        str(source_root),
        "--output-root",
        str(output_root),
        "--count",
        str(count),
        "--strategy",
        strategy,
        "--seed",
        str(seed),
        "--build-id",
        build_id,
    ]
    if continue_on_error:
        parts.append("--continue-on-error")
    if emit_domains:
        parts.append("--emit-domains")
    return shlex.join(parts)


def _scan_station_candidates(source_root: Path, seed: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    duplicate_winners: dict[str, str] = {}
    supported_candidates: list[StationCandidate] = []

    for path in sorted(item for item in source_root.rglob("*") if item.is_file()):
        source_format = _detect_source_format(path)
        station_id = _station_id_from_path(path)
        file_size_bytes = path.stat().st_size
        record: dict[str, Any] = {
            "station_id": station_id,
            "source_path": str(path.resolve()),
            "source_format": source_format or "unsupported",
            "file_size_bytes": file_size_bytes,
            "size_stratum": "",
            "selection_score": "",
            "selection_status": "scanned",
            "skip_reason": "",
            "source_url": _infer_source_url(station_id=station_id, source_path=path),
        }
        if source_format is None:
            record["selection_status"] = "skipped_invalid"
            record["skip_reason"] = "unsupported_source_format"
            records.append(record)
            continue

        score = _selection_score(seed=seed, station_id=station_id, source_path=path)
        record["selection_score"] = score
        records.append(record)
        supported_candidates.append(
            StationCandidate(
                station_id=station_id,
                source_path=path.resolve(),
                source_format=source_format,
                file_size_bytes=file_size_bytes,
                size_stratum=None,
                selection_score=score,
            )
        )

    supported_candidates = sorted(
        supported_candidates,
        key=lambda candidate: (
            candidate.station_id,
            candidate.source_path.as_posix(),
            candidate.selection_score,
        ),
    )

    deduped_candidates: list[StationCandidate] = []
    for candidate in supported_candidates:
        existing_path = duplicate_winners.get(candidate.station_id)
        if existing_path is None:
            duplicate_winners[candidate.station_id] = str(candidate.source_path)
            deduped_candidates.append(candidate)
            continue
        for record in records:
            if (
                record["station_id"] == candidate.station_id
                and record["source_path"] == str(candidate.source_path)
            ):
                record["selection_status"] = "skipped_invalid"
                record["skip_reason"] = "duplicate_station_id"
                break

    if deduped_candidates:
        strata = _assign_size_strata(deduped_candidates)
        by_key = {
            (candidate.station_id, str(candidate.source_path)): candidate.size_stratum
            for candidate in strata
        }
        for record in records:
            key = (record["station_id"], record["source_path"])
            if key in by_key and record["selection_status"] == "scanned":
                record["size_stratum"] = by_key[key] or ""

    return records


def _select_candidates(
    *,
    scan_records: list[dict[str, Any]],
    source_root: Path,
    count: int,
    strategy: str,
    seed: int,
    selected_by: str,
) -> tuple[list[StationCandidate], list[dict[str, Any]]]:
    viable_records = [
        record
        for record in scan_records
        if record["selection_status"] == "scanned" and record["size_stratum"]
    ]
    if len(viable_records) < count:
        raise ValueError(
            f"Found only {len(viable_records)} viable station files under {source_root}; "
            f"{count} are required."
        )

    viable_candidates = [
        StationCandidate(
            station_id=str(record["station_id"]),
            source_path=Path(str(record["source_path"])),
            source_format=str(record["source_format"]),
            file_size_bytes=int(record["file_size_bytes"]),
            size_stratum=str(record["size_stratum"]),
            selection_score=int(record["selection_score"]),
        )
        for record in viable_records
    ]
    selected_candidates = _select_size_stratified_candidates(
        viable_candidates=viable_candidates,
        count=count,
    )
    selected_keys = {
        (candidate.station_id, str(candidate.source_path)): rank
        for rank, candidate in enumerate(selected_candidates, start=1)
    }

    selection_rows: list[dict[str, Any]] = []
    for record in scan_records:
        station_id = str(record["station_id"])
        source_path = str(record["source_path"])
        key = (station_id, source_path)
        is_selected = key in selected_keys
        selection_status = (
            "selected"
            if is_selected
            else str(record["selection_status"]).replace("scanned", "skipped_unselected")
        )
        selection_reason = ""
        if is_selected and record["size_stratum"]:
            selection_reason = f"size_stratified_quartile_{record['size_stratum']}"
        elif selection_status == "skipped_unselected":
            selection_reason = "not_selected_after_size_stratified_sampling"
        elif selection_status == "skipped_invalid":
            selection_reason = str(record["skip_reason"] or "invalid_candidate")

        selection_rows.append(
            {
                "station_id": station_id,
                "source_path": source_path,
                "archived_raw_input_path": "",
                "source_format": str(record["source_format"]),
                "file_size_bytes": int(record["file_size_bytes"]),
                "row_count": "",
                "size_stratum": str(record["size_stratum"] or ""),
                "selection_rank": selected_keys.get(key, ""),
                "selection_reason": selection_reason,
                "selected_by": selected_by,
                "seed": seed,
                "raw_sha256": "",
                "input_root": str(source_root),
                "source_root": str(source_root),
                "copied_utc": "",
                "source_url": str(record["source_url"] or ""),
                "original_source_filename": Path(source_path).name,
                "selection_status": selection_status,
                "skip_reason": "" if is_selected else str(record["skip_reason"]),
                "processing_status": "pending" if is_selected else "",
            }
        )

    return selected_candidates, selection_rows


def _assign_size_strata(candidates: list[StationCandidate]) -> list[StationCandidate]:
    ordered = sorted(
        candidates,
        key=lambda candidate: (
            candidate.file_size_bytes,
            candidate.station_id,
            candidate.source_path.as_posix(),
        ),
    )
    labels = _quartile_labels(len(ordered))
    assigned: list[StationCandidate] = []
    for candidate, quartile in zip(ordered, labels, strict=True):
        assigned.append(
            StationCandidate(
                station_id=candidate.station_id,
                source_path=candidate.source_path,
                source_format=candidate.source_format,
                file_size_bytes=candidate.file_size_bytes,
                size_stratum=f"q{quartile}",
                selection_score=candidate.selection_score,
            )
        )
    return assigned


def _quartile_labels(size: int) -> list[int]:
    return [((index * 4) // size) + 1 for index in range(size)]


def _select_size_stratified_candidates(
    *,
    viable_candidates: list[StationCandidate],
    count: int,
) -> list[StationCandidate]:
    by_stratum: dict[str, list[StationCandidate]] = {label: [] for label in ("q1", "q2", "q3", "q4")}
    for candidate in viable_candidates:
        if candidate.size_stratum is not None:
            by_stratum[candidate.size_stratum].append(candidate)

    for label in by_stratum:
        by_stratum[label] = sorted(
            by_stratum[label],
            key=lambda candidate: (
                candidate.selection_score,
                candidate.file_size_bytes,
                candidate.station_id,
                candidate.source_path.as_posix(),
            ),
        )

    base = count // 4
    remainder = count % 4
    targets = {
        label: base + (1 if index < remainder else 0)
        for index, label in enumerate(("q1", "q2", "q3", "q4"))
    }

    selected: list[StationCandidate] = []
    leftovers: list[StationCandidate] = []
    for label in ("q1", "q2", "q3", "q4"):
        candidates = by_stratum[label]
        take = min(len(candidates), targets[label])
        selected.extend(candidates[:take])
        leftovers.extend(candidates[take:])

    if len(selected) < count:
        leftovers = sorted(
            leftovers,
            key=lambda candidate: (
                candidate.selection_score,
                candidate.size_stratum,
                candidate.file_size_bytes,
                candidate.station_id,
                candidate.source_path.as_posix(),
            ),
        )
        selected.extend(leftovers[: count - len(selected)])

    return sorted(
        selected,
        key=lambda candidate: (
            candidate.size_stratum,
            candidate.selection_score,
            candidate.station_id,
            candidate.source_path.as_posix(),
        ),
    )


def _copy_selected_raw_inputs(
    *,
    selected_candidates: list[StationCandidate],
    raw_inputs_dir: Path,
    source_root: Path,
) -> dict[tuple[str, str], dict[str, Any]]:
    copied_entries: dict[tuple[str, str], dict[str, Any]] = {}
    for candidate in selected_candidates:
        copied_utc = _now_utc_isoformat()
        archived_name = f"{candidate.station_id}{''.join(candidate.source_path.suffixes)}"
        archived_path = raw_inputs_dir / archived_name
        shutil.copy2(candidate.source_path, archived_path)
        raw_sha256 = _sha256_file(archived_path)
        copied_entries[(candidate.station_id, str(candidate.source_path))] = {
            "station_id": candidate.station_id,
            "source_path": str(candidate.source_path),
            "source_format": candidate.source_format,
            "source_file_name": candidate.source_path.name,
            "archived_raw_input_path": archived_path.relative_to(raw_inputs_dir.parent).as_posix(),
            "archived_raw_path_abs": archived_path,
            "raw_sha256": raw_sha256,
            "copied_utc": copied_utc,
            "source_root": str(source_root),
            "file_size_bytes": archived_path.stat().st_size,
            "selection_strategy": "size-stratified",
            "source_url": _infer_source_url(
                station_id=candidate.station_id,
                source_path=candidate.source_path,
            )
            or "",
        }
    return copied_entries


def _merge_copied_metadata_into_selection_rows(
    *,
    selection_rows: list[dict[str, Any]],
    copied_entries: dict[tuple[str, str], dict[str, Any]],
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    for row in selection_rows:
        updated = dict(row)
        key = (str(row["station_id"]), str(row["source_path"]))
        copied = copied_entries.get(key)
        if copied is not None:
            updated["archived_raw_input_path"] = copied["archived_raw_input_path"]
            updated["raw_sha256"] = copied["raw_sha256"]
            updated["copied_utc"] = copied["copied_utc"]
            if copied["source_url"]:
                updated["source_url"] = copied["source_url"]
        merged.append(updated)
    return merged


def _bundle_example_sort_key(example: dict[str, Any]) -> tuple[str, str, str, str, str]:
    return (
        str(example.get("station_id") or ""),
        str(example.get("identifier") or ""),
        str(example.get("part_index") or ""),
        str(example.get("reason") or ""),
        str(example.get("row_index") or ""),
    )


def _aggregate_bundle_strict_parse_summary(results_rows: list[dict[str, Any]]) -> dict[str, Any]:
    token_rejections_by_identifier: Counter[str] = Counter()
    token_rejections_by_identifier_part: Counter[str] = Counter()
    token_rejections_by_reason: Counter[str] = Counter()
    token_rejections_by_station: Counter[str] = Counter()
    affected_stations: set[str] = set()
    token_rejection_examples: list[dict[str, Any]] = []
    total_token_rejection_count = 0

    for row in results_rows:
        if row.get("status") != "success":
            continue
        strict_summary = row.get("strict_parse_summary") or {}
        station_id = str(row.get("station_id") or "")
        token_count = int(strict_summary.get("token_rejection_count", 0) or 0)
        if token_count > 0:
            affected_stations.add(station_id)
            token_rejections_by_station[station_id] += token_count
        total_token_rejection_count += token_count
        token_rejections_by_identifier.update(strict_summary.get("token_rejections_by_identifier", {}))
        token_rejections_by_identifier_part.update(
            strict_summary.get("token_rejections_by_identifier_part", {})
        )
        token_rejections_by_reason.update(strict_summary.get("token_rejections_by_reason", {}))
        for example in strict_summary.get("token_rejection_examples", ()):
            normalized = dict(example)
            if not normalized.get("station_id"):
                normalized["station_id"] = station_id
            token_rejection_examples.append(normalized)

    top_affected_stations = [
        {"station_id": station_id, "token_rejection_count": count}
        for station_id, count in sorted(
            token_rejections_by_station.items(),
            key=lambda item: (-item[1], item[0]),
        )[:10]
    ]
    capped_examples = sorted(token_rejection_examples, key=_bundle_example_sort_key)[:10]
    return {
        "token_validation_rejections": {
            "total_token_rejection_count": total_token_rejection_count,
            "affected_station_count": len(affected_stations),
            "token_rejections_by_identifier": dict(
                sorted(token_rejections_by_identifier.items())
            ),
            "token_rejections_by_identifier_part": dict(
                sorted(token_rejections_by_identifier_part.items())
            ),
            "token_rejections_by_reason": dict(sorted(token_rejections_by_reason.items())),
            "top_affected_stations": top_affected_stations,
            "token_rejection_examples": capped_examples,
            "diagnostic_note": STRICT_TOKEN_DIAGNOSTIC_LANGUAGE,
        }
    }


def _write_strict_parse_summary_report(
    *,
    output_root: Path,
    run_manifest: dict[str, Any],
    bundle_strict_summary: dict[str, Any],
) -> None:
    report = bundle_strict_summary["token_validation_rejections"]
    json_path = output_root / "strict_parse_summary_report.json"
    markdown_path = output_root / "strict_parse_summary_report.md"

    payload = {
        "artifact_id": "strict_parse_summary_report",
        "schema_version": "1.0.0",
        "build_id": run_manifest["build_id"],
        "created_utc": _now_utc_isoformat(),
        **bundle_strict_summary,
    }
    _write_json(json_path, payload)

    def _render_count_lines(mapping: dict[str, Any]) -> list[str]:
        if not mapping:
            return ["- None observed."]
        return [f"- {key}: {mapping[key]}" for key in sorted(mapping)]

    lines = [
        "# Strict Parse Summary Report",
        "",
        "## Token validation rejections",
        (
            "Strict token-level validation detected width/shape mismatches in optional "
            "section payloads. These diagnostics did not cause station-level failures "
            "or row loss."
        ),
        "",
        f"- Total token rejections: {report['total_token_rejection_count']}",
        f"- Affected stations: {report['affected_station_count']}",
        "",
        "### By identifier",
        *_render_count_lines(report["token_rejections_by_identifier"]),
        "",
        "### By identifier and part",
        *_render_count_lines(report["token_rejections_by_identifier_part"]),
        "",
        "### By reason",
        *_render_count_lines(report["token_rejections_by_reason"]),
        "",
        "### Top affected stations",
    ]
    if report["top_affected_stations"]:
        lines.extend(
            [
                f"- {entry['station_id']}: {entry['token_rejection_count']}"
                for entry in report["top_affected_stations"]
            ]
        )
    else:
        lines.append("- None observed.")

    lines.extend(["", "### Examples"])
    if report["token_rejection_examples"]:
        for example in report["token_rejection_examples"]:
            lines.append(
                "- "
                + ", ".join(
                    [
                        f"station_id={example.get('station_id')}",
                        f"identifier={example.get('identifier')}",
                        f"part_index={example.get('part_index')}",
                        f"reason={example.get('reason')}",
                        f"actual_width={example.get('actual_width')}",
                        f"expected_width={example.get('expected_width')}",
                        f"row_index={example.get('row_index')}",
                        f"token_sample={example.get('token_sample')}",
                    ]
                )
            )
    else:
        lines.append("- None observed.")

    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _selected_station_metadata_columns() -> list[str]:
    return [
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


def _write_selected_station_metadata(
    *,
    output_root: Path,
    selection_rows: list[dict[str, Any]],
    results_rows: list[dict[str, Any]],
) -> Path:
    selected_by_station = {
        str(row["station_id"]): row
        for row in selection_rows
        if row.get("selection_status") == "selected"
    }
    metadata_rows: list[dict[str, Any]] = []
    for result in sorted(results_rows, key=lambda row: str(row.get("station_id") or "")):
        station_id = str(result.get("station_id") or "")
        selection = selected_by_station.get(station_id, {})
        raw_path_value = str(result.get("archived_raw_input_path") or "")
        raw_path = output_root / raw_path_value if raw_path_value else None
        raw_metadata = (
            _read_archived_station_metadata(raw_path)
            if raw_path is not None and raw_path.exists()
            else {}
        )
        metadata_rows.append(
            {
                "station_id": station_id,
                "station_name": raw_metadata.get("station_name", ""),
                "latitude": raw_metadata.get("latitude", ""),
                "longitude": raw_metadata.get("longitude", ""),
                "min_date": raw_metadata.get("min_date", ""),
                "max_date": raw_metadata.get("max_date", ""),
                "input_rows": result.get("input_rows", ""),
                "output_rows": result.get("output_rows", ""),
                "raw_input_size_bytes": selection.get("file_size_bytes", ""),
                "size_stratum": selection.get("size_stratum", ""),
                "raw_input_sha256": result.get("raw_sha256", "") or selection.get("raw_sha256", ""),
                "canonical_output_sha256": result.get("canonical_output_sha256", ""),
            }
        )

    path = output_root / "selected_station_metadata.csv"
    write_deterministic_csv(
        pd.DataFrame(metadata_rows, columns=_selected_station_metadata_columns()),
        path,
        sort_by=("station_id",),
    )
    return path


def _read_archived_station_metadata(path: Path) -> dict[str, str]:
    try:
        if path.suffix.lower() == ".parquet":
            columns = ["NAME", "LATITUDE", "LONGITUDE", "DATE"]
            frame = pd.read_parquet(path, columns=columns)
        else:
            frame = pd.read_csv(
                path,
                dtype=str,
                compression="infer",
                usecols=lambda column: column in {"NAME", "LATITUDE", "LONGITUDE", "DATE"},
            )
    except Exception:
        return {}

    if frame.empty:
        return {}
    first = frame.iloc[0]
    metadata: dict[str, str] = {}
    for source_column, output_key in (
        ("NAME", "station_name"),
        ("LATITUDE", "latitude"),
        ("LONGITUDE", "longitude"),
    ):
        if source_column not in frame.columns:
            metadata[output_key] = ""
            continue
        value = first.get(source_column)
        metadata[output_key] = "" if pd.isna(value) else str(value)
    if "DATE" in frame.columns and not frame["DATE"].empty:
        metadata["min_date"] = "" if frame["DATE"].isna().all() else str(frame["DATE"].min())
        metadata["max_date"] = "" if frame["DATE"].isna().all() else str(frame["DATE"].max())
    else:
        metadata["min_date"] = ""
        metadata["max_date"] = ""
    return metadata


def _build_aggregate_quality_summary(
    *,
    output_root: Path,
    run_manifest: dict[str, Any],
    results_rows: list[dict[str, Any]],
    total_runtime: float,
) -> dict[str, Any]:
    strict_summary = _read_json(output_root / "strict_parse_summary_report.json")
    token_summary = strict_summary.get("token_validation_rejections", {})
    warnings_by_station = Counter(
        {
            str(row.get("station_id") or ""): int(row.get("warnings_count") or 0)
            for row in results_rows
        }
    )
    status_counts = Counter(str(row.get("status") or "") for row in results_rows)
    unsupported_identifiers: Counter[str] = Counter()
    skipped_identifiers: Counter[str] = Counter()
    parse_error_rows = 0
    runtime_values = [
        float(row.get("runtime_seconds") or 0.0)
        for row in results_rows
        if str(row.get("runtime_seconds") or "") != ""
    ]

    for report_path in sorted((output_root / "quality_reports").glob("*_quality_report.json")):
        report = _read_json(report_path)
        parse_error_rows += int(report.get("parse_error_rows") or 0)
        strict = report.get("strict_parse_summary", {})
        unsupported_identifiers.update(str(value) for value in strict.get("unsupported_identifier_columns", ()))
        skipped_identifiers.update(str(value) for value in strict.get("skipped_encoded_columns", ()))

    total_input_rows = sum(int(row.get("input_rows") or 0) for row in results_rows)
    total_output_rows = sum(int(row.get("output_rows") or 0) for row in results_rows)
    return {
        "artifact_id": "aggregate_quality_summary",
        "schema_version": "1.0.0",
        "build_id": run_manifest["build_id"],
        "created_utc": _now_utc_isoformat(),
        "total_stations": len(results_rows),
        "successful_stations": status_counts.get("success", 0),
        "failed_stations": status_counts.get("failed", 0),
        "not_run_stations": status_counts.get("not_run", 0),
        "station_status_counts": dict(sorted(status_counts.items())),
        "total_input_rows": total_input_rows,
        "total_output_rows": total_output_rows,
        "row_parity": total_input_rows == total_output_rows,
        "parse_error_rows": parse_error_rows,
        "total_warnings": sum(warnings_by_station.values()),
        "stations_with_warnings": sum(1 for count in warnings_by_station.values() if count > 0),
        "strict_token_rejection_total": int(token_summary.get("total_token_rejection_count") or 0),
        "strict_token_affected_station_count": int(token_summary.get("affected_station_count") or 0),
        "strict_token_rejections_by_identifier": token_summary.get("token_rejections_by_identifier", {}),
        "strict_token_rejections_by_reason": token_summary.get("token_rejections_by_reason", {}),
        "strict_token_rejections_by_identifier_part": token_summary.get(
            "token_rejections_by_identifier_part", {}
        ),
        "unsupported_identifiers": dict(sorted(unsupported_identifiers.items())),
        "skipped_identifiers": dict(sorted(skipped_identifiers.items())),
        "top_affected_stations_by_warning_count": [
            {"station_id": station_id, "warnings_count": count}
            for station_id, count in sorted(
                warnings_by_station.items(),
                key=lambda item: (-item[1], item[0]),
            )[:10]
        ],
        "top_affected_stations_by_strict_rejection_count": token_summary.get(
            "top_affected_stations", []
        ),
        "runtime_summary_seconds": {
            "total": total_runtime,
            "min": min(runtime_values) if runtime_values else 0.0,
            "max": max(runtime_values) if runtime_values else 0.0,
            "mean": (sum(runtime_values) / len(runtime_values)) if runtime_values else 0.0,
        },
    }


def _write_aggregate_quality_summary(
    *,
    output_root: Path,
    run_manifest: dict[str, Any],
    results_rows: list[dict[str, Any]],
    total_runtime: float,
) -> dict[str, Any]:
    payload = _build_aggregate_quality_summary(
        output_root=output_root,
        run_manifest=run_manifest,
        results_rows=results_rows,
        total_runtime=total_runtime,
    )
    _write_json(output_root / "aggregate_quality_summary.json", payload)

    lines = [
        "# Aggregate Quality Summary",
        "",
        f"- Total stations: {payload['total_stations']}",
        f"- Successful stations: {payload['successful_stations']}",
        f"- Failed stations: {payload['failed_stations']}",
        f"- Not-run stations: {payload['not_run_stations']}",
        f"- Total input rows: {payload['total_input_rows']}",
        f"- Total output rows: {payload['total_output_rows']}",
        f"- Row parity: {payload['row_parity']}",
        f"- Parse error rows: {payload['parse_error_rows']}",
        f"- Total warnings: {payload['total_warnings']}",
        f"- Stations with warnings: {payload['stations_with_warnings']}",
        f"- Strict token rejections: {payload['strict_token_rejection_total']}",
        f"- Strict token affected stations: {payload['strict_token_affected_station_count']}",
        f"- Total runtime seconds: {payload['runtime_summary_seconds']['total']:.6f}",
        "",
        "## Strict Token Rejections By Identifier",
        "",
        *_count_lines(payload["strict_token_rejections_by_identifier"]),
        "",
        "## Unsupported Identifiers",
        "",
        *_count_lines(payload["unsupported_identifiers"]),
        "",
        "## Skipped Identifiers",
        "",
        *_count_lines(payload["skipped_identifiers"]),
        "",
        "## Top Affected Stations By Warning Count",
        "",
    ]
    if payload["top_affected_stations_by_warning_count"]:
        lines.extend(
            f"- {entry['station_id']}: {entry['warnings_count']}"
            for entry in payload["top_affected_stations_by_warning_count"]
        )
    else:
        lines.append("- None observed.")
    (output_root / "aggregate_quality_summary.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    return payload


def _count_lines(mapping: dict[str, Any]) -> list[str]:
    if not mapping:
        return ["- None observed."]
    return [f"- {key}: {mapping[key]}" for key in sorted(mapping)]


def _write_strict_token_rejection_explanation(
    *,
    output_root: Path,
    aggregate_summary: dict[str, Any],
) -> Path:
    top_identifiers = aggregate_summary["strict_token_rejections_by_identifier"]
    lines = [
        "# Strict Token Rejection Explanation",
        "",
        "Strict token rejections are diagnostics emitted when an optional encoded NOAA section is present but one or more parsed tokens do not match the token width or shape expected by the current rule table.",
        "",
        "They are non-fatal observability signals. The validation workflow records them so reviewers can inspect real-world optional-section irregularity without converting those irregularities into row loss or silent claims of decoded scientific correctness.",
        "",
        "## Observed Counts",
        "",
        f"- Total strict token rejections: {aggregate_summary['strict_token_rejection_total']}",
        f"- Affected stations: {aggregate_summary['strict_token_affected_station_count']}",
        f"- Total input rows: {aggregate_summary['total_input_rows']}",
        f"- Total output rows: {aggregate_summary['total_output_rows']}",
        f"- Row parity preserved: {aggregate_summary['row_parity']}",
        f"- Parse error rows: {aggregate_summary['parse_error_rows']}",
        "",
        "## Dominant Identifiers",
        "",
        *_count_lines(top_identifiers),
        "",
        "## Interpretation",
        "",
        "A strict token rejection does not mean a station failed, a row was dropped, or the canonical row count changed. Row parity is reported separately in `station_results.csv` and `aggregate_quality_summary.json`.",
        "",
        "Unsupported, skipped, or malformed optional encoded sections are surfaced in per-station quality reports through fields such as `skipped_encoded_columns`, `unsupported_identifier_columns`, `malformed_identifier_columns`, and `token_rejection_examples`.",
        "",
        "These diagnostics do not imply upstream NOAA reconstruction. The reproducibility claim remains bounded to archived validation inputs and canonical outputs.",
        "",
        "## Future Work",
        "",
        "- Review high-volume optional encoded families against NOAA documentation and representative raw examples.",
        "- Promote common optional-section divergences into documented rule-provenance decisions where appropriate.",
        "- Add broader aggregate field-completeness and nullification reports for DOI-scale validation artifacts.",
        "- Expand upstream-traceable fixtures for optional encoded families that dominate strict diagnostics.",
        "",
    ]
    path = output_root / "strict_token_rejection_explanation.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _process_station_candidate(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    canonical_dir: Path,
    quality_dir: Path,
    domains_dir: Path | None,
    output_root: Path,
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="noaa-spec-validation-worker-") as tmpdir:
        result_path = Path(tmpdir) / f"{candidate.station_id}_result.json"
        command = _station_worker_command(
            candidate=candidate,
            copied_entry=copied_entry,
            canonical_dir=canonical_dir,
            quality_dir=quality_dir,
            domains_dir=domains_dir,
            output_root=output_root,
            result_path=result_path,
        )
        timed_out = False
        exit_code: int | None = None
        stdout = ""
        stderr = ""
        try:
            proc = subprocess.run(
                command,
                capture_output=True,
                text=True,
                env=_station_worker_env(),
                timeout=_station_worker_timeout_seconds(),
            )
            exit_code = int(proc.returncode)
            stdout = proc.stdout
            stderr = proc.stderr
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""

        worker_result = _load_station_worker_result(result_path)
        if (
            not timed_out
            and exit_code == 0
            and worker_result is not None
            and _station_result_outputs_are_valid(worker_result, output_root=output_root)
        ):
            return worker_result

        if worker_result is not None and worker_result.get("status") != "success":
            return worker_result

        return _failed_subprocess_result(
            candidate=candidate,
            copied_entry=copied_entry,
            timed_out=timed_out,
            exit_code=exit_code,
            stderr=stderr,
            stdout=stdout,
            worker_result=worker_result,
        )


def _process_station_candidate_in_worker(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    canonical_dir: Path,
    quality_dir: Path,
    domains_dir: Path | None,
    output_root: Path,
) -> dict[str, Any]:
    archived_raw_path = Path(copied_entry["archived_raw_path_abs"])
    row_count = _station_row_count(archived_raw_path, candidate.source_format)
    if row_count > _station_chunking_row_count_threshold():
        return _process_station_candidate_chunked(
            candidate=candidate,
            copied_entry=copied_entry,
            canonical_dir=canonical_dir,
            quality_dir=quality_dir,
            domains_dir=domains_dir,
            output_root=output_root,
            row_count=row_count,
        )
    return _process_station_candidate_whole_file(
        candidate=candidate,
        copied_entry=copied_entry,
        canonical_dir=canonical_dir,
        quality_dir=quality_dir,
        domains_dir=domains_dir,
        output_root=output_root,
    )


def _process_station_candidate_whole_file(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    canonical_dir: Path,
    quality_dir: Path,
    domains_dir: Path | None,
    output_root: Path,
) -> dict[str, Any]:
    start = time.perf_counter()
    archived_raw_path = Path(copied_entry["archived_raw_path_abs"])
    canonical_path = canonical_dir / f"{candidate.station_id}_cleaned.csv"
    quality_report_path = quality_dir / f"{candidate.station_id}_quality_report.json"

    try:
        raw = _read_station_data(archived_raw_path, candidate.source_format)
        input_rows = int(len(raw))
        cleaned = clean_noaa_dataframe(raw, keep_raw=False, strict_mode=True)
        output_rows = int(len(cleaned))
        write_deterministic_csv(
            cleaned,
            canonical_path,
            sort_by=("STATION", "DATE"),
            float_format="%.1f",
        )
        domain_output_paths = (
            _write_domain_outputs(
                cleaned=cleaned,
                station_id=candidate.station_id,
                domains_dir=domains_dir,
            )
            if domains_dir is not None
            else {}
        )
        strict_summary = cleaned.attrs.get("strict_parse_summary", {})
        parse_error_rows = (
            int(cleaned["__parse_error"].notna().sum())
            if "__parse_error" in cleaned.columns
            else 0
        )
        warnings_count = (
            parse_error_rows
            + int(strict_summary.get("skipped_encoded_column_count", 0))
            + int(strict_summary.get("token_rejection_count", 0))
        )
        _write_json(
            quality_report_path,
            {
                "station_id": candidate.station_id,
                "original_source_path": copied_entry["source_path"],
                "archived_raw_input_path": copied_entry["archived_raw_input_path"],
                "raw_sha256": copied_entry["raw_sha256"],
                "input_rows": input_rows,
                "output_rows": output_rows,
                "parse_error_rows": parse_error_rows,
                "strict_parse_summary": strict_summary,
                "rows_with_any_usable_metric": (
                    int(cleaned["row_has_any_usable_metric"].sum())
                    if "row_has_any_usable_metric" in cleaned.columns
                    else None
                ),
                "domain_output_paths": {
                    domain: _relative_to_root(path, output_root)
                    for domain, path in domain_output_paths.items()
                },
                "warnings_count": warnings_count,
            },
        )
        return {
            "station_id": candidate.station_id,
            "status": "success",
            "input_rows": input_rows,
            "output_rows": output_rows,
            "runtime_seconds": time.perf_counter() - start,
            "archived_raw_input_path": copied_entry["archived_raw_input_path"],
            "raw_sha256": copied_entry["raw_sha256"],
            "canonical_output_path": _relative_to_root(canonical_path, output_root),
            "canonical_output_sha256": _sha256_file(canonical_path),
            "quality_report_path": _relative_to_root(quality_report_path, output_root),
            "domain_outputs_generated": bool(domain_output_paths),
            "warnings_count": warnings_count,
            "strict_parse_summary": strict_summary,
            "error_type": "",
            "error_message": "",
        }
    except BaseException as exc:
        return {
            "station_id": candidate.station_id,
            "status": "failed",
            "input_rows": 0,
            "output_rows": 0,
            "runtime_seconds": time.perf_counter() - start,
            "archived_raw_input_path": copied_entry["archived_raw_input_path"],
            "raw_sha256": copied_entry["raw_sha256"],
            "canonical_output_path": "",
            "canonical_output_sha256": "",
            "quality_report_path": "",
            "domain_outputs_generated": False,
            "warnings_count": 0,
            "strict_parse_summary": {},
            "error_type": exc.__class__.__name__,
            "error_message": str(exc),
        }


def _station_worker_command(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    canonical_dir: Path,
    quality_dir: Path,
    domains_dir: Path | None,
    output_root: Path,
    result_path: Path,
) -> list[str]:
    return [
        sys.executable,
        "-m",
        "noaa_spec.validation",
        "_station-worker",
        "--station-id",
        candidate.station_id,
        "--source-path",
        str(candidate.source_path),
        "--source-format",
        candidate.source_format,
        "--file-size-bytes",
        str(candidate.file_size_bytes),
        "--size-stratum",
        candidate.size_stratum or "",
        "--selection-score",
        str(candidate.selection_score),
        "--archived-raw-path",
        str(copied_entry["archived_raw_path_abs"]),
        "--archived-raw-input-path",
        str(copied_entry["archived_raw_input_path"]),
        "--raw-sha256",
        str(copied_entry["raw_sha256"]),
        "--original-source-path",
        str(copied_entry["source_path"]),
        "--canonical-dir",
        str(canonical_dir),
        "--quality-dir",
        str(quality_dir),
        "--output-root",
        str(output_root),
        "--result-path",
        str(result_path),
        *([] if domains_dir is None else ["--domains-dir", str(domains_dir)]),
    ]


def _station_worker_env() -> dict[str, str]:
    env = os.environ.copy()
    src_root = Path(__file__).resolve().parents[1]
    existing = env.get("PYTHONPATH", "")
    pythonpath_parts = [str(src_root)]
    if existing:
        pythonpath_parts.append(existing)
    env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
    return env


def _station_worker_timeout_seconds() -> int | None:
    value = os.environ.get("NOAA_SPEC_VALIDATION_STATION_TIMEOUT_SECONDS", "").strip()
    if not value:
        return None
    try:
        timeout = int(value)
    except ValueError:
        return None
    return timeout if timeout > 0 else None


def _load_station_worker_result(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if payload.get("schema_version") != WORKER_RESULT_SCHEMA_VERSION:
        return None
    result = payload.get("result")
    return result if isinstance(result, dict) else None


def _station_result_outputs_are_valid(result: dict[str, Any], *, output_root: Path) -> bool:
    if result.get("status") != "success":
        return True
    required = [
        result.get("canonical_output_path"),
        result.get("quality_report_path"),
    ]
    if result.get("canonical_output_sha256"):
        canonical_path = output_root / str(result.get("canonical_output_path"))
        if not canonical_path.exists():
            return False
        if _sha256_file(canonical_path) != str(result["canonical_output_sha256"]):
            return False
    return all(bool(path) and (output_root / str(path)).exists() for path in required)


def _failed_subprocess_result(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    timed_out: bool,
    exit_code: int | None,
    stderr: str,
    stdout: str,
    worker_result: dict[str, Any] | None,
) -> dict[str, Any]:
    error_type = _subprocess_failure_type(exit_code=exit_code, timed_out=timed_out)
    if worker_result is not None and worker_result.get("status") == "success":
        error_type = "output_validation"
        error_message = (
            "station worker exited successfully but required outputs or checksums "
            "could not be validated"
        )
    else:
        error_message = _summarize_subprocess_error(
            stderr=stderr,
            stdout=stdout,
            timed_out=timed_out,
        )
    return {
        "station_id": candidate.station_id,
        "status": "failed",
        "input_rows": 0,
        "output_rows": 0,
        "runtime_seconds": 0.0,
        "archived_raw_input_path": copied_entry["archived_raw_input_path"],
        "raw_sha256": copied_entry["raw_sha256"],
        "canonical_output_path": "",
        "canonical_output_sha256": "",
        "quality_report_path": "",
        "domain_outputs_generated": False,
        "warnings_count": 0,
        "strict_parse_summary": {},
        "error_type": error_type,
        "error_message": error_message,
    }


def _subprocess_failure_type(*, exit_code: int | None, timed_out: bool) -> str:
    if timed_out:
        return "subprocess_timeout"
    if exit_code is None:
        return "subprocess_unknown"
    if exit_code < 0 or exit_code in {134, 136, 137, 139}:
        return "child_process_crash"
    if exit_code == 0:
        return "worker_result_missing"
    return "child_process_nonzero_exit"


def _summarize_subprocess_error(
    *,
    stderr: str,
    stdout: str,
    timed_out: bool,
) -> str:
    if timed_out:
        return "station worker timed out"
    text = stderr.strip() or stdout.strip()
    if not text:
        return "station worker exited without error output"
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    summary = lines[-1] if lines else text
    if len(summary) > 500:
        summary = summary[:497] + "..."
    return summary


def _process_station_candidate_chunked(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    canonical_dir: Path,
    quality_dir: Path,
    domains_dir: Path | None,
    output_root: Path,
    row_count: int,
) -> dict[str, Any]:
    start = time.perf_counter()
    archived_raw_path = Path(copied_entry["archived_raw_path_abs"])
    canonical_path = canonical_dir / f"{candidate.station_id}_cleaned.csv"
    quality_report_path = quality_dir / f"{candidate.station_id}_quality_report.json"
    runtime_root = output_root / ".runtime" / "station_chunks" / candidate.station_id
    if runtime_root.exists():
        shutil.rmtree(runtime_root)
    cleaned_chunks_dir = runtime_root / "cleaned"
    domain_chunks_dir = runtime_root / "domains"
    cleaned_chunks_dir.mkdir(parents=True, exist_ok=True)

    try:
        chunk_paths: list[Path] = []
        chunk_schemas: list[tuple[str, ...]] = []
        strict_summaries: list[dict[str, Any]] = []
        parse_error_rows = 0
        rows_with_any_usable_metric = 0
        output_rows = 0
        plans = _plan_station_chunks(row_count)

        for plan, raw_chunk in zip(
            plans,
            _iter_station_data_chunks(archived_raw_path, candidate.source_format),
            strict=True,
        ):
            cleaned_chunk = clean_noaa_dataframe(raw_chunk, keep_raw=False, strict_mode=True)
            output_rows += int(len(cleaned_chunk))
            if "__parse_error" in cleaned_chunk.columns:
                parse_error_rows += int(cleaned_chunk["__parse_error"].notna().sum())
            if "row_has_any_usable_metric" in cleaned_chunk.columns:
                rows_with_any_usable_metric += int(cleaned_chunk["row_has_any_usable_metric"].sum())
            strict_summaries.append(cleaned_chunk.attrs.get("strict_parse_summary", {}))
            chunk_schemas.append(tuple(cleaned_chunk.columns))
            chunk_path = cleaned_chunks_dir / f"chunk_{plan.chunk_index:05d}.csv"
            write_deterministic_csv(
                cleaned_chunk,
                chunk_path,
                sort_by=("STATION", "DATE"),
                float_format="%.1f",
            )
            chunk_paths.append(chunk_path)

        if len(chunk_paths) != len(plans):
            raise RuntimeError(
                f"Chunk execution mismatch for station {candidate.station_id}: "
                f"planned={len(plans)} cleaned={len(chunk_paths)}"
            )

        canonical_schema = _union_chunk_columns(chunk_schemas)
        _stream_collate_csv_chunks(
            chunk_paths=chunk_paths,
            output_path=canonical_path,
            aligned_columns=canonical_schema,
            float_format="%.1f",
        )
        domain_output_paths = (
            _write_chunked_domain_outputs(
                chunk_paths=chunk_paths,
                aligned_columns=canonical_schema,
                station_id=candidate.station_id,
                domains_dir=domains_dir,
                runtime_dir=domain_chunks_dir,
            )
            if domains_dir is not None
            else {}
        )
        strict_summary = _merge_strict_parse_summaries(strict_summaries)
        warnings_count = (
            parse_error_rows
            + int(strict_summary.get("skipped_encoded_column_count", 0))
            + int(strict_summary.get("token_rejection_count", 0))
        )
        _write_json(
            quality_report_path,
            {
                "station_id": candidate.station_id,
                "original_source_path": copied_entry["source_path"],
                "archived_raw_input_path": copied_entry["archived_raw_input_path"],
                "raw_sha256": copied_entry["raw_sha256"],
                "input_rows": row_count,
                "output_rows": output_rows,
                "parse_error_rows": parse_error_rows,
                "strict_parse_summary": strict_summary,
                "rows_with_any_usable_metric": rows_with_any_usable_metric,
                "domain_output_paths": {
                    domain: _relative_to_root(path, output_root)
                    for domain, path in domain_output_paths.items()
                },
                "warnings_count": warnings_count,
                "chunked_processing": {
                    "chunk_count": len(chunk_paths),
                    "chunk_row_count": _station_chunk_row_count(),
                    "chunking_threshold": _station_chunking_row_count_threshold(),
                },
            },
        )
        return {
            "station_id": candidate.station_id,
            "status": "success",
            "input_rows": row_count,
            "output_rows": output_rows,
            "runtime_seconds": time.perf_counter() - start,
            "archived_raw_input_path": copied_entry["archived_raw_input_path"],
            "raw_sha256": copied_entry["raw_sha256"],
            "canonical_output_path": _relative_to_root(canonical_path, output_root),
            "canonical_output_sha256": _sha256_file(canonical_path),
            "quality_report_path": _relative_to_root(quality_report_path, output_root),
            "domain_outputs_generated": bool(domain_output_paths),
            "warnings_count": warnings_count,
            "strict_parse_summary": strict_summary,
            "error_type": "",
            "error_message": "",
        }
    except BaseException as exc:
        return {
            "station_id": candidate.station_id,
            "status": "failed",
            "input_rows": 0,
            "output_rows": 0,
            "runtime_seconds": time.perf_counter() - start,
            "archived_raw_input_path": copied_entry["archived_raw_input_path"],
            "raw_sha256": copied_entry["raw_sha256"],
            "canonical_output_path": "",
            "canonical_output_sha256": "",
            "quality_report_path": "",
            "domain_outputs_generated": False,
            "warnings_count": 0,
            "strict_parse_summary": {},
            "error_type": exc.__class__.__name__,
            "error_message": str(exc),
        }
    finally:
        if runtime_root.exists():
            shutil.rmtree(runtime_root)
        _remove_empty_runtime_dirs(output_root)


def _write_domain_outputs(
    *,
    cleaned: pd.DataFrame,
    station_id: str,
    domains_dir: Path | None,
) -> dict[str, Path]:
    if domains_dir is None:
        return {}

    written: dict[str, Path] = {}
    for domain, frame in project_domains(cleaned).items():
        domain_dir = domains_dir / domain
        output_path = domain_dir / f"{station_id}_{domain}.csv"
        write_deterministic_csv(
            frame,
            output_path,
            sort_by=("STATION", "DATE"),
            float_format="%.1f",
        )
        written[domain] = output_path
    return written


def _write_chunked_domain_outputs(
    *,
    chunk_paths: list[Path],
    aligned_columns: tuple[str, ...],
    station_id: str,
    domains_dir: Path | None,
    runtime_dir: Path,
) -> dict[str, Path]:
    if domains_dir is None:
        return {}

    runtime_dir.mkdir(parents=True, exist_ok=True)
    domain_chunk_paths: dict[str, list[Path]] = {}
    domain_schemas: dict[str, list[tuple[str, ...]]] = {}
    for chunk_index, cleaned_chunk in enumerate(
        _iter_aligned_cleaned_chunks(chunk_paths, aligned_columns=aligned_columns)
    ):
        for domain, frame in project_domains(cleaned_chunk).items():
            domain_dir = runtime_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            chunk_path = domain_dir / f"chunk_{chunk_index:05d}.csv"
            write_deterministic_csv(
                frame,
                chunk_path,
                sort_by=("STATION", "DATE"),
                float_format="%.1f",
            )
            domain_chunk_paths.setdefault(domain, []).append(chunk_path)
            domain_schemas.setdefault(domain, []).append(tuple(frame.columns))

    written: dict[str, Path] = {}
    for domain, paths in sorted(domain_chunk_paths.items()):
        domain_dir = domains_dir / domain
        output_path = domain_dir / f"{station_id}_{domain}.csv"
        _stream_collate_csv_chunks(
            chunk_paths=paths,
            output_path=output_path,
            aligned_columns=_union_chunk_columns(domain_schemas[domain]),
            float_format="%.1f",
        )
        written[domain] = output_path
    return written


def _station_row_count(source_path: Path, source_format: str) -> int:
    if source_format in {"csv", "csv.gz"}:
        opener: Any
        if source_format == "csv.gz":
            import gzip

            opener = gzip.open
        else:
            opener = open
        with opener(source_path, "rt", encoding="utf-8", newline="") as handle:
            return max(sum(1 for _ in handle) - 1, 0)
    if source_format == "parquet":
        import pyarrow.parquet as pq

        return int(pq.ParquetFile(source_path).metadata.num_rows)
    raise ValueError(f"Unsupported source format: {source_format}")


def _iter_station_data_chunks(source_path: Path, source_format: str) -> Any:
    chunk_size = _station_chunk_row_count()
    if source_format == "csv":
        return pd.read_csv(source_path, dtype=str, chunksize=chunk_size)
    if source_format == "csv.gz":
        return pd.read_csv(
            source_path,
            dtype=str,
            compression="infer",
            chunksize=chunk_size,
        )
    if source_format == "parquet":
        import pyarrow.parquet as pq

        parquet_file = pq.ParquetFile(source_path)
        return (
            batch.to_pandas(split_blocks=True, self_destruct=True).astype("string")
            for batch in parquet_file.iter_batches(batch_size=chunk_size)
        )
    raise ValueError(f"Unsupported source format: {source_format}")


def _station_chunking_row_count_threshold() -> int:
    return _runtime_positive_int(
        env_name=STATION_CHUNKING_THRESHOLD_ENV,
        default=STATION_CHUNKING_ROW_COUNT_THRESHOLD,
    )


def _station_chunk_row_count() -> int:
    return _runtime_positive_int(
        env_name=STATION_CHUNK_ROW_COUNT_ENV,
        default=STATION_CHUNK_ROW_COUNT,
    )


def _runtime_positive_int(*, env_name: str, default: int) -> int:
    raw_value = os.environ.get(env_name, "").strip()
    if raw_value == "":
        return default
    value = int(raw_value)
    if value <= 0:
        raise ValueError(f"{env_name} must be a positive integer when set")
    return value


def _plan_station_chunks(row_count: int) -> tuple[StationChunkPlan, ...]:
    if row_count < 0:
        raise ValueError("row_count must be zero or greater")
    chunk_size = _station_chunk_row_count()
    plans: list[StationChunkPlan] = []
    start_row = 0
    chunk_index = 0
    while start_row < row_count:
        end_row = min(start_row + chunk_size, row_count)
        plans.append(
            StationChunkPlan(
                chunk_index=chunk_index,
                start_row=start_row,
                end_row=end_row,
            )
        )
        start_row = end_row
        chunk_index += 1
    return tuple(plans)


def _union_chunk_columns(chunk_schemas: list[tuple[str, ...]]) -> tuple[str, ...]:
    ordered: list[str] = []
    seen: set[str] = set()
    for schema in chunk_schemas:
        for column in schema:
            if column in seen:
                continue
            seen.add(column)
            ordered.append(column)
    return tuple(ordered)


def _align_chunk_columns(frame: pd.DataFrame, aligned_columns: tuple[str, ...]) -> pd.DataFrame:
    aligned = frame.copy()
    schema_changed = tuple(aligned.columns) != aligned_columns
    for column in aligned_columns:
        if column not in aligned.columns:
            aligned[column] = pd.NA
    aligned = aligned.loc[:, list(aligned_columns)]
    if schema_changed:
        aligned = _recompute_row_usability_summary(aligned)
    return aligned


def _recompute_row_usability_summary(frame: pd.DataFrame) -> pd.DataFrame:
    qc_pass_columns = [column for column in frame.columns if column.endswith("__qc_pass")]
    if not qc_pass_columns:
        return frame
    recomputed = frame.copy()
    qc_pass_frame = recomputed[qc_pass_columns].fillna(False).astype(bool)
    usable_metric_count = qc_pass_frame.sum(axis=1)
    recomputed["row_has_any_usable_metric"] = qc_pass_frame.any(axis=1)
    recomputed["usable_metric_count"] = usable_metric_count
    recomputed["usable_metric_fraction"] = (
        usable_metric_count / len(qc_pass_columns) if qc_pass_columns else 0.0
    )
    return recomputed


def _iter_aligned_cleaned_chunks(
    chunk_paths: list[Path],
    *,
    aligned_columns: tuple[str, ...],
) -> Any:
    for chunk_path in chunk_paths:
        yield _align_chunk_columns(
            pd.read_csv(chunk_path, dtype=str, low_memory=False),
            aligned_columns,
        )


def _stream_collate_csv_chunks(
    *,
    chunk_paths: list[Path],
    output_path: Path,
    aligned_columns: tuple[str, ...],
    float_format: str | None,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.parent / f".{output_path.name}.tmp-{os.getpid()}"
    try:
        wrote_header = False
        with tmp_path.open("w", encoding="utf-8", newline="") as handle:
            for chunk in _iter_aligned_cleaned_chunks(
                chunk_paths,
                aligned_columns=aligned_columns,
            ):
                if "usable_metric_fraction" in chunk.columns:
                    chunk["usable_metric_fraction"] = chunk["usable_metric_fraction"].map(
                        _format_usable_metric_fraction
                    )
                chunk.to_csv(
                    handle,
                    index=False,
                    header=not wrote_header,
                    lineterminator="\n",
                    na_rep="",
                    encoding="utf-8",
                    float_format=float_format,
                )
                wrote_header = True
        os.replace(tmp_path, output_path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def _format_usable_metric_fraction(value: object) -> object:
    if pd.isna(value) or value == "":
        return value
    formatted = f"{float(value):.6f}".rstrip("0").rstrip(".")
    if "." not in formatted:
        return f"{formatted}.0"
    return formatted


def _merge_strict_parse_summaries(summaries: list[dict[str, Any]]) -> dict[str, Any]:
    malformed_section_identifier_columns: set[str] = set()
    malformed_identifier_columns: set[str] = set()
    unsupported_identifier_columns: set[str] = set()
    supported_prefix_family_identifiers: set[str] = set()
    skipped_encoded_columns: set[str] = set()
    token_rejections_by_identifier: Counter[str] = Counter()
    token_rejections_by_reason: Counter[str] = Counter()
    token_rejections_by_identifier_part: Counter[str] = Counter()
    token_rejection_examples: list[dict[str, Any]] = []
    token_rejection_count = 0
    token_rejection_suppressed_log_count = 0

    for summary in summaries:
        malformed_section_identifier_columns.update(
            str(value) for value in summary.get("malformed_section_identifier_columns", ())
        )
        malformed_identifier_columns.update(
            str(value) for value in summary.get("malformed_identifier_columns", ())
        )
        unsupported_identifier_columns.update(
            str(value) for value in summary.get("unsupported_identifier_columns", ())
        )
        supported_prefix_family_identifiers.update(
            str(value) for value in summary.get("supported_prefix_family_identifiers", ())
        )
        skipped_encoded_columns.update(
            str(value) for value in summary.get("skipped_encoded_columns", ())
        )
        token_rejections_by_identifier.update(summary.get("token_rejections_by_identifier", {}))
        token_rejections_by_reason.update(summary.get("token_rejections_by_reason", {}))
        token_rejections_by_identifier_part.update(
            summary.get("token_rejections_by_identifier_part", {})
        )
        token_rejection_count += int(summary.get("token_rejection_count", 0) or 0)
        token_rejection_suppressed_log_count += int(
            summary.get("token_rejection_suppressed_log_count", 0) or 0
        )
        token_rejection_examples.extend(
            dict(example) for example in summary.get("token_rejection_examples", ())
        )

    return {
        "malformed_section_identifier_columns": tuple(sorted(malformed_section_identifier_columns)),
        "malformed_identifier_columns": tuple(sorted(malformed_identifier_columns)),
        "unsupported_identifier_columns": tuple(sorted(unsupported_identifier_columns)),
        "unknown_identifier_columns": tuple(sorted(unsupported_identifier_columns)),
        "supported_prefix_family_identifiers": tuple(sorted(supported_prefix_family_identifiers)),
        "skipped_encoded_columns": tuple(sorted(skipped_encoded_columns)),
        "skipped_encoded_column_count": len(skipped_encoded_columns),
        "token_rejection_count": token_rejection_count,
        "token_rejections_by_identifier": dict(sorted(token_rejections_by_identifier.items())),
        "token_rejections_by_reason": dict(sorted(token_rejections_by_reason.items())),
        "token_rejections_by_identifier_part": dict(
            sorted(token_rejections_by_identifier_part.items())
        ),
        "token_rejection_examples": token_rejection_examples[:10],
        "token_rejection_suppressed_log_count": token_rejection_suppressed_log_count,
    }


def _not_run_result(
    *,
    candidate: StationCandidate,
    copied_entry: dict[str, Any],
    output_root: Path,
    prior_station_id: str,
) -> dict[str, Any]:
    return {
        "station_id": candidate.station_id,
        "status": "not_run",
        "input_rows": 0,
        "output_rows": 0,
        "runtime_seconds": 0.0,
        "archived_raw_input_path": copied_entry["archived_raw_input_path"],
        "raw_sha256": copied_entry["raw_sha256"],
        "canonical_output_path": "",
        "canonical_output_sha256": "",
        "quality_report_path": "",
        "domain_outputs_generated": False,
        "warnings_count": 0,
        "error_type": "prior_station_failure",
        "error_message": (
            "Workflow stopped after an earlier selected station failed and "
            f"--continue-on-error was not set (first failure station_id={prior_station_id})."
        ),
    }


def _update_selection_row_with_result(
    selection_rows: list[dict[str, Any]],
    result: dict[str, Any],
) -> None:
    station_id = str(result["station_id"])
    archived_raw_input_path = str(result["archived_raw_input_path"])
    for row in selection_rows:
        if (
            row["station_id"] == station_id
            and row["archived_raw_input_path"] == archived_raw_input_path
        ):
            if int(result["input_rows"] or 0) > 0:
                row["row_count"] = int(result["input_rows"])
            row["processing_status"] = str(result["status"])
            return


def _read_station_data(source_path: Path, source_format: str) -> pd.DataFrame:
    if source_format == "csv":
        return pd.read_csv(source_path, dtype=str)
    if source_format == "csv.gz":
        return pd.read_csv(source_path, dtype=str, compression="infer")
    if source_format == "parquet":
        return pd.read_parquet(source_path).astype("string")
    raise ValueError(f"Unsupported source format: {source_format}")


def _write_summary(
    *,
    summary_path: Path,
    run_manifest: dict[str, Any],
    selection_rows: list[dict[str, Any]],
    results_rows: list[dict[str, Any]],
    total_input_rows: int,
    total_output_rows: int,
    total_runtime: float,
    bundle_strict_summary: dict[str, Any],
) -> None:
    selected_rows = [row for row in selection_rows if row["selection_status"] == "selected"]
    succeeded = [row for row in results_rows if row["status"] == "success"]
    failed = [row for row in results_rows if row["status"] == "failed"]
    not_run = [row for row in results_rows if row["status"] == "not_run"]
    selected_sizes = [int(row["file_size_bytes"]) for row in selected_rows]
    size_summary = _selected_size_summary(selected_sizes)
    counts_by_stratum = {
        label: sum(1 for row in selected_rows if row["size_stratum"] == label)
        for label in ("q1", "q2", "q3", "q4")
    }
    token_summary = bundle_strict_summary["token_validation_rejections"]

    lines = [
        "# 100-Station Validation Summary",
        "",
        "## Purpose",
        SUMMARY_OPERATIONAL_LANGUAGE,
        SUMMARY_ARCHIVAL_LANGUAGE,
        "",
        "## What this artifact demonstrates",
        "- The repository-controlled cleaning workflow completed across a deterministic stratified station sample.",
        "- The bundle freezes selected raw inputs, cleaned outputs, per-station results, manifests, and checksums for reviewer inspection.",
        "",
        "## What this artifact does not demonstrate",
        f"- {SUMMARY_NON_EXHAUSTIVE_LANGUAGE}",
        "- It does not claim exhaustive validation of the full NOAA corpus or universal correctness for all NOAA station files.",
        "",
        "## Sampling method",
        f"- Strategy: {run_manifest['sampling_strategy']}",
        f"- Seed: {run_manifest['seed']}",
        f"- Stations requested: {run_manifest['station_count_requested']}",
        f"- Stations selected: {run_manifest['station_count_selected']}",
        f"- Min file size (bytes): {size_summary['min']}",
        f"- Median file size (bytes): {size_summary['median']}",
        f"- Max file size (bytes): {size_summary['max']}",
        f"- Counts by size stratum: q1={counts_by_stratum['q1']}, q2={counts_by_stratum['q2']}, q3={counts_by_stratum['q3']}, q4={counts_by_stratum['q4']}",
        f"- {SUMMARY_SELECTION_LANGUAGE}",
        "",
        "## Provenance and raw inputs",
        "- Selected raw station files are copied into `raw_inputs/` and checksum-recorded before cleaning.",
        "- Once DOI-backed archival is complete, reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.",
        "- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.",
        "",
        "## Run environment",
        f"- Build ID: {run_manifest['build_id']}",
        f"- Timestamp (UTC): {run_manifest['timestamp_utc']}",
        f"- Python: {run_manifest['python_version']}",
        f"- Platform: {run_manifest['platform']}",
        f"- Package version: {run_manifest['package_version']}",
        f"- Repo commit SHA: {run_manifest['repo_commit_sha'] or 'unavailable'}",
        f"- Git dirty status: {run_manifest['git_dirty_status'] or 'unavailable'}",
        "",
        "## Results summary",
        f"- Stations succeeded: {len(succeeded)}",
        f"- Stations failed: {len(failed)}",
        f"- Stations not run after first failure: {len(not_run)}",
        f"- Total input rows: {total_input_rows}",
        f"- Total output rows: {total_output_rows}",
        f"- Total runtime (seconds): {total_runtime:.6f}",
        f"- Domain outputs generated: {bool(run_manifest.get('domain_outputs_requested'))}",
        f"- Primary checksum file: {summary_path.parent / 'checksums_primary.txt'}",
        f"- Supplementary domains checksum file: {summary_path.parent / 'checksums_domains.txt'}",
        "",
        "## Strict token diagnostics",
        f"- Strict token rejection count: {token_summary['total_token_rejection_count']}",
        f"- Affected station count: {token_summary['affected_station_count']}",
        f"- {STRICT_TOKEN_DIAGNOSTIC_LANGUAGE}",
        "",
        "## Failure summary",
    ]

    if failed or not_run:
        for row in failed + not_run:
            lines.append(f"- {row['station_id']}: {row['error_type']} - {row['error_message']}")
    else:
        lines.append("- No station failures were recorded.")

    lines.extend(
        [
            "",
            "## Output artifact inventory",
            "PRIMARY:",
            "- `raw_inputs/`",
            "- `canonical_cleaned/`",
            "- `quality_reports/`",
            "- `station_selection_manifest.csv`",
            "- `selected_station_metadata.csv`",
            "- `run_manifest.json`",
            "- `station_results.csv`",
            "- `aggregate_quality_summary.json`",
            "- `aggregate_quality_summary.md`",
            "- `strict_parse_summary_report.json`",
            "- `strict_parse_summary_report.md`",
            "- `strict_token_rejection_explanation.md`",
            "- `checksums_primary.txt`",
            "- `summary.md`",
            "- `archive_manifest_primary.json`",
            "",
            "SUPPLEMENTARY:",
            *(
                [
                    "- `domains/`",
                    "- `archive_manifest_domains.json`",
                    "- `checksums_domains.txt`",
                ]
                if bool(run_manifest.get("domain_outputs_requested"))
                else []
            ),
            "",
            "## Reproducibility boundary",
            run_manifest["reproducibility_boundary_note"],
            "",
            "## DOI archival status",
            f"- Primary DOI: {PRIMARY_DOI_PLACEHOLDER}",
            "- The DOI placeholder must be replaced before final DOI freeze or JOSS submission.",
            "",
        ]
    )
    summary_path.write_text("\n".join(lines), encoding="utf-8")


def _build_archive_manifest_payload(
    *,
    output_root: Path,
    run_manifest: dict[str, Any],
    archive_type: str,
) -> dict[str, Any]:
    if archive_type == "primary":
        archive_paths = _primary_archive_paths(output_root)
        checksum_file = "checksums_primary.txt"
        manifest_file = "archive_manifest_primary.json"
        intended_archive = "primary DOI archive"
        doi = PRIMARY_DOI_PLACEHOLDER
        content_classification = [
            "raw_inputs/",
            "canonical_cleaned/",
            "quality_reports/",
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
    elif archive_type == "supplementary_domains":
        archive_paths = _domains_archive_paths(output_root)
        checksum_file = "checksums_domains.txt"
        manifest_file = "archive_manifest_domains.json"
        intended_archive = "supplementary domains DOI archive"
        doi = DOMAINS_DOI_PLACEHOLDER
        content_classification = [
            "domains/",
            "archive_manifest_domains.json",
            "checksums_domains.txt",
        ]
    else:
        raise ValueError(f"unknown archive_type: {archive_type}")

    top_level_files = sorted({path.relative_to(output_root).parts[0] for path in archive_paths})
    directory_inventory = []
    for directory_name in sorted({path.relative_to(output_root).parts[0] for path in archive_paths if len(path.relative_to(output_root).parts) > 1}):
        directory = output_root / directory_name
        dir_files = sorted(path for path in archive_paths if path.is_relative_to(directory))
        directory_inventory.append(
            {
                "path": directory_name,
                "file_count": len(dir_files),
                "total_bytes": sum(path.stat().st_size for path in dir_files),
                "archive_classification": archive_type,
            }
        )

    return {
        "archive_type": archive_type,
        "artifact_name": "validation_100_station_primary" if archive_type == "primary" else "validation_100_station_domains",
        "artifact_version": str(run_manifest["build_id"]),
        "build_id": str(run_manifest["build_id"]),
        "repo_commit_sha": run_manifest["repo_commit_sha"],
        "git_sha": run_manifest["repo_commit_sha"],
        "git_tag": run_manifest["git_tag"],
        "created_utc": _now_utc_isoformat(),
        "generated_timestamp_utc": _now_utc_isoformat(),
        "intended_archive": intended_archive,
        "total_files": len(archive_paths),
        "total_bytes": sum(path.stat().st_size for path in archive_paths),
        "file_count": len(archive_paths),
        "byte_count": sum(path.stat().st_size for path in archive_paths),
        "checksum_algorithm": "SHA256",
        "checksum_file": checksum_file,
        "manifest_file": manifest_file,
        "top_level_files": top_level_files,
        "directory_inventory": directory_inventory,
        "doi": doi,
        "primary_doi": PRIMARY_DOI_PLACEHOLDER if archive_type == "primary" else None,
        "domains_doi": DOMAINS_DOI_PLACEHOLDER if archive_type == "supplementary_domains" else None,
        "claim_scope": REPRODUCIBILITY_BOUNDARY_NOTE if archive_type == "primary" else (
            "Convenience domain projections derived from canonical outputs. "
            "Domain outputs are not required to reproduce NOAA-Spec's core deterministic cleaning behavior."
        ),
        "archive_content_classification": content_classification,
    }


def _primary_archive_paths(output_root: Path) -> list[Path]:
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
    return _existing_archive_paths(output_root=output_root, entries=primary_entries)


def _domains_archive_paths(output_root: Path) -> list[Path]:
    return _existing_archive_paths(
        output_root=output_root,
        entries=["domains", "archive_manifest_domains.json", "checksums_domains.txt"],
    )


def _domains_checksum_paths(output_root: Path) -> list[Path]:
    return _existing_archive_paths(output_root=output_root, entries=["domains"])


def _existing_archive_paths(*, output_root: Path, entries: list[str]) -> list[Path]:
    paths: list[Path] = []
    for entry in entries:
        path = output_root / entry
        if path.is_file():
            paths.append(path)
        elif path.is_dir():
            paths.extend(sorted(item for item in path.rglob("*") if item.is_file()))
    return paths


def _finalize_archive_manifests_and_checksums(
    *,
    archive_manifest_primary_path: Path,
    archive_manifest_domains_path: Path,
    checksums_primary_path: Path,
    checksums_domains_path: Path,
    output_root: Path,
    run_manifest: dict[str, Any],
) -> None:
    # Manifests include byte counts for their archive boundaries. Iterate until
    # manifest/checksum sizes stabilize; checksum line lengths are fixed, so
    # this converges quickly.
    previous_sizes: tuple[int, int, int, int] | None = None
    for _ in range(5):
        _write_json(
            archive_manifest_primary_path,
            _build_archive_manifest_payload(
                output_root=output_root,
                run_manifest=run_manifest,
                archive_type="primary",
            ),
        )
        _write_json(
            archive_manifest_domains_path,
            _build_archive_manifest_payload(
                output_root=output_root,
                run_manifest=run_manifest,
                archive_type="supplementary_domains",
            ),
        )
        _write_checksums(checksums_path=checksums_primary_path, paths=_primary_archive_paths(output_root))
        _write_checksums(checksums_path=checksums_domains_path, paths=_domains_checksum_paths(output_root))
        sizes = (
            archive_manifest_primary_path.stat().st_size,
            archive_manifest_domains_path.stat().st_size,
            checksums_primary_path.stat().st_size,
            checksums_domains_path.stat().st_size,
        )
        if sizes == previous_sizes:
            return
        previous_sizes = sizes

    _write_json(
        archive_manifest_primary_path,
        _build_archive_manifest_payload(
            output_root=output_root,
            run_manifest=run_manifest,
            archive_type="primary",
        ),
    )
    _write_json(
        archive_manifest_domains_path,
        _build_archive_manifest_payload(
            output_root=output_root,
            run_manifest=run_manifest,
            archive_type="supplementary_domains",
        ),
    )
    _write_checksums(checksums_path=checksums_primary_path, paths=_primary_archive_paths(output_root))
    _write_checksums(checksums_path=checksums_domains_path, paths=_domains_checksum_paths(output_root))


def _write_checksums(*, checksums_path: Path, paths: list[Path]) -> None:
    checksums_resolved = checksums_path.resolve()
    paths = sorted(
        path
        for path in paths
        if path.is_file() and path.resolve() != checksums_resolved
    )
    output_root = checksums_path.parent
    lines = [f"{_sha256_file(path)}  {path.relative_to(output_root).as_posix()}" for path in paths]
    checksums_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _remove_empty_runtime_dirs(output_root: Path) -> None:
    runtime_root = output_root / ".runtime"
    if not runtime_root.exists():
        return
    for path in sorted(
        (item for item in runtime_root.rglob("*") if item.is_dir()),
        key=lambda item: len(item.parts),
        reverse=True,
    ):
        try:
            path.rmdir()
        except OSError:
            pass
    try:
        runtime_root.rmdir()
    except OSError:
        pass


def _selected_size_summary(selected_sizes: list[int]) -> dict[str, int]:
    if not selected_sizes:
        return {"min": 0, "median": 0, "max": 0}
    ordered = sorted(selected_sizes)
    median = int(pd.Series(ordered, dtype="int64").median())
    return {"min": ordered[0], "median": median, "max": ordered[-1]}


def _station_selection_columns() -> list[str]:
    return [
        "station_id",
        "source_path",
        "archived_raw_input_path",
        "source_format",
        "file_size_bytes",
        "row_count",
        "size_stratum",
        "selection_rank",
        "selection_reason",
        "selected_by",
        "seed",
        "raw_sha256",
        "input_root",
        "source_root",
        "copied_utc",
        "source_url",
        "original_source_filename",
        "selection_status",
        "skip_reason",
        "processing_status",
    ]


def _station_results_columns() -> list[str]:
    return [
        "station_id",
        "status",
        "input_rows",
        "output_rows",
        "runtime_seconds",
        "archived_raw_input_path",
        "raw_sha256",
        "canonical_output_path",
        "canonical_output_sha256",
        "quality_report_path",
        "domain_outputs_generated",
        "warnings_count",
        "error_type",
        "error_message",
    ]


def _detect_source_format(path: Path) -> str | None:
    name = path.name.lower()
    if name.endswith(".csv.gz"):
        return "csv.gz"
    if path.suffix.lower() == ".csv":
        return "csv"
    if path.suffix.lower() == ".parquet":
        return "parquet"
    return None


def _station_id_from_path(path: Path) -> str:
    name = path.name
    if name.lower().endswith(".csv.gz"):
        stem = name[:-7]
    else:
        stem = path.stem
    digits = "".join(character for character in stem if character.isdigit())
    if len(digits) >= 11:
        return digits[:11]
    parent_digits = "".join(character for character in path.parent.name if character.isdigit())
    if len(parent_digits) >= 11:
        return parent_digits[:11]
    return stem


def _infer_source_url(*, station_id: str, source_path: Path) -> str | None:
    if len(station_id) != 11 or not station_id.isdigit():
        return None
    year = next(
        (
            part
            for part in source_path.parts
            if len(part) == 4 and part.isdigit() and 1900 <= int(part) <= 2100
        ),
        None,
    )
    if year is None:
        return None
    return f"https://www.ncei.noaa.gov/data/global-hourly/access/{year}/{station_id}.csv"


def _selection_score(*, seed: int, station_id: str, source_path: Path) -> int:
    text = f"{seed}|{station_id}|{source_path.as_posix()}"
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _relative_to_root(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _now_utc_isoformat() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _git_metadata() -> dict[str, str | None]:
    repo_root = Path(__file__).resolve().parents[2]
    commit = _run_git_command(["git", "rev-parse", "HEAD"], repo_root)
    dirty_output = _run_git_command(["git", "status", "--porcelain"], repo_root)
    dirty_status = None if dirty_output is None else ("dirty" if dirty_output else "clean")
    git_tag = _run_git_command(["git", "describe", "--tags", "--exact-match"], repo_root)
    return {
        "repo_commit_sha": commit,
        "git_dirty_status": dirty_status,
        "git_tag": git_tag,
    }


def _env_or_none(name: str) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or None


def _run_git_command(command: list[str], cwd: Path) -> str | None:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip()


def _dependency_lock_hash() -> str | None:
    repo_root = Path(__file__).resolve().parents[2]
    poetry_lock = repo_root / "poetry.lock"
    if not poetry_lock.exists():
        return None
    return _sha256_file(poetry_lock)


def _run_station_worker_cli(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m noaa_spec.validation _station-worker")
    parser.add_argument("command", choices=("_station-worker",))
    parser.add_argument("--station-id", required=True)
    parser.add_argument("--source-path", required=True, type=Path)
    parser.add_argument("--source-format", required=True)
    parser.add_argument("--file-size-bytes", required=True, type=int)
    parser.add_argument("--size-stratum", default="")
    parser.add_argument("--selection-score", required=True, type=int)
    parser.add_argument("--archived-raw-path", required=True, type=Path)
    parser.add_argument("--archived-raw-input-path", required=True)
    parser.add_argument("--raw-sha256", required=True)
    parser.add_argument("--original-source-path", required=True)
    parser.add_argument("--canonical-dir", required=True, type=Path)
    parser.add_argument("--quality-dir", required=True, type=Path)
    parser.add_argument("--domains-dir", type=Path, default=None)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--result-path", required=True, type=Path)
    args = parser.parse_args(argv)

    candidate = StationCandidate(
        station_id=args.station_id,
        source_path=args.source_path,
        source_format=args.source_format,
        file_size_bytes=args.file_size_bytes,
        size_stratum=args.size_stratum or None,
        selection_score=args.selection_score,
    )
    copied_entry = {
        "station_id": args.station_id,
        "source_path": args.original_source_path,
        "source_format": args.source_format,
        "archived_raw_input_path": args.archived_raw_input_path,
        "archived_raw_path_abs": args.archived_raw_path,
        "raw_sha256": args.raw_sha256,
    }
    result = _process_station_candidate_in_worker(
        candidate=candidate,
        copied_entry=copied_entry,
        canonical_dir=args.canonical_dir,
        quality_dir=args.quality_dir,
        domains_dir=args.domains_dir,
        output_root=args.output_root,
    )
    _write_json(
        args.result_path,
        {
            "schema_version": WORKER_RESULT_SCHEMA_VERSION,
            "result": result,
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(_run_station_worker_cli(sys.argv[1:]))
