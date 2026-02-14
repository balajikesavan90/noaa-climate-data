# NOAA Cleaning Alignment Report

Date: 2026-02-14

## Scope

This review compares NOAA ISD documentation in `isd-format-document-parts/part-01-*.md` through `part-30-*.md` against the current data-cleaning implementation and tests:

- `src/noaa_climate_data/cleaning.py`
- `src/noaa_climate_data/constants.py`
- `tests/test_cleaning.py`

## Part-by-part alignment and misalignment snapshot

| Part | Alignment observed | Misalignment observed |
| --- | --- | --- |
| 01 Preface | Informational section; no direct parser constraints. | None specific to cleaning logic. |
| 02 Control | Control fields are validated and normalized (`cleaning.py:360-425`), with tests for date/time and code validation (`tests/test_cleaning.py:1374-1413`). | `DATE` accepts ISO timestamps via `pd.to_datetime` (`cleaning.py:366-370`; `tests/test_cleaning.py:1415-1423`) while Part 2 requires `YYYYMMDD` (`part-02-control-data-section.md:32-37`). QC code truncation behavior (`V020 -> V02`) is permissive/non-spec (`cleaning.py:421-423`; `tests/test_cleaning.py:1383-1393`). |
| 03 Mandatory | Mandatory wind/cig/vis rules and calm/clamp handling are implemented and tested (`cleaning.py:216-293`; `tests/test_cleaning.py:1425-1430`). | Fixed-width enforcement remains partial (tracked in `NEXT_STEPS.md`). |
| 04 Additional | AA/AJ/AO/AP groups implemented with sentinel and quality handling (`constants.py:865+`, `constants.py:1117+`; tests in `tests/test_cleaning.py:1143-1261`). | AP condition code should be fixed missing `9` ("not used at this time") per Part 4 (`part-04-additional-data-section.md:1080-1083`), but current AP part 2 only treats `9` as missing and does not reject non-`9` (`constants.py:1121`). |
| 05 Weather occurrence | AU/AY/AX/AZ/AW/AT parsing and quality gating are implemented with broad test coverage (`constants.py:1156-1285`; `tests/test_cleaning.py:588-607`, `tests/test_cleaning.py:743-781`). | AW code list is sparse in NOAA docs (`part-05-weather-occurrence-data.md:229-330`), but code accepts all `00-98` (`constants.py:1277`). AU component domains still not fully constrained. |
| 06 CRN unique | CB/CF/CG/CH/CI/CN groups are present and quality-gated in tests (`tests/test_cleaning.py:784-817`). | Additional numeric range and QC/FLAG domain checks remain incomplete (tracked in `NEXT_STEPS.md`). |
| 07 Network metadata | CO1 division and UTC offset rules align with Part 7 (`constants.py:842-860`; `tests/test_cleaning.py:823-841`; `part-07-network-metadata.md:14-27`). | Remaining metadata identifier mapping completeness is still open for some CO/CT/CU/CV/CW/CX variants. |
| 08 CRN control | CR1 handled and tested (`tests/test_cleaning.py:861-864`). | Full CRN QC/FLAG domain enforcement across sections still open. |
| 09 Subhourly temperature | CT groups are parsed and quality-gated in tests (`tests/test_cleaning.py:865-868`). | No new high-confidence gap beyond existing CRN-domain backlog. |
| 10 Hourly temperature | CU groups implemented and tested (`tests/test_cleaning.py:869-872`). | CRN range/domain hardening still open. |
| 11 Hourly temperature extreme | CV time and quality checks are implemented and tested (`tests/test_cleaning.py:873-889`). | No new high-confidence gap beyond open CRN-domain backlog. |
| 12 Subhourly wetness | CW section implemented and tested (`tests/test_cleaning.py:892-896`). | None new from this pass. |
| 13 Geonor summary | CX section implemented and tested (`tests/test_cleaning.py:896-900`). | None new from this pass. |
| 14 Runway visual range | ED1 direction/visibility rules are implemented and tested (`tests/test_cleaning.py:900-920`). | None new from this pass. |
| 15 Cloud and solar | GE1 convective/vertical-datum domains and sentinels match Part 15 (`constants.py:781-799`; `tests/test_cleaning.py:169-181`; `part-15-cloud-and-solar-data.md:253-321`). | Broader Part 15 cloud code-domain tightening for GA/GD/GG/GF1 remains open. |
| 16 Sunshine | GJ/GK/GL groups are present and quality-gated (tests include `GJ1`, `tests/test_cleaning.py:1278-1280`). | Min/max range enforcement for sunshine metrics remains open. |
| 17 Solar irradiance | GM1 is implemented and integrated. | UVB layout mismatch and GM data-flag domain constraints remain open. |
| 18 Net solar radiation | GO section implemented. | Time period/range enforcement gaps remain open. |
| 19 Modeled solar irradiance | GP1 is implemented and tested (`tests/test_cleaning.py:988-999`). | Source flag and uncertainty-range enforcement gaps remain open. |
| 20 Hourly solar angle | GQ1 implemented and tested (`tests/test_cleaning.py:1001-1009`). | Time-period and quality-domain hardening still open. |
| 21 Extraterrestrial radiation | GR1 implemented and tested (`tests/test_cleaning.py:1013-1019`). | Time-period and quality-domain hardening still open. |
| 22 Hail | HAIL parsing and sentinel handling exists (`tests/test_cleaning.py:183-185`). | HAIL size range (`000-200`) hard enforcement remains open. |
| 23 Ground surface | IA/IB/IC and related groups implemented; IA1 domain tested (`tests/test_cleaning.py:1024-1033`). | No new high-confidence gap beyond existing backlog. |
| 24 Temperature | KA/KC/KD/KF/KG sections implemented with quality gating (`tests/test_cleaning.py:1037-1057`). | Some period/range hard checks still open in backlog. |
| 25 Sea surface temperature | SA1 group implemented with quality checks (`constants.py:524-533`). | SA1 value range `-050..+450` hard enforcement remains open. |
| 26 Soil temperature | ST1 implemented and quality-gated (`tests/test_cleaning.py:1061`). | No new high-confidence gap from this pass. |
| 27 Pressure | MA1/MD1 rules strongly aligned with Part 27 quality and domains (`constants.py:478-521`; `tests/test_cleaning.py:538-585`; `part-27-pressure-data.md:32-67`, `part-27-pressure-data.md:85-163`). | No new high-confidence gap from this pass. |
| 28 Weather occurrence extended | MV/MW (and RH from Part 28) handled with domain/quality checks (`tests/test_cleaning.py:1114-1119`, `tests/test_cleaning.py:292`). | No new high-confidence gap from this pass. |
| 29 Wind | OA/OD/OB/OE implemented; OD calm condition enforced (`cleaning.py:208-255`; `tests/test_cleaning.py:1090-1112`; `part-29-wind-data.md:302`, `part-29-wind-data.md:360`). | OE summary-of-day constraints are incomplete: period must be fixed `24`, speed `00000-20000`, and time `0000-2359` (`part-29-wind-data.md:329-339`, `part-29-wind-data.md:363-368`), but OE rule currently lacks these bounds (`constants.py:2364-2375`). |
| 30 Marine | UA/UG/WA/WD/WG/WJ/EQD/REM/QNN sections are present; UA/UG quality/range checks are tested (`constants.py:535+`; `tests/test_cleaning.py:566-646`). | WD/WG/WJ domain/range hardening remains open. EQD parameter-code semantics are over-generalized for Q/P/R/C/D vs N families. REM parsing does not implement repeated typed remark blocks with length quantities (`part-30-marine-data.md:757-768`). |

