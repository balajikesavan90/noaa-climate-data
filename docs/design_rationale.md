# Design Rationale

NOAA-Spec's JOSS-facing core is intentionally narrow: deterministic cleaned CSV
output from `noaa-spec clean` for documented NOAA ISD / Global Hourly fields
covered by committed fixtures, tests, and source-document-linked rule families.

The implementation is larger than a minimal one-study script because NOAA
records combine mandatory fields, optional encoded sections, sentinel values,
quality flags, repeated field families, and irregular real-world payloads.
NOAA-Spec favors explicit constants, named field-family/spec-section
provenance, deterministic serialization, and anomaly diagnostics over compact
but opaque parsing.

The operational validation and identifier-inspection tools support
auditability, reproducibility checks, and maintainer review of real station
files. They are kept in the `noaa-spec dev` namespace and are not required for
normal use of the package.
