# Next steps: ISD alignment checklist

## P0: Implementation vs official ISD docs

- [x] Enforce per-field allowed-quality sets for 2-part value/quality fields (e.g., GJ/GK/GL/MV/MW) instead of the generic `QUALITY_FLAGS` gate.
- [x] Apply field-specific sentinel detection (including leading-zero normalization) for 2-part value/quality fields to match ISD/README rules.
- [x] Align 2-part field naming with ISD semantics and friendly maps: `clean_value_quality` always emits `__value`, which conflicts with `__part1` expectations for MV/GJ/GK/GL and bypasses their per-part metadata.
- [x] Apply GE1 convective cloud missing sentinel (`9`) from Part 15 in `FIELD_RULES`/cleaning.
- [x] Apply GE1 vertical datum missing sentinel (`999999`) from Part 15 in `FIELD_RULES`/cleaning.
- [x] Restrict GF1 quality parts to Part 15 cloud quality codes (currently defaults to `QUALITY_FLAGS`).
- [x] Apply GA cloud-layer type missing sentinel (`99`) from Part 15.
- [x] Apply GF1 low/mid/high cloud genus missing sentinels (`99`) from Part 15.
- [x] Apply AJ snow-depth condition missing sentinels (`9`) for depth/equivalent water codes.
- [x] Apply UA1 wave-measurement missing sentinels (method `9`, sea state `99`) from Part 30.
- [x] Restrict AU present-weather quality codes to Part 5 values (0-7, 9, M) and apply missing sentinels to AU parts (9/99 per field).
- [x] Restrict AY past-weather quality codes to Part 5 values (0-3, 9).
- [x] Restrict OC1 wind-gust quality codes to Part 29 values (0-7, 9, M).
- [x] Apply AU present-weather missing sentinels for descriptor/obscuration/other/combination codes (`9`) and precipitation code (`99`).
- [x] Restrict AA/AJ quality codes to Part 4 precipitation/snow sets (drop unsupported `C`).
- [x] Apply Part 29 calm-condition rule for OD: direction `999` with speed `0000` indicates calm wind.
- [x] Restrict MA1 station pressure quality codes to Part 27 values (exclude unsupported `C`).
- [x] Restrict MD1 quality codes to Part 27 values (0-3, 9 only).
- [x] Restrict SA1 sea-surface temperature quality codes to Part 29 values (0-3, 9 only).
- [x] Validate Control Data Section code domains (data source flag, report type code, QC process V01/V02/V03) and missing sentinels for lat/lon/elev/call letters.
- [x] Validate Mandatory Data Section domain codes and sentinels (wind type codes, CAVOK, ceiling determination, visibility variability, special missing rules like variable wind direction).
- [x] Encode Mandatory Data Section edge rules (ceiling unlimited=22000, visibility >160000 clamp, wind type 9 with speed 0000 indicates calm).
- [x] Fill in remaining Mandatory Data Section fields from master spec (dew point + quality, sea level pressure + quality, and any trailing mandatory positions missing in part-03 file).

## P1: Missing ISD groups and sections (implementation gaps)