## Confirmed alignments with direct evidence

1. Part 15 GE1 convective cloud and vertical datum constraints are implemented as explicit allowed domains and missing sentinels (`constants.py:781-799`) and validated in tests (`tests/test_cleaning.py:169-181`), matching Part 15 definitions (`part-15-cloud-and-solar-data.md:253-321`).
2. Part 27 MA1/MD1 quality domains and pressure tendency code checks are codified (`constants.py:478-521`) and tested (`tests/test_cleaning.py:538-585`), consistent with Part 27 quality/tendency tables (`part-27-pressure-data.md:32-67`, `part-27-pressure-data.md:85-163`).
3. Part 7 CO1 climate division and UTC-LST offset ranges are enforced (`constants.py:842-860`) and tested (`tests/test_cleaning.py:823-841`), aligning with Part 7 (`part-07-network-metadata.md:14-27`).
4. Part 29 OD calm-wind translation to 0-degree direction is implemented (`cleaning.py:208-255`) and tested (`tests/test_cleaning.py:1090-1092`), matching the spec note (`part-29-wind-data.md:302`).
5. Part 30 UA1 method/period/height/sea-state domain checks are implemented (`constants.py:535-555`) and tested (`tests/test_cleaning.py:624-641`).
6. Part 2 control section numeric/code checks are implemented for lat/lon/elevation/source/report/QC (`cleaning.py:381-425`) with tests (`tests/test_cleaning.py:1374-1400`).

