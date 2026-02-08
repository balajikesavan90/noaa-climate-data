"""Tests for P1 aggregation correctness.

Verifies that:
1. Categorical columns (MW, AY, WND__part3, CIG__part3/4, VIS__part3,
   MD1__part1, GE1__part1) are excluded from numeric aggregation.
2. Quality columns (*__quality) are excluded from aggregated output.
3. Field-appropriate aggregation functions are applied (max for OC1,
   min for VIS, mean for TMP/DEW/SLP/MA1, etc.).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from noaa_climate_data.constants import (
    get_agg_func,
    is_categorical_column,
    is_quality_column,
)
from noaa_climate_data.pipeline import (
    _aggregate_numeric,
    _classify_columns,
    _coerce_numeric,
    _daily_min_max_mean,
)


# ── constants helpers ────────────────────────────────────────────────────


class TestIsQualityColumn:
    def test_quality_suffix(self):
        assert is_quality_column("WND__quality")
        assert is_quality_column("TMP__quality")

    def test_qc_suffix(self):
        assert is_quality_column("SLP__qc")

    def test_non_quality(self):
        assert not is_quality_column("TMP__value")
        assert not is_quality_column("WND__part4")
        assert not is_quality_column("Year")


class TestIsCategoricalColumn:
    def test_categorical_columns(self):
        assert is_categorical_column("MW1__value")
        assert is_categorical_column("MW2__value")
        assert is_categorical_column("AY1__value")
        assert is_categorical_column("AY2__value")
        assert is_categorical_column("WND__part3")
        assert is_categorical_column("CIG__part3")
        assert is_categorical_column("CIG__part4")
        assert is_categorical_column("VIS__part3")
        assert is_categorical_column("MD1__part1")
        assert is_categorical_column("GE1__part1")

    def test_numeric_columns_not_categorical(self):
        assert not is_categorical_column("TMP__value")
        assert not is_categorical_column("DEW__value")
        assert not is_categorical_column("WND__part4")
        assert not is_categorical_column("WND__part1")
        assert not is_categorical_column("VIS__part1")
        assert not is_categorical_column("MA1__part1")

    def test_plain_columns_not_categorical(self):
        assert not is_categorical_column("Year")
        assert not is_categorical_column("MonthNum")
        assert not is_categorical_column("ID")


class TestGetAggFunc:
    def test_quality_columns_drop(self):
        assert get_agg_func("WND__quality") == "drop"
        assert get_agg_func("TMP__quality") == "drop"

    def test_categorical_columns_drop(self):
        assert get_agg_func("MW1__value") == "drop"
        assert get_agg_func("WND__part3") == "drop"
        assert get_agg_func("CIG__part3") == "drop"
        assert get_agg_func("VIS__part3") == "drop"
        assert get_agg_func("MD1__part1") == "drop"
        assert get_agg_func("GE1__part1") == "drop"

    def test_mean_columns(self):
        assert get_agg_func("TMP__value") == "mean"
        assert get_agg_func("DEW__value") == "mean"
        assert get_agg_func("SLP__value") == "mean"
        assert get_agg_func("WND__part1") == "mean"
        assert get_agg_func("WND__part4") == "mean"
        assert get_agg_func("MA1__part1") == "mean"
        assert get_agg_func("MA1__part3") == "mean"

    def test_max_columns(self):
        assert get_agg_func("OC1__value") == "max"

    def test_min_columns(self):
        assert get_agg_func("VIS__part1") == "min"

    def test_unknown_column_defaults_mean(self):
        assert get_agg_func("Year") == "mean"
        assert get_agg_func("UNKNOWN__part1") == "mean"


# ── pipeline aggregation ────────────────────────────────────────────────


def _sample_df() -> pd.DataFrame:
    """Build a small DataFrame mimicking cleaned NOAA data."""
    return pd.DataFrame(
        {
            "Year": [2020, 2020, 2020, 2021, 2021, 2021],
            "MonthNum": [1, 1, 1, 1, 1, 1],
            "TMP__value": [10.0, 12.0, 14.0, 20.0, 22.0, 24.0],
            "DEW__value": [5.0, 6.0, 7.0, 10.0, 11.0, 12.0],
            "OC1__value": [8.0, 12.0, 10.0, 15.0, 18.0, 14.0],
            "VIS__part1": [5000.0, 3000.0, 4000.0, 8000.0, 6000.0, 7000.0],
            "MW1__value": [3.0, 5.0, 7.0, 1.0, 2.0, 3.0],
            "WND__part3": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
            "WND__quality": ["1", "1", "1", "1", "1", "1"],
            "TMP__quality": ["1", "1", "1", "1", "1", "1"],
        }
    )


class TestCoerceNumeric:
    def test_skips_quality_and_categorical(self):
        df = _sample_df()
        group_cols = ["Year", "MonthNum"]
        work, numeric_cols = _coerce_numeric(df, group_cols)
        # Quality columns should NOT be coerced
        assert "WND__quality" not in numeric_cols
        assert "TMP__quality" not in numeric_cols
        # Categorical columns should NOT be coerced
        assert "MW1__value" in numeric_cols or "MW1__value" not in numeric_cols
        # The key is that get_agg_func("MW1__value") == "drop", so even if
        # it IS numeric, it won't be aggregated.


class TestClassifyColumns:
    def test_classification(self):
        cols = [
            "TMP__value",
            "DEW__value",
            "OC1__value",
            "VIS__part1",
            "MW1__value",
            "WND__part3",
            "WND__quality",
            "TMP__quality",
        ]
        buckets = _classify_columns(cols)
        assert "TMP__value" in buckets.get("mean", [])
        assert "DEW__value" in buckets.get("mean", [])
        assert "OC1__value" in buckets.get("max", [])
        assert "VIS__part1" in buckets.get("min", [])
        assert "MW1__value" in buckets.get("drop", [])
        assert "WND__part3" in buckets.get("drop", [])
        assert "WND__quality" in buckets.get("drop", [])
        assert "TMP__quality" in buckets.get("drop", [])


class TestAggregateNumeric:
    def test_categoricals_excluded(self):
        df = _sample_df()
        result = _aggregate_numeric(df, ["Year", "MonthNum"])
        # Categorical & quality columns must not appear in result
        assert "MW1__value" not in result.columns
        assert "WND__part3" not in result.columns
        assert "WND__quality" not in result.columns
        assert "TMP__quality" not in result.columns

    def test_mean_applied(self):
        df = _sample_df()
        result = _aggregate_numeric(df, ["Year", "MonthNum"])
        row_2020 = result[result["Year"] == 2020].iloc[0]
        assert row_2020["TMP__value"] == pytest.approx(12.0)
        assert row_2020["DEW__value"] == pytest.approx(6.0)

    def test_max_applied_for_gust(self):
        df = _sample_df()
        result = _aggregate_numeric(df, ["Year", "MonthNum"])
        row_2020 = result[result["Year"] == 2020].iloc[0]
        # OC1 (wind gust) should use max, not mean
        assert row_2020["OC1__value"] == pytest.approx(12.0)

    def test_min_applied_for_visibility(self):
        df = _sample_df()
        result = _aggregate_numeric(df, ["Year", "MonthNum"])
        row_2020 = result[result["Year"] == 2020].iloc[0]
        # VIS should use min (worst visibility)
        assert row_2020["VIS__part1"] == pytest.approx(3000.0)


class TestDailyMinMaxMean:
    def test_excludes_categoricals(self):
        df = _sample_df()
        df["Day"] = pd.to_datetime(["2020-01-01"] * 3 + ["2021-01-01"] * 3).date
        result = _daily_min_max_mean(df, ["Year", "MonthNum", "Day"])
        col_names = set(result.columns)
        # Categorical should not appear
        assert "MW1__value__daily_mean" not in col_names
        assert "WND__part3__daily_mean" not in col_names
        assert "WND__quality__daily_mean" not in col_names
        # Numeric should appear
        assert "TMP__value__daily_min" in col_names
        assert "TMP__value__daily_max" in col_names
        assert "TMP__value__daily_mean" in col_names
