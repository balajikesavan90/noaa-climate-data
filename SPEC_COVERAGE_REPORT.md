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
- Rules implemented in code: **1725** (48.1%)
- Progress KPI (`tested_strict`): **901** (25.1%)
- Weak coverage (`tested_any`, includes wildcard): **920** (25.7%)
- tested_any from non-wild matches only: **901** (25.1%)
- Wildcard-only tested_any (not counted toward progress): **19** (0.5%)
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
| 1 | 02 | DATE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 2 | 02 | DATE | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 3 | 02 | TIME | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 4 | 11 | CV2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 5 | 11 | CV3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 6 | 23 | IA2 | domain | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 7 | 23 | IA2 | domain | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 8 | 23 | IB1 | sentinel | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 9 | 11 | CV1 | range | neither | FALSE | TRUE | TRUE | exact_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_... |
| 10 | 11 | CV1 | range | neither | FALSE | TRUE | TRUE | exact_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_... |
| 11 | 26 | ST1 | range | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 12 | 26 | ST1 | range | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 13 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 14 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 15 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 16 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 17 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 18 | 06 | CI1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 19 | 07 | CO1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 20 | 20 | GQ1 | sentinel | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 21 | 20 | GQ1 | sentinel | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 22 | 23 | IB1 | domain | neither | FALSE | TRUE | TRUE | exact_signature | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_... |
| 23 | 26 | ST1 | domain | neither | FALSE | TRUE | TRUE | exact_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_... |
| 24 | 02 | LATITUDE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 25 | 02 | LONGITUDE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 26 | 02 | REPORT_TYPE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 27 | 02 | ELEVATION | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 28 | 02 | CALL_SIGN | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 29 | 02 | QC_PROCESS | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 30 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 31 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 32 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 33 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 34 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 35 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 36 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 37 | 04 | AA1 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 38 | 04 | AA2 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 39 | 04 | AA3 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 40 | 04 | AA4 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 41 | 04 | AA1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 42 | 04 | AA2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 43 | 04 | AA3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 44 | 04 | AA4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 45 | 04 | AA1 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 46 | 04 | AA2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 47 | 04 | AA3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 48 | 04 | AA4 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 49 | 04 | AA1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 50 | 04 | AA2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |

### Implementation gaps (strict): Not implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 02 | DATE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 2 | 02 | DATE | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 3 | 02 | TIME | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 4 | 11 | CV2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 5 | 11 | CV3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 6 | 23 | IA2 | domain | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 7 | 23 | IA2 | domain | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 8 | 23 | IB1 | sentinel | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 9 | 02 | LATITUDE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 10 | 02 | LONGITUDE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 11 | 02 | REPORT_TYPE | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 12 | 02 | ELEVATION | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 13 | 02 | CALL_SIGN | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 14 | 02 | QC_PROCESS | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 15 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 16 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 17 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 18 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 19 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 03 | WND | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 04 | AA1 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 23 | 04 | AA2 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 24 | 04 | AA3 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| 25 | 04 | AA4 | cardinality | neither | FALSE | FALSE | TRUE | wildcard_assertion | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |

### Missing tests (strict): Implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 02 | TIME | range | cleaning_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolv... |
| 2 | 09 | CT2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 3 | 09 | CT3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 4 | 10 | CU2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 5 | 10 | CU3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 6 | 10 | CU2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 7 | 10 | CU3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 8 | 11 | CV2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 9 | 11 | CV3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 10 | 11 | CV2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 11 | 11 | CV3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 12 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 13 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 14 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 15 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 16 | 13 | CX2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 17 | 13 | CX3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_i... |
| 18 | 23 | IB1 | sentinel | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_sentinel;expected_gap_from_alignment_report;test_match=none;unresolved... |
| 19 | 02 | LATITUDE | range | cleaning_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 02 | LONGITUDE | range | cleaning_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 02 | ELEVATION | range | cleaning_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 03 | WND | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 23 | 03 | WND | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 24 | 03 | WND | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |
| 25 | 03 | WND | width | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;test_match=none;unresolved_in_next_steps |

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **1241** (34.6%)
- cleaning_only: **29** (0.8%)
- both: **455** (12.7%)
- neither: **1858** (51.9%)

## Confidence breakdown

- Cleaning-implemented metric rules: **484** (13.5%)
- high: **8** (1.7%)
- medium: **476** (98.3%)
- low: **0** (0.0%)

