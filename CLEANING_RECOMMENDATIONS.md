# Data Cleaning Recommendations

## Background

The original R pipeline pulled **only TMP** (temperature), parsed its 2-part comma encoding, applied the ÷10 scale factor, filtered bad quality flags, and carried a single clean `Temperature` column through aggregation.

The Python rewrite generalised this with `clean_noaa_dataframe` — it auto-detects every comma-encoded column and expands them. This is powerful but introduces several correctness and usability issues documented below.

---

## P0 — Data Correctness (current outputs have wrong values)

- [x] **Fix missing-value sentinels leaking into numeric means** ✅
  - `_is_missing_value` in `cleaning.py` now checks per-field `missing_values` sets from `FIELD_RULES` (all-9s sentinels covered where specified). Verified: fresh cleaning of raw data produces zero leaked sentinels.
  - ⚠️ On-disk output files in `output/` are **stale** and must be re-generated to reflect this fix.

- [x] **Add scale factors for all fields that need ÷10** ✅
  - `FIELD_RULES` in `constants.py` now defines `scale=0.1` for all fields below. Verified: WND speed outputs ~3–11 m/s, OC1 gust ~8–17 m/s, MA1 altimeter ~970–1005 hPa when cleaned fresh.

  | Field | Part(s) | Meaning | Current output artefact |
  |-------|---------|---------|------------------------|
  | WND | part4 (speed) | m/s | Values 10× too large |
  | OC1 | value (gust speed) | m/s | Values 10× too large |
  | MA1 | part1 (altimeter), part3 (station pressure) | hPa | Values 10× too large |
  | KA1/KA2 | part1 (period), part3 (temperature) | hours / °C | Both 10× too large |
  | MD1 | part3 (3hr Δp), part5 (24hr Δp) | hPa | Values 10× too large |
  | OD1/OD2 | part4 (speed) | m/s | Values 10× too large |
  | SA1 | value (SST) | °C | Values 10× too large |
  | UA1 | part3 (wave height) | m | Values 10× too large |
  | UG1 | part2 (swell height) | m | Values 10× too large |

- [x] **Per-value quality-flag mapping for multi-part fields** ✅
  - `_quality_for_part` in `cleaning.py` now reads `quality_part` from each `FieldPartRule` to apply the correct quality flag per value. Verified: WND bad-direction-quality nulls direction but preserves speed; WND bad-speed-quality nulls speed but preserves direction; MA1 bad-station-pressure-quality nulls station pressure but preserves altimeter.

- [x] **Align missing sentinels to ISD spec for VIS and MD1** ✅
  - VIS distance missing should be `999999` only (ISD mandatory section). Remove `9999` from VIS missing set.
  - MD1 24-hour pressure change missing should be `+999` (ISD pressure section). Replace `9999` with `999` for part5.

- [x] **Fix OD* part ordering to match ISD spec** ✅
  - OD fields are ordered: type, period, direction, speed, speed-quality. Map part3 to direction, part4 to speed (scale 0.1), and part5 to speed-quality for filtering.

---

## P1 — Aggregation Correctness

- [x] **Exclude categorical codes from numeric aggregation** ✅
  - `FieldPartRule` now carries `kind="categorical"` and `agg="drop"` for all WMO/ISD category codes. `is_categorical_column` and `get_agg_func` in `constants.py` classify columns; `_aggregate_numeric`, `_weighted_aggregate`, and `_daily_min_max_mean` in `pipeline.py` exclude them. Quality columns (`*__quality`, `*__qc`) are also dropped from aggregated output.
  - These columns are WMO/ISD category codes, not continuous measurements. Averaging them is meaningless:

  | Column | What it is | Current yearly "mean" |
  |--------|-----------|----------------------|
  | `present_weather_code_1` | Present-weather code (WMO 4677, 00–99) | ~15.4 (nonsensical) |
  | `present_weather_code_2` | Second weather code | ~65.9 (nonsensical) |
  | `WND__part3` | Wind type code (N/C/V/9) | 9.0 (coerced string) |
  | `CIG__part3` | Ceiling determination code | 9.0 |
  | `CIG__part4` | CAVOK code | coerced |
  | `VIS__part3` | Variability code | coerced |
  | `AY1/AY2` parts | Past-weather condition codes | coerced |
  | `MD1__part1` | Pressure tendency code (0–8) | coerced |
  | `GE1__part1` | Convective cloud code | coerced |

