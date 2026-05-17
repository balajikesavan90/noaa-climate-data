# Strict Token Rejection Explanation

Strict token rejections are diagnostics emitted when an optional encoded NOAA section is present but one or more parsed tokens do not match the declared token width or shape expected by the current rule table.

These diagnostics are non-fatal. The validation workflow records them so reviewers can see where real-world optional-section payloads diverge from the strict token expectations, while still preserving station-level processing and row-level lineage.

## Observed Counts

- Total strict token rejections: 7347677
- Affected stations: 70
- Total input rows: 17884625
- Total output rows: 17884625
- Row parity preserved: True
- Parse error rows: 0

## Dominant Identifiers

- CH1: 4871002
- CI1: 402647
- MD1: 156447
- MK1: 46
- OD1: 1704737
- OD2: 129958
- SA1: 82840

## Interpretation

A strict token rejection does not mean a station failed, a row was dropped, or the canonical row count changed. In this validation bundle, all 100 stations succeeded and summed input rows equal summed output rows.

Unsupported or malformed optional encoded sections are surfaced in per-station quality reports through fields such as `skipped_encoded_columns`, `unsupported_identifier_columns`, `malformed_identifier_columns`, and `token_rejection_examples`. The cleaner does not silently convert those diagnostics into a claim of decoded scientific correctness for the affected optional payloads.

Reviewers should infer that the workflow observed substantial optional-section irregularity and recorded it explicitly. Reviewers should not infer that the 7.3M count represents row loss, station failure, or silent removal of observations.

## Future Work

- Review high-volume families such as CH1 and OD1 against NOAA documentation and representative raw examples.
- Promote common optional-section divergences into documented rule-provenance decisions where appropriate.
- Add aggregate field-completeness and nullification reports for the DOI artifact boundary.
- Expand upstream-traceable fixtures for optional encoded families that dominate strict diagnostics.
