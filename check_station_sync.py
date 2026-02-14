"""Check Stations.csv raw_data_pulled status against parquet outputs."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd


STATUS_COLUMN = "raw_data_pulled"
DEFAULT_OUTPUT_DIR = Path("/media/balaji-kesavan/LaCie/NOAA_Data")


def _latest_index_dir(base_index_dir: Path) -> Path:
    if not base_index_dir.exists():
        raise FileNotFoundError("noaa_file_index folder not found")
    candidates = [
        path
        for path in base_index_dir.iterdir()
        if path.is_dir() and path.name.isdigit() and len(path.name) == 8
    ]
    if not candidates:
        raise FileNotFoundError("noaa_file_index has no dated subfolders")
    return sorted(candidates)[-1]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Stations.csv raw_data_pulled against parquet files"
    )
    parser.add_argument(
        "--stations-csv",
        type=Path,
        default=None,
        help="Path to Stations.csv (defaults to latest noaa_file_index folder)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Root directory containing station parquet outputs",
    )
    parser.add_argument(
        "--max-mismatches",
        type=int,
        default=25,
        help="Max mismatches to print per category (default 25)",
    )
    parser.add_argument(
        "--write-report",
        type=Path,
        default=None,
        help="Optional path to write a CSV report of mismatches",
    )
    return parser.parse_args()


def _station_dir(output_dir: Path, file_name: str) -> Path:
    station_id = Path(file_name).stem
    return output_dir / station_id


def _station_parquet_path(output_dir: Path, file_name: str) -> Path:
    return _station_dir(output_dir, file_name) / "LocationData_Raw.parquet"


def main() -> None:
    args = _parse_args()
    base_index_dir = Path("noaa_file_index")
    stations_csv = args.stations_csv
    if stations_csv is None:
        stations_csv = _latest_index_dir(base_index_dir) / "Stations.csv"

    frame = pd.read_csv(stations_csv)
    if STATUS_COLUMN not in frame.columns:
        raise ValueError(f"Stations.csv missing {STATUS_COLUMN} column")

    expected_true = frame[frame[STATUS_COLUMN] == True]  # noqa: E712
    expected_false = frame[frame[STATUS_COLUMN] == False]  # noqa: E712

    missing_files: list[dict[str, object]] = []
    unexpected_files: list[dict[str, object]] = []

    for _, row in expected_true.iterrows():
        file_name = str(row["FileName"])
        parquet_path = _station_parquet_path(args.output_dir, file_name)
        if not parquet_path.exists():
            missing_files.append(
                {
                    "FileName": file_name,
                    "Expected": True,
                    "ParquetPath": str(parquet_path),
                }
            )

    for _, row in expected_false.iterrows():
        file_name = str(row["FileName"])
        parquet_path = _station_parquet_path(args.output_dir, file_name)
        if parquet_path.exists():
            unexpected_files.append(
                {
                    "FileName": file_name,
                    "Expected": False,
                    "ParquetPath": str(parquet_path),
                }
            )

    total = len(frame)
    print(f"Stations.csv: {stations_csv}")
    print(f"Output dir: {args.output_dir}")
    print(f"Total stations: {total}")
    print(f"raw_data_pulled=True: {len(expected_true)}")
    print(f"raw_data_pulled=False: {len(expected_false)}")
    print(f"Missing parquet (should exist): {len(missing_files)}")
    print(f"Unexpected parquet (should not exist): {len(unexpected_files)}")

    def _print_rows(title: str, rows: list[dict[str, object]]) -> None:
        if not rows:
            return
        print("")
        print(title)
        limit = args.max_mismatches
        for item in rows[:limit]:
            print(f"- {item['FileName']} -> {item['ParquetPath']}")
        if len(rows) > limit:
            print(f"... ({len(rows) - limit} more)")

    _print_rows("Missing parquet files:", missing_files)
    _print_rows("Unexpected parquet files:", unexpected_files)

    if args.write_report is not None:
        report_rows = (
            [
                {
                    "Issue": "missing_parquet",
                    **row,
                }
                for row in missing_files
            ]
            + [
                {
                    "Issue": "unexpected_parquet",
                    **row,
                }
                for row in unexpected_files
            ]
        )
        report_path = args.write_report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(report_rows).to_csv(report_path, index=False)
        print(f"Report written: {report_path}")


if __name__ == "__main__":
    main()
