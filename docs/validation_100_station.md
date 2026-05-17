# 100-Station Operational Validation

The repository contains maintainer tooling to produce a 100-station operational
validation artifact. The canonical DOI candidate is
`artifacts/validation_100_station/build_20260510`.

This is Tier 2 optional evidence. It is not fully reproducible from the
repository alone because large archived raw inputs and canonical cleaned outputs
are not part of the normal source checkout.

Small upstream-traceable fixtures, regression tests, and source-document-linked
rule families verify the semantic core. The 100-station validation artifact
demonstrates that the same repository-controlled workflow runs successfully
across a broader stratified operational sample. It does not prove universal
correctness across the NOAA corpus and is not required for the basic user
workflow.

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

Canonical build: `build_20260510`

DOI: `TODO_BEFORE_DOI`

Docker image: `noaa-spec-review:latest`

Docker image digest: `sha256:dbbaa759a8ccc1ae7f86ccbc1189771643fa56d0fa798e29552c415c04dd030e`

Required contents:

- selected 100 station raw parquet input files
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
- `checksums.txt`

The bounded claim is: given the archived validation inputs, NOAA-Spec
deterministically reproduces the archived cleaned outputs and quality evidence.
Exact upstream NOAA-source reconstruction is not claimed unless upstream source
URLs and upstream checksums are present in the artifact metadata.

## Reviewer quickstart

Verify the extracted DOI artifact from the repository root:

```bash
python3 scripts/verify_validation_artifact.py artifacts/validation_100_station/build_20260510
```

Inspect the manifests:

```bash
python3 -m json.tool artifacts/validation_100_station/build_20260510/run_manifest.json
python3 -m json.tool artifacts/validation_100_station/build_20260510/archive_manifest.json
sed -n '1,40p' artifacts/validation_100_station/build_20260510/station_results.csv
```

Optional single-station rerun:

```bash
mkdir -p /tmp/noaa-spec-validation-check
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
  --output-root artifacts/validation_100_station/build_20260510_rerun \
  --count 100 \
  --strategy size-stratified \
  --seed 20260510 \
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
- `checksums.txt`
- `archive_manifest.json`

The selection manifest records the auditable deterministic sample and the copied raw-input provenance. The run manifest records environment metadata and the reproducibility boundary. The results table records per-station status, row counts, runtime, raw checksums, and output checksums. The checksum file covers the key generated artifacts so the validation package can be archived externally.

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

For JOSS or later archival packaging, review `summary.md`, `checksums.txt`, and
`archive_manifest.json`, then archive the resulting `build_20260510` bundle in
an external repository or data archive that can mint a DOI. Replace
`TODO_BEFORE_DOI` before final citation. Local rerun is optional and requires
the archived input bundle for this DOI boundary.
