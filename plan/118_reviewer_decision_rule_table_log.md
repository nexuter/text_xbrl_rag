# Reviewer Decision-Rule Table Implementation Log

## Purpose

This log records implementation of `SR-00B` from `plan/112_second_revision_comprehensive_revise_plan.md`.

The reviewer reports repeatedly asked the manuscript to show how retrieval-environment validity changes audit researchers' and reviewers' decisions. This task adds a reviewer-facing decision-rule table to make the framework evaluative rather than only descriptive.

## Files Updated

| File | Change |
|---|---|
| `submission/Manuscript_Retrieval_as_Research_Design.md` | Added Table 3 callout and explanatory paragraph in Section III; renumbered later main-text tables |
| `submission/Tables_and_Figures.md` | Added new Table 3, updated placement summary, renumbered Tables 4-9, and aligned table terminology with audit-boundary/source-use wording |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Workflow tracker updated |
| `plan/116_claim_evidence_calibration_register.md` | Status updated |

## New Main-Text Table

Added:

**Table 3. Reviewer Decision Rules for Retrieval-Environment Validity Problems**

The table classifies retrieval problems into five reviewer-useful categories:

1. inference-invalidating,
2. design-confounding,
3. measurement-threatening,
4. disclosure-limiting,
5. acceptable boundary.

For each category, the table states:

1. when the problem matters,
2. the appropriate reviewer decision,
3. an example in LLM-based audit research.

## Why This Matters For The Revision

The reviewers' contribution concern was not only that retrieval matters. They wanted to know why the new framework changes how audit research is designed, evaluated, and interpreted.

The new table directly answers that concern by showing:

1. not every retrieval limitation is fatal,
2. some retrieval failures invalidate inference,
3. some retrieval differences require sensitivity analysis,
4. some measurement issues require coder validation,
5. some limitations can be handled through disclosure when the claim is appropriately bounded.

## Table Renumbering

Because the new decision-rule table belongs in Section III after the adjacent-validity discussion, existing main-text tables were renumbered:

| Prior Label | New Label |
|---|---|
| Table 3: Five Dimensions | Table 4 |
| Table 4: Retrieval Typology | Table 5 |
| Table 5: Construct-to-Retrieval Mapping | Table 6 |
| Table 6: Claim Correctness Layers | Table 7 |
| Table 7: Tiered Reporting Standard | Table 8 |
| Table 8: Selected Claim-Level Examples | Table 9 |

The manuscript callouts and `Tables_and_Figures.md` placement summary were updated accordingly.

## Additional Terminology Alignment

While adding the table, the tables packet was aligned with the red-team wording pass:

1. `retrieval effects` -> `retrieval-conditioned information differences`
2. `audit-valid conclusions` -> `audit-boundary or audit-judgment conclusions`
3. `Audit-valid correctness` -> `Audit-boundary diagnostic`
4. `evidence-use divergence` -> `source-use divergence`
5. Tier 1 purpose revised from "changes valid inference" to "shows how retrieval environments can be specified, preserved, and linked to claim-level source use"

## QA

Search QA was run on the main manuscript and tables packet for high-risk phrases:

- `audit-valid`
- `audit-validity`
- `evidence-use`
- `changes valid inference`
- `changes the evidence basis`
- `What this validates`
- `does not validate`
- `retrieval effects`

No matches remained in the checked main manuscript and tables packet.

Table-number QA confirmed:

1. manuscript callouts now run from Table 1 through Table 9,
2. `Tables_and_Figures.md` headings now run from Table 1 through Table 9,
3. the placement summary includes the new Table 3 and the renumbered Tables 4-9.

## Remaining Boundary

This task adds a conceptual reviewer-decision table, not new empirical evidence. It strengthens the incremental contribution and reviewer usability of the framework, but it does not replace the planned empirical reinforcement workstreams for construct protocols, XBRL coverage diagnostics, coding independence, and bounded sensitivity checks.

## SR-00B Status

`SR-00B` is complete. The next execution item is `SR-00C`: add the audit-evidence hierarchy to the manuscript and supplement.
