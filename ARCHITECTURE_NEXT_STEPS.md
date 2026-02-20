# Architecture next steps: normalized checklist

This document normalizes conflicts between `tech_debt.md` and `DATASET_ARCHITECTURE_RECOMMENDATIONS.md`.
Use this file as the implementation checklist and source of truth for architecture/productization work.

## Priority recommendation: `NEXT_STEPS.md` vs architecture work

- [ ] Keep `NEXT_STEPS.md` as correctness gate for parser/cleaning semantics.
- [ ] Use a working split of ~70% `NEXT_STEPS.md` and ~30% architecture tasks until `NEXT_STEPS.md` P0/P1 are complete.
- [ ] Allow parallel architecture work only for low-risk scaffolding (config, manifests, schemas, CI, release plumbing).
- [ ] Shift to ~50/50 once parser outputs are stable.
- [ ] Shift to ~30/70 (favoring architecture) once remaining `NEXT_STEPS.md` items are mostly validation hardening.

## P0: conflict normalization (lock these decisions first)

- [ ] Adopt `schemas/` as the canonical contract location; treat `data_contracts/` as deprecated naming.
- [ ] Standardize raw partitioning to `layer=raw_station/station_bucket=<00-ff>/year=<yyyy>/month=<mm>/` and keep `station_id` in file name/metadata (not a partition directory).
- [ ] Standardize clean partitioning to `layer=clean_station/station_bucket=<00-ff>/year=<yyyy>/month=<mm>/`.
- [ ] Standardize curated partitioning to `layer=curated/dataset=<metric>_station/station_bucket=<00-ff>/year=<yyyy>/month=<mm>/`.
- [ ] Standardize aggregated partitioning to `layer=aggregated/dataset=<metric>_<grain>/year=<yyyy>/month=<mm>/` (omit `month` for yearly or normals outputs).
- [ ] Keep canonical natural keys (`station_id`, `timestamp_utc`, `year`, `month`, `day`, `hour`) and add deterministic `record_id` hash for observation-level joins/dedup.
- [ ] Standardize provenance column naming with `meta_` prefix: `meta_run_id`, `meta_dataset_version`, `meta_pipeline_commit`, `meta_processed_at_utc`, `meta_source_year`, `meta_source_file_name`, `meta_parent_snapshot_id`.
- [ ] Keep raw NOAA quality/code fields and add derived usability fields (`*_qc_status`, `*_qc_pass`, `*_usable`) in clean/curated outputs.
- [ ] Canonicalize CLI names to `build-clean-station`, `build-curated`, `build-aggregates`, `validate`, `publish-release`, `run --config`; keep compatibility aliases for `build-metric-stations` and `build-release`.
- [ ] Canonicalize release artifacts to `checksums.sha256` and `CHANGELOG_DATASET.md` (keep root `CHANGELOG.md` for code changes).
- [ ] Use both contract layers: versioned JSON schemas for persisted datasets plus Pandera checks in pipeline/runtime validation.

## P1: repository architecture and compatibility boundaries

- [ ] Keep incremental migration in `src/noaa_climate_data/` (no big-bang rewrite).
- [ ] Extract modules with clear boundaries: `ingestion`, `parsing`, `cleaning`, `transforms`, `aggregation`, `validation`, `metadata`, `publish`, `io`, `orchestration`, `observability`.
- [ ] Keep `constants.py`, `cleaning.py`, and `pipeline.py` as compatibility facades while internal modules are extracted.
- [ ] Add `src/noaa_climate_data/api.py` as the stable Python API surface.
- [ ] Add `src/noaa_climate_data/config.py` and central config loading for paths, partitions, manifests, and release settings.
- [ ] Move root one-off scripts into `scripts/` or CLI commands.
- [ ] Define internal/private helpers with `_` prefix and keep them out of public docs.

## P2: dataset layering and schema contracts

- [ ] Implement and freeze layer contracts for `raw_station`, `clean_station`, curated metric station datasets, aggregated datasets, and published release datasets.
- [ ] Add versioned JSON schemas in `schemas/` for each dataset and grain.
- [ ] Define required metadata columns and nullable policy in schema files (no sentinel leakage in numeric outputs).
- [ ] Define station identity contract (`station_id`, `station_usaf`, `station_wban`) and source identity contract (`meta_source_file_name`, `meta_source_year`).
- [ ] Add uniqueness constraints for natural key and `record_id` at observation grains.
- [ ] Add schema migration notes for every backward-incompatible contract change.

## P3: manifests, lineage, and storage reliability

- [ ] Add `manifests/ingestion/<run_id>.parquet` (one row per station-year pull attempt).
- [ ] Add `manifests/dataset/<layer>/<snapshot_id>.json` with schema version, partition spec, row/file counts, null rates, and checksums.
- [ ] Add lineage tracking fields and manifest graph (raw -> clean -> curated -> aggregated -> published).
- [ ] Add deterministic parquet write settings and sort behavior for reproducible outputs.
- [ ] Add atomic write flow (temp write -> checksum verify -> commit marker).
- [ ] Add compaction plan for clean/curated/aggregated layers to control tiny files.
- [ ] Replace mutable-only station status booleans with manifest-derived run status views (keep booleans temporarily for compatibility).
- [ ] Add upload retry/resume and partial-failure handling for object-store publishing.

