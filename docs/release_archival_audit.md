# Release Archival Audit

Date: 2026-05-22

## Files Changed

- `README.md`: added citation and archived release DOI section with Zenodo badges.
- `REPRODUCIBILITY.md`: linked archived validation evidence and software DOI.
- `CITATION.cff`: updated software citation metadata for v1.0.2 and the software DOI.
- `pyproject.toml`: updated package metadata version to 1.0.2 and added project URLs for repository, documentation, and citation.
- `src/noaa_spec/__init__.py`: aligned package `__version__` metadata with v1.0.2.
- `paper/paper.md`: cited the archived software release and validation evidence where directly relevant.
- `paper/paper.bib`: added bibliography records for the software DOI and validation artifact DOIs.
- `maintainer/docs/release/README.md`: replaced stale no-archive wording with current DOI links.
- `CHANGELOG.md`: documented metadata-only archival updates.

## Rationale

These changes make the archived software release, validation artifacts, and reproducibility evidence discoverable from the repository, package metadata, citation metadata, and manuscript source. The changes are documentation and metadata only; they do not alter algorithms, validation logic, scientific claims, or runtime behavior.

## DOI Usage

- Software archive: https://doi.org/10.5281/zenodo.20350948
  - Used for the frozen implementation and citation metadata.
- Primary validation artifacts: https://doi.org/10.5281/zenodo.20320544
  - Used for operational validation artifacts, quality reports, manifests, and provenance evidence.
- Domain validation artifacts: https://doi.org/10.5281/zenodo.20320457
  - Used for domain-specific outputs intended for downstream reuse.

## Remaining Manual Actions

Zenodo metadata cross-linking:

- Software DOI:
  - HasPart -> validation DOIs
- Validation DOIs:
  - IsSupplementTo -> software DOI

Confirm that the GitHub release/tag for v1.0.2 points to the same commit archived by Zenodo.
