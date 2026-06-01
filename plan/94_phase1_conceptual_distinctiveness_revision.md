# Phase 1 Conceptual Distinctiveness Revision

## Purpose

This phase implements the first action item from the two-reviewer comprehensive revision plan: sharpen the conceptual distinctiveness of retrieval-environment validity so that reviewers can see why the paper is a methodology contribution rather than a repackaging of RAG implementation detail, construct validity, or reproducibility.

## Reviewer Concern Addressed

The main risk was that reviewers could read retrieval-environment validity as a new label for familiar validity concepts. That would weaken the paper's novelty and make the contribution appear descriptive. The revision now positions retrieval-environment validity as a retrieval-specific diagnostic lens for construct drift in LLM-based audit research.

## Manuscript Revisions Completed

- Added a new Section III subsection: `Relation To Adjacent Validity Concepts`.
- Clarified that retrieval-environment validity does not replace construct validity, measurement validity, internal validity, audit evidence sufficiency, or reproducibility.
- Explained the incremental mechanism: in dynamic retrieval designs, the information package supplied to the model is created at runtime, so validity depends on whether retrieved materials instantiate the intended audit construct.
- Added concrete audit-research counterexamples:
  - a revenue-recognition risk study where generic risk-factor retrieval omits contract-liability, variable-consideration, and XBRL relation evidence;
  - a hybrid-retrieval comparison where condition effects are confounded with prompt length, evidence labels, ordering, or token budget.
- Added reviewer-facing decision rules:
  - fatal to inference when retrieval changes the construct or prevents separability for a causal claim;
  - fixable when logs, source identifiers, and parameters permit reconstruction and bounded sensitivity checks;
  - a reporting gap when illustrative claims are made and omitted retrieval detail does not alter interpretation.

## Table Revisions Completed

Added a new main-text `Table 2. Retrieval-Environment Validity Versus Adjacent Validity Concepts`.

The table distinguishes retrieval-environment validity from:

1. construct validity;
2. measurement validity;
3. internal validity;
4. audit evidence sufficiency;
5. audit documentation;
6. textual-analysis preprocessing validation;
7. RAG system evaluation;
8. reproducibility.

Subsequent tables were renumbered so that the selected claim-level examples now appear as Table 8.

## Files Updated

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Tables_and_Figures.md`
- `plan/69_submission_ready_manuscript_v3.md`
- `plan/71_v3_main_tables_and_figures.md`

## Reviewer-Response Position

The revised argument should support the following response to reviewers:

> We agree that the original draft needed to distinguish retrieval-environment validity more explicitly from adjacent validity and reproducibility concepts. We therefore added a new Section III subsection and a new Table 2 that identify the retrieval-specific failure mechanism: dynamic retrieval creates the model's information environment at runtime, so construct validity and reproducibility can fail even when the prompt, model, and corpus are disclosed. The revision also adds concrete audit-research examples and decision rules for distinguishing inference-threatening retrieval flaws from fixable documentation gaps.

## Remaining Follow-Up

The conceptual revision is complete for Phase 1. Later phases should continue using this sharpened framing when revising validation, sensitivity, hybrid-integration, technical-specificity, and contribution-language sections.
