# SPEC Coverage Report

## How to run

```bash
python tools/spec_coverage/generate_spec_coverage.py
# Fallback in environments without `python` alias:
python3 tools/spec_coverage/generate_spec_coverage.py
```

## Overall coverage

- Total spec rules extracted: **3592**
- Synthetic rows excluded from coverage metrics: **29**
- Metric-eligible rules (excluding `unknown`): **3592**
- Unknown/noisy rows excluded from %: **0**
- Rules implemented in code: **1717** (47.8%)
- Rules with explicit tests: **3277** (91.2%)
- Expected-gap tagged rules: **114**
- Rows linked to unresolved `NEXT_STEPS.md` items: **3368**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **1666** (46.4%)
- cleaning_only: **21** (0.6%)
- both: **30** (0.8%)
- neither: **1875** (52.2%)

## Confidence breakdown

- Cleaning-implemented metric rules: **51** (1.4%)
- high: **0** (0.0%)
- medium: **51** (100.0%)
- low: **0** (0.0%)

## Precision warnings

- Tested rows matched by `exact_signature`: **275** (8.4%)
- Tested rows matched by `exact_assertion`: **376** (11.5%)
- Tested rows matched by `family_assertion`: **784** (23.9%)
- Tested rows matched by `wildcard_assertion`: **1842** (56.2%)
- Synthetic rows in CSV: **29**
- Synthetic gap rows in CSV: **29**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested: **102/171** (59.6%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0.0% | 0.0% |
| 02 | 38 | 38 | 0 | 30 | 0.0% | 78.9% |
| 03 | 53 | 53 | 42 | 46 | 79.2% | 86.8% |
| 04 | 603 | 603 | 302 | 517 | 50.1% | 85.7% |
| 05 | 450 | 450 | 261 | 438 | 58.0% | 97.3% |
| 06 | 287 | 287 | 114 | 256 | 39.7% | 89.2% |
| 07 | 74 | 74 | 53 | 65 | 71.6% | 87.8% |
| 08 | 11 | 11 | 3 | 9 | 27.3% | 81.8% |
| 09 | 28 | 28 | 12 | 26 | 42.9% | 92.9% |
| 10 | 55 | 55 | 21 | 51 | 38.2% | 92.7% |
| 11 | 109 | 109 | 33 | 101 | 30.3% | 92.7% |
| 12 | 20 | 20 | 5 | 18 | 25.0% | 90.0% |
| 13 | 109 | 109 | 39 | 101 | 35.8% | 92.7% |
| 14 | 15 | 15 | 7 | 12 | 46.7% | 80.0% |
| 15 | 472 | 472 | 252 | 452 | 53.4% | 95.8% |
| 16 | 24 | 24 | 9 | 18 | 37.5% | 75.0% |
| 17 | 84 | 84 | 30 | 71 | 35.7% | 84.5% |
| 18 | 27 | 27 | 9 | 22 | 33.3% | 81.5% |
| 19 | 38 | 38 | 20 | 31 | 52.6% | 81.6% |
| 20 | 20 | 20 | 7 | 19 | 35.0% | 95.0% |
| 21 | 20 | 20 | 7 | 19 | 35.0% | 95.0% |
| 22 | 8 | 8 | 3 | 6 | 37.5% | 75.0% |
| 23 | 109 | 109 | 44 | 107 | 40.4% | 98.2% |
| 24 | 244 | 244 | 119 | 203 | 48.8% | 83.2% |
| 25 | 7 | 7 | 3 | 6 | 42.9% | 85.7% |
| 26 | 29 | 29 | 14 | 28 | 48.3% | 96.6% |
| 27 | 109 | 109 | 52 | 104 | 47.7% | 95.4% |
| 28 | 19 | 19 | 9 | 19 | 47.4% | 100.0% |
| 29 | 306 | 306 | 178 | 280 | 58.2% | 91.5% |
| 30 | 224 | 224 | 69 | 222 | 30.8% | 99.1% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- | --- |
| AA | 68 | 68 | 16 | 56 | 23.5% | 82.4% |
| AB | 12 | 12 | 4 | 10 | 33.3% | 83.3% |
| AC | 10 | 10 | 6 | 9 | 60.0% | 90.0% |
| AD | 23 | 23 | 13 | 18 | 56.5% | 78.3% |
| AE | 26 | 26 | 9 | 21 | 34.6% | 80.8% |
| AG | 9 | 9 | 4 | 7 | 44.4% | 77.8% |
| AH | 126 | 126 | 72 | 111 | 57.1% | 88.1% |
| AI | 126 | 126 | 72 | 111 | 57.1% | 88.1% |
| AJ | 22 | 22 | 7 | 19 | 31.8% | 86.4% |
| AK | 16 | 16 | 10 | 13 | 62.5% | 81.2% |
| AL | 64 | 64 | 36 | 58 | 56.2% | 90.6% |
| AM | 23 | 23 | 13 | 18 | 56.5% | 78.3% |
| AN | 15 | 15 | 8 | 12 | 53.3% | 80.0% |
| AO | 64 | 64 | 28 | 56 | 43.8% | 87.5% |
| AP | 9 | 9 | 4 | 8 | 44.4% | 88.9% |
| AT | 80 | 80 | 40 | 80 | 50.0% | 100.0% |
| AU | 235 | 235 | 153 | 234 | 65.1% | 99.6% |
| AW | 8 | 8 | 4 | 8 | 50.0% | 100.0% |
| AX | 84 | 84 | 36 | 78 | 42.9% | 92.9% |
| AY | 26 | 26 | 12 | 22 | 46.2% | 84.6% |
| AZ | 26 | 26 | 16 | 24 | 61.5% | 92.3% |
| CB | 28 | 28 | 12 | 22 | 42.9% | 78.6% |
| CF | 33 | 33 | 12 | 27 | 36.4% | 81.8% |
| CG | 30 | 30 | 12 | 24 | 40.0% | 80.0% |
| CH | 46 | 46 | 18 | 38 | 39.1% | 82.6% |
| CI | 36 | 36 | 13 | 35 | 36.1% | 97.2% |
| CN | 113 | 113 | 47 | 109 | 41.6% | 96.5% |
| CO | 73 | 73 | 53 | 64 | 72.6% | 87.7% |
| CR | 10 | 10 | 3 | 8 | 30.0% | 80.0% |
| CT | 27 | 27 | 12 | 25 | 44.4% | 92.6% |
| CU | 54 | 54 | 21 | 50 | 38.9% | 92.6% |
| CV | 108 | 108 | 33 | 100 | 30.6% | 92.6% |
| CW | 19 | 19 | 5 | 17 | 26.3% | 89.5% |
| CX | 108 | 108 | 39 | 100 | 36.1% | 92.6% |
| ED | 14 | 14 | 7 | 11 | 50.0% | 78.6% |
| GA | 24 | 24 | 18 | 24 | 75.0% | 100.0% |
| GD | 216 | 216 | 138 | 206 | 63.9% | 95.4% |
| GE | 11 | 11 | 6 | 11 | 54.5% | 100.0% |
| GF | 39 | 39 | 17 | 39 | 43.6% | 100.0% |
| GG | 144 | 144 | 60 | 139 | 41.7% | 96.5% |
| GH | 37 | 37 | 13 | 32 | 35.1% | 86.5% |
| GJ | 8 | 8 | 3 | 6 | 37.5% | 75.0% |
| GK | 8 | 8 | 3 | 6 | 37.5% | 75.0% |
| GL | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| GM | 43 | 43 | 17 | 37 | 39.5% | 86.0% |
| GN | 40 | 40 | 13 | 33 | 32.5% | 82.5% |
| GO | 26 | 26 | 9 | 21 | 34.6% | 80.8% |
| GP | 37 | 37 | 20 | 30 | 54.1% | 81.1% |
| GQ | 19 | 19 | 7 | 18 | 36.8% | 94.7% |
| GR | 19 | 19 | 7 | 18 | 36.8% | 94.7% |
| HAIL | 7 | 7 | 3 | 5 | 42.9% | 71.4% |
| IA | 16 | 16 | 6 | 16 | 37.5% | 100.0% |
| IB | 54 | 54 | 20 | 52 | 37.0% | 96.3% |
| IC | 38 | 38 | 18 | 38 | 47.4% | 100.0% |
| KA | 60 | 60 | 32 | 48 | 53.3% | 80.0% |
| KB | 45 | 45 | 21 | 36 | 46.7% | 80.0% |
| KC | 38 | 38 | 22 | 32 | 57.9% | 84.2% |
| KD | 30 | 30 | 12 | 24 | 40.0% | 80.0% |
| KE | 26 | 26 | 9 | 25 | 34.6% | 96.2% |
| KF | 8 | 8 | 3 | 7 | 37.5% | 87.5% |
| KG | 36 | 36 | 20 | 30 | 55.6% | 83.3% |
| MA | 13 | 13 | 5 | 13 | 38.5% | 100.0% |
| MD | 18 | 18 | 11 | 17 | 61.1% | 94.4% |
| ME | 10 | 10 | 5 | 10 | 50.0% | 100.0% |
| MF | 16 | 16 | 5 | 15 | 31.2% | 93.8% |
| MG | 15 | 15 | 5 | 14 | 33.3% | 93.3% |
| MH | 14 | 14 | 5 | 13 | 35.7% | 92.9% |
| MK | 22 | 22 | 16 | 21 | 72.7% | 95.5% |
| MV | 14 | 14 | 7 | 14 | 50.0% | 100.0% |
| MW | 4 | 4 | 2 | 4 | 50.0% | 100.0% |
| N | 63 | 63 | 0 | 63 | 0.0% | 100.0% |
| OA | 51 | 51 | 30 | 45 | 58.8% | 88.2% |
| OB | 48 | 48 | 16 | 48 | 33.3% | 100.0% |
| OC | 8 | 8 | 3 | 7 | 37.5% | 87.5% |
| OD | 63 | 63 | 45 | 57 | 71.4% | 90.5% |
| OE | 69 | 69 | 48 | 61 | 69.6% | 88.4% |
| RH | 60 | 60 | 33 | 56 | 55.0% | 93.3% |
| SA | 22 | 22 | 6 | 19 | 27.3% | 86.4% |
| ST | 28 | 28 | 14 | 27 | 50.0% | 96.4% |
| UA | 19 | 19 | 8 | 17 | 42.1% | 89.5% |
| UG | 30 | 30 | 12 | 30 | 40.0% | 100.0% |
| UNSPECIFIED | 47 | 47 | 0 | 41 | 0.0% | 87.2% |
| WA | 13 | 13 | 7 | 13 | 53.8% | 100.0% |
| WD | 35 | 35 | 20 | 35 | 57.1% | 100.0% |
| WG | 11 | 11 | 2 | 11 | 18.2% | 100.0% |
| WJ | 35 | 35 | 15 | 35 | 42.9% | 100.0% |
| WND | 57 | 57 | 47 | 50 | 82.5% | 87.7% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested | Implemented % | Tested % |
| --- | --- | --- | --- | --- | --- |
| range | 364 | 286 | 118 | 78.6% | 32.4% |
| sentinel | 691 | 579 | 691 | 83.8% | 100.0% |
| allowed_quality | 82 | 75 | 82 | 91.5% | 100.0% |
| domain | 946 | 476 | 946 | 50.3% | 100.0% |
| cardinality | 128 | 109 | 128 | 85.2% | 100.0% |
| width | 1210 | 21 | 1210 | 1.7% | 100.0% |
| arity | 171 | 171 | 102 | 100.0% | 59.6% |
| unknown | 0 | 0 | 0 | excluded | excluded |

## Top gaps

| Part | Identifier | Rule type | Spec rule | Code impl | Tested | Implementation pointer | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | MIN 0000 MAX 2359 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | MIN 0000 MAX 2359 | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | AU | width | POS 47-51 width 5 | FALSE | TRUE | src/noaa_climate_data/cleaning.py:603 | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | MIN 0000 MAX 2359 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | MIN 01 MAX 99 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | Enumerated codes near line 154 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for AU) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | Enumerated codes near line 250 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CI) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | Enumerated codes near line 19 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CO) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | Missing sentinels 9 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for GQ) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | Enumerated codes near line 104 | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for IA) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested | Notes |
| --- | --- | --- | --- | --- | --- |
| 11 | CV2 | range | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | AU | width | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 23 | IB1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | IB1 | sentinel | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
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

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
