"""Tests for NOAA client helpers and CLI commands without network access."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import sys

import pandas as pd
import pytest

from noaa_climate_data import noaa_client
from noaa_climate_data.pipeline import LocationDataOutputs
import noaa_climate_data.cli as cli


@dataclass(frozen=True)
class _FakeDateTime:
    @staticmethod
    def now(tz: timezone | None = None) -> datetime:
        return datetime(2025, 1, 1, 0, 0, 0, tzinfo=tz)


class TestNoaaClient:
    def test_get_years_parses_dirs(self, monkeypatch: pytest.MonkeyPatch) -> None:
        table = pd.DataFrame({0: ["2020/", "2021/", "bad/", "202A/", "2021/", None]})
        monkeypatch.setattr(noaa_client.pd, "read_html", lambda url: [table])
        years = noaa_client.get_years(retries=0)
        assert years == ["2020", "2021"]

    def test_get_file_list_for_year(self, monkeypatch: pytest.MonkeyPatch) -> None:
        table = pd.DataFrame({0: ["AAA.csv", "BBB.txt", None, "CCC.csv"]})
        monkeypatch.setattr(noaa_client.pd, "read_html", lambda url: [table])
        files = noaa_client.get_file_list_for_year("2020", retries=0)
        assert files == ["AAA.csv", "CCC.csv"]

    def test_build_file_list(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def fake_get_file_list(year: str, **_: object) -> list[str]:
            return [f"{year}.csv"] if year != "2021" else []

        monkeypatch.setattr(noaa_client, "get_file_list_for_year", fake_get_file_list)
        result = noaa_client.build_file_list(["2020", "2021", "2022"], retries=0)
        assert result.shape[0] == 2
        assert set(result["YEAR"]) == {"2020", "2022"}

    def test_count_years_per_file(self) -> None:
        file_list = pd.DataFrame(
            {
                "YEAR": [2019, 2020, 2021, 2021],
                "FileName": ["A.csv", "A.csv", "A.csv", "B.csv"],
            }
        )
        counts = noaa_client.count_years_per_file(file_list, 2020, 2021)
        row_a = counts[counts["FileName"] == "A.csv"].iloc[0]
        row_b = counts[counts["FileName"] == "B.csv"].iloc[0]
        assert row_a["No_Of_Years"] == 2
        assert row_b["No_Of_Years"] == 1

    def test_normalize_station_file_name(self) -> None:
        assert (
            noaa_client.normalize_station_file_name("723150-03812-2006.csv")
            == "72315003812.csv"
        )
        assert (
            noaa_client.normalize_station_file_name("723150-03812")
            == "72315003812.csv"
        )

    def test_fetch_station_metadata(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(noaa_client, "_url_exists", lambda *_args, **_kwargs: True)
        frame = pd.DataFrame(
            [
                {
                    "LATITUDE": "10.5",
                    "LONGITUDE": "-20.25",
                    "ELEVATION": "15",
                    "NAME": "Test Station",
                }
            ]
        )
        monkeypatch.setattr(
            noaa_client,
            "_read_csv_head_with_retries",
            lambda *_args, **_kwargs: frame,
        )
        metadata = noaa_client.fetch_station_metadata("723150-03812-2006.csv", 2020, retries=0)
        assert metadata is not None
        assert metadata.latitude == 10.5
        assert metadata.longitude == -20.25
        assert metadata.elevation == 15.0
        assert metadata.name == "Test Station"
        assert metadata.file_name == "72315003812.csv"

    def test_fetch_station_metadata_for_years(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def fake_fetch(file_name: str, year: int, **_: object) -> noaa_client.StationMetadata | None:
            if year == 2021:
                return noaa_client.StationMetadata(
                    latitude=1.0,
                    longitude=2.0,
                    elevation=3.0,
                    name="Test",
                    file_name=file_name,
                )
            return None

        monkeypatch.setattr(noaa_client, "fetch_station_metadata", fake_fetch)
        metadata, metadata_year = noaa_client.fetch_station_metadata_for_years(
            "ABC.csv",
            [2020, 2021],
            retries=0,
        )
        assert metadata is not None
        assert metadata_year == 2021


class TestCliCommands:
    def test_cli_file_list_invokes_builders(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(cli, "datetime", _FakeDateTime)
        called: dict[str, object] = {}

        def fake_build_data_file_list(output_csv: Path, **_: object) -> pd.DataFrame:
            called["output_csv"] = output_csv
            return pd.DataFrame({"YEAR": ["2020"], "FileName": ["A.csv"]})

        def fake_build_year_counts(
            file_list: pd.DataFrame,
            output_csv: Path,
            start_year: int,
            end_year: int,
        ) -> pd.DataFrame:
            called["counts_csv"] = output_csv
            called["start_year"] = start_year
            called["end_year"] = end_year
            return pd.DataFrame()

        monkeypatch.setattr(cli, "build_data_file_list", fake_build_data_file_list)
        monkeypatch.setattr(cli, "build_year_counts", fake_build_year_counts)

        monkeypatch.setattr(
            sys,
            "argv",
            ["prog", "file-list", "--start-year", "2000", "--end-year", "2001"],
        )
        cli.main()

        output_csv = called["output_csv"]
        counts_csv = called["counts_csv"]
        assert output_csv.name == "DataFileList.csv"
        assert counts_csv.name == "DataFileList_YEARCOUNT.csv"
        assert output_csv.parent.parent == Path("noaa_file_index")
        assert called["start_year"] == 2000
        assert called["end_year"] == 2001

    def test_cli_location_ids_invokes_builder(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.chdir(tmp_path)
        base_dir = tmp_path / "noaa_file_index" / "20250101"
        base_dir.mkdir(parents=True)
        counts_path = base_dir / "DataFileList_YEARCOUNT.csv"
        file_list_path = base_dir / "DataFileList.csv"
        pd.DataFrame({"FileName": ["A.csv"], "No_Of_Years": [1]}).to_csv(
            counts_path, index=False
        )
        pd.DataFrame({"YEAR": [2020], "FileName": ["A.csv"]}).to_csv(
            file_list_path, index=False
        )

        called: dict[str, object] = {}

        def fake_build_location_ids(
            counts: pd.DataFrame,
            output_csv: Path,
            metadata_years: range,
            **kwargs: object,
        ) -> pd.DataFrame:
            called["counts_rows"] = len(counts)
            called["output_csv"] = output_csv
            called["metadata_years"] = list(metadata_years)
            called["resume"] = kwargs.get("resume")
            return pd.DataFrame()

        monkeypatch.setattr(cli, "build_location_ids", fake_build_location_ids)

        monkeypatch.setattr(
            sys,
            "argv",
            [
                "prog",
                "location-ids",
                "--start-year",
                "2000",
                "--end-year",
                "2001",
                "--no-resume",
            ],
        )
        cli.main()

        assert called["counts_rows"] == 1
        assert called["output_csv"].resolve() == (base_dir / "Stations.csv").resolve()
        assert called["metadata_years"] == [2000, 2001]
        assert called["resume"] is False

    def test_cli_process_location_writes_outputs(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.chdir(tmp_path)
        output_dir = tmp_path / "out"
        sample = pd.DataFrame({"value": [1]})

        def fake_process_location(*_: object, **__: object) -> LocationDataOutputs:
            return LocationDataOutputs(
                raw=sample,
                cleaned=sample,
                hourly=sample,
                monthly=sample,
                yearly=sample,
            )

        monkeypatch.setattr(cli, "process_location", fake_process_location)
        monkeypatch.setattr(
            sys,
            "argv",
            [
                "prog",
                "process-location",
                "TEST.csv",
                "--start-year",
                "2020",
                "--end-year",
                "2020",
                "--output-dir",
                str(output_dir),
            ],
        )
        cli.main()

        assert (output_dir / "LocationData_Raw.csv").exists()
        assert (output_dir / "LocationData_Cleaned.csv").exists()
        assert (output_dir / "LocationData_Hourly.csv").exists()
        assert (output_dir / "LocationData_Monthly.csv").exists()
        assert (output_dir / "LocationData_Yearly.csv").exists()
