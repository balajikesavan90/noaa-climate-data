"""Reproducibility test for the sample cleaning pipeline."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_reproducibility_example_output_matches_expected() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "reproducibility" / "run_pipeline_example.py"
    output_path = repo_root / "reproducibility" / "sample_station_cleaned.csv"
    expected_path = repo_root / "reproducibility" / "sample_station_cleaned_expected.csv"

    subprocess.run([sys.executable, str(script_path)], check=True, cwd=repo_root)

    output_text = output_path.read_text(encoding="utf-8")
    expected_text = expected_path.read_text(encoding="utf-8")
    assert output_text == expected_text
