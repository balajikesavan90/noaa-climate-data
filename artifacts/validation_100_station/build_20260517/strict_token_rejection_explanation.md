# Strict Token Rejection Explanation

Strict token rejections are diagnostics emitted when an optional encoded NOAA section is present but one or more parsed tokens do not match the token width or shape expected by the current rule table.

They are non-fatal observability signals. The validation workflow records them so reviewers can inspect real-world optional-section irregularity without converting those irregularities into row loss or silent claims of decoded scientific correctness.

## Observed Counts

- Total strict token rejections: 2681534
- Affected stations: 70
- Total input rows: 12612131
- Total output rows: 12612131
- Row parity preserved: True
- Parse error rows: 0

## Dominant Identifiers

- MD1: 309043
- MK1: 34
- OD1: 1824771
- OD2: 367710
- OD3: 128752
- SA1: 51224

## Interpretation

A strict token rejection does not mean a station failed, a row was dropped, or the canonical row count changed. Row parity is reported separately in `station_results.csv` and `aggregate_quality_summary.json`.

Unsupported, skipped, or malformed optional encoded sections are surfaced in per-station quality reports through fields such as `skipped_encoded_columns`, `unsupported_identifier_columns`, `malformed_identifier_columns`, and `token_rejection_examples`.

These diagnostics do not imply upstream NOAA reconstruction. The reproducibility claim remains bounded to archived validation inputs and canonical outputs.

## Future Work

- Review high-volume optional encoded families against NOAA documentation and representative raw examples.
- Promote common optional-section divergences into documented rule-provenance decisions where appropriate.
- Add broader aggregate field-completeness and nullification reports for DOI-scale validation artifacts.
- Expand upstream-traceable fixtures for optional encoded families that dominate strict diagnostics.
