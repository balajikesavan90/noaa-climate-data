# NOAA ISD Cleaning Pipeline Validation Plan

**Version:** 1.0  
**Last Updated:** 2026-02-21  
**Status:** Active  

---

## 1. Validation Objectives

### 1.1 What "Correct" Means for This Pipeline

A NOAA ISD cleaning pipeline output is **correct** if and only if:

1. **Sentinel Safety**: Missing-value sentinels (e.g., `+9999`, `999999`) NEVER appear as numeric values in cleaned output columns.
2. **Scale Fidelity**: All temperature, dew point, pressure, and other scale-requiring fields are correctly transformed by their documented scale factors (typically ÷10 or ÷100).
3. **Quality Flag Governance**: Per-value quality flags correctly null or preserve their governed field parts according to NOAA quality codes defined in `QUALITY_FLAGS`.
4. **Structural Conformance**: All parsed field parts match their spec-declared widths, cardinalities, and allowed-value constraints as defined in `constants.py` field rules.
5. **Idempotency**: Running `clean_noaa_dataframe()` twice on the same input produces identical output (no hidden state, no non-deterministic behavior).
6. **Domain Invariants**: Physical impossibilities are rejected (e.g., temperature < -273.15°C, latitude outside ±90°, wind speed < 0).
7. **Aggregation Consistency**: Monthly/yearly aggregates are derived only from complete time periods (≥20 days/month, full 12-month years) and numeric-mean semantics match researcher expectations.
8. **Traceability**: For any spec rule marked `code_implemented=TRUE` and `test_covered_strict=TRUE`, there exists demonstrable evidence in either cleaned output or rejection logs that the rule is enforced.

### 1.2 Primary KPIs

- **Progress KPI**: `test_covered_strict` ≥ 95% of metric-eligible spec rules (current: 63.6%)
- **Correctness KPI**: Zero P0 sentinel-leakage, scale-factor, or quality-flag bugs in production outputs
- **Regression KPI**: Zero false-positive test failures on unchanged code after refactoring
- **Coverage Precision**: `tested_any=TRUE AND code_implemented=FALSE` cases reduced to ≤ 1% (current: 11.2%)

---

## 2. Validation Tracks

Each track is **mandatory** for v1.0 release. All tracks must show "PASS" status before declaring the pipeline production-ready.

---

### Track A: Golden-File Tests (Deterministic Reference Outputs)

#### A.1 Purpose
Hand-curated mini datasets with known-correct expected outputs. These serve as regression anchors and concrete examples of spec compliance.

#### A.2 Artifacts to Create

1. **Input fixtures** (`tests/fixtures/golden/inputs/`):
   - `sentinel_edge_cases.csv`: All known sentinel patterns (+9999, 999999, 99.99, etc.) for TMP, DEW, SLP, VIS, CIG, WND
   - `scale_factors.csv`: Pre-scale values with known post-scale expected results
   - `quality_flags.csv`: All NOAA quality codes (0-9, A-I) applied to various fields
   - `multi_occurrence_fields.csv`: Repeated fields (AA1-AA4, CO1-CO9) with varying cardinalities
   - `mandatory_section.csv`: Minimal valid ISD record with only control + mandatory sections
   - `full_additional_data.csv`: Record with ≥10 additional-data sections to test parsing breadth

2. **Expected output fixtures** (`tests/fixtures/golden/expected/`):
   - For each input CSV above, create `<input_name>_expected_cleaned.parquet` with exact column layout and values
   - Column naming must follow `<field>__value`, `<field>__quality`, `<field>__partN` conventions
   - Include `.json` sidecar with metadata: `{"created": "YYYY-MM-DD", "spec_rules": ["rule_id1", "rule_id2"], "notes": "..."}`

#### A.3 Test Implementation

```python
# tests/test_golden_files.py
import pytest
import pandas as pd
from pathlib import Path

GOLDEN_INPUT = Path("tests/fixtures/golden/inputs")
GOLDEN_EXPECTED = Path("tests/fixtures/golden/expected")

@pytest.mark.golden
@pytest.mark.parametrize("fixture_name", [
    "sentinel_edge_cases",
    "scale_factors",
    "quality_flags",
    "multi_occurrence_fields",
    "mandatory_section",
    "full_additional_data",
])
def test_golden_file_cleaning(fixture_name):
    """Golden-file test for deterministic cleaning behavior."""
    input_csv = GOLDEN_INPUT / f"{fixture_name}.csv"
    expected_parquet = GOLDEN_EXPECTED / f"{fixture_name}_expected_cleaned.parquet"
    
    # Run cleaning pipeline
    actual = clean_noaa_dataframe(pd.read_csv(input_csv))
    expected = pd.read_parquet(expected_parquet)
    
    # Assert exact match (column order, dtypes, values, nulls)
    pd.testing.assert_frame_equal(actual, expected, check_dtype=True, check_exact=True)
```

#### A.4 How to Run

```bash
# Run only golden-file tests
poetry run pytest tests/test_golden_files.py -v -m golden

# Update expected outputs after intentional changes (manual approval required)
poetry run python tests/fixtures/golden/regenerate_expected.py --approve
```

