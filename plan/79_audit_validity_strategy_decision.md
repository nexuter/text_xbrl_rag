# Audit-Validity Strategy Decision

## Purpose

This memo decides whether the current submission package should:

1. preserve the boundary-only audit-validity path; or
2. add a limited audit-domain expert review of selected claims before submission.

The decision matters because audit-valid and integrated scores are the most likely point where reviewers may worry that the manuscript overclaims what the demonstration can support.

## Decision

For the current submission package, use the **boundary-only audit-validity path**.

Limited expert review remains a useful optional enhancement, but it is not required for the current manuscript because the paper's central claim does not depend on final audit-judgment correctness. The central claim is methodological:

> Retrieval-condition labels do not determine claim-level evidence use.

The demonstration uses audit-valid and integrated scores only as preliminary author-coded diagnostics to illustrate the claim-level correctness protocol. It does not use them as final evidence of audit judgment quality, model performance, retrieval superiority, or audit evidence sufficiency.

## Rationale

### 1. The Paper Is A Methodology Demonstration

The current paper is a Tier 1 methodological demonstration. It provides a framework, typology, coding protocol, reporting guidance, and source-to-context-to-output-to-claim evidence trail. It does not test a hypothesis about audit judgment quality.

Because the claims are methodological and bounded, independent expert coding is not required as a condition for the paper's main contribution.

### 2. The Main Empirical Illustration Does Not Depend On Audit-Valid Means

The main data-supported illustration is evidence-use divergence:

| Evidence | Count |
|---|---:|
| Total retrieval-conditioned outputs | 42 |
| Total preliminary coded claims | 182 |
| Hybrid claims | 60 |
| Hybrid claims using both text and XBRL | 7 |
| Hybrid claims using text only | 41 |
| Hybrid claims using XBRL only | 12 |

This claim depends on source-use classification and traceability, not on expert audit-validity scoring.

### 3. The Current Package Already Preserves The Required Boundary

The manuscript, tables/figures packet, supplement, README, and cover letter all state or imply that:

1. audit-valid and integrated scores are preliminary;
2. XBRL is not audit evidence or ground truth;
3. the demonstration is not a model-performance benchmark;
4. stronger audit-judgment claims require expert review.

This boundary language is sufficient for the current methodological claim.

### 4. Adding Limited Expert Review Now Could Create A New Incomplete Claim

Limited expert review would strengthen credibility if completed carefully. However, a weak or rushed expert-review exercise could create new reviewer questions:

1. Who were the experts?
2. Were they independent?
3. Were they blinded to retrieval condition?
4. How were disagreements resolved?
5. Why were only selected claims reviewed?
6. Are reviewed examples representative?

Unless the expert review is designed and executed cleanly, it may add complexity without changing the paper's central inference.

## Required Manuscript Discipline

The boundary-only path is defensible only if the final package follows these rules:

1. Do not report audit-valid or integrated scores as model accuracy.
2. Do not claim that hybrid retrieval improves audit reasoning.
3. Do not claim that XBRL retrieval improves audit judgment.
4. Do not claim that author-coded audit-valid scores are expert evidence.
5. Keep aggregate preliminary coding summaries in the supplement.
6. Use Table 7 only as selected examples of correctness layers and evidence-use divergence.
7. State that studies making stronger audit-judgment claims should use independent expert coding and reliability evidence.

## Required Language To Preserve

### Main Manuscript

> Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics. The demonstration supports claims about source traceability and claim-level evidence-use divergence, not final audit-judgment quality.

### Table 7 Note

> Scores are preliminary author-coded diagnostics used to illustrate the claim-level correctness protocol. They are not final expert audit-validity evidence and should not be interpreted as model-performance measures. Audit-valid and integrated diagnostics require audit-domain expert review before being used for stronger audit-judgment claims.

### Supplement

> Audit-valid and integrated scores are preliminary author-coded diagnostics. They should not be interpreted as model-performance measures, prevalence estimates, or final audit-validity evidence.

### README

> Audit-valid and integrated-correctness scores in the coding files are preliminary author-coded diagnostics unless independently reviewed by audit-domain experts.

## Optional Limited Expert Review Design

If the authors later decide to add a limited expert review, use the following minimum design.

### Scope

Review 15-20 selected claims:

1. all five main Table 7 claims;
2. five hybrid claims with text-only or XBRL-only evidence use;
3. five risk/assertion claims from the bounded extension;
4. optional additional claims involving CAT complexity and MSFT relation-path scarcity.

### Reviewer Profile

At least one audit-domain expert, preferably two:

1. audit faculty member;
2. experienced auditor or former auditor;
3. doctoral student with audit research training, if paired with senior review.

### Coding Conditions

At minimum, reviewers should receive:

1. claim text;
2. intended construct;
3. retrieved source evidence;
4. source IDs;
5. coding rubric.

Where feasible, reviewers should be blinded to retrieval condition and author-coded scores.

### Output

Produce a short expert-review appendix table:

| Claim ID | Author Preliminary Audit Diagnostic | Expert Review | Agreement | Reviewer Note |
|---|---:|---:|---|---|

### Use In Manuscript

If expert review is added, describe it as a limited validation check of selected illustrative claims, not as full expert coding of all 182 claims.

## Reviewer Response If Asked Why No Expert Review

Recommended response:

> The paper's primary claim is methodological: retrieval-condition labels do not determine claim-level evidence use. We therefore use audit-valid and integrated scores only as preliminary author-coded diagnostics to illustrate the proposed correctness protocol. We do not use these scores as final evidence of audit judgment quality or model performance. The manuscript explicitly states that studies making stronger audit-judgment claims should use independent audit-domain expert coding and reliability evidence.

## Final Reviewer Assessment

The boundary-only path is acceptable for the current paper because the manuscript is a methodological demonstration and because the main inference rests on source traceability and evidence-use divergence. The path would become unacceptable if the manuscript reported audit-valid means as performance evidence, ranked retrieval methods, or implied that preliminary scores validate audit judgment quality.

## Final Decision Statement

Proceed with the boundary-only audit-validity strategy for the current submission package. Treat limited expert review as an optional future enhancement, not as a blocker for submission preparation.
