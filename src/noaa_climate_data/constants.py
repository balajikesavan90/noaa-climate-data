"""Shared constants for NOAA ISD Global Hourly data."""

from __future__ import annotations

BASE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access"

QUALITY_FLAGS = {
    "0",
    "1",
    "4",
    "5",
    "9",
    "A",
    "C",
    "I",
    "M",
    "P",
    "R",
    "U",
}

DEFAULT_START_YEAR = 2000
DEFAULT_END_YEAR = 2019
