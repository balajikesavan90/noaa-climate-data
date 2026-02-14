# NOAA ISD Data-Cleaning Alignment Report

Generated: 2026-02-14

Scope reviewed:
- NOAA documentation split files: `isd-format-document-parts/part-01-...md` through `isd-format-document-parts/part-30-...md`
- Cleaning implementation: `src/noaa_climate_data/cleaning.py`, `src/noaa_climate_data/constants.py`
- Cleaning/aggregation tests: `tests/test_cleaning.py`, `tests/test_aggregation.py`, `tests/test_integration.py`

Test execution in this review:
- `poetry run pytest tests/test_cleaning.py -q` -> `250 passed`
- `poetry run pytest tests/test_aggregation.py tests/test_integration.py -q` -> `95 passed, 99 skipped`

## 1) Part-by-Part Alignment / Misalignment

Interpretation used:
- `IDs`: field identifiers documented in each NOAA part (expanded ranges like `AA1-AA4`, `Q01-Q99`, etc.).
- `Implemented`: identifier resolves to `get_field_rule(...)`, or has dedicated parser logic (`REM`, `QNN`, `ADD` marker handling).
- `Exact tests`: identifier appears directly in `tests/test_cleaning.py` assertions/calls.

| Part | NOAA Section | IDs | Implemented | Exact tests | Alignment | Misalignment |
|---|---|---:|---:|---:|---|---|
| 01 | Preface and overview | 0 | 0 | 0 | Informational section; no element IDs to implement | None found |
| 02 | Control data section | control fields | yes | yes | Latitude/longitude/elevation/source/report/call-sign/QC normalization present (`src/noaa_climate_data/cleaning.py:381`) | Date parsing accepts ISO timestamps, not only `YYYYMMDD` (`src/noaa_climate_data/cleaning.py:367`, `tests/test_cleaning.py:1415`) |
| 03 | Mandatory data section | 6 | 6 | 6 | `WND/CIG/VIS/TMP/DEW/SLP` rules and tests present (`src/noaa_climate_data/constants.py:363`, `tests/test_cleaning.py:31`) | NOAA min/max domains are not strictly enforced for all numeric mandatory values (`src/noaa_climate_data/constants.py:433`, `src/noaa_climate_data/cleaning.py:272`) |
| 04 | Additional data section | 36 | 36 | 15 | `AA*...AP*` covered via prefix rules (`src/noaa_climate_data/constants.py:865`) | Not all documented variants have direct tests; mostly prefix-representative tests only |
| 05 | Weather occurrence data | 27 | 27 | 5 | `AT*/AU*/AX*/AY*/AZ*` mapped in prefix rules (`src/noaa_climate_data/constants.py:1156`, `src/noaa_climate_data/constants.py:2470`) | Limited exact-ID testing depth relative to full documented range |
| 06 | CRN unique data | 15 | 15 | 9 | `CB/CF/CG/CH/CI/CN` implemented (`src/noaa_climate_data/constants.py:2566`, `src/noaa_climate_data/constants.py:2599`) | Some variants only prefix-covered in tests |
| 07 | Network metadata | 9 | 9 | 2 | `CO1` explicit plus `CO*` variants (`src/noaa_climate_data/constants.py:842`) | `CO3-CO9` not directly tested |
| 08 | CRN control section | 1 | 1 | 1 | `CR1` implemented and tested (`src/noaa_climate_data/constants.py:2554`) | None found |
| 09 | Subhourly temperature section | 3 | 3 | 1 | `CT*` implemented through prefix mapping | `CT2/CT3` not directly tested |
| 10 | Hourly temperature section | 3 | 3 | 1 | `CU*` implemented through prefix mapping | `CU2/CU3` not directly tested |
| 11 | Hourly temperature extreme section | 3 | 3 | 1 | `CV*` implemented through prefix mapping | `CV2/CV3` not directly tested |
| 12 | Subhourly wetness section | 1 | 1 | 1 | `CW1` implemented and tested | None found |
| 13 | Hourly geonor summary | 3 | 3 | 1 | `CX*` implemented through prefix mapping | `CX2/CX3` not directly tested |
| 14 | Runway visual range | 1 | 1 | 1 | `ED1` implemented and tested (`src/noaa_climate_data/constants.py:2408`) | None found |
| 15 | Cloud and solar data | 21 | 21 | 4 | `GA*/GD*/GE1/GF1/GG*/GH*` implemented | `GD*` and `GH1` lack direct cleaning tests |
| 16 | Sunshine observation | 3 | 3 | 1 | `GJ/GK/GL` rules implemented (`src/noaa_climate_data/constants.py:1892`) | `GK1` and `GL1` not directly tested |
| 17 | Solar irradiance | 2 | 2 | 0 | `GM/GN` rules implemented (`src/noaa_climate_data/constants.py:1925`, `src/noaa_climate_data/constants.py:1959`) | No direct cleaning tests for `GM1/GN1` |
| 18 | Net solar radiation | 1 | 1 | 0 | `GO` rule implemented (`src/noaa_climate_data/constants.py:1995`) | No direct cleaning tests for `GO1` |
| 19 | Modeled solar irradiance | 1 | 1 | 1 | `GP1` implemented and tested (`src/noaa_climate_data/constants.py:2019`, `tests/test_cleaning.py:989`) | None found |
| 20 | Hourly solar angle | 1 | 1 | 1 | `GQ1` implemented and tested (`src/noaa_climate_data/constants.py:2034`, `tests/test_cleaning.py:1002`) | None found |
| 21 | Hourly extraterrestrial radiation | 1 | 1 | 1 | `GR1` implemented and tested (`src/noaa_climate_data/constants.py:2052`, `tests/test_cleaning.py:1013`) | None found |
| 22 | Hail data | 1 | 1 | 1 | `HAIL` implemented and tested (`src/noaa_climate_data/constants.py:2070`) | None found |
| 23 | Ground surface data | 5 | 5 | 4 | `IA/IB/IC` implemented (`src/noaa_climate_data/constants.py:2081`) | `IB2` not directly tested |
| 24 | Temperature data | 15 | 15 | 7 | `KA/KB/KC/KD/KE/KF/KG` implemented | Several documented variants only prefix-covered in tests |
| 25 | Sea surface temperature | 1 | 1 | 1 | `SA1` implemented and tested (`src/noaa_climate_data/constants.py:524`) | None found |
| 26 | Soil temperature | 1 | 1 | 1 | `ST1` implemented and tested (`src/noaa_climate_data/constants.py:1727`) | None found |
| 27 | Pressure data | 7 | 7 | 6 | `MA/MD/ME/MF/MG/MH/MK` implemented (`src/noaa_climate_data/constants.py:478`) | `MH1` not directly tested |
| 28 | Weather occurrence extended | 14 | 14 | 2 | `MV*/MW*` implemented (`src/noaa_climate_data/constants.py:2436`) | Only `MV1`/`MW1` directly tested |
| 29 | Wind data | 16 | 16 | 7 | `OA/OB/OC/OD/OE/RH` implemented (`src/noaa_climate_data/constants.py:2220`) | Higher-number variants rely on prefix coverage, not exact tests |
| 30 | Marine + remarks + EQD + original obs | 604 | 604 | 9 | `UA/UG/WA/WD/WG/WJ`, `REM`, `QNN`, and `Q/P/R/C/D/N` EQD prefixes implemented (`src/noaa_climate_data/constants.py:2721`, `src/noaa_climate_data/cleaning.py:470`) | Very limited exact-ID tests for the large EQD range (`Q01-Q99`, etc.) from docs (`isd-format-document-parts/part-30-marine-data.md:794`) |

