# NOAA-Spec

NOAA-Spec provides deterministic, specification-constrained cleaning of NOAA
Integrated Surface Database (ISD) / Global Hourly CSV observations by
normalizing documented sentinel values, preserving NOAA quality-code context,
and producing checksum-stable output for a defined supported field set. Its
public JOSS-facing workflow is the single command:

```bash
noaa-spec clean INPUT.csv OUTPUT.csv
```

The command writes an observation-level cleaned CSV with documented NOAA
sentinels normalized to empty null cells, NOAA quality codes preserved in
explicit columns, and deterministic row/order serialization. If the input CSV
includes a `raw_line` or `RAW_LINE` column, the cleaner also performs raw
record/header structural validation on that column. The value is not parsing
alone; it is making a bounded set of NOAA cleaning decisions explicit,
testable, provenance-aware, and checksum-stable so downstream researchers can
start from the same documented interpretation rather than divergent local
scripts.

This project implements deterministic cleaning for a defined subset of NOAA ISD
/ Global Hourly fields. It does not attempt to cover the entire NOAA
specification. The JOSS-facing field families are `WND`, `CIG`, `VIS`, `TMP`,
`DEW`, and `SLP`, with source/control columns retained.

NOAA-Spec does not download NOAA data, orchestrate station batches, produce
releases, run analyses, or introduce a statistical/modeling method. Optional
domain projections can be emitted with `--emit-domains`, but the canonical
output remains the required public artifact. See
[docs/design_rationale.md](docs/design_rationale.md) for the canonical package
scope and validation-evidence boundary.

Scope is deliberately layered:

- JOSS core: deterministic CSV cleaning via `noaa-spec clean`; field families
  `WND`, `CIG`, `VIS`, `TMP`, `DEW`, and `SLP`; sentinel normalization;
  QC-code preservation; stable decoded column names; and checksum-stable
  output.
- Optional DOI-backed evidence: the 100-station validation bundle,
  quality reports, strict token diagnostics, validation bundle builder, and
  identifier inspection tools. These are operational diagnostics for
  transparency and auditability, not prerequisites for normal use and not
  acceptance-critical correctness evidence. Larger validation corpora, including
  any full-corpus or 27k-station validation run, should be treated the same way:
  evidence about the package, not the primary software object.

## Reproducibility Tiers

### Tier 1: Repo-native, required

Tier 1 is the required reproducibility boundary for the JOSS-facing claim. It
uses only tracked repository files.

- Workflow: `noaa-spec clean INPUT.csv OUTPUT.csv`
- Inputs: tracked raw fixture CSVs under `reproducibility/`
- Expected outputs: committed `station_cleaned_expected.csv` files
- Verification: checksum equality with `reproducibility/checksums.sha256`

Use the repository-defined Docker workflow. This is the primary tested
execution path for reviewers; local installation below is a convenience path
for users who do not want Docker.

```bash
docker build -f Dockerfile -t noaa-spec-review .
docker run --rm noaa-spec-review bash scripts/verify_reproducibility.sh
```

The 100-station validation artifact records the inspected local review image as
`noaa-spec-review:latest` with digest
`sha256:dbbaa759a8ccc1ae7f86ccbc1189771643fa56d0fa798e29552c415c04dd030e`.

Expected result: one `PASS` line for each tracked `station_cleaned_expected.csv`
entry in `reproducibility/checksums.sha256`, followed by:

```text
PASS: reproducibility verification succeeded.
Output directory: /tmp/noaa-spec-reproducibility
```

The canonical checksum list is `reproducibility/checksums.sha256`.

The Docker workflow is intended to provide a tested execution path for
reviewers. It is not claimed to be a bitwise archival environment. Debian
package metadata may be refreshed during image build. Reproducibility claims
are limited to the repository-controlled workflow: given the tracked inputs,
specification rules, and pinned Python dependencies, the canonical outputs and
checksums should remain stable. Long-term archival builds should use the tagged
release plus archived artifacts or DOIs. `requirements-review.txt` pins the
Docker verification Python dependency path only; it is not required for
standard local installation.

### Tier 2: DOI-backed, optional

Tier 2 is the `build_20260518` 100-station operational validation run. It is
not reproducible from this repository alone because the large raw inputs and
canonical outputs are archived outside the normal source checkout. Tier 2 is
optional and is not required for the core `noaa-spec clean` reproducibility
claim.

