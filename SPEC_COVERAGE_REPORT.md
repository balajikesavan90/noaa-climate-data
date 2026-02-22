# SPEC Coverage Report

## How to run

```bash
python tools/spec_coverage/generate_spec_coverage.py
# Fallback in environments without `python` alias:
python3 tools/spec_coverage/generate_spec_coverage.py
```

## Overall coverage

- Total spec rules extracted: **3583**
- Synthetic rows excluded from coverage metrics: **28**
- Metric-eligible rules (excluding `unknown`): **3583**
- Unknown/noisy rows excluded from %: **0**
- Rules implemented in code: **2896** (80.8%)
- Progress KPI (`tested_strict`): **2400** (67.0%)
- Weak coverage (`tested_any`, includes wildcard): **2400** (67.0%)
- tested_any from non-wild matches only: **2400** (67.0%)
- Wildcard-only tested_any (not counted toward progress): **0** (0.0%)
- Coverage progress is measured with `tested_strict` only.
- `test_covered` in CSV mirrors `test_covered_any` for backward compatibility.
- Expected-gap tagged rules: **112**
- Rows linked to unresolved `NEXT_STEPS.md` items: **3360**
- Open checklist items in `ARCHITECTURE_NEXT_STEPS.md`: **83**

## Top 50 real gaps (strict)

Strict gaps are metric spec-rule rows where `code_implemented=FALSE` or `test_covered_strict=FALSE`.
Rows with `identifier=UNSPECIFIED` or `synthetic_unmapped` notes are excluded from this actionable list.

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 2 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 3 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 4 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 5 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 6 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 7 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 8 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 9 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 10 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 11 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 12 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 13 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 14 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 15 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 16 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 17 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 18 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 19 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 23 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 24 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 25 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 26 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 27 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 28 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 29 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 30 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 31 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 32 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 33 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 34 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 35 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 36 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 37 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 38 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 39 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 40 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 41 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 42 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 43 | 29 | RH1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 44 | 29 | RH2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 45 | 29 | RH3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 46 | 29 | RH1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 47 | 29 | RH2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 48 | 29 | RH3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 49 | 29 | RH1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 50 | 29 | RH2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |

### Implementation gaps (strict): Not implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 2 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 3 | 29 | OC1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 4 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 5 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 6 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 7 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 8 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 9 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 10 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 11 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 12 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 13 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 14 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 15 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 16 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 17 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 18 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 19 | 29 | OD1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 29 | OD2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 29 | OD3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 23 | 29 | OE2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 24 | 29 | OE3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 25 | 29 | OE1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |

### Missing tests (strict): Implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 09 | CT2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 2 | 09 | CT3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 3 | 10 | CU2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 4 | 10 | CU3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 5 | 10 | CU2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 6 | 10 | CU3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 7 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 8 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 9 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 10 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 11 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 12 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 13 | 02 | LATITUDE | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 14 | 02 | LONGITUDE | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 15 | 02 | ELEVATION | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 16 | 02 | CALL_SIGN | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 17 | 02 | QC_PROCESS | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 18 | 04 | AL2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 19 | 04 | AL3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 20 | 04 | AL4 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 21 | 04 | AL2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 22 | 04 | AL3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 23 | 04 | AL4 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 24 | 05 | AX1 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |
| 25 | 05 | AX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;test_match=none;unresolved_in_next_steps |

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **2368** (66.1%)
- cleaning_only: **18** (0.5%)
- both: **510** (14.2%)
- neither: **687** (19.2%)

## Confidence breakdown

- Cleaning-implemented metric rules: **528** (14.7%)
- high: **4** (0.8%)
- medium: **524** (99.2%)
- low: **0** (0.0%)

## Match quality

| Match strength | Count | % of metric rules |
| --- | --- | --- |
| exact_signature | 680 | 19.0% |
| exact_assertion | 1692 | 47.2% |
| family_assertion | 28 | 0.8% |
| wildcard_assertion | 0 | 0.0% |
| none | 1183 | 33.0% |