## 2) Confirmed Misalignments with NOAA Docs

1. Control date format is more permissive than NOAA spec.
   - NOAA Part 2 defines date as `YYYYMMDD` (`isd-format-document-parts/part-02-control-data-section.md:33`).
   - Cleaner accepts any parseable datetime string (including ISO timestamps) (`src/noaa_climate_data/cleaning.py:367`), and this behavior is explicitly tested (`tests/test_cleaning.py:1415`).

2. Control QC process normalization accepts/truncates non-spec lengths.
   - NOAA Part 2 defines QC process codes `V01/V02/V03` (`isd-format-document-parts/part-02-control-data-section.md:179`).
   - Cleaner falls back to `series.str.slice(0, 3)` when full value not recognized (`src/noaa_climate_data/cleaning.py:422`), e.g., `V020 -> V02` (`tests/test_cleaning.py:1383`).

3. Mandatory numeric min/max domains are not comprehensively validated.
   - NOAA Part 3 includes strict ranges (e.g., wind direction `001-360`, TMP `-0932..+0618`, SLP `08600..10900`) (`isd-format-document-parts/part-03-mandatory-data-section.md:25`, `isd-format-document-parts/part-03-mandatory-data-section.md:200`, `isd-format-document-parts/part-03-mandatory-data-section.md:275`).
   - In code, range checks only occur when `allowed_values`/`allowed_pattern` are defined (`src/noaa_climate_data/cleaning.py:272`), but `TMP/DEW/SLP` rules do not declare such constraints (`src/noaa_climate_data/constants.py:433`).

4. Additional numeric field width/range constraints are not consistently enforced.
   - Example: Part 4 precipitation depth domain is fixed-width with max `9998` (`isd-format-document-parts/part-04-additional-data-section.md:51`).
   - `AA*` rule uses sentinel/scale but no explicit `allowed_values`/pattern for width/range (`src/noaa_climate_data/constants.py:866`), so malformed-width numerics can pass parser-level checks.

5. Several documented sections are implemented but under-tested at exact-ID level.
   - No direct cleaning tests for Part 17 (`GM1/GN1`) and Part 18 (`GO1`) despite rule definitions (`src/noaa_climate_data/constants.py:1925`, `src/noaa_climate_data/constants.py:1995`).
   - Part 30 documents large EQD ranges (`Q01-Q99`, `P01-P99`, `R01-R99`, `C01-C99`, `D01-D99`, `N01-N99`) (`isd-format-document-parts/part-30-marine-data.md:794`), but direct tests cover only small samples (`tests/test_cleaning.py:971`, `tests/test_cleaning.py:976`).

## 3) Strong Alignments

1. NOAA identifier coverage is complete for reviewed parts.
   - All extracted IDs from Parts 3-30 resolve to implementation support (direct rule, prefix rule, or dedicated parser behavior).

2. Sentinel handling, scaling, and quality gating are robust and well tested.
   - Core logic in `src/noaa_climate_data/cleaning.py:267` and wide field assertions in `tests/test_cleaning.py:25`.

3. Marine remarks and original-observation structures are explicitly represented.
   - `REM` parsing aligns with documented remark types (`isd-format-document-parts/part-30-marine-data.md:735`) via `REM_TYPE_CODES` and parser logic (`src/noaa_climate_data/constants.py:272`, `src/noaa_climate_data/cleaning.py:127`).
   - `QNN` and EQD prefix families are implemented (`src/noaa_climate_data/cleaning.py:140`, `src/noaa_climate_data/constants.py:2721`).
