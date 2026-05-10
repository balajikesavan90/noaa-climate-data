# 100-Station Validation Summary

## Purpose
Small upstream-traceable fixtures verify semantic correctness. The 100-station
validation artifact is supplementary Tier 2 operational metadata for a broader
stratified sample.
The raw inputs and canonical outputs are not tracked in this repository. They
must be published in a DOI-backed archive before this validation run can be
treated as rerunnable evidence.

## What this artifact demonstrates
- The repository-controlled cleaning workflow completed across a deterministic stratified station sample.
- The future DOI-backed bundle is expected to freeze selected raw inputs,
  cleaned outputs, per-station results, manifests, and checksums for reviewer
  inspection.

## What this artifact does not demonstrate
- This artifact does not prove correctness over the full NOAA corpus.
- It does not claim exhaustive validation of the full NOAA corpus or universal correctness for all NOAA station files.
- It is not fully reproducible from the git repository alone.

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
- Selected raw station files were copied into `raw_inputs/` during the local
  validation run and are excluded from git.
- Once DOI-backed archival is complete, reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.
- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.

## Run environment
- Build ID: 20260503
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
- Checksum file: LOCAL_PATH_PLACEHOLDER
- # Local path removed for portability

## Strict token diagnostics
- Strict token rejection count: 2352988
- Affected station count: 70
- Strict token-level validation rejections are observability signals. They identify optional-section payloads that did not match declared token-width expectations. They did not cause station-level failure or row loss in this validation run.

## Failure summary
- No station failures were recorded.

## Output artifact inventory
- `raw_inputs/` (excluded from git; expected in DOI archive)
- `canonical_cleaned/` (excluded from git; expected in DOI archive)
- `quality_reports/`
- `station_selection_manifest.csv`
- `run_manifest.json`
- `station_results.csv`
- `strict_parse_summary_report.md`
- `checksums.txt` (excluded from git; expected in DOI archive)
- `summary.md`
- `archive_manifest.json`

## Reproducibility boundary
This artifact provides Tier 2 optional operational smoke-validation metadata for
a stratified 100-station sample. It is not fully reproducible from this
repository alone. Semantic correctness is verified by tracked
upstream-traceable fixtures, tests, and source-document-linked rule families.
The selected raw inputs and canonical outputs must be archived with checksums
before reviewers can inspect or rerun the workflow without depending on live
NOAA availability.

## DOI archival status
- DOI: TO_BE_ASSIGNED
- This bundle is intended for external archival before submission; until a DOI
  is inserted, the archive should be treated as planned.
