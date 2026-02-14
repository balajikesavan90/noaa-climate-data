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
| 04 Additional | AA/AP/AJ/AH/AI/etc. groups exist and are quality/sentinel-aware. | New: Part 4 `AH/AI` numeric/time ranges are not enforced, and broad prefix matching can accept out-of-domain repeat IDs (for families with fixed limits). |
| 05 Weather Occurrence | `AT/AU/AX/AY/AZ/AW` parsing exists with broad test coverage. | New: exact repeater cardinality is not enforced for several groups (e.g., `AT9`, `AU10`, `AW5`, `AX7`, `AZ3`). |
| 06 CRN Unique | `CB/CF/CG/CH/CI/CN` sections and QC/flag handling are implemented. | New: many documented MIN/MAX bounds in `CI1` and `CN1-CN4` are still not encoded. |
| 07 Network Metadata | `CO1`, `CO2-CO9` support exists with tests. | New: exact identifier cardinality is not enforced (e.g., broad prefix matching can accept out-of-domain `CO*` identifiers). |
| 08 CRN Control | `CR1` parsing and QC handling implemented. | No net-new gap from this pass. |
| 09 Subhourly Temp | `CT1-CT3` implemented and tested. | New: Part 9 temperature value bounds are not enforced (`CT` allows extreme out-of-range values). |
| 10 Hourly Temp | `CU1-CU3` implemented and tested. | New: Part 10 average/std-dev temperature bounds are not enforced for `CU*`. |
| 11 Hourly Temp Extreme | `CV1-CV3` implemented with HHMM checks and QC tests. | New: Part 11 min/max temperature bounds are not enforced for `CV*` values (time fields are checked). |
| 12 Subhourly Wetness | `CW1` implemented and tested. | No net-new gap from this pass. |
| 13 Geonor Summary | `CX1-CX3` implemented and tested. | New: Part 13 precipitation/frequency numeric bounds are only partially enforced (`CX*` accepts out-of-range numeric values). |
| 14 Runway Visual Range | `ED1` implemented with domain and quality checks. | No net-new gap from this pass. |
| 15 Cloud and Solar | `GA/GD/GE1/GF1/GG/GH1` sections are present with core code-domain validation. | New: Part 15 cloud-height and `GH1` solar-radiation numeric MIN/MAX constraints are not enforced. |
| 16 Sunshine | `GJ/GK/GL` sections implemented and range-tested. | No net-new gap from this pass. |
| 17 Solar Irradiance | `GM1/GN1` parsing and quality domains are implemented. | New: irradiance value ranges (and GN zenith-angle range) are largely unchecked beyond sentinel handling. |
| 18 Net Solar Radiation | `GO1` implemented with time-period checks. | New: GO component value ranges (`-999..9998`) are not enforced. |
| 19 Modeled Solar Irradiance | `GP1` source flags/uncertainty bounds implemented and tested. | No net-new gap from this pass. |
| 20 Hourly Solar Angle | `GQ1` implemented with QC and period checks. | New: documented angle-value bounds (`0000-3600`) are not enforced for mean zenith/azimuth fields. |
| 21 Hourly Extraterrestrial Radiation | `GR1` implemented with QC and period checks. | New: documented radiation-value bounds (`0000-9998`) are not enforced for horizontal/normal fields. |
| 22 Hail | `HAIL` section implemented with range/quality tests. | No net-new gap from this pass. |
| 23 Ground Surface | `IA/IB/IC` sections implemented with code/quality/sentinel handling. | New: many Part 23 numeric MIN/MAX bounds (IA2/IB1/IB2/IC1) are not enforced. |
| 24 Temperature | `KA/KB/KC/KD/KE/KF/KG` sections implemented and broadly tested for sentinels/quality/code domains. | New: many numeric MIN/MAX constraints (and KC date tokens) from Part 24 are not enforced. |
| 25 Sea Surface Temp | `SA1` implemented with quality and range checks. | No net-new gap from this pass. |
| 26 Soil Temp | `ST1` implemented with categorical and quality-domain checks. | New: soil-temperature and depth numeric MIN/MAX bounds are not enforced. |
| 27 Pressure | `MA/MD/ME/MF/MG/MH/MK` sections implemented with quality and core code-domain checks. | New: pressure numeric MIN/MAX bounds and `MK1` DDHHMM occurrence-time bounds are not enforced. |
| 28 Weather Extended | `MV/MW` sections implemented with code-domain checks. | No net-new gap from this pass. |
| 29 Wind | `OA/OB/OC/OD/OE/RH` sections implemented and tested. | New: `OC1` and `RH*` MIN/MAX ranges are missing, and `OE` time validation still accepts invalid HHMM minute values like `0060`/`1261`. |
| 30 Marine | `UA/UG/WA/WD/WG/WJ/EQD/REM/QNN` sections are present; `QNN` parsing now enforces structured element/value grouping. | New: REM parsing order conflicts with generic comma-splitting; comma-bearing remarks can lose typed REM outputs when `keep_raw=False`. |

