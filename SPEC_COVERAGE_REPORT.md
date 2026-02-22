# SPEC Coverage Report

## How to run

```bash
python tools/spec_coverage/generate_spec_coverage.py
# Fallback in environments without `python` alias:
python3 tools/spec_coverage/generate_spec_coverage.py
```

## Overall coverage

- Total spec rules extracted: **2731**
- Metric-eligible rules (excluding `unknown`): **2726**
- Unknown/noisy rows excluded from %: **5**
- Rules implemented in code: **1467** (53.8%)
- Rules with explicit tests: **2442** (89.6%)
- Expected-gap tagged rules: **107**
- Rows linked to unresolved `NEXT_STEPS.md` items: **2504**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Enforcement layer breakdown

- constants_only: **1413** (51.8%)
- cleaning_only: **23** (0.8%)
- both: **31** (1.1%)
- neither: **1259** (46.2%)

## Confidence breakdown

- Cleaning-implemented metric rules: **54** (2.0%)
- high: **2** (3.7%)
- medium: **52** (96.3%)
- low: **0** (0.0%)

## Precision warnings

- Tested rows matched by `exact_signature`: **212** (8.7%)
- Tested rows matched by `exact_assertion`: **344** (14.1%)
- Tested rows matched by `family_assertion`: **711** (29.1%)
- Tested rows matched by `wildcard_assertion`: **1175** (48.1%)
- Synthetic rows in CSV: **75**
- Synthetic gap rows in CSV: **29**
- Unknown rule rows excluded from percentages: **5**
- Arity rules tested: **101/170** (59.4%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0.0% | 0.0% |
| 02 | 39 | 38 | 1 | 30 | 2.6% | 78.9% |
| 03 | 47 | 47 | 37 | 40 | 78.7% | 85.1% |
| 04 | 525 | 525 | 290 | 446 | 55.2% | 85.0% |
| 05 | 326 | 326 | 210 | 314 | 64.4% | 96.3% |
| 06 | 209 | 209 | 96 | 178 | 45.9% | 85.2% |
| 07 | 72 | 72 | 52 | 63 | 72.2% | 87.5% |
| 08 | 10 | 10 | 3 | 8 | 30.0% | 80.0% |
| 09 | 25 | 25 | 12 | 23 | 48.0% | 92.0% |
| 10 | 40 | 40 | 18 | 36 | 45.0% | 90.0% |
| 11 | 62 | 62 | 25 | 56 | 40.3% | 90.3% |
| 12 | 13 | 13 | 4 | 12 | 30.8% | 92.3% |
| 13 | 65 | 65 | 31 | 59 | 47.7% | 90.8% |
| 14 | 14 | 14 | 7 | 11 | 50.0% | 78.6% |
| 15 | 309 | 309 | 198 | 296 | 64.1% | 95.8% |
| 16 | 23 | 23 | 9 | 17 | 39.1% | 73.9% |
| 17 | 44 | 44 | 14 | 37 | 31.8% | 84.1% |
| 18 | 15 | 15 | 4 | 12 | 26.7% | 80.0% |
| 19 | 20 | 20 | 9 | 17 | 45.0% | 85.0% |
| 20 | 13 | 13 | 4 | 12 | 30.8% | 92.3% |
| 21 | 13 | 13 | 4 | 12 | 30.8% | 92.3% |
| 22 | 8 | 8 | 3 | 6 | 37.5% | 75.0% |
| 23 | 72 | 72 | 32 | 70 | 44.4% | 97.2% |
| 24 | 200 | 200 | 107 | 159 | 53.5% | 79.5% |
| 25 | 7 | 7 | 3 | 6 | 42.9% | 85.7% |
| 26 | 22 | 22 | 12 | 21 | 54.5% | 95.5% |
| 27 | 83 | 83 | 43 | 78 | 51.8% | 94.0% |
| 28 | 16 | 16 | 7 | 16 | 43.8% | 100.0% |
| 29 | 247 | 247 | 163 | 221 | 66.0% | 89.5% |
| 30 | 176 | 176 | 58 | 174 | 33.0% | 98.9% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| AA | 65 | 65 | 16 | 53 | 24.6% | 81.5% |
| AB | 12 | 12 | 5 | 10 | 41.7% | 83.3% |
| AC | 7 | 7 | 5 | 6 | 71.4% | 85.7% |
| AD | 16 | 16 | 11 | 13 | 68.8% | 81.2% |
| AE | 14 | 14 | 3 | 12 | 21.4% | 85.7% |
| AG | 8 | 8 | 4 | 6 | 50.0% | 75.0% |
| AH | 116 | 116 | 72 | 101 | 62.1% | 87.1% |
| AI | 114 | 114 | 72 | 99 | 63.2% | 86.8% |
| AJ | 18 | 18 | 6 | 15 | 33.3% | 83.3% |
| AK | 15 | 15 | 10 | 12 | 66.7% | 80.0% |
| AL | 56 | 56 | 36 | 50 | 64.3% | 89.3% |
| AM | 14 | 14 | 10 | 11 | 71.4% | 78.6% |
| AN | 13 | 13 | 8 | 10 | 61.5% | 76.9% |
| AO | 60 | 60 | 28 | 52 | 46.7% | 86.7% |
| AP | 8 | 8 | 4 | 7 | 50.0% | 87.5% |
| AT | 73 | 73 | 41 | 73 | 56.2% | 100.0% |
| AU | 144 | 144 | 108 | 143 | 75.0% | 99.3% |
| AW | 8 | 8 | 4 | 8 | 50.0% | 100.0% |
| AX | 66 | 66 | 30 | 60 | 45.5% | 90.9% |
| AY | 22 | 22 | 12 | 18 | 54.5% | 81.8% |
| AZ | 22 | 22 | 16 | 20 | 72.7% | 90.9% |
| CB | 29 | 29 | 15 | 23 | 51.7% | 79.3% |
| CF | 30 | 30 | 12 | 24 | 40.0% | 80.0% |
| CG | 27 | 27 | 12 | 21 | 44.4% | 77.8% |
| CH | 36 | 36 | 16 | 28 | 44.4% | 77.8% |
| CI | 20 | 20 | 10 | 19 | 50.0% | 95.0% |
| CN | 68 | 68 | 33 | 64 | 48.5% | 94.1% |
| CO | 72 | 72 | 53 | 63 | 73.6% | 87.5% |
| CR | 9 | 9 | 3 | 7 | 33.3% | 77.8% |
| CT | 24 | 24 | 12 | 22 | 50.0% | 91.7% |
| CU | 39 | 39 | 18 | 35 | 46.2% | 89.7% |
| CV | 61 | 61 | 25 | 55 | 41.0% | 90.2% |
| CW | 12 | 12 | 4 | 11 | 33.3% | 91.7% |
| CX | 64 | 64 | 31 | 58 | 48.4% | 90.6% |
| DATE | 3 | 2 | 2 | 2 | 100.0% | 100.0% |
| ED | 13 | 13 | 7 | 10 | 53.8% | 76.9% |
| GA | 24 | 24 | 18 | 24 | 75.0% | 100.0% |
| GD | 132 | 132 | 108 | 127 | 81.8% | 96.2% |
| GE | 7 | 7 | 4 | 7 | 57.1% | 100.0% |
| GF | 24 | 24 | 12 | 24 | 50.0% | 100.0% |
| GG | 102 | 102 | 48 | 97 | 47.1% | 95.1% |
| GH | 19 | 19 | 8 | 16 | 42.1% | 84.2% |
| GJ | 8 | 8 | 3 | 6 | 37.5% | 75.0% |
| GK | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| GL | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| GM | 22 | 22 | 8 | 19 | 36.4% | 86.4% |
| GN | 22 | 22 | 7 | 18 | 31.8% | 81.8% |
| GO | 15 | 15 | 5 | 12 | 33.3% | 80.0% |
| GP | 19 | 19 | 9 | 16 | 47.4% | 84.2% |
| GQ | 12 | 12 | 4 | 11 | 33.3% | 91.7% |
| GR | 12 | 12 | 4 | 11 | 33.3% | 91.7% |
| HAIL | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| IA | 16 | 16 | 6 | 16 | 37.5% | 100.0% |
| IB | 32 | 32 | 14 | 30 | 43.8% | 93.8% |
| IC | 23 | 23 | 12 | 23 | 52.2% | 100.0% |
| KA | 52 | 52 | 32 | 40 | 61.5% | 76.9% |
| KB | 39 | 39 | 21 | 30 | 53.8% | 76.9% |
| KC | 32 | 32 | 20 | 26 | 62.5% | 81.2% |
| KD | 26 | 26 | 12 | 20 | 46.2% | 76.9% |
| KE | 14 | 14 | 3 | 13 | 21.4% | 92.9% |
| KF | 8 | 8 | 3 | 7 | 37.5% | 87.5% |
| KG | 28 | 28 | 16 | 22 | 57.1% | 78.6% |
| MA | 10 | 10 | 4 | 10 | 40.0% | 100.0% |
| MD | 13 | 13 | 10 | 12 | 76.9% | 92.3% |
| ME | 9 | 9 | 5 | 9 | 55.6% | 100.0% |
| MF | 12 | 12 | 4 | 11 | 33.3% | 91.7% |
| MG | 12 | 12 | 4 | 11 | 33.3% | 91.7% |
| MH | 11 | 11 | 4 | 10 | 36.4% | 90.9% |
| MK | 15 | 15 | 12 | 14 | 80.0% | 93.3% |
| MV | 12 | 12 | 6 | 12 | 50.0% | 100.0% |
| MW | 4 | 4 | 2 | 4 | 50.0% | 100.0% |
| N | 58 | 58 | 1 | 58 | 1.7% | 100.0% |
| OA | 49 | 49 | 31 | 43 | 63.3% | 87.8% |
| OB | 28 | 28 | 13 | 28 | 46.4% | 100.0% |
| OC | 8 | 8 | 3 | 7 | 37.5% | 87.5% |
| OD | 54 | 54 | 42 | 48 | 77.8% | 88.9% |
| OE | 63 | 63 | 48 | 55 | 76.2% | 87.3% |
| RH | 39 | 39 | 24 | 35 | 61.5% | 89.7% |
| SA | 21 | 21 | 6 | 18 | 28.6% | 85.7% |
| ST | 22 | 22 | 13 | 21 | 59.1% | 95.5% |
| TMP | 2 | 2 | 1 | 2 | 50.0% | 100.0% |
| UA | 16 | 14 | 7 | 12 | 50.0% | 85.7% |
| UG | 24 | 24 | 10 | 24 | 41.7% | 100.0% |
| UNSPECIFIED | 50 | 48 | 0 | 42 | 0.0% | 87.5% |
| WA | 9 | 9 | 6 | 9 | 66.7% | 100.0% |
| WD | 20 | 20 | 14 | 20 | 70.0% | 100.0% |
| WG | 7 | 7 | 2 | 7 | 28.6% | 100.0% |
| WJ | 25 | 25 | 13 | 25 | 52.0% | 100.0% |
| WND | 51 | 51 | 42 | 44 | 82.4% | 86.3% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- |
| range | 323 | 248 | 108 | 76.8% | 33.4% |
| sentinel | 422 | 371 | 422 | 87.9% | 100.0% |
| allowed_quality | 82 | 75 | 82 | 91.5% | 100.0% |
| domain | 951 | 480 | 951 | 50.5% | 100.0% |
| cardinality | 122 | 102 | 122 | 83.6% | 100.0% |
| width | 656 | 21 | 656 | 3.2% | 100.0% |
| arity | 170 | 170 | 101 | 100.0% | 59.4% |
| unknown | 5 | 0 | 0 | excluded | excluded |

## Top gaps

| Part | Identifier | Rule type | Spec rule | Code impl | Tested | Implementation pointer | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | MIN 0000 MAX 2359 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | AU | width | POS 47-51 width 5 | FALSE | TRUE | src/noaa_climate_data/cleaning.py:603 | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | MIN 0000 MAX 2359 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | MIN 0 MAX 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | Enumerated codes near line 154 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for AU) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | Enumerated codes near line 250 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CI) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | Enumerated codes near line 19 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CO) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | Missing sentinels 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for GQ) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | Enumerated codes near line 104 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for IA) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | Enumerated codes near line 105 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested | Notes |
| --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | AU | width | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | DATE | unknown | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO8 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO9 | cardinality | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 09 | CT1 | range | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 10 | CU1 | range | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX1 | range | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
