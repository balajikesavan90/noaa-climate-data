"""End-to-end pipeline helpers for NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Literal
import time

import pandas as pd

from .cleaning import clean_noaa_dataframe
from .constants import DEFAULT_END_YEAR, DEFAULT_START_YEAR
from .noaa_client import (
    StationMetadata,
    build_file_list,
    count_years_per_file,
    fetch_station_metadata,
    fetch_station_metadata_for_years,
    get_years,
    normalize_station_file_name,
    url_for,
)


@dataclass(frozen=True)
class LocationDataOutputs:
    raw: pd.DataFrame
    cleaned: pd.DataFrame
    hourly: pd.DataFrame
    monthly: pd.DataFrame
    yearly: pd.DataFrame


AggregationStrategy = Literal[
    "best_hour",
    "fixed_hour",
    "hour_day_month_year",
    "weighted_hours",
    "daily_min_max_mean",
]


def build_data_file_list(
    output_csv: Path,
    sleep_seconds: float = 0.0,
    retries: int = 3,
    backoff_base: float = 0.5,
    backoff_max: float = 8.0,
) -> pd.DataFrame:
    years = get_years(
        retries=retries,
        backoff_base=backoff_base,
        backoff_max=backoff_max,
    )
    file_list = build_file_list(
        years,
        sleep_seconds=sleep_seconds,
        retries=retries,
        backoff_base=backoff_base,
        backoff_max=backoff_max,
    )
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
    metadata_years: Iterable[int],
    include_legacy_id: bool = True,
    resume: bool = True,
    start_index: int = 0,
    max_locations: int | None = None,
    checkpoint_every: int = 100,
    checkpoint_dir: Path | None = None,
    sleep_seconds: float = 0.0,
    retries: int = 3,
    backoff_base: float = 0.5,
    backoff_max: float = 8.0,
) -> pd.DataFrame:
    full_coverage = year_counts
    rows: list[dict[str, object]] = []
    processed: set[str] = set()
    total = len(full_coverage)
    if resume and output_csv.exists():
        existing = pd.read_csv(output_csv)
        if not existing.empty:
            rows = existing.to_dict(orient="records")
            processed = set(existing["FileName"].dropna().astype(str))
            print(
                f"Resuming Stations.csv: {len(rows)} rows already written; "
                f"{len(processed)} stations will be skipped."
            )
    metadata_years = list(metadata_years)
    if not metadata_years:
        raise ValueError("metadata_years must contain at least one year")
    if checkpoint_every is not None and checkpoint_every <= 0:
        raise ValueError("checkpoint_every must be positive")
    if start_index < 0:
        raise ValueError("start_index must be >= 0")

    new_count = 0
    print(
        f"Starting metadata fetch for {total} stations "
        f"(start_index={start_index}, max_locations={max_locations})."
    )
    for idx, file_name in enumerate(full_coverage["FileName"], start=1):
        if idx <= start_index:
            continue
        if max_locations is not None and new_count >= max_locations:
            break
        if file_name in processed:
            continue
        metadata, metadata_year = fetch_station_metadata_for_years(
            file_name,
            metadata_years,
            sleep_seconds=sleep_seconds,
            retries=retries,
            backoff_base=backoff_base,
            backoff_max=backoff_max,
        )
        if metadata is None or metadata_year is None:
            continue
        station_id = Path(normalize_station_file_name(metadata.file_name)).stem
        metadata_complete = all(
            value is not None
            for value in (
                metadata.latitude,
                metadata.longitude,
                metadata.elevation,
                metadata.name,
            )
        )
        row: dict[str, object] = {
            "ID": station_id,
            "FileName": metadata.file_name,
            "LATITUDE": metadata.latitude,
            "LONGITUDE": metadata.longitude,
            "ELEVATION": metadata.elevation,
            "NAME": metadata.name,
            "No_Of_Years": int(
                year_counts.loc[year_counts["FileName"] == file_name, "No_Of_Years"].iloc[0]
            ),
            "METADATA_YEAR": metadata_year,
            "METADATA_COMPLETE": metadata_complete,
        }
        if include_legacy_id:
            row["LegacyID"] = idx
        rows.append(
            row
        )
        processed.add(file_name)
        new_count += 1
        print(
            f"Fetched {file_name} (year={metadata_year}) -> "
            f"{len(rows)}/{total} total, {new_count} new."
        )
        if checkpoint_every and (len(rows) % checkpoint_every == 0):
            frame = pd.DataFrame(rows)
            frame.to_csv(output_csv, index=False)
            target_dir = checkpoint_dir or output_csv.parent
            checkpoint_path = target_dir / f"{output_csv.stem}_checkpoint_{len(rows):05d}.csv"
            frame.to_csv(checkpoint_path, index=False)
            print(
                f"Progress: {len(rows)}/{total} rows saved "
                f"(new this run: {new_count})."
            )
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)
    frame = pd.DataFrame(rows)
    frame.to_csv(output_csv, index=False)
    print(
        f"Finished metadata fetch. Total rows: {len(rows)} "
        f"(new this run: {new_count})."
    )
    return frame


def download_location_data(
    file_name: str,
    years: Iterable[int],
    sleep_seconds: float = 0.0,
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
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)
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


def _filter_full_years(df: pd.DataFrame, min_months: int = 12) -> pd.DataFrame:
    months = df.groupby("Year")["MonthNum"].nunique().reset_index(name="months")
    full = months[months["months"] >= min_months]
    return df[df["Year"].isin(full["Year"])]


def _coerce_numeric(
    df: pd.DataFrame,
    group_cols: list[str],
) -> tuple[pd.DataFrame, list[str]]:
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
    return work, numeric_cols


def _aggregate_numeric(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    work, numeric_cols = _coerce_numeric(df, group_cols)
    if not numeric_cols:
        return work[group_cols].drop_duplicates()
    agg = work.groupby(group_cols)[numeric_cols].mean().reset_index()
    return agg


def _weighted_aggregate(
    df: pd.DataFrame,
    group_cols: list[str],
    weight_col: str,
) -> pd.DataFrame:
    work, numeric_cols = _coerce_numeric(df, group_cols + [weight_col])
    if not numeric_cols:
        return work[group_cols].drop_duplicates()

    group = work.groupby(group_cols)
    weight_sum = group[weight_col].sum()
    data: dict[str, pd.Series] = {}
    for col in numeric_cols:
        weighted_sum = (work[col] * work[weight_col]).groupby(group_cols).sum()
        data[col] = weighted_sum / weight_sum
    return pd.DataFrame(data).reset_index()


def _daily_min_max_mean(
    df: pd.DataFrame,
    group_cols: list[str],
) -> pd.DataFrame:
    work, numeric_cols = _coerce_numeric(df, group_cols)
    if not numeric_cols:
        return work[group_cols].drop_duplicates()
    group = work.groupby(group_cols)
    frames: list[pd.Series] = []
    for col in numeric_cols:
        frames.append(group[col].min().rename(f"{col}__daily_min"))
        frames.append(group[col].max().rename(f"{col}__daily_max"))
        frames.append(group[col].mean().rename(f"{col}__daily_mean"))
    return pd.concat(frames, axis=1).reset_index()


def process_location(
    file_name: str,
    years: Iterable[int],
    location_id: int | None = None,
    aggregation_strategy: AggregationStrategy = "best_hour",
    min_hours_per_day: int = 18,
    min_days_per_month: int = 20,
    min_months_per_year: int = 12,
    fixed_hour: int | None = None,
    sleep_seconds: float = 0.0,
) -> LocationDataOutputs:
    raw = download_location_data(file_name, years, sleep_seconds=sleep_seconds)
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

    month_group = ["Year", "MonthNum"]
    year_group = ["Year"]
    if "ID" in cleaned.columns:
        month_group = ["ID"] + month_group
        year_group = ["ID"] + year_group

    if aggregation_strategy == "best_hour":
        hourly = cleaned
        best_hour = _best_hour(hourly)
        if best_hour is not None:
            hourly = hourly[hourly["Hour"] == best_hour]
        hourly = _filter_full_months(hourly, min_days=min_days_per_month)
        hourly = _filter_full_years(hourly, min_months=min_months_per_year)
        monthly = _aggregate_numeric(hourly, month_group)
        yearly = _aggregate_numeric(hourly, year_group)
    elif aggregation_strategy == "fixed_hour":
        if fixed_hour is None:
            raise ValueError("fixed_hour must be provided for fixed_hour strategy")
        hourly = cleaned[cleaned["Hour"] == fixed_hour]
        hourly = _filter_full_months(hourly, min_days=min_days_per_month)
        hourly = _filter_full_years(hourly, min_months=min_months_per_year)
        monthly = _aggregate_numeric(hourly, month_group)
        yearly = _aggregate_numeric(hourly, year_group)
    elif aggregation_strategy == "hour_day_month_year":
        hour_group = ["Year", "MonthNum", "Day", "Hour"]
        day_group = ["Year", "MonthNum", "Day"]
        if "ID" in cleaned.columns:
            hour_group = ["ID"] + hour_group
            day_group = ["ID"] + day_group
        hourly = _aggregate_numeric(cleaned, hour_group)
        daily = _aggregate_numeric(hourly, day_group)
        daily = _filter_full_months(daily, min_days=min_days_per_month)
        daily = _filter_full_years(daily, min_months=min_months_per_year)
        valid_months = daily[["Year", "MonthNum"]].drop_duplicates()
        hourly = hourly.merge(valid_months, on=["Year", "MonthNum"], how="inner")
        hourly = hourly[hourly["Year"].isin(daily["Year"].unique())]
        monthly = _aggregate_numeric(daily, month_group)
        yearly = _aggregate_numeric(daily, year_group)
    elif aggregation_strategy == "weighted_hours":
        hour_group = ["Year", "MonthNum", "Day", "Hour"]
        day_group = ["Year", "MonthNum", "Day"]
        if "ID" in cleaned.columns:
            hour_group = ["ID"] + hour_group
            day_group = ["ID"] + day_group
        hourly = _aggregate_numeric(cleaned, hour_group)
        hours_per_day = (
            hourly.groupby(day_group)["Hour"].nunique().reset_index(name="hours")
        )
        hours_per_day = hours_per_day[hours_per_day["hours"] >= min_hours_per_day]
        daily = _aggregate_numeric(hourly, day_group)
        daily = daily.merge(hours_per_day, on=day_group, how="inner")
        daily = _filter_full_months(daily, min_days=min_days_per_month)
        daily = _filter_full_years(daily, min_months=min_months_per_year)
        valid_days = daily[day_group].drop_duplicates()
        hourly = hourly.merge(valid_days, on=day_group, how="inner")
        monthly = _weighted_aggregate(daily, month_group, "hours")
        yearly = _weighted_aggregate(daily, year_group, "hours")
    elif aggregation_strategy == "daily_min_max_mean":
        hour_group = ["Year", "MonthNum", "Day", "Hour"]
        day_group = ["Year", "MonthNum", "Day"]
        if "ID" in cleaned.columns:
            hour_group = ["ID"] + hour_group
            day_group = ["ID"] + day_group
        hourly = _aggregate_numeric(cleaned, hour_group)
        daily = _daily_min_max_mean(hourly, day_group)
        daily = _filter_full_months(daily, min_days=min_days_per_month)
        daily = _filter_full_years(daily, min_months=min_months_per_year)
        valid_days = daily[day_group].drop_duplicates()
        hourly = hourly.merge(valid_days, on=day_group, how="inner")
        monthly = _aggregate_numeric(daily, month_group)
        yearly = _aggregate_numeric(daily, year_group)
    else:
        raise ValueError(f"Unknown aggregation strategy: {aggregation_strategy}")

    return LocationDataOutputs(
        raw=raw,
        cleaned=cleaned,
        hourly=hourly,
        monthly=monthly,
        yearly=yearly,
    )
