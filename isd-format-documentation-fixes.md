# ISD Format Documentation Fixes

Accuracy review of the 30 part files in `isd-format-document-parts/` compared against the source `isd-format-document.md` and `isd-format-document.txt`.

---

## Content Fixes Needed (6 parts)

### Fix 1 — Part 1: Preface and Dataset Overview (MAJOR — Truncated)

- **File**: `part-01-preface-and-dataset-overview.md`
- **Severity**: Major
- **Issue**: ~75 lines of content are missing after data-sequence item 6. The file ends at the page "2" marker.

**Missing content**:
- Data sequence item 7 (`GEOPHYSICAL-REPORT-TYPE code`)
- Record Structure description (`Maximum record size: 2,844 characters`, `Maximum block length: 8,192 characters`)
- Control Data Section description (60 characters, fixed length)
- Mandatory Data Section description (45 characters, fixed length)
- Additional Data Section description (0–637 characters, variable)
- Remarks Data description (max 515 characters)
- Element Quality Data Section description (0–1,587 characters)
- Missing Values convention paragraph
- Longitude and Latitude Coordinates conventions paragraph
- Items 5 and 6 (Access Method, Element Names)

**Root cause**: OCR/conversion artifacts (stray Part headings from PDF footers) at source lines ~108–146 caused the extraction to stop early. Content after those artifacts was lost.

**Source reference**: `isd-format-document.md` lines 147–223, or `isd-format-document.txt` lines 69–118.

- [ ] Fixed

---

### Fix 2 — Part 3: Mandatory Data Section (MAJOR — Wrong Values and Names)

- **File**: `part-03-mandatory-data-section.md`
- **Severity**: Major
- **Issue**: Five fields (POS 93–105) have wrong observation-type names, wrong MIN/MAX values, missing quality codes, and spurious trailing content.

**Specific errors**:

| Position | Field | Error |
|---|---|---|
| POS 93 | Quality code | Named `AIR-TEMPERATURE-OBSERVATION quality code` — should be `AIR-TEMPERATURE-OBSERVATION air temperature quality code`. Extended quality codes **A, C, I, M, P, R, U** with descriptions are completely missing. |
| POS 94–98 | Dew point temp | Named `DEW-POINT-OBSERVATION dew point temperature` — should be `AIR-TEMPERATURE-OBSERVATION dew point temperature`. **MIN is wrong**: shows `-0932`, should be `-0982`. **MAX is wrong**: shows `+0618`, should be `+0368`. Description is simplified. |
| POS 99 | Dew point quality | Named `DEW-POINT-OBSERVATION quality code` — should be `AIR-TEMPERATURE-OBSERVATION dew point quality code`. Extended quality codes A/C/I/M/P/R/U missing. |
| POS 100–104 | Sea level pressure | Named `SEA-LEVEL-PRESSURE-OBSERVATION sea level pressure` — should be `ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure`. Description simplified. |
| POS 105 | Pressure quality | Named `SEA-LEVEL-PRESSURE-OBSERVATION quality code` — should be `ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure quality code`. Has **spurious trailing content** (duplicated SCALING FACTOR/DOM block from air temperature section). |

**Source reference**: `isd-format-document.md` lines 628–727 (the source labels these under `## Part 8` due to document ordering, but they are POS 93–105 of the mandatory data section).

- [ ] Fixed

---

### Fix 3 — Part 9: Subhourly Temperature Section (CRITICAL — Wrong Content)

- **File**: `part-09-subhourly-temperature-section.md`
- **Severity**: Critical
- **Issue**: The heading says "Subhourly Temperature Section" but the body contains the **generic document preface/overview text** (record structure descriptions, missing value conventions). The actual Part 9 content is completely absent.

**What the file should contain**:
- Identifiers: CT1, CT2, CT3 (three co-located sensors)
- Fields: `AVG_TEMP` (5-minute average air temperature), `AVG_TEMP_QC`, `AVG_TEMP_FLAG`
- Temperature scaling factor 10, degrees Celsius, MIN: -9999 / MAX: +9998, missing = +9999
- Description of 5-minute data stream (12 records/hour) and 15-minute data stream behavior

**Source reference**: `isd-format-document.md` lines 3239–3274, or `isd-format-document.txt` lines 2970–3005.

- [ ] Fixed

---

### Fix 4 — Part 12: Subhourly Wetness Section (MAJOR — Empty Stub)

- **File**: `part-12-subhourly-wetness-section.md`
- **Severity**: Major
- **Issue**: Contains only the heading line. All content is missing.

**What the file should contain** (~70 lines):
- Identifier: CW1
- Fields: `WET1` wetness indicator (FLD LEN 5, MIN: 00000, MAX: 99999, SCALING FACTOR: 10)
- `WET1_QC` (quality codes 1/3/9)
- `WET1_FLAG` (quality codes 0/1-9)
- `WET2` wetness indicator (same structure)
- `WET2_QC`, `WET2_FLAG`

**Source reference**: `isd-format-document.md` lines 3493–3558, or `isd-format-document.txt` lines 3208–3268.

- [ ] Fixed

---

### Fix 5 — Part 13: Hourly Geonor Vibrating Wire Summary (MAJOR — Empty Stub)

- **File**: `part-13-hourly-geonor-vibrating-wire-summary-section.md`
- **Severity**: Major
- **Issue**: Contains only the heading line. All content is missing.

