#!/usr/bin/env python3
"""Split domain CSV files into station-specific CSV files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


DEMO_BASE_COLUMNS = (
    "station_id",
    "station_name",
    "DATE",
    "LATITUDE",
    "LONGITUDE",
    "ELEVATION",
    "Year",
    "MonthNum",
    "Day",
    "Hour",
    "row_has_any_usable_metric",
    "usable_metric_fraction",
)

DEMO_DOMAIN_COLUMNS: dict[str, tuple[str, ...]] = {
    "temperature": (
        "temperature_c",
        "extreme_temp_c_1",
        "extreme_temp_type_1",
        "extreme_temp_period_hours_1",
        "sea_surface_temperature_c",
        "TMP__qc_pass",
    ),
    "dew_point": (
        "dew_point_c",
        "DEW__qc_pass",
    ),
    "wind": (
        "wind_speed_ms",
        "wind_direction_deg",
        "wind_gust_ms",
        "wind_type_code",
        "WND__part4__qc_pass",
    ),
    "pressure": (
        "sea_level_pressure_hpa",
        "station_pressure_hpa",
        "altimeter_setting_hpa",
        "SLP__qc_pass",
    ),
    "visibility_ceiling": (
        "visibility_m",
        "ceiling_height_m",
        "ceiling_cavok_code",
        "VIS__part1__qc_pass",
        "CIG__part1__qc_pass",
    ),
    "precipitation": (
        "precip_amount_1",
        "precip_period_hours_1",
        "precip_amount_2",
        "precip_period_hours_2",
        "snow_accum_depth_cm_1",
        "AA1__part2__qc_pass",
        "AA2__part2__qc_pass",
    ),
    "cloud_solar": (
        "cloud_total_coverage",
        "cloud_opaque_coverage",
        "cloud_lowest_base_height_m",
        "cloud_layer_coverage_1",
        "cloud_layer_base_height_m_1",
        "convective_cloud_code",
    ),
    "weather_occurrence": (
        "present_weather_code_1",
        "automated_present_weather_code_1",
        "past_weather_condition_code_1",
        "past_weather_period_hours_1",
        "past_weather_condition_code_2",
        "past_weather_period_hours_2",
    ),
    "other": (
        "remarks_text",
        "wave_height_m",
        "wave_period_seconds",
        "swell_height_m",
        "swell_direction_deg",
        "sea_state_code",
    ),
}


BASE_METADATA_COLUMNS = {
    "station_id",
    "station_name",
    "STATION",
    "DATE",
    "YEAR",
    "SOURCE",
    "LATITUDE",
    "LONGITUDE",
    "ELEVATION",
    "NAME",
    "REPORT_TYPE",
    "CALL_SIGN",
    "QUALITY_CONTROL",
    "Year",
    "MonthNum",
    "MonthName",
    "Day",
    "Hour",
    "row_has_any_usable_metric",
    "usable_metric_count",
    "usable_metric_fraction",
}


def _sanitize_station_name(name: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", str(name).strip())
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "UNKNOWN_STATION"


def _parse_domain(file_path: Path) -> str:
    stem = file_path.stem
    if "__" in stem:
        return stem.split("__")[-1]
    return stem


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Split domain CSV files into per-station CSV files."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("output/high_profile_stations_domains"),
        help="Directory containing domain CSV files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output/high_profile_stations_domains_by_station"),
        help="Directory to write station-specific files",
    )
    parser.add_argument(
        "--chunksize",
        type=int,
        default=50000,
        help="Rows per read chunk",
    )
    parser.add_argument(
        "--profile",
        choices=("full", "demo"),
        default="full",
        help="Column profile: full keeps all columns, demo keeps a curated subset",
    )
    return parser


def _select_columns(columns: list[str], domain: str, profile: str) -> list[str]:
    if profile == "full":
        return columns

    desired = list(DEMO_BASE_COLUMNS) + list(DEMO_DOMAIN_COLUMNS.get(domain, ()))
    selected: list[str] = []
    for column in desired:
        if column in columns and column not in selected:
            selected.append(column)
    if not selected:
        return columns
    return selected


def _coerce_qc_pass(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False)
    truthy = {"true", "1", "yes", "y", "t"}
    return (
        series.fillna(False)
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(truthy)
    )


def _recompute_usability_columns(chunk: pd.DataFrame) -> pd.DataFrame:
    qc_pass_columns = [col for col in chunk.columns if col.endswith("__qc_pass")]

    if qc_pass_columns:
        qc_frame = pd.DataFrame(
            {col: _coerce_qc_pass(chunk[col]) for col in qc_pass_columns},
            index=chunk.index,
        )
        usable_metric_count = qc_frame.sum(axis=1).astype(int)
        total_metrics = len(qc_pass_columns)
        usable_metric_fraction = usable_metric_count / total_metrics
        row_has_any_usable_metric = usable_metric_count > 0
    else:
        metric_columns = [col for col in chunk.columns if col not in BASE_METADATA_COLUMNS]
        if metric_columns:
            usable_metric_count = chunk[metric_columns].notna().sum(axis=1).astype(int)
            total_metrics = len(metric_columns)
            usable_metric_fraction = usable_metric_count / total_metrics
            row_has_any_usable_metric = usable_metric_count > 0
        else:
            usable_metric_count = pd.Series(0, index=chunk.index, dtype="int64")
            usable_metric_fraction = pd.Series(0.0, index=chunk.index, dtype="float64")
            row_has_any_usable_metric = pd.Series(False, index=chunk.index, dtype="bool")

    if "row_has_any_usable_metric" in chunk.columns:
        chunk["row_has_any_usable_metric"] = row_has_any_usable_metric
    if "usable_metric_count" in chunk.columns:
        chunk["usable_metric_count"] = usable_metric_count
    if "usable_metric_fraction" in chunk.columns:
        chunk["usable_metric_fraction"] = usable_metric_fraction

    return chunk


def main() -> None:
    args = _build_parser().parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    domain_files = sorted(
        file_path
        for file_path in input_dir.glob("*.csv")
        if "manifest" not in file_path.name
    )
    if not domain_files:
        raise FileNotFoundError(f"No domain CSV files found in {input_dir}")

    first_write: dict[tuple[str, str], bool] = {}
    stats: dict[tuple[str, str], dict[str, object]] = {}

    for domain_file in domain_files:
        domain = _parse_domain(domain_file)
        print(f"Processing domain: {domain} ({domain_file.name})")

        for chunk in pd.read_csv(
            domain_file,
            chunksize=args.chunksize,
            low_memory=False,
            dtype={"station_id": "string", "station_name": "string"},
        ):
            if "station_name" not in chunk.columns:
                raise ValueError(
                    f"Missing required column 'station_name' in {domain_file}"
                )

            selected_columns = _select_columns(list(chunk.columns), domain, args.profile)
            chunk = chunk[selected_columns]
            chunk = _recompute_usability_columns(chunk)

            for station_name, station_chunk in chunk.groupby("station_name", dropna=False):
                station_value = (
                    "UNKNOWN_STATION"
                    if pd.isna(station_name)
                    else str(station_name)
                )
                station_slug = _sanitize_station_name(station_value)
                output_file = output_dir / f"{station_slug}__{domain}.csv"
                key = (station_slug, domain)

                write_mode = "w" if not first_write.get(key, False) else "a"
                write_header = not first_write.get(key, False)
                station_chunk.to_csv(
                    output_file,
                    index=False,
                    mode=write_mode,
                    header=write_header,
                )
                first_write[key] = True

                record = stats.setdefault(
                    key,
                    {
                        "station_name": station_value,
                        "domain": domain,
                        "profile": args.profile,
                        "rows": 0,
                        "columns": len(station_chunk.columns),
                        "file": str(output_file),
                    },
                )
                record["rows"] = int(record["rows"]) + len(station_chunk)

    manifest_rows = []
    for key in sorted(stats):
        record = stats[key]
        file_path = Path(str(record["file"]))
        size_mb = file_path.stat().st_size / (1024 * 1024)
        out_row = dict(record)
        out_row["size_mb"] = round(size_mb, 2)
        manifest_rows.append(out_row)

    manifest_path = output_dir / "station_split_manifest.csv"
    pd.DataFrame(manifest_rows).to_csv(manifest_path, index=False)

    print(f"Wrote {len(manifest_rows)} station-domain files")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