## Reproducibility Boundary

This validation artifact supports deterministic reproducibility from archived validation inputs to archived outputs. Reconstruction from upstream NOAA archives is not claimed because upstream NOAA source URLs and checksums are not preserved within this artifact.

The primary DOI archive is the canonical deterministic cleaning artifact and
contains the canonical reproducibility boundary:

archived inputs → deterministic NOAA-Spec processing → canonical cleaned outputs

The supplementary DOI archive contains convenience domain projections derived
from canonical outputs. Domain outputs are not required to reproduce
NOAA-Spec's core deterministic cleaning behavior.

Domain outputs are archived separately as supplementary artifacts and are outside the primary reproducibility claim.

See
[artifacts/validation_100_station/README.md](artifacts/validation_100_station/README.md)
and [docs/validation_100_station.md](docs/validation_100_station.md).

## Traceable Fixtures

The upstream-traceable reproducibility fixtures are:

- `reproducibility/real_provenance_example/`: 20 rows from station `78724099999` in 2001.
- `reproducibility/traceable_peru_il_2014_aa1_qc/`: one row from station `72214904899` in 2014.
- `reproducibility/traceable_albion_ne_2014_calm_aa1/`: one row from station `72344154921` in 2014.
- Checksums: `reproducibility/checksums.sha256`
- Provenance note: `reproducibility/TRACEABLE_FIXTURES.md`

These demonstrate selected traceable NOAA source slices; they are not a claim
of broad NOAA coverage. The strongest core evidence in these fixtures is for
`WND`, `CIG`, `VIS`, `TMP`, `DEW`, and `SLP`.

```text
https://www.ncei.noaa.gov/data/global-hourly/access/2001/78724099999.csv
https://www.ncei.noaa.gov/data/global-hourly/access/2014/72214904899.csv
https://www.ncei.noaa.gov/data/global-hourly/access/2014/72344154921.csv
```

After Docker or local install, run:

```bash
noaa-spec clean \
  reproducibility/real_provenance_example/station_raw.csv \
  /tmp/noaa-spec-real-provenance.csv
sha256sum /tmp/noaa-spec-real-provenance.csv
```

Compare the generated checksum with the matching
`reproducibility/real_provenance_example/station_cleaned_expected.csv` entry in
`reproducibility/checksums.sha256`.

Core-field snapshot from the tracked expected output:

| STATION | DATE | temperature_c | temperature_quality_code | visibility_m | visibility_quality_code | wind_speed_ms | wind_type_code | sea_level_pressure_hpa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 78724099999 | 2001-01-01T15:00:00 | 29.3 | 1 | 28000.0 | 1.0 | 8.2 | N | 1013.8 |
| 78724099999 | 2001-01-01T18:00:00 | 32.7 | 1 | 28000.0 | 1.0 | 10.8 | N | 1011.9 |

## Minimal Output View

From the tracked primary fixture, this raw row snippet:

```text
STATION=40435099999
DATE=2000-03-17T09:00:00
TMP=+9999,9
VIS=999999,9,N,1
WND=999,9,9,9999,9
SLP=99999,9
```

becomes this compact core-column view:

| STATION | DATE | temperature_c | temperature_quality_code | visibility_m | visibility_quality_code | wind_speed_ms | wind_speed_quality_code | sea_level_pressure_hpa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40435099999 | 2000-03-17T09:00:00 |  | 9 |  | 9.0 |  | 9.0 |  |

The useful behavior is explicit: sentinel-coded measurements become null while
the NOAA quality-code context remains visible.

Full output schema includes additional sidecar columns and quality fields. See
[docs/schema.md](docs/schema.md) for full details.

## First Output: Suggested First Inspection

The full cleaned CSV is intentionally wide because it preserves decoded
measurements, NOAA quality codes, parser sidecars, and row-level usability
signals. For a first pass, start with decoded measurement columns and their NOAA
quality-code columns. Leave `__qc_*` sidecars for a second pass unless a decoded value is empty or
surprising.

