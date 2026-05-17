# 100-Station Validation Summary

## Purpose
Small upstream-traceable fixtures verify semantic correctness. The 100-station validation artifact is supplementary operational evidence that the same repository-controlled workflow runs successfully across a broader stratified sample.
The raw inputs are intended for DOI-backed archival before submission so the validation evidence can be inspected and rerun without relying on live NOAA availability.

## What this artifact demonstrates
- The repository-controlled cleaning workflow completed across a deterministic stratified station sample.
- The bundle freezes selected raw inputs, cleaned outputs, per-station results, manifests, and checksums for reviewer inspection.

## What this artifact does not demonstrate
- This artifact does not prove correctness over the full NOAA corpus.
- It does not claim exhaustive validation of the full NOAA corpus or universal correctness for all NOAA station files.

## Sampling method
- Strategy: size-stratified
- Seed: 20260510
- Stations requested: 100
- Stations selected: 100
- Min file size (bytes): 15283
- Median file size (bytes): 1418796
- Max file size (bytes): 53121220
- Counts by size stratum: q1=25, q2=25, q3=25, q4=25
- The sample is deterministic and size-stratified, not manually selected for favorable outcomes.

## Provenance and raw inputs
- Selected raw station files are copied into `raw_inputs/` and checksum-recorded before cleaning.
- Once DOI-backed archival is complete, reviewers can inspect the archived bundle without needing the original local station corpus or live NOAA access.
- Local rerun requires either the archived raw input bundle or a local NOAA station corpus.

## Run environment
- Build ID: 20260510
- Timestamp (UTC): 2026-05-13T01:22:21Z
- Python: 3.12.3
- Platform: Linux-6.17.0-19-generic-x86_64-with-glibc2.39
- Package version: 1.0.0
- Repo commit SHA: 03d378f10b8f6da683051bac712d03e75669ff94
- Git dirty status: clean

## Results summary
- Stations succeeded: 100
- Stations failed: 0
- Stations not run after first failure: 0
- Total input rows: 17884625
- Total output rows: 17884625
- Total runtime (seconds): 40298.503880
- Domain outputs generated: True
- Checksum file: /home/balaji-kesavan/Documents/AI_Projects/noaa-spec/artifacts/validation_100_station/build_20260510/checksums.txt

## Strict token diagnostics
- Strict token rejection count: 7347677
- Affected station count: 70
- Strict token-level validation rejections are observability signals. They identify optional-section payloads that did not match declared token-width expectations. They did not cause station-level failure or row loss in this validation run.

## Failure summary
- No station failures were recorded.

## Output artifact inventory
- `raw_inputs/`
- `canonical_cleaned/`
- `domains/`
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
This artifact provides operational smoke validation for a stratified 100-station sample. It does not claim exhaustive validation of the full NOAA corpus. Semantic correctness is verified by tracked upstream-traceable fixtures, tests, and source-document-linked rule families. The selected raw inputs are archived with checksums so reviewers can inspect or rerun the workflow without depending on live NOAA availability once a DOI-backed archive exists.

## DOI archival status
- DOI: TO_BE_ADDED_BEFORE_JOSS_SUBMISSION
- This bundle is intended for external archival before submission; until a DOI is inserted, the archive should be treated as planned.
