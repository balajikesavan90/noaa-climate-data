# SPEC Coverage Report

## How to run

```bash
python tools/spec_coverage/generate_spec_coverage.py
# Fallback in environments without `python` alias:
python3 tools/spec_coverage/generate_spec_coverage.py
```

## Overall coverage

- Total spec rules extracted: **2702**
- Metric-eligible rules (excluding `unknown`): **2697**
- Unknown/noisy rows excluded from %: **5**
- Rules implemented in code: **1795** (66.6%)
- Rules with explicit tests: **2387** (88.5%)
- Expected-gap tagged rules: **133**
- Rows linked to unresolved `NEXT_STEPS.md` items: **2435**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Precision warnings

- Tested rows matched by `exact_signature`: **194** (8.1%)
- Tested rows matched by `exact_assertion`: **341** (14.3%)
- Tested rows matched by `family_assertion`: **934** (39.1%)
- Tested rows matched by `wildcard_assertion`: **918** (38.5%)
- Synthetic rows in CSV: **115**
- Synthetic gap rows in CSV: **29**
- Unknown rule rows excluded from percentages: **5**
- Arity rules tested: **128/191** (67.0%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0.0% | 0.0% |
| 02 | 31 | 30 | 12 | 23 | 40.0% | 76.7% |
| 03 | 47 | 47 | 28 | 40 | 59.6% | 85.1% |
| 04 | 749 | 749 | 452 | 621 | 60.3% | 82.9% |
| 05 | 247 | 247 | 204 | 235 | 82.6% | 95.1% |
| 06 | 105 | 105 | 66 | 94 | 62.9% | 89.5% |
| 07 | 30 | 30 | 24 | 27 | 80.0% | 90.0% |
| 08 | 10 | 10 | 6 | 8 | 60.0% | 80.0% |
| 09 | 25 | 25 | 19 | 23 | 76.0% | 92.0% |
| 10 | 40 | 40 | 28 | 36 | 70.0% | 90.0% |
| 11 | 62 | 62 | 35 | 56 | 56.5% | 90.3% |
| 12 | 13 | 13 | 7 | 12 | 53.8% | 92.3% |
| 13 | 65 | 65 | 41 | 59 | 63.1% | 90.8% |
| 14 | 14 | 14 | 9 | 11 | 64.3% | 78.6% |
| 15 | 390 | 390 | 283 | 369 | 72.6% | 94.6% |
| 16 | 10 | 10 | 4 | 7 | 40.0% | 70.0% |
| 17 | 11 | 11 | 4 | 8 | 36.4% | 72.7% |
| 18 | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| 19 | 20 | 20 | 13 | 17 | 65.0% | 85.0% |
| 20 | 13 | 13 | 6 | 12 | 46.2% | 92.3% |
| 21 | 13 | 13 | 6 | 12 | 46.2% | 92.3% |
| 22 | 8 | 8 | 6 | 6 | 75.0% | 75.0% |
| 23 | 72 | 72 | 51 | 70 | 70.8% | 97.2% |
| 24 | 189 | 189 | 134 | 150 | 70.9% | 79.4% |
| 25 | 7 | 7 | 6 | 6 | 85.7% | 85.7% |
| 26 | 23 | 23 | 17 | 18 | 73.9% | 78.3% |
| 27 | 83 | 83 | 61 | 76 | 73.5% | 91.6% |
| 28 | 19 | 19 | 15 | 19 | 78.9% | 100.0% |
| 29 | 248 | 248 | 180 | 222 | 72.6% | 89.5% |
| 30 | 140 | 140 | 69 | 138 | 49.3% | 98.6% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| AA | 209 | 209 | 56 | 157 | 26.8% | 75.1% |
| AH | 110 | 110 | 90 | 95 | 81.8% | 86.4% |
| AI | 228 | 228 | 180 | 193 | 78.9% | 84.6% |
| AL | 128 | 128 | 76 | 110 | 59.4% | 85.9% |
| AM | 18 | 18 | 13 | 14 | 72.2% | 77.8% |
| AO | 72 | 72 | 48 | 64 | 66.7% | 88.9% |
| AT | 33 | 33 | 33 | 33 | 100.0% | 100.0% |
| AU | 82 | 82 | 81 | 82 | 98.8% | 100.0% |
| AW | 8 | 8 | 7 | 8 | 87.5% | 100.0% |
| AX | 66 | 66 | 42 | 60 | 63.6% | 90.9% |
| AY | 22 | 22 | 16 | 18 | 72.7% | 81.8% |
| AZ | 22 | 22 | 18 | 20 | 81.8% | 90.9% |
| CB | 4 | 4 | 3 | 4 | 75.0% | 100.0% |
| CI | 20 | 20 | 13 | 19 | 65.0% | 95.0% |
| CN | 68 | 68 | 46 | 64 | 67.6% | 94.1% |
| CO | 23 | 23 | 20 | 21 | 87.0% | 91.3% |
| CR | 9 | 9 | 5 | 7 | 55.6% | 77.8% |
| CT | 24 | 24 | 18 | 22 | 75.0% | 91.7% |
| CU | 39 | 39 | 27 | 35 | 69.2% | 89.7% |
| CV | 61 | 61 | 34 | 55 | 55.7% | 90.2% |
| CW | 12 | 12 | 6 | 11 | 50.0% | 91.7% |
| CX | 64 | 64 | 40 | 58 | 62.5% | 90.6% |
| DATE | 2 | 1 | 0 | 1 | 0.0% | 100.0% |
| DEW | 36 | 36 | 4 | 34 | 11.1% | 94.4% |
| ED | 13 | 13 | 8 | 10 | 61.5% | 76.9% |
| GA | 26 | 26 | 26 | 26 | 100.0% | 100.0% |
| GD | 132 | 132 | 132 | 127 | 100.0% | 96.2% |
| GE | 2 | 2 | 2 | 2 | 100.0% | 100.0% |
| GF | 24 | 24 | 16 | 24 | 66.7% | 100.0% |
| GG | 198 | 198 | 102 | 183 | 51.5% | 92.4% |
| GH | 1 | 1 | 1 | 1 | 100.0% | 100.0% |
| GL | 2 | 2 | 1 | 2 | 50.0% | 100.0% |
| GN | 1 | 1 | 1 | 1 | 100.0% | 100.0% |
| GO | 1 | 1 | 1 | 1 | 100.0% | 100.0% |
| GP | 19 | 19 | 12 | 16 | 63.2% | 84.2% |
| GQ | 12 | 12 | 5 | 11 | 41.7% | 91.7% |
| GR | 15 | 15 | 6 | 14 | 40.0% | 93.3% |
| HAIL | 7 | 7 | 5 | 5 | 71.4% | 71.4% |
| IA | 16 | 16 | 12 | 16 | 75.0% | 100.0% |
| IB | 32 | 32 | 22 | 30 | 68.8% | 93.8% |
| IC | 23 | 23 | 16 | 23 | 69.6% | 100.0% |
| KA | 53 | 53 | 41 | 41 | 77.4% | 77.4% |
| KB | 39 | 39 | 30 | 30 | 76.9% | 76.9% |
| KC | 32 | 32 | 26 | 26 | 81.2% | 81.2% |
| KD | 26 | 26 | 18 | 20 | 69.2% | 76.9% |
| KE | 14 | 14 | 6 | 13 | 42.9% | 92.9% |
| KF | 8 | 8 | 6 | 7 | 75.0% | 87.5% |
| KG | 4 | 4 | 2 | 2 | 50.0% | 50.0% |
| MA | 11 | 11 | 8 | 11 | 72.7% | 100.0% |
| MD | 13 | 13 | 13 | 12 | 100.0% | 92.3% |
| ME | 9 | 9 | 7 | 9 | 77.8% | 100.0% |
| MF | 1 | 1 | 1 | 0 | 100.0% | 0.0% |
| MG | 12 | 12 | 7 | 11 | 58.3% | 91.7% |
| MH | 11 | 11 | 7 | 10 | 63.6% | 90.9% |
| MK | 15 | 15 | 14 | 14 | 93.3% | 93.3% |
| MV | 9 | 9 | 7 | 9 | 77.8% | 100.0% |
| MW | 13 | 13 | 10 | 13 | 76.9% | 100.0% |
| N | 14 | 14 | 8 | 14 | 57.1% | 100.0% |
| OA | 49 | 49 | 37 | 43 | 75.5% | 87.8% |
| OB | 28 | 28 | 14 | 28 | 50.0% | 100.0% |
| OC | 8 | 8 | 6 | 7 | 75.0% | 87.5% |
| OD | 54 | 54 | 36 | 48 | 66.7% | 88.9% |
| OE | 63 | 63 | 51 | 55 | 81.0% | 87.3% |
| RH | 40 | 40 | 31 | 36 | 77.5% | 90.0% |
| SA | 27 | 27 | 15 | 24 | 55.6% | 88.9% |
| SLP | 11 | 11 | 4 | 9 | 36.4% | 81.8% |
| ST | 8 | 8 | 5 | 6 | 62.5% | 75.0% |
| TIME | 7 | 7 | 4 | 6 | 57.1% | 85.7% |
| TMP | 2 | 2 | 1 | 2 | 50.0% | 100.0% |
| UA | 16 | 14 | 8 | 12 | 57.1% | 85.7% |
| UG | 24 | 24 | 10 | 24 | 41.7% | 100.0% |
| UNSPECIFIED | 90 | 88 | 50 | 68 | 56.8% | 77.3% |
| WA | 9 | 9 | 7 | 9 | 77.8% | 100.0% |
| WD | 20 | 20 | 15 | 20 | 75.0% | 100.0% |
| WG | 7 | 7 | 4 | 7 | 57.1% | 100.0% |
| WJ | 25 | 25 | 15 | 25 | 60.0% | 100.0% |
| WND | 46 | 46 | 27 | 39 | 58.7% | 84.8% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- |
| range | 361 | 116 | 114 | 32.1% | 31.6% |
| sentinel | 373 | 293 | 373 | 78.6% | 100.0% |
| allowed_quality | 89 | 87 | 89 | 97.8% | 100.0% |
| domain | 1015 | 460 | 1015 | 45.3% | 100.0% |
| cardinality | 123 | 103 | 123 | 83.7% | 100.0% |
| width | 545 | 545 | 545 | 100.0% | 100.0% |
| arity | 191 | 191 | 128 | 100.0% | 67.0% |
| unknown | 5 | 0 | 0 | excluded | excluded |

## Top gaps

| Part | Identifier | Rule type | Spec rule | Code impl | Tested | Implementation pointer | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | MIN 0000 MAX 2359 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 26 | AM | range | MIN -1100 MAX 0630 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for AM) | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV1 | range | MIN 0000 MAX 2359 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 20 | GQ1 | range | MIN 0001 MAX 9998 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for GQ) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 21 | GR1 | range | MIN 0001 MAX 9998 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for GR) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | MIN 1 MAX 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 27 | MK1 | range | MIN 010000 MAX 312359 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for MK) | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 02 | AU | domain | Enumerated codes near line 154 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for AU) | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 05 | MW | domain | Enumerated codes near line 61 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for MW) | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | Enumerated codes near line 250 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CI) | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested | Notes |
| --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | FALSE | FALSE | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 26 | AM | range | FALSE | FALSE | coverage_reason=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 20 | GQ1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 21 | GR1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 27 | MK1 | range | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 02 | AU | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 05 | MW | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | TIME | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 15 | CB | sentinel | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 15 | GF1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 29 | RH1 | domain | FALSE | TRUE | coverage_reason=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | DATE | unknown | FALSE | FALSE | coverage_reason=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | coverage_reason=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | coverage_reason=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_for_row()` for new implementation metadata fields.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
