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

### Station metadata (Stations.csv)

- `Stations.csv`: station metadata with year coverage and derived flags.

#### Command:

- `poetry run python -m noaa_climate_data.cli location-ids --start-year 1975 --end-year 2025 --sleep-seconds 0.5 --retries 3 --backoff-base 0.5 --backoff-max 8`

#### Behavior:
- Reads `DataFileList_YEARCOUNT.csv` to identify stations with coverage in the selected year range.
- Fetches NOAA station metadata and joins it to the file list.
- Computes coverage fields (`No_Of_Years`, `FIRST_YEAR`, `LAST_YEAR`, `YEAR_COUNT`).
- Marks completeness via `METADATA_COMPLETE` and writes `Stations.csv`.

#### Notes
- Creation started on 2026-02-07.
- Metadata collection for all 27k stations completed on 2026-02-12.
- **2026-02-21**: Internet outage on 2026-02-20 caused data loss during a `location-ids` run. The resume logic loaded 23,738 stations but failed to fetch metadata for the remaining 3,748 stations (stations with IDs in the 725xxxxx range). The process wrote Stations.csv with only the successfully loaded rows, losing 13.6% of station metadata. Recovery performed on 2026-02-21 using `recover_missing_stations.py` to fetch and append the missing station metadata.

### Raw data pulls (cron)

#### Outputs:

- `output/<station_id>/LocationData_Raw.parquet`: raw NOAA data per station.
- `Stations.csv`: `raw_data_pulled` is updated to `True` after a successful write.

#### Command:

- `poetry run python -m noaa_climate_data.cli pick-location --start-year 1975 --end-year 2025 --sleep-seconds 0.5 --output-dir /media/balaji-kesavan/LaCie/NOAA_Data`

#### Behavior:
- Picks a random station with `raw_data_pulled=False`.
- Downloads yearly NOAA CSVs with 0.5s delay between requests.
- Writes `LocationData_Raw.parquet` to the external output directory.
- Marks the station as `raw_data_pulled=True` on success.

#### Notes
- Cron schedule runs every 5 minutes.
- Schedule started on 2026-02-13.

### Data cleaning (placeholder)

#### Outputs:

- `output/<station_id>/LocationData_Cleaned.parquet`: cleaned station data.
- `Stations.csv`: `data_cleaned` is updated to `True` after a successful write.

#### Command:

- Placeholder (cleaning CLI entrypoint not yet implemented).

#### Behavior:
- Picks a random station with `raw_data_pulled=True` and `data_cleaned=False`.
- Cleans the raw parquet and writes `LocationData_Cleaned.parquet`.
- Marks the station as `data_cleaned=True` on success.

#### Notes
- Placeholder only; cleaning pipeline is not yet wired for cron.

### Data aggregation (placeholder)

#### Outputs:

- Aggregated parquet outputs (to be defined).
- `Stations.csv`: `data_aggregated` is updated to `True` after a successful write.

#### Command:

- Placeholder (aggregation CLI entrypoint not yet implemented).

#### Behavior:
- Picks a random station with `raw_data_pulled=True`, `data_cleaned=True`, and
	`data_aggregated=False`.
- Aggregates the cleaned parquet into summary outputs.
- Marks the station as `data_aggregated=True` on success.

#### Notes
- Placeholder only; aggregation pipeline is not yet wired for cron.

