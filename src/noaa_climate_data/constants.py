"""Shared constants for NOAA ISD Global Hourly data."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

BASE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access"

QUALITY_FLAGS = {
    "0",
    "1",
    "2",
    "4",
    "5",
    "6",
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
    agg: str = "mean"  # mean | max | min | mode | sum | drop | circular_mean


@dataclass(frozen=True)
class FieldRule:
    code: str
    parts: dict[int, FieldPartRule]


FIELD_RULES: dict[str, FieldRule] = {
    "WND": FieldRule(
        code="WND",
        parts={
            1: FieldPartRule(missing_values={"999"}, quality_part=2, agg="circular_mean"),
            3: FieldPartRule(kind="categorical", agg="drop"),  # wind type code
            4: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=5),
        },
    ),
    "CIG": FieldRule(
        code="CIG",
        parts={
            1: FieldPartRule(missing_values={"99999"}, quality_part=2),
            3: FieldPartRule(kind="categorical", agg="drop"),  # determination code
            4: FieldPartRule(kind="categorical", agg="drop"),  # CAVOK code
        },
    ),
    "VIS": FieldRule(
        code="VIS",
        parts={
            1: FieldPartRule(missing_values={"999999", "9999"}, quality_part=2, agg="min"),
            3: FieldPartRule(quality_part=4, kind="categorical", agg="drop"),
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
        parts={1: FieldPartRule(scale=0.1, missing_values={"9999"}, quality_part=2, agg="max")},
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
            1: FieldPartRule(kind="categorical", agg="drop"),  # pressure tendency code
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
    "GE1": FieldRule(
        code="GE1",
        parts={1: FieldPartRule(kind="categorical", agg="drop")},  # convective cloud code
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
    "MW": FieldRule(
        code="MW*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop"),  # present-weather code
        },
    ),
    "AY": FieldRule(
        code="AY*",
        parts={
            1: FieldPartRule(kind="categorical", agg="drop"),  # past-weather condition code
            3: FieldPartRule(kind="categorical", agg="drop"),  # past-weather period
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


def _parse_expanded_col(col: str) -> tuple[str, str] | None:
    """Return (field_prefix, suffix) for an expanded column, or None."""
    m = _EXPANDED_COL_RE.match(col)
    if m:
        return m.group("field"), m.group("suffix")
    return None


def is_quality_column(col: str) -> bool:
    """True for observation-level quality columns (e.g. WND__quality)."""
    return col.endswith("__quality") or col.endswith("__qc")


def is_categorical_column(col: str) -> bool:
    """True if the column is a WMO/ISD category code that must not be averaged."""
    parsed = _parse_expanded_col(col)
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
    if part_rule and part_rule.kind == "categorical":
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
    parsed = _parse_expanded_col(col)
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
