"""Shared constants for NOAA ISD Global Hourly data."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

BASE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access"

QUALITY_FLAGS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "9",
    "A",
    "C",
    "I",
    "M",
    "P",
    "R",
    "U",
}

DATA_SOURCE_FLAGS = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
}

REPORT_TYPE_CODES = {
    "AERO",
    "AUST",
    "AUTO",
    "BOGUS",
    "BRAZ",
    "COOPD",
    "COOPS",
    "CRB",
    "CRN05",
    "CRN15",
    "FM-12",
    "FM-13",
    "FM-14",
    "FM-15",
    "FM-16",
    "FM-18",
    "GREEN",
    "MESOH",
    "MESOS",
    "MESOW",
    "MEXIC",
    "NSRDB",
    "PCP15",
    "PCP60",
    "S-S-A",
    "SA-AU",
    "SAO",
    "SAOSP",
    "SHEF",
    "SMARS",
    "SOD",
    "SOM",
    "SURF",
    "SY-AE",
    "SY-AU",
    "SY-MT",
    "SY-SA",
    "WBO",
    "WNO",
}

QC_PROCESS_CODES = {
    "V01",
    "V02",
    "V03",
}

CLOUD_QUALITY_FLAGS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "9",
    "M",
}

CLOUD_SUMMATION_QC_FLAGS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "9",
}

SOLARAD_QC_FLAGS = {"1", "3", "9"}

SOLAR_IRRADIANCE_QC_FLAGS = {"0", "1", "2", "3", "9"}

SUNSHINE_PERCENT_QC_FLAGS = {"4", "5", "6", "7", "9", "M"}

DEFAULT_START_YEAR = 2000
DEFAULT_END_YEAR = 2019


@dataclass(frozen=True)
class FieldPartRule:
    scale: float | None = None
    missing_values: set[str] | None = None
    quality_part: int | None = None
    allowed_quality: set[str] | None = None
    allowed_values: set[str] | None = None
    kind: str = "numeric"
    agg: str = "mean"  # mean | max | min | mode | sum | drop | circular_mean


@dataclass(frozen=True)
class FieldRule:
    code: str
    parts: dict[int, FieldPartRule]


@dataclass(frozen=True)
class FieldRegistryEntry:
    code: str
    part: int
    internal_name: str
    name: str
    kind: str
    scale: float | None
    missing_values: set[str] | None
    quality_part: int | None
    agg: str


FIELD_RULES: dict[str, FieldRule] = {
    "WND": FieldRule(
        code="WND",
        parts={
            1: FieldPartRule(missing_values={"999"}, quality_part=2, agg="circular_mean"),
            2: FieldPartRule(kind="quality", agg="drop"),  # direction quality
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"A", "B", "C", "H", "N", "R", "Q", "T", "V"},
            ),  # wind type code
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop"),  # speed quality
        },
    ),
    "CIG": FieldRule(
        code="CIG",
        parts={
            1: FieldPartRule(missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop"),  # height quality
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"A", "B", "C", "D", "E", "M", "P", "R", "S", "U", "V", "W"},
            ),  # determination code
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"N", "Y"},
            ),  # CAVOK code
        },
    ),
    "VIS": FieldRule(
        code="VIS",
        parts={
            1: FieldPartRule(missing_values={"999999"}, quality_part=2, agg="min"),
            2: FieldPartRule(kind="quality", agg="drop"),  # distance quality
            3: FieldPartRule(
                quality_part=4,
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"N", "V"},
            ),
            4: FieldPartRule(kind="quality", agg="drop"),  # variability quality
        },
    ),
    "TMP": FieldRule(
        code="TMP",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"9999"},
                quality_part=2,
                allowed_quality=QUALITY_FLAGS,
            )
        },
    ),
    "DEW": FieldRule(
        code="DEW",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"9999"},
                quality_part=2,
                allowed_quality=QUALITY_FLAGS,
            )
        },
    ),
    "SLP": FieldRule(
        code="SLP",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"99999"},
                quality_part=2,
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            )
        },
    ),
    "OC1": FieldRule(
        code="OC1",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"9999"},
                quality_part=2,
                agg="max",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            )
        },
    ),
    "MA1": FieldRule(
        code="MA1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop"),  # altimeter quality
            3: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # station pressure quality
        },
    ),
    "MD1": FieldRule(
        code="MD1",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=2,
                missing_values={"9"},
            ),  # pressure tendency code
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # tendency quality
            3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # 3-hr pressure quality
            5: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=6),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # 24-hr pressure quality
        },
    ),
    "SA1": FieldRule(
        code="SA1",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"999"},
                quality_part=2,
                allowed_quality={"0", "1", "2", "3", "9"},
            )
        },
    ),
    "UA1": FieldRule(
        code="UA1",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=4,
            ),  # method code
            2: FieldPartRule(missing_values={"99"}, quality_part=4),  # wave period (seconds)
            3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # wave height quality
            5: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=6,
            ),  # sea state code
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # sea state quality
        },
    ),
    "UG1": FieldRule(
        code="UG1",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=4),  # primary swell period (seconds)
            2: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            3: FieldPartRule(missing_values={"999"}, agg="circular_mean", quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # swell height quality
        },
    ),
    "GE1": FieldRule(
        code="GE1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # convective cloud code
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"999999"}),  # vertical datum
            3: FieldPartRule(missing_values={"99999"}),  # base height upper range
            4: FieldPartRule(missing_values={"99999"}),  # base height lower range
        },
    ),
    "GF1": FieldRule(
        code="GF1",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=3, agg="mean"),
            2: FieldPartRule(missing_values={"99"}, agg="mean"),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # total coverage quality
            4: FieldPartRule(missing_values={"99"}, quality_part=5, agg="mean"),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # lowest cloud cover quality
            6: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),  # low cloud genus
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # low cloud genus quality
            8: FieldPartRule(missing_values={"99999"}, quality_part=9),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # lowest base height quality
            10: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),  # mid cloud genus
            11: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # mid cloud genus quality
            12: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),  # high cloud genus
            13: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # high cloud genus quality
        },
    ),
    "CO1": FieldRule(
        code="CO1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
        },
    ),
}

FIELD_RULE_PREFIXES: dict[str, FieldRule] = {
    "AA": FieldRule(
        code="AA*",
        parts={
            1: FieldPartRule(missing_values={"99"}, agg="drop"),  # period hours
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4, agg="sum"),
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # condition code
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AB": FieldRule(
        code="AB*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=3),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # condition code
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AC": FieldRule(
        code="AC*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"0", "1", "2", "3"},
                quality_part=3,
            ),  # duration code
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"C", "I"},
                quality_part=3,
            ),  # characteristic code
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AD": FieldRule(
        code="AD*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=6),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),  # condition code
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),  # date 1
            4: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),  # date 2
            5: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),  # date 3
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AE": FieldRule(
        code="AE*",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=2),  # days >= .01
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),
            3: FieldPartRule(missing_values={"99"}, quality_part=4),  # days >= .10
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),
            5: FieldPartRule(missing_values={"99"}, quality_part=6),  # days >= .50
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),
            7: FieldPartRule(missing_values={"99"}, quality_part=8),  # days >= 1.00
            8: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),
        },
    ),
    "AG": FieldRule(
        code="AG*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"0", "1", "2", "3", "4", "5"},
            ),  # discrepancy code
            2: FieldPartRule(missing_values={"999"}),  # estimated depth mm
        },
    ),
    "AH": FieldRule(
        code="AH*",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),  # period minutes
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),  # depth mm
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2"},
            ),  # condition code
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"999999"},
            ),  # end date-time
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AI": FieldRule(
        code="AI*",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),  # period minutes
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),  # depth mm
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2"},
            ),  # condition code
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"999999"},
            ),  # end date-time
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AK": FieldRule(
        code="AK1",
        parts={
            1: FieldPartRule(missing_values={"9999"}, quality_part=4),  # depth cm
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3", "4"},
            ),  # condition code
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"999999"},
            ),  # dates of occurrence
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # quality code
        },
    ),
    "AL": FieldRule(
        code="AL*",
        parts={
            1: FieldPartRule(missing_values={"99"}, agg="drop"),  # period hours
            2: FieldPartRule(
                missing_values={"999"},
                quality_part=4,
                agg="sum",
            ),  # depth cm
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3", "4", "5", "6", "E"},
            ),  # condition code
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # quality code
        },
    ),
    "AM": FieldRule(
        code="AM1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=6),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3", "4"},
            ),  # condition code
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            4: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            5: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),  # quality code
        },
    ),
    "AN": FieldRule(
        code="AN1",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),  # period hours
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3", "4", "5", "6", "7", "E"},
            ),  # condition code
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # quality code
        },
    ),
    "AO": FieldRule(
        code="AO*",
        parts={
            1: FieldPartRule(missing_values={"99"}, agg="drop"),  # period minutes
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4, agg="sum"),
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3", "4", "5", "6", "7", "8", "E", "I", "J"},
            ),  # condition code
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),  # quality code
        },
    ),
    "AP": FieldRule(
        code="AP*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=3),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
        },
    ),
    "AJ": FieldRule(
        code="AJ*",
        parts={
            1: FieldPartRule(missing_values={"9999"}, quality_part=3),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
            ),  # snow depth condition
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # snow depth quality
            4: FieldPartRule(scale=0.1, missing_values={"999999"}, quality_part=6),
            5: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
            ),  # equiv water condition
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=QUALITY_FLAGS - {"C"},
            ),  # equiv water quality
        },
    ),
    "AT": FieldRule(
        code="AT*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=4,
                allowed_values={"AU", "AW", "MW"},
            ),  # source element
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=4,
                allowed_values={
                    "01",
                    "02",
                    "03",
                    "04",
                    "05",
                    "06",
                    "07",
                    "08",
                    "09",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                    "19",
                    "21",
                    "22",
                },
            ),  # daily present weather type
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=4,
                allowed_values={
                    "FG",
                    "FG+",
                    "TS",
                    "PL",
                    "GR",
                    "GL",
                    "DU",
                    "HZ",
                    "BLSN",
                    "FC",
                    "WIND",
                    "BLPY",
                    "BR",
                    "DZ",
                    "FZDZ",
                    "RA",
                    "FZRA",
                    "SN",
                    "UP",
                    "MIFG",
                    "FZFG",
                },
            ),  # daily present weather abbreviation
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # quality code
        },
    ),
    "AU": FieldRule(
        code="AU*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", quality_part=7),  # intensity
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=7,
            ),  # descriptor
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=7,
            ),  # precip code
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=7,
            ),  # obscuration
            5: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=7,
            ),  # other phenomena
            6: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=7,
            ),  # combo indicator
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # quality code
        },
    ),
    "CB": FieldRule(
        code="CB*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            2: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=3),
            3: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CF": FieldRule(
        code="CF*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CG": FieldRule(
        code="CG*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CH": FieldRule(
        code="CH*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            5: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=6),
            6: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CO": FieldRule(
        code="CO*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"999"}),
            2: FieldPartRule(scale=0.1, missing_values={"9999"}),
        },
    ),
    "CT": FieldRule(
        code="CT*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CU": FieldRule(
        code="CU*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CV": FieldRule(
        code="CV*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9999"},
                quality_part=5,
            ),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            10: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9999"},
                quality_part=11,
            ),
            11: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            12: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CW": FieldRule(
        code="CW*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CX": FieldRule(
        code="CX*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(missing_values={"9999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            10: FieldPartRule(missing_values={"9999"}, quality_part=11),
            11: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            12: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "GA": FieldRule(
        code="GA*",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=2, agg="mean"),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # coverage quality
            3: FieldPartRule(missing_values={"99999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # base height quality
            5: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=6,
            ),  # cloud type
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),  # cloud type quality
        },
    ),
    "GD": FieldRule(
        code="GD*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                quality_part=3,
            ),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=3,
            ),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_SUMMATION_QC_FLAGS,
            ),
            4: FieldPartRule(missing_values={"99999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_SUMMATION_QC_FLAGS,
            ),
            6: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
            ),
        },
    ),
    "GG": FieldRule(
        code="GG*",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=2, agg="mean"),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
            3: FieldPartRule(missing_values={"99999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
            5: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=6,
            ),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
            7: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=8,
            ),
            8: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "KA": FieldRule(
        code="KA*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"999"}),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(kind="quality", agg="drop"),  # temperature quality
        },
    ),
    "KB": FieldRule(
        code="KB*",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"A", "M", "N"},
            ),
            3: FieldPartRule(scale=0.01, missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
        },
    ),
    "KC": FieldRule(
        code="KC*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"N", "M"},
            ),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1"},
            ),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            4: FieldPartRule(kind="categorical", agg="drop", missing_values={"999999"}),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),
        },
    ),
    "KD": FieldRule(
        code="KD*",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"H", "C"},
            ),
            3: FieldPartRule(missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
        },
    ),
    "KE1": FieldRule(
        code="KE1",
        parts={
            1: FieldPartRule(missing_values={"99"}, quality_part=2),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
            3: FieldPartRule(missing_values={"99"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
            5: FieldPartRule(missing_values={"99"}, quality_part=6),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
            7: FieldPartRule(missing_values={"99"}, quality_part=8),
            8: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
        },
    ),
    "KF1": FieldRule(
        code="KF1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
        },
    ),
    "KG": FieldRule(
        code="KG*",
        parts={
            1: FieldPartRule(missing_values={"999"}, agg="drop"),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"D", "W"},
            ),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"D"},
            ),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9"},
            ),
        },
    ),
    "GH": FieldRule(
        code="GH*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLARAD_QC_FLAGS,
            ),
            3: FieldPartRule(kind="categorical", agg="drop"),
            4: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLARAD_QC_FLAGS,
            ),
            6: FieldPartRule(kind="categorical", agg="drop"),
            7: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=8),
            8: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLARAD_QC_FLAGS,
            ),
            9: FieldPartRule(kind="categorical", agg="drop"),
            10: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=11),
            11: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLARAD_QC_FLAGS,
            ),
            12: FieldPartRule(kind="categorical", agg="drop"),
        },
    ),
    "GJ": FieldRule(
        code="GJ*",
        parts={
            1: FieldPartRule(missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_QUALITY_FLAGS,
            ),
        },
    ),
    "GK": FieldRule(
        code="GK*",
        parts={
            1: FieldPartRule(missing_values={"999"}, quality_part=2),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SUNSHINE_PERCENT_QC_FLAGS,
            ),
        },
    ),
    "GL": FieldRule(
        code="GL*",
        parts={
            1: FieldPartRule(missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=CLOUD_SUMMATION_QC_FLAGS,
            ),
        },
    ),
    "GM": FieldRule(
        code="GM*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(missing_values={"9999"}, quality_part=4),
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            5: FieldPartRule(missing_values={"9999"}, quality_part=7),
            6: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            8: FieldPartRule(missing_values={"9999"}, quality_part=10),
            9: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            10: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            11: FieldPartRule(missing_values={"9999"}, quality_part=13),
            12: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            13: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
        },
    ),
    "GN": FieldRule(
        code="GN*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            4: FieldPartRule(missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            6: FieldPartRule(missing_values={"9999"}, quality_part=7),
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            8: FieldPartRule(missing_values={"9999"}, quality_part=9),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            10: FieldPartRule(missing_values={"999"}, quality_part=11),
            11: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
        },
    ),
    "GO": FieldRule(
        code="GO*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            4: FieldPartRule(missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
            6: FieldPartRule(missing_values={"9999"}, quality_part=7),
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality=SOLAR_IRRADIANCE_QC_FLAGS,
            ),
        },
    ),
    "GP1": FieldRule(
        code="GP1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(missing_values={"9999"}),
            3: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            4: FieldPartRule(missing_values={"999"}),
            5: FieldPartRule(missing_values={"9999"}),
            6: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            7: FieldPartRule(missing_values={"999"}),
            8: FieldPartRule(missing_values={"9999"}),
            9: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            10: FieldPartRule(missing_values={"999"}),
        },
    ),
    "GQ1": FieldRule(
        code="GQ1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "GR1": FieldRule(
        code="GR1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9999"}),
            2: FieldPartRule(missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
            4: FieldPartRule(missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "HAIL": FieldRule(
        code="HAIL",
        parts={
            1: FieldPartRule(
                scale=0.1,
                missing_values={"999"},
                quality_part=2,
                allowed_quality={"0", "1", "2", "3", "9"},
            )
        },
    ),
    "IA1": FieldRule(
        code="IA1",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=2,
            ),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "IA2": FieldRule(
        code="IA2",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=3),
            2: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=3),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "IB1": FieldRule(
        code="IB1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            10: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=11),
            11: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            12: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "IB2": FieldRule(
        code="IB2",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "IC1": FieldRule(
        code="IC1",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            2: FieldPartRule(missing_values={"9999"}, quality_part=4),
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3"},
                quality_part=4,
            ),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
            5: FieldPartRule(scale=0.01, missing_values={"999"}, quality_part=7),
            6: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3"},
                quality_part=7,
            ),
            7: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
            8: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=10),
            9: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3"},
                quality_part=10,
            ),
            10: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
            11: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=13),
            12: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"1", "2", "3"},
                quality_part=13,
            ),
            13: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
        },
    ),
    "OA": FieldRule(
        code="OA*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", missing_values={"9"}),
            2: FieldPartRule(kind="categorical", agg="drop", missing_values={"99"}),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "OD": FieldRule(
        code="OD*",
        parts={
            1: FieldPartRule(missing_values={"9"}, kind="categorical", agg="drop"),
            2: FieldPartRule(missing_values={"99"}, kind="categorical", agg="drop"),
            3: FieldPartRule(missing_values={"999"}, agg="circular_mean"),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(
                missing_values={"9"},
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "ED1": FieldRule(
        code="ED1",
        parts={
            1: FieldPartRule(scale=10.0, missing_values={"99"}, quality_part=4),
            2: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"L", "C", "R", "U"},
                quality_part=4,
            ),
            3: FieldPartRule(missing_values={"9999"}, quality_part=4),
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),
        },
    ),
    "MV": FieldRule(
        code="MV*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=2,
            ),
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"4", "5", "6", "7", "9"},
            ),
        },
    ),
    "MW": FieldRule(
        code="MW*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop", quality_part=2),  # present-weather code
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "9", "M"},
            ),  # present-weather quality
        },
    ),
    "AY": FieldRule(
        code="AY*",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                quality_part=2,
            ),  # past-weather condition code
            2: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # past-weather condition quality
            3: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"99"},
                quality_part=4,
            ),  # past-weather period
            4: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "9"},
            ),  # past-weather period quality
        },
    ),
    "CR1": FieldRule(
        code="CR1",
        parts={
            1: FieldPartRule(scale=0.001, missing_values={"99999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CI1": FieldRule(
        code="CI1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            10: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=11),
            11: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            12: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CN1": FieldRule(
        code="CN1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CN2": FieldRule(
        code="CN2",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(missing_values={"99"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CN3": FieldRule(
        code="CN3",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"999999"}, quality_part=2),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(scale=0.1, missing_values={"999999"}, quality_part=5),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
    "CN4": FieldRule(
        code="CN4",
        parts={
            1: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9"},
                allowed_values={"0", "1", "9"},
                quality_part=2,
            ),
            2: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            3: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            4: FieldPartRule(
                kind="categorical",
                agg="drop",
                missing_values={"9999"},
                quality_part=5,
            ),
            5: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            6: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            7: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=8),
            8: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            9: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
            10: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=11),
            11: FieldPartRule(kind="quality", agg="drop", allowed_quality={"1", "3", "9"}),
            12: FieldPartRule(
                kind="quality",
                agg="drop",
                allowed_quality={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            ),
        },
    ),
}


def get_field_rule(prefix: str) -> FieldRule | None:
    if prefix in FIELD_RULES:
        return FIELD_RULES[prefix]
    for key, rule in FIELD_RULE_PREFIXES.items():
        if prefix.startswith(key):
            return rule
    return None


# ── Column classification helpers ────────────────────────────────────────

_EXPANDED_COL_RE = re.compile(r"^(?P<field>[A-Z][A-Z0-9]*)__(?P<suffix>.+)$")

FRIENDLY_COLUMN_MAP: dict[str, str] = {
    "WND__part1": "wind_direction_deg",
    "WND__part2": "wind_direction_quality_code",
    "WND__part3": "wind_type_code",
    "WND__part4": "wind_speed_ms",
    "WND__part5": "wind_speed_quality_code",
    "WND__direction_variable": "wind_direction_variable",
    "CIG__part1": "ceiling_height_m",
    "CIG__part2": "ceiling_height_quality_code",
    "CIG__part3": "ceiling_determination_code",
    "CIG__part4": "ceiling_cavok_code",
    "VIS__part1": "visibility_m",
    "VIS__part2": "visibility_quality_code",
    "VIS__part3": "visibility_variability_code",
    "VIS__part4": "visibility_variability_quality_code",
    "TMP__value": "temperature_c",
    "TMP__quality": "temperature_quality_code",
    "DEW__value": "dew_point_c",
    "DEW__quality": "dew_point_quality_code",
    "SLP__value": "sea_level_pressure_hpa",
    "SLP__quality": "sea_level_pressure_quality_code",
    "OC1__value": "wind_gust_ms",
    "OC1__quality": "wind_gust_quality_code",
    "MA1__part1": "altimeter_setting_hpa",
    "MA1__part2": "altimeter_quality_code",
    "MA1__part3": "station_pressure_hpa",
    "MA1__part4": "station_pressure_quality_code",
    "MD1__part1": "pressure_tendency_code",
    "MD1__part2": "pressure_tendency_quality_code",
    "MD1__part3": "pressure_change_3hr_hpa",
    "MD1__part4": "pressure_change_3hr_quality_code",
    "MD1__part5": "pressure_change_24hr_hpa",
    "MD1__part6": "pressure_change_24hr_quality_code",
    "SA1__value": "sea_surface_temperature_c",
    "SA1__quality": "sea_surface_temperature_quality_code",
    "UA1__part1": "wave_method_code",
    "UA1__part2": "wave_period_seconds",
    "UA1__part3": "wave_height_m",
    "UA1__part4": "wave_height_quality_code",
    "UA1__part5": "sea_state_code",
    "UA1__part6": "sea_state_quality_code",
    "UG1__part1": "swell_period_seconds",
    "UG1__part2": "swell_height_m",
    "UG1__part3": "swell_direction_deg",
    "UG1__part4": "swell_height_quality_code",
    "GE1__part1": "convective_cloud_code",
    "GE1__part2": "cloud_vertical_datum_code",
    "GE1__part3": "cloud_base_height_upper_m",
    "GE1__part4": "cloud_base_height_lower_m",
    "GF1__part1": "cloud_total_coverage",
    "GF1__part2": "cloud_opaque_coverage",
    "GF1__part3": "cloud_total_coverage_quality_code",
    "GF1__part4": "cloud_lowest_coverage",
    "GF1__part5": "cloud_lowest_coverage_quality_code",
    "GF1__part6": "cloud_low_genus_code",
    "GF1__part7": "cloud_low_genus_quality_code",
    "GF1__part8": "cloud_lowest_base_height_m",
    "GF1__part9": "cloud_lowest_base_height_quality_code",
    "GF1__part10": "cloud_mid_genus_code",
    "GF1__part11": "cloud_mid_genus_quality_code",
    "GF1__part12": "cloud_high_genus_code",
    "GF1__part13": "cloud_high_genus_quality_code",
    "CO1__part1": "climate_division_number",
    "CO1__part2": "utc_lst_offset_hours",
    "CR1__part1": "crn_datalogger_version",
    "CR1__part2": "crn_datalogger_version_qc",
    "CR1__part3": "crn_datalogger_version_flag",
    "ED1__part1": "runway_direction_deg",
    "ED1__part2": "runway_designator_code",
    "ED1__part3": "runway_visibility_m",
    "ED1__part4": "runway_visibility_quality_code",
    "GQ1__part1": "solar_angle_period_minutes",
    "GQ1__part2": "solar_zenith_angle_deg_mean",
    "GQ1__part3": "solar_zenith_angle_quality_code",
    "GQ1__part4": "solar_azimuth_angle_deg_mean",
    "GQ1__part5": "solar_azimuth_angle_quality_code",
    "GR1__part1": "extraterrestrial_radiation_period_minutes",
    "GR1__part2": "extraterrestrial_radiation_horizontal_wm2",
    "GR1__part3": "extraterrestrial_radiation_horizontal_quality_code",
    "GR1__part4": "extraterrestrial_radiation_normal_wm2",
    "GR1__part5": "extraterrestrial_radiation_normal_quality_code",
    "HAIL__value": "hail_size_cm",
    "HAIL__quality": "hail_size_quality_code",
    "IA1__part1": "ground_surface_observation_code",
    "IA1__part2": "ground_surface_observation_quality_code",
    "IA2__part1": "ground_surface_min_temp_period_hours",
    "IA2__part2": "ground_surface_min_temp_c",
    "IA2__part3": "ground_surface_min_temp_quality_code",
    "IB1__part1": "surface_temp_avg_c",
    "IB1__part2": "surface_temp_avg_qc",
    "IB1__part3": "surface_temp_avg_flag",
    "IB1__part4": "surface_temp_min_c",
    "IB1__part5": "surface_temp_min_qc",
    "IB1__part6": "surface_temp_min_flag",
    "IB1__part7": "surface_temp_max_c",
    "IB1__part8": "surface_temp_max_qc",
    "IB1__part9": "surface_temp_max_flag",
    "IB1__part10": "surface_temp_std_c",
    "IB1__part11": "surface_temp_std_qc",
    "IB1__part12": "surface_temp_std_flag",
    "IB2__part1": "surface_temp_sensor_c",
    "IB2__part2": "surface_temp_sensor_qc",
    "IB2__part3": "surface_temp_sensor_flag",
    "IB2__part4": "surface_temp_sensor_std_c",
    "IB2__part5": "surface_temp_sensor_std_qc",
    "IB2__part6": "surface_temp_sensor_std_flag",
    "IC1__part1": "ground_surface_period_hours",
    "IC1__part2": "ground_surface_wind_movement_miles",
    "IC1__part3": "ground_surface_wind_condition_code",
    "IC1__part4": "ground_surface_wind_quality_code",
    "IC1__part5": "ground_surface_evaporation_in",
    "IC1__part6": "ground_surface_evaporation_condition_code",
    "IC1__part7": "ground_surface_evaporation_quality_code",
    "IC1__part8": "ground_surface_pan_temp_max_c",
    "IC1__part9": "ground_surface_pan_temp_max_condition_code",
    "IC1__part10": "ground_surface_pan_temp_max_quality_code",
    "IC1__part11": "ground_surface_pan_temp_min_c",
    "IC1__part12": "ground_surface_pan_temp_min_condition_code",
    "IC1__part13": "ground_surface_pan_temp_min_quality_code",
    "KE1__part1": "extreme_days_max_le_32f",
    "KE1__part2": "extreme_days_max_le_32f_quality_code",
    "KE1__part3": "extreme_days_max_ge_90f",
    "KE1__part4": "extreme_days_max_ge_90f_quality_code",
    "KE1__part5": "extreme_days_min_le_32f",
    "KE1__part6": "extreme_days_min_le_32f_quality_code",
    "KE1__part7": "extreme_days_min_le_0f",
    "KE1__part8": "extreme_days_min_le_0f_quality_code",
    "KF1__part1": "derived_air_temp_c",
    "KF1__part2": "derived_air_temp_quality_code",
}

_FRIENDLY_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^MW(?P<idx>\d+)__part1$"), "present_weather_code_{idx}"),
    (re.compile(r"^MV(?P<idx>\d+)__part1$"), "present_weather_vicinity_code_{idx}"),
    (re.compile(r"^MV(?P<idx>\d+)__part2$"), "present_weather_vicinity_quality_code_{idx}"),
    (re.compile(r"^AY(?P<idx>\d+)__part1$"), "past_weather_condition_code_{idx}"),
    (re.compile(r"^AY(?P<idx>\d+)__part3$"), "past_weather_period_hours_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part1$"), "precip_period_hours_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part2$"), "precip_amount_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part3$"), "precip_condition_code_{idx}"),
    (re.compile(r"^AA(?P<idx>\d+)__part4$"), "precip_quality_code_{idx}"),
    (re.compile(r"^AB(?P<idx>\d+)__part1$"), "precip_monthly_total_{idx}"),
    (re.compile(r"^AB(?P<idx>\d+)__part2$"), "precip_monthly_condition_code_{idx}"),
    (re.compile(r"^AB(?P<idx>\d+)__part3$"), "precip_monthly_quality_code_{idx}"),
    (re.compile(r"^AC(?P<idx>\d+)__part1$"), "precip_history_duration_code_{idx}"),
    (re.compile(r"^AC(?P<idx>\d+)__part2$"), "precip_history_characteristic_code_{idx}"),
    (re.compile(r"^AC(?P<idx>\d+)__part3$"), "precip_history_quality_code_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part1$"), "precip_24h_max_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part2$"), "precip_24h_condition_code_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part3$"), "precip_24h_date_1_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part4$"), "precip_24h_date_2_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part5$"), "precip_24h_date_3_{idx}"),
    (re.compile(r"^AD(?P<idx>\d+)__part6$"), "precip_24h_quality_code_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part1$"), "precip_days_ge_001_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part2$"), "precip_days_ge_001_quality_code_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part3$"), "precip_days_ge_010_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part4$"), "precip_days_ge_010_quality_code_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part5$"), "precip_days_ge_050_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part6$"), "precip_days_ge_050_quality_code_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part7$"), "precip_days_ge_100_{idx}"),
    (re.compile(r"^AE(?P<idx>\d+)__part8$"), "precip_days_ge_100_quality_code_{idx}"),
    (re.compile(r"^AG(?P<idx>\d+)__part1$"), "precip_estimated_discrepancy_code_{idx}"),
    (re.compile(r"^AG(?P<idx>\d+)__part2$"), "precip_estimated_depth_mm_{idx}"),
    (re.compile(r"^AH(?P<idx>\d+)__part1$"), "precip_short_duration_period_minutes_{idx}"),
    (re.compile(r"^AH(?P<idx>\d+)__part2$"), "precip_short_duration_amount_mm_{idx}"),
    (re.compile(r"^AH(?P<idx>\d+)__part3$"), "precip_short_duration_condition_code_{idx}"),
    (re.compile(r"^AH(?P<idx>\d+)__part4$"), "precip_short_duration_end_datetime_{idx}"),
    (re.compile(r"^AH(?P<idx>\d+)__part5$"), "precip_short_duration_quality_code_{idx}"),
    (re.compile(r"^AI(?P<idx>\d+)__part1$"), "precip_short_duration_period_minutes_{idx}"),
    (re.compile(r"^AI(?P<idx>\d+)__part2$"), "precip_short_duration_amount_mm_{idx}"),
    (re.compile(r"^AI(?P<idx>\d+)__part3$"), "precip_short_duration_condition_code_{idx}"),
    (re.compile(r"^AI(?P<idx>\d+)__part4$"), "precip_short_duration_end_datetime_{idx}"),
    (re.compile(r"^AI(?P<idx>\d+)__part5$"), "precip_short_duration_quality_code_{idx}"),
    (re.compile(r"^AK(?P<idx>\d+)__part1$"), "snow_depth_monthly_max_{idx}"),
    (re.compile(r"^AK(?P<idx>\d+)__part2$"), "snow_depth_monthly_max_condition_code_{idx}"),
    (re.compile(r"^AK(?P<idx>\d+)__part3$"), "snow_depth_monthly_max_dates_{idx}"),
    (re.compile(r"^AK(?P<idx>\d+)__part4$"), "snow_depth_monthly_max_quality_code_{idx}"),
    (re.compile(r"^AL(?P<idx>\d+)__part1$"), "snow_accum_period_hours_{idx}"),
    (re.compile(r"^AL(?P<idx>\d+)__part2$"), "snow_accum_depth_cm_{idx}"),
    (re.compile(r"^AL(?P<idx>\d+)__part3$"), "snow_accum_condition_code_{idx}"),
    (re.compile(r"^AL(?P<idx>\d+)__part4$"), "snow_accum_quality_code_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part1$"), "snow_accum_24h_max_cm_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part2$"), "snow_accum_24h_max_condition_code_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part3$"), "snow_accum_24h_date_1_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part4$"), "snow_accum_24h_date_2_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part5$"), "snow_accum_24h_date_3_{idx}"),
    (re.compile(r"^AM(?P<idx>\d+)__part6$"), "snow_accum_24h_max_quality_code_{idx}"),
    (re.compile(r"^AN(?P<idx>\d+)__part1$"), "snow_accum_day_month_period_hours_{idx}"),
    (re.compile(r"^AN(?P<idx>\d+)__part2$"), "snow_accum_day_month_depth_cm_{idx}"),
    (re.compile(r"^AN(?P<idx>\d+)__part3$"), "snow_accum_day_month_condition_code_{idx}"),
    (re.compile(r"^AN(?P<idx>\d+)__part4$"), "snow_accum_day_month_quality_code_{idx}"),
    (re.compile(r"^AO(?P<idx>\d+)__part1$"), "precip_minute_period_minutes_{idx}"),
    (re.compile(r"^AO(?P<idx>\d+)__part2$"), "precip_minute_amount_mm_{idx}"),
    (re.compile(r"^AO(?P<idx>\d+)__part3$"), "precip_minute_condition_code_{idx}"),
    (re.compile(r"^AO(?P<idx>\d+)__part4$"), "precip_minute_quality_code_{idx}"),
    (re.compile(r"^AP(?P<idx>\d+)__part1$"), "hpd_gauge_value_mm_{idx}"),
    (re.compile(r"^AP(?P<idx>\d+)__part2$"), "hpd_gauge_condition_code_{idx}"),
    (re.compile(r"^AP(?P<idx>\d+)__part3$"), "hpd_gauge_quality_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part1$"), "snow_depth_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part2$"), "snow_depth_condition_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part3$"), "snow_depth_quality_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part4$"), "snow_water_equivalent_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part5$"), "snow_water_condition_code_{idx}"),
    (re.compile(r"^AJ(?P<idx>\d+)__part6$"), "snow_water_quality_code_{idx}"),
    (re.compile(r"^AT(?P<idx>\d+)__part1$"), "daily_present_weather_source_{idx}"),
    (re.compile(r"^AT(?P<idx>\d+)__part2$"), "daily_present_weather_type_code_{idx}"),
    (re.compile(r"^AT(?P<idx>\d+)__part3$"), "daily_present_weather_type_abbr_{idx}"),
    (re.compile(r"^AT(?P<idx>\d+)__part4$"), "daily_present_weather_quality_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part1$"), "weather_intensity_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part2$"), "weather_descriptor_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part3$"), "weather_precip_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part4$"), "weather_obscuration_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part5$"), "weather_other_code_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part6$"), "weather_combo_indicator_{idx}"),
    (re.compile(r"^AU(?P<idx>\d+)__part7$"), "weather_quality_code_{idx}"),
    (re.compile(r"^CB(?P<idx>\d+)__part1$"), "secondary_precip_period_minutes_{idx}"),
    (re.compile(r"^CB(?P<idx>\d+)__part2$"), "secondary_precip_depth_mm_{idx}"),
    (re.compile(r"^CB(?P<idx>\d+)__part3$"), "secondary_precip_qc_{idx}"),
    (re.compile(r"^CB(?P<idx>\d+)__part4$"), "secondary_precip_flag_{idx}"),
    (re.compile(r"^CF(?P<idx>\d+)__part1$"), "crn_fan_speed_rps_{idx}"),
    (re.compile(r"^CF(?P<idx>\d+)__part2$"), "crn_fan_speed_qc_{idx}"),
    (re.compile(r"^CF(?P<idx>\d+)__part3$"), "crn_fan_speed_flag_{idx}"),
    (re.compile(r"^CG(?P<idx>\d+)__part1$"), "primary_precip_depth_mm_{idx}"),
    (re.compile(r"^CG(?P<idx>\d+)__part2$"), "primary_precip_qc_{idx}"),
    (re.compile(r"^CG(?P<idx>\d+)__part3$"), "primary_precip_flag_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part1$"), "rh_temp_period_minutes_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part2$"), "rh_temp_avg_c_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part3$"), "rh_temp_avg_qc_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part4$"), "rh_temp_avg_flag_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part5$"), "rh_avg_percent_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part6$"), "rh_avg_qc_{idx}"),
    (re.compile(r"^CH(?P<idx>\d+)__part7$"), "rh_avg_flag_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part1$"), "rh_temp_min_c_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part2$"), "rh_temp_min_qc_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part3$"), "rh_temp_min_flag_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part4$"), "rh_temp_max_c_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part5$"), "rh_temp_max_qc_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part6$"), "rh_temp_max_flag_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part7$"), "rh_temp_std_c_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part8$"), "rh_temp_std_qc_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part9$"), "rh_temp_std_flag_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part10$"), "rh_std_percent_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part11$"), "rh_std_qc_{idx}"),
    (re.compile(r"^CI(?P<idx>\d+)__part12$"), "rh_std_flag_{idx}"),
    (re.compile(r"^CO(?P<idx>[2-9])__part1$"), "coop_element_id_{idx}"),
    (re.compile(r"^CO(?P<idx>[2-9])__part2$"), "coop_time_offset_hours_{idx}"),
    (re.compile(r"^CT(?P<idx>\d+)__part1$"), "subhourly_temp_avg_c_{idx}"),
    (re.compile(r"^CT(?P<idx>\d+)__part2$"), "subhourly_temp_avg_qc_{idx}"),
    (re.compile(r"^CT(?P<idx>\d+)__part3$"), "subhourly_temp_avg_flag_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part1$"), "hourly_temp_avg_c_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part2$"), "hourly_temp_avg_qc_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part3$"), "hourly_temp_avg_flag_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part4$"), "hourly_temp_std_c_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part5$"), "hourly_temp_std_qc_{idx}"),
    (re.compile(r"^CU(?P<idx>\d+)__part6$"), "hourly_temp_std_flag_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part1$"), "hourly_temp_min_c_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part2$"), "hourly_temp_min_qc_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part3$"), "hourly_temp_min_flag_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part4$"), "hourly_temp_min_time_hhmm_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part5$"), "hourly_temp_min_time_qc_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part6$"), "hourly_temp_min_time_flag_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part7$"), "hourly_temp_max_c_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part8$"), "hourly_temp_max_qc_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part9$"), "hourly_temp_max_flag_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part10$"), "hourly_temp_max_time_hhmm_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part11$"), "hourly_temp_max_time_qc_{idx}"),
    (re.compile(r"^CV(?P<idx>\d+)__part12$"), "hourly_temp_max_time_flag_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part1$"), "wetness_channel1_value_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part2$"), "wetness_channel1_qc_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part3$"), "wetness_channel1_flag_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part4$"), "wetness_channel2_value_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part5$"), "wetness_channel2_qc_{idx}"),
    (re.compile(r"^CW(?P<idx>\d+)__part6$"), "wetness_channel2_flag_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part1$"), "geonor_precip_total_mm_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part2$"), "geonor_precip_qc_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part3$"), "geonor_precip_flag_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part4$"), "geonor_freq_avg_hz_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part5$"), "geonor_freq_avg_qc_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part6$"), "geonor_freq_avg_flag_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part7$"), "geonor_freq_min_hz_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part8$"), "geonor_freq_min_qc_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part9$"), "geonor_freq_min_flag_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part10$"), "geonor_freq_max_hz_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part11$"), "geonor_freq_max_qc_{idx}"),
    (re.compile(r"^CX(?P<idx>\d+)__part12$"), "geonor_freq_max_flag_{idx}"),
    (re.compile(r"^CN1__part1$"), "battery_voltage_avg_v_1"),
    (re.compile(r"^CN1__part2$"), "battery_voltage_avg_qc_1"),
    (re.compile(r"^CN1__part3$"), "battery_voltage_avg_flag_1"),
    (re.compile(r"^CN1__part4$"), "battery_voltage_full_load_v_1"),
    (re.compile(r"^CN1__part5$"), "battery_voltage_full_load_qc_1"),
    (re.compile(r"^CN1__part6$"), "battery_voltage_full_load_flag_1"),
    (re.compile(r"^CN1__part7$"), "battery_voltage_datalogger_v_1"),
    (re.compile(r"^CN1__part8$"), "battery_voltage_datalogger_qc_1"),
    (re.compile(r"^CN1__part9$"), "battery_voltage_datalogger_flag_1"),
    (re.compile(r"^CN2__part1$"), "panel_temp_c_1"),
    (re.compile(r"^CN2__part2$"), "panel_temp_qc_1"),
    (re.compile(r"^CN2__part3$"), "panel_temp_flag_1"),
    (re.compile(r"^CN2__part4$"), "inlet_temp_max_c_1"),
    (re.compile(r"^CN2__part5$"), "inlet_temp_max_qc_1"),
    (re.compile(r"^CN2__part6$"), "inlet_temp_max_flag_1"),
    (re.compile(r"^CN2__part7$"), "door_open_minutes_1"),
    (re.compile(r"^CN2__part8$"), "door_open_qc_1"),
    (re.compile(r"^CN2__part9$"), "door_open_flag_1"),
    (re.compile(r"^CN3__part1$"), "reference_resistance_ohm_1"),
    (re.compile(r"^CN3__part2$"), "reference_resistance_qc_1"),
    (re.compile(r"^CN3__part3$"), "reference_resistance_flag_1"),
    (re.compile(r"^CN3__part4$"), "datalogger_signature_1"),
    (re.compile(r"^CN3__part5$"), "datalogger_signature_qc_1"),
    (re.compile(r"^CN3__part6$"), "datalogger_signature_flag_1"),
    (re.compile(r"^CN4__part1$"), "precip_heater_flag_1"),
    (re.compile(r"^CN4__part2$"), "precip_heater_qc_1"),
    (re.compile(r"^CN4__part3$"), "precip_heater_flag_code_1"),
    (re.compile(r"^CN4__part4$"), "datalogger_door_flag_1"),
    (re.compile(r"^CN4__part5$"), "datalogger_door_flag_qc_1"),
    (re.compile(r"^CN4__part6$"), "datalogger_door_flag_code_1"),
    (re.compile(r"^CN4__part7$"), "forward_transmitter_wattage_1"),
    (re.compile(r"^CN4__part8$"), "forward_transmitter_qc_1"),
    (re.compile(r"^CN4__part9$"), "forward_transmitter_flag_1"),
    (re.compile(r"^CN4__part10$"), "reflected_transmitter_wattage_1"),
    (re.compile(r"^CN4__part11$"), "reflected_transmitter_qc_1"),
    (re.compile(r"^CN4__part12$"), "reflected_transmitter_flag_1"),
    (re.compile(r"^GA(?P<idx>\d+)__part1$"), "cloud_layer_coverage_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part2$"), "cloud_layer_coverage_quality_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part3$"), "cloud_layer_base_height_m_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part4$"), "cloud_layer_base_height_quality_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part5$"), "cloud_layer_type_code_{idx}"),
    (re.compile(r"^GA(?P<idx>\d+)__part6$"), "cloud_layer_type_quality_code_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part3$"), "extreme_temp_c_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part2$"), "extreme_temp_type_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part1$"), "extreme_temp_period_hours_{idx}"),
    (re.compile(r"^KA(?P<idx>\d+)__part4$"), "extreme_temp_quality_code_{idx}"),
    (re.compile(r"^KC(?P<idx>\d+)__part1$"), "extreme_month_temp_type_{idx}"),
    (re.compile(r"^KC(?P<idx>\d+)__part2$"), "extreme_month_temp_condition_{idx}"),
    (re.compile(r"^KC(?P<idx>\d+)__part3$"), "extreme_month_temp_c_{idx}"),
    (re.compile(r"^KC(?P<idx>\d+)__part4$"), "extreme_month_temp_dates_{idx}"),
    (re.compile(r"^KC(?P<idx>\d+)__part5$"), "extreme_month_temp_quality_code_{idx}"),
    (re.compile(r"^KD(?P<idx>\d+)__part1$"), "degree_days_period_hours_{idx}"),
    (re.compile(r"^KD(?P<idx>\d+)__part2$"), "degree_days_type_{idx}"),
    (re.compile(r"^KD(?P<idx>\d+)__part3$"), "degree_days_value_{idx}"),
    (re.compile(r"^KD(?P<idx>\d+)__part4$"), "degree_days_quality_code_{idx}"),
    (re.compile(r"^KG(?P<idx>\d+)__part1$"), "avg_dew_wet_period_hours_{idx}"),
    (re.compile(r"^KG(?P<idx>\d+)__part2$"), "avg_dew_wet_type_{idx}"),
    (re.compile(r"^KG(?P<idx>\d+)__part3$"), "avg_dew_wet_temp_c_{idx}"),
    (re.compile(r"^KG(?P<idx>\d+)__part4$"), "avg_dew_wet_derived_code_{idx}"),
    (re.compile(r"^KG(?P<idx>\d+)__part5$"), "avg_dew_wet_quality_code_{idx}"),
    (re.compile(r"^KB(?P<idx>\d+)__part1$"), "avg_air_temp_period_hours_{idx}"),
    (re.compile(r"^KB(?P<idx>\d+)__part2$"), "avg_air_temp_type_{idx}"),
    (re.compile(r"^KB(?P<idx>\d+)__part3$"), "avg_air_temp_c_{idx}"),
    (re.compile(r"^KB(?P<idx>\d+)__part4$"), "avg_air_temp_quality_code_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part1$"), "sky_cover_summation_code_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part2$"), "sky_cover_summation_okta_code_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part3$"), "sky_cover_summation_quality_code_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part4$"), "sky_cover_summation_height_m_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part5$"), "sky_cover_summation_height_quality_code_{idx}"),
    (re.compile(r"^GD(?P<idx>\d+)__part6$"), "sky_cover_summation_characteristic_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part1$"), "below_station_cloud_coverage_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part2$"), "below_station_cloud_coverage_quality_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part3$"), "below_station_cloud_top_height_m_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part4$"), "below_station_cloud_top_height_quality_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part5$"), "below_station_cloud_type_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part6$"), "below_station_cloud_type_quality_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part7$"), "below_station_cloud_top_code_{idx}"),
    (re.compile(r"^GG(?P<idx>\d+)__part8$"), "below_station_cloud_top_quality_code_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part1$"), "solar_radiation_avg_wm2_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part2$"), "solar_radiation_avg_qc_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part3$"), "solar_radiation_avg_flag_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part4$"), "solar_radiation_min_wm2_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part5$"), "solar_radiation_min_qc_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part6$"), "solar_radiation_min_flag_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part7$"), "solar_radiation_max_wm2_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part8$"), "solar_radiation_max_qc_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part9$"), "solar_radiation_max_flag_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part10$"), "solar_radiation_std_wm2_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part11$"), "solar_radiation_std_qc_{idx}"),
    (re.compile(r"^GH(?P<idx>\d+)__part12$"), "solar_radiation_std_flag_{idx}"),
    (re.compile(r"^GJ(?P<idx>\d+)__part1$"), "sunshine_duration_minutes_{idx}"),
    (re.compile(r"^GJ(?P<idx>\d+)__part2$"), "sunshine_duration_quality_code_{idx}"),
    (re.compile(r"^GK(?P<idx>\d+)__part1$"), "sunshine_percent_{idx}"),
    (re.compile(r"^GK(?P<idx>\d+)__part2$"), "sunshine_percent_quality_code_{idx}"),
    (re.compile(r"^GL(?P<idx>\d+)__part1$"), "sunshine_month_minutes_{idx}"),
    (re.compile(r"^GL(?P<idx>\d+)__part2$"), "sunshine_month_quality_code_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part1$"), "solar_irradiance_period_minutes_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part2$"), "global_irradiance_wm2_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part3$"), "global_irradiance_flag_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part4$"), "global_irradiance_quality_code_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part5$"), "direct_beam_irradiance_wm2_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part6$"), "direct_beam_irradiance_flag_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part7$"), "direct_beam_irradiance_quality_code_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part8$"), "diffuse_irradiance_wm2_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part9$"), "diffuse_irradiance_flag_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part10$"), "diffuse_irradiance_quality_code_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part11$"), "uvb_global_irradiance_mw_m2_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part12$"), "uvb_global_irradiance_flag_{idx}"),
    (re.compile(r"^GM(?P<idx>\d+)__part13$"), "uvb_global_irradiance_quality_code_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part1$"), "solar_radiation_period_minutes_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part2$"), "upwelling_global_solar_radiation_mw_m2_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part3$"), "upwelling_global_solar_radiation_quality_code_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part4$"), "downwelling_thermal_ir_mw_m2_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part5$"), "downwelling_thermal_ir_quality_code_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part6$"), "upwelling_thermal_ir_mw_m2_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part7$"), "upwelling_thermal_ir_quality_code_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part8$"), "photosynthetic_radiation_mw_m2_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part9$"), "photosynthetic_radiation_quality_code_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part10$"), "solar_zenith_angle_deg_{idx}"),
    (re.compile(r"^GN(?P<idx>\d+)__part11$"), "solar_zenith_angle_quality_code_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part1$"), "net_radiation_period_minutes_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part2$"), "net_solar_radiation_wm2_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part3$"), "net_solar_radiation_quality_code_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part4$"), "net_infrared_radiation_wm2_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part5$"), "net_infrared_radiation_quality_code_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part6$"), "net_radiation_wm2_{idx}"),
    (re.compile(r"^GO(?P<idx>\d+)__part7$"), "net_radiation_quality_code_{idx}"),
    (re.compile(r"^GP1__part1$"), "modeled_solar_period_minutes"),
    (re.compile(r"^GP1__part2$"), "modeled_global_horizontal_wm2"),
    (re.compile(r"^GP1__part3$"), "modeled_global_horizontal_source_flag"),
    (re.compile(r"^GP1__part4$"), "modeled_global_horizontal_uncertainty_pct"),
    (re.compile(r"^GP1__part5$"), "modeled_direct_normal_wm2"),
    (re.compile(r"^GP1__part6$"), "modeled_direct_normal_source_flag"),
    (re.compile(r"^GP1__part7$"), "modeled_direct_normal_uncertainty_pct"),
    (re.compile(r"^GP1__part8$"), "modeled_diffuse_horizontal_wm2"),
    (re.compile(r"^GP1__part9$"), "modeled_diffuse_horizontal_source_flag"),
    (re.compile(r"^GP1__part10$"), "modeled_diffuse_horizontal_uncertainty_pct"),
    (re.compile(r"^OA(?P<idx>\d+)__part1$"), "supp_wind_oa_type_code_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part2$"), "supp_wind_oa_period_hours_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part3$"), "supp_wind_oa_speed_ms_{idx}"),
    (re.compile(r"^OA(?P<idx>\d+)__part4$"), "supp_wind_oa_speed_quality_code_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part1$"), "supp_wind_type_code_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part2$"), "supp_wind_period_hours_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part3$"), "supp_wind_direction_deg_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part4$"), "supp_wind_speed_ms_{idx}"),
    (re.compile(r"^OD(?P<idx>\d+)__part5$"), "supp_wind_speed_quality_code_{idx}"),
]

_INTERNAL_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^present_weather_code_(?P<idx>\d+)$"), "MW{idx}__part1"),
    (re.compile(r"^present_weather_vicinity_code_(?P<idx>\d+)$"), "MV{idx}__part1"),
    (re.compile(r"^present_weather_vicinity_quality_code_(?P<idx>\d+)$"), "MV{idx}__part2"),
    (re.compile(r"^past_weather_condition_code_(?P<idx>\d+)$"), "AY{idx}__part1"),
    (re.compile(r"^past_weather_period_hours_(?P<idx>\d+)$"), "AY{idx}__part3"),
    (re.compile(r"^precip_period_hours_(?P<idx>\d+)$"), "AA{idx}__part1"),
    (re.compile(r"^precip_amount_(?P<idx>\d+)$"), "AA{idx}__part2"),
    (re.compile(r"^precip_condition_code_(?P<idx>\d+)$"), "AA{idx}__part3"),
    (re.compile(r"^precip_quality_code_(?P<idx>\d+)$"), "AA{idx}__part4"),
    (re.compile(r"^precip_monthly_total_(?P<idx>\d+)$"), "AB{idx}__part1"),
    (re.compile(r"^precip_monthly_condition_code_(?P<idx>\d+)$"), "AB{idx}__part2"),
    (re.compile(r"^precip_monthly_quality_code_(?P<idx>\d+)$"), "AB{idx}__part3"),
    (re.compile(r"^precip_history_duration_code_(?P<idx>\d+)$"), "AC{idx}__part1"),
    (re.compile(r"^precip_history_characteristic_code_(?P<idx>\d+)$"), "AC{idx}__part2"),
    (re.compile(r"^precip_history_quality_code_(?P<idx>\d+)$"), "AC{idx}__part3"),
    (re.compile(r"^precip_24h_max_(?P<idx>\d+)$"), "AD{idx}__part1"),
    (re.compile(r"^precip_24h_condition_code_(?P<idx>\d+)$"), "AD{idx}__part2"),
    (re.compile(r"^precip_24h_date_1_(?P<idx>\d+)$"), "AD{idx}__part3"),
    (re.compile(r"^precip_24h_date_2_(?P<idx>\d+)$"), "AD{idx}__part4"),
    (re.compile(r"^precip_24h_date_3_(?P<idx>\d+)$"), "AD{idx}__part5"),
    (re.compile(r"^precip_24h_quality_code_(?P<idx>\d+)$"), "AD{idx}__part6"),
    (re.compile(r"^precip_days_ge_001_(?P<idx>\d+)$"), "AE{idx}__part1"),
    (re.compile(r"^precip_days_ge_001_quality_code_(?P<idx>\d+)$"), "AE{idx}__part2"),
    (re.compile(r"^precip_days_ge_010_(?P<idx>\d+)$"), "AE{idx}__part3"),
    (re.compile(r"^precip_days_ge_010_quality_code_(?P<idx>\d+)$"), "AE{idx}__part4"),
    (re.compile(r"^precip_days_ge_050_(?P<idx>\d+)$"), "AE{idx}__part5"),
    (re.compile(r"^precip_days_ge_050_quality_code_(?P<idx>\d+)$"), "AE{idx}__part6"),
    (re.compile(r"^precip_days_ge_100_(?P<idx>\d+)$"), "AE{idx}__part7"),
    (re.compile(r"^precip_days_ge_100_quality_code_(?P<idx>\d+)$"), "AE{idx}__part8"),
    (re.compile(r"^precip_estimated_discrepancy_code_(?P<idx>\d+)$"), "AG{idx}__part1"),
    (re.compile(r"^precip_estimated_depth_mm_(?P<idx>\d+)$"), "AG{idx}__part2"),
    (re.compile(r"^precip_short_duration_period_minutes_(?P<idx>\d+)$"), "AH{idx}__part1"),
    (re.compile(r"^precip_short_duration_amount_mm_(?P<idx>\d+)$"), "AH{idx}__part2"),
    (re.compile(r"^precip_short_duration_condition_code_(?P<idx>\d+)$"), "AH{idx}__part3"),
    (re.compile(r"^precip_short_duration_end_datetime_(?P<idx>\d+)$"), "AH{idx}__part4"),
    (re.compile(r"^precip_short_duration_quality_code_(?P<idx>\d+)$"), "AH{idx}__part5"),
    (re.compile(r"^snow_depth_monthly_max_(?P<idx>\d+)$"), "AK{idx}__part1"),
    (re.compile(r"^snow_depth_monthly_max_condition_code_(?P<idx>\d+)$"), "AK{idx}__part2"),
    (re.compile(r"^snow_depth_monthly_max_dates_(?P<idx>\d+)$"), "AK{idx}__part3"),
    (re.compile(r"^snow_depth_monthly_max_quality_code_(?P<idx>\d+)$"), "AK{idx}__part4"),
    (re.compile(r"^snow_accum_period_hours_(?P<idx>\d+)$"), "AL{idx}__part1"),
    (re.compile(r"^snow_accum_depth_cm_(?P<idx>\d+)$"), "AL{idx}__part2"),
    (re.compile(r"^snow_accum_condition_code_(?P<idx>\d+)$"), "AL{idx}__part3"),
    (re.compile(r"^snow_accum_quality_code_(?P<idx>\d+)$"), "AL{idx}__part4"),
    (re.compile(r"^snow_accum_24h_max_cm_(?P<idx>\d+)$"), "AM{idx}__part1"),
    (re.compile(r"^snow_accum_24h_max_condition_code_(?P<idx>\d+)$"), "AM{idx}__part2"),
    (re.compile(r"^snow_accum_24h_date_1_(?P<idx>\d+)$"), "AM{idx}__part3"),
    (re.compile(r"^snow_accum_24h_date_2_(?P<idx>\d+)$"), "AM{idx}__part4"),
    (re.compile(r"^snow_accum_24h_date_3_(?P<idx>\d+)$"), "AM{idx}__part5"),
    (re.compile(r"^snow_accum_24h_max_quality_code_(?P<idx>\d+)$"), "AM{idx}__part6"),
    (re.compile(r"^snow_accum_day_month_period_hours_(?P<idx>\d+)$"), "AN{idx}__part1"),
    (re.compile(r"^snow_accum_day_month_depth_cm_(?P<idx>\d+)$"), "AN{idx}__part2"),
    (re.compile(r"^snow_accum_day_month_condition_code_(?P<idx>\d+)$"), "AN{idx}__part3"),
    (re.compile(r"^snow_accum_day_month_quality_code_(?P<idx>\d+)$"), "AN{idx}__part4"),
    (re.compile(r"^precip_minute_period_minutes_(?P<idx>\d+)$"), "AO{idx}__part1"),
    (re.compile(r"^precip_minute_amount_mm_(?P<idx>\d+)$"), "AO{idx}__part2"),
    (re.compile(r"^precip_minute_condition_code_(?P<idx>\d+)$"), "AO{idx}__part3"),
    (re.compile(r"^precip_minute_quality_code_(?P<idx>\d+)$"), "AO{idx}__part4"),
    (re.compile(r"^hpd_gauge_value_mm_(?P<idx>\d+)$"), "AP{idx}__part1"),
    (re.compile(r"^hpd_gauge_condition_code_(?P<idx>\d+)$"), "AP{idx}__part2"),
    (re.compile(r"^hpd_gauge_quality_code_(?P<idx>\d+)$"), "AP{idx}__part3"),
    (re.compile(r"^snow_depth_(?P<idx>\d+)$"), "AJ{idx}__part1"),
    (re.compile(r"^snow_depth_condition_code_(?P<idx>\d+)$"), "AJ{idx}__part2"),
    (re.compile(r"^snow_depth_quality_code_(?P<idx>\d+)$"), "AJ{idx}__part3"),
    (re.compile(r"^snow_water_equivalent_(?P<idx>\d+)$"), "AJ{idx}__part4"),
    (re.compile(r"^snow_water_condition_code_(?P<idx>\d+)$"), "AJ{idx}__part5"),
    (re.compile(r"^snow_water_quality_code_(?P<idx>\d+)$"), "AJ{idx}__part6"),
    (re.compile(r"^daily_present_weather_source_(?P<idx>\d+)$"), "AT{idx}__part1"),
    (re.compile(r"^daily_present_weather_type_code_(?P<idx>\d+)$"), "AT{idx}__part2"),
    (re.compile(r"^daily_present_weather_type_abbr_(?P<idx>\d+)$"), "AT{idx}__part3"),
    (re.compile(r"^daily_present_weather_quality_code_(?P<idx>\d+)$"), "AT{idx}__part4"),
    (re.compile(r"^weather_intensity_code_(?P<idx>\d+)$"), "AU{idx}__part1"),
    (re.compile(r"^weather_descriptor_code_(?P<idx>\d+)$"), "AU{idx}__part2"),
    (re.compile(r"^weather_precip_code_(?P<idx>\d+)$"), "AU{idx}__part3"),
    (re.compile(r"^weather_obscuration_code_(?P<idx>\d+)$"), "AU{idx}__part4"),
    (re.compile(r"^weather_other_code_(?P<idx>\d+)$"), "AU{idx}__part5"),
    (re.compile(r"^weather_combo_indicator_(?P<idx>\d+)$"), "AU{idx}__part6"),
    (re.compile(r"^weather_quality_code_(?P<idx>\d+)$"), "AU{idx}__part7"),
    (re.compile(r"^secondary_precip_period_minutes_(?P<idx>\d+)$"), "CB{idx}__part1"),
    (re.compile(r"^secondary_precip_depth_mm_(?P<idx>\d+)$"), "CB{idx}__part2"),
    (re.compile(r"^secondary_precip_qc_(?P<idx>\d+)$"), "CB{idx}__part3"),
    (re.compile(r"^secondary_precip_flag_(?P<idx>\d+)$"), "CB{idx}__part4"),
    (re.compile(r"^crn_fan_speed_rps_(?P<idx>\d+)$"), "CF{idx}__part1"),
    (re.compile(r"^crn_fan_speed_qc_(?P<idx>\d+)$"), "CF{idx}__part2"),
    (re.compile(r"^crn_fan_speed_flag_(?P<idx>\d+)$"), "CF{idx}__part3"),
    (re.compile(r"^primary_precip_depth_mm_(?P<idx>\d+)$"), "CG{idx}__part1"),
    (re.compile(r"^primary_precip_qc_(?P<idx>\d+)$"), "CG{idx}__part2"),
    (re.compile(r"^primary_precip_flag_(?P<idx>\d+)$"), "CG{idx}__part3"),
    (re.compile(r"^rh_temp_period_minutes_(?P<idx>\d+)$"), "CH{idx}__part1"),
    (re.compile(r"^rh_temp_avg_c_(?P<idx>\d+)$"), "CH{idx}__part2"),
    (re.compile(r"^rh_temp_avg_qc_(?P<idx>\d+)$"), "CH{idx}__part3"),
    (re.compile(r"^rh_temp_avg_flag_(?P<idx>\d+)$"), "CH{idx}__part4"),
    (re.compile(r"^rh_avg_percent_(?P<idx>\d+)$"), "CH{idx}__part5"),
    (re.compile(r"^rh_avg_qc_(?P<idx>\d+)$"), "CH{idx}__part6"),
    (re.compile(r"^rh_avg_flag_(?P<idx>\d+)$"), "CH{idx}__part7"),
    (re.compile(r"^rh_temp_min_c_(?P<idx>\d+)$"), "CI{idx}__part1"),
    (re.compile(r"^rh_temp_min_qc_(?P<idx>\d+)$"), "CI{idx}__part2"),
    (re.compile(r"^rh_temp_min_flag_(?P<idx>\d+)$"), "CI{idx}__part3"),
    (re.compile(r"^rh_temp_max_c_(?P<idx>\d+)$"), "CI{idx}__part4"),
    (re.compile(r"^rh_temp_max_qc_(?P<idx>\d+)$"), "CI{idx}__part5"),
    (re.compile(r"^rh_temp_max_flag_(?P<idx>\d+)$"), "CI{idx}__part6"),
    (re.compile(r"^rh_temp_std_c_(?P<idx>\d+)$"), "CI{idx}__part7"),
    (re.compile(r"^rh_temp_std_qc_(?P<idx>\d+)$"), "CI{idx}__part8"),
    (re.compile(r"^rh_temp_std_flag_(?P<idx>\d+)$"), "CI{idx}__part9"),
    (re.compile(r"^rh_std_percent_(?P<idx>\d+)$"), "CI{idx}__part10"),
    (re.compile(r"^rh_std_qc_(?P<idx>\d+)$"), "CI{idx}__part11"),
    (re.compile(r"^rh_std_flag_(?P<idx>\d+)$"), "CI{idx}__part12"),
    (re.compile(r"^climate_division_number$"), "CO1__part1"),
    (re.compile(r"^utc_lst_offset_hours$"), "CO1__part2"),
    (re.compile(r"^coop_element_id_(?P<idx>[2-9])$"), "CO{idx}__part1"),
    (re.compile(r"^coop_time_offset_hours_(?P<idx>[2-9])$"), "CO{idx}__part2"),
    (re.compile(r"^crn_datalogger_version$"), "CR1__part1"),
    (re.compile(r"^crn_datalogger_version_qc$"), "CR1__part2"),
    (re.compile(r"^crn_datalogger_version_flag$"), "CR1__part3"),
    (re.compile(r"^subhourly_temp_avg_c_(?P<idx>\d+)$"), "CT{idx}__part1"),
    (re.compile(r"^subhourly_temp_avg_qc_(?P<idx>\d+)$"), "CT{idx}__part2"),
    (re.compile(r"^subhourly_temp_avg_flag_(?P<idx>\d+)$"), "CT{idx}__part3"),
    (re.compile(r"^hourly_temp_avg_c_(?P<idx>\d+)$"), "CU{idx}__part1"),
    (re.compile(r"^hourly_temp_avg_qc_(?P<idx>\d+)$"), "CU{idx}__part2"),
    (re.compile(r"^hourly_temp_avg_flag_(?P<idx>\d+)$"), "CU{idx}__part3"),
    (re.compile(r"^hourly_temp_std_c_(?P<idx>\d+)$"), "CU{idx}__part4"),
    (re.compile(r"^hourly_temp_std_qc_(?P<idx>\d+)$"), "CU{idx}__part5"),
    (re.compile(r"^hourly_temp_std_flag_(?P<idx>\d+)$"), "CU{idx}__part6"),
    (re.compile(r"^hourly_temp_min_c_(?P<idx>\d+)$"), "CV{idx}__part1"),
    (re.compile(r"^hourly_temp_min_qc_(?P<idx>\d+)$"), "CV{idx}__part2"),
    (re.compile(r"^hourly_temp_min_flag_(?P<idx>\d+)$"), "CV{idx}__part3"),
    (re.compile(r"^hourly_temp_min_time_hhmm_(?P<idx>\d+)$"), "CV{idx}__part4"),
    (re.compile(r"^hourly_temp_min_time_qc_(?P<idx>\d+)$"), "CV{idx}__part5"),
    (re.compile(r"^hourly_temp_min_time_flag_(?P<idx>\d+)$"), "CV{idx}__part6"),
    (re.compile(r"^hourly_temp_max_c_(?P<idx>\d+)$"), "CV{idx}__part7"),
    (re.compile(r"^hourly_temp_max_qc_(?P<idx>\d+)$"), "CV{idx}__part8"),
    (re.compile(r"^hourly_temp_max_flag_(?P<idx>\d+)$"), "CV{idx}__part9"),
    (re.compile(r"^hourly_temp_max_time_hhmm_(?P<idx>\d+)$"), "CV{idx}__part10"),
    (re.compile(r"^hourly_temp_max_time_qc_(?P<idx>\d+)$"), "CV{idx}__part11"),
    (re.compile(r"^hourly_temp_max_time_flag_(?P<idx>\d+)$"), "CV{idx}__part12"),
    (re.compile(r"^wetness_channel1_value_(?P<idx>\d+)$"), "CW{idx}__part1"),
    (re.compile(r"^wetness_channel1_qc_(?P<idx>\d+)$"), "CW{idx}__part2"),
    (re.compile(r"^wetness_channel1_flag_(?P<idx>\d+)$"), "CW{idx}__part3"),
    (re.compile(r"^wetness_channel2_value_(?P<idx>\d+)$"), "CW{idx}__part4"),
    (re.compile(r"^wetness_channel2_qc_(?P<idx>\d+)$"), "CW{idx}__part5"),
    (re.compile(r"^wetness_channel2_flag_(?P<idx>\d+)$"), "CW{idx}__part6"),
    (re.compile(r"^geonor_precip_total_mm_(?P<idx>\d+)$"), "CX{idx}__part1"),
    (re.compile(r"^geonor_precip_qc_(?P<idx>\d+)$"), "CX{idx}__part2"),
    (re.compile(r"^geonor_precip_flag_(?P<idx>\d+)$"), "CX{idx}__part3"),
    (re.compile(r"^geonor_freq_avg_hz_(?P<idx>\d+)$"), "CX{idx}__part4"),
    (re.compile(r"^geonor_freq_avg_qc_(?P<idx>\d+)$"), "CX{idx}__part5"),
    (re.compile(r"^geonor_freq_avg_flag_(?P<idx>\d+)$"), "CX{idx}__part6"),
    (re.compile(r"^geonor_freq_min_hz_(?P<idx>\d+)$"), "CX{idx}__part7"),
    (re.compile(r"^geonor_freq_min_qc_(?P<idx>\d+)$"), "CX{idx}__part8"),
    (re.compile(r"^geonor_freq_min_flag_(?P<idx>\d+)$"), "CX{idx}__part9"),
    (re.compile(r"^geonor_freq_max_hz_(?P<idx>\d+)$"), "CX{idx}__part10"),
    (re.compile(r"^geonor_freq_max_qc_(?P<idx>\d+)$"), "CX{idx}__part11"),
    (re.compile(r"^geonor_freq_max_flag_(?P<idx>\d+)$"), "CX{idx}__part12"),
    (re.compile(r"^battery_voltage_avg_v_1$"), "CN1__part1"),
    (re.compile(r"^battery_voltage_avg_qc_1$"), "CN1__part2"),
    (re.compile(r"^battery_voltage_avg_flag_1$"), "CN1__part3"),
    (re.compile(r"^battery_voltage_full_load_v_1$"), "CN1__part4"),
    (re.compile(r"^battery_voltage_full_load_qc_1$"), "CN1__part5"),
    (re.compile(r"^battery_voltage_full_load_flag_1$"), "CN1__part6"),
    (re.compile(r"^battery_voltage_datalogger_v_1$"), "CN1__part7"),
    (re.compile(r"^battery_voltage_datalogger_qc_1$"), "CN1__part8"),
    (re.compile(r"^battery_voltage_datalogger_flag_1$"), "CN1__part9"),
    (re.compile(r"^panel_temp_c_1$"), "CN2__part1"),
    (re.compile(r"^panel_temp_qc_1$"), "CN2__part2"),
    (re.compile(r"^panel_temp_flag_1$"), "CN2__part3"),
    (re.compile(r"^inlet_temp_max_c_1$"), "CN2__part4"),
    (re.compile(r"^inlet_temp_max_qc_1$"), "CN2__part5"),
    (re.compile(r"^inlet_temp_max_flag_1$"), "CN2__part6"),
    (re.compile(r"^door_open_minutes_1$"), "CN2__part7"),
    (re.compile(r"^door_open_qc_1$"), "CN2__part8"),
    (re.compile(r"^door_open_flag_1$"), "CN2__part9"),
    (re.compile(r"^reference_resistance_ohm_1$"), "CN3__part1"),
    (re.compile(r"^reference_resistance_qc_1$"), "CN3__part2"),
    (re.compile(r"^reference_resistance_flag_1$"), "CN3__part3"),
    (re.compile(r"^datalogger_signature_1$"), "CN3__part4"),
    (re.compile(r"^datalogger_signature_qc_1$"), "CN3__part5"),
    (re.compile(r"^datalogger_signature_flag_1$"), "CN3__part6"),
    (re.compile(r"^precip_heater_flag_1$"), "CN4__part1"),
    (re.compile(r"^precip_heater_qc_1$"), "CN4__part2"),
    (re.compile(r"^precip_heater_flag_code_1$"), "CN4__part3"),
    (re.compile(r"^datalogger_door_flag_1$"), "CN4__part4"),
    (re.compile(r"^datalogger_door_flag_qc_1$"), "CN4__part5"),
    (re.compile(r"^datalogger_door_flag_code_1$"), "CN4__part6"),
    (re.compile(r"^forward_transmitter_wattage_1$"), "CN4__part7"),
    (re.compile(r"^forward_transmitter_qc_1$"), "CN4__part8"),
    (re.compile(r"^forward_transmitter_flag_1$"), "CN4__part9"),
    (re.compile(r"^reflected_transmitter_wattage_1$"), "CN4__part10"),
    (re.compile(r"^reflected_transmitter_qc_1$"), "CN4__part11"),
    (re.compile(r"^reflected_transmitter_flag_1$"), "CN4__part12"),
    (re.compile(r"^cloud_layer_coverage_(?P<idx>\d+)$"), "GA{idx}__part1"),
    (re.compile(r"^cloud_layer_coverage_quality_code_(?P<idx>\d+)$"), "GA{idx}__part2"),
    (re.compile(r"^cloud_layer_base_height_m_(?P<idx>\d+)$"), "GA{idx}__part3"),
    (re.compile(r"^cloud_layer_base_height_quality_code_(?P<idx>\d+)$"), "GA{idx}__part4"),
    (re.compile(r"^cloud_layer_type_code_(?P<idx>\d+)$"), "GA{idx}__part5"),
    (re.compile(r"^cloud_layer_type_quality_code_(?P<idx>\d+)$"), "GA{idx}__part6"),
    (re.compile(r"^extreme_temp_c_(?P<idx>\d+)$"), "KA{idx}__part3"),
    (re.compile(r"^extreme_temp_type_(?P<idx>\d+)$"), "KA{idx}__part2"),
    (re.compile(r"^extreme_temp_period_hours_(?P<idx>\d+)$"), "KA{idx}__part1"),
    (re.compile(r"^extreme_temp_quality_code_(?P<idx>\d+)$"), "KA{idx}__part4"),
    (re.compile(r"^avg_air_temp_period_hours_(?P<idx>\d+)$"), "KB{idx}__part1"),
    (re.compile(r"^avg_air_temp_type_(?P<idx>\d+)$"), "KB{idx}__part2"),
    (re.compile(r"^avg_air_temp_c_(?P<idx>\d+)$"), "KB{idx}__part3"),
    (re.compile(r"^avg_air_temp_quality_code_(?P<idx>\d+)$"), "KB{idx}__part4"),
    (re.compile(r"^extreme_month_temp_type_(?P<idx>\d+)$"), "KC{idx}__part1"),
    (re.compile(r"^extreme_month_temp_condition_(?P<idx>\d+)$"), "KC{idx}__part2"),
    (re.compile(r"^extreme_month_temp_c_(?P<idx>\d+)$"), "KC{idx}__part3"),
    (re.compile(r"^extreme_month_temp_dates_(?P<idx>\d+)$"), "KC{idx}__part4"),
    (re.compile(r"^extreme_month_temp_quality_code_(?P<idx>\d+)$"), "KC{idx}__part5"),
    (re.compile(r"^degree_days_period_hours_(?P<idx>\d+)$"), "KD{idx}__part1"),
    (re.compile(r"^degree_days_type_(?P<idx>\d+)$"), "KD{idx}__part2"),
    (re.compile(r"^degree_days_value_(?P<idx>\d+)$"), "KD{idx}__part3"),
    (re.compile(r"^degree_days_quality_code_(?P<idx>\d+)$"), "KD{idx}__part4"),
    (re.compile(r"^avg_dew_wet_period_hours_(?P<idx>\d+)$"), "KG{idx}__part1"),
    (re.compile(r"^avg_dew_wet_type_(?P<idx>\d+)$"), "KG{idx}__part2"),
    (re.compile(r"^avg_dew_wet_temp_c_(?P<idx>\d+)$"), "KG{idx}__part3"),
    (re.compile(r"^avg_dew_wet_derived_code_(?P<idx>\d+)$"), "KG{idx}__part4"),
    (re.compile(r"^avg_dew_wet_quality_code_(?P<idx>\d+)$"), "KG{idx}__part5"),
    (re.compile(r"^sky_cover_summation_code_(?P<idx>\d+)$"), "GD{idx}__part1"),
    (re.compile(r"^sky_cover_summation_okta_code_(?P<idx>\d+)$"), "GD{idx}__part2"),
    (re.compile(r"^sky_cover_summation_quality_code_(?P<idx>\d+)$"), "GD{idx}__part3"),
    (re.compile(r"^sky_cover_summation_height_m_(?P<idx>\d+)$"), "GD{idx}__part4"),
    (re.compile(r"^sky_cover_summation_height_quality_code_(?P<idx>\d+)$"), "GD{idx}__part5"),
    (re.compile(r"^sky_cover_summation_characteristic_code_(?P<idx>\d+)$"), "GD{idx}__part6"),
    (re.compile(r"^below_station_cloud_coverage_(?P<idx>\d+)$"), "GG{idx}__part1"),
    (re.compile(r"^below_station_cloud_coverage_quality_code_(?P<idx>\d+)$"), "GG{idx}__part2"),
    (re.compile(r"^below_station_cloud_top_height_m_(?P<idx>\d+)$"), "GG{idx}__part3"),
    (re.compile(r"^below_station_cloud_top_height_quality_code_(?P<idx>\d+)$"), "GG{idx}__part4"),
    (re.compile(r"^below_station_cloud_type_code_(?P<idx>\d+)$"), "GG{idx}__part5"),
    (re.compile(r"^below_station_cloud_type_quality_code_(?P<idx>\d+)$"), "GG{idx}__part6"),
    (re.compile(r"^below_station_cloud_top_code_(?P<idx>\d+)$"), "GG{idx}__part7"),
    (re.compile(r"^below_station_cloud_top_quality_code_(?P<idx>\d+)$"), "GG{idx}__part8"),
    (re.compile(r"^solar_radiation_avg_wm2_(?P<idx>\d+)$"), "GH{idx}__part1"),
    (re.compile(r"^solar_radiation_avg_qc_(?P<idx>\d+)$"), "GH{idx}__part2"),
    (re.compile(r"^solar_radiation_avg_flag_(?P<idx>\d+)$"), "GH{idx}__part3"),
    (re.compile(r"^solar_radiation_min_wm2_(?P<idx>\d+)$"), "GH{idx}__part4"),
    (re.compile(r"^solar_radiation_min_qc_(?P<idx>\d+)$"), "GH{idx}__part5"),
    (re.compile(r"^solar_radiation_min_flag_(?P<idx>\d+)$"), "GH{idx}__part6"),
    (re.compile(r"^solar_radiation_max_wm2_(?P<idx>\d+)$"), "GH{idx}__part7"),
    (re.compile(r"^solar_radiation_max_qc_(?P<idx>\d+)$"), "GH{idx}__part8"),
    (re.compile(r"^solar_radiation_max_flag_(?P<idx>\d+)$"), "GH{idx}__part9"),
    (re.compile(r"^solar_radiation_std_wm2_(?P<idx>\d+)$"), "GH{idx}__part10"),
    (re.compile(r"^solar_radiation_std_qc_(?P<idx>\d+)$"), "GH{idx}__part11"),
    (re.compile(r"^solar_radiation_std_flag_(?P<idx>\d+)$"), "GH{idx}__part12"),
    (re.compile(r"^sunshine_duration_minutes_(?P<idx>\d+)$"), "GJ{idx}__part1"),
    (re.compile(r"^sunshine_duration_quality_code_(?P<idx>\d+)$"), "GJ{idx}__part2"),
    (re.compile(r"^sunshine_percent_(?P<idx>\d+)$"), "GK{idx}__part1"),
    (re.compile(r"^sunshine_percent_quality_code_(?P<idx>\d+)$"), "GK{idx}__part2"),
    (re.compile(r"^sunshine_month_minutes_(?P<idx>\d+)$"), "GL{idx}__part1"),
    (re.compile(r"^sunshine_month_quality_code_(?P<idx>\d+)$"), "GL{idx}__part2"),
    (re.compile(r"^solar_irradiance_period_minutes_(?P<idx>\d+)$"), "GM{idx}__part1"),
    (re.compile(r"^global_irradiance_wm2_(?P<idx>\d+)$"), "GM{idx}__part2"),
    (re.compile(r"^global_irradiance_flag_(?P<idx>\d+)$"), "GM{idx}__part3"),
    (re.compile(r"^global_irradiance_quality_code_(?P<idx>\d+)$"), "GM{idx}__part4"),
    (re.compile(r"^direct_beam_irradiance_wm2_(?P<idx>\d+)$"), "GM{idx}__part5"),
    (re.compile(r"^direct_beam_irradiance_flag_(?P<idx>\d+)$"), "GM{idx}__part6"),
    (re.compile(r"^direct_beam_irradiance_quality_code_(?P<idx>\d+)$"), "GM{idx}__part7"),
    (re.compile(r"^diffuse_irradiance_wm2_(?P<idx>\d+)$"), "GM{idx}__part8"),
    (re.compile(r"^diffuse_irradiance_flag_(?P<idx>\d+)$"), "GM{idx}__part9"),
    (re.compile(r"^diffuse_irradiance_quality_code_(?P<idx>\d+)$"), "GM{idx}__part10"),
    (re.compile(r"^uvb_global_irradiance_mw_m2_(?P<idx>\d+)$"), "GM{idx}__part11"),
    (re.compile(r"^uvb_global_irradiance_flag_(?P<idx>\d+)$"), "GM{idx}__part12"),
    (re.compile(r"^uvb_global_irradiance_quality_code_(?P<idx>\d+)$"), "GM{idx}__part13"),
    (re.compile(r"^solar_radiation_period_minutes_(?P<idx>\d+)$"), "GN{idx}__part1"),
    (re.compile(r"^upwelling_global_solar_radiation_mw_m2_(?P<idx>\d+)$"), "GN{idx}__part2"),
    (re.compile(r"^upwelling_global_solar_radiation_quality_code_(?P<idx>\d+)$"), "GN{idx}__part3"),
    (re.compile(r"^downwelling_thermal_ir_mw_m2_(?P<idx>\d+)$"), "GN{idx}__part4"),
    (re.compile(r"^downwelling_thermal_ir_quality_code_(?P<idx>\d+)$"), "GN{idx}__part5"),
    (re.compile(r"^upwelling_thermal_ir_mw_m2_(?P<idx>\d+)$"), "GN{idx}__part6"),
    (re.compile(r"^upwelling_thermal_ir_quality_code_(?P<idx>\d+)$"), "GN{idx}__part7"),
    (re.compile(r"^photosynthetic_radiation_mw_m2_(?P<idx>\d+)$"), "GN{idx}__part8"),
    (re.compile(r"^photosynthetic_radiation_quality_code_(?P<idx>\d+)$"), "GN{idx}__part9"),
    (re.compile(r"^solar_zenith_angle_deg_(?P<idx>\d+)$"), "GN{idx}__part10"),
    (re.compile(r"^solar_zenith_angle_quality_code_(?P<idx>\d+)$"), "GN{idx}__part11"),
    (re.compile(r"^net_radiation_period_minutes_(?P<idx>\d+)$"), "GO{idx}__part1"),
    (re.compile(r"^net_solar_radiation_wm2_(?P<idx>\d+)$"), "GO{idx}__part2"),
    (re.compile(r"^net_solar_radiation_quality_code_(?P<idx>\d+)$"), "GO{idx}__part3"),
    (re.compile(r"^net_infrared_radiation_wm2_(?P<idx>\d+)$"), "GO{idx}__part4"),
    (re.compile(r"^net_infrared_radiation_quality_code_(?P<idx>\d+)$"), "GO{idx}__part5"),
    (re.compile(r"^net_radiation_wm2_(?P<idx>\d+)$"), "GO{idx}__part6"),
    (re.compile(r"^net_radiation_quality_code_(?P<idx>\d+)$"), "GO{idx}__part7"),
    (re.compile(r"^modeled_solar_period_minutes$"), "GP1__part1"),
    (re.compile(r"^modeled_global_horizontal_wm2$"), "GP1__part2"),
    (re.compile(r"^modeled_global_horizontal_source_flag$"), "GP1__part3"),
    (re.compile(r"^modeled_global_horizontal_uncertainty_pct$"), "GP1__part4"),
    (re.compile(r"^modeled_direct_normal_wm2$"), "GP1__part5"),
    (re.compile(r"^modeled_direct_normal_source_flag$"), "GP1__part6"),
    (re.compile(r"^modeled_direct_normal_uncertainty_pct$"), "GP1__part7"),
    (re.compile(r"^modeled_diffuse_horizontal_wm2$"), "GP1__part8"),
    (re.compile(r"^modeled_diffuse_horizontal_source_flag$"), "GP1__part9"),
    (re.compile(r"^modeled_diffuse_horizontal_uncertainty_pct$"), "GP1__part10"),
    (re.compile(r"^extraterrestrial_radiation_period_minutes$"), "GR1__part1"),
    (re.compile(r"^extraterrestrial_radiation_horizontal_wm2$"), "GR1__part2"),
    (re.compile(r"^extraterrestrial_radiation_horizontal_quality_code$"), "GR1__part3"),
    (re.compile(r"^extraterrestrial_radiation_normal_wm2$"), "GR1__part4"),
    (re.compile(r"^extraterrestrial_radiation_normal_quality_code$"), "GR1__part5"),
    (re.compile(r"^supp_wind_oa_type_code_(?P<idx>\d+)$"), "OA{idx}__part1"),
    (re.compile(r"^supp_wind_oa_period_hours_(?P<idx>\d+)$"), "OA{idx}__part2"),
    (re.compile(r"^supp_wind_oa_speed_ms_(?P<idx>\d+)$"), "OA{idx}__part3"),
    (re.compile(r"^supp_wind_oa_speed_quality_code_(?P<idx>\d+)$"), "OA{idx}__part4"),
    (re.compile(r"^supp_wind_type_code_(?P<idx>\d+)$"), "OD{idx}__part1"),
    (re.compile(r"^supp_wind_period_hours_(?P<idx>\d+)$"), "OD{idx}__part2"),
    (re.compile(r"^supp_wind_direction_deg_(?P<idx>\d+)$"), "OD{idx}__part3"),
    (re.compile(r"^supp_wind_speed_ms_(?P<idx>\d+)$"), "OD{idx}__part4"),
    (re.compile(r"^supp_wind_speed_quality_code_(?P<idx>\d+)$"), "OD{idx}__part5"),
]

_INTERNAL_COLUMN_MAP = {v: k for k, v in FRIENDLY_COLUMN_MAP.items()}

FIELD_REGISTRY: dict[str, FieldRegistryEntry] = {}


def _parse_expanded_col(col: str) -> tuple[str, str] | None:
    """Return (field_prefix, suffix) for an expanded column, or None."""
    m = _EXPANDED_COL_RE.match(col)
    if m:
        return m.group("field"), m.group("suffix")
    return None


def to_friendly_column(col: str) -> str:
    mapped = FRIENDLY_COLUMN_MAP.get(col)
    if mapped:
        return mapped
    for pattern, template in _FRIENDLY_PATTERNS:
        match = pattern.match(col)
        if match:
            return template.format(**match.groupdict())
    return col


def to_internal_column(col: str) -> str:
    mapped = _INTERNAL_COLUMN_MAP.get(col)
    if mapped:
        return mapped
    for pattern, template in _INTERNAL_PATTERNS:
        match = pattern.match(col)
        if match:
            return template.format(**match.groupdict())
    return col


def _internal_name(prefix: str, part_idx: int, suffix: str) -> str:
    if suffix == "value":
        return f"{prefix}__value"
    return f"{prefix}__part{part_idx}"


def get_field_registry_entry(
    prefix: str,
    part_idx: int,
    suffix: str = "part",
) -> FieldRegistryEntry | None:
    internal_name = _internal_name(prefix, part_idx, suffix)
    entry = FIELD_REGISTRY.get(internal_name)
    if entry is not None:
        return entry
    rule = get_field_rule(prefix)
    if rule is None:
        return None
    part_rule = rule.parts.get(part_idx)
    if part_rule is None:
        return None
    entry = FieldRegistryEntry(
        code=prefix,
        part=part_idx,
        internal_name=internal_name,
        name=to_friendly_column(internal_name),
        kind=part_rule.kind,
        scale=part_rule.scale,
        missing_values=part_rule.missing_values,
        quality_part=part_rule.quality_part,
        agg=part_rule.agg,
    )
    FIELD_REGISTRY[internal_name] = entry
    return entry


def is_quality_column(col: str) -> bool:
    """True for observation-level quality columns (e.g. WND__quality)."""
    internal = to_internal_column(col)
    return internal.endswith("__quality") or internal.endswith("__qc")


def is_categorical_column(col: str) -> bool:
    """True if the column is a WMO/ISD category code that must not be averaged."""
    parsed = _parse_expanded_col(to_internal_column(col))
    if parsed is None:
        return False
    field_prefix, suffix = parsed
    rule = get_field_rule(field_prefix)
    if rule is None:
        return False
    # Match suffix like "part3" or "value"
    if suffix == "value":
        part_idx = 1
    elif suffix.startswith("part"):
        try:
            part_idx = int(suffix[4:])
        except ValueError:
            return False
    else:
        return False
    part_rule = rule.parts.get(part_idx)
    if part_rule and part_rule.kind in {"categorical", "quality"}:
        return True
    return False


def get_agg_func(col: str) -> str:
    """Return the preferred aggregation function name for *col*.

    Returns one of: ``"mean"``, ``"max"``, ``"min"``, ``"mode"``,
    ``"sum"``, ``"drop"``, ``"circular_mean"``.  Defaults to ``"mean"`` for columns that
    have no explicit rule.
    """
    if is_quality_column(col):
        return "drop"
    parsed = _parse_expanded_col(to_internal_column(col))
    if parsed is None:
        return "mean"
    field_prefix, suffix = parsed
    rule = get_field_rule(field_prefix)
    if rule is None:
        return "mean"
    if suffix == "value":
        part_idx = 1
    elif suffix.startswith("part"):
        try:
            part_idx = int(suffix[4:])
        except ValueError:
            return "mean"
    else:
        return "mean"
    part_rule = rule.parts.get(part_idx)
    if part_rule:
        return part_rule.agg
    return "mean"
