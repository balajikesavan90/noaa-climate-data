"""Shared constants for NOAA ISD Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass

BASE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access"

QUALITY_FLAGS = {
    "0",
    "1",
    "4",
    "5",
    "9",
    "A",
    "C",
    "I",
    "M",
    "P",
    "R",
    "U",
}

DEFAULT_START_YEAR = 2000
DEFAULT_END_YEAR = 2019


@dataclass(frozen=True)
class FieldPartRule:
    scale: float | None = None
    missing_values: set[str] | None = None
    quality_part: int | None = None
    kind: str = "numeric"


@dataclass(frozen=True)
class FieldRule:
    code: str
    parts: dict[int, FieldPartRule]


FIELD_RULES: dict[str, FieldRule] = {
    "WND": FieldRule(
        code="WND",
        parts={
            1: FieldPartRule(missing_values={"999"}, quality_part=2),
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
        },
    ),
    "CIG": FieldRule(
        code="CIG",
        parts={1: FieldPartRule(missing_values={"99999"}, quality_part=2)},
    ),
    "VIS": FieldRule(
        code="VIS",
        parts={
            1: FieldPartRule(missing_values={"999999"}, quality_part=2),
            3: FieldPartRule(quality_part=4, kind="categorical"),
        },
    ),
    "TMP": FieldRule(
        code="TMP",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2)},
    ),
    "DEW": FieldRule(
        code="DEW",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2)},
    ),
    "SLP": FieldRule(
        code="SLP",
        parts={1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2)},
    ),
    "OC1": FieldRule(
        code="OC1",
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2)},
    ),
    "MA1": FieldRule(
        code="MA1",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=2),
            3: FieldPartRule(scale=0.1, missing_values={"99999"}, quality_part=4),
        },
    ),
    "MD1": FieldRule(
        code="MD1",
        parts={
            3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4),
            5: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=6),
        },
    ),
    "SA1": FieldRule(
        code="SA1",
        parts={1: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=2)},
    ),
    "UA1": FieldRule(
        code="UA1",
        parts={3: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4)},
    ),
    "UG1": FieldRule(
        code="UG1",
        parts={2: FieldPartRule(scale=0.1, missing_values={"999"}, quality_part=4)},
    ),
}

FIELD_RULE_PREFIXES: dict[str, FieldRule] = {
    "KA": FieldRule(
        code="KA*",
        parts={
            1: FieldPartRule(scale=0.1, missing_values={"999"}),
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
        },
    ),
    "OD": FieldRule(
        code="OD*",
        parts={
            3: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=4),
            5: FieldPartRule(missing_values={"999"}, quality_part=4),
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