#### A.5 Storage & Versioning

- Store all fixtures in `tests/fixtures/golden/` (committed to git)
- Expected outputs are **source-controlled** and require explicit approval to update
- Each fixture must include a `README.md` describing its purpose and which spec rules it exercises

#### A.6 CI Integration

```yaml
# .github/workflows/validation.yml
- name: Golden File Tests
  run: poetry run pytest tests/test_golden_files.py -v -m golden --tb=short
  # Fail on any difference; no auto-regeneration in CI
```

#### A.7 Acceptance Criteria

- [ ] All 6 baseline golden files created and committed
- [ ] `test_golden_files.py` implemented with exact-match assertions
- [ ] Zero test failures on current main branch
- [ ] Golden-file updates require explicit git diff review

---

### Track B: Invariant/Property Tests (Domain Constraints)

#### B.1 Purpose
Assert universal truth properties about pipeline outputs, regardless of input data. These catch logic errors that golden files might miss.

#### B.2 Invariants to Test

1. **Sentinel Exclusion Property**:
   ```python
   # No numeric column should contain values matching sentinel patterns
   for col in numeric_columns:
       assert not any(df[col].astype(str).str.match(r"^[+]?9{4,}$"))
   ```

2. **Scale Factor Consistency**:
   ```python
   # TMP, DEW must be in reasonable range after scaling (÷10)
   assert df["temperature_c__value"].between(-100, 60).all()
   assert df["dew_point_c__value"].between(-100, 40).all()
   ```

3. **Quality Nullification**:
   ```python
   # If quality flag is bad (not in [0,1,4,5,9,A,C,I]), value must be null
   bad_quality = ~df["temperature_c__quality"].isin(QUALITY_FLAGS["passed"])
   assert df.loc[bad_quality, "temperature_c__value"].isna().all()
   ```

4. **Idempotency**:
   ```python
   cleaned_once = clean_noaa_dataframe(raw)
   cleaned_twice = clean_noaa_dataframe(cleaned_once)
   pd.testing.assert_frame_equal(cleaned_once, cleaned_twice)
   ```

5. **Physical Domain Constraints**:
   ```python
   # No negative visibility or wind speed
   assert (df["visibility_m__value"] >= 0).all()
   assert (df["wind_speed_ms__value"] >= 0).all()
   
   # Latitude [-90, 90], Longitude [-180, 180]
   assert df["latitude"].between(-90, 90).all()
   assert df["longitude"].between(-180, 180).all()
   ```

6. **Aggregation Completeness**:
   ```python
   # Monthly data must have ≥20 days per month
   monthly_counts = monthly_df.groupby(["year", "month"]).size()
   assert (monthly_counts >= 20).all()
   
   # Yearly data requires full 12 months
   yearly_month_counts = yearly_df.groupby("year")["month"].nunique()
   assert (yearly_month_counts == 12).all()
   ```

#### B.3 Test Implementation

```python
# tests/test_invariants.py
import pytest
import pandas as pd
from noaa_climate_data.cleaning import clean_noaa_dataframe
from noaa_climate_data.constants import QUALITY_FLAGS

@pytest.mark.invariant
class TestCleaningInvariants:
    
    @pytest.mark.parametrize("sample_csv", ["station_01116099999.csv", "station_12930099999.csv"])
    def test_no_sentinel_leakage(self, sample_csv):
        """Sentinels must not appear in numeric outputs."""
        raw = pd.read_csv(f"tests/fixtures/samples/{sample_csv}")
        cleaned = clean_noaa_dataframe(raw)
        
        numeric_cols = cleaned.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            sentinel_pattern = r"^[+\-]?9{4,}$"
            leaked = cleaned[col].astype(str).str.match(sentinel_pattern)
            assert not leaked.any(), f"Sentinel leaked in {col}"
    
    def test_idempotency(self):
        """Cleaning twice produces identical output."""
        raw = pd.read_csv("tests/fixtures/samples/basic_station.csv")
        once = clean_noaa_dataframe(raw)
        twice = clean_noaa_dataframe(once)
        pd.testing.assert_frame_equal(once, twice)
    
    # Additional invariant tests...
```

#### B.4 How to Run

```bash
poetry run pytest tests/test_invariants.py -v -m invariant
```

#### B.5 Storage

- Test code in `tests/test_invariants.py`
- Sample inputs in `tests/fixtures/samples/` (real station extracts, 100-1000 rows each)
- Logs saved to `docs/validation_artifacts/invariant_logs/` on failure

#### B.6 CI Integration

```yaml
- name: Invariant Property Tests
  run: poetry run pytest tests/test_invariants.py -v -m invariant --tb=short
```

#### B.7 Acceptance Criteria

- [ ] All 6 core invariants implemented and passing
- [ ] At least 3 real sample stations tested per invariant
- [ ] Zero invariant violations on current codebase

---

### Track C: Differential Tests (Regression Detection)

