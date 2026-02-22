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
- Rules implemented in code: **2079** (76.3%)
- Rules with explicit tests: **2442** (89.6%)
- Expected-gap tagged rules: **107**
- Rows linked to unresolved `NEXT_STEPS.md` items: **2504**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

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
| 02 | 39 | 38 | 15 | 30 | 39.5% | 78.9% |
| 03 | 47 | 47 | 28 | 40 | 59.6% | 85.1% |
| 04 | 525 | 525 | 413 | 446 | 78.7% | 85.0% |
| 05 | 326 | 326 | 293 | 314 | 89.9% | 96.3% |
| 06 | 209 | 209 | 149 | 178 | 71.3% | 85.2% |
| 07 | 72 | 72 | 71 | 63 | 98.6% | 87.5% |
| 08 | 10 | 10 | 6 | 8 | 60.0% | 80.0% |
| 09 | 25 | 25 | 19 | 23 | 76.0% | 92.0% |
| 10 | 40 | 40 | 28 | 36 | 70.0% | 90.0% |
| 11 | 62 | 62 | 35 | 56 | 56.5% | 90.3% |
| 12 | 13 | 13 | 7 | 12 | 53.8% | 92.3% |
| 13 | 65 | 65 | 41 | 59 | 63.1% | 90.8% |
| 14 | 14 | 14 | 11 | 11 | 78.6% | 78.6% |
| 15 | 309 | 309 | 262 | 296 | 84.8% | 95.8% |
| 16 | 23 | 23 | 17 | 17 | 73.9% | 73.9% |
| 17 | 44 | 44 | 22 | 37 | 50.0% | 84.1% |
| 18 | 15 | 15 | 7 | 12 | 46.7% | 80.0% |
| 19 | 20 | 20 | 13 | 17 | 65.0% | 85.0% |
| 20 | 13 | 13 | 7 | 12 | 53.8% | 92.3% |
| 21 | 13 | 13 | 7 | 12 | 53.8% | 92.3% |
| 22 | 8 | 8 | 6 | 6 | 75.0% | 75.0% |
| 23 | 72 | 72 | 51 | 70 | 70.8% | 97.2% |
| 24 | 200 | 200 | 155 | 159 | 77.5% | 79.5% |
| 25 | 7 | 7 | 6 | 6 | 85.7% | 85.7% |
| 26 | 22 | 22 | 17 | 21 | 77.3% | 95.5% |
| 27 | 83 | 83 | 65 | 78 | 78.3% | 94.0% |
| 28 | 16 | 16 | 12 | 16 | 75.0% | 100.0% |
| 29 | 247 | 247 | 210 | 221 | 85.0% | 89.5% |
| 30 | 176 | 176 | 96 | 174 | 54.5% | 98.9% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| AA | 65 | 65 | 32 | 53 | 49.2% | 81.5% |
| AB | 12 | 12 | 8 | 10 | 66.7% | 83.3% |
| AC | 7 | 7 | 7 | 6 | 100.0% | 85.7% |
| AD | 16 | 16 | 15 | 13 | 93.8% | 81.2% |
| AE | 14 | 14 | 6 | 12 | 42.9% | 85.7% |
| AG | 8 | 8 | 6 | 6 | 75.0% | 75.0% |
| AH | 116 | 116 | 102 | 101 | 87.9% | 87.1% |
| AI | 114 | 114 | 102 | 99 | 89.5% | 86.8% |
| AJ | 18 | 18 | 10 | 15 | 55.6% | 83.3% |
| AK | 15 | 15 | 14 | 12 | 93.3% | 80.0% |
| AL | 56 | 56 | 48 | 50 | 85.7% | 89.3% |
| AM | 14 | 14 | 13 | 11 | 92.9% | 78.6% |
| AN | 13 | 13 | 11 | 10 | 84.6% | 76.9% |
| AO | 60 | 60 | 44 | 52 | 73.3% | 86.7% |
| AP | 8 | 8 | 6 | 7 | 75.0% | 87.5% |
| AT | 73 | 73 | 65 | 73 | 89.0% | 100.0% |
| AU | 144 | 144 | 138 | 143 | 95.8% | 99.3% |
| AW | 8 | 8 | 7 | 8 | 87.5% | 100.0% |
| AX | 66 | 66 | 48 | 60 | 72.7% | 90.9% |
| AY | 22 | 22 | 18 | 18 | 81.8% | 81.8% |
| AZ | 22 | 22 | 20 | 20 | 90.9% | 90.9% |
| CB | 29 | 29 | 23 | 23 | 79.3% | 79.3% |
| CF | 30 | 30 | 21 | 24 | 70.0% | 80.0% |
| CG | 27 | 27 | 21 | 21 | 77.8% | 77.8% |
| CH | 36 | 36 | 26 | 28 | 72.2% | 77.8% |
| CI | 20 | 20 | 13 | 19 | 65.0% | 95.0% |
| CN | 68 | 68 | 46 | 64 | 67.6% | 94.1% |
| CO | 72 | 72 | 71 | 63 | 98.6% | 87.5% |
| CR | 9 | 9 | 5 | 7 | 55.6% | 77.8% |
| CT | 24 | 24 | 18 | 22 | 75.0% | 91.7% |
| CU | 39 | 39 | 27 | 35 | 69.2% | 89.7% |
| CV | 61 | 61 | 34 | 55 | 55.7% | 90.2% |
| CW | 12 | 12 | 6 | 11 | 50.0% | 91.7% |
| CX | 64 | 64 | 40 | 58 | 62.5% | 90.6% |
| DATE | 3 | 2 | 0 | 2 | 0.0% | 100.0% |
| ED | 13 | 13 | 10 | 10 | 76.9% | 76.9% |
| GA | 24 | 24 | 24 | 24 | 100.0% | 100.0% |
| GD | 132 | 132 | 132 | 127 | 100.0% | 96.2% |
| GE | 7 | 7 | 7 | 7 | 100.0% | 100.0% |
| GF | 24 | 24 | 16 | 24 | 66.7% | 100.0% |
| GG | 102 | 102 | 72 | 97 | 70.6% | 95.1% |
| GH | 19 | 19 | 10 | 16 | 52.6% | 84.2% |
| GJ | 8 | 8 | 6 | 6 | 75.0% | 75.0% |
| GK | 7 | 7 | 5 | 5 | 71.4% | 71.4% |
| GL | 7 | 7 | 5 | 5 | 71.4% | 71.4% |
| GM | 22 | 22 | 12 | 19 | 54.5% | 86.4% |
| GN | 22 | 22 | 10 | 18 | 45.5% | 81.8% |
| GO | 15 | 15 | 7 | 12 | 46.7% | 80.0% |
| GP | 19 | 19 | 12 | 16 | 63.2% | 84.2% |
| GQ | 12 | 12 | 6 | 11 | 50.0% | 91.7% |
| GR | 12 | 12 | 6 | 11 | 50.0% | 91.7% |
| HAIL | 7 | 7 | 5 | 5 | 71.4% | 71.4% |
| IA | 16 | 16 | 12 | 16 | 75.0% | 100.0% |
| IB | 32 | 32 | 22 | 30 | 68.8% | 93.8% |
| IC | 23 | 23 | 16 | 23 | 69.6% | 100.0% |
| KA | 52 | 52 | 44 | 40 | 84.6% | 76.9% |
| KB | 39 | 39 | 30 | 30 | 76.9% | 76.9% |
| KC | 32 | 32 | 28 | 26 | 87.5% | 81.2% |
| KD | 26 | 26 | 18 | 20 | 69.2% | 76.9% |
| KE | 14 | 14 | 6 | 13 | 42.9% | 92.9% |
| KF | 8 | 8 | 6 | 7 | 75.0% | 87.5% |
| KG | 28 | 28 | 22 | 22 | 78.6% | 78.6% |
| MA | 10 | 10 | 7 | 10 | 70.0% | 100.0% |
| MD | 13 | 13 | 13 | 12 | 100.0% | 92.3% |
| ME | 9 | 9 | 8 | 9 | 88.9% | 100.0% |
| MF | 12 | 12 | 7 | 11 | 58.3% | 91.7% |
| MG | 12 | 12 | 7 | 11 | 58.3% | 91.7% |
| MH | 11 | 11 | 7 | 10 | 63.6% | 90.9% |
| MK | 15 | 15 | 15 | 14 | 100.0% | 93.3% |
| MV | 12 | 12 | 9 | 12 | 75.0% | 100.0% |
| MW | 4 | 4 | 3 | 4 | 75.0% | 100.0% |
| N | 58 | 58 | 6 | 58 | 10.3% | 100.0% |
| OA | 49 | 49 | 43 | 43 | 87.8% | 87.8% |
| OB | 28 | 28 | 18 | 28 | 64.3% | 100.0% |
| OC | 8 | 8 | 6 | 7 | 75.0% | 87.5% |
| OD | 54 | 54 | 45 | 48 | 83.3% | 88.9% |
| OE | 63 | 63 | 63 | 55 | 100.0% | 87.3% |
| RH | 39 | 39 | 30 | 35 | 76.9% | 89.7% |
| SA | 21 | 21 | 13 | 18 | 61.9% | 85.7% |
| ST | 22 | 22 | 17 | 21 | 77.3% | 95.5% |
| TMP | 2 | 2 | 1 | 2 | 50.0% | 100.0% |
| UA | 16 | 14 | 10 | 12 | 71.4% | 85.7% |
| UG | 24 | 24 | 16 | 24 | 66.7% | 100.0% |
| UNSPECIFIED | 50 | 48 | 37 | 42 | 77.1% | 87.5% |
| WA | 9 | 9 | 8 | 9 | 88.9% | 100.0% |
| WD | 20 | 20 | 17 | 20 | 85.0% | 100.0% |
| WG | 7 | 7 | 5 | 7 | 71.4% | 100.0% |
| WJ | 25 | 25 | 18 | 25 | 72.0% | 100.0% |
| WND | 51 | 51 | 30 | 44 | 58.8% | 86.3% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- |
| range | 323 | 248 | 108 | 76.8% | 33.4% |
| sentinel | 422 | 371 | 422 | 87.9% | 100.0% |
| allowed_quality | 82 | 75 | 82 | 91.5% | 100.0% |
| domain | 951 | 457 | 951 | 48.1% | 100.0% |
| cardinality | 122 | 102 | 122 | 83.6% | 100.0% |
| width | 656 | 656 | 656 | 100.0% | 100.0% |
| arity | 170 | 170 | 101 | 100.0% | 59.4% |
| unknown | 5 | 0 | 0 | excluded | excluded |

## Top gaps

| Part | Identifier | Rule type | Spec rule | Code impl | Tested | Implementation pointer | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | MIN 0000 MAX 2359 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV1 | range | MIN 0000 MAX 2359 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | MIN 0 MAX 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | Enumerated codes near line 154 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for AU) | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | Enumerated codes near line 250 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CI) | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | Enumerated codes near line 19 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CO) | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | Missing sentinels 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for GQ) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | Enumerated codes near line 104 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for IA) | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | Enumerated codes near line 105 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | MIN -9999 MAX 9998 | TRUE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CT) | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested | Notes |
| --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | FALSE | FALSE | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | DATE | unknown | FALSE | FALSE | coverage_reason=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 02 | AU | width | TRUE | TRUE | coverage_reason=strict_gate_width;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO8 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO9 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 09 | CT1 | range | TRUE | TRUE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 10 | CU1 | range | TRUE | TRUE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX1 | range | TRUE | TRUE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_for_row()` for new implementation metadata fields.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