| Column | What to check |
| --- | --- |
| `STATION`, `DATE` | Source station and observation timestamp. |
| `temperature_c` | Decoded air temperature; sentinels become null. |
| `temperature_quality_code` | NOAA QC code preserved from `TMP`. |
| `dew_point_c` | Decoded dew point temperature. |
| `visibility_m` | Decoded visibility; `999999` becomes null. |
| `visibility_quality_code` | NOAA QC code preserved from `VIS`. |
| `wind_speed_ms` | Decoded wind speed from `WND`. |
| `wind_speed_quality_code` | NOAA QC code preserved for wind speed. |
| `sea_level_pressure_hpa` | Decoded sea-level pressure; `99999` becomes null. |

Compact core-column excerpt from the tracked primary fixture:

| STATION | DATE | temperature_c | temperature_quality_code | visibility_m | visibility_quality_code | wind_speed_ms | wind_type_code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 40435099999 | 2000-01-10T06:00:00 | 18.0 | 1 | 10000.0 | 1.0 | 0.0 | C |
| 40435099999 | 2000-03-17T09:00:00 |  | 9 |  | 9.0 |  |  |

For a slightly longer guide, see [docs/first_output_guide.md](docs/first_output_guide.md). For the supported field registry, see [docs/supported_fields.md](docs/supported_fields.md).
For Python embedding boundaries, see [docs/public_api.md](docs/public_api.md).

## Core Contribution vs Extended Coverage

The core JOSS-facing contribution is `noaa-spec clean`, deterministic cleaned
CSV generation, documented sentinel-to-null normalization, explicit NOAA QC
preservation, stable decoded column names, and checksum-backed reproduction of
tracked fixtures. The core field families are the retained source/control
columns plus `WND`, `CIG`, `VIS`, `TMP`, `DEW`, and `SLP`.

Additional NOAA families remain implemented, but they are not part of the
primary JOSS-reviewed claim. Treat them as secondary implementation inventory:
included for transparency, covered by regression tests and operational
diagnostics, but not all backed by upstream-replay fixtures. Use
[docs/evidence_matrix.md](docs/evidence_matrix.md) and
[docs/supported_fields.md](docs/supported_fields.md) for the evidence boundary.

## Why not a simple script?

A 500-1000 line script can parse NOAA fields for one project. That is not the
claim NOAA-Spec makes.

NOAA-Spec provides:

- deterministic outputs that are checksum stable;
- explicit sentinel-to-null handling tied to NOAA documentation;
- preservation of NOAA quality codes;
- traceability to source documentation and rule families;
- reproducibility guarantees across supported environments for the tracked
  fixture workflow.

This project is not about parsing NOAA data - it is about standardizing its
interpretation.

## Why A Shared Cleaning Tool?

A careful project-local script can reproduce the core cleaning mechanics for
one study. NOAA-Spec is useful when that interpretation needs to be shared: it
publishes stable decoded column names, explicit QC preservation,
checksum-backed regression behavior, field-family/spec-section provenance, and
deterministic CSV serialization as a versioned contract across users and
studies instead of leaving each study to carry a private preprocessing policy.

As a concrete illustration, a raw visibility token such as:

```text
VIS=999999,9,N,1
```

can be naively split into a numeric value of `999999`, which is not a real visibility distance. NOAA-Spec emits an empty `visibility_m`, preserves `visibility_quality_code=9`, and records the parser reason in `VIS__part1__qc_reason`.

Run the minimal comparison:

```bash
python3 examples/pandas_vs_noaa_spec.py
```

For a compact edge-case table of selected real rows, see [docs/reviewer_cleaning_examples.md](docs/reviewer_cleaning_examples.md). For claim-to-evidence mapping, see [docs/evidence_matrix.md](docs/evidence_matrix.md).

For a concise explanation of why the implementation is larger than a minimal
study-local script, see [docs/design_rationale.md](docs/design_rationale.md).

## Relationship to Existing NOAA Tools

NOAA-Spec does not claim that other tools produce incorrect values. It operates
at a narrower layer: an explicit cleaned-output policy for documented NOAA ISD /
Global Hourly fields. Documented sentinels become nulls, NOAA QC codes stay in
explicit columns, parser sidecars record cleaning evidence, and decoded column
names plus CSV serialization are deterministic for the same committed input.

