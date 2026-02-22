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


def _read_csv_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def _stable_sort_key(row: dict[str, str]) -> tuple[object, ...]:
    row_kind_rank = {"spec_rule": 0, "synthetic": 1}.get(row.get("row_kind", ""), 2)
    line_start = int(row["spec_line_start"]) if row.get("spec_line_start", "").isdigit() else 10**9
    line_end = int(row["spec_line_end"]) if row.get("spec_line_end", "").isdigit() else 10**9
    return (
        row_kind_rank,
        row.get("spec_file", ""),
        line_start,
        line_end,
        row.get("identifier", ""),
        row.get("rule_type", ""),
        row.get("rule_id", ""),
    )


def test_rule_ids_differ_by_line_range_and_are_not_merged() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    module = _load_generator_module(repo_root)

    row_a = module.SpecRuleRow(
        spec_part="99",
        spec_doc="part-99-fixture.md",
        spec_file="part-99-fixture.md",
        spec_line_start=10,
        spec_line_end=10,
        identifier="AB1",
        identifier_family="AB",
        rule_type="range",
        spec_rule_text="MIN 0 MAX 9",
        min_value="0",
        max_value="9",
    )
    row_b = module.SpecRuleRow(
        spec_part="99",
        spec_doc="part-99-fixture.md",
        spec_file="part-99-fixture.md",
        spec_line_start=20,
        spec_line_end=20,
        identifier="AB1",
        identifier_family="AB",
        rule_type="range",
        spec_rule_text="MIN 0 MAX 9",
        min_value="0",
        max_value="9",
    )

    rows = module.normalize_and_assign_rule_ids([row_a, row_b])
    assert rows[0].rule_id != rows[1].rule_id
    assert rows[0].rule_id.startswith("part-99-fixture.md:10-10::AB1::range::")
    assert rows[1].rule_id.startswith("part-99-fixture.md:20-20::AB1::range::")

    merged = module.merge_duplicate_rows(rows)
    assert len(merged) == 2, "Rows with identical payload but different line ranges must remain separate"


def test_spec_coverage_generator_smoke() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    module = _load_generator_module(repo_root)

    module.main()

    csv_path = repo_root / "spec_coverage.csv"
    report_path = repo_root / "SPEC_COVERAGE_REPORT.md"

    assert csv_path.exists(), "spec_coverage.csv should be generated"
    assert report_path.exists(), "SPEC_COVERAGE_REPORT.md should be generated"

    rows = _read_csv_rows(csv_path)

    assert len(rows) > 200, f"Expected >200 spec rows, got {len(rows)}"

    report_text = report_path.read_text(encoding="utf-8")
    assert "Overall coverage" in report_text
    assert "Enforcement layer breakdown" in report_text
    assert "Confidence breakdown" in report_text
    assert "Precision warnings" in report_text
    assert "Rule Identity & Provenance" in report_text
    assert "identical payloads at different ranges remain separate" in report_text

    metric_rows = [
        row
        for row in rows
        if row.get("row_kind") == "spec_rule" and row.get("rule_type") != "unknown"
    ]

    required_columns = {
        "rule_id",
        "row_kind",
        "spec_file",
        "spec_line_start",
        "spec_line_end",
        "spec_evidence",
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

    assert [row["rule_id"] for row in rows] == [row["rule_id"] for row in sorted(rows, key=_stable_sort_key)]

    synthetic_rows = [row for row in rows if row.get("row_kind") == "synthetic"]
    assert synthetic_rows, "Expected synthetic rows to be present"

    for row in rows:
        assert row["rule_id"], "rule_id must be populated"
        assert row["row_kind"] in {"spec_rule", "synthetic"}
        assert row["implemented_in_constants"] in {"TRUE", "FALSE"}
        assert row["implemented_in_cleaning"] in {"TRUE", "FALSE"}
        assert row["implementation_confidence"] in {"high", "medium", "low"}
        assert row["enforcement_layer"] in {"constants_only", "cleaning_only", "both", "neither"}
        if row["row_kind"] == "spec_rule":
            assert row["rule_id"].count("::") >= 3
            assert row["spec_file"] not in {"", "N/A"}
            assert row["spec_line_start"].isdigit()
            assert row["spec_line_end"].isdigit()
        else:
            assert row["rule_id"].startswith("synthetic::")
            assert row["spec_file"] == "N/A"
            assert row["spec_line_start"] == ""
            assert row["spec_line_end"] == ""
            assert row["spec_evidence"] == ""

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
        if row.get("row_kind") == "spec_rule"
        and row.get("rule_type") == "domain"
        and row.get("implementation_confidence") in {"high", "medium"}
        and "src/noaa_climate_data/cleaning.py:" in (row.get("cleaning_location") or "")
    ]
    assert known_cleaning_only, "Expected at least one spec-derived domain rule to be cleaning-only with medium/high confidence"

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

    total_match = re.search(r"Total spec rules extracted: \*\*(\d+)\*\*", report_text)
    assert total_match, "Expected total extracted rule count in report"
    report_total = int(total_match.group(1))
    expected_total = sum(1 for row in rows if row.get("row_kind") == "spec_rule")
    assert report_total == expected_total, "Synthetic rows must be excluded from total spec rule metrics"

    metric_match = re.search(r"Metric-eligible rules \(excluding `unknown`\): \*\*(\d+)\*\*", report_text)
    assert metric_match, "Expected metric-eligible count in report"
    report_metric_total = int(metric_match.group(1))
    expected_metric_total = sum(
        1 for row in rows if row.get("row_kind") == "spec_rule" and row.get("rule_type") != "unknown"
    )
    assert report_metric_total == expected_metric_total, "Synthetic rows must be excluded from metric denominator"

    first_run_rule_ids = [row["rule_id"] for row in rows]
    module.main()
    second_run_rule_ids = [row["rule_id"] for row in _read_csv_rows(csv_path)]
    assert first_run_rule_ids == second_run_rule_ids, "rule_id sequence should be stable across runs"