#### C.1 Purpose
Compare outputs across pipeline versions or configuration changes to detect unintended behavioral drift.

#### C.2 What to Compare

1. **Version-to-version**: Compare cleaned outputs from `main` vs. feature branch
2. **Configuration variations**: Test with different `enforce_domain` strictness levels
3. **Aggregation strategies**: Compare "best_hour" vs. "fixed_hour" vs. "hour_day_month_year"

#### C.3 Artifacts

1. **Baseline snapshots** (`tests/fixtures/differential/baselines/`):
   - Store cleaned outputs from known-good commit (e.g., `v0.9.0`)
   - Include metadata: commit SHA, run timestamp, Python version

2. **Diff reports** (`docs/validation_artifacts/differential_reports/`):
   - CSV format: `[column, baseline_mean, current_mean, diff_%, row_count_changed, null_count_diff]`
   - Human-readable summary with thresholds:
     - `diff_% < 0.1%` → GREEN
     - `0.1% ≤ diff_% < 1%` → YELLOW (review)
     - `diff_% ≥ 1%` → RED (regression)

#### C.4 Test Implementation

```python
# tests/test_differential.py
import pytest
import pandas as pd
from pathlib import Path

BASELINE_DIR = Path("tests/fixtures/differential/baselines")
REPORT_DIR = Path("docs/validation_artifacts/differential_reports")

@pytest.mark.differential
def test_cleaning_regression_vs_baseline():
    """Detect unexpected changes vs. baseline cleaned output."""
    baseline = pd.read_parquet(BASELINE_DIR / "station_01116099999_cleaned.parquet")
    current = clean_noaa_dataframe(pd.read_csv("tests/fixtures/samples/station_01116099999.csv"))
    
    diff_report = []
    for col in baseline.columns:
        if col not in current.columns:
            diff_report.append({"column": col, "status": "REMOVED"})
            continue
        
        if pd.api.types.is_numeric_dtype(baseline[col]):
            baseline_mean = baseline[col].mean()
            current_mean = current[col].mean()
            diff_pct = abs(current_mean - baseline_mean) / baseline_mean * 100 if baseline_mean else 0
            
            status = "GREEN" if diff_pct < 0.1 else ("YELLOW" if diff_pct < 1 else "RED")
            diff_report.append({
                "column": col,
                "baseline_mean": baseline_mean,
                "current_mean": current_mean,
                "diff_%": diff_pct,
                "status": status,
            })
    
    # Save report
    report_df = pd.DataFrame(diff_report)
    report_df.to_csv(REPORT_DIR / "regression_report.csv", index=False)
    
    # Fail if any RED status
    assert not (report_df["status"] == "RED").any(), "Regression detected"
```

#### C.5 How to Run

```bash
# Capture new baseline after approved changes
poetry run python tests/fixtures/differential/capture_baseline.py --commit-sha $(git rev-parse HEAD)

# Run differential tests
poetry run pytest tests/test_differential.py -v -m differential

# View latest diff report
cat docs/validation_artifacts/differential_reports/regression_report.csv
```

#### C.6 Storage

- Baselines: `tests/fixtures/differential/baselines/` (versioned)
- Reports: `docs/validation_artifacts/differential_reports/` (gitignored; CI artifacts)

#### C.7 CI Integration

```yaml
- name: Differential Regression Tests
  run: |
    poetry run pytest tests/test_differential.py -v -m differential
    # Upload diff reports as artifacts
- uses: actions/upload-artifact@v3
  with:
    name: differential-reports
    path: docs/validation_artifacts/differential_reports/
```

#### C.8 Acceptance Criteria

- [ ] Baseline captured for at least 5 representative stations
- [ ] Differential test framework operational
- [ ] Current codebase shows <0.1% drift from baselines (all GREEN)

---

### Track D: Spec-to-Output Traceability Audit

#### D.1 Purpose
Provide forensic evidence that spec rules marked as "implemented" and "tested" actually manifest in cleaned outputs or rejection logs.

#### D.2 Audit Methodology

1. **Sample Selection**:
   - Query `spec_coverage.csv` for rows where `code_implemented=TRUE` and `test_covered_strict=TRUE`
   - Randomly sample 50 rules across all enforcement layers and rule types
   - Ensure coverage of: domain, range, width, cardinality, scale, quality rules

2. **Evidence Collection**:
   For each sampled rule, provide one of:
   - **Positive evidence**: Show cleaned output where rule is enforced (e.g., value within range, quality flag nulled bad value)
   - **Negative evidence**: Show input that violates rule + demonstrate it was rejected/nulled in output
   - **Test citation**: Link to specific test assertion in `tests/test_cleaning.py` that exercises the rule

3. **Output Format**:
   ```json
   {
     "rule_id": "part-03-mandatory-data-section.md:207-225::TMP::domain::52bade1af7",
     "identifier": "TMP",
     "rule_type": "domain",
     "enforcement_layer": "cleaning_only",
     "evidence_type": "negative",
     "input_value": "+9999",
     "output_value": null,
     "test_file": "tests/test_cleaning.py",
     "test_line": 45,
     "notes": "Sentinel +9999 correctly nulled in TMP__value column"
   }
   ```

