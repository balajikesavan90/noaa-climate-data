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

    def test_tmp_negative_all_9_not_missing(self):
        rule = get_field_rule("TMP").parts[1]
        assert not _is_missing_value("-9999", rule)

    def test_wnd_direction_sentinel_999(self):
        rule = get_field_rule("WND").parts[1]
        assert _is_missing_value("999", rule)

    def test_wnd_speed_sentinel_9999(self):
        rule = get_field_rule("WND").parts[4]
        assert _is_missing_value("9999", rule)

    def test_vis_sentinel_999999(self):
        rule = get_field_rule("VIS").parts[1]
        assert _is_missing_value("999999", rule)

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

    def test_fallback_negative_all_9_not_missing(self):
        assert not _is_missing_value("-9999", None)

    def test_sentinel_does_not_match_real_value(self):
        """A 3-digit value of 999 is missing for WND direction but 123 is not."""
        rule = get_field_rule("WND").parts[1]
        assert not _is_missing_value("123", rule)

    def test_ge1_convective_cloud_missing(self):
        rule = get_field_rule("GE1").parts[1]
        assert _is_missing_value("9", rule)

    def test_ge1_vertical_datum_missing(self):
        rule = get_field_rule("GE1").parts[2]
        assert _is_missing_value("999999", rule)


class TestPrefixRuleMapping:
    """Numeric suffixes should resolve to prefix-based field rules."""

    @pytest.mark.parametrize(
        ("prefix", "expected_code"),
        [
            ("OA1", "OA*"),
            ("OD2", "OD*"),
            ("OB1", "OB*"),
            ("OE3", "OE*"),
            ("RH2", "RH*"),
            ("MV1", "MV*"),
            ("MW2", "MW*"),
            ("AY1", "AY*"),
            ("CO2", "CO*"),
            ("CT3", "CT*"),
            ("CU2", "CU*"),
            ("CV1", "CV*"),
            ("CW1", "CW*"),
            ("CX3", "CX*"),
        ],
    )
    def test_numeric_suffixes_use_prefix_rules(self, prefix: str, expected_code: str):
        rule = get_field_rule(prefix)
        assert rule is not None
        assert rule.code == expected_code


