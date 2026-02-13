# NOAA file index (2026-02-07)

This folder contains the NOAA Global Hourly file index and year-counts used by the pipeline.

## How it was generated

### Pre Metadata

- `DataFileList.csv`: all available file names by year in the 1975–2025 range.
- `DataFileList_YEARCOUNT.csv`: number of years each file appears in within 1975–2025.

#### Command:

- `poetry run python -m noaa_climate_data.cli file-list --start-year 1975 --end-year 2025 --sleep-seconds 0.5 --retries 3 --backoff-base 0.5 --backoff-max 8`

#### Behavior:
- Scrapes the NOAA Global Hourly directory listing for available year folders.
- For each year, scrapes the list of `.csv` files.
- Builds a file list (`DataFileList.csv`) with `YEAR` + `FileName`.
- Aggregates year counts per file into `DataFileList_YEARCOUNT.csv`.
- Uses retries with exponential backoff and a 0.5s delay between year requests.

#### Notes
- Output folder naming uses UTC date (`YYYYMMDD`).
- This index does not download station data; it only lists available files.

## Station metadata (Stations.csv)

- `Stations.csv`: station metadata with year coverage and derived flags.

#### Command:

- `poetry run python -m noaa_climate_data.cli location-ids --start-year 1975 --end-year 2025 --sleep-seconds 0.5 --retries 3 --backoff-base 0.5 --backoff-max 8`

#### Behavior:
- Reads `DataFileList_YEARCOUNT.csv` to identify stations with coverage in the selected year range.
- Fetches NOAA station metadata and joins it to the file list.
- Computes coverage fields (`No_Of_Years`, `FIRST_YEAR`, `LAST_YEAR`, `YEAR_COUNT`).
- Marks completeness via `METADATA_COMPLETE` and writes `Stations.csv`.

#### Notes
Timeline:
- Creation started on 2026-02-07.
- Metadata collection for all 27k stations completed on 2026-02-12.

