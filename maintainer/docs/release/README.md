# Release Workflow Notes

Archived release and validation bundles are linked for this revision:

- Software archive: https://doi.org/10.5281/zenodo.20350948
- Primary validation artifacts: https://doi.org/10.5281/zenodo.20320544
- Domain validation artifacts: https://doi.org/10.5281/zenodo.20320457

This directory belongs to the broader artifact publication workflow. It is useful when working on release manifests and validation evidence, but the portable first-run path remains the core canonical cleaner and the in-repo reproducibility fixtures.

For fixture-level verification, use:

- `python3 reproducibility/run_pipeline_example.py --out /tmp/noaa-spec-sample.csv`
- `bash scripts/verify_reproducibility.sh`
- `pytest -q`

Frozen release artifacts belong to the broader publication workflow and are archived externally.