## P4: CLI/API contract hardening and run orchestration

- [ ] Keep existing commands stable (`file-list`, `location-ids`, `pick-location`, `clean-parquet`, `process-location`) until deprecation windows are published.
- [ ] Add/finish commands: `ingest-raw`, `build-clean-station`, `build-curated`, `build-aggregates`, `validate`, `publish-release`, `run --config`.
- [ ] Add explicit deprecation policy for command and argument changes in README.
- [ ] Document idempotency and overwrite behavior per command.
- [ ] Implement run IDs and structured logging context in all pipeline entry points.
- [ ] Add minimal stable API functions: `build_file_index`, `build_station_registry`, `build_clean_station`, `build_curated_station`, `build_aggregates`, `publish_release`, `run_pipeline`.

## P5: quality usability and user-facing utility datasets

- [ ] Add row-level and station-level usability signals (`row_has_any_usable_metric`, coverage percentages, quality score/tier).
- [ ] Ensure aggregates include completeness metadata (`obs_count`, `usable_obs_count`, `coverage_pct`).
- [ ] Add curated-derived metrics (dual units, humidity/comfort metrics, wind utility metrics, precipitation intensity where valid).
- [ ] Add completeness outputs: `station_completeness_daily`, `station_completeness_monthly`, `station_quality_monthly`.
- [ ] Add metadata tables: `dim_station`, `dim_variable`, `fact_station_coverage_daily`, `fact_station_quality_monthly`, `fact_processing_runs`, `dim_dataset_release`.
- [ ] Add machine-readable dataset catalog and sample query/notebook assets.

## P6: validation, testing, and CI governance

- [ ] Add Pandera-based runtime validation profiles for clean/curated/aggregated writes.
- [ ] Add schema contract tests against versioned JSON schemas.
- [ ] Add dataset-level contract tests under `tests/contract/` or `tests/contracts/` (pick one path and standardize).
- [ ] Add regression links to open items in `NEXT_STEPS.md`.
- [ ] Add property-based tests (Hypothesis) for malformed/edge NOAA encodings.
- [ ] Add deterministic smoke-test fixture and expected outputs for CI.
- [ ] Add GitHub Actions for lint, type-check, tests, schema contracts, manifest validation, and smoke pipeline run.
- [ ] Require validation-report generation on release branches before tagging.

## P7: publication and DOI release workflow

- [ ] Implement `publish-release` workflow that builds immutable `published/release=vX.Y.Z/` artifacts.
- [ ] Include required release artifacts: parquet snapshots, dataset manifests, `checksums.sha256`, schema bundle, `DATA_DICTIONARY.md`, `README_RELEASE.md`, `CHANGELOG_DATASET.md`, `CITATION.cff`, `LICENSE`, `PROVENANCE.md`.
- [ ] Add semantic version policy for dataset releases (major/minor/patch compatibility rules).
- [ ] Add automated release packaging for GitHub Release outputs.
- [ ] Add Zenodo deposition metadata template and DOI linkage process.
- [ ] Add release validation checks that block publish when manifests/checksums/citation artifacts are missing.

## P8: methods paper readiness and evidence artifacts

- [ ] Finalize methods outline tied to implemented pipeline stages.
- [ ] Run validation experiments: parse fidelity, coverage deltas, QC attrition, cross-source comparisons, reproducibility reruns.
- [ ] Run scaling benchmarks by station count and year window.
- [ ] Produce paper figures (architecture DAG, coverage, QC waterfall, scaling).
- [ ] Produce paper tables (schema summary, QC policy matrix, validation thresholds, release diffs).
- [ ] Add reproducibility appendix with exact config, versions, manifests, and checksums.

## P9: PR-sized execution order

- [ ] PR 1: Add `config.py`, `configs/runs/`, and `run --config`.
- [ ] PR 2: Add `run_id` + structured logging context across CLI and pipeline.
- [ ] PR 3: Add deterministic/atomic parquet writer helpers and normalized partition utilities.
- [ ] PR 4: Add ingestion manifest writer and manifest-derived station status view.
- [ ] PR 5: Add schema set under `schemas/` and enforce clean write contracts.
- [ ] PR 6: Implement `build-clean-station` writer with natural-key + `record_id` uniqueness checks.
- [ ] PR 7: Implement `build-curated` (with compatibility alias `build-metric-stations`) and first curated datasets.
- [ ] PR 8: Replace aggregation placeholder with `build-aggregates` outputs and aggregation metadata.
- [ ] PR 9: Add Pandera validation profiles, contract tests, and `validate` command.
- [ ] PR 10: Add completeness/quality summary tables and metadata dimension/fact tables.
- [ ] PR 11: Add dataset manifest builder, lineage graph, and checksum generation.
- [ ] PR 12: Add CI workflows for lint/type/test/smoke/schema/manifest gates.
- [ ] PR 13: Add `publish-release` packaging flow and release artifact docs.
- [ ] PR 14: Run bounded dry-run release candidate, publish validation report, and capture follow-up fixes.
