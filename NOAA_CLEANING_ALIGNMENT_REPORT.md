# NOAA Cleaning Alignment Report (ISD Parts 01-30)

Date: 2026-02-14

## Scope

Compared `isd-format-document-parts/part-01-*.md` through `part-30-*.md` against:

- `src/noaa_climate_data/cleaning.py`
- `src/noaa_climate_data/constants.py`
- `tests/test_cleaning.py`

## Part-by-Part Alignment and Misalignment

| Part | Alignment snapshot | Misalignment snapshot |
| --- | --- | --- |
| 01 Preface | Record/section concepts reflected in pipeline structure. | Record/section length enforcement remains backlog (`NEXT_STEPS.md`). |
| 02 Control | DATE/TIME, lat/lon/elev, source/report/QC normalization is implemented and tested. | No net-new gap from this pass. |
| 03 Mandatory | `WND`, `CIG`, `VIS`, `TMP`, `DEW`, `SLP` decoding, calm/clamp behavior, quality gating are implemented and tested. | Remaining hard min/max enforcement is still a known backlog item. |
| 04 Additional | AA/AP/AJ/AH/AI/etc. groups exist and are quality/sentinel-aware. | No net-new gap from this pass. |
| 05 Weather Occurrence | `AT/AU/AX/AY/AZ/AW` parsing exists with broad test coverage. | New: `AW=99` is treated as missing, but Part 5 defines `99 = Tornado`. |
| 06 CRN Unique | `CB/CF/CG/CH/CI/CN` sections and QC/flag handling are implemented. | No net-new gap from this pass. |
| 07 Network Metadata | `CO1`, `CO2-CO9` support exists with tests. | No net-new gap from this pass. |
| 08 CRN Control | `CR1` parsing and QC handling implemented. | No net-new gap from this pass. |
| 09 Subhourly Temp | `CT1-CT3` implemented and tested. | No net-new gap from this pass. |
| 10 Hourly Temp | `CU1-CU3` implemented and tested. | No net-new gap from this pass. |
| 11 Hourly Temp Extreme | `CV1-CV3` implemented with HHMM checks and QC tests. | No net-new gap from this pass. |
| 12 Subhourly Wetness | `CW1` implemented and tested. | No net-new gap from this pass. |
| 13 Geonor Summary | `CX1-CX3` implemented and tested. | No net-new gap from this pass. |
| 14 Runway Visual Range | `ED1` implemented with domain and quality checks. | No net-new gap from this pass. |
| 15 Cloud and Solar | `GA/GD/GE1/GF1/GG` sections are present with extensive code-domain validation. | No net-new gap from this pass. |
| 16 Sunshine | `GJ/GK/GL` sections implemented and range-tested. | No net-new gap from this pass. |
| 17 Solar Irradiance | `GM1/GN1` parsing and quality domains are implemented. | New: UVB friendly-name mapping still assumes a UVB data-flag part and mislabels UVB quality output. |
| 18 Net Solar Radiation | `GO1` implemented with time-period checks. | No net-new gap from this pass. |
| 19 Modeled Solar Irradiance | `GP1` source flags/uncertainty bounds implemented and tested. | No net-new gap from this pass. |
| 20 Hourly Solar Angle | `GQ1` implemented with QC and period checks. | No net-new gap from this pass. |
| 21 Hourly Extraterrestrial Radiation | `GR1` implemented with QC and period checks. | No net-new gap from this pass. |
| 22 Hail | `HAIL` section implemented with range/quality tests. | No net-new gap from this pass. |
| 23 Ground Surface | `IA/IB/IC` sections implemented with key domain tests. | No net-new gap from this pass. |
| 24 Temperature | `KA/KB/KC/KD/KE/KF/KG` sections implemented and broadly tested. | No net-new gap from this pass. |
| 25 Sea Surface Temp | `SA1` implemented with quality and range checks. | No net-new gap from this pass. |
| 26 Soil Temp | `ST1` implemented with domain/QC checks. | No net-new gap from this pass. |
| 27 Pressure | `MA/MD/ME/MF/MG/MH/MK` sections implemented with domain/QC checks. | No net-new gap from this pass. |
| 28 Weather Extended | `MV/MW` sections implemented with code-domain checks. | No net-new gap from this pass. |
| 29 Wind | `OA/OB/OC/OD/OE/RH` sections implemented and tested. | No net-new gap from this pass. |
| 30 Marine | `UA/UG/WA/WD/WG/WJ/EQD/REM/QNN` sections are present. | New: `QNN` parser does not follow the Part 30 tokenized/repeating layout (`QNN@1234...` + 6-char values). REM length/repeat handling remains already-tracked backlog. |

## Net-New Misalignments Identified

1. AW tornado code is dropped as missing.
   - Spec: `99 = Tornado` in AW code table (`isd-format-document-parts/part-05-weather-occurrence-data.md:330`).
   - Current: `AW` rule sets `missing_values={"99"}` (`src/noaa_climate_data/constants.py:1470`) and tests assert `99` is missing (`tests/test_cleaning.py:987`).

2. GM1 UVB friendly-column mapping is out of sync with parser layout.
   - Current parser/rules use 12 GM parts (UVB value + UVB quality) (`src/noaa_climate_data/constants.py:2222`).
   - Friendly maps still label `GM*__part12` as UVB flag and expect `GM*__part13` as UVB quality (`src/noaa_climate_data/constants.py:3601`, `src/noaa_climate_data/constants.py:3602`), which mislabels outputs.
   - Part 17 field block defines UVB value + quality field (`isd-format-document-parts/part-17-solar-irradiance-section.md:163`, `isd-format-document-parts/part-17-solar-irradiance-section.md:179`).

3. QNN parsing is shape-based and not spec-structured.
   - Spec: explicit tokenized format with repeating element blocks (e.g., `QNN@1234...`) and 6-char data values (`isd-format-document-parts/part-30-marine-data.md:1152`, `isd-format-document-parts/part-30-marine-data.md:1160`, `isd-format-document-parts/part-30-marine-data.md:1193`).
   - Current parser uses regex scan plus leftover-length heuristics (`src/noaa_climate_data/cleaning.py:166`, `src/noaa_climate_data/cleaning.py:178`), and tests only cover simplified free-form examples (`tests/test_cleaning.py:1663`).

## Added to Next Steps

These three items were added to `NEXT_STEPS.md` as new unchecked tasks under `P0`.
