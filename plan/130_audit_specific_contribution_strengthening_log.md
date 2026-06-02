# Audit-Specific Contribution Strengthening Log

## Purpose

This revision implements SR-11 from the second-revision workflow. The objective is to make the paper read unmistakably as an auditing-methodology contribution rather than as general RAG documentation with audit examples.

## Implemented Revisions

1. Added intended audit-research use cases to the introduction:
   - archival audit research using LLMs as measurement tools;
   - audit analytics and retrieval/system-design studies;
   - judgment-and-decision-making studies of LLM-assisted audit judgments.
2. Clarified that the framework specifies the evidence environment observed by the LLM but does not establish audit evidence sufficiency or appropriateness.
3. Added a compact audit-specific example in Section V showing that the same inventory evidence can be:
   - text-supported;
   - graph-valid;
   - assertion-relevant;
   - still insufficient for an audit conclusion.
4. Added a discussion paragraph mapping the framework to three audit-research use cases and the audit-methodological requirement common to all three.
5. Strengthened the conclusion by stating that the paper's contribution is not generic retrieval documentation, but reviewer-evaluable rules for audit construct support, evidence meaning, traceability, source overreach, and audit evidence sufficiency boundaries.
6. Added `Appendix Table F1B. Same Evidence Across Audit Interpretation Levels` to the online supplement.
7. Updated manuscript appendix cross-references to include Appendix Table F1B.

## Reviewer-Facing Position

The revision clarifies that retrieval-environment validity matters in auditing because audit inferences depend on the source, nature, reliability, and evidentiary status of information. A faithful RAG answer can still be invalid for audit research if it treats management-reported filings as audit evidence or makes an audit conclusion unsupported by sufficient appropriate evidence.

## Files Revised

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## QA Focus

- Confirm that the manuscript uses audit-specific terms: sufficient appropriate evidence, assertion relevance, audit evidence sufficiency, audit-boundary diagnostics, management-reported XBRL, and audit judgment.
- Confirm that the new example does not imply that public filing text or XBRL can prove reserve adequacy, valuation correctness, GAAP compliance, fraud, or control failure.
- Confirm that Appendix Table F numbering remains internally consistent.

## Remaining Boundary

No new audit-domain expert coding was added in this step. Audit-boundary diagnostics remain qualitative/preliminary unless a future Tier 2 design adds expert coding, reconciliation, and reliability evidence.
