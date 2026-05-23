---
title: "NOAA-Spec: Deterministic Canonical Interpretation of NOAA Integrated Surface Database Observations"
tags:
  - climate
  - meteorology
  - data-cleaning
  - reproducibility
  - scientific-software
authors:
  - name: Balaji Kesavan
    affiliation: 1
    orcid: 0009-0002-7714-518X
affiliations:
  - name: Independent Researcher
    index: 1
date: 2026-03-29
bibliography: paper.bib
---

# Abstract

NOAA-Spec is open-source software for deterministic, specification-constrained canonical interpretation of NOAA Integrated Surface Database (ISD) / Global Hourly CSV observations. Its public `noaa-spec clean` command converts raw NOAA-style CSV rows into a deterministic observation-level CSV by normalizing documented sentinel values, preserving NOAA quality-code context, and producing checksum-stable output for a defined supported field set. The contribution is not that individual transformations are difficult; it is shared, versioned, traceable, regression-tested cleaning behavior for documented NOAA ISD / Global Hourly fields.

# Summary

NOAA ISD is widely used in weather and climate research, but raw rows require NOAA-specific interpretation before cleaned observation tables can be compared across studies [@smith2011isd; @noaa_isd_docs]. Packed measurement fields combine values and quality codes; sentinel values encode missingness; and many fields have documented widths, scales, ranges, and quality semantics. NOAA-Spec packages a bounded set of those interpretation decisions into one Python library and CLI centered on:

```bash
noaa-spec clean INPUT.csv OUTPUT.csv
```

The submitted software surface is intentionally narrow. NOAA-Spec reads raw NOAA ISD / Global Hourly CSV rows, applies deterministic field-interpretation rules for recognized fields, and writes a cleaned CSV whose serialization and emitted columns are stable for a given input. The JOSS-facing field families are `WND`, `CIG`, `VIS`, `TMP`, `DEW`, and `SLP`, with source/control columns retained. Broader implemented fields are documented for transparency, but the paper does not assert exhaustive NOAA coverage, a downloader, a statistical analysis package, or a single authoritative schema for all possible NOAA data. NOAA-Spec is intended for researchers and practitioners who require deterministic, inspectable preprocessing of supported NOAA ISD fields before downstream analysis.

The repository evidence is built around executable checks rather than narrative assurance: 1,995 collected automated tests, eight checksum-verified fixture pairs, three upstream-traceable fixture slices, and archived supplementary validation artifacts. The 100-station validation bundle records deterministic execution over 15,699,389 input rows and 15,699,389 output rows, with strict-token diagnostics retained as evidence instead of converted into row loss.

# Statement of Need

The decisions required to preprocess NOAA ISD are specific to the format. A token such as `TMP=+9999,9` contains both a numeric segment and a quality code [@noaa_isd_docs]. The numeric segment is not a large temperature; it is a sentinel-coded missing value. An informed researcher can write a project-local script to handle this correctly for one analysis.

The problem NOAA-Spec addresses is that such scripts tend not to be shared, versioned, or coordinated. The problem NOAA-Spec addresses is not that researchers cannot preprocess NOAA ISD, but that interpretation decisions are often implemented privately and inconsistently. Independent projects may normalize sentinels differently, retain or discard quality semantics, or emit incompatible cleaned schemas. When studies begin from the same NOAA source rows but apply divergent local preprocessing policies, comparing results requires auditing undocumented interpretation choices rather than verifying a shared transformation contract. This limits reproducibility and comparability in computational workflows [@peng2011reproducible].

NOAA-Spec publishes one documented, checksum-backed implementation of a defined set of cleaning decisions as a versioned Python CLI. It normalizes documented sentinels to null, preserves NOAA QC codes in explicit columns, writes stable decoded column names, and records parser decisions in QC sidecars where appropriate. A downstream researcher using `noaa-spec clean` on the same input obtains the same output, verifiable by checksum.

# State of the Field

Existing NOAA tools help users obtain, parse, or locally preprocess ISD data. NOAA-Spec makes a narrower build-vs-contribute choice: it contributes a deterministic interpretation layer rather than a new data-access client. Parsing tools expose NOAA structures; data-access tools help retrieve files; local scripts implement study-specific policies. NOAA-Spec instead standardizes reusable interpretation semantics for supported fields: sentinel normalization, QC preservation, canonical outputs, and checksum-friendly serialization. This comparison describes scope and output policy; it does not assert that other tools produce incorrect values.

| Criterion | Local preprocessing scripts | Parsing-oriented tools (`isdparser` [@chamberlain_isdparser], `isd` [@isd_python]) | NOAA-Spec |
| --- | --- | --- | --- |
| Sentinel normalization for `TMP=+9999,9` | Each project reimplements a table | Parsed structure can be exposed; downstream workflow chooses missing-value handling | Emits null `temperature_c`, preserves `temperature_quality_code=9`, records `TMP__qc_reason= SENTINEL_MISSING` |
| Packed visibility `VIS=999999,9,N,1` | Cleaning policy is project-specific | Parsed structure can be exposed; downstream workflow chooses cleaning policy | Emits null `visibility_m`, preserves visibility QC, keeps variability fields explicit |
| Stable decoded column names | Requires local naming convention | Analysis tables depend on downstream workflow | Uses documented names such as `temperature_c`, `visibility_m`, and `sea_level_pressure_hpa` |
| QC preservation as output | Easy to drop while extracting values | Available if retained downstream | Preserved in explicit columns and `__qc_*` sidecars |
| Reproducible cleaned CSV | Requires local serialization and checksums | Downstream workflow chooses serialization policy | Writes deterministic CSV output with checksum-backed fixtures |
| Shared versioned interpretation | Usually private or unpublished | Cleaning decisions vary by project | Documented cleaning decisions are versioned, testable, and reusable |

