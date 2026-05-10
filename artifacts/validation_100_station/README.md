# 100-Station Validation Artifact

> ⚠️ This validation bundle is NOT fully reproducible from this repository alone.
> Raw inputs and canonical outputs are excluded and will be published via DOI
> prior to final JOSS submission.

This directory contains metadata for a deterministic operational validation
artifact generated from a stratified 100-station sample of NOAA station files.

The purpose of this artifact is to demonstrate that the repository-controlled
cleaning workflow executes successfully across a broader operational sample
beyond the small upstream-traceable semantic fixtures used in the test suite.
It is supplementary smoke-validation evidence, not required for the basic
`noaa-spec clean INPUT.csv OUTPUT.csv` workflow, and it is not part of the
repo-native reproducibility claim.

---

# Scope

This artifact is intended to provide:

* Operational smoke-validation evidence
* Workflow provenance for future DOI-backed reruns
* Archived validation metadata
* Per-station audit summaries
* Deterministic sampling evidence
* Validation manifests that become rerunnable only with the external archived
  raw inputs

This artifact is **not** intended to prove universal correctness across the entire NOAA corpus.

Semantic correctness is established separately through:

* upstream-traceable fixtures
* repository-controlled tests
* source-document-linked rule families
* deterministic transformation rules

---

# What This Metadata Records

The tracked metadata records that a local validation workflow:

* selected a deterministic stratified station sample
* recorded raw input provenance for future DOI-backed archival
* executed the repository-controlled cleaning pipeline
* generated canonical cleaned outputs outside git
* generated per-station quality reports
* preserved row-level parity
* produced deterministic manifests and diagnostics

---

# Directory Structure

```text
build_<timestamp>/
├── archive_manifest.json
├── run_manifest.json
├── station_results.csv
├── station_selection_manifest.csv
├── strict_parse_summary_report.md
├── summary.md
├── domains/                 # optional, only when --emit-domains is used
└── quality_reports/
```

Large generated payloads are intentionally excluded from the Git repository:

* `raw_inputs/`
* `canonical_cleaned/`
* `checksums.txt`
* `domains/` when optional domain projections are emitted

These large artifacts are intended for external archival, for example
DOI-backed archive storage before JOSS submission. Until an actual DOI is
inserted, the archive should be treated as planned rather than already
available.

---

# Deterministic Sampling

The validation sample is deterministic and repository-controlled.

Sampling strategy:

* strategy: `size-stratified`
* quartiles: `q1/q2/q3/q4`
* stations per quartile: `25`
* total stations: `100`

The sample was not manually curated for favorable outcomes.

---

# Per-Station Quality Reports

Each station produces a small machine-readable quality report containing:

* row-count parity
* provenance metadata
* SHA256 hashes
* strict token diagnostics
* unsupported identifier summaries
* warning counts
* parse statistics

These reports are intended for auditability and reviewer inspection.

---

# Strict Token Diagnostics

Strict token validation diagnostics identify optional-section payloads that do
not match declared token-width expectations. They are observability signals, not
parse failures.

These diagnostics are intentionally non-fatal because:

* NOAA optional sections contain irregular real-world payloads
* preserving row-level processing is preferred over destructive failure
* diagnostics are intended to surface anomalies rather than silently discard rows

Strict token diagnostics:

* do not imply station-level failure
* do not imply row loss
* are tracked explicitly for transparency

See:

* `strict_parse_summary_report.md`

---

# Optional Domain Projections

The validation workflow can optionally emit domain projection CSVs with:

```bash
noaa-spec dev build-validation-bundle ... --emit-domains
```

When enabled, the bundle includes `domains/<domain>/<station>_<domain>.csv`
files for the projection domains exposed by `noaa-spec clean --emit-domains`.
The default validation behavior does not emit these files, and the canonical
cleaned CSV remains the required output.

---

# Reproducibility Boundary

This artifact is Tier 2 optional / future evidence. It is not fully
reproducible from the git repository alone.

It does not claim exhaustive reproducibility validation for the full NOAA corpus.

After DOI-backed archival exists, the validation metadata should allow reviewers to:

* inspect the selected station sample
* inspect deterministic provenance
* inspect diagnostic outputs
* rerun the workflow against archived raw inputs

without depending on live NOAA availability. Until then, treat this directory as
metadata only.

---

# Related Repository Components

Primary semantic validation lives in:

* upstream-traceable fixtures
* repository-controlled tests
* source-document-linked rule families
* validation logic linked to NOAA documentation

This validation artifact complements — but does not replace — those correctness mechanisms.

---

# DOI / External Archive

Large validation payloads are intended for external archival before submission.

DOI status:

* `TO_BE_ASSIGNED`

---
