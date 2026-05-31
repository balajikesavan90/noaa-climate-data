# 100-Station Operational Validation

The repository contains maintainer tooling to produce a 100-station operational
validation artifact. The canonical DOI candidate is
`artifacts/validation_100_station/build_20260518`.

This is Tier 2 optional evidence. It is not fully reproducible from the
repository alone because large archived raw inputs and canonical cleaned outputs
are not part of the normal source checkout.

Small upstream-traceable fixtures, regression tests, and source-document-linked
rule families verify the semantic core. The 100-station validation artifact
demonstrates that the same repository-controlled workflow runs successfully
across a broader stratified operational sample. It does not prove universal
correctness across the NOAA corpus and is not required for the basic user
workflow. For the package-scope boundary that applies to validation artifacts
and larger corpora, see [design_rationale.md](design_rationale.md).

## A. Quick semantic verification

This is the normal reviewer quick path.

- Uses the small tracked fixtures already committed in the repository.
- No external data is required.
- The fixture-backed path verifies semantic behavior and checksum-stable output for the public cleaning workflow.

See `REPRODUCIBILITY.md`, `reproducibility/checksums.sha256`, and the tracked fixture directories for the in-repo verification path.

## B. DOI-backed 100-station validation bundle

This section documents the canonical 100-station artifact intended for DOI
archival.

- Uses externally archived validation parquet inputs rather than live NOAA
  downloads.
- Allows inspection of selected station inputs, canonical cleaned outputs,
  manifests, checksums, quality summaries, and `summary.md`.
- Not required for the public `noaa-spec clean INPUT.csv OUTPUT.csv` workflow.

## Archived validation bundle

Canonical build: `build_20260518`

Primary DOI: `TODO_PRIMARY_DOI`

Supplementary Domains DOI: `TODO_DOMAINS_DOI`

Docker image: `noaa-spec-review:latest`

Docker image digest: `sha256:dbbaa759a8ccc1ae7f86ccbc1189771643fa56d0fa798e29552c415c04dd030e`

## Reproducibility Boundary

This validation artifact supports deterministic reproducibility from archived validation inputs to archived outputs. Reconstruction from upstream NOAA archives is not claimed because upstream NOAA source URLs and checksums are not preserved within this artifact.

The primary DOI archive is the canonical deterministic cleaning artifact and
contains the canonical reproducibility boundary:

archived inputs → deterministic NOAA-Spec processing → canonical cleaned outputs

The supplementary DOI archive contains convenience domain projections derived
from canonical outputs. Domain outputs are not required to reproduce
NOAA-Spec's core deterministic cleaning behavior.

Domain outputs are archived separately as supplementary artifacts and are outside the primary reproducibility claim.

Primary archive contents:

- `raw_inputs/`
- `canonical_cleaned/`
- `quality_reports/`
- `checksums_primary.txt`
- `station_selection_manifest.csv`
- `selected_station_metadata.csv`
- `run_manifest.json`
- `archive_manifest_primary.json`
- `station_results.csv`
- `strict_parse_summary_report.json`
- `strict_parse_summary_report.md`
- `strict_token_rejection_explanation.md`
- `aggregate_quality_summary.json`
- `aggregate_quality_summary.md`
- `summary.md`

Supplementary archive contents:

- `domains/`
- `archive_manifest_domains.json`
- `checksums_domains.txt`

## Reviewer quickstart

Verify the extracted DOI artifact from the repository root:

```bash
python3 scripts/verify_validation_artifact.py artifacts/validation_100_station/build_20260518
```

Inspect the manifests:

```bash
python3 -m json.tool artifacts/validation_100_station/build_20260518/run_manifest.json
python3 -m json.tool artifacts/validation_100_station/build_20260518/archive_manifest_primary.json
sed -n '1,40p' artifacts/validation_100_station/build_20260518/station_results.csv
```

Optional single-station rerun:

```bash
mkdir -p /tmp/noaa-spec-validation-check
mkdir -p /tmp/noaa-spec-validation-check/source
STATION_ID=$(python3 - <<'PY'
import csv
with open("artifacts/validation_100_station/build_20260518/selected_station_metadata.csv", newline="", encoding="utf-8") as handle:
    print(next(csv.DictReader(handle))["station_id"])
PY
)
cp "artifacts/validation_100_station/build_20260518/raw_inputs/${STATION_ID}.parquet" \
  /tmp/noaa-spec-validation-check/source/
noaa-spec dev build-validation-bundle \
  --source-root /tmp/noaa-spec-validation-check/source \
  --output-root /tmp/noaa-spec-validation-check/out \
  --count 1 \
  --seed 20260518 \
  --build-id reviewer-single-station
sha256sum "/tmp/noaa-spec-validation-check/out/canonical_cleaned/${STATION_ID}_cleaned.csv"
grep "canonical_cleaned/${STATION_ID}_cleaned.csv" \
  artifacts/validation_100_station/build_20260518/checksums_primary.txt
```