## Precision warnings

- Wildcard policy: `wildcard_assertion` counts as tested-any only; it never counts as strict.
- Tested-any rows matched by `exact_signature`: **680** (28.3%)
- Tested-any rows matched by `exact_assertion`: **1692** (70.5%)
- Tested-any rows matched by `family_assertion`: **28** (1.2%)
- Tested-any rows matched by `wildcard_assertion`: **0** (0.0%)
- Synthetic rows in CSV: **28**
- Synthetic gap rows in CSV: **28**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested (strict): **42/171** (24.6%)
- Arity rules tested (any): **42/171** (24.6%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Suspicious coverage

- tested_any=TRUE and code_implemented=FALSE: **403** (11.2%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-03-mandatory-data-section.md:99-99::CIG::domain::6333f4110f | CIG | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:103-113::CIG::domain::82b0e05aae | CIG | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:161-171::VIS::domain::82b0e05aae | VIS | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:183-193::VIS::domain::82b0e05aae | VIS | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:207-225::TMP::domain::52bade1af7 | TMP | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:241-259::DEW::domain::52bade1af7 | DEW | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:278-278::SLP::domain::6333f4110f | SLP | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-03-mandatory-data-section.md:282-293::SLP::domain::82b0e05aae | SLP | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:49-49::AA1::domain::f68b43c01b | AA | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:57-57::AA1::domain::af972d72f4 | AA | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |

- tested_any=TRUE and match_strength=`wildcard_assertion`: **0** (0.0%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| (none) | - | - | - |

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| 02 | 29 | 29 | 21 | 11 | 11 | 72.4% | 37.9% | 37.9% |
| 03 | 53 | 53 | 44 | 51 | 51 | 83.0% | 96.2% | 96.2% |
| 04 | 603 | 603 | 549 | 461 | 461 | 91.0% | 76.5% | 76.5% |
| 05 | 450 | 450 | 416 | 260 | 260 | 92.4% | 57.8% | 57.8% |
| 06 | 287 | 287 | 222 | 212 | 212 | 77.4% | 73.9% | 73.9% |
| 07 | 74 | 74 | 73 | 42 | 42 | 98.6% | 56.8% | 56.8% |
| 08 | 11 | 11 | 7 | 7 | 7 | 63.6% | 63.6% | 63.6% |
| 09 | 28 | 28 | 21 | 15 | 15 | 75.0% | 53.6% | 53.6% |
| 10 | 55 | 55 | 39 | 31 | 31 | 70.9% | 56.4% | 56.4% |
| 11 | 109 | 109 | 96 | 90 | 90 | 88.1% | 82.6% | 82.6% |
| 12 | 20 | 20 | 13 | 19 | 19 | 65.0% | 95.0% | 95.0% |
| 13 | 109 | 109 | 75 | 63 | 63 | 68.8% | 57.8% | 57.8% |
| 14 | 15 | 15 | 11 | 11 | 11 | 73.3% | 73.3% | 73.3% |
| 15 | 472 | 472 | 425 | 243 | 243 | 90.0% | 51.5% | 51.5% |
| 16 | 24 | 24 | 17 | 20 | 20 | 70.8% | 83.3% | 83.3% |
| 17 | 84 | 84 | 54 | 60 | 60 | 64.3% | 71.4% | 71.4% |
| 18 | 27 | 27 | 16 | 19 | 19 | 59.3% | 70.4% | 70.4% |
| 19 | 38 | 38 | 30 | 30 | 30 | 78.9% | 78.9% | 78.9% |
| 20 | 20 | 20 | 14 | 18 | 18 | 70.0% | 90.0% | 90.0% |
| 21 | 20 | 20 | 12 | 18 | 18 | 60.0% | 90.0% | 90.0% |
| 22 | 8 | 8 | 5 | 6 | 6 | 62.5% | 75.0% | 75.0% |
| 23 | 109 | 109 | 98 | 77 | 77 | 89.9% | 70.6% | 70.6% |
| 24 | 244 | 244 | 211 | 202 | 202 | 86.5% | 82.8% | 82.8% |
| 25 | 7 | 7 | 5 | 4 | 4 | 71.4% | 57.1% | 57.1% |
| 26 | 29 | 29 | 28 | 27 | 27 | 96.6% | 93.1% | 93.1% |
| 27 | 109 | 109 | 89 | 94 | 94 | 81.7% | 86.2% | 86.2% |
| 28 | 19 | 19 | 14 | 15 | 15 | 73.7% | 78.9% | 78.9% |
| 29 | 306 | 306 | 210 | 146 | 146 | 68.6% | 47.7% | 47.7% |
| 30 | 224 | 224 | 81 | 148 | 148 | 36.2% | 66.1% | 66.1% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AA | 68 | 68 | 60 | 41 | 41 | 88.2% | 60.3% | 60.3% |
| AB | 12 | 12 | 8 | 9 | 9 | 66.7% | 75.0% | 75.0% |
| AC | 10 | 10 | 10 | 9 | 9 | 100.0% | 90.0% | 90.0% |
| AD | 23 | 23 | 23 | 23 | 23 | 100.0% | 100.0% | 100.0% |
| AE | 26 | 26 | 18 | 25 | 25 | 69.2% | 96.2% | 96.2% |
| AG | 9 | 9 | 8 | 9 | 9 | 88.9% | 100.0% | 100.0% |
| AH | 126 | 126 | 126 | 76 | 76 | 100.0% | 60.3% | 60.3% |
| AI | 126 | 126 | 126 | 101 | 101 | 100.0% | 80.2% | 80.2% |
| AJ | 22 | 22 | 14 | 21 | 21 | 63.6% | 95.5% | 95.5% |
| AK | 16 | 16 | 15 | 15 | 15 | 93.8% | 93.8% | 93.8% |
| AL | 64 | 64 | 56 | 46 | 46 | 87.5% | 71.9% | 71.9% |
| AM | 23 | 23 | 20 | 22 | 22 | 87.0% | 95.7% | 95.7% |
| AN | 15 | 15 | 13 | 14 | 14 | 86.7% | 93.3% | 93.3% |
| AO | 64 | 64 | 56 | 55 | 55 | 87.5% | 85.9% | 85.9% |
| AP | 9 | 9 | 8 | 7 | 7 | 88.9% | 77.8% | 77.8% |
| AT | 80 | 80 | 72 | 49 | 49 | 90.0% | 61.2% | 61.2% |
| AU | 225 | 225 | 225 | 120 | 120 | 100.0% | 53.3% | 53.3% |
| AW | 8 | 8 | 7 | 8 | 8 | 87.5% | 100.0% | 100.0% |
| AX | 84 | 84 | 66 | 45 | 45 | 78.6% | 53.6% | 53.6% |
| AY | 26 | 26 | 22 | 17 | 17 | 84.6% | 65.4% | 65.4% |
| AZ | 26 | 26 | 24 | 21 | 21 | 92.3% | 80.8% | 80.8% |
| CALL_SIGN | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| CB | 28 | 28 | 22 | 18 | 18 | 78.6% | 64.3% | 64.3% |
| CF | 33 | 33 | 24 | 22 | 22 | 72.7% | 66.7% | 66.7% |
| CG | 30 | 30 | 24 | 19 | 19 | 80.0% | 63.3% | 63.3% |
| CH | 46 | 46 | 34 | 31 | 31 | 73.9% | 67.4% | 67.4% |
| CI | 36 | 36 | 32 | 23 | 23 | 88.9% | 63.9% | 63.9% |
| CIG | 12 | 12 | 10 | 12 | 12 | 83.3% | 100.0% | 100.0% |
| CN | 113 | 113 | 86 | 99 | 99 | 76.1% | 87.6% | 87.6% |
| CO | 73 | 73 | 73 | 42 | 42 | 100.0% | 57.5% | 57.5% |
| CR | 10 | 10 | 7 | 7 | 7 | 70.0% | 70.0% | 70.0% |
| CT | 27 | 27 | 21 | 15 | 15 | 77.8% | 55.6% | 55.6% |
| CU | 54 | 54 | 39 | 31 | 31 | 72.2% | 57.4% | 57.4% |
| CV | 108 | 108 | 96 | 90 | 90 | 88.9% | 83.3% | 83.3% |
| CW | 19 | 19 | 13 | 19 | 19 | 68.4% | 100.0% | 100.0% |
| CX | 108 | 108 | 75 | 63 | 63 | 69.4% | 58.3% | 58.3% |
| DATE | 2 | 2 | 2 | 2 | 2 | 100.0% | 100.0% | 100.0% |
| DEW | 5 | 5 | 4 | 4 | 4 | 80.0% | 80.0% | 80.0% |
| ED | 14 | 14 | 11 | 11 | 11 | 78.6% | 78.6% | 78.6% |
| ELEVATION | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| GA | 24 | 24 | 24 | 15 | 15 | 100.0% | 62.5% | 62.5% |
| GD | 216 | 216 | 216 | 116 | 116 | 100.0% | 53.7% | 53.7% |
| GE | 11 | 11 | 11 | 11 | 11 | 100.0% | 100.0% | 100.0% |
| GF | 39 | 39 | 31 | 39 | 39 | 79.5% | 100.0% | 100.0% |
| GG | 144 | 144 | 114 | 37 | 37 | 79.2% | 25.7% | 25.7% |
| GH | 37 | 37 | 29 | 25 | 25 | 78.4% | 67.6% | 67.6% |
| GJ | 8 | 8 | 6 | 7 | 7 | 75.0% | 87.5% | 87.5% |
| GK | 8 | 8 | 6 | 7 | 7 | 75.0% | 87.5% | 87.5% |
| GL | 7 | 7 | 5 | 6 | 6 | 71.4% | 85.7% | 85.7% |
| GM | 43 | 43 | 30 | 31 | 31 | 69.8% | 72.1% | 72.1% |
| GN | 40 | 40 | 24 | 29 | 29 | 60.0% | 72.5% | 72.5% |
| GO | 26 | 26 | 16 | 19 | 19 | 61.5% | 73.1% | 73.1% |
| GP | 37 | 37 | 30 | 30 | 30 | 81.1% | 81.1% | 81.1% |
| GQ | 19 | 19 | 14 | 18 | 18 | 73.7% | 94.7% | 94.7% |
| GR | 19 | 19 | 12 | 18 | 18 | 63.2% | 94.7% | 94.7% |
| HAIL | 7 | 7 | 5 | 6 | 6 | 71.4% | 85.7% | 85.7% |
| IA | 16 | 16 | 15 | 12 | 12 | 93.8% | 75.0% | 75.0% |
| IB | 54 | 54 | 52 | 36 | 36 | 96.3% | 66.7% | 66.7% |
| IC | 38 | 38 | 31 | 29 | 29 | 81.6% | 76.3% | 76.3% |
| KA | 60 | 60 | 56 | 47 | 47 | 93.3% | 78.3% | 78.3% |
| KB | 45 | 45 | 39 | 36 | 36 | 86.7% | 80.0% | 80.0% |
| KC | 38 | 38 | 36 | 32 | 32 | 94.7% | 84.2% | 84.2% |
| KD | 30 | 30 | 24 | 26 | 26 | 80.0% | 86.7% | 86.7% |
| KE | 26 | 26 | 18 | 25 | 25 | 69.2% | 96.2% | 96.2% |
| KF | 8 | 8 | 6 | 7 | 7 | 75.0% | 87.5% | 87.5% |
| KG | 36 | 36 | 32 | 29 | 29 | 88.9% | 80.6% | 80.6% |
| LATITUDE | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| LONGITUDE | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| MA | 13 | 13 | 10 | 11 | 11 | 76.9% | 84.6% | 84.6% |
| MD | 18 | 18 | 18 | 14 | 14 | 100.0% | 77.8% | 77.8% |
| ME | 10 | 10 | 9 | 10 | 10 | 90.0% | 100.0% | 100.0% |
| MF | 16 | 16 | 10 | 15 | 15 | 62.5% | 93.8% | 93.8% |
| MG | 15 | 15 | 10 | 12 | 12 | 66.7% | 80.0% | 80.0% |
| MH | 14 | 14 | 10 | 11 | 11 | 71.4% | 78.6% | 78.6% |
| MK | 22 | 22 | 22 | 21 | 21 | 100.0% | 95.5% | 95.5% |
| MV | 14 | 14 | 11 | 11 | 11 | 78.6% | 78.6% | 78.6% |
| MW | 4 | 4 | 3 | 4 | 4 | 75.0% | 100.0% | 100.0% |
| N | 63 | 63 | 0 | 52 | 52 | 0.0% | 82.5% | 82.5% |
| OA | 51 | 51 | 45 | 29 | 29 | 88.2% | 56.9% | 56.9% |
| OB | 48 | 48 | 31 | 47 | 47 | 64.6% | 97.9% | 97.9% |
| OC | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| OD | 63 | 63 | 45 | 17 | 17 | 71.4% | 27.0% | 27.0% |
| OE | 69 | 69 | 48 | 24 | 24 | 69.6% | 34.8% | 34.8% |
| QC_PROCESS | 2 | 2 | 1 | 0 | 0 | 50.0% | 0.0% | 0.0% |
| REPORT_TYPE | 4 | 4 | 4 | 3 | 3 | 100.0% | 75.0% | 75.0% |
| RH | 60 | 60 | 33 | 21 | 21 | 55.0% | 35.0% | 35.0% |
| SA | 12 | 12 | 10 | 8 | 8 | 83.3% | 66.7% | 66.7% |
| SLP | 5 | 5 | 3 | 5 | 5 | 60.0% | 100.0% | 100.0% |
| ST | 28 | 28 | 28 | 27 | 27 | 100.0% | 96.4% | 96.4% |
| TIME | 2 | 2 | 2 | 2 | 2 | 100.0% | 100.0% | 100.0% |
| TMP | 5 | 5 | 4 | 5 | 5 | 80.0% | 100.0% | 100.0% |
| UA | 19 | 19 | 8 | 10 | 10 | 42.1% | 52.6% | 52.6% |
| UG | 30 | 30 | 12 | 17 | 17 | 40.0% | 56.7% | 56.7% |
| UNSPECIFIED | 36 | 36 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| VIS | 10 | 10 | 8 | 10 | 10 | 80.0% | 100.0% | 100.0% |
| WA | 13 | 13 | 7 | 8 | 8 | 53.8% | 61.5% | 61.5% |
| WD | 35 | 35 | 20 | 23 | 23 | 57.1% | 65.7% | 65.7% |
| WG | 11 | 11 | 2 | 4 | 4 | 18.2% | 36.4% | 36.4% |
| WJ | 35 | 35 | 15 | 22 | 22 | 42.9% | 62.9% | 62.9% |
| WND | 20 | 20 | 20 | 15 | 15 | 100.0% | 75.0% | 75.0% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| range | 363 | 355 | 261 | 261 | 97.8% | 71.9% | 71.9% |
| sentinel | 688 | 595 | 240 | 240 | 86.5% | 34.9% | 34.9% |
| allowed_quality | 81 | 75 | 71 | 71 | 92.6% | 87.7% | 87.7% |
| domain | 945 | 525 | 695 | 695 | 55.6% | 73.5% | 73.5% |
| cardinality | 128 | 126 | 128 | 128 | 98.4% | 100.0% | 100.0% |
| width | 1207 | 1049 | 963 | 963 | 86.9% | 79.8% | 79.8% |
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
| 09 | CT2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
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
| 10 | CU1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 11 | CV3 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 13 | CX1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 20 | GQ1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 21 | GR1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_allowed_values_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 23 | IA2 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IB1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
