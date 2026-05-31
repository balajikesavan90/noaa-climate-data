# Public API Boundary

NOAA-Spec's primary public interface is the command-line workflow:

```bash
noaa-spec clean INPUT.csv OUTPUT.csv
```

The Python API is intentionally small. Use it when embedding the cleaner in a
larger Python workflow; use the CLI when you need the repository's standard
deterministic CSV output path.

| API | Stability | Purpose |
| --- | --- | --- |
| `noaa_spec.cleaning.clean_noaa_dataframe(df, keep_raw=True, strict_mode=True)` | Public for this release | Clean a pandas DataFrame containing NOAA ISD / Global Hourly-style columns and return decoded values, preserved quality-code columns, validation sidecars, and row-level usability fields. |
| `noaa_spec.projections.project_domains(df)` | Public convenience API | Build optional domain projection DataFrames from an already-cleaned DataFrame. The canonical cleaned DataFrame remains the source artifact. |
| `noaa_spec.deterministic_io.write_deterministic_csv(frame, output_path, sort_by=..., float_format=...)` | Public helper, mainly for repository-consistent outputs | Write CSV with stable row ordering, UTF-8 encoding, LF line endings, empty null cells, and deterministic float formatting when requested. |

Everything else in `src/noaa_spec/` should be treated as internal implementation
detail unless a future release documents it here. In particular, rule tables,
parser helpers, validation-bundle builders, and identifier-inspection utilities
may change as NOAA field coverage and maintainer diagnostics evolve.

For the cleaned output contract, see [schema.md](schema.md) and
[supported_fields.md](supported_fields.md). For the package-scope boundary, see
[design_rationale.md](design_rationale.md).