## Net-New Misalignments Identified

1. Identifier family cardinality is over-permissive.
   - Spec bounds are explicit for repeated identifiers: `CO2-CO9` (`isd-format-document-parts/part-07-network-metadata.md:43`), `OA1-OA3`/`OD1-OD3`/`OE1-OE3`/`RH1-RH3` (`isd-format-document-parts/part-29-wind-data.md:9`, `isd-format-document-parts/part-29-wind-data.md:245`, `isd-format-document-parts/part-29-wind-data.md:311`, `isd-format-document-parts/part-29-wind-data.md:387`), and `Q01-99`/`N01-99` families (`isd-format-document-parts/part-30-marine-data.md:794`, `isd-format-document-parts/part-30-marine-data.md:803`).
   - Current matching uses broad `startswith` lookup (`src/noaa_climate_data/constants.py:3123`) fed by coarse prefixes (`src/noaa_climate_data/constants.py:3114`), so out-of-domain IDs can still resolve to rules.
   - Tests validate valid suffix examples only (`tests/test_cleaning.py:94`) and do not assert rejection of invalid suffixes.

2. Part 15 cloud-height ranges are not enforced for multiple sections.
   - Spec ranges: GA/GD heights to `+35000` (`isd-format-document-parts/part-15-cloud-and-solar-data.md:52`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:205`), GE1 upper/lower ranges to `+15000` (`isd-format-document-parts/part-15-cloud-and-solar-data.md:328`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:337`), GF1 lowest cloud base to `15000` (`isd-format-document-parts/part-15-cloud-and-solar-data.md:518`), GG height to `35000` (`isd-format-document-parts/part-15-cloud-and-solar-data.md:666`).
   - Current rules define sentinels but no min/max constraints on these numeric parts (`src/noaa_climate_data/constants.py:1754`, `src/noaa_climate_data/constants.py:1796`, `src/noaa_climate_data/constants.py:1824`, `src/noaa_climate_data/constants.py:946`, `src/noaa_climate_data/constants.py:947`, `src/noaa_climate_data/constants.py:991`).
   - Existing GE1 tests cover code/sentinel behavior, not numeric bounds (`tests/test_cleaning.py:186`).

