"""Tests for P0 — Data Correctness.

Covers the three P0 fixes:
1. Missing-value sentinels do not leak into numeric outputs.
2. Scale factors (÷10) are applied to all fields that need them.
3. Per-value quality-flag mapping nulls only the governed part.
"""

from __future__ import annotations

import pandas as pd
import pytest

from noaa_climate_data.cleaning import (
    _expand_parsed,
    _is_missing_value,
    _quality_for_part,
    clean_noaa_dataframe,
    clean_value_quality,
    parse_field,
)
from noaa_climate_data.constants import FieldPartRule, get_field_rule


# ── 1. Missing-value sentinels ───────────────────────────────────────────


class TestIsMissingValue:
    """_is_missing_value must recognise per-field sentinel patterns."""

    def test_tmp_sentinel_9999(self):
        rule = get_field_rule("TMP").parts[1]
        assert _is_missing_value("+9999", rule)
        assert _is_missing_value("9999", rule)

    def test_tmp_real_value(self):
        rule = get_field_rule("TMP").parts[1]
        assert not _is_missing_value("+0250", rule)
        assert not _is_missing_value("-0032", rule)

    def test_wnd_direction_sentinel_999(self):
        rule = get_field_rule("WND").parts[1]
        assert _is_missing_value("999", rule)

    def test_wnd_speed_sentinel_9999(self):
        rule = get_field_rule("WND").parts[4]
        assert _is_missing_value("9999", rule)

    def test_vis_sentinel_999999(self):
        rule = get_field_rule("VIS").parts[1]
        assert _is_missing_value("999999", rule)

    def test_vis_secondary_sentinel_9999(self):
        rule = get_field_rule("VIS").parts[1]
        assert _is_missing_value("9999", rule)
        # Ensure leading-zero forms are also detected
        assert _is_missing_value("009999", rule)

    def test_slp_sentinel_99999(self):
        rule = get_field_rule("SLP").parts[1]
        assert _is_missing_value("99999", rule)

    def test_cig_sentinel_99999(self):
        rule = get_field_rule("CIG").parts[1]
        assert _is_missing_value("99999", rule)

    def test_fallback_generic_when_no_rule(self):
        # Without a rule, the generic all-9s heuristic applies.
        assert _is_missing_value("9999", None)
        assert _is_missing_value("99999", None)
        assert not _is_missing_value("1234", None)

    def test_sentinel_does_not_match_real_value(self):
        """A 3-digit value of 999 is missing for WND direction but 123 is not."""
        rule = get_field_rule("WND").parts[1]
        assert not _is_missing_value("123", rule)