## C. Reproduce the 100-station validation locally

This path is optional.

- It is for maintainers or reviewers who want to regenerate the archived validation artifact.
- It requires the archived input bundle for the DOI reproducibility boundary.
- It uses `noaa-spec dev build-validation-bundle`.

Provide a directory of station files that this repository can read as `.csv`,
`.csv.gz`, or `.parquet` inputs, or point the workflow at an unpacked archived
input bundle. Then run:

```bash
noaa-spec dev build-validation-bundle \
  --source-root /path/to/downloaded/stations \
  --output-root artifacts/validation_100_station/build_20260518 \
  --count 100 \
  --strategy size-stratified \
  --seed 20260518 \
  --emit-domains
```

The workflow fails if fewer than the requested number of viable station files are available. By default it also fails if any selected station run fails. Use `--continue-on-error` only when diagnostic partial output is more important than strict pass/fail behavior.

## Generated artifacts

The output directory contains:

- `raw_inputs/`
- `station_selection_manifest.csv`
- `selected_station_metadata.csv`
- `run_manifest.json`
- `station_results.csv`
- `canonical_cleaned/`
- `quality_reports/`
- `strict_parse_summary_report.json`
- `strict_parse_summary_report.md`
- `strict_token_rejection_explanation.md`
- `aggregate_quality_summary.json`
- `aggregate_quality_summary.md`
- `summary.md`
- `checksums_primary.txt`
- `archive_manifest_primary.json`
- `checksums_domains.txt`
- `archive_manifest_domains.json`

The selection manifest records the auditable deterministic sample and the copied raw-input provenance. The run manifest records environment metadata and the reproducibility boundary. The results table records per-station status, row counts, runtime, raw checksums, and output checksums. `checksums_primary.txt` covers only primary archive contents, while `checksums_domains.txt` covers only `domains/*` supplementary outputs.

Strict-parse flags in the per-station quality reports are observability signals,
not parse failures and not silent cleaning behavior. Unsupported optional
identifiers are reported explicitly when encountered. In the 100-station bundle,
skipped optional identifiers did not cause station-level failures or row loss,
and the `HL1` investigation artifact documents the observed exclusion rather
than silently ignoring it.

## Relationship to the tracked fixtures

The repository’s small tracked fixtures remain the semantic verification layer
and the normal quick reviewer path. The 100-station workflow complements them by
showing that the same cleaning code path executes successfully across a broader
stratified operational sample without turning this repository into a downloader
or claiming NOAA-wide exhaustiveness.

## External archival

For JOSS or later archival packaging, review `summary.md`,
`checksums_primary.txt`, `archive_manifest_primary.json`,
`checksums_domains.txt`, and `archive_manifest_domains.json`, then package two
archives:

```bash
tar -czf \
  release_artifacts/noaa-spec-validation-primary-v1.0.2.tar.gz \
  -C artifacts/validation_100_station/build_20260518 \
  raw_inputs canonical_cleaned quality_reports run_manifest.json \
  selected_station_metadata.csv station_results.csv station_selection_manifest.csv \
  aggregate_quality_summary.json aggregate_quality_summary.md \
  strict_parse_summary_report.json strict_parse_summary_report.md \
  strict_token_rejection_explanation.md summary.md \
  archive_manifest_primary.json checksums_primary.txt

tar -czf \
  release_artifacts/noaa-spec-validation-domains-v1.0.2.tar.gz \
  -C artifacts/validation_100_station/build_20260518 \
  domains archive_manifest_domains.json checksums_domains.txt
```

Verify extracted archives independently:

```bash
python3 scripts/verify_validation_artifact.py /path/to/extracted-primary
python3 scripts/verify_validation_artifact.py /path/to/extracted-domains --verify-domains
```

Replace `TODO_PRIMARY_DOI` only in primary archive documentation before final
citation. Replace `TODO_DOMAINS_DOI` only where supplementary domain artifacts
are discussed. Local rerun is optional and requires the archived input bundle
for this DOI boundary.