# Software Design

NOAA-Spec separates NOAA field interpretation (`cleaning.py` and `constants.py`) from deterministic CSV writing (`deterministic_io.py`) and the command-line entry point (`cli.py`). The cleaned output is intentionally wide: it preserves decoded measurements, source/control columns, NOAA quality codes, validation sidecars, and row-level usability summaries in one observation-level table. This makes the canonical file less compact, but avoids prematurely choosing one analysis subset or hiding QC context.

These choices reflect a deliberate tradeoff: NOAA-Spec prioritizes interpretability, reproducibility, semantic preservation, and deterministic outputs over compact schemas, minimal output width, or convenience-first preprocessing. Wide outputs increase downstream complexity, but they preserve the NOAA semantics needed to audit a cleaned value. QC retention increases file size, but keeps the evidence required for later filtering decisions. Deterministic serialization constrains implementation details, but enables checksum validation across users and releases.

QC codes are preserved because NOAA quality semantics are part of the observation, not merely parser metadata. Sentinel handling is separated from filtering for the same reason: missing markers are normalized to explicit nulls, while the evidence needed to decide whether an observation should be excluded remains available to researchers. The supported-field contracts, provenance inventory, fixtures, and validation strategy were designed together so that cleaning behavior remains inspectable rather than implicit in project-local scripts.

Optional domain views can be emitted for convenience, but they are derived projections of the canonical output rather than independent products. This preserves a single canonical interpretation layer while still giving users compact views for wind, visibility, pressure-temperature, precipitation, remarks, and quality-code workflows. Reproducibility fixtures exist to keep this contract executable: committed raw inputs, expected outputs, and SHA256 checksums verify that the public cleaning workflow remains stable. The supported-field registry, schema guide, and rule-provenance inventory document which outputs are public contracts and which rules are documented NOAA behavior or engineering safeguards.

Maintainer operational tooling for validation bundles and identifier inspection is kept under the `noaa-spec dev` namespace. That tooling supports auditability, but the normal user workflow and JOSS core claim remain the public `noaa-spec clean INPUT.csv OUTPUT.csv` command.

# Reproducibility

The repository includes tracked raw inputs, expected cleaned outputs, and checksum-backed verification under `reproducibility/`. The core claim is reproducible from repository files alone: for committed fixtures, `clean(committed_input) = committed_output`. Of the eight committed fixture pairs verified by `reproducibility/checksums.sha256`, three additionally record upstream NOAA/NCEI source URLs, retrieval dates, observed upstream checksums, and extraction commands.

The DOI-backed 100-station validation artifact provides additional operational evidence beyond committed reproducibility fixtures. It records a deterministic size-stratified sample, manifests, checksums, strict-token diagnostics, and row-count parity. The artifact broadens validation beyond the committed fixtures while leaving the core reproducibility claim centered on the public `noaa-spec clean` workflow.

# Research Impact Statement

NOAA-Spec provides is a reusable, reviewable preprocessing contract for NOAA ISD studies. It reduces repeated interpretation work by making supported NOAA sentinel handling, QC retention, stable naming, documented cleaning contracts, and deterministic serialization available through a citeable CLI. The contribution is demonstrated through reproducibility artifacts, archived validation evidence, automated testing, checksum-backed outputs, and operational validation, without claiming external adoption.

Verified repository evidence includes checksum-verified fixtures, upstream-traceable examples, and automated tests covering supported-field contracts and deterministic output behavior. The validation artifact also records 4,438,272 strict-token rejections as diagnostics rather than row-loss failures, supporting transparent handling of optional-section anomalies like format mismatches and malformed tokens.

# AI Usage Disclosure

Development and writing used AI assistance, including ChatGPT, Codex and GitHub Copilot using LLMs like GPT 5 series and Claude 4 series. These tools were used for implementation assistance, refactoring, test scaffolding, documentation and README editing, paper drafting, architecture review, reproducibility review, copy editing, and reviewer-simulation feedback.

Their scope was assistive: code generation suggestions, refactoring proposals, test-generation drafts, documentation wording, manuscript drafting, and review prompts. The human author determined the architecture, validation strategy, reproducibility strategy, supported-field contracts, publication decisions, and acceptance or rejection of AI outputs. Human review and validation included automated tests, reproducibility fixtures, checksum comparisons, archived validation-artifact manifests where applicable, and manual review; the human author remains responsible for the submitted software and manuscript.

# Limitations

NOAA-Spec is NOAA-specific software. This submission covers deterministic cleaning behavior exposed by `noaa-spec clean` for documented fields supported in this release. It does not claim to download NOAA data, orchestrate station batches, publish releases, or provide statistical analysis.

# Acknowledgements

The author acknowledges NOAA National Centers for Environmental Information (NCEI) for maintaining the ISD dataset and documentation.

# References
