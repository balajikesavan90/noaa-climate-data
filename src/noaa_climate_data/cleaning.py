"""Cleaning utilities for NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd

from .constants import (
    DATA_SOURCE_FLAGS,
    QUALITY_FLAGS,
    QC_PROCESS_CODES,
    REPORT_TYPE_CODES,
    FieldPartRule,
    get_field_registry_entry,
    get_field_rule,
    to_friendly_column,
)


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


def _normalize_missing(value: str) -> str:
    stripped = value.replace(".", "").replace("-", "").replace("+", "")
    return stripped.lstrip("0") or "0"


def _is_missing_value(value: str, rule: FieldPartRule | None) -> bool:
    if rule and rule.missing_values:
        stripped = _normalize_missing(value)
        return stripped in rule.missing_values
    return _is_missing_numeric(value)


def _quality_for_part(prefix: str, part_index: int, parts: list[str]) -> str | None:
    rule = get_field_rule(prefix)
    if not rule:
        return None
    part_rule = rule.parts.get(part_index)
    if not part_rule or part_rule.quality_part is None:
        return None
    quality_index = part_rule.quality_part
    if quality_index > len(parts):
        return None
    return parts[quality_index - 1]


def _allowed_quality_set(prefix: str, quality_part_index: int) -> set[str]:
    rule = get_field_rule(prefix)
    if rule is None:
        return QUALITY_FLAGS
    quality_rule = rule.parts.get(quality_part_index)
    if quality_rule and quality_rule.allowed_quality:
        return quality_rule.allowed_quality
    return QUALITY_FLAGS


def _allowed_quality_for_value(prefix: str, part_index: int) -> set[str]:
    rule = get_field_rule(prefix)
    if rule is None:
        return QUALITY_FLAGS
    part_rule = rule.parts.get(part_index)
    if part_rule is None or part_rule.quality_part is None:
        return QUALITY_FLAGS
    return _allowed_quality_set(prefix, part_rule.quality_part)


def _single_quality_part(prefix: str) -> int | None:
    rule = get_field_rule(prefix)
    if not rule:
        return None
    quality_parts = {
        part.quality_part
        for part in rule.parts.values()
        if part.quality_part is not None
    }
    if len(quality_parts) == 1:
        return next(iter(quality_parts))
    return None


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
    is_variable_direction = (
        prefix == "WND"
        and len(parsed.parts) >= 3
        and parsed.parts[0].strip() == "999"
        and parsed.parts[2].strip().upper() == "V"
    )
    if prefix == "WND":
        payload["WND__direction_variable"] = is_variable_direction
    is_od_calm = (
        prefix.startswith("OD")
        and len(parsed.parts) >= 4
        and parsed.parts[2].strip() == "999"
        and parsed.parts[3].strip() == "0000"
    )
    is_wnd_calm = (
        prefix == "WND"
        and len(parsed.parts) >= 4
        and parsed.parts[2].strip() == "9"
        and parsed.parts[3].strip() == "0000"
    )
    is_oe_calm = (
        prefix.startswith("OE")
        and len(parsed.parts) >= 4
        and parsed.parts[2].strip() == "00000"
        and parsed.parts[3].strip() == "999"
    )
    field_rule = get_field_rule(prefix)
    quality_value = None
    if allow_quality:
        quality_part_index = _single_quality_part(prefix)
        if quality_part_index is not None and quality_part_index <= len(parsed.parts):
            quality_value = parsed.parts[quality_part_index - 1].strip()
            if quality_value == "":
                quality_value = None
    allowed_quality = QUALITY_FLAGS
    if allow_quality and quality_part_index is not None:
        allowed_quality = _allowed_quality_set(prefix, quality_part_index)
    invalid_quality = (
        allow_quality
        and quality_value is not None
        and quality_value not in allowed_quality
    )
    for idx, (part, value) in enumerate(zip(parsed.parts, parsed.values), start=1):
        entry = get_field_registry_entry(prefix, idx, suffix="part")
        key = entry.internal_name if entry else f"{prefix}__part{idx}"
        part_rule = field_rule.parts.get(idx) if field_rule else None
        if is_variable_direction and idx == 1:
            payload[key] = None
            continue
        if is_wnd_calm and idx == 3:
            payload[key] = "C"
            continue
        if is_od_calm and idx == 3:
            payload[key] = 0.0
            continue
        if is_oe_calm and idx == 4:
            payload[key] = 0.0
            continue
        part_quality = _quality_for_part(prefix, idx, parsed.parts) if allow_quality else None
        allowed_for_part = _allowed_quality_for_value(prefix, idx)
        if part_quality is not None and part_quality not in allowed_for_part:
            payload[key] = None
            continue
        if invalid_quality and idx == 1 and part_quality is None:
            payload[key] = None
            continue
        # Check field-specific sentinels first — raw parts like "009999"
        # may parse numerically but still be declared missing.
        if _is_missing_value(part, part_rule):
            payload[key] = None
            continue
        if part_rule and part_rule.allowed_values:
            if part.strip().upper() not in part_rule.allowed_values:
                payload[key] = None
                continue
        if value is None:
            payload[key] = part
            continue
        scale = part_rule.scale if part_rule else None
        scaled = value * scale if scale is not None else value
        if prefix == "CIG" and idx == 1 and scaled is not None and scaled > 22000:
            scaled = 22000.0
        if prefix == "VIS" and idx == 1 and scaled is not None and scaled > 160000:
            scaled = 160000.0
        payload[key] = scaled
    if allow_quality and quality_value is not None:
        payload[f"{prefix}__quality"] = quality_value
    return payload


def _is_value_quality_field(prefix: str, part_count: int) -> bool:
    if part_count != 2:
        return False
    rule = get_field_rule(prefix)
    if rule is None:
        return False
    part_rule = rule.parts.get(1)
    if part_rule is None or part_rule.quality_part is None:
        return False
    return len(rule.parts) == 1


def clean_value_quality(raw: str, prefix: str) -> dict[str, object]:
    parsed = parse_field(raw)
    if len(parsed.parts) != 2:
        return _expand_parsed(parsed, prefix, allow_quality=True)
    if not _is_value_quality_field(prefix, len(parsed.parts)):
        return _expand_parsed(parsed, prefix, allow_quality=True)
    field_rule = get_field_rule(prefix)
    part_rule = field_rule.parts.get(1) if field_rule else None
    entry = get_field_registry_entry(prefix, 1, suffix="value")
    value_key = entry.internal_name if entry else f"{prefix}__value"
    quality = parsed.quality
    quality_index = part_rule.quality_part if part_rule else None
    if quality_index is not None and quality_index <= len(parsed.parts):
        quality = parsed.parts[quality_index - 1].strip() or None
    allowed_quality = (
        _allowed_quality_set(prefix, quality_index)
        if quality_index is not None
        else QUALITY_FLAGS
    )
    if (
        quality_index is not None
        and allowed_quality == QUALITY_FLAGS
        and part_rule
        and part_rule.allowed_quality
    ):
        allowed_quality = part_rule.allowed_quality
    value: float | None
    if part_rule and _is_missing_value(parsed.parts[0], part_rule):
        value = None
    else:
        value = parsed.values[0]
    if quality is not None and quality not in allowed_quality:
        value = None
    if value is not None and part_rule and part_rule.scale is not None:
        value = value * part_rule.scale
    return {
        value_key: value,
        f"{prefix}__quality": quality,
    }


def _should_parse_column(values: Iterable[str]) -> bool:
    for value in values:
        if isinstance(value, str) and "," in value:
            return True
    return False


def _normalize_control_fields(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()

    def _normalize_numeric(series: pd.Series) -> pd.Series:
        return pd.to_numeric(series, errors="coerce")

    if "LATITUDE" in work.columns:
        series = _normalize_numeric(work["LATITUDE"])
        series = series.where(series.between(-90.0, 90.0))
        work["LATITUDE"] = series

    if "LONGITUDE" in work.columns:
        series = _normalize_numeric(work["LONGITUDE"])
        series = series.where(series.between(-180.0, 180.0))
        work["LONGITUDE"] = series

    if "ELEVATION" in work.columns:
        series = _normalize_numeric(work["ELEVATION"])
        series = series.where(series.between(-400.0, 8850.0))
        work["ELEVATION"] = series

    if "CALL_SIGN" in work.columns:
        series = work["CALL_SIGN"].astype(str).str.strip()
        series = series.where(~series.isin({"99999", "nan", "None", ""}))
        work["CALL_SIGN"] = series.where(series.notna())

    if "SOURCE" in work.columns:
        series = work["SOURCE"].astype(str).str.strip().str.upper()
        series = series.where(series.isin(DATA_SOURCE_FLAGS))
        series = series.where(series != "9")
        work["SOURCE"] = series.where(series.notna())

    if "REPORT_TYPE" in work.columns:
        series = work["REPORT_TYPE"].astype(str).str.strip().str.upper()
        series = series.where(series.isin(REPORT_TYPE_CODES))
        series = series.where(series != "99999")
        work["REPORT_TYPE"] = series.where(series.notna())

    if "QUALITY_CONTROL" in work.columns:
        series = work["QUALITY_CONTROL"].astype(str).str.strip().str.upper()
        normalized = series.where(series.isin(QC_PROCESS_CODES))
        normalized = normalized.where(~normalized.isna(), series.str.slice(0, 3))
        normalized = normalized.where(normalized.isin(QC_PROCESS_CODES))
        work["QUALITY_CONTROL"] = normalized.where(normalized.notna())

    return work


def clean_noaa_dataframe(df: pd.DataFrame, keep_raw: bool = True) -> pd.DataFrame:
    """Expand NOAA comma-encoded fields into parsed numeric columns.

    For fields with the pattern value,quality this will create
    `<column>__value` and `<column>__quality` columns and apply the NOAA
    quality filter. For fields with additional parts, the parts are expanded
    into `<column>__partN` columns and, when available, a
    `<column>__quality` column.
    """
    cleaned = df.copy()
    if "ADD" in cleaned.columns:
        add_series = cleaned["ADD"].astype(str).str.strip().str.upper()
        add_mask = add_series.replace("", pd.NA).dropna().eq("ADD")
        if add_mask.empty or add_mask.all():
            cleaned = cleaned.drop(columns=["ADD"])
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

    for column in cleaned.columns:
        series = cleaned[column]
        if not pd.api.types.is_object_dtype(series) and not pd.api.types.is_string_dtype(series):
            continue
        cleaned[column] = series.apply(
            lambda value: None
            if isinstance(value, str) and _is_missing_numeric(value)
            else value
        )

    cleaned = _normalize_control_fields(cleaned)

    rename_map = {col: to_friendly_column(col) for col in cleaned.columns}
    if any(key != value for key, value in rename_map.items()):
        cleaned = cleaned.rename(columns=rename_map)

    return cleaned
