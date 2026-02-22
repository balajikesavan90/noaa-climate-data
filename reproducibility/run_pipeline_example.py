"""Run a small cleaning example for reproducibility artifacts."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from noaa_climate_data.cleaning import clean_noaa_dataframe


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    raw_path = repo_root / "reproducibility" / "sample_station_raw.txt"
    cleaned_path = repo_root / "reproducibility" / "sample_station_cleaned.csv"

    raw = pd.read_csv(raw_path)
    cleaned = clean_noaa_dataframe(raw, keep_raw=False, strict_mode=True)
    cleaned.to_csv(cleaned_path, index=False)


if __name__ == "__main__":
    main()