#### D.3 Artifacts

1. **Audit queue** (`docs/validation_artifacts/traceability/audit_queue.csv`):
   - Generated by: `python tools/spec_coverage/generate_audit_queue.py --sample-size 50`
   - Columns: `rule_id`, `identifier`, `rule_type`, `enforcement_layer`, `evidence_provided`, `evidence_type`, `audited_by`, `audited_date`

2. **Evidence bundle** (`docs/validation_artifacts/traceability/evidence/`):
   - One JSON file per audited rule
   - Include input/output CSV snippets (max 10 rows)

#### D.4 Test/Script Implementation

```python
# tools/spec_coverage/sample_audit_rules.py
import pandas as pd
from pathlib import Path

def generate_audit_queue(sample_size=50, output_path="docs/validation_artifacts/traceability/audit_queue.csv"):
    """Sample spec rules for traceability audit."""
    coverage = pd.read_csv("spec_coverage.csv")
    
    # Filter to implemented + strict-tested
    eligible = coverage[
        (coverage["code_implemented"] == True) & 
        (coverage["test_covered_strict"] == True)
    ]
    
    # Stratified sample across enforcement layers
    queue = eligible.groupby("enforcement_layer").sample(
        n=sample_size // 4, 
        random_state=42
    )
    
    queue["evidence_provided"] = False
    queue.to_csv(output_path, index=False)
    print(f"Audit queue saved: {output_path}")

# Manual audit step (human review)
# tests/test_traceability_audit.py validates that all queue items have evidence
@pytest.mark.traceability
def test_all_audited_rules_have_evidence():
    """Ensure all sampled rules in audit queue have evidence bundle."""
    queue = pd.read_csv("docs/validation_artifacts/traceability/audit_queue.csv")
    evidence_dir = Path("docs/validation_artifacts/traceability/evidence")
    
    for idx, row in queue.iterrows():
        rule_id_hash = row["rule_id"].split("::")[-1]
        evidence_file = evidence_dir / f"{rule_id_hash}.json"
        assert evidence_file.exists(), f"Missing evidence for {row['rule_id']}"
```

#### D.5 How to Run

```bash
# 1. Generate audit queue
poetry run python tools/spec_coverage/sample_audit_rules.py

# 2. Manual audit: collect evidence for each rule (human QA step)
# Edit audit_queue.csv → mark evidence_provided=TRUE after collecting evidence

# 3. Validate evidence completeness
poetry run pytest tests/test_traceability_audit.py -v -m traceability
```

#### D.6 Storage

- Audit queue: `docs/validation_artifacts/traceability/audit_queue.csv` (committed)
- Evidence bundles: `docs/validation_artifacts/traceability/evidence/*.json` (committed)
- Audit log: `docs/validation_artifacts/traceability/audit_log.md` (human-readable summary)

#### D.7 CI Integration

```yaml
- name: Traceability Audit Validation
  run: poetry run pytest tests/test_traceability_audit.py -v -m traceability
  # Fails if any audited rule lacks evidence bundle
```

#### D.8 Acceptance Criteria

- [ ] Audit queue generated with ≥50 sampled rules
- [ ] Evidence bundle created for 100% of sampled rules
- [ ] At least 3 examples each of positive/negative evidence
- [ ] Audit log documents any rules where evidence is weak or missing

---

### Track E: "Suspicious Coverage" Audit

#### E.1 Purpose
Investigate and resolve the 401 cases (11.2%) where `tested_any=TRUE` but `code_implemented=FALSE`, plus the 2 wildcard-only matches.

#### E.2 Root Cause Categories

1. **False Positive Tests**: Test asserts behavior that doesn't actually exist in code (test may be wrong)
2. **Indirect Implementation**: Rule enforced via side effect (e.g., pandas auto-conversion) but not explicit code
3. **Deprecated Spec Rules**: Rule is obsolete/irrelevant to our pipeline scope
4. **Wildcard Over-Matching**: Test uses `assert "pattern" in output` without precise column/value check

#### E.3 Audit Procedure

For each suspicious case:

1. **Locate Test**: Find the test assertion that triggered `tested_any=TRUE`
   ```bash
   # Example for CIG domain rule
   grep -rn "CIG" tests/test_cleaning.py
   ```

2. **Trace Code Path**: Verify if rule is actually enforced in `cleaning.py` or `constants.py`
   ```bash
   grep -rn "CIG" src/noaa_climate_data/cleaning.py
   grep -rn "CIG" src/noaa_climate_data/constants.py
   ```

3. **Classify & Document**:
   - If test is correct but code missing → **ACTION: Implement code**
   - If test is wildcard/weak → **ACTION: Strengthen test to exact assertion**
   - If rule is out-of-scope → **ACTION: Mark as expected-gap in coverage report**
   - If implementation exists but not detected → **ACTION: Fix coverage detector**

