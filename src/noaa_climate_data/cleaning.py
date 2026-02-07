"""Cleaning utilities for NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd

from .constants import QUALITY_FLAGS


FIELD_SCALES: dict[str, float] = {
    "TMP": 0.1,
    "DEW": 0.1,
    "SLP": 0.1,
}


@dataclass(frozen=True)
class ParsedField:
    parts: list[str]
    values: list[float | None]
    quality: str | None


def _strip_plus(value: str) -> str:
    return value[1:] if value.startswith("+") else value


def _is_missing_numeric(value: str) -> bool:
    stripped = value.replace(".", "").replace("-", "").replace("+", "")
    return stripped.isdigit() and len(stripped) >= 2 and set(stripped) == {"9"}


def _to_float(value: str) -> float | None:
    value = value.strip()
    if value == "":
        return None
    value = _strip_plus(value)
    if _is_missing_numeric(value):
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _split_field(raw: str) -> list[str]:
    return [part.strip() for part in raw.split(",")]


def parse_field(raw: str) -> ParsedField:
    parts = _split_field(raw)
    values = [_to_float(part) for part in parts]
    quality = parts[-1] if parts and len(parts[-1]) == 1 else None
    return ParsedField(parts=parts, values=values, quality=quality)


def _expand_parsed(
    parsed: ParsedField,
    prefix: str,
    allow_quality: bool,
) -> dict[str, object]:
    payload: dict[str, object] = {}
    invalid_quality = (
        allow_quality
        and parsed.quality is not None
        and parsed.quality not in QUALITY_FLAGS
    )
    for idx, (part, value) in enumerate(zip(parsed.parts, parsed.values), start=1):
        key = f"{prefix}__part{idx}"
        if invalid_quality and idx == 1:
            payload[key] = None
        else:
            payload[key] = value if value is not None else part
    if allow_quality and parsed.quality is not None:
        payload[f"{prefix}__quality"] = parsed.quality
    return payload


def _maybe_apply_quality(value: float | None, quality: str | None) -> float | None:
    if quality is None:
        return value
    if quality not in QUALITY_FLAGS:
        return None
    return value


def clean_value_quality(raw: str, prefix: str) -> dict[str, object]:
    parsed = parse_field(raw)
    if len(parsed.parts) != 2:
        return _expand_parsed(parsed, prefix, allow_quality=True)
    value = _maybe_apply_quality(parsed.values[0], parsed.quality)
    if value is not None and prefix in FIELD_SCALES:
        value = value * FIELD_SCALES[prefix]
    return {
        f"{prefix}__value": value,
        f"{prefix}__quality": parsed.quality,
    }


def _should_parse_column(values: Iterable[str]) -> bool:
    for value in values:
        if isinstance(value, str) and "," in value:
            return True
    return False


def clean_noaa_dataframe(df: pd.DataFrame, keep_raw: bool = True) -> pd.DataFrame:
    """Expand NOAA comma-encoded fields into parsed numeric columns.

    For fields with the pattern value,quality this will create
    `<column>__value` and `<column>__quality` columns and apply the NOAA
    quality filter. For fields with additional parts, the parts are expanded
    into `<column>__partN` columns and, when available, a
    `<column>__quality` column.
    """
    cleaned = df.copy()
    expansion_frames: list[pd.DataFrame] = []

    for column in cleaned.columns:
        series = cleaned[column]
        if not pd.api.types.is_object_dtype(series) and not pd.api.types.is_string_dtype(series):
            continue
        sample = series.dropna().astype(str).head(200)
        if sample.empty or not _should_parse_column(sample):
            continue

        parsed_rows = []
        for value in series.fillna("").astype(str):
            if value == "":
                parsed_rows.append({})
                continue
            payload = clean_value_quality(value, column)
            parsed_rows.append(payload)

        expanded = pd.DataFrame(parsed_rows, index=cleaned.index)
        expansion_frames.append(expanded)
        if not keep_raw:
            cleaned = cleaned.drop(columns=[column])

    if expansion_frames:
        cleaned = pd.concat([cleaned] + expansion_frames, axis=1)

    return cleaned