**What the file should contain** (~130 lines):
- Identifiers: CX1, CX2, CX3 (three co-located sensors, 15-min data stream only)
- Explanatory note about vibrating wire transducer frequencies
- Fields: `PRECIPITATION` (FLD LEN 6, MIN: -99999, MAX: +99999, SCALING FACTOR: 10, millimeters)
- `PRECIP_QC`, `PRECIP_FLAG`
- `FREQ_AVG` (FLD LEN 4, MIN: 0000, MAX: 9999, Hertz)
- `FREQ_AVG_QC`, `FREQ_AVG_FLAG`
- `FREQ_MIN` (FLD LEN 4, MIN: 0000, MAX: 9998, Hertz)
- `FREQ_MIN_QC`, `FREQ_MIN_FLAG`
- `FREQ_MAX` (FLD LEN 4, MIN: 0000, MAX: 9998, Hertz)
- `FREQ_MAX_QC`, `FREQ_MAX_FLAG`

**Source reference**: `isd-format-document.md` lines 3563–3697, or `isd-format-document.txt` lines 3274–3397.

- [ ] Fixed

---

### Fix 6 — Part 17: Solar Irradiance Section (MINOR — Truncated Identifier List)

- **File**: `part-17-solar-irradiance-section.md`
- **Severity**: Minor
- **Issue**: The GN1 (Solar Radiation Section) identifier list shows only 5 of 11 items. The actual field definitions for the missing items *are* present later in the file — only the summary list at the top of the GN1 section is truncated.

**Missing from GN1 identifier list** (6 items):
- Upwelling thermal infrared radiation
- Upwelling thermal infrared radiation quality code
- Photosynthetically active radiation
- Photosynthetically active radiation quality code
- Solar zenith angle
- Solar zenith angle quality code

**Source reference**: Compare Part 15's copy of the GN1 identifier list (which is complete) or `isd-format-document.md` around line 4800.

- [ ] Fixed

---

## Boundary / Overlap Issues (7 parts)

These are scoping issues where part boundaries don't cleanly separate content, causing duplication across files. No data is inaccurate — the content itself is correct but appears in multiple places.

### Overlap 1 — Part 15 contains Parts 16, 17, 18, 19

- **File**: `part-15-cloud-and-solar-data.md` (1,496 lines)
- **Issue**: Part 15 includes the full content that was also extracted into separate Parts 16 (Sunshine), 17 (Solar Irradiance), 18 (Net Solar Radiation), and 19 (Modeled Solar Irradiance). All four sub-parts are complete duplicates of subsets of Part 15.
- **Note**: In the source document, Parts 16–19 are subsections within Part 15 — they don't have their own `## Part` headings.

- [ ] Resolved

---

### Overlap 2 — Part 20 contains Parts 21 and 22

- **File**: `part-20-hourly-solar-angle-section.md` (169 lines)
- **Issue**: Part 20 includes the Hourly Extraterrestrial Radiation Section (Part 21 content, GR1) and Hail Data (Part 22 content) in addition to its own Solar Angle content (GQ1). Parts 21 and 22 also exist as separate standalone files, creating full duplication.

- [ ] Resolved

---

### Overlap 3 — Part 23 contains Part 24 content

- **File**: `part-23-ground-surface-data.md` (934 lines)
- **Issue**: After its own Ground Surface Data content (~450 lines: IA1, IA2, IB1, IB2, IC1), Part 23 continues with ~480 lines of Temperature Data (KA1–KG2) that belongs to Part 24. This content is duplicated verbatim in Part 24.

- [ ] Resolved

---

### Overlap 4 — Part 24 contains Parts 27, 28, 29 content

- **File**: `part-24-temperature-data.md` (1,643 lines)
- **Issue**: After its own Temperature Data content (~490 lines: KA1–KG2), Part 24 continues with:
  - ~380 lines of Pressure Data (MA1–MK1) — belongs to Part 27
  - ~330 lines of Weather Occurrence Extended (MV1–MW7) — belongs to Part 28
  - ~380 lines of Wind Data (OA1–OE3) — belongs to Part 29
  - ~60 lines of Relative Humidity (RH1–RH3)
- All this spillover content is duplicated in the correct standalone part files.

- [ ] Resolved

---

## Summary

| # | Part | Issue | Severity | Status |
|---|---|---|---|---|
| 1 | Part 1 | Truncated — ~75 lines missing | Major | ☐ |
| 2 | Part 3 | Wrong field names, wrong MIN/MAX values, missing quality codes | Major | ☐ |
| 3 | Part 9 | Contains wrong content entirely | Critical | ☐ |
| 4 | Part 12 | Empty stub — all content missing | Major | ☐ |
| 5 | Part 13 | Empty stub — all content missing | Major | ☐ |
| 6 | Part 17 | GN1 identifier list truncated (6 of 11 items missing) | Minor | ☐ |
| 7 | Parts 15↔16/17/18/19 | Content duplication (subsections extracted as separate parts) | Overlap | ☐ |
| 8 | Part 20↔21/22 | Content duplication | Overlap | ☐ |
| 9 | Part 23↔24 | Content duplication (~480 lines) | Overlap | ☐ |
| 10 | Part 24↔27/28/29 | Content duplication (~1,150 lines) | Overlap | ☐ |

**19 of 30 parts are clean** — Parts 2, 4, 5, 6, 7, 8, 10, 11, 14, 15, 16, 18, 19, 22, 25, 26, 27, 28, 29, 30.
