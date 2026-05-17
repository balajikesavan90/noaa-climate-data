# 100-Station Validation Artifact

This directory documents the canonical 100-station operational validation
artifact for DOI packaging:

```text
artifacts/validation_100_station/build_20260510
```

The DOI artifact is reproducible only within the archived validation boundary:
given the archived validation inputs, NOAA-Spec deterministically reproduces
the archived cleaned outputs and quality evidence.

Exact reconstruction of these validation inputs directly from upstream NOAA
services is not claimed unless upstream source URLs and upstream checksums are
present for the selected files.

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
* Workflow provenance for DOI-backed reruns from archived validation inputs
* Archived validation metadata
* Per-station audit summaries
* Deterministic sampling evidence
* Validation manifests for the external archived raw parquet inputs

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
* recorded archived raw input provenance
* executed the repository-controlled cleaning pipeline
* generated canonical cleaned outputs outside git
* generated per-station quality reports
* preserved row-level parity
* produced deterministic manifests and diagnostics

---

# Directory Structure

```text
build_20260510/
├── archive_manifest.json
├── aggregate_quality_summary.json
├── aggregate_quality_summary.md
├── checksums.txt
├── canonical_cleaned/
├── domains/                 # emitted with --emit-domains
├── raw_inputs/
├── run_manifest.json
├── selected_station_metadata.csv
├── station_results.csv
├── station_selection_manifest.csv
├── strict_parse_summary_report.json
├── strict_parse_summary_report.md
├── strict_token_rejection_explanation.md
├── summary.md
└── quality_reports/
```

Large generated payloads may be excluded from the Git repository but must be
included in the external DOI artifact:

* `raw_inputs/`
* `canonical_cleaned/`
* `checksums.txt`
* `domains/` when optional domain projections are emitted

The current DOI placeholder is `TODO_BEFORE_DOI` and must be replaced before
the final frozen archive is cited.

Frozen Docker metadata:

* repository: `noaa-spec-review`
* tag: `latest`
* digest: `sha256:dbbaa759a8ccc1ae7f86ccbc1189771643fa56d0fa798e29552c415c04dd030e`

---

# Reviewer Quickstart

From the repository root, verify the extracted DOI artifact:

```bash
python3 scripts/verify_validation_artifact.py artifacts/validation_100_station/build_20260510
```

This verifies `checksums.txt`, required files, the expected 100 raw inputs, 100
canonical cleaned outputs, 100 quality reports, 100 successful station results,
row-count parity, and `selected_station_metadata.csv`.

Inspect the main manifests:

```bash
python3 -m json.tool artifacts/validation_100_station/build_20260510/run_manifest.json
python3 -m json.tool artifacts/validation_100_station/build_20260510/archive_manifest.json
sed -n '1,40p' artifacts/validation_100_station/build_20260510/station_results.csv
```

Optional small rerun check for one archived station:

```bash
mkdir -p /tmp/noaa-spec-validation-check/source
cp artifacts/validation_100_station/build_20260510/raw_inputs/01121099999.parquet \
  /tmp/noaa-spec-validation-check/source/
noaa-spec dev build-validation-bundle \
  --source-root /tmp/noaa-spec-validation-check/source \
  --output-root /tmp/noaa-spec-validation-check/out \
  --count 1 \
  --seed 20260510 \
  --build-id reviewer-single-station
sha256sum /tmp/noaa-spec-validation-check/out/canonical_cleaned/01121099999_cleaned.csv
grep 'canonical_cleaned/01121099999_cleaned.csv' \
  artifacts/validation_100_station/build_20260510/checksums.txt
```

The full 100-station rerun is optional and expensive; it is not required for a
quick reviewer inspection.

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

# Selected Station Metadata

`selected_station_metadata.csv` summarizes the 100 selected stations with
station identifiers, station labels, coordinates, date ranges, row counts, size
strata, and raw/canonical checksums where available. If a field cannot be read
from an archived parquet input or manifest, it is left blank rather than
inferred.

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

This artifact is Tier 2 optional evidence. It is not fully reproducible from
the git repository alone.

It does not claim exhaustive reproducibility validation for the full NOAA corpus.

The DOI artifact allows reviewers to:

* inspect the selected station sample
* inspect deterministic provenance
* inspect diagnostic outputs
* rerun the workflow against archived raw parquet inputs

without depending on live NOAA availability. The boundary is
archived-inputs-to-archived-outputs, not upstream NOAA reconstruction.

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

DOI status:

* `TODO_BEFORE_DOI`

---