class TestSentinelsInCleanedOutput:
    """Sentinels must become None/NaN, never appear as numeric values."""

    def test_tmp_sentinel_becomes_none(self):
        result = clean_value_quality("+9999,1", "TMP")
        assert result["TMP__value"] is None

    def test_tmp_negative_all_9_kept(self):
        result = clean_value_quality("-9999,1", "TMP")
        assert result["TMP__value"] == pytest.approx(-999.9)

    def test_slp_sentinel_becomes_none(self):
        result = clean_value_quality("99999,1", "SLP")
        assert result["SLP__value"] is None

    def test_slp_quality_rejects_alpha_codes(self):
        result = clean_value_quality("10132,A", "SLP")
        assert result["SLP__value"] is None

    def test_wnd_sentinels_become_none(self):
        # direction=999, type=N, speed=9999
        result = clean_value_quality("999,1,N,9999,1", "WND")
        assert result["WND__part1"] is None
        assert result["WND__part4"] is None

    def test_vis_sentinel_becomes_none(self):
        result = clean_value_quality("999999,1,N,1", "VIS")
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
        assert pd.isna(cleaned.loc[1, "temperature_c"])
        assert pd.isna(cleaned.loc[1, "sea_level_pressure_hpa"])
        assert pd.isna(cleaned.loc[1, "wind_direction_deg"])
        assert pd.isna(cleaned.loc[1, "wind_speed_ms"])
        # Rows 0 and 2 should have real numeric values.
        assert cleaned.loc[0, "temperature_c"] == pytest.approx(25.0)
        assert cleaned.loc[2, "temperature_c"] == pytest.approx(-3.2)

    def test_wnd_variable_direction_sets_flag(self):
        result = clean_value_quality("999,1,V,0050,1", "WND")
        assert result["WND__direction_variable"] is True
        assert result["WND__part1"] is None
        assert result["WND__part4"] == pytest.approx(5.0)

    def test_ge1_missing_parts(self):
        result = clean_value_quality("9,999999,99999,99999", "GE1")
        assert result["GE1__part1"] is None
        assert result["GE1__part2"] is None

    def test_ge1_invalid_convective_cloud_code(self):
        result = clean_value_quality("8,AGL,99999,99999", "GE1")
        assert result["GE1__part1"] is None
        assert result["GE1__part2"] == "AGL"

    def test_ge1_invalid_vertical_datum_code(self):
        result = clean_value_quality("1,BADXXX,99999,99999", "GE1")
        assert result["GE1__part1"] == pytest.approx(1.0)
        assert result["GE1__part2"] is None

    def test_hail_sentinel_becomes_none(self):
        result = clean_value_quality("999,1", "HAIL")
        assert result["HAIL__value"] is None

    def test_ia1_missing_observation_code(self):
        result = clean_value_quality("99,1", "IA1")
        assert result["IA1__part1"] is None

    def test_ia1_valid_observation_code(self):
        result = clean_value_quality("00,1", "IA1")
        assert result["IA1__part1"] == pytest.approx(0.0)
        result = clean_value_quality("31,1", "IA1")
        assert result["IA1__part1"] == pytest.approx(31.0)

    def test_ia1_invalid_observation_code(self):
        result = clean_value_quality("32,1", "IA1")
        assert result["IA1__part1"] is None

    def test_ia2_missing_min_temp_parts(self):
        result = clean_value_quality("999,+9999,1", "IA2")
        assert result["IA2__part1"] is None
        assert result["IA2__part2"] is None

    def test_ka_invalid_extreme_code(self):
        result = clean_value_quality("005,X,0123,1", "KA1")
        assert result["KA1__part2"] is None
        assert result["KA1__part3"] == pytest.approx(12.3)

    def test_ka_quality_allows_m(self):
        result = clean_value_quality("005,N,0123,M", "KA1")
        assert result["KA1__part1"] == pytest.approx(0.5)
        assert result["KA1__part2"] == "N"
        assert result["KA1__part3"] == pytest.approx(12.3)

    def test_kb_missing_parts(self):
        result = clean_value_quality("999,9,+9999,1", "KB1")
        assert result["KB1__part1"] is None
        assert result["KB1__part2"] is None
        assert result["KB1__part3"] is None

    def test_kc_missing_parts(self):
        result = clean_value_quality("9,9,+9999,999999,1", "KC1")
        assert result["KC1__part1"] is None
        assert result["KC1__part2"] is None
        assert result["KC1__part3"] is None
        assert result["KC1__part4"] is None

    def test_kd_missing_parts(self):
        result = clean_value_quality("999,9,9999,1", "KD1")
        assert result["KD1__part1"] is None
        assert result["KD1__part2"] is None
        assert result["KD1__part3"] is None

    def test_ke_missing_parts(self):
        result = clean_value_quality("99,1,99,1,99,1,99,1", "KE1")
        assert result["KE1__part1"] is None
        assert result["KE1__part3"] is None
        assert result["KE1__part5"] is None
        assert result["KE1__part7"] is None

    def test_kf_missing_parts(self):
        result = clean_value_quality("9999,1", "KF1")
        assert result["KF1__part1"] is None

    def test_kg_missing_parts(self):
        result = clean_value_quality("999,9,+9999,9,1", "KG1")
        assert result["KG1__part1"] is None
        assert result["KG1__part2"] is None
        assert result["KG1__part3"] is None
        assert result["KG1__part4"] is None

    def test_st1_missing_parts(self):
        result = clean_value_quality("9,+9999,4,9999,4,99,4,9,4", "ST1")
        assert result["ST1__part1"] is None
        assert result["ST1__part2"] is None
        assert result["ST1__part4"] is None
        assert result["ST1__part6"] is None
        assert result["ST1__part8"] is None

    def test_me1_missing_parts(self):
        result = clean_value_quality("9,9999,1", "ME1")
        assert result["ME1__part1"] is None
        assert result["ME1__part2"] is None

    def test_me1_invalid_code(self):
        result = clean_value_quality("6,0123,1", "ME1")
        assert result["ME1__part1"] is None
        assert result["ME1__part2"] == pytest.approx(123.0)

    def test_mf1_missing_parts(self):
        result = clean_value_quality("99999,1,99999,1", "MF1")
        assert result["MF1__part1"] is None
        assert result["MF1__part3"] is None

    def test_mk1_missing_parts(self):
        result = clean_value_quality("99999,999999,1,99999,999999,1", "MK1")
        assert result["MK1__part1"] is None
        assert result["MK1__part2"] is None
        assert result["MK1__part4"] is None
        assert result["MK1__part5"] is None

    def test_rh1_missing_parts(self):
        result = clean_value_quality("999,9,999,9,9", "RH1")
        assert result["RH1__part1"] is None
        assert result["RH1__part2"] is None
        assert result["RH1__part3"] is None
        assert result["RH1__part4"] is None

    def test_rh1_valid_values(self):
        result = clean_value_quality("024,M,085,D,1", "RH1")
        assert result["RH1__part1"] == pytest.approx(24.0)
        assert result["RH1__part2"] == "M"
        assert result["RH1__part3"] == pytest.approx(85.0)
        assert result["RH1__part4"] == "D"
        assert result["RH1__quality"] == "1"

    def test_ob1_missing_parts(self):
        result = clean_value_quality(
            "999,9999,9,9,999,9,9,99999,9,9,99999,9,9",
            "OB1",
        )
        assert result["OB1__part1"] is None
        assert result["OB1__part2"] is None
        assert result["OB1__part5"] is None
        assert result["OB1__part8"] is None
        assert result["OB1__part11"] is None

    def test_oe1_missing_parts(self):
        result = clean_value_quality("9,99,99999,999,9999,9", "OE1")
        assert result["OE1__part1"] is None
        assert result["OE1__part2"] is None
        assert result["OE1__part3"] is None
        assert result["OE1__part4"] is None
        assert result["OE1__part5"] is None

    def test_oe1_requires_24_hour_period(self):
        result = clean_value_quality("1,12,00010,180,1200,4", "OE1")
        assert result["OE1__part2"] is None
        assert result["OE1__part3"] == pytest.approx(0.1)

    def test_oe1_speed_range_enforced(self):
        result = clean_value_quality("1,24,20001,180,1200,4", "OE1")
        assert result["OE1__part3"] is None

    def test_oe1_direction_range_enforced(self):
        result = clean_value_quality("1,24,00010,361,1200,4", "OE1")
        assert result["OE1__part4"] is None

    def test_oe1_occurrence_time_range_enforced(self):
        result = clean_value_quality("1,24,00010,180,2360,4", "OE1")
        assert result["OE1__part5"] is None

    def test_wa1_missing_parts(self):
        result = clean_value_quality("9,999,9,9", "WA1")
        assert result["WA1__part1"] is None
        assert result["WA1__part2"] is None
        assert result["WA1__part3"] is None

    def test_wa1_invalid_thickness(self):
        result = clean_value_quality("1,999,1,1", "WA1")
        assert result["WA1__part2"] is None

    def test_wd1_missing_parts(self):
        result = clean_value_quality("99,999,99,9,9,9,99,9,999,999,9", "WD1")
        assert result["WD1__part1"] is None
        assert result["WD1__part2"] is None
        assert result["WD1__part3"] is None
        assert result["WD1__part4"] is None
        assert result["WD1__part5"] is None
        assert result["WD1__part6"] is None
        assert result["WD1__part7"] is None
        assert result["WD1__part8"] is None
        assert result["WD1__part9"] is None
        assert result["WD1__part10"] is None

    def test_wd1_invalid_edge_bearing_code(self):
        result = clean_value_quality("11,050,06,1,1,1,00,1,050,010,1", "WD1")
        assert result["WD1__part1"] is None

    def test_wd1_invalid_concentration_rate(self):
        result = clean_value_quality("01,101,06,1,1,1,00,1,050,010,1", "WD1")
        assert result["WD1__part2"] is None

    def test_wd1_invalid_non_uniform_code(self):
        result = clean_value_quality("01,050,05,1,1,1,00,1,050,010,1", "WD1")
        assert result["WD1__part3"] is None

    def test_wd1_invalid_ship_position_code(self):
        result = clean_value_quality("01,050,06,3,1,1,00,1,050,010,1", "WD1")
        assert result["WD1__part4"] is None

    def test_wd1_invalid_penetrability_code(self):
        result = clean_value_quality("01,050,06,1,0,1,00,1,050,010,1", "WD1")
        assert result["WD1__part5"] is None

    def test_wd1_invalid_ice_trend_code(self):
        result = clean_value_quality("01,050,06,1,1,0,00,1,050,010,1", "WD1")
        assert result["WD1__part6"] is None

    def test_wd1_invalid_development_code(self):
        result = clean_value_quality("01,050,06,1,1,1,10,1,050,010,1", "WD1")
        assert result["WD1__part7"] is None

    def test_wd1_invalid_growler_presence_code(self):
        result = clean_value_quality("01,050,06,1,1,1,00,3,050,010,1", "WD1")
        assert result["WD1__part8"] is None

    def test_wd1_invalid_growler_quantity(self):
        result = clean_value_quality("01,050,06,1,1,1,00,1,999,010,1", "WD1")
        assert result["WD1__part9"] is None

    def test_wd1_invalid_iceberg_quantity(self):
        result = clean_value_quality("01,050,06,1,1,1,00,1,050,999,1", "WD1")
        assert result["WD1__part10"] is None

    def test_wg1_missing_parts(self):
        result = clean_value_quality("99,99,99,99,99,9", "WG1")
        assert result["WG1__part1"] is None
        assert result["WG1__part2"] is None
        assert result["WG1__part3"] is None
        assert result["WG1__part4"] is None
        assert result["WG1__part5"] is None

    def test_wg1_invalid_edge_bearing_code(self):
        result = clean_value_quality("11,10,01,01,01,1", "WG1")
        assert result["WG1__part1"] is None

    def test_wg1_invalid_edge_distance(self):
        result = clean_value_quality("01,99,01,01,01,1", "WG1")
        assert result["WG1__part2"] is None

    def test_wg1_invalid_edge_orientation_code(self):
        result = clean_value_quality("01,10,10,01,01,1", "WG1")
        assert result["WG1__part3"] is None

    def test_wg1_invalid_formation_type_code(self):
        result = clean_value_quality("01,10,01,10,01,1", "WG1")
        assert result["WG1__part4"] is None

    def test_wg1_invalid_navigation_effect_code(self):
        result = clean_value_quality("01,10,01,01,10,1", "WG1")
        assert result["WG1__part5"] is None

    def test_wj1_missing_parts(self):
        result = clean_value_quality("999,99999,99,99,9999,9,9", "WJ1")
        assert result["WJ1__part1"] is None
        assert result["WJ1__part2"] is None
        assert result["WJ1__part3"] is None
        assert result["WJ1__part4"] is None
        assert result["WJ1__part5"] is None
        assert result["WJ1__part6"] is None
        assert result["WJ1__part7"] is None

    def test_wj1_invalid_primary_ice_code(self):
        result = clean_value_quality("010,01000,74,00,0100,1,B", "WJ1")
        assert result["WJ1__part3"] is None

    def test_wj1_invalid_secondary_ice_code(self):
        result = clean_value_quality("010,01000,00,74,0100,1,B", "WJ1")
        assert result["WJ1__part4"] is None

    def test_wj1_invalid_slush_condition(self):
        result = clean_value_quality("010,01000,00,00,0100,4,B", "WJ1")
        assert result["WJ1__part6"] is None

    def test_wj1_invalid_ice_thickness(self):
        result = clean_value_quality("1000,01000,00,00,0100,1,B", "WJ1")
        assert result["WJ1__part1"] is None

    def test_wj1_invalid_discharge_rate(self):
        result = clean_value_quality("010,100000,00,00,0100,1,B", "WJ1")
        assert result["WJ1__part2"] is None

    def test_wj1_invalid_stage_height(self):
        result = clean_value_quality("010,01000,00,00,10000,1,B", "WJ1")
        assert result["WJ1__part5"] is None


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

    def test_hail_scaled(self):
        result = clean_value_quality("025,1", "HAIL")
        assert result["HAIL__value"] == pytest.approx(2.5)

    def test_ic1_evaporation_scaled(self):
        result = clean_value_quality("24,0100,1,4,050,1,4,+050,1,4,+040,1,4", "IC1")
        assert result["IC1__part5"] == pytest.approx(0.5)

    def test_kb_scaled(self):
        result = clean_value_quality("024,A,0100,1", "KB1")
        assert result["KB1__part3"] == pytest.approx(1.0)

    def test_kc_scaled(self):
        result = clean_value_quality("M,1,0123,010203,1", "KC1")
        assert result["KC1__part3"] == pytest.approx(12.3)

    def test_kf_scaled(self):
        result = clean_value_quality("0123,1", "KF1")
        assert result["KF1__part1"] == pytest.approx(12.3)

    def test_kg_scaled(self):
        result = clean_value_quality("024,D,0123,D,1", "KG1")
        assert result["KG1__part3"] == pytest.approx(12.3)

    def test_st1_scaled(self):
        result = clean_value_quality("1,0123,4,0050,4,01,4,2,4", "ST1")
        assert result["ST1__part2"] == pytest.approx(12.3)
        assert result["ST1__part4"] == pytest.approx(5.0)

    def test_mf1_scaled(self):
        result = clean_value_quality("10132,1,09876,1", "MF1")
        assert result["MF1__part1"] == pytest.approx(1013.2)
        assert result["MF1__part3"] == pytest.approx(987.6)


