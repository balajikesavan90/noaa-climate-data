# NOAA file index (2026-02-07)

This folder contains the NOAA Global Hourly file index and year-counts used by the pipeline.

## How it was generated

Command:

- `poetry run python -m noaa_climate_data.cli file-list --start-year 1975 --end-year 2025 --sleep-seconds 0.5 --retries 3 --backoff-base 0.5 --backoff-max 8`

Behavior:
- Scrapes the NOAA Global Hourly directory listing for available year folders.
- For each year, scrapes the list of `.csv` files.
- Builds a file list (`DataFileList.csv`) with `YEAR` + `FileName`.
- Aggregates year counts per file into `DataFileList_YEARCOUNT.csv`.
- Uses retries with exponential backoff and a 0.5s delay between year requests.

## Outputs

- `DataFileList.csv`: all available file names by year in the 1975–2025 range.
- `DataFileList_YEARCOUNT.csv`: number of years each file appears in within 1975–2025.

## Notes

- Output folder naming uses UTC date (`YYYYMMDD`).
- This index does not download station data; it only lists available files.
