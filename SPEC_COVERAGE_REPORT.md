# SPEC Coverage Report

## How to run

```bash
python tools/spec_coverage/generate_spec_coverage.py
# Fallback in environments without `python` alias:
python3 tools/spec_coverage/generate_spec_coverage.py
```

## Overall coverage

- Total spec rules extracted: **3524**
- Synthetic rows excluded from coverage metrics: **28**
- Metric-eligible rules (excluding `unknown`): **3524**
- Unknown/noisy rows excluded from %: **0**
- Rules implemented in code: **3488** (99.0%)
- Progress KPI (`tested_strict`): **2748** (78.0%)
- Weak coverage (`tested_any`, includes wildcard): **2748** (78.0%)
- tested_any from non-wild matches only: **2748** (78.0%)
- Wildcard-only tested_any (not counted toward progress): **0** (0.0%)
- Coverage progress is measured with `tested_strict` only.
- `test_covered` in CSV mirrors `test_covered_any` for backward compatibility.
- Expected-gap tagged rules: **112**
- Rows linked to unresolved `NEXT_STEPS.md` items: **3301**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Top 50 real gaps (strict)

Strict gaps are metric spec-rule rows where `code_implemented=FALSE` or `test_covered_strict=FALSE`.
Rows with `identifier=UNSPECIFIED` or `synthetic_unmapped` notes are excluded from this actionable list.

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 29 | OA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 2 | 29 | OA2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 3 | 29 | OA3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 4 | 29 | OA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 5 | 29 | OA2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 6 | 29 | OA3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 7 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 8 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 9 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 10 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 11 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 12 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 13 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 14 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 15 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 16 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 17 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 18 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 19 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 20 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 21 | 29 | RH2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 22 | 29 | RH3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 23 | 29 | RH2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax_overlap;test_match=none;unresolved_in_next_steps |
| 24 | 29 | RH3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax_overlap;test_match=none;unresolved_in_next_steps |
| 25 | 30 | UA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 26 | 30 | UA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 27 | 30 | UG2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 28 | 30 | UG2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 29 | 30 | UG2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 30 | 30 | UG2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 31 | 30 | UG2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 32 | 30 | WND2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 33 | 30 | WND2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 34 | 30 | WND2 | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 35 | 02 | LATITUDE | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 36 | 02 | LONGITUDE | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 37 | 02 | REPORT_TYPE | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 38 | 02 | ELEVATION | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 39 | 02 | CALL_SIGN | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 40 | 03 | DEW | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 41 | 04 | AA1 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 42 | 04 | AA2 | domain | both | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=global_domain_gate;coverage_reason_constants=field_rule_domain_missing;test_match=none;unresolved_in_next_steps |
| 43 | 04 | AA2 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 44 | 04 | AA3 | domain | both | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=global_domain_gate;coverage_reason_constants=field_rule_domain_missing;test_match=none;unresolved_in_next_steps |
| 45 | 04 | AA3 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 46 | 04 | AA4 | domain | both | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=global_domain_gate;coverage_reason_constants=field_rule_domain_missing;test_match=none;unresolved_in_next_steps |
| 47 | 04 | AA4 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 48 | 04 | AA1 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |
| 49 | 04 | AA2 | domain | both | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=global_domain_gate;coverage_reason_constants=field_rule_domain_missing;test_match=none;unresolved_in_next_steps |
| 50 | 04 | AA2 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;test_match=none;unresolved_in_next_steps |

### Implementation gaps (strict): Not implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | - | - | - | - | (none) |

### Missing tests (strict): Implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 29 | OA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 2 | 29 | OA2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 3 | 29 | OA3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 4 | 29 | OA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 5 | 29 | OA2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 6 | 29 | OA3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 7 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 8 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 9 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 10 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 11 | 29 | OD2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 12 | 29 | OD3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 13 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 14 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 15 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 16 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 17 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 18 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 19 | 29 | OE2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 20 | 29 | OE3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 21 | 29 | RH2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 22 | 29 | RH3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 23 | 29 | RH2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax_overlap;test_match=none;unresolved_in_next_steps |
| 24 | 29 | RH3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax_overlap;test_match=none;unresolved_in_next_steps |
| 25 | 30 | UA1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **2597** (73.7%)
- cleaning_only: **4** (0.1%)
- both: **887** (25.2%)
- neither: **36** (1.0%)