- [x] Add Part 4 additional data section identifier ADD (section boundary for variable groups).
- [x] Add precipitation groups from Part 4 beyond AA/AJ/AU (e.g., AB1 monthly total, AC1 precipitation history, AD1 greatest 24-hour amount).
- [x] Add Part 4 additional precipitation groups: AE1, AG1.
- [x] Add Part 4 additional precipitation groups: AH1-AH6, AI1-AI6, AK1, AL1-AL4, AM1, AN1, AO1-AO4, AP1-AP4.
- [x] Add Part 4 snow-accumulation groups AL1-AL4 (accumulation period/depth), AM1 (greatest 24-hour amount), AN1 (day/month totals).
- [x] Add Part 4 additional liquid-precip groups AO1-AO4 (minutes-based), AP1-AP4 (HPD 15-min gauges with quality codes).
- [x] Add Part 5 weather occurrence groups AT1-AT8 (daily present weather) and AU1-AU9 (present weather observation components).
- [x] Add Part 6 CRN unique groups CB1-CB2 (secondary precip), CF1-CF3 (fan speed), CG1-CG3 (primary precip), CH1-CH2 (RH/Temp), CI1 (hourly RH/Temp stats), and CN1-CN4 (battery + diagnostics).
- [x] Add Part 7 network metadata groups CO1 (climate division + UTC offset), CO2-CO9 (element time offsets), CR1 (CRN control), CT1-CT3 (subhourly temp), CU1-CU3 (hourly temp + std dev).
- [x] Add Part 7 network metadata groups CV1-CV3 (hourly temp extremes + times), CW1 (subhourly wetness), CX1-CX3 (hourly Geonor vibrating wire summary).
- [x] Add Part 8 CRN control section fields (air temp QC, dew point + QC, sea level pressure + QC).
- [x] Add Part 14 runway visual range group ED1 (runway designator, direction, visibility, quality).
- [x] Implement remaining cloud/solar groups from Part 15 (e.g., below-station cloud layer sections not yet mapped).
- [x] Add Part 15 below-station cloud layer group GG1-GG6 (coverage, heights, type/top codes, and quality flags).
- [x] Add Part 15 modeled solar irradiance group GP1 (modeled global/direct/diffuse values, flags, and uncertainties).
- [x] Add Part 20 hourly solar angle group GQ1 (time period, mean zenith/azimuth angles, QC).
- [x] Add Part 20 hourly extraterrestrial radiation group GR1 (time period, horizontal/normal values, QC).
- [x] Add Hail data group from Part 20/22 (identifier + hail size/quality); master doc labels a HAIL identifier but does not show its code.
- [x] Add Part 23 ground surface groups IA1/IA2, IB1/IB2, IC1 (ground condition, min/max temps, snow depth), with quality codes.
- [x] Add Part 23 air temperature groups KB1-KB3 (average air temperature) with scaling/sentinels.
- [x] Add Part 23 ground/soil temperature groups KC1-KC2, KD1-KD2, KE1, KF1, KG1-KG2 (soil/ground temps and quality flags).
- [x] Add Part 24 temperature groups KC1-KC2 (extreme air temperature for month) and KD1-KD2 (heating/cooling degree days).
- [x] Add Part 24 temperature groups KF1 (derived hourly air temperature) and KG1-KG2 (average dew point/wet bulb).
- [ ] Add Part 26 soil temperature group ST1 (type, temp, depth, cover, subplot, quality codes).
- [ ] Add Part 27 pressure groups beyond MA1/MD1 (ME1, MF1, MG1, MH1, MK1).
- [ ] Add Part 28 relative humidity group RH1-RH3 (period, code, derived, QC).
- [ ] Add Part 29 hourly/sub-hourly wind section OB1-OB2.
- [ ] Add Part 29 supplementary wind group OE1-OE3 (summary-of-day wind).
- [ ] Add remaining marine groups from Part 30 (e.g., WA1 platform ice accretion, other marine sections listed in Part 30).
- [ ] Add Part 30 secondary swell group UG2 and remaining marine groups (WA1, WD1, WG1, WJ1).
- [ ] Add Part 30 element quality data section (EQD with Q01-P01-R01/C01/D01/N01 identifiers, parameter/units codes, and marine-specific QC definitions).
- [ ] Add EQD element-units table plus parameter-code flag conventions (Flag-1/Flag-2 definitions and element-name codes).
- [ ] Add Part 30 remarks data section (REM) and remark type identifiers (SYN/AWY/MET/SOD/SOM/HPD).
- [ ] Add Original Observation Data Section identifiers QNN (original NCEI surface hourly source codes/flags).
- [ ] Add QNN original observation element identifiers (A-Y mapping for DS3280 elements) and data value format.

## P2: README alignment (implementation vs README)

- [ ] Clarify README vs implementation for multi-part fields: code only emits a single `__quality` column when all parts share one `quality_part`; most multi-part ISD groups only expose per-part quality columns.
- [ ] Align `LocationData_Hourly.csv` definition with behavior: either apply completeness filters to hourly output or update README to state it is best-hour only.

## P3: Supporting docs, validation, and tests

- [ ] Populate missing ISD docs in-repo (Parts 10/11/16/17/18/19/21/22/24/25) to verify KA*/SA1 scaling/sentinels and solar/sunshine/hail sections.
- [ ] Add tests for new groups to ensure sentinel removal and quality filtering are applied consistently.
- [ ] Capture Domain Value ID tables for code validation (e.g., pressure tendency, geopotential levels, weather codes) if used in parsing.
- [ ] Consider enforcing record/section length constraints (control=60, mandatory=45, max record 2844, max block 8192) if parser validates structure.
