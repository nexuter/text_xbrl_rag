# Integrated v4 Versus Separate-File Submission Decision

## Purpose

This file resolves whether to create an optional integrated v4 manuscript or keep the current separate-file submission package.

## Decision

Keep the **separate-file submission format** for the current AJPT package.

## Rationale

The current manuscript is already organized around table and figure callouts, and the corresponding tables, figures, supplement, and replication materials are cleanly separated in the `submission/` folder. Creating an integrated v4 manuscript would reduce navigation across files, but it would also create a very long document and increase the risk that reviewers treat the paper as a technical appendix-heavy system paper rather than as a focused methodology contribution.

The separate-file format better matches the current positioning:

| Reviewer Need | Separate-File Benefit |
|---|---|
| Read the argument cleanly | Main manuscript remains focused on theory, method, and demonstration interpretation |
| Inspect framework artifacts | Tables and figures file provides concentrated reviewer access |
| Audit the evidence trail | Online supplement contains retrieval logs, coding structure, and bounded-extension diagnostics |
| Assess reproducibility | Replication package remains distinct from the scholarly argument |
| Avoid overclaiming | Boundary statements are repeated in the relevant files without overloading the main text |

## Reviewer-Risk Assessment

| Risk | Separate-File Response |
|---|---|
| Reviewer cannot find tables or figures | Submission README and file names make the package structure explicit |
| Reviewer sees the supplement as too large | Main manuscript explains that the supplement is for inspection and reproducibility, not additional empirical claims |
| Editor expects a self-contained manuscript | Main text includes table/figure callouts and the scholarly argument remains complete without reading every appendix table |
| Integrated v4 would look more polished | Final formatting/export can still produce polished separate files |

## Conditions That Would Justify An Integrated v4 Later

An integrated v4 manuscript should be created only if:

1. The journal explicitly requires tables and figures embedded in the main manuscript.
2. The editor requests a single file for review.
3. The author team decides that a preprint or working-paper version should be easier to read as one document.

## Current Action

Do not create integrated v4 for the current submission package. Preserve:

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Tables_and_Figures.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `submission/Replication_Package_Manifest.md`

## Next Step

Proceed to final format conversion planning: identify which clean `.md` files need to become `.docx`, `.pdf`, repository files, or submission-system text fields.