4. **Record in Audit Log**:
   ```markdown
   ## CIG domain rule (part-03:99-99::CIG::domain)
   - **Status**: Test over-matches
   - **Root Cause**: Test uses `assert "ceiling_height_m" in df.columns` but doesn't check actual domain enforcement
   - **Resolution**: Updated test to `assert df["ceiling_height_m__value"].between(0, 22000).all()`
   - **Auditor**: @username
   - **Date**: 2026-02-21
   ```

#### E.4 Artifacts

1. **Suspicious cases export** (`docs/validation_artifacts/suspicious_coverage/suspicious_cases.csv`):
   ```bash
   python tools/spec_coverage/export_suspicious_cases.py
   ```

2. **Audit log** (`docs/validation_artifacts/suspicious_coverage/audit_log.md`):
   - One section per audited rule
   - Include: rule ID, status, root cause, resolution, auditor, date

3. **Wildcard inventory** (`docs/validation_artifacts/suspicious_coverage/wildcard_matches.csv`):
   - List of all tests using wildcard assertions
   - Action plan to replace with exact assertions

#### E.5 Test/Script Implementation

```python
# tools/spec_coverage/export_suspicious_cases.py
import pandas as pd

def export_suspicious_cases():
    """Extract suspicious coverage cases for audit."""
    coverage = pd.read_csv("spec_coverage.csv")
    
    # Case 1: tested_any=TRUE but code_implemented=FALSE
    false_positives = coverage[
        (coverage["test_covered_any"] == True) & 
        (coverage["code_implemented"] == False)
    ]
    
    # Case 2: wildcard-only matches
    wildcards = coverage[coverage["match_strength"] == "wildcard_assertion"]
    
    suspicious = pd.concat([false_positives, wildcards]).drop_duplicates()
    suspicious.to_csv("docs/validation_artifacts/suspicious_coverage/suspicious_cases.csv", index=False)
    print(f"Exported {len(suspicious)} suspicious cases")

# tests/test_suspicious_audit.py
@pytest.mark.suspicious
def test_no_unresolved_suspicious_coverage():
    """All suspicious coverage cases must be audited and resolved."""
    audit_log = Path("docs/validation_artifacts/suspicious_coverage/audit_log.md").read_text()
    suspicious = pd.read_csv("docs/validation_artifacts/suspicious_coverage/suspicious_cases.csv")
    
    for idx, row in suspicious.iterrows():
        rule_id = row["rule_id"]
        assert rule_id in audit_log, f"Unaudited suspicious case: {rule_id}"
```

#### E.6 How to Run

```bash
# 1. Export suspicious cases
poetry run python tools/spec_coverage/export_suspicious_cases.py

# 2. Manual audit: review each case and document in audit_log.md

# 3. Validate all cases audited
poetry run pytest tests/test_suspicious_audit.py -v -m suspicious
```

#### E.7 Storage

- Suspicious cases list: `docs/validation_artifacts/suspicious_coverage/suspicious_cases.csv` (regenerated on demand)
- Audit log: `docs/validation_artifacts/suspicious_coverage/audit_log.md` (committed, append-only)
- Resolution tracking: `docs/validation_artifacts/suspicious_coverage/resolution_tracker.csv` (columns: `rule_id`, `status`, `resolution_type`, `resolved_date`)

#### E.8 CI Integration

```yaml
- name: Suspicious Coverage Audit Check
  run: poetry run pytest tests/test_suspicious_audit.py -v -m suspicious
  # Requires all exported suspicious cases to have audit log entry
```

#### E.9 Acceptance Criteria

- [ ] All 401 `tested_any=TRUE & code_implemented=FALSE` cases exported
- [ ] ≥90% of suspicious cases audited and documented
- [ ] All 2 wildcard-only matches replaced with exact assertions
- [ ] Remaining unresolved cases tagged as `expected-gap` in coverage report

---

## 3. Validation Checklist (v1.0 Release Gate)

### 3.1 Mandatory Pass Criteria

All checkboxes must be ticked before v1.0 release:

**Track A: Golden Files**
- [ ] 6+ golden input files created and committed
- [ ] 6+ expected output files generated and reviewed
- [ ] `test_golden_files.py` passes with 100% success rate
- [ ] Golden-file update process documented

**Track B: Invariants**
- [ ] All 6 core invariants implemented
- [ ] Invariant tests pass on ≥3 real sample stations
- [ ] No sentinel leakage detected in last 50 test runs
- [ ] Idempotency verified on all test fixtures

**Track C: Differential**
- [ ] Baseline snapshots captured for 5+ stations
- [ ] Differential tests show <0.1% drift from baselines
- [ ] Diff report generation automated
- [ ] No RED-status regressions in current codebase

**Track D: Traceability**
- [ ] ≥50 spec rules sampled for audit
- [ ] Evidence bundle created for 100% of sampled rules
- [ ] Evidence includes positive + negative examples
- [ ] Traceability audit log completed

**Track E: Suspicious Coverage**
- [ ] All 401 suspicious cases exported and reviewed
- [ ] ≥90% of cases audited with documented resolution
- [ ] Wildcard assertions reduced to <0.05% (target: 0)
- [ ] Coverage tool updated to reduce false positives

