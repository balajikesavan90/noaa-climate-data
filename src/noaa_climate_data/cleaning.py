"""Cleaning utilities for NOAA Global Hourly data."""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

import pandas as pd

from .constants import (
    ADDITIONAL_DATA_PREFIXES,
    DATA_SOURCE_FLAGS,
    EQD_ELEMENT_NAMES,
    EQD_FLAG1_CODES,
    EQD_FLAG2_CODES,
    LEGACY_EQD_MSD_PATTERN,
    LEGACY_EQD_PARAMETER_CODES,
    QNN_ELEMENT_IDENTIFIERS,
    REM_TYPE_CODES,
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
    stripped = value.replace(".", "").replace("+", "")
    if stripped.startswith("-"):
        return False
    return stripped.isdigit() and len(stripped) >= 2 and set(stripped) == {"9"}


def _normalize_missing(value: str) -> str:
    stripped = value.replace(".", "").replace("+", "")
    sign = ""
    if stripped.startswith("-"):
        sign = "-"
        stripped = stripped[1:]
    stripped = stripped.lstrip("0") or "0"
    return f"{sign}{stripped}"


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


def _additional_data_fixed_width(
    prefix: str, part_rule: FieldPartRule | None
) -> int | None:
    if part_rule is None or part_rule.kind != "numeric":
        return None
    prefix_key = prefix[:2]
    if prefix_key not in ADDITIONAL_DATA_PREFIXES:
        return None
    if not part_rule.missing_values:
        return None
    lengths = {
        len(value)
        for value in part_rule.missing_values
        if value.isdigit()
    }
    return next(iter(lengths)) if len(lengths) == 1 else None


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


def _is_eqd_prefix(prefix: str) -> bool:
    return len(prefix) == 3 and prefix[0] in {"Q", "P", "R", "C", "D", "N"} and prefix[1:].isdigit()


def _is_valid_eqd_parameter_code(prefix: str, value: str) -> bool:
    if prefix.startswith("N"):
        if len(value) != 6:
            return False
        element = value[:4]
        flag1 = value[4]
        flag2 = value[5]
        return (
            element in EQD_ELEMENT_NAMES
            and flag1 in EQD_FLAG1_CODES
            and flag2 in EQD_FLAG2_CODES
        )
    normalized = value.strip().upper()
    if normalized in LEGACY_EQD_PARAMETER_CODES:
        return True
    return prefix.startswith("R") and bool(LEGACY_EQD_MSD_PATTERN.fullmatch(normalized))


def _parse_remark(value: object) -> tuple[str | None, str | None]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None, None
    text = str(value).strip()
    if text in {"", "nan", "None"}:
        return None, None
    prefix = text[:3].upper()
    if prefix in REM_TYPE_CODES:
        remainder = text[3:].strip()
        return prefix, remainder or None
    return None, text


def _parse_qnn(value: object) -> tuple[str | None, str | None, str | None]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None, None, None
    text = str(value).strip()
    if text in {"", "nan", "None"}:
        return None, None, None
    if not text.upper().startswith("QNN"):
        return None, None, None
    payload = text[3:]
    payload_upper = payload.upper()
    element_ids: list[str] = []
    source_flags: list[str] = []
    pattern = re.compile(r"([A-Y])(\d{4})")
    for match in pattern.finditer(payload_upper):
        element = match.group(1)
        flags = match.group(2)
        if element not in QNN_ELEMENT_IDENTIFIERS:
            continue
        element_ids.append(element)
        source_flags.append(flags)
    if not element_ids:
        return None, None, None
    remainder = pattern.sub("", payload_upper)
    remainder = re.sub(r"[^A-Z0-9]", "", remainder)
    data_values: list[str] = []
    if remainder and len(remainder) % 6 == 0:
        data_values = [remainder[i : i + 6] for i in range(0, len(remainder), 6)]
    return ",".join(element_ids), ",".join(source_flags), ",".join(data_values) or None


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
    is_eqd = _is_eqd_prefix(prefix)
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
        if part_rule and part_rule.kind == "quality" and part_rule.allowed_quality:
            if part.strip().upper() not in part_rule.allowed_quality:
                payload[key] = None
                continue
        fixed_width = _additional_data_fixed_width(prefix, part_rule)
        if fixed_width is not None:
            normalized = part.strip()
            if not normalized.isdigit() or len(normalized) != fixed_width:
                payload[key] = None
                continue
        if part_rule and part_rule.allowed_values:
            if part.strip().upper() not in part_rule.allowed_values:
                payload[key] = None
                continue
        if part_rule and part_rule.allowed_pattern:
            if not part_rule.allowed_pattern.fullmatch(part.strip()):
                payload[key] = None
                continue
        if is_eqd and idx == 3:
            param_code = part.strip()
            if param_code != "" and not _is_valid_eqd_parameter_code(prefix, param_code):
                payload[key] = None
                continue
        if value is None:
            payload[key] = part
            continue
        if part_rule and part_rule.kind == "numeric":
            if part_rule.min_value is not None and value < part_rule.min_value:
                payload[key] = None
                continue
            if part_rule.max_value is not None and value > part_rule.max_value:
                payload[key] = None
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
    if value is not None and part_rule and part_rule.kind == "numeric":
        if part_rule.min_value is not None and value < part_rule.min_value:
            value = None
        elif part_rule.max_value is not None and value > part_rule.max_value:
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

    def _normalize_date(series: pd.Series) -> pd.Series:
        text = series.astype(str).str.strip()
        text = text.where(~text.isin({"", "nan", "None"}))
        match = text.str.fullmatch(r"\d{8}")
        parsed = pd.to_datetime(text, format="%Y%m%d", errors="coerce", utc=True)
        return text.where(match & parsed.notna())

    def _normalize_time(series: pd.Series) -> pd.Series:
        text = series.astype(str).str.strip()
        text = text.where(~text.isin({"", "nan", "None"}))
        match = text.str.fullmatch(r"\d{4}")
        hour = pd.to_numeric(text.str.slice(0, 2), errors="coerce")
        minute = pd.to_numeric(text.str.slice(2, 4), errors="coerce")
        valid = match & hour.between(0, 23) & minute.between(0, 59)
        return text.where(valid)

    if "LATITUDE" in work.columns:
        series = _normalize_numeric(work["LATITUDE"])
        series = series.where(series.between(-90.0, 90.0))
        work["LATITUDE"] = series

    if "LONGITUDE" in work.columns:
        series = _normalize_numeric(work["LONGITUDE"])
        series = series.where(series.between(-180.0, 180.0))
        work["LONGITUDE"] = series

    if "DATE" in work.columns:
        work["DATE"] = _normalize_date(work["DATE"])

    if "TIME" in work.columns:
        work["TIME"] = _normalize_time(work["TIME"])

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

    if "REM" in cleaned.columns:
        remark_types = []
        remark_texts = []
        for value in cleaned["REM"]:
            remark_type, remark_text = _parse_remark(value)
            remark_types.append(remark_type)
            remark_texts.append(remark_text)
        cleaned["REM__type"] = remark_types
        cleaned["REM__text"] = remark_texts

    if "QNN" in cleaned.columns:
        qnn_elements = []
        qnn_flags = []
        qnn_values = []
        for value in cleaned["QNN"]:
            element_ids, source_flags, data_values = _parse_qnn(value)
            qnn_elements.append(element_ids)
            qnn_flags.append(source_flags)
            qnn_values.append(data_values)
        cleaned["QNN__elements"] = qnn_elements
        cleaned["QNN__source_flags"] = qnn_flags
        cleaned["QNN__data_values"] = qnn_values

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