## Confidence breakdown

- Cleaning-implemented metric rules: **891** (25.3%)
- high: **4** (0.4%)
- medium: **887** (99.6%)
- low: **0** (0.0%)

## Match quality

| Match strength | Count | % of metric rules |
| --- | --- | --- |
| exact_signature | 849 | 24.1% |
| exact_assertion | 1887 | 53.5% |
| family_assertion | 12 | 0.3% |
| wildcard_assertion | 0 | 0.0% |
| none | 776 | 22.0% |

## Precision warnings

- Wildcard policy: `wildcard_assertion` counts as tested-any only; it never counts as strict.
- Tested-any rows matched by `exact_signature`: **849** (30.9%)
- Tested-any rows matched by `exact_assertion`: **1887** (68.7%)
- Tested-any rows matched by `family_assertion`: **12** (0.4%)
- Tested-any rows matched by `wildcard_assertion`: **0** (0.0%)
- Synthetic rows in CSV: **28**
- Synthetic gap rows in CSV: **28**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested (strict): **42/171** (24.6%)
- Arity rules tested (any): **42/171** (24.6%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Suspicious coverage

- tested_any=TRUE and code_implemented=FALSE: **0** (0.0%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| (none) | - | - | - |

- tested_any=TRUE and match_strength=`wildcard_assertion`: **0** (0.0%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| (none) | - | - | - |

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| 02 | 29 | 29 | 22 | 16 | 16 | 75.9% | 55.2% | 55.2% |
| 03 | 53 | 53 | 52 | 51 | 51 | 98.1% | 96.2% | 96.2% |
| 04 | 603 | 603 | 601 | 467 | 467 | 99.7% | 77.4% | 77.4% |
| 05 | 450 | 450 | 449 | 290 | 290 | 99.8% | 64.4% | 64.4% |
| 06 | 287 | 287 | 286 | 234 | 234 | 99.7% | 81.5% | 81.5% |
| 07 | 74 | 74 | 73 | 51 | 51 | 98.6% | 68.9% | 68.9% |
| 08 | 11 | 11 | 10 | 7 | 7 | 90.9% | 63.6% | 63.6% |
| 09 | 28 | 28 | 27 | 19 | 19 | 96.4% | 67.9% | 67.9% |
| 10 | 55 | 55 | 54 | 40 | 40 | 98.2% | 72.7% | 72.7% |
| 11 | 109 | 109 | 108 | 90 | 90 | 99.1% | 82.6% | 82.6% |
| 12 | 20 | 20 | 19 | 19 | 19 | 95.0% | 95.0% | 95.0% |
| 13 | 109 | 109 | 108 | 82 | 82 | 99.1% | 75.2% | 75.2% |
| 14 | 15 | 15 | 14 | 13 | 13 | 93.3% | 86.7% | 86.7% |
| 15 | 472 | 472 | 471 | 391 | 391 | 99.8% | 82.8% | 82.8% |
| 16 | 24 | 24 | 23 | 20 | 20 | 95.8% | 83.3% | 83.3% |
| 17 | 84 | 84 | 83 | 60 | 60 | 98.8% | 71.4% | 71.4% |
| 18 | 27 | 27 | 26 | 19 | 19 | 96.3% | 70.4% | 70.4% |
| 19 | 38 | 38 | 37 | 36 | 36 | 97.4% | 94.7% | 94.7% |
| 20 | 20 | 20 | 19 | 18 | 18 | 95.0% | 90.0% | 90.0% |
| 21 | 20 | 20 | 19 | 18 | 18 | 95.0% | 90.0% | 90.0% |
| 22 | 8 | 8 | 7 | 6 | 6 | 87.5% | 75.0% | 75.0% |
| 23 | 109 | 109 | 108 | 88 | 88 | 99.1% | 80.7% | 80.7% |
| 24 | 244 | 244 | 243 | 202 | 202 | 99.6% | 82.8% | 82.8% |
| 25 | 7 | 7 | 6 | 4 | 4 | 85.7% | 57.1% | 57.1% |
| 26 | 29 | 29 | 28 | 27 | 27 | 96.6% | 93.1% | 93.1% |
| 27 | 109 | 109 | 108 | 94 | 94 | 99.1% | 86.2% | 86.2% |
| 28 | 17 | 17 | 16 | 13 | 13 | 94.1% | 76.5% | 76.5% |
| 29 | 306 | 306 | 305 | 222 | 222 | 99.7% | 72.5% | 72.5% |
| 30 | 167 | 167 | 166 | 151 | 151 | 99.4% | 90.4% | 90.4% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AA | 68 | 68 | 68 | 41 | 41 | 100.0% | 60.3% | 60.3% |
| AB | 12 | 12 | 12 | 9 | 9 | 100.0% | 75.0% | 75.0% |
| AC | 10 | 10 | 10 | 9 | 9 | 100.0% | 90.0% | 90.0% |
| AD | 23 | 23 | 23 | 23 | 23 | 100.0% | 100.0% | 100.0% |
| AE | 26 | 26 | 26 | 25 | 25 | 100.0% | 96.2% | 96.2% |
| AG | 9 | 9 | 9 | 9 | 9 | 100.0% | 100.0% | 100.0% |
| AH | 126 | 126 | 126 | 76 | 76 | 100.0% | 60.3% | 60.3% |
| AI | 126 | 126 | 126 | 101 | 101 | 100.0% | 80.2% | 80.2% |
| AJ | 22 | 22 | 22 | 21 | 21 | 100.0% | 95.5% | 95.5% |
| AK | 16 | 16 | 16 | 15 | 15 | 100.0% | 93.8% | 93.8% |
| AL | 64 | 64 | 64 | 52 | 52 | 100.0% | 81.2% | 81.2% |
| AM | 23 | 23 | 23 | 22 | 22 | 100.0% | 95.7% | 95.7% |
| AN | 15 | 15 | 15 | 14 | 14 | 100.0% | 93.3% | 93.3% |
| AO | 64 | 64 | 64 | 55 | 55 | 100.0% | 85.9% | 85.9% |
| AP | 9 | 9 | 9 | 7 | 7 | 100.0% | 77.8% | 77.8% |
| AT | 80 | 80 | 80 | 49 | 49 | 100.0% | 61.2% | 61.2% |
| AU | 225 | 225 | 225 | 120 | 120 | 100.0% | 53.3% | 53.3% |
| AW | 8 | 8 | 8 | 8 | 8 | 100.0% | 100.0% | 100.0% |
| AX | 84 | 84 | 84 | 67 | 67 | 100.0% | 79.8% | 79.8% |
| AY | 26 | 26 | 26 | 23 | 23 | 100.0% | 88.5% | 88.5% |
| AZ | 26 | 26 | 26 | 23 | 23 | 100.0% | 88.5% | 88.5% |
| CALL_SIGN | 3 | 3 | 3 | 2 | 2 | 100.0% | 66.7% | 66.7% |
| CB | 28 | 28 | 28 | 20 | 20 | 100.0% | 71.4% | 71.4% |
| CF | 33 | 33 | 33 | 24 | 24 | 100.0% | 72.7% | 72.7% |
| CG | 30 | 30 | 30 | 21 | 21 | 100.0% | 70.0% | 70.0% |
| CH | 46 | 46 | 46 | 34 | 34 | 100.0% | 73.9% | 73.9% |
| CI | 36 | 36 | 36 | 36 | 36 | 100.0% | 100.0% | 100.0% |
| CIG | 12 | 12 | 12 | 12 | 12 | 100.0% | 100.0% | 100.0% |
| CN | 113 | 113 | 113 | 99 | 99 | 100.0% | 87.6% | 87.6% |
| CO | 73 | 73 | 73 | 51 | 51 | 100.0% | 69.9% | 69.9% |
| CR | 10 | 10 | 10 | 7 | 7 | 100.0% | 70.0% | 70.0% |
| CT | 27 | 27 | 27 | 19 | 19 | 100.0% | 70.4% | 70.4% |
| CU | 54 | 54 | 54 | 40 | 40 | 100.0% | 74.1% | 74.1% |
| CV | 108 | 108 | 108 | 90 | 90 | 100.0% | 83.3% | 83.3% |
| CW | 19 | 19 | 19 | 19 | 19 | 100.0% | 100.0% | 100.0% |
| CX | 108 | 108 | 108 | 82 | 82 | 100.0% | 75.9% | 75.9% |
| DATE | 2 | 2 | 2 | 2 | 2 | 100.0% | 100.0% | 100.0% |
| DEW | 5 | 5 | 5 | 4 | 4 | 100.0% | 80.0% | 80.0% |
| ED | 14 | 14 | 14 | 13 | 13 | 100.0% | 92.9% | 92.9% |
| ELEVATION | 3 | 3 | 3 | 2 | 2 | 100.0% | 66.7% | 66.7% |
| GA | 24 | 24 | 24 | 15 | 15 | 100.0% | 62.5% | 62.5% |
| GD | 216 | 216 | 216 | 170 | 170 | 100.0% | 78.7% | 78.7% |
| GE | 11 | 11 | 11 | 11 | 11 | 100.0% | 100.0% | 100.0% |
| GF | 39 | 39 | 39 | 39 | 39 | 100.0% | 100.0% | 100.0% |
| GG | 144 | 144 | 144 | 119 | 119 | 100.0% | 82.6% | 82.6% |
| GH | 37 | 37 | 37 | 37 | 37 | 100.0% | 100.0% | 100.0% |
| GJ | 8 | 8 | 8 | 7 | 7 | 100.0% | 87.5% | 87.5% |
| GK | 8 | 8 | 8 | 7 | 7 | 100.0% | 87.5% | 87.5% |
| GL | 7 | 7 | 7 | 6 | 6 | 100.0% | 85.7% | 85.7% |
| GM | 43 | 43 | 43 | 31 | 31 | 100.0% | 72.1% | 72.1% |
| GN | 40 | 40 | 40 | 29 | 29 | 100.0% | 72.5% | 72.5% |
| GO | 26 | 26 | 26 | 19 | 19 | 100.0% | 73.1% | 73.1% |
| GP | 37 | 37 | 37 | 36 | 36 | 100.0% | 97.3% | 97.3% |
| GQ | 19 | 19 | 19 | 18 | 18 | 100.0% | 94.7% | 94.7% |
| GR | 19 | 19 | 19 | 18 | 18 | 100.0% | 94.7% | 94.7% |
| HAIL | 7 | 7 | 7 | 6 | 6 | 100.0% | 85.7% | 85.7% |
| IA | 16 | 16 | 16 | 16 | 16 | 100.0% | 100.0% | 100.0% |
| IB | 54 | 54 | 54 | 43 | 43 | 100.0% | 79.6% | 79.6% |
| IC | 38 | 38 | 38 | 29 | 29 | 100.0% | 76.3% | 76.3% |
| KA | 60 | 60 | 60 | 47 | 47 | 100.0% | 78.3% | 78.3% |
| KB | 45 | 45 | 45 | 36 | 36 | 100.0% | 80.0% | 80.0% |
| KC | 38 | 38 | 38 | 32 | 32 | 100.0% | 84.2% | 84.2% |
| KD | 30 | 30 | 30 | 26 | 26 | 100.0% | 86.7% | 86.7% |
| KE | 26 | 26 | 26 | 25 | 25 | 100.0% | 96.2% | 96.2% |
| KF | 8 | 8 | 8 | 7 | 7 | 100.0% | 87.5% | 87.5% |
| KG | 36 | 36 | 36 | 29 | 29 | 100.0% | 80.6% | 80.6% |
| LATITUDE | 3 | 3 | 3 | 2 | 2 | 100.0% | 66.7% | 66.7% |
| LONGITUDE | 3 | 3 | 3 | 2 | 2 | 100.0% | 66.7% | 66.7% |
| MA | 13 | 13 | 13 | 11 | 11 | 100.0% | 84.6% | 84.6% |
| MD | 18 | 18 | 18 | 14 | 14 | 100.0% | 77.8% | 77.8% |
| ME | 10 | 10 | 10 | 10 | 10 | 100.0% | 100.0% | 100.0% |
| MF | 16 | 16 | 16 | 15 | 15 | 100.0% | 93.8% | 93.8% |
| MG | 15 | 15 | 15 | 12 | 12 | 100.0% | 80.0% | 80.0% |
| MH | 14 | 14 | 14 | 11 | 11 | 100.0% | 78.6% | 78.6% |
| MK | 22 | 22 | 22 | 21 | 21 | 100.0% | 95.5% | 95.5% |
| MV | 12 | 12 | 12 | 9 | 9 | 100.0% | 75.0% | 75.0% |
| MW | 4 | 4 | 4 | 4 | 4 | 100.0% | 100.0% | 100.0% |
| N | 11 | 11 | 11 | 11 | 11 | 100.0% | 100.0% | 100.0% |
| OA | 51 | 51 | 51 | 29 | 29 | 100.0% | 56.9% | 56.9% |
| OB | 48 | 48 | 48 | 47 | 47 | 100.0% | 97.9% | 97.9% |
| OC | 8 | 8 | 8 | 7 | 7 | 100.0% | 87.5% | 87.5% |
| OD | 63 | 63 | 63 | 40 | 40 | 100.0% | 63.5% | 63.5% |
| OE | 69 | 69 | 69 | 51 | 51 | 100.0% | 73.9% | 73.9% |
| QC_PROCESS | 2 | 2 | 2 | 1 | 1 | 100.0% | 50.0% | 50.0% |
| REPORT_TYPE | 4 | 4 | 4 | 3 | 3 | 100.0% | 75.0% | 75.0% |
| RH | 60 | 60 | 60 | 44 | 44 | 100.0% | 73.3% | 73.3% |
| SA | 12 | 12 | 12 | 8 | 8 | 100.0% | 66.7% | 66.7% |
| SLP | 5 | 5 | 5 | 5 | 5 | 100.0% | 100.0% | 100.0% |
| ST | 28 | 28 | 28 | 27 | 27 | 100.0% | 96.4% | 96.4% |
| TIME | 2 | 2 | 2 | 2 | 2 | 100.0% | 100.0% | 100.0% |
| TMP | 5 | 5 | 5 | 5 | 5 | 100.0% | 100.0% | 100.0% |
| UA | 19 | 19 | 19 | 17 | 17 | 100.0% | 89.5% | 89.5% |
| UG | 30 | 30 | 30 | 22 | 22 | 100.0% | 73.3% | 73.3% |
| UNSPECIFIED | 36 | 36 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| VIS | 10 | 10 | 10 | 10 | 10 | 100.0% | 100.0% | 100.0% |
| WA | 13 | 13 | 13 | 13 | 13 | 100.0% | 100.0% | 100.0% |
| WD | 35 | 35 | 35 | 35 | 35 | 100.0% | 100.0% | 100.0% |
| WG | 11 | 11 | 11 | 11 | 11 | 100.0% | 100.0% | 100.0% |
| WJ | 30 | 30 | 30 | 30 | 30 | 100.0% | 100.0% | 100.0% |
| WND | 20 | 20 | 20 | 15 | 15 | 100.0% | 75.0% | 75.0% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| range | 362 | 360 | 334 | 334 | 99.4% | 92.3% | 92.3% |
| sentinel | 688 | 687 | 240 | 240 | 99.9% | 34.9% | 34.9% |
| allowed_quality | 80 | 80 | 77 | 77 | 100.0% | 96.2% | 96.2% |
| domain | 888 | 888 | 761 | 761 | 100.0% | 85.7% | 85.7% |
| cardinality | 128 | 128 | 128 | 128 | 100.0% | 100.0% | 100.0% |
| width | 1207 | 1174 | 1166 | 1166 | 97.3% | 96.6% | 96.6% |
| arity | 171 | 171 | 42 | 42 | 100.0% | 24.6% | 24.6% |
| unknown | 0 | 0 | 0 | 0 | excluded | excluded | excluded |

## Wildcard-only coverage (not counted toward progress)

- Wildcard-only rows (`test_covered_any=TRUE` and `test_covered_strict=FALSE`): **0** (0.0%)

| Part | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| (none) | 0 | 0.0% |

| Rule type | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| range | 0 | 0.0% |
| sentinel | 0 | 0.0% |
| allowed_quality | 0 | 0.0% |
| domain | 0 | 0.0% |
| cardinality | 0 | 0.0% |
| width | 0 | 0.0% |
| arity | 0 | 0.0% |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested strict | Tested any | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 04 | TMP | cardinality | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 23 | IA | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;gap_tag_cap_exceeded;gap_tag_overflow=53;synthetic_gap_row;test_match=none;unresolved_in_next_steps |
| 02 | DATE | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | DATE | width | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 02 | TIME | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | TIME | width | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO8 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO9 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 09 | CT1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 10 | CU1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV3 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 20 | GQ1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 21 | GR1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 23 | IA2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