class TestScaleFactorsInDataframe:
    """Scale factors work end-to-end through clean_noaa_dataframe."""

    def test_dataframe_tmp_scaled(self):
        df = pd.DataFrame({"TMP": ["+0250,1", "-0100,1"]})
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "temperature_c"] == pytest.approx(25.0)
        assert cleaned.loc[1, "temperature_c"] == pytest.approx(-10.0)

    def test_dataframe_wnd_speed_scaled(self):
        df = pd.DataFrame({"WND": ["090,1,N,0110,1", "270,1,N,0030,1"]})
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "wind_speed_ms"] == pytest.approx(11.0)
        assert cleaned.loc[1, "wind_speed_ms"] == pytest.approx(3.0)

    def test_dataframe_hail_renamed(self):
        df = pd.DataFrame({"HAIL": ["025,1", "999,9"]})
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert "hail_size_cm" in cleaned.columns
        assert cleaned.loc[0, "hail_size_cm"] == pytest.approx(2.5)
        assert pd.isna(cleaned.loc[1, "hail_size_cm"])


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
        parts = ["180", "8", "N", "0050", "1"]  # part2=8 → bad for direction
        assert _quality_for_part("WND", 1, parts) == "8"  # direction gets bad flag
        assert _quality_for_part("WND", 4, parts) == "1"  # speed keeps good flag

    def test_ma1_separate_quality_parts(self):
        parts = ["10132", "1", "09876", "1"]
        assert _quality_for_part("MA1", 1, parts) == "1"  # altimeter → part2
        assert _quality_for_part("MA1", 3, parts) == "1"  # station press → part4

    def test_ma1_bad_stn_press_quality_only(self):
        parts = ["10132", "1", "09876", "3"]  # part4=3 → bad for station press
        assert _quality_for_part("MA1", 1, parts) == "1"  # altimeter still good
        assert _quality_for_part("MA1", 3, parts) == "3"  # station press bad

    def test_ua1_wave_parts_use_part4_quality(self):
        parts = ["I", "05", "120", "1", "03", "9"]
        assert _quality_for_part("UA1", 2, parts) == "1"
        assert _quality_for_part("UA1", 3, parts) == "1"

    def test_ua1_sea_state_quality_is_part6(self):
        parts = ["I", "05", "120", "1", "03", "9"]
        assert _quality_for_part("UA1", 5, parts) == "9"

    def test_no_rule_returns_none(self):
        assert _quality_for_part("UNKNOWN", 1, ["x", "y"]) is None