| Tool or approach | Relationship to NOAA-Spec |
| --- | --- |
| `pandas` | Complementary general dataframe library. NOAA-Spec uses pandas internally, but provides NOAA-specific sentinel normalization, QC preservation, sidecar evidence, and deterministic serialization policy. |
| `xarray` | Complementary labeled-array/data-model library for analysis workflows. NOAA-Spec produces cleaned observation-level CSVs before a researcher chooses a downstream table, array, or gridded representation. |
| `noaa-sdk` | Complementary retrieval/API-oriented package. NOAA-Spec does not download NOAA data; it cleans NOAA ISD / Global Hourly CSV observations already obtained by the user. |
| `meteostat` | Complementary weather-data access and analysis-oriented ecosystem. NOAA-Spec focuses on transparent canonical cleaning of NOAA ISD / Global Hourly source rows rather than providing a broad weather data service. |
| Herbie | Complementary retrieval tool for NOAA model/product data. NOAA-Spec targets ISD / Global Hourly station observations and deterministic cleaning, not GRIB/model-product discovery or download. |
| Custom NOAA parsing scripts | A project-local script can handle one study's preprocessing policy. NOAA-Spec's distinction is a shared, versioned cleaning contract with documented sentinel handling, explicit QC columns, validation sidecars, stable serialization, and reproducibility fixtures. |

## Local Install (Convenience Path)

The Docker commands above are the primary tested reviewer path for workflow
reproducibility. The local convenience path works on macOS, Linux, and
Windows, but the virtual-environment commands are platform-specific. Python
3.11 or 3.12 is required.

macOS or Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -e .
```

Use `python3.11` instead of `python3.12` if that is your supported local
interpreter.

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e .
```

Use `py -3.11` instead of `py -3.12` if that is your supported local
interpreter. After activation, `python` refers to the virtual-environment
interpreter.

If the console script is not on `PATH`, use:

```bash
python3 -m noaa_spec.cli clean INPUT.csv OUTPUT.csv
```

## Reproducibility Fixtures

The tracked fixtures are small by design:

- `reproducibility/real_provenance_example/`: 20 rows from a recorded NOAA/NCEI Global Hourly source URL.
- `reproducibility/traceable_peru_il_2014_aa1_qc/`: one upstream-traceable row promoted from an edge-case example.
- `reproducibility/traceable_albion_ne_2014_calm_aa1/`: one upstream-traceable row promoted from an edge-case example.
- `reproducibility/minimal/`: five raw rows for the compact reproducibility fixture.
- `reproducibility/minimal_second/`: eight raw rows covering additional encoded fields.
- `reproducibility/station_03041099999_aonach_mor/`, `reproducibility/station_01116099999_stokka/`, and `reproducibility/station_94368099999_hamilton_island/`: four-row curated station slices. Their exact upstream retrieval metadata was not retained.

These fixtures verify deterministic behavior for committed input/output pairs:
`clean(committed_input) = committed_output`, verified by checksums. The
`real_provenance_example/`, `traceable_peru_il_2014_aa1_qc/`, and
`traceable_albion_ne_2014_calm_aa1/` fixtures additionally record upstream NOAA
URLs, retrieval dates, and observed upstream checksums. The older curated
station fixtures do not replay upstream NOAA acquisition and do not claim
exhaustive NOAA coverage. Broader field behavior is supported by tests, not by a
claim that the small fixtures exercise every NOAA field. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md),
[reproducibility/TRACEABLE_FIXTURES.md](reproducibility/TRACEABLE_FIXTURES.md),
[reproducibility/FIXTURE_PROVENANCE.md](reproducibility/FIXTURE_PROVENANCE.md),
and [docs/evidence_matrix.md](docs/evidence_matrix.md).

To run a bundled fixture manually after Docker or local install, use:

```bash
noaa-spec clean \
  reproducibility/minimal/station_raw.csv \
  /tmp/noaa-spec-minimal.csv
diff -u \
  reproducibility/minimal/station_cleaned_expected.csv \
  /tmp/noaa-spec-minimal.csv
sha256sum /tmp/noaa-spec-minimal.csv
```

For any other bundled fixture, replace `minimal` with the fixture directory
name, for example `minimal_second` or `real_provenance_example`. The `diff`
command should produce no output. The checksum should match the corresponding
`station_cleaned_expected.csv` entry in `reproducibility/checksums.sha256`.

## Run Tests

```bash
source .venv/bin/activate
python3 -m pip install -e .
python3 -m pip install pytest
python3 -m pytest tests -v
```
