# Phase 6 Demonstration Reviewer Stress Test

## Purpose

This memo evaluates whether the Phase 6 methodological demonstration is strong enough to support the paper's AJPT-style methodology contribution.

The assessment is written from the perspective of a skeptical reviewer.

## Reviewer Verdict

Conditional favorable.

The demonstration is now strong enough to support the paper's methodological claim if the manuscript keeps the inference bounded and moves the full reproducibility trail to the appendix.

The demonstration should not be presented as evidence that hybrid retrieval is better, that XBRL improves audit reasoning, or that `gemma4:31b` has strong audit expertise. It should be presented as evidence that retrieval design changes the evidence basis and valid interpretation of LLM audit claims.

## Acceptance Criteria Check

| Criterion | Status | Reviewer Assessment |
|---|---|---|
| Uses actual SEC filings and Inline XBRL | Met | Nike, Starbucks, and Target filings were downloaded, extracted, and used. |
| Retrieval conditions are inspectable | Met | Context files, prompts, retrieval logs, and manifests are preserved. |
| Compares retrieval designs without ranking | Met with caution | Draft language avoids ranking, but manuscript must maintain this discipline. |
| Applies claim-level correctness protocol | Met preliminarily | 94 claims were segmented and preliminarily coded; expert review remains needed. |
| Shows inference shift | Met | Hybrid outputs sometimes integrate evidence, but often remain text-only or XBRL-only at claim level. |
| Includes LLM-only diagnostic baseline | Met | Baseline outputs stated context insufficiency rather than generating filing-specific claims. |
| Provides source and graph spot-checks | Met for selected examples | Selected examples trace to processed chunks/facts and raw Inline XBRL where applicable. |

## Main Strengths

### 1. The Demonstration Shows the Paper's Central Point

The most persuasive result is not that one retrieval design performs better. The persuasive result is that retrieval-condition labels are not enough.

A hybrid prompt can generate:

- a truly integrated text-XBRL factual claim;
- an XBRL-only claim inside a hybrid condition;
- a text-only claim inside a hybrid condition;
- a no-context diagnostic statement under the baseline condition.

This supports the paper's central contribution: retrieval is part of research design because it shapes what kind of claim can be validly inferred from the LLM output.

### 2. The Selected Examples Are No Longer Too Narrow

The selected example table now includes all three demonstration filers:

- Starbucks: integrated inventory corroboration.
- Nike: revenue risk cue examples and LLM-only diagnostic.
- Target: inventory XBRL-only claim inside a hybrid condition.

This reduces the concern that the demonstration is driven by one company's idiosyncratic filing.

### 3. Source Traceability Is Credible

The selected examples are tied to:

- actual LLM output files;
- prompt and context files;
- extracted text chunks;
- processed XBRL fact tables;
- raw Inline XBRL tags for the selected XBRL facts.

This is enough for a methodology demonstration, provided the paper does not claim that all 94 claims have been manually verified.

### 4. The LLM-Only Baseline Helps With Pretraining Risk

The familiar filer choice remains a review risk, but the LLM-only baseline makes the risk visible. The model did not generate filing-specific claims when context was absent. This does not eliminate pretraining contamination, but it supports the traceability design.

## Remaining Reviewer Concerns

### Concern 1: Audit-valid coding is still preliminary.

This is the largest remaining weakness. The current audit-valid and integrated scores are author-coded and partly rule-assisted. A reviewer will not accept them as final expert judgment.

Required manuscript handling:

- Label current coding as preliminary in development materials.
- For the final paper, either obtain expert review for selected examples or describe the demonstration as author-coded illustrative evidence.
- Avoid numeric audit-valid conclusions unless expert coding is completed.

### Concern 2: The table may still look like cherry-picking.

The selected examples are defensible because they cover pre-specified evidence types, but the main text should disclose that the full 94-claim table is in the appendix.

Required manuscript handling:

- State that selected examples were chosen to illustrate pre-specified divergence patterns.
- Provide the full claim table in appendix.
- Report the condition-level summary, but avoid treating preliminary means as final performance results.

### Concern 3: Integrated correctness may be too strict or too narrow.

Some readers may argue that a claim does not need to cite both text and XBRL to be useful in a hybrid condition. That is correct. The paper should clarify that "useful" and "integrated" are not the same construct.

Required manuscript handling:

> A hybrid output may contain useful text-supported or graph-valid claims without satisfying integrated correctness. Integrated correctness is reserved for claims that reconcile narrative, structured reported facts, and audit reasoning within the same claim.

### Concern 4: XBRL fact verification may be mistaken for audit evidence.

The spot-check verifies reported values, not audit evidence sufficiency.

Required manuscript handling:

- Repeat that XBRL is management-reported structured data.
- Do not imply that graph-valid claims are audit-valid because the XBRL fact exists.
- Keep audit-valid language as "risk cue" or "assertion-mapping consideration."

### Concern 5: The demonstration does not yet include inter-rater reliability.

This is acceptable for a descriptive methodology demonstration, but not for a hypothesis-testing study.

Required manuscript handling:

- State that the demonstration is descriptive.
- Present inter-rater reliability as required guidance for future hypothesis-testing applications.
- If possible, add expert review of selected examples before submission.

## Required Revisions Before Manuscript Integration

1. Keep Table X as a selected-example table, not a results table.
2. Add a short paragraph explaining example-selection logic:
   - one integrated corroboration case;
   - one XBRL-only-in-hybrid case;
   - one text-only-in-hybrid case;
   - one LLM-only diagnostic;
   - one additional filer-coverage example.
3. Move the 94-claim table to the appendix.
4. Move source spot-check details to the appendix.
5. In the main text, report only the inference shift, not a headline correctness score.
6. Obtain or simulate an expert-review protocol before final submission; do not present preliminary audit-valid scores as final.

## Final Reviewer-Style Assessment

From a reviewer perspective, the Phase 6 demonstration is now viable for an AJPT methodology paper.

The demonstration works because it does not try to prove that XBRL or hybrid retrieval improves audit performance. Instead, it shows that:

- retrieval design changes the evidence available to the LLM;
- claim-level source use can differ from retrieval-condition labels;
- graph-validity and text-support are distinct from audit-valid inference;
- hybrid retrieval requires evidence-use coding before researchers can claim integrated reasoning;
- no-context baselines help diagnose traceability and pretraining risk.

The remaining risk is not conceptual. It is evidentiary: the final paper must be transparent that audit-valid and integrated correctness require expert judgment. If that limitation is handled carefully, the demonstration should receive a favorable methodological assessment.

## Next Step

Proceed to Phase 7 reproducibility and reporting materials:

- main-text reporting checklist;
- appendix reporting checklist;
- sensitivity check guidance;
- appendix templates for retrieval logs, prompts, claim coding, failure modes, and source spot-checks.