class TestSentinelsInCleanedOutput:
    """Sentinels must become None/NaN, never appear as numeric values."""

    def test_tmp_sentinel_becomes_none(self):
        result = clean_value_quality("+9999,1", "TMP")
        assert result["TMP__value"] is None

    def test_slp_sentinel_becomes_none(self):
        result = clean_value_quality("99999,1", "SLP")
        assert result["SLP__value"] is None

    def test_wnd_sentinels_become_none(self):
        # direction=999, type=N, speed=9999
        result = clean_value_quality("999,1,N,9999,1", "WND")
        assert result["WND__part1"] is None
        assert result["WND__part4"] is None

    def test_vis_sentinel_becomes_none(self):
        result = clean_value_quality("999999,1,N,1", "VIS")
        assert result["VIS__part1"] is None

    def test_vis_secondary_sentinel_9999_becomes_none(self):
        """VIS=9999 is a secondary sentinel (distance=9999 with variability=9)."""
        result = clean_value_quality("009999,5,N,1", "VIS")
        assert result["VIS__part1"] is None

    def test_clean_dataframe_no_leaked_sentinels(self):
        """End-to-end: cleaning a DataFrame must not leave sentinel numbers."""
        df = pd.DataFrame(
            {
                "TMP": ["+0250,1", "+9999,1", "-0032,1"],
                "SLP": ["10132,1", "99999,1", "10089,1"],
                "WND": [
                    "180,1,N,0050,1",
                    "999,1,N,9999,1",
                    "270,1,N,0030,1",
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        # Row 1 (index 1) should have NaN for all value columns.
        assert pd.isna(cleaned.loc[1, "TMP__value"])
        assert pd.isna(cleaned.loc[1, "SLP__value"])
        assert pd.isna(cleaned.loc[1, "WND__part1"])
        assert pd.isna(cleaned.loc[1, "WND__part4"])
        # Rows 0 and 2 should have real numeric values.
        assert cleaned.loc[0, "TMP__value"] == pytest.approx(25.0)
        assert cleaned.loc[2, "TMP__value"] == pytest.approx(-3.2)


# ── 2. Scale factors (÷10) ──────────────────────────────────────────────


class TestScaleFactors:
    """Fields with scale=0.1 must divide by 10 in cleaned output."""

    def test_tmp_scaled(self):
        result = clean_value_quality("+0250,1", "TMP")
        assert result["TMP__value"] == pytest.approx(25.0)

    def test_dew_scaled(self):
        result = clean_value_quality("+0120,1", "DEW")
        assert result["DEW__value"] == pytest.approx(12.0)

    def test_slp_scaled(self):
        result = clean_value_quality("10132,1", "SLP")
        assert result["SLP__value"] == pytest.approx(1013.2)

    def test_oc1_gust_scaled(self):
        result = clean_value_quality("0085,1", "OC1")
        assert result["OC1__value"] == pytest.approx(8.5)

    def test_wnd_speed_scaled(self):
        result = clean_value_quality("180,1,N,0050,1", "WND")
        assert result["WND__part4"] == pytest.approx(5.0)

    def test_wnd_direction_not_scaled(self):
        result = clean_value_quality("180,1,N,0050,1", "WND")
        assert result["WND__part1"] == pytest.approx(180.0)

    def test_ma1_altimeter_and_station_pressure_scaled(self):
        result = clean_value_quality("10132,1,09876,1", "MA1")
        assert result["MA1__part1"] == pytest.approx(1013.2)
        assert result["MA1__part3"] == pytest.approx(987.6)

    def test_sa1_sst_scaled(self):
        result = clean_value_quality("0215,1", "SA1")
        assert result["SA1__value"] == pytest.approx(21.5)

    def test_md1_pressure_change_scaled(self):
        result = clean_value_quality("5,1,045,1,0123,1", "MD1")
        assert result["MD1__part3"] == pytest.approx(4.5)
        assert result["MD1__part5"] == pytest.approx(12.3)

    def test_negative_temperature_scaled(self):
        result = clean_value_quality("-0032,1", "TMP")
        assert result["TMP__value"] == pytest.approx(-3.2)


class TestScaleFactorsInDataframe:
    """Scale factors work end-to-end through clean_noaa_dataframe."""

    def test_dataframe_tmp_scaled(self):
        df = pd.DataFrame({"TMP": ["+0250,1", "-0100,1"]})
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "TMP__value"] == pytest.approx(25.0)
        assert cleaned.loc[1, "TMP__value"] == pytest.approx(-10.0)

    def test_dataframe_wnd_speed_scaled(self):
        df = pd.DataFrame({"WND": ["090,1,N,0110,1", "270,1,N,0030,1"]})
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "WND__part4"] == pytest.approx(11.0)
        assert cleaned.loc[1, "WND__part4"] == pytest.approx(3.0)


# ── 3. Per-value quality-flag mapping ────────────────────────────────────


class TestQualityForPart:
    """_quality_for_part must return the correct quality flag for each part."""

    def test_wnd_direction_quality_is_part2(self):
        parts = ["180", "1", "N", "0050", "1"]
        assert _quality_for_part("WND", 1, parts) == "1"

    def test_wnd_speed_quality_is_part5(self):
        parts = ["180", "1", "N", "0050", "1"]
        assert _quality_for_part("WND", 4, parts) == "1"

    def test_wnd_direction_bad_quality_does_not_affect_speed(self):
        parts = ["180", "3", "N", "0050", "1"]  # part2=3 → bad for direction
        assert _quality_for_part("WND", 1, parts) == "3"  # direction gets bad flag
        assert _quality_for_part("WND", 4, parts) == "1"  # speed keeps good flag

    def test_ma1_separate_quality_parts(self):
        parts = ["10132", "1", "09876", "1"]
        assert _quality_for_part("MA1", 1, parts) == "1"  # altimeter → part2
        assert _quality_for_part("MA1", 3, parts) == "1"  # station press → part4

    def test_ma1_bad_stn_press_quality_only(self):
        parts = ["10132", "1", "09876", "3"]  # part4=3 → bad for station press
        assert _quality_for_part("MA1", 1, parts) == "1"  # altimeter still good
        assert _quality_for_part("MA1", 3, parts) == "3"  # station press bad

    def test_no_rule_returns_none(self):
        assert _quality_for_part("UNKNOWN", 1, ["x", "y"]) is None


class TestQualityNullsCorrectPart:
    """Bad quality must null only the governed value, not siblings."""

    def test_wnd_bad_direction_quality_nulls_direction_only(self):
        # part2=3 (bad quality for direction), part5=1 (good for speed)
        result = clean_value_quality("180,3,N,0050,1", "WND")
        assert result["WND__part1"] is None         # direction nulled
        assert result["WND__part4"] == pytest.approx(5.0)  # speed preserved

    def test_wnd_bad_speed_quality_nulls_speed_only(self):
        # part2=1 (good for direction), part5=3 (bad for speed)
        result = clean_value_quality("180,1,N,0050,3", "WND")
        assert result["WND__part1"] == pytest.approx(180.0)  # direction preserved
        assert result["WND__part4"] is None          # speed nulled

    def test_wnd_both_bad_nulls_both(self):
        result = clean_value_quality("180,3,N,0050,3", "WND")
        assert result["WND__part1"] is None
        assert result["WND__part4"] is None

    def test_ma1_bad_station_pressure_preserves_altimeter(self):
        result = clean_value_quality("10132,1,09876,3", "MA1")
        assert result["MA1__part1"] == pytest.approx(1013.2)  # altimeter preserved
        assert result["MA1__part3"] is None  # station pressure nulled

    def test_ma1_bad_altimeter_preserves_station_pressure(self):
        result = clean_value_quality("10132,3,09876,1", "MA1")
        assert result["MA1__part1"] is None  # altimeter nulled
        assert result["MA1__part3"] == pytest.approx(987.6)  # station pressure preserved

    def test_tmp_bad_quality_nulls_value(self):
        result = clean_value_quality("+0250,3", "TMP")
        assert result["TMP__value"] is None

    def test_tmp_good_quality_keeps_value(self):
        result = clean_value_quality("+0250,1", "TMP")
        assert result["TMP__value"] == pytest.approx(25.0)

    def test_quality_in_dataframe(self):
        df = pd.DataFrame(
            {
                "WND": [
                    "180,1,N,0050,1",   # both good
                    "180,3,N,0050,1",   # bad direction
                    "180,1,N,0050,3",   # bad speed
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        # Row 0: both values present
        assert cleaned.loc[0, "WND__part1"] == pytest.approx(180.0)
        assert cleaned.loc[0, "WND__part4"] == pytest.approx(5.0)
        # Row 1: direction nulled, speed kept
        assert pd.isna(cleaned.loc[1, "WND__part1"])
        assert cleaned.loc[1, "WND__part4"] == pytest.approx(5.0)
        # Row 2: direction kept, speed nulled
        assert cleaned.loc[2, "WND__part1"] == pytest.approx(180.0)
        assert pd.isna(cleaned.loc[2, "WND__part4"])