3. Part 15 `GH1` solar-radiation value ranges are not enforced.
   - Spec defines `GH1` component bounds up to `99998` with `99999` missing (`isd-format-document-parts/part-15-cloud-and-solar-data.md:774`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:798`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:822`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:854`).
   - Current `GH*` numeric value parts have sentinels/scaling but no min/max checks (`src/noaa_climate_data/constants.py:2129`, `src/noaa_climate_data/constants.py:2140`, `src/noaa_climate_data/constants.py:2151`, `src/noaa_climate_data/constants.py:2162`).

4. Parts 17-18 `GM/GN/GO` numeric component ranges are only partially enforced.
   - Spec ranges include `GM/GN` irradiance components (`0000-9998`), `GN` solar zenith angle (`000-998`) (`isd-format-document-parts/part-17-solar-irradiance-section.md:41`, `isd-format-document-parts/part-17-solar-irradiance-section.md:219`, `isd-format-document-parts/part-17-solar-irradiance-section.md:306`), and `GO` net radiation components (`-999..9998`) (`isd-format-document-parts/part-18-net-solar-radiation-section.md:28`, `isd-format-document-parts/part-18-net-solar-radiation-section.md:47`, `isd-format-document-parts/part-18-net-solar-radiation-section.md:65`).
   - Current rules constrain time-period part 1 but leave many component numeric parts without min/max bounds (`src/noaa_climate_data/constants.py:2232`, `src/noaa_climate_data/constants.py:2244`, `src/noaa_climate_data/constants.py:2256`, `src/noaa_climate_data/constants.py:2268`, `src/noaa_climate_data/constants.py:2285`, `src/noaa_climate_data/constants.py:2291`, `src/noaa_climate_data/constants.py:2297`, `src/noaa_climate_data/constants.py:2303`, `src/noaa_climate_data/constants.py:2309`, `src/noaa_climate_data/constants.py:2326`, `src/noaa_climate_data/constants.py:2332`, `src/noaa_climate_data/constants.py:2338`).
   - Tests currently focus on flag/quality/time-period behavior (`tests/test_cleaning.py:1307`, `tests/test_cleaning.py:1326`, `tests/test_cleaning.py:1330`, `tests/test_cleaning.py:1334`).

5. Part 27 pressure ranges are only partially enforced.
   - Spec ranges are explicit for MA1/MD1/MF1/MG1/MH1/MK1 fields, e.g. MA station pressure `04500-10900`, MD1 3-hour pressure change `000-500`, MD1 24-hour change `-800..+800`, and MF/MG/MH/MK pressure fields (`isd-format-document-parts/part-27-pressure-data.md:49`, `isd-format-document-parts/part-27-pressure-data.md:128`, `isd-format-document-parts/part-27-pressure-data.md:148`, `isd-format-document-parts/part-27-pressure-data.md:232`, `isd-format-document-parts/part-27-pressure-data.md:262`, `isd-format-document-parts/part-27-pressure-data.md:297`, `isd-format-document-parts/part-27-pressure-data.md:316`, `isd-format-document-parts/part-27-pressure-data.md:355`, `isd-format-document-parts/part-27-pressure-data.md:378`, `isd-format-document-parts/part-27-pressure-data.md:424`, `isd-format-document-parts/part-27-pressure-data.md:454`).
   - Current rules mostly apply sentinel/quality handling without min/max checks for these parts (`src/noaa_climate_data/constants.py:570`, `src/noaa_climate_data/constants.py:576`, `src/noaa_climate_data/constants.py:599`, `src/noaa_climate_data/constants.py:605`, `src/noaa_climate_data/constants.py:2059`, `src/noaa_climate_data/constants.py:2065`, `src/noaa_climate_data/constants.py:2076`, `src/noaa_climate_data/constants.py:2082`, `src/noaa_climate_data/constants.py:2093`, `src/noaa_climate_data/constants.py:2099`, `src/noaa_climate_data/constants.py:2110`, `src/noaa_climate_data/constants.py:2117`).

6. Part 27 `MK1` occurrence date-time fields are not range-validated.
   - Spec defines `MK1` occurrence date-time as DDHHMM with `MIN 010000` and `MAX 312359` (`isd-format-document-parts/part-27-pressure-data.md:432`, `isd-format-document-parts/part-27-pressure-data.md:434`, `isd-format-document-parts/part-27-pressure-data.md:462`, `isd-format-document-parts/part-27-pressure-data.md:464`).
   - Current `MK1` date-time parts are treated as generic categorical strings with only missing sentinel handling (`src/noaa_climate_data/constants.py:2111`, `src/noaa_climate_data/constants.py:2118`).

7. Part 24 temperature ranges/dates are only partially enforced.
   - Spec defines explicit ranges for KA/KB/KC/KD/KF/KG values and KC date tokens (e.g., KA period `001-480`, KA temperature `-0932..+0618`, KB period `001-744`, KB temperature `-9900..+6300`, KC temperature `-1100..+0630`, KC dates `01-31`, KD period `001-744`, KD value `0000-5000`, KF `-9999..+9998`, KG period `001-744`, KG temperature `-9900..+6300`) (`isd-format-document-parts/part-24-temperature-data.md:19`, `isd-format-document-parts/part-24-temperature-data.md:44`, `isd-format-document-parts/part-24-temperature-data.md:81`, `isd-format-document-parts/part-24-temperature-data.md:99`, `isd-format-document-parts/part-24-temperature-data.md:157`, `isd-format-document-parts/part-24-temperature-data.md:166`, `isd-format-document-parts/part-24-temperature-data.md:208`, `isd-format-document-parts/part-24-temperature-data.md:224`, `isd-format-document-parts/part-24-temperature-data.md:374`, `isd-format-document-parts/part-24-temperature-data.md:405`, `isd-format-document-parts/part-24-temperature-data.md:430`).
   - Current rules for these sections emphasize sentinels, quality, and code domains; they do not encode those numeric/day ranges (`src/noaa_climate_data/constants.py:1859`, `src/noaa_climate_data/constants.py:1866`, `src/noaa_climate_data/constants.py:1877`, `src/noaa_climate_data/constants.py:1884`, `src/noaa_climate_data/constants.py:1907`, `src/noaa_climate_data/constants.py:1908`, `src/noaa_climate_data/constants.py:1919`, `src/noaa_climate_data/constants.py:1926`, `src/noaa_climate_data/constants.py:1966`, `src/noaa_climate_data/constants.py:1973`, `src/noaa_climate_data/constants.py:1980`).

8. Part 23 ground-surface numeric ranges are only partially enforced.
   - Spec provides explicit bounds for IA2/IB1/IB2/IC1 numeric fields (e.g., IA2 period `001-480`, IA2 minimum temperature `-1100..+1500`, IB temperature fields `-9999..+9998`, IB standard deviation `0000..9998`, IC period `01-98`, IC wind movement `0000..9998`, IC evaporation `000..998`, IC pan-water temperatures `-100..+500`) (`isd-format-document-parts/part-23-ground-surface-data.md:89`, `isd-format-document-parts/part-23-ground-surface-data.md:97`, `isd-format-document-parts/part-23-ground-surface-data.md:144`, `isd-format-document-parts/part-23-ground-surface-data.md:168`, `isd-format-document-parts/part-23-ground-surface-data.md:193`, `isd-format-document-parts/part-23-ground-surface-data.md:226`, `isd-format-document-parts/part-23-ground-surface-data.md:266`, `isd-format-document-parts/part-23-ground-surface-data.md:299`, `isd-format-document-parts/part-23-ground-surface-data.md:346`, `isd-format-document-parts/part-23-ground-surface-data.md:354`, `isd-format-document-parts/part-23-ground-surface-data.md:388`, `isd-format-document-parts/part-23-ground-surface-data.md:415`, `isd-format-document-parts/part-23-ground-surface-data.md:450`).
   - Current rules for these fields are largely sentinel/quality-based without min/max constraints (`src/noaa_climate_data/constants.py:2460`, `src/noaa_climate_data/constants.py:2461`, `src/noaa_climate_data/constants.py:2472`, `src/noaa_climate_data/constants.py:2479`, `src/noaa_climate_data/constants.py:2486`, `src/noaa_climate_data/constants.py:2493`, `src/noaa_climate_data/constants.py:2505`, `src/noaa_climate_data/constants.py:2512`, `src/noaa_climate_data/constants.py:2524`, `src/noaa_climate_data/constants.py:2525`, `src/noaa_climate_data/constants.py:2538`, `src/noaa_climate_data/constants.py:2551`, `src/noaa_climate_data/constants.py:2564`).

9. Part 26 `ST1` numeric ranges are only partially enforced.
   - Spec defines `ST1` soil temperature range `-1100..+0630` and depth range `0000..9998` (`isd-format-document-parts/part-26-soil-temperature-data.md:34`, `isd-format-document-parts/part-26-soil-temperature-data.md:52`).
   - Current `ST1` numeric parts carry sentinels/quality links but no min/max checks (`src/noaa_climate_data/constants.py:2031`, `src/noaa_climate_data/constants.py:2037`), and tests focus on sentinel/quality behavior (`tests/test_cleaning.py:397`, `tests/test_cleaning.py:1470`).

10. Part 20/21 `GQ1` and `GR1` value ranges are not enforced.
   - Spec defines `GQ1` mean zenith/azimuth `0000..3600` (`isd-format-document-parts/part-20-hourly-solar-angle-section.md:32`, `isd-format-document-parts/part-20-hourly-solar-angle-section.md:50`) and `GR1` horizontal/normal radiation `0000..9998` (`isd-format-document-parts/part-21-hourly-extraterrestrial-radiation-section.md:27`, `isd-format-document-parts/part-21-hourly-extraterrestrial-radiation-section.md:53`).
   - Current rules validate time period and quality but not those value bounds (`src/noaa_climate_data/constants.py:2418`, `src/noaa_climate_data/constants.py:2424`, `src/noaa_climate_data/constants.py:2441`, `src/noaa_climate_data/constants.py:2447`); tests likewise cover missing/quality/time period only (`tests/test_cleaning.py:1367`, `tests/test_cleaning.py:1378`, `tests/test_cleaning.py:1382`, `tests/test_cleaning.py:1393`).

11. Part 24 `KE1` day-count ranges are not enforced.
   - Spec defines each `KE1` count field as `00..31` with `99` missing (`isd-format-document-parts/part-24-temperature-data.md:269`, `isd-format-document-parts/part-24-temperature-data.md:290`, `isd-format-document-parts/part-24-temperature-data.md:312`, `isd-format-document-parts/part-24-temperature-data.md:333`).
   - Current `KE1` count parts apply missing/quality handling but no min/max constraint (`src/noaa_climate_data/constants.py:1937`, `src/noaa_climate_data/constants.py:1943`, `src/noaa_climate_data/constants.py:1949`, `src/noaa_climate_data/constants.py:1955`), and tests do not assert out-of-range rejection (`tests/test_cleaning.py:317`, `tests/test_cleaning.py:1458`).

12. Part 30 `REM` parsing can be bypassed by generic comma expansion.
   - Spec defines REM as typed remark blocks (`REM` + type + length + text), where free-text remark content is ASCII and can include punctuation (`isd-format-document-parts/part-30-marine-data.md:731`, `isd-format-document-parts/part-30-marine-data.md:737`, `isd-format-document-parts/part-30-marine-data.md:760`, `isd-format-document-parts/part-30-marine-data.md:766`).
   - Current flow parses any comma-bearing object column first (`src/noaa_climate_data/cleaning.py:506`, `src/noaa_climate_data/cleaning.py:511`, `src/noaa_climate_data/cleaning.py:524`) and runs REM-specific parsing later only if raw `REM` still exists (`src/noaa_climate_data/cleaning.py:530`).
   - Reproduced: `clean_noaa_dataframe(pd.DataFrame({'REM':['SYN 005 hello,world']}), keep_raw=False)` yields only `REM__part*` columns (no `remarks_type_code`/`remarks_text`); existing test coverage checks a simple REM case only (`tests/test_cleaning.py:1751`).

13. Part 29 `OE` time-of-occurrence validation does not enforce real HHMM minute semantics.
   - Spec defines summary wind occurrence time as `MIN 0000` to `MAX 2359` in HHMM format (`isd-format-document-parts/part-29-wind-data.md:363`, `isd-format-document-parts/part-29-wind-data.md:365`).
   - Current rule uses a simple numeric set `0000..2359` (`src/noaa_climate_data/constants.py:2769`, `src/noaa_climate_data/constants.py:2773`), which accepts invalid values like `0060` and `1261`.
   - Existing test only checks `2360` rejection (`tests/test_cleaning.py:473`), leaving invalid-minute cases uncovered.

14. Part 29 `OC1` wind-gust numeric range is not enforced.
   - Spec defines `OC1` gust as `MIN 0050` and `MAX 1100` (`isd-format-document-parts/part-29-wind-data.md:219`).
   - Current `OC1` rule includes scaling/sentinel/quality but no min/max bound (`src/noaa_climate_data/constants.py:555`, `src/noaa_climate_data/constants.py:563`), so values below and above spec limits are retained.
   - Tests cover scaling and quality only (`tests/test_cleaning.py:621`, `tests/test_cleaning.py:1012`).

15. Part 29 `RH1-RH3` period and humidity bounds are not enforced.
   - Spec defines `RH` period `001..744` hours and humidity `000..100` percent (`isd-format-document-parts/part-29-wind-data.md:397`, `isd-format-document-parts/part-29-wind-data.md:416`).
   - Current `RH*` rule sets sentinels/codes/quality but no min/max constraints on part 1 or part 3 (`src/noaa_climate_data/constants.py:2782`, `src/noaa_climate_data/constants.py:2785`, `src/noaa_climate_data/constants.py:2792`).
   - Existing tests validate missing and nominal values only (`tests/test_cleaning.py:426`, `tests/test_cleaning.py:433`).

16. Part 4 `AH/AI` short-duration precipitation ranges are not enforced.
   - Spec defines `AH` period `005..045`, `AI` period `060..180`, depth `0000..3000`, and ending date-time `010000..312359` (`isd-format-document-parts/part-04-additional-data-section.md:485`, `isd-format-document-parts/part-04-additional-data-section.md:493`, `isd-format-document-parts/part-04-additional-data-section.md:510`, `isd-format-document-parts/part-04-additional-data-section.md:561`, `isd-format-document-parts/part-04-additional-data-section.md:569`, `isd-format-document-parts/part-04-additional-data-section.md:586`).
   - Current `AH*`/`AI*` rules use sentinels and condition/quality domains but no min/max or DDHHMM range validation for these parts (`src/noaa_climate_data/constants.py:1163`, `src/noaa_climate_data/constants.py:1166`, `src/noaa_climate_data/constants.py:1167`, `src/noaa_climate_data/constants.py:1174`, `src/noaa_climate_data/constants.py:1186`, `src/noaa_climate_data/constants.py:1189`, `src/noaa_climate_data/constants.py:1190`, `src/noaa_climate_data/constants.py:1197`).
   - Existing tests focus on missing/quality behavior (`tests/test_cleaning.py:1589`, `tests/test_cleaning.py:1596`, `tests/test_cleaning.py:1600`, `tests/test_cleaning.py:1607`).

17. Remaining Part 6/9/10/11/13 numeric range enforcement is incomplete.
   - Specs define explicit numeric bounds for `CI1`/`CN1-CN4` diagnostics in Part 6 (`isd-format-document-parts/part-06-climate-reference-network-unique-data.md:243`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:269`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:303`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:329`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:381`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:437`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:479`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:511`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:537`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:584`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:609`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:711`, `isd-format-document-parts/part-06-climate-reference-network-unique-data.md:743`), plus temperature/frequency bounds for `CT/CU/CV/CX` in Parts 9-13 (`isd-format-document-parts/part-09-subhourly-temperature-section.md:29`, `isd-format-document-parts/part-10-hourly-temperature-section.md:22`, `isd-format-document-parts/part-10-hourly-temperature-section.md:54`, `isd-format-document-parts/part-11-hourly-temperature-extreme-section.md:28`, `isd-format-document-parts/part-11-hourly-temperature-extreme-section.md:84`, `isd-format-document-parts/part-13-hourly-geonor-vibrating-wire-summary-section.md:33`, `isd-format-document-parts/part-13-hourly-geonor-vibrating-wire-summary-section.md:56`, `isd-format-document-parts/part-13-hourly-geonor-vibrating-wire-summary-section.md:87`, `isd-format-document-parts/part-13-hourly-geonor-vibrating-wire-summary-section.md:110`).
   - Current rules for these sections largely apply sentinels + quality domains but omit many explicit min/max checks (`src/noaa_climate_data/constants.py:1625`, `src/noaa_climate_data/constants.py:1637`, `src/noaa_climate_data/constants.py:1656`, `src/noaa_climate_data/constants.py:1720`, `src/noaa_climate_data/constants.py:2964`, `src/noaa_climate_data/constants.py:2997`, `src/noaa_climate_data/constants.py:3023`, `src/noaa_climate_data/constants.py:3049`, `src/noaa_climate_data/constants.py:3068`).

