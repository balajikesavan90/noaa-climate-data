# Data Cleaning Recommendations

## Background

The original R pipeline pulled **only TMP** (temperature), parsed its 2-part comma encoding, applied the ÷10 scale factor, filtered bad quality flags, and carried a single clean `Temperature` column through aggregation.

The Python rewrite generalised this with `clean_noaa_dataframe` — it auto-detects every comma-encoded column and expands them. This is powerful but introduces several correctness and usability issues documented below.

---

## P0 — Data Correctness (current outputs have wrong values)

- [x] **Fix missing-value sentinels leaking into numeric means** ✅
  - `_is_missing_value` in `cleaning.py` now checks per-field `missing_values` sets from `FIELD_RULES` (999, 9999, 99999, 999999 all covered). Verified: fresh cleaning of raw data produces zero leaked sentinels.
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
  | OD1/OD2 | part3 (speed) | m/s | Values 10× too large |
  | SA1 | value (SST) | °C | Values 10× too large |
  | UA1 | part3 (wave height) | m | Values 10× too large |
  | UG1 | part2 (swell height) | m | Values 10× too large |

- [x] **Per-value quality-flag mapping for multi-part fields** ✅
  - `_quality_for_part` in `cleaning.py` now reads `quality_part` from each `FieldPartRule` to apply the correct quality flag per value. Verified: WND bad-direction-quality nulls direction but preserves speed; WND bad-speed-quality nulls speed but preserves direction; MA1 bad-station-pressure-quality nulls station pressure but preserves altimeter.

---

## P1 — Aggregation Correctness

- [ ] **Exclude categorical codes from numeric aggregation**
  - These columns are WMO/ISD category codes, not continuous measurements. Averaging them is meaningless:

  | Column | What it is | Current yearly "mean" |
  |--------|-----------|----------------------|
  | `MW1__value` | Present-weather code (WMO 4677, 00–99) | ~15.4 (nonsensical) |
  | `MW2__value` | Second weather code | ~65.9 (nonsensical) |
  | `WND__part3` | Wind type code (N/C/V/9) | 9.0 (coerced string) |
  | `CIG__part3` | Ceiling determination code | 9.0 |
  | `CIG__part4` | CAVOK code | coerced |
  | `VIS__part3` | Variability code | coerced |
  | `AY1/AY2` parts | Past-weather condition codes | coerced |
  | `MD1__part1` | Pressure tendency code (0–8) | coerced |
  | `GE1__part1` | Convective cloud code | coerced |

- [ ] **Use field-appropriate aggregation functions instead of universal mean**
  - Temperature, dew point, pressure → **mean** ✓
  - Wind speed → **mean** + preserve **max** (for max sustained / gust)
  - Wind gust (OC1) → **max**
  - Precipitation (AA1–AA4 if added) → **sum**
  - Visibility → **min** (worst visibility is climatologically significant)
  - Sky coverage (GA oktas, GF1 total coverage) → **mean** is acceptable
  - Weather codes (MW, AY) → **mode** or **frequency counts** per period
  - Extreme temperatures (KA) → **min** of minimums, **max** of maximums

---

## P2 — Researcher Usability

- [ ] **Rename expanded columns to human-readable names**
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
  - `KA*__part3` → `extreme_temp_c` (with min/max qualifier from part2)
  - `MW*__value` → `present_weather_code`
  - etc.

- [ ] **Create a `FIELD_REGISTRY` dataclass/dict in `constants.py`**
  - Each entry encodes: field code, part index, human-readable name, type (`numeric` / `categorical` / `quality`), scale factor, missing-value sentinel, which quality-flag part governs it, and preferred aggregation function.
  - This replaces both `FIELD_SCALES` and the generic part-numbering logic in `_expand_parsed`.

- [ ] **Drop quality-flag and raw-code columns from aggregated outputs**
  - Quality columns (`*__quality`, `*__qc`) and type/determination codes are observation-level metadata. They should remain in `LocationData_Cleaned.csv` but be excluded from monthly/yearly aggregation to reduce noise.

- [ ] **Add unit-conversion options**
  - The old R code converted °C → °F for the charts. Consider a post-cleaning step or CLI flag that adds `_f` columns for temperatures, `_kt` / `_mph` for wind, `_mi` for visibility, `_inhg` for pressure, etc.

---

## P3 — Expand Research Value

- [ ] **Add precipitation fields (AA1–AA4)**
  - Hourly liquid precipitation, mm ÷10, missing = `9999`. Essential for climate research but not currently present in the raw download columns for many stations. The pipeline should look for and parse these when available.

- [ ] **Add snow depth (AJ1)**
  - Snow depth in cm, scale ×1, missing = `9999`. Note: SA1 is **sea-surface temperature**, not snow — this is a common source of confusion.

- [ ] **Add precipitation estimate fields (AU1–AU5)**
  - For stations that lack AA data, AU provides condition codes and estimated precipitation intensity/duration.

- [ ] **Compute derived quantities**
  - With TMP and DEW both cleaned, the pipeline can derive:
    - **Relative humidity (%)** via the Magnus formula
    - **Wet-bulb temperature** (increasingly important for climate-health research)
  - With TMP and WND speed:
    - **Wind chill** (when TMP < 10 °C and speed > 4.8 km/h)
    - **Heat index** (when TMP > 27 °C and RH > 40%)

- [ ] **Handle multi-occurrence fields (GA1–GA6, MW1–MW7, KA1–KA4)**
  - These represent *layers* or *concurrent observations*, not repeated measurements. For sky cover (GA), the pipeline could derive a single "total cloud cover" summary. For extreme temps (KA), separate min vs max into distinct columns based on the code in part2 (`N`=min, `M`=max).

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
| MD1 | 6 | 3=3hr Δp, 5=24hr Δp | 0.1, 0.1 | 999, 9999 | 4, 6 | numeric |
| OD* | 5 | 3=speed, 5=direction | 0.1, 1 | 9999, 999 | 4 | numeric |
| GA* | 6 | 1=coverage, 3=base height | 1, 1 | 99, 99999 | 2, 4, 6 | mixed |
| GF1 | 13 | 1=total cov, 8=base ht | 1, 1 | 99, 99999 | 3, 5, 7, 9, 11, 13 | mixed |
| MW* | 2 | 1=weather code | — | — | 2 | categorical |
| AY* | 4 | 1=condition, 3=period | —, 1 | —, 99 | 2, 4 | categorical |
| SA1 | 2 | 1=SST | 0.1 | 999 | 2 | numeric |
| UA1 | 6 | 2=period, 3=wave ht | 1, 0.1 | 99, 999 | 4 | numeric |
| UG1 | 4 | 1=period, 2=swell ht | 1, 0.1 | 99, 999 | 4 | numeric |