## Confirmed misalignments

### Newly identified in this review (added to `NEXT_STEPS.md`)

1. OE summary-of-day wind constraints missing:
   - Spec: period fixed to 24, speed range 00000-20000, time range 0000-2359 (`part-29-wind-data.md:329-339`, `part-29-wind-data.md:363-368`).
   - Current: OE part2/part3/part5 rules do not enforce these exact bounds (`constants.py:2364-2375`).
2. AP condition code not fixed to `9` only:
   - Spec: "Not used at this time. Value set to missing. 9=Missing" (`part-04-additional-data-section.md:1080-1083`).
   - Current: AP part2 only treats `9` as missing, but accepts any other categorical value (`constants.py:1121`).
3. AW automated weather code is over-permissive:
   - Spec: explicit sparse code list in Part 5 (`part-05-weather-occurrence-data.md:229-330`).
   - Current: accepts all `00-98` values (`constants.py:1277`).
4. EQD parameter-code validation not split by identifier family:
   - Spec: Q/P/R/C/D parameter codes include legacy code tables/patterns; N01-N99 uses units + element/flag structure (`part-30-marine-data.md:794-833`, `part-30-marine-data.md:998-1048`).
   - Current: generic element+flag validation is applied to all EQD prefixes (`cleaning.py:114-124`, `cleaning.py:280-283`, `constants.py:2722-2724`).
5. REM section structure parsing is incomplete:
   - Spec: each typed remark carries a length quantity and text; remarks can repeat in one REM section (`part-30-marine-data.md:737-768`).
   - Current: parser only performs a single 3-char prefix + remainder split (`cleaning.py:127-137`, `cleaning.py:470-478`).

### Existing open misalignments still applicable

1. Part 2 DATE accepts non-`YYYYMMDD` formats (`cleaning.py:366-370`; `tests/test_cleaning.py:1415-1423`) against strict Part 2 format requirement (`part-02-control-data-section.md:32-37`).
2. Part 30 WD/WG/WJ code-domain and numeric-range enforcement is incomplete.
3. Part 5 AU component code-domain enforcement is incomplete.
4. Parts 6-8 CRN numeric-range and QC/FLAG domain hardening is incomplete.
5. Parts 16-25 solar/sunshine/hail/sea-temperature min-max and code-domain enforcement has remaining gaps (see `NEXT_STEPS.md` open items).

## Test coverage observations for gaps

1. OE tests currently cover quality gating and calm-direction conversion (`tests/test_cleaning.py:945-951`) but do not assert rejection for non-24 periods, out-of-range speeds, or invalid HHMM.
2. AP tests cover missing sentinel/quality behavior (`tests/test_cleaning.py:1254-1261`) but do not assert non-`9` condition codes are rejected.
3. AW tests do not enforce sparse-code list behavior; they currently verify missing/quality paths only (`tests/test_cleaning.py:776-781`).
4. EQD tests are centered on the current generic validator (`tests/test_cleaning.py:970-986`) and do not cover Q/P/R/C/D legacy parameter-code families from Part 30.
5. REM tests validate only simple type/text extraction (`tests/test_cleaning.py:1330-1349`) and do not cover repeated typed remarks with explicit length quantities.