**General Quality Gates**
- [ ] `test_covered_strict` ≥ 95% (current: 63.6%)
- [ ] All P0 tests (sentinel, scale, quality) passing
- [ ] CI runs all 5 validation tracks without failure
- [ ] README.md updated with validation status badge

### 3.2 Stop Condition (Pipeline is Production-Ready)

The pipeline is **production-ready** when:

1. **All mandatory checkboxes** in §3.1 are ticked
2. **Zero P0 bugs** in last 30 days (sentinel leakage, scale errors, quality mishandling)
3. **Coverage KPI met**: `test_covered_strict ≥ 95%`
4. **Validation tracks stable**: All 5 tracks show PASS status for ≥3 consecutive CI runs
5. **Audit debt resolved**: Suspicious coverage cases <1% and traceability evidence complete
6. **Documentation complete**: All validation artifacts committed and README.md updated

**Sign-off required from**: Lead Engineer + QA Lead

---

## 4. Known Threats to Validity

### 4.1 Coverage Metric Limitations

#### Threat: Wildcard Assertions Inflate `tested_any`
- **Current Status**: 2 rules (0.1%) rely on wildcard-only matches
- **Risk**: Tests assert vague patterns (e.g., `"TMP" in output`) without verifying actual cleaning logic
- **Mitigation**: Track E audits all wildcard cases; replace with exact assertions (e.g., `assert df["temperature_c__value"].dtype == float`)
- **Validation**: Monitor `wildcard_assertion` count in spec coverage reports; target: 0

#### Threat: `tested_strict` vs. `tested_any` Gap
- **Current Status**: 2 rules show `tested_any=TRUE` but `tested_strict=FALSE` (wildcard-only)
- **Risk**: False confidence that a rule is tested when coverage is weak
- **Mitigation**: Policy change: only `tested_strict` counts toward progress KPI
- **Validation**: Track B invariant tests enforce concrete behavior; wildcard tests insufficient

#### Threat: `match_strength` Ambiguity
- **Current Status**: 
  - `exact_signature`: 18.8%
  - `exact_assertion`: 44.0%
  - `family_assertion`: 0.8%
  - `wildcard_assertion`: 0.1%
  - `none`: 36.3%
- **Risk**: "none" and "family_assertion" may hide under-specified tests
- **Mitigation**: Track D traceability audit requires evidence for all implemented rules; weak matches flagged for review
- **Validation**: Audit log must document why `match_strength=family_assertion` or `none` is acceptable

### 4.2 Code Implementation Detection Gaps

#### Threat: `tested_any=TRUE & code_implemented=FALSE` (401 cases, 11.2%)
- **Root Causes**:
  1. Tests assert indirect behavior (e.g., pandas auto-converts types) not explicit in our code
  2. Coverage detector misses indirect enforcement (e.g., range checks in constants propagate to cleaning)
  3. Tests are over-optimistic or wrong
- **Risk**: Spec rules falsely believed to be covered; may fail on edge cases not in test data
- **Mitigation**: Track E suspicious coverage audit investigates every case; classify as false-positive test, indirect implementation, or out-of-scope
- **Validation**: Reduce suspicious cases to <1% via audit; remaining cases tagged as `expected-gap`

#### Threat: Enforcement Layer Misclassification
- **Current Status**:
  - `constants_only`: 63.0%
  - `cleaning_only`: 0.5%
  - `both`: 14.2%
  - `neither`: 22.2%
- **Risk**: "neither" layer (796 rules) may represent missing implementation or detector blind spots
- **Mitigation**: Cross-reference "neither" rules against code comments and expected-gap tags; validate via Track D traceability
- **Validation**: For any "neither" rule marked `code_implemented=TRUE`, require evidence that it's enforced indirectly (e.g., by dependencies)

### 4.3 Test Data Coverage Biases

#### Threat: Golden Files May Miss Real-World Diversity
- **Risk**: Hand-curated fixtures are clean and predictable; real NOAA data has unexpected encoding errors, malformed records, mixed versions
- **Mitigation**: Track B invariant tests run on real sample stations (not synthetic); Track C differential tests use production-like data
- **Validation**: Download ≥10 real station CSVs spanning 1990-2025; include in sample fixtures; document edge cases found

#### Threat: Sample Stations May Be Unrepresentative
- **Risk**: If all samples come from US/Europe, pipeline may fail on tropical, polar, or marine stations
- **Mitigation**: Stratify sample selection by:
  - Geography: ≥1 station per continent
  - Elevation: sea-level, mid-altitude, high-altitude
  - Data density: sparse (1960s), dense (2010s), mixed
- **Validation**: Document sample station metadata in `tests/fixtures/samples/README.md`

### 4.4 Aggregation Correctness Assumptions

