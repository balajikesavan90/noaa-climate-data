"""Smoke test for spec coverage generator outputs."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path
import re
import sys


def _load_generator_module(repo_root: Path):
    script_path = repo_root / "tools" / "spec_coverage" / "generate_spec_coverage.py"
    spec = importlib.util.spec_from_file_location("spec_coverage_generator", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load generator module from {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_spec_coverage_generator_smoke() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    module = _load_generator_module(repo_root)

    module.main()

    csv_path = repo_root / "spec_coverage.csv"
    report_path = repo_root / "SPEC_COVERAGE_REPORT.md"

    assert csv_path.exists(), "spec_coverage.csv should be generated"
    assert report_path.exists(), "SPEC_COVERAGE_REPORT.md should be generated"

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    assert len(rows) > 200, f"Expected >200 spec rows, got {len(rows)}"

    report_text = report_path.read_text(encoding="utf-8")
    assert "Overall coverage" in report_text
    assert "Enforcement layer breakdown" in report_text
    assert "Confidence breakdown" in report_text
    assert "Precision warnings" in report_text

    metric_rows = [row for row in rows if row.get("rule_type") != "unknown"]

    required_columns = {
        "implemented_in_constants",
        "constants_location",
        "implemented_in_cleaning",
        "cleaning_location",
        "implementation_confidence",
        "enforcement_layer",
        "code_implemented",
    }
    missing_columns = required_columns - set(rows[0].keys())
    assert not missing_columns, f"Missing expected CSV columns: {sorted(missing_columns)}"

    for row in rows:
        assert row["implemented_in_constants"] in {"TRUE", "FALSE"}
        assert row["implemented_in_cleaning"] in {"TRUE", "FALSE"}
        assert row["implementation_confidence"] in {"high", "medium", "low"}
        assert row["enforcement_layer"] in {"constants_only", "cleaning_only", "both", "neither"}

        expected_implemented = (
            row["implemented_in_constants"] == "TRUE" or row["implemented_in_cleaning"] == "TRUE"
        )
        assert row["code_implemented"] == ("TRUE" if expected_implemented else "FALSE")

        if row["enforcement_layer"] == "constants_only":
            assert row["implemented_in_constants"] == "TRUE"
            assert row["implemented_in_cleaning"] == "FALSE"
        elif row["enforcement_layer"] == "cleaning_only":
            assert row["implemented_in_constants"] == "FALSE"
            assert row["implemented_in_cleaning"] == "TRUE"
        elif row["enforcement_layer"] == "both":
            assert row["implemented_in_constants"] == "TRUE"
            assert row["implemented_in_cleaning"] == "TRUE"
        else:
            assert row["implemented_in_constants"] == "FALSE"
            assert row["implemented_in_cleaning"] == "FALSE"

    range_rows = [row for row in metric_rows if row.get("rule_type") == "range"]
    assert range_rows, "Expected at least one range rule row"
    range_tested_count = sum(1 for row in range_rows if row.get("test_covered") == "TRUE")
    range_tested_pct = (100.0 * range_tested_count / len(range_rows)) if range_rows else 0.0
    assert range_tested_pct < 95.0, f"Range tested% too high ({range_tested_pct:.2f}%), likely overmatching"

    arity_rows = [row for row in metric_rows if row.get("rule_type") == "arity"]
    arity_tested_count = sum(1 for row in arity_rows if row.get("test_covered") == "TRUE")
    tests_cleaning_text = (repo_root / "tests" / "test_cleaning.py").read_text(encoding="utf-8")
    arity_tests_detected = bool(
        re.search(r"\barity\b", tests_cleaning_text, re.IGNORECASE)
        or re.search(r"truncated payload", tests_cleaning_text, re.IGNORECASE)
        or re.search(r"expected\s+\d+\s+parts", tests_cleaning_text, re.IGNORECASE)
    )
    if arity_tests_detected:
        assert arity_rows, "Arity tests detected in tests/test_cleaning.py but no arity rows were extracted"
        assert arity_tested_count > 0, "Arity tests are present but arity tested coverage is 0"
    else:
        assert (
            "Arity tests not detected; arity tested% may be 0." in report_text
        ), "Report should explicitly explain why arity tested% may be 0 when no arity tests are detected"

    cleaning_only_rows = [
        row
        for row in metric_rows
        if row.get("implemented_in_constants") == "FALSE"
        and row.get("implemented_in_cleaning") == "TRUE"
        and row.get("enforcement_layer") == "cleaning_only"
    ]
    assert cleaning_only_rows, "Expected at least one cleaning-only implemented rule"

    known_cleaning_only = [
        row
        for row in cleaning_only_rows
        if row.get("identifier") == "DATE"
        and row.get("rule_type") == "domain"
        and row.get("implementation_confidence") in {"high", "medium"}
        and "src/noaa_climate_data/cleaning.py:" in (row.get("cleaning_location") or "")
    ]
    assert known_cleaning_only, "Expected DATE domain rule to be detected as cleaning-only with medium/high confidence"

    neither_rows = [
        row
        for row in metric_rows
        if row.get("implemented_in_constants") == "FALSE"
        and row.get("implemented_in_cleaning") == "FALSE"
        and row.get("enforcement_layer") == "neither"
    ]
    assert neither_rows, "Expected at least one rule to remain unimplemented in both layers"

    implemented_rows = [row for row in metric_rows if row.get("code_implemented") == "TRUE"]
    cleaning_only_share = (len(cleaning_only_rows) / len(implemented_rows)) if implemented_rows else 0.0
    assert (
        cleaning_only_share <= 0.5
    ), f"Cleaning-only implementation share too high ({cleaning_only_share:.2%}); likely overmatching"

    expected_gap_rows = [
        row
        for row in rows
        if "expected_gap_from_alignment_report" in (row.get("notes", "") or "")
    ]

    uncovered_expected_gap_rows = [
        row
        for row in expected_gap_rows
        if row.get("code_implemented") == "FALSE" or row.get("test_covered") == "FALSE"
    ]

    assert (
        len(uncovered_expected_gap_rows) >= 3
    ), "Expected at least 3 known gaps to remain uncovered in code or tests"
