"""Shared constants for NOAA ISD Global Hourly data."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

BASE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access"

QUALITY_FLAGS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "9",
    "A",
    "C",
    "I",
    "M",
    "P",
    "R",
    "U",
}

CLOUD_QUALITY_FLAGS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "9",
    "M",
}

DEFAULT_START_YEAR = 2000
DEFAULT_END_YEAR = 2019


@dataclass(frozen=True)
class FieldPartRule:
    scale: float | None = None
    missing_values: set[str] | None = None
    quality_part: int | None = None
    allowed_quality: set[str] | None = None
    kind: str = "numeric"
    agg: str = "mean"  # mean | max | min | mode | sum | drop | circular_mean


@dataclass(frozen=True)
class FieldRule:
    code: str
    parts: dict[int, FieldPartRule]


@dataclass(frozen=True)
class FieldRegistryEntry:
    code: str
    part: int
    internal_name: str
    name: str
    kind: str
    scale: float | None
    missing_values: set[str] | None
    quality_part: int | None
    agg: str


FIELD_RULES: dict[str, FieldRule] = {
    "WND": FieldRule(
        code="WND",
        parts={
            1: FieldPartRule(missing_values={"999"}, quality_part=2, agg="circular_mean"),
            2: FieldPartRule(kind="quality", agg="drop"),  # direction quality
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # wind type code
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop"),  # speed quality
        },
    ),
    "CIG": FieldRule(
        code="CIG",
        parts={
            1: FieldPartRule(missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop"),  # height quality
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # determination code
            4: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # CAVOK code
        },
    ),
    "VIS": FieldRule(
        code="VIS",
        parts={
            1: FieldPartRule(missing_values={"999999"}, quality_part=2, agg="min"),
            2: FieldPartRule(kind="quality", agg="drop"),  # distance quality
            3: FieldPartRule(quality_part=4, kind="categorical", agg="drop", missing_values={"9"}),
            4: FieldPartRule(kind="quality", agg="drop"),  # variability quality
        },
    ),
    "TMP": FieldRule(
        code="TMP",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2)},
    ),
    "DEW": FieldRule(
        code="DEW",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2)},
    ),
    "SLP": FieldRule(
        code="SLP",
        parts={1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2)},
    ),
    "OC1": FieldRule(
        code="OC1",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2, agg="max")},
    ),
    "MA1": FieldRule(
        code="MA1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop"),  # altimeter quality
            3: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=4),
            4: FieldPartRule(kind="quality", agg="drop"),  # station pressure quality
        },
    ),
    "MD1": FieldRule(
        code="MD1",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=2,
                missing_values={"9"},
            ),  # pressure tendency code
            2: FieldPartRule(kind="quality", agg="drop"),  # tendency quality
            3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            4: FieldPartRule(kind="quality", agg="drop"),  # 3-hr pressure quality
            5: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=6),
            6: FieldPartRule(kind="quality", agg="drop"),  # 24-hr pressure quality
        },
    ),
    "SA1": FieldRule(
        code="SA1",
        parts={1: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=2)},
    ),
    "UA1": FieldRule(
        code="UA1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", quality_part=4),  # method code
            2: FieldPartRule(missing_values={"99"}, quality_part=4),  # wave period (seconds)
            3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # wave height quality
            5: FieldPartRule(kind="categorical", agg="drop", quality_part=6),  # sea state code
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # sea state quality
        },
    ),
    "UG1": FieldRule(
        code="UG1",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=4),  # primary swell period (seconds)
            2: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            3: FieldPartRule(missing_values={"999"}, agg="circular_mean", quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # swell height quality
        },
    ),
    "GE1": FieldRule(
        code="GE1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop"),  # convective cloud code
            2: FieldPartRule(kind="categorical", agg="drop"),  # vertical datum
            3: FieldPartRule(missing_values={"99999"}),  # base height upper range
            4: FieldPartRule(missing_values={"99999"}),  # base height lower range
        },
    ),
    "GF1": FieldRule(
        code="GF1",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=3, agg="mean"),
            2: FieldPartRule(missing_values={"99"}, agg="mean"),
            3: FieldPartRule(kind="quality", agg="drop"),  # total coverage quality
            4: FieldPartRule(missing_values={"99"}, quality_part=5, agg="mean"),
            5: FieldPartRule(kind="quality", agg="drop"),  # lowest cloud cover quality
            6: FieldPartRule(kind="categorical", agg="drop"),  # low cloud genus
            7: FieldPartRule(kind="quality", agg="drop"),  # low cloud genus quality
            8: FieldPartRule(missing_values={"99999"}, quality_part=9),
            9: FieldPartRule(kind="quality", agg="drop"),  # lowest base height quality
            10: FieldPartRule(kind="categorical", agg="drop"),  # mid cloud genus
            11: FieldPartRule(kind="quality", agg="drop"),  # mid cloud genus quality
            12: FieldPartRule(kind="categorical", agg="drop"),  # high cloud genus
            13: FieldPartRule(kind="quality", agg="drop"),  # high cloud genus quality
        },
    ),
}

FIELD_RULE_PREFIXES: dict[str, FieldRule] = {
    "AA": FieldRule(
        code="AA*",
        parts={
            1: FieldPartRule(missing_values={"99"}, agg="drop"),  # period hours
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4, agg="sum"),
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # condition code
            4: FieldPartRule(kind="quality", agg="drop"),  # quality code
        },
    ),
    "AJ": FieldRule(
        code="AJ*",
        parts={
            1: FieldPartRule(missing_values={"9999"}, quality_part=3),
            2: FieldPartRule(kind="categorical", agg="drop"),  # snow depth condition
            3: FieldPartRule(kind="quality", agg="drop"),  # snow depth quality
            4: FieldPartRule(scale=0.1, missing_values={"999999"}, quality_part=6),
            5: FieldPartRule(kind="categorical", agg="drop"),  # equiv water condition
            6: FieldPartRule(kind="quality", agg="drop"),  # equiv water quality
        },
    ),
    "AU": FieldRule(
        code="AU*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # intensity
            2: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # descriptor
            3: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # precip code
            4: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # obscuration
            5: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # other phenomena
            6: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # combo indicator
            7: FieldPartRule(kind="quality", agg="drop"),  # quality code
        },
    ),
    "GA": FieldRule(
        code="GA*",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=2, agg="mean"),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # coverage quality
            3: FieldPartRule(missing_values={"99999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # base height quality
            5: FieldPartRule(kind="categorical", agg="drop", quality_part=6),  # cloud type
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # cloud type quality
        },
    ),
    "KA": FieldRule(
        code="KA*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"999"}),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(kind="quality", agg="drop"),  # temperature quality
        },
    ),
    "OA": FieldRule(
        code="OA*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "OD": FieldRule(
        code="OD*",
        parts={
            1: FieldPartRule(missing_values={"9"}, kind="categorical", agg="drop"),
            2: FieldPartRule(missing_values={"99"}, kind="categorical", agg="drop"),
            3: FieldPartRule(missing_values={"999"}, agg="circular_mean"),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                missing_values={"9"},
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "MV": FieldRule(
        code="MV*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
        },
    ),
    "MW": FieldRule(
        code="MW*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop"),  # present-weather code
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # present-weather quality
        },
    ),
    "AY": FieldRule(
        code="AY*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop"),  # past-weather condition code
            2: FieldPartRule(kind="quality", agg="drop"),  # past-weather condition quality
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),  # past-weather period
            4: FieldPartRule(kind="quality", agg="drop"),  # past-weather period quality
        },
    ),
}


def get_field_rule(prefix: str) -> FieldRule | None:
    if prefix in FIELD_RULES:
        return FIELD_RULES[prefix]
    for key, rule in FIELD_RULE_PREFIXES.items():
        if prefix.startswith(key):
            return rule
    return None


# ── Column classification helpers ────────────────────────────────────────

_EXPANDED_COL_RE = re.compile(r"^(?P<field>[A-Z][A-Z0-9]*)__(?P<suffix>.+)$")

FRIENDLY_COLUMN_MAP: dict[str, str] = {
    "WND__part1": "wind_direction_deg",
    "WND__part2": "wind_direction_quality_code",
    "WND__part3": "wind_type_code",
    "WND__part4": "wind_speed_ms",
    "WND__part5": "wind_speed_quality_code",
    "WND__direction_variable": "wind_direction_variable",
    "CIG__part1": "ceiling_height_m",
    "CIG__part2": "ceiling_height_quality_code",
    "CIG__part3": "ceiling_determination_code",
    "CIG__part4": "ceiling_cavok_code",
    "VIS__part1": "visibility_m",
    "VIS__part2": "visibility_quality_code",
    "VIS__part3": "visibility_variability_code",
    "VIS__part4": "visibility_variability_quality_code",
    "TMP__value": "temperature_c",
    "TMP__quality": "temperature_quality_code",
    "DEW__value": "dew_point_c",
    "DEW__quality": "dew_point_quality_code",
    "SLP__value": "sea_level_pressure_hpa",
    "SLP__quality": "sea_level_pressure_quality_code",
    "OC1__value": "wind_gust_ms",
    "OC1__quality": "wind_gust_quality_code",
    "MA1__part1": "altimeter_setting_hpa",
    "MA1__part2": "altimeter_quality_code",
    "MA1__part3": "station_pressure_hpa",
    "MA1__part4": "station_pressure_quality_code",
    "MD1__part1": "pressure_tendency_code",
    "MD1__part2": "pressure_tendency_quality_code",
    "MD1__part3": "pressure_change_3hr_hpa",
    "MD1__part4": "pressure_change_3hr_quality_code",
    "MD1__part5": "pressure_change_24hr_hpa",
    "MD1__part6": "pressure_change_24hr_quality_code",
    "SA1__value": "sea_surface_temperature_c",
    "SA1__quality": "sea_surface_temperature_quality_code",
    "UA1__part1": "wave_method_code",
    "UA1__part2": "wave_period_seconds",
    "UA1__part3": "wave_height_m",
    "UA1__part4": "wave_height_quality_code",
    "UA1__part5": "sea_state_code",
    "UA1__part6": "sea_state_quality_code",
    "UG1__part1": "swell_period_seconds",
    "UG1__part2": "swell_height_m",
    "UG1__part3": "swell_direction_deg",
    "UG1__part4": "swell_height_quality_code",
    "GE1__part1": "convective_cloud_code",
    "GE1__part2": "cloud_vertical_datum_code",
    "GE1__part3": "cloud_base_height_upper_m",
    "GE1__part4": "cloud_base_height_lower_m",
    "GF1__part1": "cloud_total_coverage",
    "GF1__part2": "cloud_opaque_coverage",
    "GF1__part3": "cloud_total_coverage_quality_code",
    "GF1__part4": "cloud_lowest_coverage",
    "GF1__part5": "cloud_lowest_coverage_quality_code",
    "GF1__part6": "cloud_low_genus_code",
    "GF1__part7": "cloud_low_genus_quality_code",
    "GF1__part8": "cloud_lowest_base_height_m",
    "GF1__part9": "cloud_lowest_base_height_quality_code",
    "GF1__part10": "cloud_mid_genus_code",
    "GF1__part11": "cloud_mid_genus_quality_code",
    "GF1__part12": "cloud_high_genus_code",
    "GF1__part13": "cloud_high_genus_quality_code",
}

_FRIENDLY_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^MW(?P<idx>\d+)__value$"), "present_weather_code_{idx}"),
    (re.compile(r"^MV(?P<idx>\d+)__part1$"), "present_weather_vicinity_code_{idx}"),
    (re.compile(r"^MV(?P<idx>\d+)__part2$"), "present_weather_vicinity_quality_code_{idx}"),
    (re.compile(r"^AY(?P<idx>\d+)__part1$"), "past_weather_condition_code_{idx}"),
    (re.compile(r"^AY(?P<idx>\d+)__part3$"), "past_weather_period_hours_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part1$"), "precip_period_hours_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part2$"), "precip_amount_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part3$"), "precip_condition_code_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part4$"), "precip_quality_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part1$"), "snow_depth_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part2$"), "snow_depth_condition_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part3$"), "snow_depth_quality_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part4$"), "snow_water_equivalent_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part5$"), "snow_water_condition_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part6$"), "snow_water_quality_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part1$"), "weather_intensity_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part2$"), "weather_descriptor_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part3$"), "weather_precip_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part4$"), "weather_obscuration_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part5$"), "weather_other_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part6$"), "weather_combo_indicator_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part7$"), "weather_quality_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part1$"), "cloud_layer_coverage_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part2$"), "cloud_layer_coverage_quality_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part3$"), "cloud_layer_base_height_m_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part4$"), "cloud_layer_base_height_quality_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part5$"), "cloud_layer_type_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part6$"), "cloud_layer_type_quality_code_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part3$"), "extreme_temp_c_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part2$"), "extreme_temp_type_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part1$"), "extreme_temp_period_hours_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part4$"), "extreme_temp_quality_code_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part1$"), "supp_wind_oa_type_code_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part2$"), "supp_wind_oa_period_hours_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part3$"), "supp_wind_oa_speed_ms_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part4$"), "supp_wind_oa_speed_quality_code_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part1$"), "supp_wind_type_code_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part2$"), "supp_wind_period_hours_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part3$"), "supp_wind_direction_deg_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part4$"), "supp_wind_speed_ms_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part5$"), "supp_wind_speed_quality_code_{idx}"),
]

_INTERNAL_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^present_weather_code_(?P<idx>\d+)$"), "MW{idx}__value"),
    (re.compile(r"^present_weather_vicinity_code_(?P<idx>\d+)$"), "MV{idx}__part1"),
    (re.compile(r"^present_weather_vicinity_quality_code_(?P<idx>\d+)$"), "MV{idx}__part2"),
    (re.compile(r"^past_weather_condition_code_(?P<idx>\d+)$"), "AY{idx}__part1"),
    (re.compile(r"^past_weather_period_hours_(?P<idx>\d+)$"), "AY{idx}__part3"),
    (re.compile(r"^precip_period_hours_(?P<idx>\d+)$"), "AA{idx}__part1"),
    (re.compile(r"^precip_amount_(?P<idx>\d+)$"), "AA{idx}__part2"),
    (re.compile(r"^precip_condition_code_(?P<idx>\d+)$"), "AA{idx}__part3"),
    (re.compile(r"^precip_quality_code_(?P<idx>\d+)$"), "AA{idx}__part4"),
    (re.compile(r"^snow_depth_(?P<idx>\d+)$"), "AJ{idx}__part1"),
    (re.compile(r"^snow_depth_condition_code_(?P<idx>\d+)$"), "AJ{idx}__part2"),
    (re.compile(r"^snow_depth_quality_code_(?P<idx>\d+)$"), "AJ{idx}__part3"),
    (re.compile(r"^snow_water_equivalent_(?P<idx>\d+)$"), "AJ{idx}__part4"),
    (re.compile(r"^snow_water_condition_code_(?P<idx>\d+)$"), "AJ{idx}__part5"),
    (re.compile(r"^snow_water_quality_code_(?P<idx>\d+)$"), "AJ{idx}__part6"),
    (re.compile(r"^weather_intensity_code_(?P<idx>\d+)$"), "AU{idx}__part1"),
    (re.compile(r"^weather_descriptor_code_(?P<idx>\d+)$"), "AU{idx}__part2"),
    (re.compile(r"^weather_precip_code_(?P<idx>\d+)$"), "AU{idx}__part3"),
    (re.compile(r"^weather_obscuration_code_(?P<idx>\d+)$"), "AU{idx}__part4"),
    (re.compile(r"^weather_other_code_(?P<idx>\d+)$"), "AU{idx}__part5"),
    (re.compile(r"^weather_combo_indicator_(?P<idx>\d+)$"), "AU{idx}__part6"),
    (re.compile(r"^weather_quality_code_(?P<idx>\d+)$"), "AU{idx}__part7"),
    (re.compile(r"^cloud_layer_coverage_(?P<idx>\d+)$"), "GA{idx}__part1"),
    (re.compile(r"^cloud_layer_coverage_quality_code_(?P<idx>\d+)$"), "GA{idx}__part2"),
    (re.compile(r"^cloud_layer_base_height_m_(?P<idx>\d+)$"), "GA{idx}__part3"),
    (re.compile(r"^cloud_layer_base_height_quality_code_(?P<idx>\d+)$"), "GA{idx}__part4"),
    (re.compile(r"^cloud_layer_type_code_(?P<idx>\d+)$"), "GA{idx}__part5"),
    (re.compile(r"^cloud_layer_type_quality_code_(?P<idx>\d+)$"), "GA{idx}__part6"),
    (re.compile(r"^extreme_temp_c_(?P<idx>\d+)$"), "KA{idx}__part3"),
    (re.compile(r"^extreme_temp_type_(?P<idx>\d+)$"), "KA{idx}__part2"),
    (re.compile(r"^extreme_temp_period_hours_(?P<idx>\d+)$"), "KA{idx}__part1"),
    (re.compile(r"^extreme_temp_quality_code_(?P<idx>\d+)$"), "KA{idx}__part4"),
    (re.compile(r"^supp_wind_oa_type_code_(?P<idx>\d+)$"), "OA{idx}__part1"),
    (re.compile(r"^supp_wind_oa_period_hours_(?P<idx>\d+)$"), "OA{idx}__part2"),
    (re.compile(r"^supp_wind_oa_speed_ms_(?P<idx>\d+)$"), "OA{idx}__part3"),
    (re.compile(r"^supp_wind_oa_speed_quality_code_(?P<idx>\d+)$"), "OA{idx}__part4"),
    (re.compile(r"^supp_wind_type_code_(?P<idx>\d+)$"), "OD{idx}__part1"),
    (re.compile(r"^supp_wind_period_hours_(?P<idx>\d+)$"), "OD{idx}__part2"),
    (re.compile(r"^supp_wind_direction_deg_(?P<idx>\d+)$"), "OD{idx}__part3"),
    (re.compile(r"^supp_wind_speed_ms_(?P<idx>\d+)$"), "OD{idx}__part4"),
    (re.compile(r"^supp_wind_speed_quality_code_(?P<idx>\d+)$"), "OD{idx}__part5"),
]

_INTERNAL_COLUMN_MAP = {v: k for k, v in FRIENDLY_COLUMN_MAP.items()}

FIELD_REGISTRY: dict[str, FieldRegistryEntry] = {}


def _parse_expanded_col(col: str) -> tuple[str, str] | None:
    """Return (field_prefix, suffix) for an expanded column, or None."""
    m = _EXPANDED_COL_RE.match(col)
    if m:
        return m.group("field"), m.group("suffix")
    return None


def to_friendly_column(col: str) -> str:
    mapped = FRIENDLY_COLUMN_MAP.get(col)
    if mapped:
        return mapped
    for pattern, template in _FRIENDLY_PATTERNS:
        match = pattern.match(col)
        if match:
            return template.format(**match.groupdict())
    return col


def to_internal_column(col: str) -> str:
    mapped = _INTERNAL_COLUMN_MAP.get(col)
    if mapped:
        return mapped
    for pattern, template in _INTERNAL_PATTERNS:
        match = pattern.match(col)
        if match:
            return template.format(**match.groupdict())
    return col


def _internal_name(prefix: str, part_idx: int, suffix: str) -> str:
    if suffix == "value":
        return f"{prefix}__value"
    return f"{prefix}__part{part_idx}"


def get_field_registry_entry(
    prefix: str,
    part_idx: int,
    suffix: str = "part",
) -> FieldRegistryEntry | None:
    internal_name = _internal_name(prefix, part_idx, suffix)
    entry = FIELD_REGISTRY.get(internal_name)
    if entry is not None:
        return entry
    rule = get_field_rule(prefix)
    if rule is None:
        return None
    part_rule = rule.parts.get(part_idx)
    if part_rule is None:
        return None
    entry = FieldRegistryEntry(
        code=prefix,
        part=part_idx,
        internal_name=internal_name,
        name=to_friendly_column(internal_name),
        kind=part_rule.kind,
        scale=part_rule.scale,
        missing_values=part_rule.missing_values,
        quality_part=part_rule.quality_part,
        agg=part_rule.agg,
    )
    FIELD_REGISTRY[internal_name] = entry
    return entry


def is_quality_column(col: str) -> bool:
    """True for observation-level quality columns (e.g. WND__quality)."""
    internal = to_internal_column(col)
    return internal.endswith("__quality") or internal.endswith("__qc")


def is_categorical_column(col: str) -> bool:
    """True if the column is a WMO/ISD category code that must not be averaged."""
    parsed = _parse_expanded_col(to_internal_column(col))
    if parsed is None:
        return False
    field_prefix, suffix = parsed
    rule = get_field_rule(field_prefix)
    if rule is None:
        return False
    # Match suffix like "part3" or "value"
    if suffix == "value":
        part_idx = 1
    elif suffix.startswith("part"):
        try:
            part_idx = int(suffix[4:])
        except ValueError:
            return False
    else:
        return False
    part_rule = rule.parts.get(part_idx)
    if part_rule and part_rule.kind in {"categorical", "quality"}:
        return True
    return False


def get_agg_func(col: str) -> str:
    """Return the preferred aggregation function name for *col*.

    Returns one of: ``"mean"``, ``"max"``, ``"min"``, ``"mode"``,
    ``"sum"``, ``"drop"``, ``"circular_mean"``.  Defaults to ``"mean"`` for columns that
    have no explicit rule.
    """
    if is_quality_column(col):
        return "drop"
    parsed = _parse_expanded_col(to_internal_column(col))
    if parsed is None:
        return "mean"
    field_prefix, suffix = parsed
    rule = get_field_rule(field_prefix)
    if rule is None:
        return "mean"
    if suffix == "value":
        part_idx = 1
    elif suffix.startswith("part"):
        try:
            part_idx = int(suffix[4:])
        except ValueError:
            return "mean"
    else:
        return "mean"
    part_rule = rule.parts.get(part_idx)
    if part_rule:
        return part_rule.agg
    return "mean"