- [x] **Use field-appropriate aggregation functions instead of universal mean** ✅
  - `FieldPartRule.agg` now encodes the preferred function per field-part. `_aggregate_numeric` builds a per-column `agg_spec` and delegates to `groupby().agg()` with mixed functions (mean / max / min / sum) plus a mode fallback. Verified with 19 unit tests.
  - Temperature, dew point, pressure → **mean** ✓
  - Wind speed → **mean** ✓
  - Wind gust (OC1) → **max** ✓
  - Precipitation (AA1–AA4 if added) → **sum** (ready when fields are added)
  - Visibility → **min** ✓ (worst visibility is climatologically significant)
  - Sky coverage (GA oktas, GF1 total coverage) → **mean** ✓
  - Weather codes (MW, AY) → **drop** ✓ (excluded from numeric aggregation)
  - Extreme temperatures (KA) → **mean** (min-of-min / max-of-max deferred to P3 multi-occurrence handling)

- [x] **Exclude per-part quality codes from aggregation** ✅
  - WND part2/part5, CIG part2, VIS part4, and other multi-part quality fields now use `kind="categorical"` / `agg="drop"` so aggregation ignores them.

---

## P2 — Researcher Usability

- [x] **Rename expanded columns to human-readable names** ✅
  - `WND__part4` → `wind_speed_ms`
  - `WND__part1` → `wind_direction_deg`
  - `CIG__part1` → `ceiling_height_m`
  - `VIS__part1` → `visibility_m`
  - `TMP__value` → `temperature_c`
  - `DEW__value` → `dew_point_c`
  - `SLP__value` → `sea_level_pressure_hpa`
  - `OC1__value` → `wind_gust_ms`
  - `MA1__part1` → `altimeter_setting_hpa`
  - `MA1__part3` → `station_pressure_hpa`
  - `KA*__part3` → `extreme_temp_c_<n>` (paired with `extreme_temp_type_<n>` from part2)
  - `MW*__value` → `present_weather_code_<n>`
  - etc.

- [x] **Create a `FIELD_REGISTRY` dataclass/dict in `constants.py`** ✅
  - Each entry encodes: field code, part index, human-readable name, type (`numeric` / `categorical` / `quality`), scale factor, missing-value sentinel, which quality-flag part governs it, and preferred aggregation function.
  - This replaces both `FIELD_SCALES` and the generic part-numbering logic in `_expand_parsed`.

- [x] **Drop quality-flag and raw-code columns from aggregated outputs** ✅
  - Quality columns (`*__quality`, `*__qc`) and type/determination codes are observation-level metadata. They remain in `LocationData_Cleaned.csv` but are explicitly removed from monthly/yearly aggregation.

- [x] **Add unit-conversion options** ✅
  - Optional `--add-unit-conversions` flag adds `_f`, `_kt`, `_mph`, `_mi`, `_inhg` columns; metric remains the default.

---

## P3 — Expand Research Value

See [P3_EXPAND_RESEARCH_VALUE.md](P3_EXPAND_RESEARCH_VALUE.md) for the expanded plan and research-facing deliverables.

---

## P4 — NOAA Alignment

- [x] **Include full NOAA quality-code domain (excluding erroneous 3, 7)** ✅
  - Accept 0–2, 4–6, and 9 in addition to manual QC flags (A/C/I/M/P/R/U); keep 3 and 7 filtered as erroneous.

