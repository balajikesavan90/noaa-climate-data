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
- Rules implemented in code: **1957** (54.6%)
- Progress KPI (`tested_strict`): **1394** (38.9%)
- Weak coverage (`tested_any`, includes wildcard): **1407** (39.3%)
- tested_any from non-wild matches only: **1394** (38.9%)
- Wildcard-only tested_any (not counted toward progress): **13** (0.4%)
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
| 1 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 2 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 3 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 4 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 5 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 6 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 7 | 04 | AI2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 8 | 04 | AI3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 9 | 04 | AI4 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 10 | 04 | AI5 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 11 | 04 | AI6 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 12 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 13 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 14 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 15 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 16 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 17 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 18 | 04 | AI2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 19 | 04 | AI3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 04 | AI4 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 04 | AI5 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 04 | AI6 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 23 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 24 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 25 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 26 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 27 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 28 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 29 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 30 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 31 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 32 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 33 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 34 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 35 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 36 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 37 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 38 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 39 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 40 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 41 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 42 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 43 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 44 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 45 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 46 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 47 | 04 | AJ1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 48 | 04 | AJ1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 49 | 04 | AJ1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 50 | 04 | AJ1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |

### Implementation gaps (strict): Not implemented + not tested_strict

| rank | spec_part | identifier | rule_type | enforcement_layer | implemented | test_strict | test_any | match_strength | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 2 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 3 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 4 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 5 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 6 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 7 | 04 | AI2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 8 | 04 | AI3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 9 | 04 | AI4 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 10 | 04 | AI5 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 11 | 04 | AI6 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 12 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 13 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 14 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 15 | 04 | AI4 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 16 | 04 | AI5 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 17 | 04 | AI6 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 18 | 04 | AI2 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 19 | 04 | AI3 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 20 | 04 | AI4 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 21 | 04 | AI5 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 22 | 04 | AI6 | range | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 23 | 04 | AI1 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 24 | 04 | AI2 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |
| 25 | 04 | AI3 | width | neither | FALSE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=none;unresolved_in_next_steps |

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
| 18 | 04 | AI2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_pattern_range;test_match=none;unresolved_in_next_steps |
| 19 | 04 | AI3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_pattern_range;test_match=none;unresolved_in_next_steps |
| 20 | 04 | AI4 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_pattern_range;test_match=none;unresolved_in_next_steps |
| 21 | 04 | AI5 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_pattern_range;test_match=none;unresolved_in_next_steps |
| 22 | 04 | AI6 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_pattern_range;test_match=none;unresolved_in_next_steps |
| 23 | 04 | AL2 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 24 | 04 | AL3 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |
| 25 | 04 | AL4 | range | constants_only | TRUE | FALSE | FALSE | none | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;test_match=none;unresolved_in_next_steps |

## Rule Identity & Provenance

- `rule_id` format for spec rows: `{spec_file}:{start}-{end}::{identifier}::{rule_type}::{payload_hash}`.
- `rule_id` format for synthetic rows: `synthetic::{source}::{name_or_key}`.
- Rows are tracked per spec origin line range; identical payloads at different ranges remain separate rows intentionally.

## Enforcement layer breakdown

- constants_only: **1429** (39.9%)
- cleaning_only: **18** (0.5%)
- both: **510** (14.2%)
- neither: **1626** (45.4%)

## Confidence breakdown

- Cleaning-implemented metric rules: **528** (14.7%)
- high: **4** (0.8%)
- medium: **524** (99.2%)
- low: **0** (0.0%)

## Match quality

| Match strength | Count | % of metric rules |
| --- | --- | --- |
| exact_signature | 599 | 16.7% |
| exact_assertion | 711 | 19.8% |
| family_assertion | 84 | 2.3% |
| wildcard_assertion | 13 | 0.4% |
| none | 2176 | 60.7% |

## Precision warnings

- Wildcard policy: `wildcard_assertion` counts as tested-any only; it never counts as strict.
- Tested-any rows matched by `exact_signature`: **599** (42.6%)
- Tested-any rows matched by `exact_assertion`: **711** (50.5%)
- Tested-any rows matched by `family_assertion`: **84** (6.0%)
- Tested-any rows matched by `wildcard_assertion`: **13** (0.9%)
- Synthetic rows in CSV: **28**
- Synthetic gap rows in CSV: **28**
- Unknown rule rows excluded from percentages: **0**
- Arity rules tested (strict): **39/171** (22.8%)
- Arity rules tested (any): **39/171** (22.8%)
- Arity tests detected in `tests/test_cleaning.py`: **YES**

## Suspicious coverage

