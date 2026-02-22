#!/usr/bin/env python3
"""
Recover missing station metadata lost during internet outage.

This script identifies stations present in DataFileList_YEARCOUNT.csv but
missing from Stations.csv, then fetches their metadata and appends them.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import pandas as pd

from noaa_climate_data.noaa_client import fetch_station_metadata_for_years
from noaa_climate_data.pipeline import normalize_station_file_name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recover missing station metadata")
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=Path("noaa_file_index/20260207"),
        help="Directory containing DataFileList_YEARCOUNT.csv and Stations.csv",
    )
    parser.add_argument(
        "--metadata-years",
        type=int,
        nargs="+",
        default=[1975, 2000, 2025],
        help="Years to try for metadata (first success wins)",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.5,
        help="Delay between metadata requests",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of retries per metadata request",
    )
    parser.add_argument(
        "--backoff-base",
        type=float,
        default=0.5,
        help="Base backoff time for retries",
    )
    parser.add_argument(
        "--backoff-max",
        type=float,
        default=8.0,
        help="Max backoff time for retries",
    )
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=100,
        help="Save progress every N stations",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    
    year_counts_csv = args.index_dir / "DataFileList_YEARCOUNT.csv"
    stations_csv = args.index_dir / "Stations.csv"
    data_file_list_csv = args.index_dir / "DataFileList.csv"
    
    if not year_counts_csv.exists():
        raise FileNotFoundError(f"Missing {year_counts_csv}")
    if not stations_csv.exists():
        raise FileNotFoundError(f"Missing {stations_csv}")
    
    # Load existing data
    print("Loading existing data...")
    year_counts = pd.read_csv(year_counts_csv)
    stations = pd.read_csv(stations_csv)
    
    # Build year summary from DataFileList.csv if available
    year_summary: dict[str, tuple[int | None, int | None, int | None]] = {}
    if data_file_list_csv.exists():
        print(f"Building year summary from {data_file_list_csv}...")
        file_list = pd.read_csv(data_file_list_csv)
        file_list["YEAR"] = pd.to_numeric(file_list["YEAR"], errors="coerce")
        grouped = file_list.groupby("FileName")["YEAR"].agg(["min", "max", "count"]).reset_index()
        year_summary = {
            row["FileName"]: (
                int(row["min"]) if pd.notna(row["min"]) else None,
                int(row["max"]) if pd.notna(row["max"]) else None,
                int(row["count"]) if pd.notna(row["count"]) else None,
            )
            for _, row in grouped.iterrows()
        }
    
    # Find missing stations
    all_files = set(year_counts["FileName"])
    existing_files = set(stations["FileName"])
    missing_files = sorted(all_files - existing_files)
    
    print(f"\nStatus:")
    print(f"  Total stations in year counts: {len(all_files):,}")
    print(f"  Stations in Stations.csv: {len(existing_files):,}")
    print(f"  Missing stations: {len(missing_files):,}")
    
    if not missing_files:
        print("\n✓ No missing stations - nothing to recover!")
        return
    
    print(f"\nSample missing stations (first 10):")
    for fname in missing_files[:10]:
        years = year_counts[year_counts["FileName"] == fname]["No_Of_Years"].iloc[0]
        print(f"  {fname} ({years} years)")
    
    if args.dry_run:
        print(f"\n[DRY RUN] Would fetch metadata for {len(missing_files):,} stations")
        return
    
    # Backup current Stations.csv
    backup_path = stations_csv.parent / f"{stations_csv.stem}_backup_pre_recovery.csv"
    print(f"\nBacking up Stations.csv to {backup_path}...")
    stations.to_csv(backup_path, index=False)
    
    # Fetch metadata for missing stations
    print(f"\nFetching metadata for {len(missing_files):,} missing stations...")
    print(f"  Metadata years to try: {args.metadata_years}")
    print(f"  Sleep between requests: {args.sleep_seconds}s")
    print(f"  Retries per request: {args.retries}")
    print(f"  Checkpoint every: {args.checkpoint_every} stations")
    
    # Get the max LegacyID to continue from
    next_legacy_id = int(stations["LegacyID"].max()) + 1 if "LegacyID" in stations.columns else 1
    
    new_rows = []
    failed_files = []
    
    for idx, file_name in enumerate(missing_files, start=1):
        try:
            metadata, metadata_year = fetch_station_metadata_for_years(
                file_name,
                args.metadata_years,
                sleep_seconds=args.sleep_seconds,
                retries=args.retries,
                backoff_base=args.backoff_base,
                backoff_max=args.backoff_max,
            )
            
            if metadata is None or metadata_year is None:
                print(f"  ✗ [{idx}/{len(missing_files)}] {file_name} - no metadata found")
                failed_files.append(file_name)
                continue
            
            station_id = Path(normalize_station_file_name(metadata.file_name)).stem
            metadata_complete = all(
                value is not None
                for value in (
                    metadata.latitude,
                    metadata.longitude,
                    metadata.elevation,
                    metadata.name,
                )
            )
            
            first_year, last_year, year_count = year_summary.get(file_name, (None, None, None))
            no_of_years = int(
                year_counts.loc[year_counts["FileName"] == file_name, "No_Of_Years"].iloc[0]
            )
            
            row = {
                "ID": station_id,
                "FileName": metadata.file_name,
                "LATITUDE": metadata.latitude,
                "LONGITUDE": metadata.longitude,
                "ELEVATION": metadata.elevation,
                "NAME": metadata.name,
                "No_Of_Years": no_of_years,
                "FIRST_YEAR": first_year,
                "LAST_YEAR": last_year,
                "YEAR_COUNT": year_count,
                "METADATA_YEAR": metadata_year,
                "METADATA_COMPLETE": metadata_complete,
                "LegacyID": next_legacy_id,
                "raw_data_pulled": False,
                "data_cleaned": False,
                "data_aggregated": False,
            }
            
            new_rows.append(row)
            next_legacy_id += 1
            
            print(
                f"  ✓ [{idx}/{len(missing_files)}] {file_name} "
                f"(year={metadata_year}, name={metadata.name})"
            )
            
            # Checkpoint
            if args.checkpoint_every and (len(new_rows) % args.checkpoint_every == 0):
                temp_df = pd.concat([stations, pd.DataFrame(new_rows)], ignore_index=True)
                temp_df.to_csv(stations_csv, index=False)
                checkpoint_path = (
                    stations_csv.parent / 
                    f"{stations_csv.stem}_recovery_checkpoint_{len(new_rows):05d}.csv"
                )
                temp_df.to_csv(checkpoint_path, index=False)
                print(
                    f"\n  💾 Checkpoint: {len(new_rows)} new stations saved "
                    f"({len(failed_files)} failed so far)\n"
                )
        
        except KeyboardInterrupt:
            print("\n\n⚠ Interrupted by user!")
            break
        except Exception as e:
            print(f"  ✗ [{idx}/{len(missing_files)}] {file_name} - error: {e}")
            failed_files.append(file_name)
    
    # Save final results
    if new_rows:
        print(f"\nSaving final results...")
        final_df = pd.concat([stations, pd.DataFrame(new_rows)], ignore_index=True)
        final_df.to_csv(stations_csv, index=False)
        print(f"  ✓ Appended {len(new_rows)} stations to Stations.csv")
        print(f"  ✓ Total stations now: {len(final_df):,}")
    
    # Summary
    print(f"\n{'='*60}")
    print("Recovery Summary:")
    print(f"  Attempted: {len(missing_files):,}")
    print(f"  Recovered: {len(new_rows):,}")
    print(f"  Failed: {len(failed_files):,}")
    
    if failed_files:
        print(f"\nFailed stations (first 20):")
        for fname in failed_files[:20]:
            print(f"  - {fname}")
        if len(failed_files) > 20:
            print(f"  ... and {len(failed_files) - 20} more")
    
    if new_rows:
        print(f"\n✓ Recovery complete! Stations.csv now has {len(final_df):,} stations.")
        print(f"  Backup saved to: {backup_path}")
    else:
        print("\n⚠ No stations were recovered.")


if __name__ == "__main__":
    main()
