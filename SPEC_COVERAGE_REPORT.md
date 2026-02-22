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
- Tested (strict): **1443** (40.2%)
- Tested (any): **3277** (91.2%)
- `test_covered` in CSV mirrors `test_covered_any` for backward compatibility.
- Expected-gap tagged rules: **114**
- Rows linked to unresolved `NEXT_STEPS.md` items: **3368**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **1241** (34.5%)
- cleaning_only: **21** (0.6%)
- both: **455** (12.7%)
- neither: **1875** (52.2%)

## Confidence breakdown

- Cleaning-implemented metric rules: **476** (13.3%)
- high: **0** (0.0%)
- medium: **476** (100.0%)
- low: **0** (0.0%)

## Match quality

| Match strength | Count | % of metric rules |
| --- | --- | --- |
| exact_signature | 289 | 8.0% |
| exact_assertion | 375 | 10.4% |
| family_assertion | 779 | 21.7% |
| wildcard_assertion | 1834 | 51.1% |
| none | 315 | 8.8% |

## Precision warnings

- Wildcard policy: `wildcard_assertion` counts as tested-any only; it never counts as strict.
- Tested-any rows matched by `exact_signature`: **289** (8.8%)
- Tested-any rows matched by `exact_assertion`: **375** (11.4%)
- Tested-any rows matched by `family_assertion`: **779** (23.8%)
- Tested-any rows matched by `wildcard_assertion`: **1834** (56.0%)
- Synthetic rows in CSV: **29**
- Synthetic gap rows in CSV: **29**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested (strict): **102/171** (59.6%)
- Arity rules tested (any): **102/171** (59.6%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Suspicious coverage

- tested_any=TRUE and code_implemented=FALSE: **1809** (50.4%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-02-control-data-section.md:7-7::UNSPECIFIED::width::0677af5a69 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:13-13::UNSPECIFIED::width::e4960d47dd | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:19-19::UNSPECIFIED::width::974abc75d9 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:32-32::UNSPECIFIED::width::47b38e688f | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:39-39::UNSPECIFIED::width::cf444da7a0 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:47-47::UNSPECIFIED::width::e023ac762f | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:87-87::UNSPECIFIED::sentinel::0006a4e09e | UNSPECIFIED | sentinel | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:93-93::UNSPECIFIED::width::3da8034b39 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:100-100::UNSPECIFIED::sentinel::e0e972235a | UNSPECIFIED | sentinel | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:102-102::UNSPECIFIED::width::e38868682e | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |

- tested_any=TRUE and match_strength=`wildcard_assertion`: **1834** (51.1%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-02-control-data-section.md:7-7::UNSPECIFIED::width::0677af5a69 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:13-13::UNSPECIFIED::width::e4960d47dd | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:19-19::UNSPECIFIED::width::974abc75d9 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:32-32::UNSPECIFIED::width::47b38e688f | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:39-39::UNSPECIFIED::width::cf444da7a0 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:47-47::UNSPECIFIED::width::e023ac762f | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:87-87::UNSPECIFIED::sentinel::0006a4e09e | UNSPECIFIED | sentinel | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:93-93::UNSPECIFIED::width::3da8034b39 | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:100-100::UNSPECIFIED::sentinel::e0e972235a | UNSPECIFIED | sentinel | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-02-control-data-section.md:102-102::UNSPECIFIED::width::e38868682e | UNSPECIFIED | width | coverage_reason_cleaning=none;coverage_reason_constants=none;synthetic_unmapped;test_match=wildcard_assertion;unresolved_in_next_steps |

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested strict | Tested any | Implemented % | Tested strict % | Tested any % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| 02 | 38 | 38 | 0 | 7 | 30 | 0.0% | 18.4% | 78.9% |
| 03 | 53 | 53 | 42 | 45 | 46 | 79.2% | 84.9% | 86.8% |
| 04 | 603 | 603 | 302 | 232 | 517 | 50.1% | 38.5% | 85.7% |
| 05 | 450 | 450 | 261 | 256 | 438 | 58.0% | 56.9% | 97.3% |
| 06 | 287 | 287 | 114 | 56 | 256 | 39.7% | 19.5% | 89.2% |
| 07 | 74 | 74 | 53 | 45 | 65 | 71.6% | 60.8% | 87.8% |
| 08 | 11 | 11 | 3 | 1 | 9 | 27.3% | 9.1% | 81.8% |
| 09 | 28 | 28 | 12 | 10 | 26 | 42.9% | 35.7% | 92.9% |
| 10 | 55 | 55 | 21 | 20 | 51 | 38.2% | 36.4% | 92.7% |
| 11 | 109 | 109 | 33 | 64 | 101 | 30.3% | 58.7% | 92.7% |
| 12 | 20 | 20 | 5 | 11 | 18 | 25.0% | 55.0% | 90.0% |
| 13 | 109 | 109 | 39 | 40 | 101 | 35.8% | 36.7% | 92.7% |
| 14 | 15 | 15 | 7 | 3 | 12 | 46.7% | 20.0% | 80.0% |
| 15 | 472 | 472 | 252 | 220 | 452 | 53.4% | 46.6% | 95.8% |
| 16 | 24 | 24 | 9 | 0 | 18 | 37.5% | 0.0% | 75.0% |
| 17 | 84 | 84 | 30 | 0 | 71 | 35.7% | 0.0% | 84.5% |
| 18 | 27 | 27 | 9 | 0 | 22 | 33.3% | 0.0% | 81.5% |
| 19 | 38 | 38 | 20 | 10 | 31 | 52.6% | 26.3% | 81.6% |
| 20 | 20 | 20 | 7 | 8 | 19 | 35.0% | 40.0% | 95.0% |
| 21 | 20 | 20 | 7 | 8 | 19 | 35.0% | 40.0% | 95.0% |
| 22 | 8 | 8 | 3 | 1 | 6 | 37.5% | 12.5% | 75.0% |
| 23 | 109 | 109 | 44 | 26 | 107 | 40.4% | 23.9% | 98.2% |
| 24 | 244 | 244 | 119 | 11 | 203 | 48.8% | 4.5% | 83.2% |
| 25 | 7 | 7 | 3 | 1 | 6 | 42.9% | 14.3% | 85.7% |
| 26 | 29 | 29 | 14 | 18 | 28 | 48.3% | 62.1% | 96.6% |
| 27 | 109 | 109 | 52 | 34 | 104 | 47.7% | 31.2% | 95.4% |
| 28 | 19 | 19 | 9 | 12 | 19 | 47.4% | 63.2% | 100.0% |
| 29 | 306 | 306 | 178 | 161 | 280 | 58.2% | 52.6% | 91.5% |
| 30 | 224 | 224 | 69 | 143 | 222 | 30.8% | 63.8% | 99.1% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested strict | Tested any | Implemented % | Tested strict % | Tested any % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AA | 68 | 68 | 16 | 20 | 56 | 23.5% | 29.4% | 82.4% |
| AB | 12 | 12 | 4 | 0 | 10 | 33.3% | 0.0% | 83.3% |
| AC | 10 | 10 | 6 | 0 | 9 | 60.0% | 0.0% | 90.0% |
| AD | 23 | 23 | 13 | 0 | 18 | 56.5% | 0.0% | 78.3% |
| AE | 26 | 26 | 9 | 0 | 21 | 34.6% | 0.0% | 80.8% |
| AG | 9 | 9 | 4 | 0 | 7 | 44.4% | 0.0% | 77.8% |
| AH | 126 | 126 | 72 | 69 | 111 | 57.1% | 54.8% | 88.1% |
| AI | 126 | 126 | 72 | 69 | 111 | 57.1% | 54.8% | 88.1% |
| AJ | 22 | 22 | 7 | 0 | 19 | 31.8% | 0.0% | 86.4% |
| AK | 16 | 16 | 10 | 0 | 13 | 62.5% | 0.0% | 81.2% |
| AL | 64 | 64 | 36 | 38 | 58 | 56.2% | 59.4% | 90.6% |
| AM | 23 | 23 | 13 | 0 | 18 | 56.5% | 0.0% | 78.3% |
| AN | 15 | 15 | 8 | 0 | 12 | 53.3% | 0.0% | 80.0% |
| AO | 64 | 64 | 28 | 36 | 56 | 43.8% | 56.2% | 87.5% |
| AP | 9 | 9 | 4 | 0 | 8 | 44.4% | 0.0% | 88.9% |
| AT | 80 | 80 | 40 | 48 | 80 | 50.0% | 60.0% | 100.0% |
| AU | 235 | 235 | 153 | 159 | 234 | 65.1% | 67.7% | 99.6% |
| AW | 8 | 8 | 4 | 5 | 8 | 50.0% | 62.5% | 100.0% |
| AX | 84 | 84 | 36 | 36 | 78 | 42.9% | 42.9% | 92.9% |
| AY | 26 | 26 | 12 | 0 | 22 | 46.2% | 0.0% | 84.6% |
| AZ | 26 | 26 | 16 | 14 | 24 | 61.5% | 53.8% | 92.3% |
| CB | 28 | 28 | 12 | 0 | 22 | 42.9% | 0.0% | 78.6% |
| CF | 33 | 33 | 12 | 0 | 27 | 36.4% | 0.0% | 81.8% |
| CG | 30 | 30 | 12 | 0 | 24 | 40.0% | 0.0% | 80.0% |
| CH | 46 | 46 | 18 | 0 | 38 | 39.1% | 0.0% | 82.6% |
| CI | 36 | 36 | 13 | 8 | 35 | 36.1% | 22.2% | 97.2% |
| CN | 113 | 113 | 47 | 48 | 109 | 41.6% | 42.5% | 96.5% |
| CO | 73 | 73 | 53 | 45 | 64 | 72.6% | 61.6% | 87.7% |
| CR | 10 | 10 | 3 | 1 | 8 | 30.0% | 10.0% | 80.0% |
| CT | 27 | 27 | 12 | 10 | 25 | 44.4% | 37.0% | 92.6% |
| CU | 54 | 54 | 21 | 20 | 50 | 38.9% | 37.0% | 92.6% |
| CV | 108 | 108 | 33 | 64 | 100 | 30.6% | 59.3% | 92.6% |
| CW | 19 | 19 | 5 | 11 | 17 | 26.3% | 57.9% | 89.5% |
| CX | 108 | 108 | 39 | 40 | 100 | 36.1% | 37.0% | 92.6% |
| ED | 14 | 14 | 7 | 3 | 11 | 50.0% | 21.4% | 78.6% |
| GA | 24 | 24 | 18 | 18 | 24 | 75.0% | 75.0% | 100.0% |
| GD | 216 | 216 | 138 | 86 | 206 | 63.9% | 39.8% | 95.4% |
| GE | 11 | 11 | 6 | 6 | 11 | 54.5% | 54.5% | 100.0% |
| GF | 39 | 39 | 17 | 25 | 39 | 43.6% | 64.1% | 100.0% |
| GG | 144 | 144 | 60 | 85 | 139 | 41.7% | 59.0% | 96.5% |
| GH | 37 | 37 | 13 | 0 | 32 | 35.1% | 0.0% | 86.5% |
| GJ | 8 | 8 | 3 | 0 | 6 | 37.5% | 0.0% | 75.0% |
| GK | 8 | 8 | 3 | 0 | 6 | 37.5% | 0.0% | 75.0% |
| GL | 7 | 7 | 3 | 0 | 5 | 42.9% | 0.0% | 71.4% |
| GM | 43 | 43 | 17 | 0 | 37 | 39.5% | 0.0% | 86.0% |
| GN | 40 | 40 | 13 | 0 | 33 | 32.5% | 0.0% | 82.5% |
| GO | 26 | 26 | 9 | 0 | 21 | 34.6% | 0.0% | 80.8% |
| GP | 37 | 37 | 20 | 10 | 30 | 54.1% | 27.0% | 81.1% |
| GQ | 19 | 19 | 7 | 8 | 18 | 36.8% | 42.1% | 94.7% |
| GR | 19 | 19 | 7 | 8 | 18 | 36.8% | 42.1% | 94.7% |
| HAIL | 7 | 7 | 3 | 1 | 5 | 42.9% | 14.3% | 71.4% |
| IA | 16 | 16 | 6 | 9 | 16 | 37.5% | 56.2% | 100.0% |
| IB | 54 | 54 | 20 | 12 | 52 | 37.0% | 22.2% | 96.3% |
| IC | 38 | 38 | 18 | 5 | 38 | 47.4% | 13.2% | 100.0% |
| KA | 60 | 60 | 32 | 0 | 48 | 53.3% | 0.0% | 80.0% |
| KB | 45 | 45 | 21 | 0 | 36 | 46.7% | 0.0% | 80.0% |
| KC | 38 | 38 | 22 | 0 | 32 | 57.9% | 0.0% | 84.2% |
| KD | 30 | 30 | 12 | 0 | 24 | 40.0% | 0.0% | 80.0% |
| KE | 26 | 26 | 9 | 8 | 25 | 34.6% | 30.8% | 96.2% |
| KF | 8 | 8 | 3 | 3 | 7 | 37.5% | 37.5% | 87.5% |
| KG | 36 | 36 | 20 | 0 | 30 | 55.6% | 0.0% | 83.3% |
| MA | 13 | 13 | 5 | 3 | 13 | 38.5% | 23.1% | 100.0% |
| MD | 18 | 18 | 11 | 7 | 17 | 61.1% | 38.9% | 94.4% |
| ME | 10 | 10 | 5 | 6 | 10 | 50.0% | 60.0% | 100.0% |
| MF | 16 | 16 | 5 | 6 | 15 | 31.2% | 37.5% | 93.8% |
| MG | 15 | 15 | 5 | 2 | 14 | 33.3% | 13.3% | 93.3% |
| MH | 14 | 14 | 5 | 2 | 13 | 35.7% | 14.3% | 92.9% |
| MK | 22 | 22 | 16 | 8 | 21 | 72.7% | 36.4% | 95.5% |
| MV | 14 | 14 | 7 | 9 | 14 | 50.0% | 64.3% | 100.0% |
| MW | 4 | 4 | 2 | 3 | 4 | 50.0% | 75.0% | 100.0% |
| N | 63 | 63 | 0 | 52 | 63 | 0.0% | 82.5% | 100.0% |
| OA | 51 | 51 | 30 | 21 | 45 | 58.8% | 41.2% | 88.2% |
| OB | 48 | 48 | 16 | 33 | 48 | 33.3% | 68.8% | 100.0% |
| OC | 8 | 8 | 3 | 4 | 7 | 37.5% | 50.0% | 87.5% |
| OD | 63 | 63 | 45 | 24 | 57 | 71.4% | 38.1% | 90.5% |
| OE | 69 | 69 | 48 | 40 | 61 | 69.6% | 58.0% | 88.4% |
| RH | 60 | 60 | 33 | 38 | 56 | 55.0% | 63.3% | 93.3% |
| SA | 22 | 22 | 6 | 3 | 19 | 27.3% | 13.6% | 86.4% |
| ST | 28 | 28 | 14 | 18 | 27 | 50.0% | 64.3% | 96.4% |
| UA | 19 | 19 | 8 | 10 | 17 | 42.1% | 52.6% | 89.5% |
| UG | 30 | 30 | 12 | 20 | 30 | 40.0% | 66.7% | 100.0% |
| UNSPECIFIED | 47 | 47 | 0 | 0 | 41 | 0.0% | 0.0% | 87.2% |
| WA | 13 | 13 | 7 | 8 | 13 | 53.8% | 61.5% | 100.0% |
| WD | 35 | 35 | 20 | 23 | 35 | 57.1% | 65.7% | 100.0% |
| WG | 11 | 11 | 2 | 4 | 11 | 18.2% | 36.4% | 100.0% |
| WJ | 35 | 35 | 15 | 21 | 35 | 42.9% | 60.0% | 100.0% |
| WND | 57 | 57 | 47 | 50 | 50 | 82.5% | 87.7% | 87.7% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested strict | Tested any | Implemented % | Tested strict % | Tested any % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| range | 364 | 286 | 118 | 118 | 78.6% | 32.4% | 32.4% |
| sentinel | 691 | 579 | 362 | 691 | 83.8% | 52.4% | 100.0% |
| allowed_quality | 82 | 75 | 65 | 82 | 91.5% | 79.3% | 100.0% |
| domain | 946 | 476 | 666 | 946 | 50.3% | 70.4% | 100.0% |
| cardinality | 128 | 109 | 109 | 128 | 85.2% | 85.2% | 100.0% |
| width | 1210 | 21 | 21 | 1210 | 1.7% | 1.7% | 100.0% |
| arity | 171 | 171 | 102 | 102 | 100.0% | 59.6% | 59.6% |
| unknown | 0 | 0 | 0 | 0 | excluded | excluded | excluded |

## Top gaps

| Part | Identifier | Rule type | Spec rule | Code impl | Tested strict | Tested any | Implementation pointer | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02 | AU | width | POS 47-51 width 5 | FALSE | FALSE | TRUE | src/noaa_climate_data/cleaning.py:616 | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV2 | range | MIN 0000 MAX 2359 | FALSE | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | MIN 0000 MAX 2359 | FALSE | FALSE | FALSE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 06 | CI1 | domain | Enumerated codes near line 250 | FALSE | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CI) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | IB1 | domain | Enumerated codes near line 151 | FALSE | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for IB) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | IB1 | sentinel | Missing sentinels 9 | FALSE | FALSE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for IB) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | MIN 0000 MAX 2359 | FALSE | TRUE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CV) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | MIN 01 MAX 99 | FALSE | TRUE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for ST) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | Enumerated codes near line 154 | FALSE | TRUE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for AU) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | Enumerated codes near line 19 | FALSE | TRUE | TRUE | src/noaa_climate_data/constants.py (FIELD_RULES for CO) | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested strict | Tested any | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 02 | AU | width | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV2 | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | IB1 | domain | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | IB1 | sentinel | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=wildcard_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | AU | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 26 | ST1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 04 | AA | range | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=wildcard_assertion;unresolved_in_next_steps |
| 04 | TMP | cardinality | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=wildcard_assertion;unresolved_in_next_steps |
| 02 | DATE | unknown | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO8 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
