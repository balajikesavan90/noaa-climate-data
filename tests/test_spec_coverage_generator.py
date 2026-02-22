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
    assert "Precision warnings" in report_text

    metric_rows = [row for row in rows if row.get("rule_type") != "unknown"]

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