#### Threat: "Best Hour" Selection May Introduce Bias
- **Current Logic**: Choose hour with most unique days, then aggregate only that hour across months/years
- **Risk**: If station reports sporadically (e.g., only during storms), "best hour" may not be representative
- **Mitigation**: Alternative aggregation strategies tested via Track C differential; document trade-offs in pipeline docs
- **Validation**: Compare "best_hour" vs. "fixed_hour=12" vs. "hour_day_month_year" on ≥5 stations; verify <5% mean difference

#### Threat: Completeness Filters May Over-Exclude Data
- **Current Logic**: Monthly data requires ≥20 days; yearly requires full 12 months
- **Risk**: Stations with minor gaps (e.g., 19 days in February) excluded unnecessarily
- **Mitigation**: Track sensitivity: re-run with relaxed thresholds (≥15 days, ≥11 months); measure data loss
- **Validation**: Document in `PIPELINE_DESIGN_DOC.md` why 20/12 thresholds chosen; cite researcher requirements

### 4.5 Idempotency Edge Cases

#### Threat: Non-Deterministic Aggregation (Ties in "Best Hour")
- **Risk**: If two hours have equal day counts, selection may be random
- **Current Mitigation**: Code deterministically picks first hour alphabetically (implementation detail)
- **Validation**: Track B idempotency test catches this; also add explicit tie-breaking test

#### Threat: Pandas Version Differences
- **Risk**: pandas 3.x vs. 2.x may handle nulls/dtypes differently
- **Mitigation**: Pin pandas version in `pyproject.toml` (currently `>=3.0.0,<4.0.0`); CI tests on multiple Python versions
- **Validation**: Run Track A golden files on Python 3.12, 3.13, pandas 3.0, 3.1; ensure bit-identical outputs

---

## 5. Automation & CI Integration

### 5.1 Proposed CI Workflow Structure

```yaml
# .github/workflows/validation.yml
name: Pipeline Validation

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  track-a-golden-files:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run pytest tests/test_golden_files.py -v -m golden --tb=short

  track-b-invariants:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run pytest tests/test_invariants.py -v -m invariant --tb=short

  track-c-differential:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run pytest tests/test_differential.py -v -m differential --tb=short
      - uses: actions/upload-artifact@v3
        with:
          name: differential-reports
          path: docs/validation_artifacts/differential_reports/

  track-d-traceability:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run pytest tests/test_traceability_audit.py -v -m traceability --tb=short

  track-e-suspicious-coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run pytest tests/test_suspicious_audit.py -v -m suspicious --tb=short

  spec-coverage-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install poetry && poetry install
      - run: poetry run python tools/spec_coverage/generate_spec_coverage.py
      - uses: actions/upload-artifact@v3
        with:
          name: spec-coverage-csv
          path: spec_coverage.csv

  validation-summary:
    runs-on: ubuntu-latest
    needs: [track-a-golden-files, track-b-invariants, track-c-differential, track-d-traceability, track-e-suspicious-coverage]
    steps:
      - run: echo "✅ All validation tracks passed"
```

### 5.2 Local Development Workflow

```bash
# Run all validation tracks (pre-commit hook candidate)
poetry run pytest tests/ -v -m "golden or invariant or differential or traceability or suspicious"

# Run only fast tests (golden + invariants, ~30s)
poetry run pytest tests/ -v -m "golden or invariant"

# Full validation suite (includes audit steps, ~5min)
./scripts/run_full_validation.sh
```

### 5.3 Validation Artifacts Organization

```
docs/
  validation_artifacts/
    differential_reports/          # gitignored; CI artifacts
      regression_report_YYYYMMDD.csv
    invariant_logs/                # gitignored; failure logs only
      sentinel_leak_YYYYMMDD.log
    traceability/                  # committed
      audit_queue.csv
      audit_log.md
      evidence/
        52bade1af7.json
        82b0e05aae.json
    suspicious_coverage/           # committed
      suspicious_cases.csv
      audit_log.md
      resolution_tracker.csv

tests/
  fixtures/
    golden/                        # committed
      inputs/
        sentinel_edge_cases.csv
        scale_factors.csv
      expected/
        sentinel_edge_cases_expected_cleaned.parquet
      README.md
    samples/                       # committed; real station extracts
      station_01116099999.csv
      station_12930099999.csv
      README.md
    differential/                  # committed
      baselines/
        v0.9.0_station_01116099999_cleaned.parquet
      README.md
```

---

## 6. Versioning & Maintenance

### 6.1 Validation Plan Versioning

- This document follows semantic versioning: `MAJOR.MINOR` (e.g., `1.0`, `1.1`, `2.0`)
- **MAJOR** bump: Add/remove entire validation track or change acceptance criteria
- **MINOR** bump: Refine test implementation, update thresholds, fix typos
- Changes tracked via git history + changelog section at top of document

### 6.2 Validation Artifact Refresh Cadence

| Artifact | Refresh Trigger | Responsibility |
|----------|----------------|----------------|
| Golden file expected outputs | After cleaning logic change | Engineer + QA review |
| Differential baselines | Major release (e.g., v1.0 → v2.0) | Release manager |
| Spec coverage report | Every PR merge to main | Automated (CI) |
| Traceability audit queue | When `test_covered_strict` increases >5% | QA lead |
| Suspicious coverage audit log | Weekly during active development | Rotating engineer |

