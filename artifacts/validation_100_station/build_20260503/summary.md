# 100-Station Validation Summary

## Purpose
Small upstream-traceable fixtures verify semantic correctness. The 100-station validation artifact demonstrates that the same repository-controlled workflow runs successfully across a broader stratified operational sample.
The archived raw inputs are included to make the validation evidence inspectable and rerunnable without relying on live NOAA availability.

## What this artifact demonstrates
- The repository-controlled cleaning workflow completed across a deterministic stratified station sample.
- The bundle freezes selected raw inputs, cleaned outputs, per-station results, manifests, and checksums for reviewer inspection.

## What this artifact does not demonstrate
- This artifact does not prove correctness over the full NOAA corpus.
- It does not claim exhaustive validation of the full NOAA corpus or universal correctness for all NOAA station files.

## Sampling method
- Strategy: size-stratified
- Seed: 20260503
- Stations requested: 100
- Stations selected: 100
- Min file size (bytes): 14531
- Median file size (bytes): 1563037
- Max file size (bytes): 18686079
- Counts by size stratum: q1=25, q2=25, q3=25, q4=25
- The sample is deterministic and size-stratified, not manually selected for favorable outcomes.

## Provenance and raw inputs
- Selected raw station files are copied into `raw_inputs/` and checksum-recorded before cleaning.
- Reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.
- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.

## Run environment
- Build ID: 20260502
- Timestamp (UTC): 2026-05-04T02:28:46Z
- Python: 3.12.3
- Platform: Linux-6.17.0-19-generic-x86_64-with-glibc2.39
- Package version: 1.0.0
- Repo commit SHA: fb56c08d8bc5fc33a7b4c2e14059d0bd1a8f6ace
- Git dirty status: clean

## Results summary
- Stations succeeded: 100
- Stations failed: 0
- Stations not run after first failure: 0
- Total input rows: 11068671
- Total output rows: 11068671
- Total runtime (seconds): 10447.239716
- Checksum file: /home/balaji-kesavan/Documents/AI_Projects/noaa-spec/artifacts/validation_100_station/build_20260503/checksums.txt

## Strict token diagnostics
- Strict token rejection count: 2352988
- Affected station count: 70
- Strict token-level validation rejections are diagnostic. They identify optional-section payloads that did not match declared token-width expectations. They did not cause station-level failure or row loss in this validation run.

## Failure summary
- No station failures were recorded.

## Output artifact inventory
- `raw_inputs/`
- `canonical_cleaned/`
- `quality_reports/`
- `station_selection_manifest.csv`
- `run_manifest.json`
- `station_results.csv`
- `strict_parse_summary_report.json`
- `strict_parse_summary_report.md`
- `checksums.txt`
- `summary.md`
- `archive_manifest.json`

## Reproducibility boundary
This artifact provides operational smoke validation for a stratified 100-station sample. It does not claim exhaustive validation of the full NOAA corpus. Semantic correctness is verified by tracked upstream-traceable fixtures and tests. The selected raw inputs are archived with checksums so reviewers can inspect or rerun the workflow without depending on live NOAA availability.

## DOI archival status
- DOI: TO_BE_ADDED_BEFORE_JOSS_SUBMISSION
- This bundle is intended for external archival so reviewers can inspect it without rerunning the workflow.
