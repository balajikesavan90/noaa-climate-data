"""Utilities for listing and downloading NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd
import requests

from .constants import BASE_URL


@dataclass(frozen=True)
class StationMetadata:
    latitude: float | None
    longitude: float | None
    elevation: float | None
    name: str | None
    file_name: str


def _normalize_year_dir(text: str) -> str | None:
    text = text.strip()
    if not text.endswith("/"):
        return None
    year = text[:-1]
    if not year.isdigit():
        return None
    if len(year) != 4:
        return None
    return year


def get_years() -> list[str]:
    """Fetch available year directories from NOAA access page."""
    tables = pd.read_html(BASE_URL + "/")
    if not tables:
        return []
    year_cells = tables[0].iloc[:, 0].astype(str).tolist()
    years = [
        year
        for cell in year_cells
        if (year := _normalize_year_dir(cell)) is not None
    ]
    return sorted(set(years))


def get_file_list_for_year(year: str) -> list[str]:
    """Fetch available CSV filenames for a given year directory."""
    url = f"{BASE_URL}/{year}/"
    tables = pd.read_html(url)
    if not tables:
        return []
    entries = tables[0].iloc[:, 0].astype(str).tolist()
    return [entry for entry in entries if entry.endswith(".csv")]


def build_file_list(years: Iterable[str]) -> pd.DataFrame:
    """Build a dataframe with YEAR and FileName columns."""
    frames: list[pd.DataFrame] = []
    for year in years:
        files = get_file_list_for_year(year)
        if not files:
            continue
        frames.append(pd.DataFrame({"YEAR": year, "FileName": files}))
    if not frames:
        return pd.DataFrame(columns=["YEAR", "FileName"])
    return pd.concat(frames, ignore_index=True)


def count_years_per_file(
    file_list: pd.DataFrame,
    start_year: int,
    end_year: int,
) -> pd.DataFrame:
    """Count occurrences per file within the given year range."""
    filtered = file_list[
        (file_list["YEAR"].astype(int) >= start_year)
        & (file_list["YEAR"].astype(int) <= end_year)
    ]
    counts = (
        filtered.groupby("FileName", as_index=False)["YEAR"]
        .count()
        .rename(columns={"YEAR": "No_Of_Years"})
    )
    return counts


def url_for(year: int | str, file_name: str) -> str:
    return f"{BASE_URL}/{year}/{file_name}"


def _url_exists(url: str, timeout: int = 20) -> bool:
    try:
        response = requests.head(url, timeout=timeout)
    except requests.RequestException:
        return False
    return response.status_code == 200


def fetch_station_metadata(file_name: str, year: int) -> StationMetadata | None:
    """Fetch station metadata by reading the first row of a CSV file."""
    url = url_for(year, file_name)
    if not _url_exists(url):
        return None
    try:
        frame = pd.read_csv(url, nrows=1, dtype=str, low_memory=False)
    except Exception:
        return None
    if frame.empty:
        return None
    row = frame.iloc[0]
    def _to_float(value: object) -> float | None:
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    return StationMetadata(
        latitude=_to_float(row.get("LATITUDE")),
        longitude=_to_float(row.get("LONGITUDE")),
        elevation=_to_float(row.get("ELEVATION")),
        name=str(row.get("NAME")) if row.get("NAME") is not None else None,
        file_name=file_name,
    )
