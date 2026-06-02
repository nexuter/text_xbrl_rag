# Audit-Evidence Hierarchy Implementation Log

## Purpose

This log records implementation of `SR-00C` from `plan/112_second_revision_comprehensive_revise_plan.md`.

The goal was to address the reviewers' concern that the manuscript's audit positioning could exceed what public filing text and management-reported XBRL data can support.

## Files Updated

| File | Change |
|---|---|
| `submission/Manuscript_Retrieval_as_Research_Design.md` | Added audit-evidence hierarchy in Section V and clarified that the demonstration does not establish audit evidence sufficiency |
| `submission/Online_Supplement_Appendix.md` | Added Appendix Table F1A, Audit-Evidence Hierarchy For Coding Boundaries |
| `submission/Tables_and_Figures.md` | Updated Table 7 note to align claim correctness layers with the audit-evidence hierarchy |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Workflow tracker updated |
| `plan/116_claim_evidence_calibration_register.md` | Status updated |

## Hierarchy Added

The revision now distinguishes five levels:

1. public-filing support,
2. XBRL graph/reporting support,
3. assertion relevance,
4. audit-boundary diagnostic,
5. audit evidence sufficiency.

## Main Manuscript Implementation

Section V now states that the current demonstration reaches the first four levels as a methodological diagnostic but does **not** establish audit evidence sufficiency.

The manuscript also clarifies that text-supported and graph-valid claims can support public-reporting analysis and assertion-relevant diagnostics, but they should not be treated as audit conclusions without additional audit evidence, professional judgment, and expert validation procedures.

## Supplement Implementation

Added:

**Appendix Table F1A. Audit-Evidence Hierarchy For Coding Boundaries**

The table specifies, for each level:

1. meaning,
2. current demonstration status,
3. coding implication.

The key coding boundary is that audit-boundary diagnostics remain preliminary unless independently reviewed by audit-domain experts, and the current public-filing/XBRL package should not be coded as establishing audit evidence sufficiency.

## Tables Packet Alignment

The note under main-text Table 7 now states that the demonstration distinguishes public-filing support, XBRL graph/reporting support, assertion relevance, and preliminary audit-boundary diagnostics from audit evidence sufficiency.

## QA

Search QA confirmed that hierarchy terms appear in the intended files:

1. `public-filing support`
2. `XBRL graph/reporting support`
3. `Assertion relevance`
4. `Audit-boundary diagnostic`
5. `audit evidence sufficiency`

Search QA also confirmed that remaining references to audit conclusions, audit truth, and audit evidence sufficiency are boundary statements, not completed-result claims.

## Reviewer Risk Reduced

This revision directly responds to:

1. Reviewer 1 Major Comment 3: distinguish factual filing support from audit-risk inference.
2. Reviewer 2 Major Comment 5: clarify that public filing/XBRL evidence is audit-relevant but not audit evidence sufficiency.
3. Reviewer 1 Minor Comment 6 and Reviewer 2 Major Comment 3: replace audit-validity language with a bounded audit-boundary diagnostic unless expert validation is added.

## Remaining Boundary

This task improves conceptual and coding-boundary clarity. It does not add expert audit-domain coding. If the paper later makes stronger audit-judgment claims, expert coding and reliability evidence remain required.

## SR-00C Status

`SR-00C` is complete. The next planned workstream is Workstream 1 / `SR-01`: sharpen incremental contribution through an adjacent-validity comparison section and table, including non-accounting retrieval-evaluation and evidence-traceability literature.
