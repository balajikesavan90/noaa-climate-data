# Contributing

## Development setup

Use the same Python 3.12 virtual-environment flow documented in the README:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
```

If `python3 -m venv` is unavailable on Ubuntu/Debian, install `python3-venv` first.

Install test tooling if needed:

```bash
python3 -m pip install pytest pytest-cov
```

## Running tests

Run the full suite:

```bash
python3 -m pytest -q
```

Run CLI smoke checks:

```bash
python3 -m noaa_spec.cli --help
noaa-spec --help
```

## Support and maintenance scope

NOAA-Spec supports Python 3.11 and 3.12, matching the `pyproject.toml`
metadata. Reports should include the NOAA-Spec version or commit, Python
version, operating system, command or API call, and a minimal reproducible
example when possible.

In scope for issues:

- bugs in deterministic cleaning, sentinel normalization, QC preservation, or
  documented output schemas;
- installation, packaging, and CLI problems;
- documentation gaps or unclear examples;
- focused requests for supported NOAA ISD / Global Hourly field handling.

Out of scope:

- NOAA data download services;
- general climate analysis, modeling, statistics, or visualization workflows;
- requests to treat validation artifacts or station corpora as the package
  itself;
- support for private data that cannot be reduced to a minimal public or
  synthetic example.

Maintainers should preserve the package's bounded scope, deterministic output
behavior, and rule-provenance trail. Changes that alter cleaned output,
schema-like column names, or parsing rules should include tests and
documentation updates in the same pull request.

## Adding or updating rules

- Treat NOAA documentation as the authoritative source.
- Keep rule provenance explicit in code and tests.
- Prefer adding or tightening validation through declarative rules and deterministic checks.
- If a rule is stricter than the source documentation, record that rationale clearly and avoid silent data loss.

## Coding standards

- Preserve deterministic outputs and stable schema contracts.
- Keep production code under `src/noaa_spec/`.
- Keep reproducibility helper scripts minimal and reproducibility-oriented.
- Update tests and documentation in the same change whenever paths, commands, or contracts change.

## Release checklist

NOAA-Spec is not documented here as published on PyPI. Until a PyPI release is
made, install from a source checkout with `python3 -m pip install -e .`.

Before tagging a release:

1. Confirm version numbers match in `pyproject.toml`, `src/noaa_spec/__init__.py`,
   `CITATION.cff`, and release notes.
2. Update `CHANGELOG.md`.
3. Run the test suite:

   ```bash
   python3 -m pytest -q
   ```

4. Run the reproducibility check:

   ```bash
   bash scripts/verify_reproducibility.sh
   ```

5. Build package artifacts:

   ```bash
   python3 -m pip install build
   python3 -m build
   ```

6. Install from the built wheel in a fresh environment and run a CLI smoke
   check:

   ```bash
   python3 -m pip install dist/noaa_spec-*.whl
   noaa-spec --help
   ```

7. Review whether documentation, citation metadata, and validation-artifact
   references match the release scope.
8. Create a git tag and GitHub release only after the checks above pass.
9. If publishing to PyPI in a future release, upload only after the local build
   and install checks pass, then update installation documentation to use the
   published package.
