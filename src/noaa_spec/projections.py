"""Optional domain projections for cleaned NOAA-Spec output."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Dict

import pandas as pd


IDENTITY_COLUMNS = (
    "STATION",
    "DATE",
    "SOURCE",
    "REPORT_TYPE",
    "CALL_SIGN",
    "QUALITY_CONTROL",
)

DOMAIN_COLUMNS: dict[str, tuple[str, ...]] = {
    "core_meteorology": (
        "temperature_c",
        "dew_point_c",
        "visibility_m",
        "wind_direction_deg",
        "wind_type_code",
        "wind_speed_ms",
        "ceiling_height_m",
        "sea_level_pressure_hpa",
    ),
    "wind": (
        "wind_direction_deg",
        "wind_direction_quality_code",
        "wind_type_code",
        "wind_speed_ms",
        "wind_speed_quality_code",
        "wind_direction_variable",
        "qc_calm_wind_detected",
    ),
    "visibility": (
        "visibility_m",
        "visibility_quality_code",
        "visibility_variability_code",
        "visibility_variability_quality_code",
        "ceiling_height_m",
        "ceiling_height_quality_code",
        "ceiling_determination_code",
        "ceiling_cavok_code",
    ),
    "pressure_temperature": (
        "temperature_c",
        "temperature_quality_code",
        "dew_point_c",
        "dew_point_quality_code",
        "sea_level_pressure_hpa",
        "sea_level_pressure_quality_code",
        "altimeter_setting_hpa",
        "altimeter_quality_code",
        "station_pressure_hpa",
        "station_pressure_quality_code",
    ),
    "clouds": (
        "ceiling_height_m",
        "ceiling_height_quality_code",
        "cloud_layer_coverage_1",
        "cloud_layer_base_height_m_1",
        "cloud_layer_type_code_1",
        "cloud_total_coverage",
        "cloud_lowest_coverage",
        "cloud_lowest_base_height_m",
    ),
    "precipitation": (
        "precip_period_hours_1",
        "precip_amount_1",
        "precip_condition_code_1",
        "precip_quality_code_1",
        "precip_period_hours_2",
        "precip_amount_2",
        "precip_condition_code_2",
        "precip_quality_code_2",
        "precip_period_hours_3",
        "precip_amount_3",
        "precip_condition_code_3",
        "precip_quality_code_3",
        "precip_period_hours_4",
        "precip_amount_4",
        "precip_condition_code_4",
        "precip_quality_code_4",
    ),
    "remarks": (
        "REM",
        "remarks_type_code",
        "remarks_text",
        "remarks_type_codes",
        "remarks_text_blocks_json",
    ),
}

QUALITY_STATUS_COLUMNS = (
    "row_has_any_usable_metric",
    "usable_metric_count",
    "usable_metric_fraction",
)


def project_domains(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Return optional domain views from an already-cleaned dataframe."""
    domains = {
        domain: _select_columns(df, columns)
        for domain, columns in DOMAIN_COLUMNS.items()
    }
    domains["quality_codes"] = _select_columns(
        df,
        _quality_columns(df),
    )
    return domains


def _select_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    selected = _present_columns(df, (*IDENTITY_COLUMNS, *tuple(columns)))
    return df.loc[:, selected].copy()


def _quality_columns(df: pd.DataFrame) -> tuple[str, ...]:
    return tuple(
        column
        for column in df.columns
        if column.endswith("_quality_code")
        or "__qc_" in column
        or column.startswith("qc_")
        or column in QUALITY_STATUS_COLUMNS
    )


def _present_columns(df: pd.DataFrame, columns: Iterable[str]) -> list[str]:
    present: list[str] = []
    seen: set[str] = set()
    for column in columns:
        if column in df.columns and column not in seen:
            present.append(column)
            seen.add(column)
    return present