- tested_any=TRUE and code_implemented=FALSE: **379** (10.6%)
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

- tested_any=TRUE and match_strength=`wildcard_assertion`: **13** (0.4%)
| Rule ID | Identifier family | Rule type | Notes |
| --- | --- | --- | --- |
| part-24-temperature-data.md:9-9::KA1::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA2::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA3::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:9-9::KA4::cardinality::78392f3dcb | KA | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:71-71::KB1::cardinality::1513fc79d9 | KB | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:71-71::KB2::cardinality::1513fc79d9 | KB | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:71-71::KB3::cardinality::1513fc79d9 | KB | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:132-132::KC1::cardinality::68a77eced2 | KC | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:132-132::KC2::cardinality::68a77eced2 | KC | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |
| part-24-temperature-data.md:199-199::KD1::cardinality::68a77eced2 | KD | cardinality | coverage_reason_cleaning=none;coverage_reason_constants=none;test_match=wildcard_assertion;unresolved_in_next_steps |

## Breakdown by ISD part

| Part | Rules | Metric rules | Implemented | Tested strict | Tested any (weak) | Implemented % | Tested strict % | Tested any (weak) % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.0% | 0.0% |
| 02 | 29 | 29 | 21 | 11 | 11 | 72.4% | 37.9% | 37.9% |
| 03 | 53 | 53 | 44 | 51 | 51 | 83.0% | 96.2% | 96.2% |
| 04 | 603 | 603 | 425 | 288 | 288 | 70.5% | 47.8% | 47.8% |
| 05 | 450 | 450 | 261 | 105 | 105 | 58.0% | 23.3% | 23.3% |
| 06 | 287 | 287 | 133 | 104 | 104 | 46.3% | 36.2% | 36.2% |
| 07 | 74 | 74 | 54 | 23 | 23 | 73.0% | 31.1% | 31.1% |
| 08 | 11 | 11 | 3 | 3 | 3 | 27.3% | 27.3% | 27.3% |
| 09 | 28 | 28 | 12 | 6 | 6 | 42.9% | 21.4% | 21.4% |
| 10 | 55 | 55 | 21 | 13 | 13 | 38.2% | 23.6% | 23.6% |
| 11 | 109 | 109 | 60 | 54 | 54 | 55.0% | 49.5% | 49.5% |
| 12 | 20 | 20 | 5 | 11 | 11 | 25.0% | 55.0% | 55.0% |
| 13 | 109 | 109 | 39 | 27 | 27 | 35.8% | 24.8% | 24.8% |
| 14 | 15 | 15 | 7 | 7 | 7 | 46.7% | 46.7% | 46.7% |
| 15 | 472 | 472 | 268 | 131 | 131 | 56.8% | 27.8% | 27.8% |
| 16 | 24 | 24 | 9 | 12 | 12 | 37.5% | 50.0% | 50.0% |
| 17 | 84 | 84 | 30 | 36 | 36 | 35.7% | 42.9% | 42.9% |
| 18 | 27 | 27 | 9 | 12 | 12 | 33.3% | 44.4% | 44.4% |
| 19 | 38 | 38 | 20 | 20 | 20 | 52.6% | 52.6% | 52.6% |
| 20 | 20 | 20 | 9 | 13 | 13 | 45.0% | 65.0% | 65.0% |
| 21 | 20 | 20 | 7 | 13 | 13 | 35.0% | 65.0% | 65.0% |
| 22 | 8 | 8 | 3 | 2 | 2 | 37.5% | 25.0% | 25.0% |
| 23 | 109 | 109 | 62 | 48 | 48 | 56.9% | 44.0% | 44.0% |
| 24 | 244 | 244 | 119 | 66 | 79 | 48.8% | 27.0% | 32.4% |
| 25 | 7 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| 26 | 29 | 29 | 19 | 18 | 18 | 65.5% | 62.1% | 62.1% |
| 27 | 109 | 109 | 52 | 57 | 57 | 47.7% | 52.3% | 52.3% |
| 28 | 19 | 19 | 9 | 10 | 10 | 47.4% | 52.6% | 52.6% |
| 29 | 306 | 306 | 178 | 109 | 109 | 58.2% | 35.6% | 35.6% |
| 30 | 224 | 224 | 75 | 142 | 142 | 33.5% | 63.4% | 63.4% |

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
| AI | 126 | 126 | 72 | 24 | 24 | 57.1% | 19.0% | 19.0% |
| AJ | 22 | 22 | 7 | 14 | 14 | 31.8% | 63.6% | 63.6% |
| AK | 16 | 16 | 10 | 10 | 10 | 62.5% | 62.5% | 62.5% |
| AL | 64 | 64 | 36 | 18 | 18 | 56.2% | 28.1% | 28.1% |
| AM | 23 | 23 | 13 | 15 | 15 | 56.5% | 65.2% | 65.2% |
| AN | 15 | 15 | 8 | 9 | 9 | 53.3% | 60.0% | 60.0% |
| AO | 64 | 64 | 28 | 12 | 12 | 43.8% | 18.8% | 18.8% |
| AP | 9 | 9 | 4 | 0 | 0 | 44.4% | 0.0% | 0.0% |
| AT | 80 | 80 | 40 | 17 | 17 | 50.0% | 21.2% | 21.2% |
| AU | 225 | 225 | 153 | 48 | 48 | 68.0% | 21.3% | 21.3% |
| AW | 8 | 8 | 4 | 5 | 5 | 50.0% | 62.5% | 62.5% |
| AX | 84 | 84 | 36 | 15 | 15 | 42.9% | 17.9% | 17.9% |
| AY | 26 | 26 | 12 | 7 | 7 | 46.2% | 26.9% | 26.9% |
| AZ | 26 | 26 | 16 | 13 | 13 | 61.5% | 50.0% | 50.0% |
| CALL_SIGN | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| CB | 28 | 28 | 12 | 5 | 5 | 42.9% | 17.9% | 17.9% |
| CF | 33 | 33 | 12 | 4 | 4 | 36.4% | 12.1% | 12.1% |
| CG | 30 | 30 | 12 | 3 | 3 | 40.0% | 10.0% | 10.0% |
| CH | 46 | 46 | 18 | 9 | 9 | 39.1% | 19.6% | 19.6% |
| CI | 36 | 36 | 32 | 23 | 23 | 88.9% | 63.9% | 63.9% |
| CIG | 12 | 12 | 10 | 12 | 12 | 83.3% | 100.0% | 100.0% |
| CN | 113 | 113 | 47 | 60 | 60 | 41.6% | 53.1% | 53.1% |
| CO | 73 | 73 | 54 | 23 | 23 | 74.0% | 31.5% | 31.5% |
| CR | 10 | 10 | 3 | 3 | 3 | 30.0% | 30.0% | 30.0% |
| CT | 27 | 27 | 12 | 6 | 6 | 44.4% | 22.2% | 22.2% |
| CU | 54 | 54 | 21 | 13 | 13 | 38.9% | 24.1% | 24.1% |
| CV | 108 | 108 | 60 | 54 | 54 | 55.6% | 50.0% | 50.0% |
| CW | 19 | 19 | 5 | 11 | 11 | 26.3% | 57.9% | 57.9% |
| CX | 108 | 108 | 39 | 27 | 27 | 36.1% | 25.0% | 25.0% |
| DATE | 2 | 2 | 2 | 2 | 2 | 100.0% | 100.0% | 100.0% |
| DEW | 5 | 5 | 4 | 4 | 4 | 80.0% | 80.0% | 80.0% |
| ED | 14 | 14 | 7 | 7 | 7 | 50.0% | 50.0% | 50.0% |
| ELEVATION | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| GA | 24 | 24 | 18 | 9 | 9 | 75.0% | 37.5% | 37.5% |
| GD | 216 | 216 | 138 | 38 | 38 | 63.9% | 17.6% | 17.6% |
| GE | 11 | 11 | 6 | 6 | 6 | 54.5% | 54.5% | 54.5% |
| GF | 39 | 39 | 17 | 25 | 25 | 43.6% | 64.1% | 64.1% |
| GG | 144 | 144 | 60 | 28 | 28 | 41.7% | 19.4% | 19.4% |
| GH | 37 | 37 | 29 | 25 | 25 | 78.4% | 67.6% | 67.6% |
| GJ | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| GK | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| GL | 7 | 7 | 3 | 4 | 4 | 42.9% | 57.1% | 57.1% |
| GM | 43 | 43 | 17 | 18 | 18 | 39.5% | 41.9% | 41.9% |
| GN | 40 | 40 | 13 | 18 | 18 | 32.5% | 45.0% | 45.0% |
| GO | 26 | 26 | 9 | 12 | 12 | 34.6% | 46.2% | 46.2% |
| GP | 37 | 37 | 20 | 20 | 20 | 54.1% | 54.1% | 54.1% |
| GQ | 19 | 19 | 9 | 13 | 13 | 47.4% | 68.4% | 68.4% |
| GR | 19 | 19 | 7 | 13 | 13 | 36.8% | 68.4% | 68.4% |
| HAIL | 7 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| IA | 16 | 16 | 12 | 9 | 9 | 75.0% | 56.2% | 56.2% |
| IB | 54 | 54 | 32 | 23 | 23 | 59.3% | 42.6% | 42.6% |
| IC | 38 | 38 | 18 | 16 | 16 | 47.4% | 42.1% | 42.1% |
| KA | 60 | 60 | 32 | 8 | 12 | 53.3% | 13.3% | 20.0% |
| KB | 45 | 45 | 21 | 8 | 11 | 46.7% | 17.8% | 24.4% |
| KC | 38 | 38 | 22 | 11 | 13 | 57.9% | 28.9% | 34.2% |
| KD | 30 | 30 | 12 | 8 | 10 | 40.0% | 26.7% | 33.3% |
| KE | 26 | 26 | 9 | 16 | 16 | 34.6% | 61.5% | 61.5% |
| KF | 8 | 8 | 3 | 4 | 4 | 37.5% | 50.0% | 50.0% |
| KG | 36 | 36 | 20 | 11 | 13 | 55.6% | 30.6% | 36.1% |
| LATITUDE | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
| LONGITUDE | 3 | 3 | 3 | 1 | 1 | 100.0% | 33.3% | 33.3% |
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
| QC_PROCESS | 2 | 2 | 1 | 0 | 0 | 50.0% | 0.0% | 0.0% |
| REPORT_TYPE | 4 | 4 | 4 | 3 | 3 | 100.0% | 75.0% | 75.0% |
| RH | 60 | 60 | 33 | 21 | 21 | 55.0% | 35.0% | 35.0% |
| SA | 12 | 12 | 6 | 4 | 4 | 50.0% | 33.3% | 33.3% |
| SLP | 5 | 5 | 3 | 5 | 5 | 60.0% | 100.0% | 100.0% |
| ST | 28 | 28 | 19 | 18 | 18 | 67.9% | 64.3% | 64.3% |
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
| range | 363 | 331 | 218 | 218 | 91.2% | 60.1% | 60.1% |
| sentinel | 688 | 595 | 240 | 240 | 86.5% | 34.9% | 34.9% |
| allowed_quality | 81 | 75 | 64 | 64 | 92.6% | 79.0% | 79.0% |
| domain | 945 | 525 | 605 | 605 | 55.6% | 64.0% | 64.0% |
| cardinality | 128 | 113 | 115 | 128 | 88.3% | 89.8% | 100.0% |
| width | 1207 | 147 | 113 | 113 | 12.2% | 9.4% | 9.4% |
| arity | 171 | 171 | 39 | 39 | 100.0% | 22.8% | 22.8% |
| unknown | 0 | 0 | 0 | 0 | excluded | excluded | excluded |