18. Repeated-identifier cardinality remains over-permissive for many families outside current gated ranges.
   - Spec cardinality is explicit in multiple sections: e.g., `AH1-AH6`/`AI1-AI6`/`AL1-AL4`/`AO1-AO4` (`isd-format-document-parts/part-04-additional-data-section.md:474`, `isd-format-document-parts/part-04-additional-data-section.md:550`, `isd-format-document-parts/part-04-additional-data-section.md:787`, `isd-format-document-parts/part-04-additional-data-section.md:992`), `AT1-AT8`/`AU1-AU9`/`AW1-AW4`/`AX1-AX6`/`AZ1-AZ2` (`isd-format-document-parts/part-05-weather-occurrence-data.md:8`, `isd-format-document-parts/part-05-weather-occurrence-data.md:108`, `isd-format-document-parts/part-05-weather-occurrence-data.md:218`, `isd-format-document-parts/part-05-weather-occurrence-data.md:353`, `isd-format-document-parts/part-05-weather-occurrence-data.md:482`), `GA1-GA6`/`GD1-GD6`/`GG1-GG6` (`isd-format-document-parts/part-15-cloud-and-solar-data.md:9`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:131`, `isd-format-document-parts/part-15-cloud-and-solar-data.md:626`), and `MV1-MV7`/`MW1-MW7` (`isd-format-document-parts/part-28-weather-occurrence-data-extended.md:9`, `isd-format-document-parts/part-28-weather-occurrence-data-extended.md:53`).
   - `_REPEATED_IDENTIFIER_RANGES` currently enforces bounds for a small subset only (`src/noaa_climate_data/constants.py:3147`), while generic prefix matching still resolves out-of-domain IDs for other families (`src/noaa_climate_data/constants.py:3190`, `src/noaa_climate_data/constants.py:3193`).
   - Reproduced with `get_field_rule(...)`: `AT9`, `AU10`, `AW5`, `AX7`, `AZ3`, `AH7`, `AL5`, `AO5`, `GA7`, `GD7`, `GG7`, `MV8`, and `MW8` all currently resolve as valid.

## Added to Next Steps

These eighteen items were recorded under `P0` in `NEXT_STEPS.md`.
