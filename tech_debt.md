# Tech debt: architecture, productization, and publication checklist

## Priority recommendation: `NEXT_STEPS.md` vs `tech_debt.md`

- [ ] Adopt working split: spend ~70% effort on `NEXT_STEPS.md` and ~30% on `tech_debt.md` until `NEXT_STEPS.md` P0/P1 is complete.
- [ ] Treat `NEXT_STEPS.md` as correctness gate: do not publish broad releases until remaining ISD alignment items are resolved or explicitly documented as known limitations.
- [ ] Start `tech_debt.md` tasks in parallel only when they are low-risk scaffolding (config, manifests, CI, contracts) that does not change cleaning semantics.
- [ ] Shift to ~50/50 split once `NEXT_STEPS.md` P0 is complete and parser outputs are stable.
- [ ] Shift to ~30/70 (favoring `tech_debt.md`) once remaining `NEXT_STEPS.md` items are mostly validation hardening and no longer blocking schema contracts.
- [ ] Revisit this recommendation after each milestone release and adjust based on blocker type (data correctness blocker = prioritize `NEXT_STEPS.md`; packaging/release blocker = prioritize `tech_debt.md`).

## P0: repository architecture and module boundaries (incremental refactor only)

- [ ] Keep existing `src/noaa_climate_data/` package and migrate incrementally (no big-bang rewrite).
- [ ] Split current responsibilities into explicit modules: `ingest`, `parse_qc`, `transform`, `aggregate`, `storage`, `publish`, `validation`.
- [ ] Keep `constants.py`, `cleaning.py`, and `pipeline.py` as compatibility facades while extracting internals gradually.
- [ ] Introduce `src/noaa_climate_data/api.py` as the stable public API surface.
- [ ] Define internal/private helpers with `_` prefix and keep them out of public docs.
- [ ] Replace direct script-style orchestration with thin CLI commands that call service functions.
- [ ] Move one-off root scripts (`rerun_stations.py`, `check_station_sync.py`) into `scripts/` and/or packaged commands.
- [ ] Add `config.py` and central run config loading to avoid hardcoded paths and magic defaults.

## P1: public API and CLI contract hardening

- [ ] Keep existing CLI commands stable: `file-list`, `location-ids`, `pick-location`, `clean-parquet`, `process-location`.
- [ ] Add new CLI commands: `build-clean-station`, `build-metric-stations`, `build-aggregates`, `validate`, `publish-release`, `run --config`.
- [ ] Define minimal Python API entrypoints (`build_file_index`, `build_station_registry`, `build_clean_station`, `build_metric_station`, `build_aggregates`, `publish_release`, `run_pipeline`).
- [ ] Add deprecation policy for command/argument changes and document in README.
- [ ] Add idempotency guarantee notes for each CLI step (re-run behavior and overwrite rules).

## P2: dataset layering and schema contracts

- [ ] Implement canonical `clean_station` parquet dataset as the superset truth layer.
- [ ] Implement metric-specific station datasets (`temperature_station`, `wind_station`, `dew_station`, etc.) derived strictly from `clean_station`.
- [ ] Implement aggregation layers per metric (`daily_summary`, `monthly_summary`, `yearly_summary`, `monthly_normals`, `extremes`).
- [ ] Define contract files in `data_contracts/` for each dataset (schema, keys, granularity, required columns).
- [ ] Standardize naming convention: snake_case and explicit unit suffixes (e.g., `_c`, `_f`, `_ms`, `_kt`, `_hpa`, `_pct`, `_m`).
- [ ] Standardize missingness representation: nulls only in numeric outputs (no sentinel leakage).
- [ ] Add required provenance columns across datasets (`run_id`, `dataset_version`, `code_version`, `processed_at_utc`, `source_year`).
- [ ] Standardize station identity columns (`station_id`, `station_usaf`, `station_wban`, `source_file_name`).
- [ ] Add deterministic primary key strategy (`record_id` hash) for observation-level layers.
- [ ] Add dataset-level uniqueness checks for primary key contracts.

## P3: QC model and usability signals

- [ ] Preserve raw NOAA quality fields in canonical outputs for auditability.
- [ ] Add derived QC fields per metric (`*_qc_pass`, `*_qc_status`, `*_usable`).
- [ ] Add row-level confidence indicator (e.g., `row_confidence_score`, `row_has_any_usable_metric`).
- [ ] Add station-day and station-month coverage percentages.
- [ ] Ensure aggregation includes completeness metadata (`obs_count`, `usable_obs_count`, `coverage_pct`).
- [ ] Document quality policy distinctions: raw flags vs derived QC vs usable masks.

## P4: storage layout, partitioning, and object-store publishing