- [x] **Handle variable wind direction** ✅
  - Treat `WND` direction `999` as "variable" when type code is `V` instead of missing.

- [x] **Expand field rules beyond current subset** ✅
  - Add rules for additional mandatory/additional sections with correct scales, sentinels, and quality mappings.

- [x] **Document aggregation as a derived analysis layer** ✅
  - Make explicit that monthly/yearly aggregation is not part of NOAA spec and is a project-specific analytic choice.

- [x] **Update README to match ISD + code behavior** ✅
  - Quality flags should include 2 and 6 (ISD allows them), WND direction uses circular mean, VIS missing is `999999` only, and MD1 24-hour missing is `+999`.

- [x] **Only emit `__quality` columns when the ISD field defines a single quality part** ✅
  - Multi-part fields like CIG now emit `__quality` from the defined quality part, and fields with multiple quality parts (e.g. WND) no longer emit `__quality`.

---

## P5 — Test Coverage

- [x] **Add coverage for pipeline aggregation branches** ✅
  - Tests for `fixed_hour`, `weighted_hours`, `daily_min_max_mean`, and `hour_day_month_year` strategies.

- [x] **Add edge-case tests for cleaning quality and missing values** ✅
  - Cover `invalid_quality` behavior, per-part quality flags, and sentinel handling in `clean_noaa_dataframe`.

- [x] **Add tests for field-specific aggregation rules** ✅
  - Assert min/max/sum/drop/mode behavior from `FieldPartRule.agg` on representative columns.

- [x] **Add tests for NOAA client and CLI paths** ✅
  - Minimal mocks to exercise `noaa_client` and `cli` workflows without network access.

---

## Reference — ISD Field Structure

| Field | Parts | Key value part(s) | Scale | Missing | Quality part(s) | Type |
|-------|-------|-------------------|-------|---------|-----------------|------|
| WND | 5 | 1=direction, 4=speed | 1, 0.1 | 999, 9999 | 2, 5 | numeric |
| CIG | 4 | 1=height | 1 | 99999 | 2 | numeric |
| VIS | 4 | 1=distance | 1 | 999999 | 2 | numeric |
| TMP | 2 | 1=temperature | 0.1 | 9999 | 2 | numeric |
| DEW | 2 | 1=dew point | 0.1 | 9999 | 2 | numeric |
| SLP | 2 | 1=pressure | 0.1 | 99999 | 2 | numeric |
| OC1 | 2 | 1=gust speed | 0.1 | 9999 | 2 | numeric |
| MA1 | 4 | 1=altimeter, 3=stn press | 0.1, 0.1 | 99999, 99999 | 2, 4 | numeric |
| KA* | 4 | 1=period, 3=temperature | 0.1, 0.1 | 999, 9999 | 4 | numeric |
| MD1 | 6 | 3=3hr Δp, 5=24hr Δp | 0.1, 0.1 | 999, +999 | 4, 6 | numeric |
| OD* | 5 | 3=direction, 4=speed, 5=speed-quality | 1, 0.1 | 999, 9999 | 5 | numeric |
| GA* | 6 | 1=coverage, 3=base height | 1, 1 | 99, 99999 | 2, 4, 6 | mixed |
| GF1 | 13 | 1=total cov, 8=base ht | 1, 1 | 99, 99999 | 3, 5, 7, 9, 11, 13 | mixed |
| MW* | 2 | 1=weather code | — | — | 2 | categorical |
| AY* | 4 | 1=condition, 3=period | —, 1 | —, 99 | 2, 4 | categorical |
| SA1 | 2 | 1=SST | 0.1 | 999 | 2 | numeric |
| UA1 | 6 | 2=period, 3=wave ht | 1, 0.1 | 99, 999 | 4 | numeric |
| UG1 | 4 | 1=period, 2=swell ht | 1, 0.1 | 99, 999 | 4 | numeric |
