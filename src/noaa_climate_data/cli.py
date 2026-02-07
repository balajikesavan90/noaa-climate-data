"""Command-line interface for NOAA climate data pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .constants import DEFAULT_END_YEAR, DEFAULT_START_YEAR
from .pipeline import (
    build_data_file_list,
    build_location_ids,
    build_year_counts,
    process_location,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="NOAA Global Hourly pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    file_list_parser = subparsers.add_parser("file-list", help="Build NOAA file list")
    file_list_parser.add_argument(
        "--output",
        type=Path,
        default=Path("DataFileList.csv"),
        help="Output CSV path",
    )
    file_list_parser.add_argument(
        "--counts-output",
        type=Path,
        default=Path("DataFileList_YEARCOUNT_POST2000.csv"),
        help="Output CSV path for year counts",
    )
    file_list_parser.add_argument(
        "--start-year",
        type=int,
        default=DEFAULT_START_YEAR,
    )
    file_list_parser.add_argument(
        "--end-year",
        type=int,
        default=DEFAULT_END_YEAR,
    )

    location_parser = subparsers.add_parser(
        "location-ids", help="Build station metadata list"
    )
    location_parser.add_argument(
        "--counts-input",
        type=Path,
        default=Path("DataFileList_YEARCOUNT_POST2000.csv"),
        help="Input year count CSV",
    )
    location_parser.add_argument(
        "--output",
        type=Path,
        default=Path("IDData.csv"),
        help="Output CSV path",
    )
    location_parser.add_argument(
        "--metadata-year",
        type=int,
        default=DEFAULT_START_YEAR,
    )
    location_parser.add_argument(
        "--start-year",
        type=int,
        default=DEFAULT_START_YEAR,
    )
    location_parser.add_argument(
        "--end-year",
        type=int,
        default=DEFAULT_END_YEAR,
    )

    process_parser = subparsers.add_parser(
        "process-location", help="Download and clean a station's data"
    )
    process_parser.add_argument("file_name", help="Station file name (.csv)")
    process_parser.add_argument(
        "--start-year",
        type=int,
        default=DEFAULT_START_YEAR,
    )
    process_parser.add_argument(
        "--end-year",
        type=int,
        default=DEFAULT_END_YEAR,
    )
    process_parser.add_argument("--location-id", type=int, default=None)
    process_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    if args.command == "file-list":
        file_list = build_data_file_list(args.output)
        build_year_counts(file_list, args.counts_output, args.start_year, args.end_year)
        return

    if args.command == "location-ids":
        year_counts = args.counts_input
        if year_counts.exists():
            counts = pd.read_csv(year_counts)
        else:
            raise FileNotFoundError(f"Missing {year_counts}")
        expected_years = args.end_year - args.start_year + 1
        build_location_ids(counts, args.output, args.metadata_year, expected_years)
        return

    if args.command == "process-location":
        output_dir: Path = args.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        years = range(args.start_year, args.end_year + 1)
        outputs = process_location(args.file_name, years, args.location_id)

        outputs.raw.to_csv(output_dir / "LocationData_Raw.csv", index=False)
        outputs.cleaned.to_csv(output_dir / "LocationData_Cleaned.csv", index=False)
        outputs.hourly.to_csv(output_dir / "LocationData_Hourly.csv", index=False)
        outputs.monthly.to_csv(output_dir / "LocationData_Monthly.csv", index=False)
        outputs.yearly.to_csv(output_dir / "LocationData_Yearly.csv", index=False)
        return


if __name__ == "__main__":
    main()