## Wildcard-only coverage (not counted toward progress)

- Wildcard-only rows (`test_covered_any=TRUE` and `test_covered_strict=FALSE`): **13** (0.4%)

| Part | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| 24 | 13 | 0.4% |

| Rule type | Wildcard-only rows | % of metric rules |
| --- | --- | --- |
| range | 0 | 0.0% |
| sentinel | 0 | 0.0% |
| allowed_quality | 0 | 0.0% |
| domain | 0 | 0.0% |
| cardinality | 13 | 0.4% |
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
| 04 | TMP | cardinality | FALSE | FALSE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=none;expected_gap_from_alignment_report;synthetic_gap_row;test_match=wildcard_assertion;unresolved_in_next_steps |
| 02 | DATE | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | DATE | width | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 02 | TIME | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=exact_fallback_bounds;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_signature;unresolved_in_next_steps |
| 02 | TIME | width | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=strict_gate_width;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 06 | CI1 | range | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=field_rule_minmax;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO2 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=exact_assertion;unresolved_in_next_steps |
| 07 | CO3 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO4 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO5 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO6 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO7 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO8 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
| 07 | CO9 | cardinality | TRUE | TRUE | TRUE | coverage_reason_cleaning=none;coverage_reason_constants=repeated_identifier_range;expected_gap_from_alignment_report;test_match=family_assertion;unresolved_in_next_steps |
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

## How to extend

- Add or tweak regexes in `parse_spec_docs()` for new rule text patterns.
- Extend `infer_rule_types_from_text()` if new rule classes appear.
- Extend `coverage_in_constants_for_row()` and `coverage_in_cleaning_for_row()` for new enforcement metadata.
- Extend `parse_tests_evidence()` value-token and assertion-intent hooks for new test styles.
- Keep deterministic ordering by preserving `sort_key()` and fixed table order.
