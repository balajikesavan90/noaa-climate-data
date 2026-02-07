# noaa-climate-data
The application contains the pipeline to pull and clean climate from NOAA.

## Python rewrite
This project replaces the legacy R scripts with a Python pipeline that:
- Builds the NOAA Global Hourly file list and year coverage counts.
- Builds station metadata (location IDs) for stations with full year coverage.
- Downloads all available metrics for a station and cleans comma-encoded fields.
- Aggregates numeric metrics to monthly and yearly summaries.

### Install
```bash
poetry install
```

### Commands
Build the file list and coverage counts:
```bash
poetry run python -m noaa_climate_data.cli file-list \
	--output DataFileList.csv \
	--counts-output DataFileList_YEARCOUNT_POST2000.csv \
	--start-year 2000 \
	--end-year 2019
```

Build station metadata (location IDs):
```bash
poetry run python -m noaa_climate_data.cli location-ids \
	--counts-input DataFileList_YEARCOUNT_POST2000.csv \
	--output IDData.csv \
	--metadata-year 2000 \
	--start-year 2000 \
	--end-year 2019
```

Download, clean, and aggregate a station:
```bash
poetry run python -m noaa_climate_data.cli process-location 01001099999.csv \
	--start-year 2000 \
	--end-year 2019 \
	--output-dir output
```

This writes:
- LocationData_Raw.csv
- LocationData_Cleaned.csv
- LocationData_Hourly.csv
- LocationData_Monthly.csv
- LocationData_Yearly.csv

## Data pipeline details

### 1) How the data is pulled
The pipeline targets NOAA’s Global Hourly CSV archive at the base URL in
[src/noaa_climate_data/constants.py](src/noaa_climate_data/constants.py).

**File list discovery**
- `get_years()` scrapes the NOAA access page, keeping only 4‑digit directory names.
- `get_file_list_for_year(year)` scrapes each year directory and retains only `.csv` entries.
- `build_file_list(years)` produces `YEAR` + `FileName` rows for all available year directories.

**Station coverage selection**
- `count_years_per_file(...)` filters file list by the requested year range and counts how many
	years each file appears.
- `build_location_ids(...)` keeps stations with *full coverage* across the requested window
	(`No_Of_Years == expected_years`).
- For each full‑coverage file, `fetch_station_metadata(...)` reads the first row from the CSV for
	latitude/longitude/elevation/name.

**Download for a station**
- `download_location_data(file_name, years)` attempts `pandas.read_csv(url)` for each year.
- A year is skipped if the read fails or is empty.
- Each non‑empty year frame is tagged with a `YEAR` column and concatenated.

Assumptions:
- NOAA HTML listings are stable enough for `pandas.read_html` parsing.
- A station file is considered available if the CSV is readable; otherwise it is skipped.
- Metadata is sourced from the first available row of the station CSV.

### 2) How it is cleaned (all assumptions for all metrics)
Cleaning is performed by `clean_noaa_dataframe(...)` in
[src/noaa_climate_data/cleaning.py](src/noaa_climate_data/cleaning.py).

**What gets parsed**
- Only object/string columns are candidates.
- A column is parsed if any sampled value contains a comma.
- Values are split on commas into parts (e.g., `value,quality` or longer compound fields).

**Missing value rules (applies to all metrics)**
- Empty strings become `None`.
- Numeric “all‑9s” encodings are treated as missing, e.g. `99`, `999`, `9999`, `+9999`, `-9999`.
- A leading `+` is removed before numeric conversion.

**Quality filtering (applies to all metrics with a quality code)**
- Allowed quality flags are in `QUALITY_FLAGS`:
	`{0,1,4,5,9,A,C,I,M,P,R,U}`.
- If a `value,quality` pair has a quality flag *not* in the allowed list, the value becomes `None`.
- For multi‑part fields with a quality flag, the first part is set to `None` when the quality is
	invalid; other parts are preserved.

**Metric‑specific scaling assumptions**
For fields that NOAA encodes with scale factors, the following are applied when the first part is
parsed as a numeric value:
- `TMP` (air temperature): multiplied by `0.1`.
- `DEW` (dew point): multiplied by `0.1`.
- `SLP` (sea level pressure): multiplied by `0.1`.

**Column expansion behavior**
- If a field parses into exactly two parts, output columns are:
	- `<column>__value` (numeric after quality filtering and scaling, if applicable)
	- `<column>__quality` (the quality flag, if present)
- If a field parses into more than two parts, output columns are:
	- `<column>__partN` for each part (numeric if parseable, otherwise raw text)
	- `<column>__quality` if a 1‑character quality flag exists
- By default, the original raw column is preserved (`keep_raw=True`).

### 3) How it is prepared
Preparation happens in `process_location(...)` in
[src/noaa_climate_data/pipeline.py](src/noaa_climate_data/pipeline.py).

**Time extraction**
- `DATE` is parsed as UTC; rows with invalid dates are dropped.
- Derived columns are added:
	- `Year`, `MonthNum`, `Day` (date only), and `Hour`.

**Best‑hour selection**
- The “best hour” is the hour with the most unique `Day` values.
- Only rows for that hour are kept before aggregation.

**Completeness filters**
- A month is considered complete if it has at least 20 unique days.
- A year is considered complete if it has all 12 months present after the month filter.

**Aggregation rules**
- Numeric columns are averaged within each group.
- Non‑numeric columns are coerced to numeric when possible; if any values convert, the column is
	treated as numeric for aggregation.
- Monthly grouping keys: `Year`, `MonthNum` (and `ID` if provided).
- Yearly grouping keys: `Year` (and `ID` if provided).

Assumptions:
- Aggregation uses mean for all numeric metrics, regardless of unit or distribution.
- Only data from the “best hour” is retained for monthly/yearly summaries.
- Monthly summaries represent months with at least 20 days; yearly summaries represent years with
	12 complete months.

### 4) How it is stored
All outputs are CSV files written by the CLI in
[src/noaa_climate_data/cli.py](src/noaa_climate_data/cli.py).

For a station processed with `process-location`, the following files are created in the chosen
output directory:
- `LocationData_Raw.csv`: concatenated raw yearly CSVs with an added `YEAR` column.
- `LocationData_Cleaned.csv`: cleaned/expanded fields plus derived time columns.
- `LocationData_Hourly.csv`: cleaned data filtered to the “best hour” and complete months/years.
- `LocationData_Monthly.csv`: monthly averages across numeric metrics.
- `LocationData_Yearly.csv`: yearly averages across numeric metrics.

Station metadata outputs:
- `DataFileList.csv`: available NOAA CSV files by year.
- `DataFileList_YEARCOUNT_POST2000.csv`: year coverage counts for each file.
- `IDData.csv`: station metadata for full‑coverage stations.
