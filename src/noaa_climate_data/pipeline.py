"""End-to-end pipeline helpers for NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd

from .cleaning import clean_noaa_dataframe
from .constants import DEFAULT_END_YEAR, DEFAULT_START_YEAR
from .noaa_client import (
    StationMetadata,
    build_file_list,
    count_years_per_file,
    fetch_station_metadata,
    get_years,
    url_for,
)


@dataclass(frozen=True)
class LocationDataOutputs:
    raw: pd.DataFrame
    cleaned: pd.DataFrame
    hourly: pd.DataFrame
    monthly: pd.DataFrame
    yearly: pd.DataFrame


def build_data_file_list(output_csv: Path) -> pd.DataFrame:
    years = get_years()
    file_list = build_file_list(years)
    file_list.to_csv(output_csv, index=False)
    return file_list


def build_year_counts(
    file_list: pd.DataFrame,
    output_csv: Path,
    start_year: int = DEFAULT_START_YEAR,
    end_year: int = DEFAULT_END_YEAR,
) -> pd.DataFrame:
    counts = count_years_per_file(file_list, start_year, end_year)
    counts.to_csv(output_csv, index=False)
    return counts


def build_location_ids(
    year_counts: pd.DataFrame,
    output_csv: Path,
    year_for_metadata: int = DEFAULT_START_YEAR,
    expected_years: int | None = None,
) -> pd.DataFrame:
    if expected_years is None:
        expected_years = DEFAULT_END_YEAR - DEFAULT_START_YEAR + 1
    full_coverage = year_counts[year_counts["No_Of_Years"] == expected_years]
    rows: list[dict[str, object]] = []
    for idx, file_name in enumerate(full_coverage["FileName"], start=1):
        metadata = fetch_station_metadata(file_name, year_for_metadata)
        if metadata is None:
            continue
        rows.append(
            {
                "ID": idx,
                "FileName": metadata.file_name,
                "LATITUDE": metadata.latitude,
                "LONGITUDE": metadata.longitude,
                "ELEVATION": metadata.elevation,
                "NAME": metadata.name,
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(output_csv, index=False)
    return frame


def download_location_data(
    file_name: str,
    years: Iterable[int],
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for year in years:
        url = url_for(year, file_name)
        try:
            frame = pd.read_csv(url, dtype=str, low_memory=False)
        except Exception:
            continue
        if not frame.empty:
            frame["YEAR"] = year
            frames.append(frame)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def _extract_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce", utc=True)
    df = df.dropna(subset=["DATE"])
    df["Year"] = df["DATE"].dt.year
    df["MonthNum"] = df["DATE"].dt.month
    df["Day"] = df["DATE"].dt.date
    df["Hour"] = df["DATE"].dt.hour
    return df


def _best_hour(df: pd.DataFrame) -> int | None:
    if df.empty:
        return None
    counts = df.groupby("Hour")["Day"].nunique().sort_values(ascending=False)
    if counts.empty:
        return None
    return int(counts.index[0])


def _filter_full_months(df: pd.DataFrame, min_days: int = 20) -> pd.DataFrame:
    days = df.groupby(["Year", "MonthNum"])['Day'].nunique().reset_index(name="days")
    full = days[days["days"] >= min_days]
    return df.merge(full[["Year", "MonthNum"]], on=["Year", "MonthNum"], how="inner")


def _filter_full_years(df: pd.DataFrame) -> pd.DataFrame:
    months = df.groupby("Year")["MonthNum"].nunique().reset_index(name="months")
    full = months[months["months"] == 12]
    return df[df["Year"].isin(full["Year"])]


def _aggregate_numeric(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    work = df.copy()
    numeric_cols = set(work.select_dtypes(include=["number"]).columns)
    candidates = [col for col in work.columns if col not in group_cols]

    for col in candidates:
        if col in numeric_cols:
            continue
        if work[col].dtype == "object":
            converted = pd.to_numeric(work[col], errors="coerce")
            if converted.notna().any():
                work[col] = converted
                numeric_cols.add(col)

    numeric_cols = [col for col in numeric_cols if col not in group_cols]
    if not numeric_cols:
        return work[group_cols].drop_duplicates()
    agg = work.groupby(group_cols)[numeric_cols].mean().reset_index()
    return agg


def process_location(
    file_name: str,
    years: Iterable[int],
    location_id: int | None = None,
) -> LocationDataOutputs:
    raw = download_location_data(file_name, years)
    if raw.empty:
        return LocationDataOutputs(
            raw=raw,
            cleaned=raw,
            hourly=raw,
            monthly=raw,
            yearly=raw,
        )

    cleaned = clean_noaa_dataframe(raw, keep_raw=True)
    cleaned = _extract_time_columns(cleaned)
    if location_id is not None:
        cleaned["ID"] = location_id

    hourly = cleaned

    best_hour = _best_hour(hourly)
    if best_hour is not None:
        hourly = hourly[hourly["Hour"] == best_hour]

    hourly = _filter_full_months(hourly)
    hourly = _filter_full_years(hourly)

    month_group = ["Year", "MonthNum"]
    year_group = ["Year"]
    if "ID" in cleaned.columns:
        month_group = ["ID"] + month_group
        year_group = ["ID"] + year_group

    monthly = _aggregate_numeric(hourly, month_group)
    yearly = _aggregate_numeric(hourly, year_group)

    return LocationDataOutputs(
        raw=raw,
        cleaned=cleaned,
        hourly=hourly,
        monthly=monthly,
        yearly=yearly,
    )