## Match quality

| Match strength | Count | % of metric rules |
| --- | --- | --- |
| exact_signature | 390 | 10.9% |
| exact_assertion | 423 | 11.8% |
| family_assertion | 88 | 2.5% |
| wildcard_assertion | 19 | 0.5% |
| none | 2663 | 74.3% |

## Precision warnings

- Wildcard policy: `wildcard_assertion` counts as tested-any only; it never counts as strict.
- Tested-any rows matched by `exact_signature`: **390** (42.4%)
- Tested-any rows matched by `exact_assertion`: **423** (46.0%)
- Tested-any rows matched by `family_assertion`: **88** (9.6%)
- Tested-any rows matched by `wildcard_assertion`: **19** (2.1%)
- Synthetic rows in CSV: **28**
- Synthetic gap rows in CSV: **28**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested (strict): **24/171** (14.0%)
- Arity rules tested (any): **24/171** (14.0%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Suspicious coverage

- tested_any=TRUE and code_implemented=FALSE: **311** (8.7%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-04-additional-data-section.md:37-37::AA1::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA2::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA3::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA4::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:485-485::AH1::range::b9c0ae8c11 | AH | range | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:493-493::AH1::range::7157a2e995 | AH | range | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:561-561::AI1::range::e6aafd7d1d | AI | range | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-04-additional-data-section.md:569-569::AI1::range::7157a2e995 | AI | range | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:799-799::AL1::domain::f68b43c01b | AL | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_signature;unresolved_in_next_steps |
| part-04-additional-data-section.md:799-799::AL4::domain::f68b43c01b | AL | domain | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=exact_assertion;unresolved_in_next_steps |

- tested_any=TRUE and match_strength=`wildcard_assertion`: **19** (0.5%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-04-additional-data-section.md:37-37::AA1::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA2::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA3::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-04-additional-data-section.md:37-37::AA4::cardinality::78392f3dcb | AA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-05-weather-occurrence-data.md:418-418::AY1::cardinality::68a77eced2 | AY | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-05-weather-occurrence-data.md:418-418::AY2::cardinality::68a77eced2 | AY | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA1::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA2::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA3::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA4::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| 02 | 29 | 29 | 8 | 0 | 0 | 27.6% | 0.0% | 0.0% |
| 03 | 53 | 53 | 42 | 0 | 0 | 79.2% | 0.0% | 0.0% |
| 04 | 603 | 603 | 302 | 73 | 77 | 50.1% | 12.1% | 12.8% |
| 05 | 450 | 450 | 261 | 98 | 100 | 58.0% | 21.8% | 22.2% |
| 06 | 287 | 287 | 114 | 74 | 74 | 39.7% | 25.8% | 25.8% |
| 07 | 74 | 74 | 53 | 23 | 23 | 71.6% | 31.1% | 31.1% |
| 08 | 11 | 11 | 3 | 3 | 3 | 27.3% | 27.3% | 27.3% |
| 09 | 28 | 28 | 12 | 6 | 6 | 42.9% | 21.4% | 21.4% |
| 10 | 55 | 55 | 21 | 13 | 13 | 38.2% | 23.6% | 23.6% |
| 11 | 109 | 109 | 33 | 24 | 24 | 30.3% | 22.0% | 22.0% |
| 12 | 20 | 20 | 5 | 11 | 11 | 25.0% | 55.0% | 55.0% |
| 13 | 109 | 109 | 39 | 27 | 27 | 35.8% | 24.8% | 24.8% |
| 14 | 15 | 15 | 7 | 7 | 7 | 46.7% | 46.7% | 46.7% |
| 15 | 472 | 472 | 252 | 106 | 106 | 53.4% | 22.5% | 22.5% |
| 16 | 24 | 24 | 9 | 0 | 0 | 37.5% | 0.0% | 0.0% |
| 17 | 84 | 84 | 30 | 0 | 0 | 35.7% | 0.0% | 0.0% |
| 18 | 27 | 27 | 9 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| 19 | 38 | 38 | 20 | 20 | 20 | 52.6% | 52.6% | 52.6% |
| 20 | 20 | 20 | 7 | 13 | 13 | 35.0% | 65.0% | 65.0% |
| 21 | 20 | 20 | 7 | 13 | 13 | 35.0% | 65.0% | 65.0% |
| 22 | 8 | 8 | 3 | 0 | 0 | 37.5% | 0.0% | 0.0% |
| 23 | 109 | 109 | 44 | 38 | 38 | 40.4% | 34.9% | 34.9% |
| 24 | 244 | 244 | 119 | 20 | 33 | 48.8% | 8.2% | 13.5% |
| 25 | 7 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| 26 | 29 | 29 | 14 | 18 | 18 | 48.3% | 62.1% | 62.1% |
| 27 | 109 | 109 | 52 | 57 | 57 | 47.7% | 52.3% | 52.3% |
| 28 | 19 | 19 | 9 | 10 | 10 | 47.4% | 52.6% | 52.6% |
| 29 | 306 | 306 | 178 | 109 | 109 | 58.2% | 35.6% | 35.6% |
| 30 | 224 | 224 | 69 | 136 | 136 | 30.8% | 60.7% | 60.7% |

## Breakdown by identifier family

| Identifier family | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AA | 68 | 68 | 16 | 0 | 4 | 23.5% | 0.0% | 5.9% |
| AB | 12 | 12 | 4 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| AC | 10 | 10 | 6 | 0 | 0 | 60.0% | 0.0% | 0.0% |
| AD | 23 | 23 | 13 | 0 | 0 | 56.5% | 0.0% | 0.0% |
| AE | 26 | 26 | 9 | 0 | 0 | 34.6% | 0.0% | 0.0% |
| AG | 9 | 9 | 4 | 0 | 0 | 44.4% | 0.0% | 0.0% |
| AH | 126 | 126 | 72 | 19 | 19 | 57.1% | 15.1% | 15.1% |
| AI | 126 | 126 | 72 | 24 | 24 | 57.1% | 19.0% | 19.0% |
| AJ | 22 | 22 | 7 | 0 | 0 | 31.8% | 0.0% | 0.0% |
| AK | 16 | 16 | 10 | 0 | 0 | 62.5% | 0.0% | 0.0% |
| AL | 64 | 64 | 36 | 18 | 18 | 56.2% | 28.1% | 28.1% |
| AM | 23 | 23 | 13 | 0 | 0 | 56.5% | 0.0% | 0.0% |
| AN | 15 | 15 | 8 | 0 | 0 | 53.3% | 0.0% | 0.0% |
| AO | 64 | 64 | 28 | 12 | 12 | 43.8% | 18.8% | 18.8% |
| AP | 9 | 9 | 4 | 0 | 0 | 44.4% | 0.0% | 0.0% |
| AT | 80 | 80 | 40 | 17 | 17 | 50.0% | 21.2% | 21.2% |
| AU | 225 | 225 | 153 | 48 | 48 | 68.0% | 21.3% | 21.3% |
| AW | 8 | 8 | 4 | 5 | 5 | 50.0% | 62.5% | 62.5% |
| AX | 84 | 84 | 36 | 15 | 15 | 42.9% | 17.9% | 17.9% |
| AY | 26 | 26 | 12 | 0 | 2 | 46.2% | 0.0% | 7.7% |
| AZ | 26 | 26 | 16 | 13 | 13 | 61.5% | 50.0% | 50.0% |
| CALL_SIGN | 3 | 3 | 1 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| CB | 28 | 28 | 12 | 0 | 0 | 42.9% | 0.0% | 0.0% |
| CF | 33 | 33 | 12 | 0 | 0 | 36.4% | 0.0% | 0.0% |
| CG | 30 | 30 | 12 | 0 | 0 | 40.0% | 0.0% | 0.0% |
| CH | 46 | 46 | 18 | 0 | 0 | 39.1% | 0.0% | 0.0% |
| CI | 36 | 36 | 13 | 14 | 14 | 36.1% | 38.9% | 38.9% |
| CN | 113 | 113 | 47 | 60 | 60 | 41.6% | 53.1% | 53.1% |
| CO | 73 | 73 | 53 | 23 | 23 | 72.6% | 31.5% | 31.5% |
| CR | 10 | 10 | 3 | 3 | 3 | 30.0% | 30.0% | 30.0% |
| CT | 27 | 27 | 12 | 6 | 6 | 44.4% | 22.2% | 22.2% |
| CU | 54 | 54 | 21 | 13 | 13 | 38.9% | 24.1% | 24.1% |
| CV | 108 | 108 | 33 | 24 | 24 | 30.6% | 22.2% | 22.2% |
| CW | 19 | 19 | 5 | 11 | 11 | 26.3% | 57.9% | 57.9% |
| CX | 108 | 108 | 39 | 27 | 27 | 36.1% | 25.0% | 25.0% |
| DATE | 2 | 2 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| ED | 14 | 14 | 7 | 7 | 7 | 50.0% | 50.0% | 50.0% |
| ELEVATION | 3 | 3 | 1 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| GA | 24 | 24 | 18 | 9 | 9 | 75.0% | 37.5% | 37.5% |
| GD | 216 | 216 | 138 | 38 | 38 | 63.9% | 17.6% | 17.6% |
| GE | 11 | 11 | 6 | 6 | 6 | 54.5% | 54.5% | 54.5% |
| GF | 39 | 39 | 17 | 25 | 25 | 43.6% | 64.1% | 64.1% |
| GG | 144 | 144 | 60 | 28 | 28 | 41.7% | 19.4% | 19.4% |
| GH | 37 | 37 | 13 | 0 | 0 | 35.1% | 0.0% | 0.0% |
| GJ | 8 | 8 | 3 | 0 | 0 | 37.5% | 0.0% | 0.0% |
| GK | 8 | 8 | 3 | 0 | 0 | 37.5% | 0.0% | 0.0% |
| GL | 7 | 7 | 3 | 0 | 0 | 42.9% | 0.0% | 0.0% |
| GM | 43 | 43 | 17 | 0 | 0 | 39.5% | 0.0% | 0.0% |
| GN | 40 | 40 | 13 | 0 | 0 | 32.5% | 0.0% | 0.0% |
| GO | 26 | 26 | 9 | 0 | 0 | 34.6% | 0.0% | 0.0% |
| GP | 37 | 37 | 20 | 20 | 20 | 54.1% | 54.1% | 54.1% |
| GQ | 19 | 19 | 7 | 13 | 13 | 36.8% | 68.4% | 68.4% |
| GR | 19 | 19 | 7 | 13 | 13 | 36.8% | 68.4% | 68.4% |
| HAIL | 7 | 7 | 3 | 0 | 0 | 42.9% | 0.0% | 0.0% |
| IA | 16 | 16 | 6 | 7 | 7 | 37.5% | 43.8% | 43.8% |
| IB | 54 | 54 | 20 | 15 | 15 | 37.0% | 27.8% | 27.8% |
| IC | 38 | 38 | 18 | 16 | 16 | 47.4% | 42.1% | 42.1% |
| KA | 60 | 60 | 32 | 0 | 4 | 53.3% | 0.0% | 6.7% |
| KB | 45 | 45 | 21 | 0 | 3 | 46.7% | 0.0% | 6.7% |
| KC | 38 | 38 | 22 | 0 | 2 | 57.9% | 0.0% | 5.3% |
| KD | 30 | 30 | 12 | 0 | 2 | 40.0% | 0.0% | 6.7% |
| KE | 26 | 26 | 9 | 16 | 16 | 34.6% | 61.5% | 61.5% |
| KF | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| KG | 36 | 36 | 20 | 0 | 2 | 55.6% | 0.0% | 5.6% |
| LATITUDE | 3 | 3 | 1 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| LONGITUDE | 3 | 3 | 1 | 0 | 0 | 33.3% | 0.0% | 0.0% |
| MA | 13 | 13 | 5 | 6 | 6 | 38.5% | 46.2% | 46.2% |
| MD | 18 | 18 | 11 | 7 | 7 | 61.1% | 38.9% | 38.9% |
| ME | 10 | 10 | 5 | 6 | 6 | 50.0% | 60.0% | 60.0% |
| MF | 16 | 16 | 5 | 10 | 10 | 31.2% | 62.5% | 62.5% |
| MG | 15 | 15 | 5 | 7 | 7 | 33.3% | 46.7% | 46.7% |
| MH | 14 | 14 | 5 | 6 | 6 | 35.7% | 42.9% | 42.9% |
| MK | 22 | 22 | 16 | 15 | 15 | 72.7% | 68.2% | 68.2% |
| MV | 14 | 14 | 7 | 7 | 7 | 50.0% | 50.0% | 50.0% |
| MW | 4 | 4 | 2 | 3 | 3 | 50.0% | 75.0% | 75.0% |
| N | 63 | 63 | 0 | 52 | 52 | 0.0% | 82.5% | 82.5% |
| OA | 51 | 51 | 30 | 9 | 9 | 58.8% | 17.6% | 17.6% |
| OB | 48 | 48 | 16 | 32 | 32 | 33.3% | 66.7% | 66.7% |
| OC | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| OD | 63 | 63 | 45 | 17 | 17 | 71.4% | 27.0% | 27.0% |
| OE | 69 | 69 | 48 | 24 | 24 | 69.6% | 34.8% | 34.8% |
| QC_PROCESS | 2 | 2 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| REPORT_TYPE | 4 | 4 | 3 | 0 | 0 | 75.0% | 0.0% | 0.0% |
| RH | 60 | 60 | 33 | 21 | 21 | 55.0% | 35.0% | 35.0% |
| SA | 12 | 12 | 6 | 4 | 4 | 50.0% | 33.3% | 33.3% |
| ST | 28 | 28 | 14 | 18 | 18 | 50.0% | 64.3% | 64.3% |
| TIME | 2 | 2 | 1 | 0 | 0 | 50.0% | 0.0% | 0.0% |
| UA | 19 | 19 | 8 | 10 | 10 | 42.1% | 52.6% | 52.6% |
| UG | 30 | 30 | 12 | 17 | 17 | 40.0% | 56.7% | 56.7% |
| UNSPECIFIED | 36 | 36 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| WA | 13 | 13 | 7 | 8 | 8 | 53.8% | 61.5% | 61.5% |
| WD | 35 | 35 | 20 | 23 | 23 | 57.1% | 65.7% | 65.7% |
| WG | 11 | 11 | 2 | 4 | 4 | 18.2% | 36.4% | 36.4% |
| WJ | 35 | 35 | 15 | 22 | 22 | 42.9% | 62.9% | 62.9% |
| WND | 57 | 57 | 47 | 0 | 0 | 82.5% | 0.0% | 0.0% |

## Breakdown by rule type

| Rule type | Rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| range | 363 | 290 | 118 | 118 | 79.9% | 32.5% | 32.5% |
| sentinel | 688 | 580 | 160 | 160 | 84.3% | 23.3% | 23.3% |
| allowed_quality | 81 | 75 | 47 | 47 | 92.6% | 58.0% | 58.0% |
| domain | 945 | 479 | 443 | 443 | 50.7% | 46.9% | 46.9% |
| cardinality | 128 | 109 | 109 | 128 | 85.2% | 85.2% | 100.0% |
| width | 1207 | 21 | 0 | 0 | 1.7% | 0.0% | 0.0% |
| arity | 171 | 171 | 24 | 24 | 100.0% | 14.0% | 14.0% |
| unknown | 0 | 0 | 0 | 0 | excluded | excluded | excluded |

## Wildcard-only coverage (not counted toward progress)

- Wildcard-only rows (`test_covered_any=TRUE` and `test_covered_strict=FALSE`): **19** (0.5%)

| Part | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| 04 | 4 | 0.1% |
| 05 | 2 | 0.1% |
| 24 | 13 | 0.4% |

| Rule type | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| range | 0 | 0.0% |
| sentinel | 0 | 0.0% |
| allowed_quality | 0 | 0.0% |
| domain | 0 | 0.0% |
| cardinality | 19 | 0.5% |
| width | 0 | 0.0% |
| arity | 0 | 0.0% |

## Known-gap traceability

Showing top 30 expected-gap rows (full list is in `spec_coverage.csv`).

| Part | Identifier | Rule type | Code impl | Tested strict | Tested any | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 02 | DATE | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | DATE | width | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 02 | TIME | width | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV2 | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV3 | range | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 23 | IA2 | domain | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 23 | IB1 | sentinel | FALSE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 11 | CV1 | range | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 26 | ST1 | range | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 06 | CI1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 07 | CO1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 20 | GQ1 | sentinel | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 23 | IB1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 26 | ST1 | domain | FALSE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 02 | TIME | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=none;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 09 | CT3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 10 | CU3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX2 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 13 | CX3 | range | TRUE | FALSE | FALSE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=none;unresolved_in_next_steps |
| 04 | AA | range | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=wildcard_assertion;unresolved_in_next_steps |
| 04 | TMP | cardinality | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=wildcard_assertion;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