- [ ] Migrate output target from per-station CSV folders to parquet-first layered output structure.
- [ ] Partition observation datasets by `year`, `month`, and stable `station_bucket` (hash bucket).
- [ ] Avoid partitioning by raw `station_id` to prevent tiny-file explosion.
- [ ] Partition aggregate datasets by `metric` + temporal grain (`year`, `month`, baseline window where applicable).
- [ ] Add deterministic sort + parquet writer settings to produce reproducible files.
- [ ] Add manifest writer for each run with row counts, partitions, and min/max timestamps.
- [ ] Add object-store publish adapter (Supabase bucket compatible) with dry-run mode.
- [ ] Add retry/resume and partial-failure handling for uploads.

## P5: derived fields and end-user utility upgrades

- [ ] Add dual-unit conversions where applicable (`temperature_f`, `wind_speed_kt`, `wind_speed_mph`, etc.).
- [ ] Add humidity and comfort metrics (`relative_humidity_pct`, `heat_index_c/f`, `wind_chill_c/f`).
- [ ] Add metric-level usability indicators for user filtering.
- [ ] Add station-level quality summary tables (coverage and confidence rollups).
- [ ] Add metadata tables: `station_metadata`, `variable_dictionary`, `unit_dictionary`, `qc_dictionary`, `aggregation_dictionary`.
- [ ] Add query/discovery assets: dataset catalog manifest, sample SQL/DuckDB queries, quickstart notebook(s).

## P6: reproducibility, validation, and CI governance

- [ ] Add run configs under `configs/runs/` (`ci_smoke`, production ranges).
- [ ] Pin and lock dependencies with Poetry and enforce lockfile in CI.
- [ ] Add schema/data validation layer (Pandera preferred) in pipeline + CI gates.
- [ ] Add property-based tests (Hypothesis) for malformed NOAA encodings and edge cases.
- [ ] Add dataset-level contract tests in `tests/contracts/`.
- [ ] Add CI workflow for lint, type-check, tests, sample pipeline run, schema validation.
- [ ] Add run manifest including per-station status, failure reason, retries, durations, and output locations.
- [ ] Add structured logging for pipeline stages and station-level outcomes.
- [ ] Add non-flaky smoke test dataset and deterministic expected outputs.

## P7: publication-ready data artifact plan

- [ ] Define release bundle structure for each dataset version.
- [ ] Include data artifacts, schema files, manifests, checksums, changelog, license, and citation metadata in release bundle.
- [ ] Generate `SHA256SUMS.txt` for all published files.
- [ ] Add `CHANGELOG_DATASET.md` with explicit schema/data/QC changes by version.
- [ ] Add `CITATION.cff` and “How to cite” section in root README.
- [ ] Add dataset docs set: `README`, data dictionary, methodology, limitations, known issues.
- [ ] Add semantic version policy for both code and dataset (with compatibility rules).
- [ ] Automate GitHub Release packaging for datasets.
- [ ] Prepare Zenodo metadata for DOI minting (concept DOI + version DOI).

## P8: methods paper readiness and validation evidence

- [ ] Create methods paper outline aligned to implemented pipeline stages.
- [ ] Run validation experiment: station/time coverage before vs after cleaning.
- [ ] Run validation experiment: parse/QC error rates by field and station.
- [ ] Run validation experiment: aggregated metric comparison against NOAA summary references where available.
- [ ] Run validation experiment: reproducibility reruns with checksum equivalence.
- [ ] Run runtime scaling benchmark across station counts and year windows.
- [ ] Produce figure set: station coverage map, missingness heatmap, QC distribution, runtime scaling curve.
- [ ] Produce table set: schema summary, QC policy matrix, aggregation function matrix, validation metrics.
- [ ] Add reproducibility appendix describing exact config, versions, and run manifests.

## P9: execution order (PR-sized backlog)

- [ ] PR 1: Add `config.py` + `configs/runs/` and `run --config` entrypoint.
- [ ] PR 2: Add storage utilities (`parquet_writer`, `partitioning`) with deterministic write options.
- [ ] PR 3: Add `build-clean-station` command and initial `clean_station` parquet writer.
- [ ] PR 4: Add metric registry config + `build-metric-stations` command.
- [ ] PR 5: Replace `aggregate-parquet` placeholder with real aggregation pipeline from cleaned parquet.
- [ ] PR 6: Add metadata dictionary table builders.
- [ ] PR 7: Add validation contracts (Pandera) and `validate` command.
- [ ] PR 8: Add manifest/catalog/checksum generation and tests.
- [ ] PR 9: Add CI workflows for lint/type/test/smoke/contracts.
- [ ] PR 10: Add release docs/assets (`CITATION.cff`, dataset changelog, release process, Zenodo metadata template).