class TestQualityNullsCorrectPart:
    """Bad quality must null only the governed value, not siblings."""

    def test_wnd_bad_direction_quality_nulls_direction_only(self):
        # part2=8 (bad quality for direction), part5=1 (good for speed)
        result = clean_value_quality("180,8,N,0050,1", "WND")
        assert result["WND__part1"] is None         # direction nulled
        assert result["WND__part4"] == pytest.approx(5.0)  # speed preserved

    def test_wnd_bad_speed_quality_nulls_speed_only(self):
        # part2=1 (good for direction), part5=8 (bad for speed)
        result = clean_value_quality("180,1,N,0050,8", "WND")
        assert result["WND__part1"] == pytest.approx(180.0)  # direction preserved
        assert result["WND__part4"] is None          # speed nulled

    def test_wnd_rejects_non_mandatory_quality(self):
        result = clean_value_quality("180,M,N,0050,1", "WND")
        assert result["WND__part1"] is None
        assert result["WND__part4"] == pytest.approx(5.0)

    def test_wnd_both_bad_nulls_both(self):
        result = clean_value_quality("180,8,N,0050,8", "WND")
        assert result["WND__part1"] is None
        assert result["WND__part4"] is None

    def test_cig_rejects_non_mandatory_quality(self):
        result = clean_value_quality("01000,M,9,9", "CIG")
        assert result["CIG__part1"] is None

    def test_vis_rejects_non_mandatory_quality(self):
        result = clean_value_quality("010000,M,N,1", "VIS")
        assert result["VIS__part1"] is None

    def test_ma1_bad_station_pressure_preserves_altimeter(self):
        result = clean_value_quality("10132,1,09876,8", "MA1")
        assert result["MA1__part1"] == pytest.approx(1013.2)  # altimeter preserved
        assert result["MA1__part3"] is None  # station pressure nulled

    def test_ma1_bad_altimeter_preserves_station_pressure(self):
        result = clean_value_quality("10132,8,09876,1", "MA1")
        assert result["MA1__part1"] is None  # altimeter nulled
        assert result["MA1__part3"] == pytest.approx(987.6)  # station pressure preserved

    def test_ma1_altimeter_rejects_non_mandatory_quality(self):
        result = clean_value_quality("10132,A,09876,1", "MA1")
        assert result["MA1__part1"] is None
        assert result["MA1__part3"] == pytest.approx(987.6)

    def test_ma1_station_pressure_rejects_non_mandatory_quality(self):
        result = clean_value_quality("10132,1,09876,U", "MA1")
        assert result["MA1__part1"] == pytest.approx(1013.2)
        assert result["MA1__part3"] is None

    def test_tmp_bad_quality_nulls_value(self):
        result = clean_value_quality("+0250,8", "TMP")
        assert result["TMP__value"] is None

    def test_tmp_good_quality_keeps_value(self):
        result = clean_value_quality("+0250,1", "TMP")
        assert result["TMP__value"] == pytest.approx(25.0)

    def test_ua1_bad_sea_state_quality_nulls_sea_state_only(self):
        result = clean_value_quality("I,05,120,1,03,8", "UA1")
        assert result["UA1__part2"] == pytest.approx(5.0)
        assert result["UA1__part3"] == pytest.approx(12.0)
        assert result["UA1__part5"] is None

    def test_ua1_bad_wave_quality_nulls_wave_values_only(self):
        result = clean_value_quality("I,05,120,8,03,1", "UA1")
        assert result["UA1__part2"] is None
        assert result["UA1__part3"] is None
        assert result["UA1__part5"] == pytest.approx(3.0)

    def test_md1_bad_tendency_quality_nulls_tendency_only(self):
        result = clean_value_quality("5,8,045,1,0123,1", "MD1")
        assert result["MD1__part1"] is None
        assert result["MD1__part3"] == pytest.approx(4.5)
        assert result["MD1__part5"] == pytest.approx(12.3)

    def test_md1_invalid_tendency_code(self):
        result = clean_value_quality("A,1,045,1,0123,1", "MD1")
        assert result["MD1__part1"] is None

    def test_ay_invalid_condition_code(self):
        result = clean_value_quality("10,1,01,1", "AY1")
        assert result["AY1__part1"] is None
        assert result["AY1__part3"] == pytest.approx(1.0)

    def test_ay_invalid_period_quantity(self):
        result = clean_value_quality("1,1,25,1", "AY1")
        assert result["AY1__part3"] is None

    def test_ax_invalid_condition_code(self):
        result = clean_value_quality("12,4,24,4", "AX1")
        assert result["AX1__part1"] is None
        assert result["AX1__part3"] == pytest.approx(24.0)

    def test_ax_invalid_period_quantity(self):
        result = clean_value_quality("01,4,01,4", "AX1")
        assert result["AX1__part3"] is None

    def test_az_invalid_period_quantity(self):
        result = clean_value_quality("1,1,25,1", "AZ1")
        assert result["AZ1__part3"] is None

    def test_ua1_bad_wave_quality_nulls_wave_parts(self):
        result = clean_value_quality("M,10,050,8,04,1", "UA1")
        assert result["UA1__part1"] is None
        assert result["UA1__part2"] is None
        assert result["UA1__part3"] is None
        assert result["UA1__part5"] == pytest.approx(4.0)

    def test_ua1_quality_code_outside_marine_domain(self):
        result = clean_value_quality("M,10,050,4,04,1", "UA1")
        assert result["UA1__part1"] is None
        assert result["UA1__part2"] is None
        assert result["UA1__part3"] is None
        assert result["UA1__part5"] == pytest.approx(4.0)

    def test_ua1_invalid_method_code(self):
        result = clean_value_quality("X,05,120,1,03,1", "UA1")
        assert result["UA1__part1"] is None
        assert result["UA1__part2"] == pytest.approx(5.0)
        assert result["UA1__part3"] == pytest.approx(12.0)

    def test_ua1_invalid_sea_state_code(self):
        result = clean_value_quality("I,05,120,1,10,1", "UA1")
        assert result["UA1__part2"] == pytest.approx(5.0)
        assert result["UA1__part3"] == pytest.approx(12.0)
        assert result["UA1__part5"] is None

    def test_ua1_invalid_wave_period(self):
        result = clean_value_quality("I,31,120,1,03,1", "UA1")
        assert result["UA1__part2"] is None

    def test_ua1_invalid_wave_height(self):
        result = clean_value_quality("I,05,501,1,03,1", "UA1")
        assert result["UA1__part3"] is None

    def test_ug1_bad_swell_quality_nulls_swell_parts(self):
        result = clean_value_quality("10,050,180,8", "UG1")
        assert result["UG1__part1"] is None
        assert result["UG1__part2"] is None
        assert result["UG1__part3"] is None

    def test_ug1_quality_code_outside_marine_domain(self):
        result = clean_value_quality("10,050,180,4", "UG1")
        assert result["UG1__part1"] is None
        assert result["UG1__part2"] is None
        assert result["UG1__part3"] is None

    def test_ug2_bad_swell_quality_nulls_swell_parts(self):
        result = clean_value_quality("10,050,180,8", "UG2")
        assert result["UG2__part1"] is None
        assert result["UG2__part2"] is None
        assert result["UG2__part3"] is None

    def test_ug2_quality_code_outside_marine_domain(self):
        result = clean_value_quality("10,050,180,4", "UG2")
        assert result["UG2__part1"] is None
        assert result["UG2__part2"] is None
        assert result["UG2__part3"] is None

    def test_ug1_invalid_swell_ranges(self):
        result = clean_value_quality("15,501,000,1", "UG1")
        assert result["UG1__part1"] is None
        assert result["UG1__part2"] is None
        assert result["UG1__part3"] is None

    def test_ug2_invalid_swell_ranges(self):
        result = clean_value_quality("15,501,000,1", "UG2")
        assert result["UG2__part1"] is None
        assert result["UG2__part2"] is None
        assert result["UG2__part3"] is None

    def test_wa1_invalid_source_and_tendency_codes(self):
        result = clean_value_quality("6,010,5,1", "WA1")
        assert result["WA1__part1"] is None
        assert result["WA1__part3"] is None

    def test_quality_in_dataframe(self):
        df = pd.DataFrame(
            {
                "WND": [
                    "180,1,N,0050,1",   # both good
                    "180,8,N,0050,1",   # bad direction
                    "180,1,N,0050,8",   # bad speed
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        # Row 0: both values present
        assert cleaned.loc[0, "wind_direction_deg"] == pytest.approx(180.0)
        assert cleaned.loc[0, "wind_speed_ms"] == pytest.approx(5.0)
        # Row 1: direction nulled, speed kept
        assert pd.isna(cleaned.loc[1, "wind_direction_deg"])
        assert cleaned.loc[1, "wind_speed_ms"] == pytest.approx(5.0)
        # Row 2: direction kept, speed nulled
        assert cleaned.loc[2, "wind_direction_deg"] == pytest.approx(180.0)
        assert pd.isna(cleaned.loc[2, "wind_speed_ms"])

    def test_gf1_cloud_quality_gates_values(self):
        result = clean_value_quality("05,05,8,05,8,99,8,5000,8,99,8,99,8", "GF1")
        assert result["GF1__part1"] is None
        assert result["GF1__part4"] is None
        assert result["GF1__part6"] is None
        assert result["GF1__part8"] is None
        assert result["GF1__part10"] is None
        assert result["GF1__part12"] is None

    def test_ga_cloud_type_missing(self):
        result = clean_value_quality("05,1,01000,1,99,1", "GA1")
        assert result["GA1__part5"] is None

    def test_oc1_quality_rejects_c(self):
        result = clean_value_quality("0085,C", "OC1")
        assert result["OC1__value"] is None

    def test_ma1_station_pressure_quality_rejects_c(self):
        result = clean_value_quality("10132,1,09876,C", "MA1")
        assert result["MA1__part1"] == pytest.approx(1013.2)
        assert result["MA1__part3"] is None

    def test_md1_quality_rejects_4(self):
        result = clean_value_quality("5,4,045,1,0123,1", "MD1")
        assert result["MD1__part1"] is None
        assert result["MD1__part3"] == pytest.approx(4.5)
        assert result["MD1__part5"] == pytest.approx(12.3)

    def test_md1_quality_rejects_4_for_pressure(self):
        result = clean_value_quality("5,1,045,4,0123,1", "MD1")
        assert result["MD1__part3"] is None
        assert result["MD1__part5"] == pytest.approx(12.3)

    def test_sa1_quality_rejects_4(self):
        result = clean_value_quality("0215,4", "SA1")
        assert result["SA1__value"] is None

    def test_au_quality_rejects_8(self):
        result = clean_value_quality("1,1,01,1,1,1,8", "AU1")
        assert result["AU1__part1"] is None
        assert result["AU1__part2"] is None
        assert result["AU1__part3"] is None
        assert result["AU1__part4"] is None
        assert result["AU1__part5"] is None
        assert result["AU1__part6"] is None

    def test_au_missing_sentinels(self):
        result = clean_value_quality("1,9,99,9,9,9,1", "AU1")
        assert result["AU1__part2"] is None
        assert result["AU1__part3"] is None
        assert result["AU1__part4"] is None
        assert result["AU1__part5"] is None
        assert result["AU1__part6"] is None

    def test_au_invalid_component_codes(self):
        result = clean_value_quality("5,9,10,9,6,4,1", "AU1")
        assert result["AU1__part1"] is None
        assert result["AU1__part3"] is None
        assert result["AU1__part5"] is None
        assert result["AU1__part6"] is None

    def test_at_quality_rejects_8(self):
        result = clean_value_quality("AU,01,FG,8", "AT1")
        assert result["AT1__part1"] is None
        assert result["AT1__part2"] is None
        assert result["AT1__part3"] is None

    def test_at_invalid_source_code(self):
        result = clean_value_quality("XX,01,FG,1", "AT1")
        assert result["AT1__part1"] is None
        assert result["AT1__part2"] == pytest.approx(1.0)
        assert result["AT1__part3"] == "FG"

    def test_at_invalid_weather_type(self):
        result = clean_value_quality("AU,99,FG,1", "AT1")
        assert result["AT1__part2"] is None

    def test_aw_missing_sentinel(self):
        result = clean_value_quality("99,1", "AW1")
        assert result["AW1__part1"] is None

    def test_aw_quality_rejects_8(self):
        result = clean_value_quality("01,8", "AW1")
        assert result["AW1__part1"] is None

    def test_aw_invalid_code(self):
        result = clean_value_quality("06,1", "AW1")
        assert result["AW1__part1"] is None

    def test_aw_valid_code(self):
        result = clean_value_quality("89,1", "AW1")
        assert result["AW1__part1"] == pytest.approx(89.0)

    def test_cb_quality_rejects_2(self):
        result = clean_value_quality("05,+000123,2,0", "CB1")
        assert result["CB1__part2"] is None

    def test_cf_quality_rejects_2(self):
        result = clean_value_quality("0123,2,0", "CF1")
        assert result["CF1__part1"] is None

    def test_cg_quality_rejects_2(self):
        result = clean_value_quality("+000123,2,0", "CG1")
        assert result["CG1__part1"] is None

    def test_ch_temp_quality_rejects_2(self):
        result = clean_value_quality("30,+01234,2,0,0456,1,0", "CH1")
        assert result["CH1__part2"] is None
        assert result["CH1__part5"] == pytest.approx(45.6)

    def test_ci_std_rh_quality_rejects_2(self):
        result = clean_value_quality("00010,1,0,00020,1,0,00030,1,0,00040,2,0", "CI1")
        assert result["CI1__part10"] is None

    def test_cn1_datalogger_quality_rejects_2(self):
        result = clean_value_quality("0123,1,0,0456,1,0,0789,2,0", "CN1")
        assert result["CN1__part7"] is None

    def test_cn2_door_open_missing(self):
        result = clean_value_quality("0001,1,0,0002,1,0,99,1,0", "CN2")
        assert result["CN2__part7"] is None

    def test_cn3_signature_quality_rejects_2(self):
        result = clean_value_quality("000100,1,0,000200,2,0", "CN3")
        assert result["CN3__part4"] is None

    def test_cn4_flag_missing_and_quality_rejects_2(self):
        result = clean_value_quality("9,1,0,0001,1,0,100,2,0,100,1,0", "CN4")
        assert result["CN4__part1"] is None
        assert result["CN4__part7"] is None
        assert result["CN4__part10"] == pytest.approx(10.0)

    def test_co1_missing_parts(self):
        result = clean_value_quality("99,+99", "CO1")
        assert result["CO1__part1"] is None
        assert result["CO1__part2"] is None

    def test_co1_invalid_climate_division(self):
        result = clean_value_quality("10,+00", "CO1")
        assert result["CO1__part1"] is None
        assert result["CO1__part2"] == pytest.approx(0.0)

    def test_co1_invalid_utc_offset(self):
        result = clean_value_quality("05,+13", "CO1")
        assert result["CO1__part1"] == pytest.approx(5.0)
        assert result["CO1__part2"] is None

    def test_co1_valid_utc_offsets(self):
        result = clean_value_quality("05,+12", "CO1")
        assert result["CO1__part2"] == pytest.approx(12.0)
        result = clean_value_quality("05,-12", "CO1")
        assert result["CO1__part2"] == pytest.approx(-12.0)

    def test_co2_missing_element(self):
        result = clean_value_quality("999,+0010", "CO2")
        assert result["CO2__part1"] is None
        assert result["CO2__part2"] == pytest.approx(1.0)

    def test_co2_invalid_element_id(self):
        result = clean_value_quality("AB,+0010", "CO2")
        assert result["CO2__part1"] is None
        assert result["CO2__part2"] == pytest.approx(1.0)

    def test_co2_offset_range(self):
        result = clean_value_quality("TMP,+9998", "CO2")
        assert result["CO2__part2"] == pytest.approx(999.8)
        result = clean_value_quality("TMP,+9999", "CO2")
        assert result["CO2__part2"] is None
        result = clean_value_quality("TMP,-9999", "CO2")
        assert result["CO2__part2"] == pytest.approx(-999.9)

    def test_cr1_quality_rejects_2(self):
        result = clean_value_quality("00123,2,0", "CR1")
        assert result["CR1__part1"] is None

    def test_ct_quality_rejects_2(self):
        result = clean_value_quality("+00123,2,0", "CT1")
        assert result["CT1__part1"] is None

    def test_cu_std_quality_rejects_2(self):
        result = clean_value_quality("+00123,1,0,0100,2,0", "CU1")
        assert result["CU1__part4"] is None

    def test_cv_min_quality_rejects_2(self):
        result = clean_value_quality("+00123,2,0,1200,1,0,+00234,1,0,1300,1,0", "CV1")
        assert result["CV1__part1"] is None
        assert result["CV1__part7"] == pytest.approx(23.4)

    def test_cv_max_time_missing(self):
        result = clean_value_quality("+00123,1,0,1200,1,0,+00234,1,0,9999,1,0", "CV1")
        assert result["CV1__part10"] is None

    def test_cv_min_time_invalid(self):
        result = clean_value_quality("+00123,1,0,2460,1,0,+00234,1,0,1300,1,0", "CV1")
        assert result["CV1__part4"] is None
        assert result["CV1__part7"] == pytest.approx(23.4)

    def test_cv_max_time_invalid(self):
        result = clean_value_quality("+00123,1,0,1200,1,0,+00234,1,0,2400,1,0", "CV1")
        assert result["CV1__part10"] is None

    def test_cw_wet2_missing(self):
        result = clean_value_quality("00010,1,0,99999,1,0", "CW1")
        assert result["CW1__part4"] is None

    def test_cx_precip_quality_rejects_2(self):
        result = clean_value_quality("+00100,2,0,1000,1,0,1000,1,0,1000,1,0", "CX1")
        assert result["CX1__part1"] is None

    def test_ed1_missing_parts(self):
        result = clean_value_quality("99,9,9999,1", "ED1")
        assert result["ED1__part1"] is None
        assert result["ED1__part2"] is None
        assert result["ED1__part3"] is None

    def test_ed1_quality_rejects_8(self):
        result = clean_value_quality("18,L,0800,8", "ED1")
        assert result["ED1__part1"] is None
        assert result["ED1__part2"] is None
        assert result["ED1__part3"] is None

    def test_ed1_invalid_direction(self):
        result = clean_value_quality("00,L,0800,1", "ED1")
        assert result["ED1__part1"] is None
        result = clean_value_quality("37,L,0800,1", "ED1")
        assert result["ED1__part1"] is None

    def test_ed1_invalid_visibility(self):
        result = clean_value_quality("18,L,5001,1", "ED1")
        assert result["ED1__part3"] is None
        result = clean_value_quality("18,L,0000,1", "ED1")
        assert result["ED1__part3"] == pytest.approx(0.0)

    def test_gg_missing_parts(self):
        result = clean_value_quality("99,9,99999,9,99,9,99,9", "GG1")
        assert result["GG1__part1"] is None
        assert result["GG1__part3"] is None
        assert result["GG1__part5"] is None
        assert result["GG1__part7"] is None

    def test_gg_quality_rejects_8(self):
        result = clean_value_quality("01,8,00100,8,01,8,01,8", "GG1")
        assert result["GG1__part1"] is None
        assert result["GG1__part3"] is None
        assert result["GG1__part5"] is None
        assert result["GG1__part7"] is None

    def test_ob1_quality_rejects_8(self):
        result = clean_value_quality(
            "060,0100,8,0,090,1,0,00010,1,0,00020,1,0",
            "OB1",
        )
        assert result["OB1__part2"] is None
        assert result["OB1__part5"] == pytest.approx(90.0)

    def test_oe1_quality_rejects_8(self):
        result = clean_value_quality("1,24,00100,090,1230,8", "OE1")
        assert result["OE1__part3"] is None

    def test_oe1_calm_direction(self):
        result = clean_value_quality("1,24,00000,999,1200,4", "OE1")
        assert result["OE1__part4"] == pytest.approx(0.0)

    def test_wa1_quality_rejects_8(self):
        result = clean_value_quality("1,001,1,8", "WA1")
        assert result["WA1__part1"] is None
        assert result["WA1__part2"] is None
        assert result["WA1__part3"] is None

    def test_wd1_quality_rejects_8(self):
        result = clean_value_quality("01,050,06,0,1,1,01,1,010,020,8", "WD1")
        assert result["WD1__part1"] is None
        assert result["WD1__part2"] is None
        assert result["WD1__part3"] is None

    def test_wg1_quality_rejects_8(self):
        result = clean_value_quality("01,10,01,01,01,8", "WG1")
        assert result["WG1__part1"] is None
        assert result["WG1__part2"] is None

    def test_eqd_q01_reason_code_rejects_8(self):
        result = clean_value_quality("123456,8,APC3", "Q01")
        assert result["Q01__part1"] == pytest.approx(123456.0)
        assert result["Q01__part2"] is None

    def test_eqd_n01_units_code_rejects_z(self):
        result = clean_value_quality("ABCDEF,Z,ALTP0A", "N01")
        assert result["N01__part1"] == "ABCDEF"
        assert result["N01__part2"] is None

    def test_eqd_q01_param_code_rejects_unknown_element(self):
        result = clean_value_quality("123456,1,ZZZZb0", "Q01")
        assert result["Q01__part3"] is None

    def test_eqd_q01_param_code_accepts_valid(self):
        result = clean_value_quality("123456,1,ALTPb0", "Q01")
        assert result["Q01__part3"] == "ALTPb0"

    def test_gp1_missing_parts(self):
        result = clean_value_quality("9999,9999,99,999,9999,99,999,9999,99,999", "GP1")
        assert result["GP1__part1"] is None
        assert result["GP1__part2"] is None
        assert result["GP1__part3"] is None
        assert result["GP1__part4"] is None
        assert result["GP1__part5"] is None
        assert result["GP1__part6"] is None
        assert result["GP1__part7"] is None
        assert result["GP1__part8"] is None
        assert result["GP1__part9"] is None
        assert result["GP1__part10"] is None

    def test_gq1_missing_parts(self):
        result = clean_value_quality("9999,9999,9,9999,9", "GQ1")
        assert result["GQ1__part1"] is None
        assert result["GQ1__part2"] is None
        assert result["GQ1__part4"] is None

    def test_gq1_quality_rejects_8(self):
        result = clean_value_quality("0060,0123,8,0456,1", "GQ1")
        assert result["GQ1__part2"] is None
        assert result["GQ1__part4"] == pytest.approx(45.6)

    def test_gr1_missing_parts(self):
        result = clean_value_quality("9999,9999,9,9999,9", "GR1")
        assert result["GR1__part1"] is None
        assert result["GR1__part2"] is None
        assert result["GR1__part4"] is None

    def test_gr1_quality_rejects_8(self):
        result = clean_value_quality("0060,0800,8,0900,1", "GR1")
        assert result["GR1__part2"] is None
        assert result["GR1__part4"] == pytest.approx(900.0)

    def test_ia1_quality_rejects_8(self):
        result = clean_value_quality("01,8", "IA1")
        assert result["IA1__part1"] is None

    def test_ib1_quality_rejects_2(self):
        result = clean_value_quality("+0100,2,0,+0050,1,0,+0150,1,0,0010,1,0", "IB1")
        assert result["IB1__part1"] is None
        assert result["IB1__part4"] == pytest.approx(5.0)

    def test_ic1_quality_rejects_2(self):
        result = clean_value_quality("24,0100,1,2,050,1,4,+050,1,4,+040,1,4", "IC1")
        assert result["IC1__part2"] is None

    def test_kb_quality_rejects_8(self):
        result = clean_value_quality("024,A,0100,8", "KB1")
        assert result["KB1__part3"] is None

    def test_kc_quality_rejects_8(self):
        result = clean_value_quality("M,1,0123,010203,8", "KC1")
        assert result["KC1__part3"] is None

    def test_kd_quality_rejects_8(self):
        result = clean_value_quality("024,H,0100,8", "KD1")
        assert result["KD1__part3"] is None

    def test_ke_quality_rejects_8(self):
        result = clean_value_quality("01,8,02,1,03,1,04,1", "KE1")
        assert result["KE1__part1"] is None

    def test_kf_quality_rejects_2(self):
        result = clean_value_quality("0123,2", "KF1")
        assert result["KF1__part1"] is None

    def test_kg_quality_rejects_8(self):
        result = clean_value_quality("024,D,0100,D,8", "KG1")
        assert result["KG1__part3"] is None

    def test_st1_quality_rejects_2(self):
        result = clean_value_quality("1,0123,2,0050,4,01,4,2,4", "ST1")
        assert result["ST1__part2"] is None

    def test_me1_quality_rejects_8(self):
        result = clean_value_quality("1,0123,8", "ME1")
        assert result["ME1__part2"] is None

    def test_mg1_quality_rejects_1(self):
        result = clean_value_quality("10132,1,09876,9", "MG1")
        assert result["MG1__part1"] is None

    def test_ay_quality_rejects_4(self):
        result = clean_value_quality("1,4,12,1", "AY1")
        assert result["AY1__part1"] is None
        assert result["AY1__part3"] == pytest.approx(12.0)

    def test_ay_period_quality_rejects_4(self):
        result = clean_value_quality("1,1,12,4", "AY1")
        assert result["AY1__part3"] is None

    def test_aa_quality_rejects_c(self):
        result = clean_value_quality("01,0010,1,C", "AA1")
        assert result["AA1__part2"] is None

    def test_aj_quality_rejects_c(self):
        result = clean_value_quality("0010,1,C,000100,1,C", "AJ1")
        assert result["AJ1__part1"] is None
        assert result["AJ1__part4"] is None

    def test_od_calm_direction(self):
        result = clean_value_quality("9,99,999,0000,1", "OD1")
        assert result["OD1__part3"] == pytest.approx(0.0)

    def test_oa_invalid_type_code(self):
        result = clean_value_quality("7,01,0005,1", "OA1")
        assert result["OA1__part1"] is None

    def test_oa_invalid_period_quantity(self):
        result = clean_value_quality("1,00,0005,1", "OA1")
        assert result["OA1__part2"] is None

    def test_oa_invalid_speed_rate(self):
        result = clean_value_quality("1,01,2001,1", "OA1")
        assert result["OA1__part3"] is None

    def test_od_invalid_direction_range(self):
        result = clean_value_quality("1,01,361,0005,1", "OD1")
        assert result["OD1__part3"] is None

    def test_od_invalid_speed_rate(self):
        result = clean_value_quality("1,01,090,2001,1", "OD1")
        assert result["OD1__part4"] is None

    def test_mv_invalid_code(self):
        result = clean_value_quality("10,4", "MV1")
        assert result["MV1__part1"] is None

    def test_mw_invalid_code(self):
        result = clean_value_quality("100,1", "MW1")
        assert result["MW1__part1"] is None

    def test_ob_invalid_period_minutes(self):
        result = clean_value_quality("000,0050,1,0,090,1,0,00010,1,0,00020,1,0", "OB1")
        assert result["OB1__part1"] is None

    def test_ob_invalid_max_gust(self):
        result = clean_value_quality("060,10000,1,0,090,1,0,00010,1,0,00020,1,0", "OB1")
        assert result["OB1__part2"] is None

    def test_ob_invalid_direction(self):
        result = clean_value_quality("060,0050,1,0,361,1,0,00010,1,0,00020,1,0", "OB1")
        assert result["OB1__part5"] is None

    def test_ob_invalid_speed_std(self):
        result = clean_value_quality("060,0050,1,0,090,1,0,100000,1,0,00020,1,0", "OB1")
        assert result["OB1__part8"] is None

    def test_ob_invalid_direction_std(self):
        result = clean_value_quality("060,0050,1,0,090,1,0,00010,1,0,100000,1,0", "OB1")
        assert result["OB1__part11"] is None

    def test_aj_condition_missing(self):
        result = clean_value_quality("0010,9,1,000100,9,1", "AJ1")
        assert result["AJ1__part2"] is None
        assert result["AJ1__part5"] is None

    def test_ua1_missing_method_and_sea_state(self):
        result = clean_value_quality("9,05,120,1,99,1", "UA1")
        assert result["UA1__part1"] is None
        assert result["UA1__part5"] is None

    def test_ab_monthly_total_quality(self):
        result = clean_value_quality("00500,1,8", "AB1")
        assert result["AB1__part1"] is None

    def test_ac_duration_characteristic_codes(self):
        result = clean_value_quality("4,C,1", "AC1")
        assert result["AC1__part1"] is None
        assert result["AC1__part2"] == "C"

    def test_ac_characteristic_missing(self):
        result = clean_value_quality("1,9,1", "AC1")
        assert result["AC1__part2"] is None

    def test_ad_missing_dates(self):
        result = clean_value_quality("01000,2,9999,0102,9999,1", "AD1")
        assert result["AD1__part3"] is None
        assert result["AD1__part5"] is None

    def test_ae_missing_and_quality(self):
        result = clean_value_quality("99,1,05,8,10,1,00,1", "AE1")
        assert result["AE1__part1"] is None
        assert result["AE1__part3"] is None

    def test_ag_discrepancy_and_missing_depth(self):
        result = clean_value_quality("9,999", "AG1")
        assert result["AG1__part1"] is None
        assert result["AG1__part2"] is None

    def test_ah_missing_and_quality(self):
        result = clean_value_quality("999,9999,9,999999,1", "AH1")
        assert result["AH1__part1"] is None
        assert result["AH1__part2"] is None
        assert result["AH1__part3"] is None
        assert result["AH1__part4"] is None

    def test_ah_quality_rejects_c(self):
        result = clean_value_quality("015,0123,1,010100,C", "AH1")
        assert result["AH1__part2"] is None

    def test_ai_missing_and_quality(self):
        result = clean_value_quality("999,9999,9,999999,1", "AI1")
        assert result["AI1__part1"] is None
        assert result["AI1__part2"] is None
        assert result["AI1__part3"] is None
        assert result["AI1__part4"] is None

    def test_ai_quality_rejects_c(self):
        result = clean_value_quality("060,0123,1,010100,C", "AI1")
        assert result["AI1__part2"] is None

    def test_ak_missing_and_quality(self):
        result = clean_value_quality("9999,9,999999,1", "AK1")
        assert result["AK1__part1"] is None
        assert result["AK1__part2"] is None
        assert result["AK1__part3"] is None

    def test_ak_quality_rejects_c(self):
        result = clean_value_quality("0100,1,010203,C", "AK1")
        assert result["AK1__part1"] is None

    def test_al_missing_and_quality(self):
        result = clean_value_quality("99,999,9,1", "AL1")
        assert result["AL1__part1"] is None
        assert result["AL1__part2"] is None
        assert result["AL1__part3"] is None

    def test_al_quality_rejects_c(self):
        result = clean_value_quality("24,010,1,C", "AL1")
        assert result["AL1__part2"] is None

    def test_am_missing_and_quality(self):
        result = clean_value_quality("9999,9,9999,9999,9999,1", "AM1")
        assert result["AM1__part1"] is None
        assert result["AM1__part2"] is None
        assert result["AM1__part3"] is None
        assert result["AM1__part4"] is None
        assert result["AM1__part5"] is None

    def test_am_quality_rejects_c(self):
        result = clean_value_quality("0100,1,0102,0203,0304,C", "AM1")
        assert result["AM1__part1"] is None

    def test_an_missing_and_quality(self):
        result = clean_value_quality("999,9999,9,1", "AN1")
        assert result["AN1__part1"] is None
        assert result["AN1__part2"] is None
        assert result["AN1__part3"] is None

    def test_an_quality_rejects_c(self):
        result = clean_value_quality("024,0100,1,C", "AN1")
        assert result["AN1__part2"] is None

    def test_ao_missing_and_quality(self):
        result = clean_value_quality("99,9999,9,1", "AO1")
        assert result["AO1__part1"] is None
        assert result["AO1__part2"] is None
        assert result["AO1__part3"] is None

    def test_ao_quality_rejects_8(self):
        result = clean_value_quality("15,0010,1,8", "AO1")
        assert result["AO1__part2"] is None

    def test_ap_missing_and_quality(self):
        result = clean_value_quality("9999,9,1", "AP1")
        assert result["AP1__part1"] is None
        assert result["AP1__part2"] is None

    def test_ap_quality_rejects_8(self):
        result = clean_value_quality("0010,9,8", "AP1")
        assert result["AP1__part1"] is None


class TestTwoPartFieldNamingAndQuality:
    def test_mw_two_part_uses_parts(self):
        result = clean_value_quality("12,4", "MW1")
        assert "MW1__part1" in result
        assert "MW1__part2" in result

    def test_mw_quality_gates_code(self):
        result = clean_value_quality("12,8", "MW1")
        assert result["MW1__part1"] is None

    def test_mv_quality_gates_code(self):
        result = clean_value_quality("05,3", "MV1")
        assert result["MV1__part1"] is None

    def test_gj_quality_gates_value(self):
        result = clean_value_quality("0100,8", "GJ1")
        assert result["GJ1__part1"] is None


class TestCleanDataframeEdgeCases:
    def test_invalid_quality_nulls_values_in_dataframe(self):
        df = pd.DataFrame(
            {
                "TMP": [
                    "+0250,1",
                    "+0250,8",
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "temperature_c"] == pytest.approx(25.0)
        assert pd.isna(cleaned.loc[1, "temperature_c"])

    def test_invalid_quality_in_multipart_field(self):
        df = pd.DataFrame(
            {
                "KA1": [
                    "005,1,0123,8",  # invalid quality code
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert pd.isna(cleaned.loc[0, "extreme_temp_period_hours_1"])
        assert pd.isna(cleaned.loc[0, "extreme_temp_c_1"])

    def test_vis_missing_with_leading_zeros(self):
        df = pd.DataFrame(
            {
                "VIS": [
                    "009999,5,N,1",
                ],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "visibility_m"] == pytest.approx(9999.0)

    def test_add_section_marker_dropped(self):
        df = pd.DataFrame(
            {
                "ADD": ["ADD", "ADD"],
                "TMP": ["+0250,1", "+0260,1"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=True)
        assert "ADD" not in cleaned.columns

    def test_remark_parsing(self):
        df = pd.DataFrame(
            {
                "REM": [
                    "SYN052AAXX 01004",
                    "METfoo",
                    "XYZbar",
                    None,
                ]
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "remarks_type_code"] == "SYN"
        assert cleaned.loc[0, "remarks_text"] == "052AAXX 01004"
        assert cleaned.loc[1, "remarks_type_code"] == "MET"
        assert cleaned.loc[1, "remarks_text"] == "foo"
        assert pd.isna(cleaned.loc[2, "remarks_type_code"])
        assert cleaned.loc[2, "remarks_text"] == "XYZbar"
        assert pd.isna(cleaned.loc[3, "remarks_type_code"])
        assert pd.isna(cleaned.loc[3, "remarks_text"])

    def test_qnn_parsing(self):
        df = pd.DataFrame(
            {
                "QNN": [
                    "QNN A1234B5678 001234002345",
                    "QNNZ9999",
                    None,
                ]
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "qnn_element_ids"] == "A,B"
        assert cleaned.loc[0, "qnn_source_flags"] == "1234,5678"
        assert cleaned.loc[0, "qnn_data_values"] == "001234,002345"
        assert pd.isna(cleaned.loc[1, "qnn_element_ids"])
        assert pd.isna(cleaned.loc[1, "qnn_source_flags"])
        assert pd.isna(cleaned.loc[1, "qnn_data_values"])
        assert pd.isna(cleaned.loc[2, "qnn_element_ids"])
        assert pd.isna(cleaned.loc[2, "qnn_source_flags"])
        assert pd.isna(cleaned.loc[2, "qnn_data_values"])


class TestControlAndMandatoryNormalization:
    def test_control_field_validation(self):
        df = pd.DataFrame(
            {
                "LATITUDE": [99.999, 45.0],
                "LONGITUDE": [181.0, -120.0],
                "ELEVATION": [9000.0, 100.0],
                "CALL_SIGN": ["99999", "KJFK"],
                "SOURCE": ["9", "4"],
                "REPORT_TYPE": ["FM-12", "BOGUS"],
                "QUALITY_CONTROL": ["V020", "V02"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=True)
        assert pd.isna(cleaned.loc[0, "LATITUDE"])
        assert pd.isna(cleaned.loc[0, "LONGITUDE"])
        assert pd.isna(cleaned.loc[0, "ELEVATION"])
        assert pd.isna(cleaned.loc[0, "CALL_SIGN"])
        assert pd.isna(cleaned.loc[0, "SOURCE"])
        assert cleaned.loc[0, "REPORT_TYPE"] == "FM-12"
        assert pd.isna(cleaned.loc[0, "QUALITY_CONTROL"])
        assert cleaned.loc[1, "LATITUDE"] == pytest.approx(45.0)
        assert cleaned.loc[1, "LONGITUDE"] == pytest.approx(-120.0)
        assert cleaned.loc[1, "ELEVATION"] == pytest.approx(100.0)
        assert cleaned.loc[1, "CALL_SIGN"] == "KJFK"
        assert cleaned.loc[1, "SOURCE"] == "4"
        assert cleaned.loc[1, "REPORT_TYPE"] == "BOGUS"
        assert cleaned.loc[1, "QUALITY_CONTROL"] == "V02"

    def test_control_date_time_validation(self):
        df = pd.DataFrame(
            {
                "DATE": ["20240131", "20240132"],
                "TIME": ["2359", "2360"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=True)
        assert cleaned.loc[0, "DATE"] == "20240131"
        assert cleaned.loc[0, "TIME"] == "2359"
        assert pd.isna(cleaned.loc[1, "DATE"])
        assert pd.isna(cleaned.loc[1, "TIME"])

    def test_control_date_rejects_iso_timestamps(self):
        df = pd.DataFrame(
            {
                "DATE": ["2024-01-31T23:59:00Z", "2024-13-01T00:00:00Z"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=True)
        assert pd.isna(cleaned.loc[0, "DATE"])
        assert pd.isna(cleaned.loc[1, "DATE"])

    def test_mandatory_clamps_and_calm_wind(self):
        df = pd.DataFrame(
            {
                "CIG": ["25000,1,9,9"],
                "VIS": ["170000,1,N,1"],
                "WND": ["090,1,9,0000,1"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert cleaned.loc[0, "ceiling_height_m"] == pytest.approx(22000.0)
        assert cleaned.loc[0, "visibility_m"] == pytest.approx(160000.0)
        assert cleaned.loc[0, "wind_type_code"] == "C"

    def test_mandatory_domain_codes(self):
        df = pd.DataFrame(
            {
                "WND": ["090,1,Z,0005,1"],
                "CIG": ["01000,1,Z,X"],
                "VIS": ["010000,1,X,1"],
            }
        )
        cleaned = clean_noaa_dataframe(df, keep_raw=False)
        assert pd.isna(cleaned.loc[0, "wind_type_code"])
        assert pd.isna(cleaned.loc[0, "ceiling_determination_code"])
        assert pd.isna(cleaned.loc[0, "ceiling_cavok_code"])
        assert pd.isna(cleaned.loc[0, "visibility_variability_code"])