### 6.3 Failure Response Protocol

When any validation track fails:

1. **Triage** (within 1 business day):
   - Classify as: P0 (data corruption), P1 (regression), P2 (test flakiness), P3 (documentation drift)
   
2. **Root Cause Analysis** (P0: <4hrs, P1: <2 days):
   - Document in GitHub issue with label `validation-failure`
   - Link to CI run, relevant code, and suspected cause
   
3. **Resolution**:
   - P0: Immediate hotfix + rollback if in production
   - P1: Fix within sprint; regression test added
   - P2: Fix test; may indicate environment issue
   - P3: Update docs; no code change
   
4. **Post-Mortem** (for P0/P1):
   - Add case to golden files if it's a novel edge case
   - Update invariant tests if a new constraint discovered
   - Document in `docs/validation_artifacts/failure_log.md`

---

## 7. Acceptance Sign-Off

### 7.1 Validation Plan Approval

| Role | Name | Approval Date | Signature |
|------|------|---------------|-----------|
| Lead Engineer | _______________ | _______________ | _______________ |
| QA Lead | _______________ | _______________ | _______________ |
| Data Scientist (Researcher Rep) | _______________ | _______________ | _______________ |

### 7.2 v1.0 Release Sign-Off (Template)

_To be completed when all validation tracks pass:_

> On **[DATE]**, all validation tracks (A-E) passed with the following metrics:
> - `test_covered_strict`: **X%** (target: ≥95%)
> - Suspicious coverage cases: **X** (target: <1%)
> - Golden file pass rate: **100%**
> - Invariant violations: **0**
> - Differential drift: **<0.1%**
> - Traceability evidence: **100%**
> 
> The NOAA ISD cleaning pipeline is hereby declared **production-ready** for v1.0 release.
> 
> **Signed:**
> - Lead Engineer: _______________ (Date: _______)
> - QA Lead: _______________ (Date: _______)
> - Data Science Lead: _______________ (Date: _______)

---

## Appendix A: Quick Reference Commands

```bash
# ── Validation Execution ───────────────────────────────────────────────

# Run all validation tracks
poetry run pytest tests/ -v -m "golden or invariant or differential or traceability or suspicious"

# Run individual tracks
poetry run pytest tests/test_golden_files.py -v -m golden
poetry run pytest tests/test_invariants.py -v -m invariant
poetry run pytest tests/test_differential.py -v -m differential
poetry run pytest tests/test_traceability_audit.py -v -m traceability
poetry run pytest tests/test_suspicious_audit.py -v -m suspicious

# ── Artifact Generation ────────────────────────────────────────────────

# Regenerate spec coverage report
poetry run python tools/spec_coverage/generate_spec_coverage.py

# Generate audit queue for traceability
poetry run python tools/spec_coverage/sample_audit_rules.py

# Export suspicious coverage cases
poetry run python tools/spec_coverage/export_suspicious_cases.py

# Capture differential baseline
poetry run python tests/fixtures/differential/capture_baseline.py --commit-sha $(git rev-parse HEAD)

# ── Fixture Management ─────────────────────────────────────────────────

# Regenerate golden-file expected outputs (requires approval)
poetry run python tests/fixtures/golden/regenerate_expected.py --approve

# Add new sample station
poetry run python tests/fixtures/samples/download_station.py --station-id 01116099999 --years 2020-2023

# ── Reporting ──────────────────────────────────────────────────────────

# View latest differential report
cat docs/validation_artifacts/differential_reports/regression_report.csv

# Check traceability audit progress
grep "evidence_provided" docs/validation_artifacts/traceability/audit_queue.csv | wc -l

# Suspicious coverage resolution status
poetry run python tools/spec_coverage/report_suspicious_status.py
```

---

## Appendix B: Future Enhancements (Post-v1.0)

_Deferred validation improvements for v2.0+:_

1. **Property-Based Testing (Hypothesis)**:
   - Generate random valid ISD records; verify no crashes or sentinel leaks
   - Fuzz-test edge cases (max field widths, boundary values)

2. **Statistical Validation**:
   - Compare cleaned data distributions to NOAA's official QC reports
   - Detect anomalies (e.g., station suddenly reports 10x more nulls)

3. **Performance Regression Tests**:
   - Benchmark cleaning throughput (rows/sec)
   - Alert if >20% slowdown vs. baseline

4. **Cross-Pipeline Validation**:
   - Compare our outputs to legacy R scripts (where available)
   - Quantify differences; document intentional divergences

5. **User Acceptance Testing (UAT)**:
   - Provide sample cleaned datasets to 3+ researchers
   - Collect feedback on usability, missing fields, unexpected transformations

6. **Continuous Monitoring (Production)**:
   - Log sentinel-detection attempts; alert if frequency spikes
   - Track quality flag distribution over time; detect data source changes

---

**Document Version:** 1.0  
**Last Updated:** 2026-02-21  
**Next Review:** Upon completion of v1.0 validation checklist
