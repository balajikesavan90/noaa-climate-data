# 100-Station Validation Summary

## Purpose
Small upstream-traceable fixtures verify semantic correctness. The 100-station validation artifact is supplementary operational evidence that the same repository-controlled workflow runs successfully across a broader stratified sample.
This validation artifact supports deterministic reproducibility from archived validation inputs to archived outputs. Reconstruction from upstream NOAA archives is not claimed because upstream NOAA source URLs and checksums are not preserved within this artifact.

## What this artifact demonstrates
- The repository-controlled cleaning workflow completed across a deterministic stratified station sample.
- The bundle freezes selected raw inputs, cleaned outputs, per-station results, manifests, and checksums for reviewer inspection.

## What this artifact does not demonstrate
- This artifact does not prove correctness over the full NOAA corpus.
- It does not claim exhaustive validation of the full NOAA corpus or universal correctness for all NOAA station files.

## Sampling method
- Strategy: size-stratified
- Seed: 20260517
- Stations requested: 100
- Stations selected: 100
- Min file size (bytes): 12751
- Median file size (bytes): 1611885
- Max file size (bytes): 50554472
- Counts by size stratum: q1=25, q2=25, q3=25, q4=25
- The sample is deterministic and size-stratified, not manually selected for favorable outcomes.

## Provenance and raw inputs
- Selected raw station files are copied into `raw_inputs/` and checksum-recorded before cleaning.
- Once DOI-backed archival is complete, reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.
- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.

## Run environment
- Build ID: 20260517
- Timestamp (UTC): 2026-05-18T04:40:25Z
- Python: 3.12.3
- Platform: Linux-6.17.0-19-generic-x86_64-with-glibc2.39
- Package version: 1.0.0
- Repo commit SHA: d086cfec3096d137d40ca4acb97b1370f6b29400
- Git dirty status: clean

## Results summary
- Stations succeeded: 100
- Stations failed: 0
- Stations not run after first failure: 0
- Total input rows: 12612131
- Total output rows: 12612131
- Total runtime (seconds): 20596.293976
- Domain outputs generated: True
- Checksum file: /home/balaji-kesavan/Documents/AI_Projects/noaa-spec/artifacts/validation_100_station/build_20260517/checksums.txt

## Strict token diagnostics
- Strict token rejection count: 2681534
- Affected station count: 70
- Strict token-level validation rejections are observability signals. They identify optional-section payloads that did not match declared token-width expectations. They did not cause station-level failure or row loss in this validation run.

## Failure summary
- No station failures were recorded.

## Output artifact inventory
PRIMARY:
- `raw_inputs/`
- `canonical_cleaned/`
- `quality_reports/`
- `station_selection_manifest.csv`
- `selected_station_metadata.csv`
- `run_manifest.json`
- `station_results.csv`
- `aggregate_quality_summary.json`
- `aggregate_quality_summary.md`
- `strict_parse_summary_report.json`
- `strict_parse_summary_report.md`
- `strict_token_rejection_explanation.md`
- `checksums.txt`
- `summary.md`
- `archive_manifest.json`

SUPPLEMENTARY:
- `domains/`

## Reproducibility boundary
This validation artifact supports deterministic reproducibility from archived validation inputs to archived outputs. Reconstruction from upstream NOAA archives is not claimed because upstream NOAA source URLs and checksums are not preserved within this artifact.

The primary DOI archive contains the canonical reproducibility boundary:

archived inputs → deterministic NOAA-Spec processing → canonical cleaned outputs

Domain outputs are convenience projections intended to improve interpretability for downstream workflows. They are derived from canonical cleaned outputs and are not required to reproduce NOAA-Spec's core deterministic cleaning behavior.

Domain outputs are archived separately as supplementary artifacts and are outside the primary reproducibility claim.

## DOI archival status
- Primary DOI: TODO_PRIMARY_DOI
- Supplementary Domains DOI: TODO_DOMAINS_DOI
- The DOI placeholders must be replaced before final DOI freeze or JOSS submission.
