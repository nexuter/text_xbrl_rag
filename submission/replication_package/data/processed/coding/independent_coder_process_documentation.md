# Independent Coder Process Documentation

## Purpose

This document records the independent coding process used for the 120-claim validation sample. It is intended to make the measurement-validation procedure reviewer-evaluable. The process supports reliability evidence for claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, integrated correctness, and confidence coding. It does not convert qualitative audit-boundary notes into final audit-judgment evidence.

## Sample Construction

| Design Element | Implementation |
|---|---|
| Source archive | Full 281-claim author-coded archive from the nine-filer protocol-validation demonstration |
| Validation sample size | 120 claims |
| Hybrid coverage | All 89 hybrid-condition claims |
| Non-hybrid anchors | 31 comparison claims: 12 LLM-only, 10 XBRL-only, and 9 text-only |
| Rationale | Hybrid claims were intentionally oversampled because the central measurement question is whether a hybrid retrieval condition actually produces integrated text-XBRL source use |
| Unit of coding | Claim-level assertion, not response-level output |

## Coder Materials

| Material | Purpose |
|---|---|
| Coder instructions | Step-by-step completion guidance |
| Coding protocol | Variable definitions, decision rules, and reliability expectations |
| Codebook | Allowed values and concise definitions |
| Claim evidence packet | Claim text, filer metadata, retrieval condition, and source identifiers needed to evaluate each claim |
| Blank coding form | Independent coder input form with coding fields left blank |

## Independence And Blinding

| Process Feature | Implementation |
|---|---|
| Independent coding | Two coders completed the same 120-claim sample separately |
| Author-code blinding | Coders received blank coding fields and were not asked to copy or verify author codes |
| Source availability | Coders received claim text and source identifiers needed to assess support; they were instructed not to conduct outside company research |
| Retrieval-condition visibility | Coders could see the retrieval condition because condition labels are necessary for interpreting source availability and `integrated_code`; the exercise therefore validates coding consistency, not blinded treatment effects |
| Coder role boundary | Coders were used to evaluate the measurement protocol. They are not represented as audit-domain expert validators unless separately documented |

## Variables Independently Coded

| Variable | Reliability Purpose |
|---|---|
| Claim segmentation agreement | Whether the row is a separately assessable assertion |
| Claim kind | Whether the claim is factual, risk/assertion, integration, boundary, or other |
| Evidence-use type | Whether the claim uses no source, text only, XBRL only, integrated text-XBRL evidence, or ambiguous evidence |
| Text-supported correctness | Whether cited or supplied text supports the claim |
| Graph-valid correctness | Whether XBRL facts, contexts, units, periods, or relation paths support the claim |
| Integrated correctness | Whether text and XBRL evidence are jointly used in one coherent inferential bridge |
| Audit-boundary note | Qualitative note about whether the claim overreaches beyond public filing or management-reported XBRL support |
| Confidence | Coder confidence in the assigned codes |

## Key Instruction Clarification

The revised protocol specifies that `integrated_code` applies to every validation-sample claim. Ordinary non-integration is coded as `0`, not `NA`. Text-only, XBRL-only, LLM-only, and hybrid-but-one-source claims therefore normally receive `integrated_code = 0`.

## Reliability Results

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Reconciliation Procedure

Disagreements were preserved in a disagreement file and summarized in reconciliation notes. Three focal disagreements remained after recoding. They involved the boundary between factual accounting-policy descriptions and risk/assertion inferences. The disagreements did not affect evidence-use type or integrated correctness, both of which reached 100.0 percent agreement.

## Interpretation Boundary

The independent coding exercise validates that the central claim-level variables can be applied consistently by coders using the provided protocol. It does not establish model performance, retrieval-method superiority, audit evidence sufficiency, or final audit-judgment correctness. Stronger audit-boundary or audit-judgment claims would require audit-domain expert coding, reconciliation procedures, and reliability evidence targeted to those claims.
