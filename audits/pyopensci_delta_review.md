# pyOpenSci Delta Review

## Current Recommendation

Ready for pre-submission inquiry.

The deduplication pass resolved the main positioning and overlap-documentation risks for a pre-submission inquiry. `docs/design_rationale.md` is now the natural scope boundary, README links to it, README has a concise existing-tools comparison, `docs/first_output_guide.md` covers the beginner clean-and-inspect path, and `docs/public_api.md` defines the small Python API boundary.

Implementation note: the packaging pass added `SECURITY.md`, minimal issue and PR templates, support/maintenance/release guidance in `CONTRIBUTING.md`, CI coverage for Python 3.11 and 3.12, and wheel/sdist build plus installed-package smoke checks. The repository is now ready for a focused pyOpenSci pre-submission inquiry about scope fit and review timing.

## Remaining True Blockers Before Inquiry

None identified after the packaging pass.

## Blockers Before Full Submission But Not Inquiry

- Actual PyPI publication, assuming the inquiry confirms scope fit. For inquiry, clear status language is enough; for full submission, package availability is much more important.
- A completed release process that has been used at least once for a tagged release.
- Green CI on GitHub for the new Python 3.11/3.12 matrix and package build/install checks.
- Explicit Code of Conduct reporting contact if pyOpenSci considers the existing generic wording too vague.
- DOI placeholder cleanup for validation artifacts if those artifacts are cited in submission materials. This is not needed for pre-submission inquiry.

## Nice-to-Have Only

- A fuller downstream research tutorial. The current `docs/first_output_guide.md` is sufficient for inquiry; a richer analysis example can wait.
- Generated API reference docs. `docs/public_api.md` is enough while the Python API remains small.
- Coverage reporting.
- A glossary.
- A separate architecture page. Existing `docs/design_rationale.md`, `docs/rule_provenance.md`, and `docs/public_api.md` are enough for now.
- Deeper landscape/tool comparison. README is concise and adequate unless pyOpenSci asks for more.

## Things Not To Touch Now

- Do not make the 27k-station corpus central to pyOpenSci inquiry readiness. It is not needed for the inquiry and would distract from package scope.
- Do not create `docs/pyopensci_scope.md`; `docs/design_rationale.md` is already the canonical scope boundary.
- Do not create `docs/tool_landscape.md`; README already contains the concise overlap section.
- Do not create `docs/tutorial_clean_one_station.md`; `docs/first_output_guide.md` is the existing beginner path.
- Do not create `docs/cli.md` unless the CLI grows or reviewers ask. README plus argparse help are enough for now.
- Do not rewrite JOSS-oriented validation material unless it becomes misleading. Current docs already separate core package behavior from validation artifacts.
- Do not refactor parser, cleaning, validation, or artifact-generation source code for pyOpenSci inquiry readiness.

## Recommended Next Implementation Pass

No further implementation is required before opening a pre-submission inquiry.

Next action: draft the inquiry using the package as the reviewed object, link to `docs/design_rationale.md`, and keep validation artifacts secondary.
