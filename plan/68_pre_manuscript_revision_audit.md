# Pre-Manuscript Revision Audit

## Purpose

This memo checks whether any revisions or improvements should be completed before drafting the submission-ready v3 manuscript.

The review stance is that of an AJPT reviewer asking:

> If the authors write the manuscript now, what unresolved issues could still weaken the paper or trigger avoidable reviewer criticism?

## Reviewer Verdict

The project is **ready to proceed to v3 manuscript drafting**, but only under a disciplined drafting protocol.

The core contribution, demonstration data, appendix structure, table/figure strategy, and reproducibility materials are strong enough to support the manuscript. The remaining issues are not conceptual blockers. They are **pre-drafting decisions and manuscript-control constraints** that must be resolved or explicitly bounded before the full draft is written.

## High-Priority Improvements Before Drafting

### 1. Lock The Audit-Valid Coding Strategy

Current status:

The project repeatedly states that audit-valid and integrated-correctness scores are preliminary author-coded diagnostics unless reviewed by audit-domain experts.

Reviewer risk:

If the manuscript reports audit-valid means or selected examples without a strong boundary, reviewers may read the paper as making unsupported audit-judgment claims.

Required pre-manuscript decision:

Choose one of two paths before drafting:

| Path | Treatment | Reviewer Strength |
|---|---|---|
| Boundary-only path | State clearly that audit-valid and integrated scores are preliminary author-coded diagnostics; do not use them as evidence of audit judgment quality | Acceptable for a methodology paper |
| Limited expert-review path | Add one audit-domain expert review of 10-20 selected claims or one independent recoding subset | Stronger and more reviewer-friendly |

Recommended decision:

Proceed with the **boundary-only path** for v3 unless expert review can be obtained quickly. The manuscript's main inference should rest on source traceability and evidence-use divergence, not audit-valid scores.

Required wording:

> Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics. The demonstration supports claims about source traceability and claim-level evidence-use divergence, not final audit-judgment quality.

### 2. Create A Submission-Facing Replication README Before Or During V3

Current status:

The core reproducibility files exist and counts match expected claims. However, there is no single README that tells a reviewer how to navigate the package.

Reviewer risk:

Without a README, the reproducibility package may feel like a project archive rather than a submission supplement.

Recommended action:

Create a short replication README before the final v3 manuscript is marked submission-ready. It should include:

1. project purpose;
2. folder map;
3. source filing manifest;
4. script execution order;
5. local model configuration;
6. expected artifact counts;
7. known limitations;
8. data availability statement.

Drafting implication:

The v3 manuscript can proceed now, but the README should be completed before final submission packaging.

### 3. Decide Whether To Capture Exact Ollama Model Metadata

Current status:

The run summaries document provider, model name, temperature, and execution time. They do not yet preserve the exact local model digest or detailed model metadata.

Reviewer risk:

A reviewer may ask whether exact LLM output replication is possible.

Recommended action:

Before final submission, capture the local model metadata if available through the local Ollama environment and reference it in the appendix or README.

Drafting implication:

The manuscript should say:

> Exact output replication may depend on local model build and serving environment; the replication package preserves prompts, contexts, raw outputs, and model configuration metadata.

Do not claim exact model-level reproducibility unless the digest is captured.

### 4. Do Not Add VectorDB, RDF/OWL, Or GraphRAG Claims Beyond Guidance

Current status:

The project includes valuable implementation guidance for vector retrieval and RDF/OWL portability, but the actual demonstration uses keyword-ranked text retrieval and table-based XBRL relational retrieval.

Reviewer risk:

If the manuscript title, abstract, or demonstration suggests a completed ontology database, vector database, or GraphRAG implementation, reviewers may see a mismatch between claims and artifacts.

Required drafting rule:

Use this distinction consistently:

| Implemented In Demonstration | Guidance For Future Studies |
|---|---|
| Keyword-ranked contextual text retrieval | Vector DB, embedding model variation, reranking |
| Table-based XBRL fact/path retrieval | RDF/OWL triple store, graph database, GraphRAG |
| Source IDs and retrieval logs | Production-scale retrieval architecture |

Recommended wording:

> The demonstration uses an inspectable keyword/text retrieval prototype and table-based XBRL relational retrieval. Vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions and reporting considerations, not as completed performance claims.

### 5. Freeze The Main Demonstration Claim

Current status:

The data strongly support claim-level evidence-use divergence.

Reviewer risk:

The manuscript could drift into performance language because the data include condition labels and coding scores.

Required main claim:

> Retrieval-condition labels do not determine claim-level evidence use.

Supported statistic:

> In hybrid conditions, only 7 of 60 claims used both text and XBRL sources, while 41 used text only and 12 used XBRL only.

Claims to avoid:

1. Hybrid retrieval improves audit reasoning.
2. XBRL retrieval is more accurate than text retrieval.
3. `gemma4:31b` demonstrates audit expertise.
4. The extension validates the framework across SEC filers.
5. The observed failure-mode frequencies generalize to a population.

## Medium-Priority Improvements Before Drafting

### 6. Add A Short "What Researchers Should Do Differently" Box Or Paragraph

Reviewer risk:

Methodology papers can be criticized as conceptual checklists unless the practical takeaway is unmistakable.

Recommended manuscript element:

Add a concise paragraph near the end of the introduction and again in the conclusion:

> Researchers using LLMs in auditing studies should define the audit construct before retrieval, choose retrieval operators that match that construct, preserve the retrieved information environment, code outputs at the claim level, distinguish text-supported, graph-valid, audit-valid, and integrated claims, and report retrieval sensitivity proportional to the study's claims.

This paragraph will help answer the reviewer question:

> What would an audit researcher do differently after reading this paper?

### 7. Make The AJPT Call Fit Explicit But Not Repetitive

Current status:

The paper aligns with the AJPT Methodological Papers call through research design, modeling/variable selection, and data collection/variable construction.

Reviewer risk:

If the manuscript over-explains the call fit, it may sound like a cover letter. If it under-explains the fit, reviewers may classify it as a systems paper.

Recommended treatment:

Mention the call fit once in the introduction:

> The paper contributes to auditing research methodology by treating retrieval as a research-design and data/variable-construction problem in LLM-based audit studies.

Then let the framework, tables, and demonstration carry the point.

### 8. Keep Emerging Audit-System Papers In A Contrast Paragraph Only

Current status:

The reference package includes emerging LLM/RAG audit-system papers for contrast.

Reviewer risk:

Too much attention to audit-system papers could pull the manuscript toward audit automation or performance benchmarking.

Recommended treatment:

Use one concise contrast paragraph:

> Emerging LLM/RAG audit studies increasingly evaluate systems, agents, or task performance. Our focus is different: we provide criteria for auditing researchers to evaluate whether the retrieval-created information environment supports the inference they draw from LLM outputs.

Do not build the literature review around audit-system papers.

### 9. Decide How To Refer To Appendices In The Manuscript

Current status:

The final appendix package uses Appendix A-I and Appendix Tables A1-A10.

Reviewer risk:

If the manuscript cites internal project file paths, it will read like a working memo rather than a journal article.

Required drafting rule:

In the manuscript, cite appendices and tables, not local files:

| Avoid | Use Instead |
|---|---|
| `plan/65_final_appendix_package.md` | Appendix A-I |
| `data/processed/coding/...` | Appendix F |
| `plan/66_final_tables_and_figures_check.md` | Appendix Tables A1-A10 |
| `data/processed/retrieval_contexts/...` | Appendix D |

The local paths should remain in the planning and reproducibility package, not in the manuscript body.

### 10. Verify Recent Reference Status Before Final Submission

Current status:

The final reference package includes accepted, working-paper, and emerging 2025-2026 items.

Reviewer risk:

Recent LLM/accounting papers and audit-system papers may have changed publication status.

Recommended action:

Before final submission, verify publication status for:

1. Blankespoor, deHaan, and Li;
2. Kim, Muhn, and Nikolaev;
3. Wang and Wang;
4. emerging LLM/RAG audit-system papers used only as contrast.

Drafting implication:

The v3 draft can use the current reference package, but a final reference-status verification should occur before submission.

## Low-Priority Improvements That Should Not Delay V3

### 11. Raw-File Hash Manifest

Value:

Strengthens reproducibility if a public replication archive is released.

Decision:

Helpful but not required before manuscript drafting.

### 12. Top-k Or Chunk-Window Sensitivity Check

Value:

Would strengthen stability and selection-validity evidence.

Decision:

Not required for a Tier 1 methodological demonstration. Mention as future Tier 2/Tier 3 guidance unless performed.

### 13. RDF/OWL Export Example

Value:

Would strengthen the ontology portability angle.

Decision:

Do not add unless the manuscript shifts toward an ontology implementation paper. Current positioning should not require it.

### 14. Cross-Model Comparison

Value:

Would strengthen claims about model-generalizability.

Decision:

Do not add. The paper is method-agnostic but the demonstration is not a model comparison.

## Manuscript-Control Rules

Use these rules while drafting v3:

| Risk | Control Rule |
|---|---|
| Sounds like audit practice | Say "LLM-based auditing research," not "audit workflow improvement" |
| Sounds like retrieval benchmark | Say "methodological demonstration," not "performance evaluation" |
| XBRL overclaim | Say "management-reported structured data," not "audit evidence" |
| Hybrid overclaim | Say "hybrid creates possible integration," not "hybrid improves reasoning" |
| Audit-valid overclaim | Say "preliminary author-coded diagnostics," not "expert-validated audit correctness" |
| Generalizability overclaim | Say "bounded extension," not "validation across industries" |
| System-building drift | Say "reporting guidance," not "implemented production architecture" |
| Appendix overload | Refer to Appendix A-I, not file paths |

## Section-Specific Revision Guidance

### Abstract

Keep the 135-word abstract from `plan/56`, but ensure the final sentence says:

> without treating XBRL as audit evidence or benchmarking model performance.

### Introduction

Must include:

1. retrieval as research design;
2. retrieval-environment validity definition;
3. contribution hierarchy;
4. data/variable-construction contribution;
5. two-layer demonstration;
6. what the paper is not.

Avoid:

1. long technical discussion of XBRL ontology;
2. claims about audit workflow improvement;
3. language implying LLM audit competence.

### Related Literature

Organize around four contrasts:

1. AJPT methodology guidance;
2. XBRL/text-as-data;
3. LLM accounting research;
4. audit analytics and emerging LLM/RAG audit-system work.

End the section with:

> Prior work studies data, tools, models, auditors, or outcomes. This paper studies the retrieval-created information environment that connects source data to LLM output in auditing research designs.

### Framework

Keep this as the conceptual center. Do not let the demonstration appear before the framework has done its work.

### Retrieval Designs

Use Table 3 and Table 4 to show that retrieval design should follow construct definition. This is where XBRL relational retrieval should be introduced as one retrieval environment, not as the superior environment.

### Correctness Protocol

Make claim-level coding the unit of analysis. Explicitly say that a claim can be text-supported and graph-valid but still not audit-valid.

### Reporting Guidance

Keep the guidance tiered. This prevents the checklist from feeling too burdensome and explains why the current paper is Tier 1.

### Demonstration

Use this sequence:

1. data sources and case design;
2. retrieval conditions;
3. LLM execution and claim coding;
4. main deep cases;
5. bounded extension;
6. what the demonstration shows;
7. what the demonstration does not show.

Only one main result table should appear: selected claim-level examples.

### Discussion And Conclusion

End with a clear methodological takeaway:

> In LLM-based auditing research, retrieval is not an implementation detail; it is part of the research design that determines the information environment from which output-based inferences are drawn.

## Pre-Manuscript Go / No-Go Checklist

| Item | Status | Manuscript Action |
|---|---|---|
| Core contribution locked | Go | Use retrieval-environment validity as central construct |
| AJPT call fit locked | Go | Frame as research design and variable construction |
| Demonstration claim locked | Go | Evidence-use divergence only |
| Data counts verified | Go | Use 42 outputs and 182 claims |
| Appendix structure finalized | Go | Cite Appendix A-I |
| Table/figure placement finalized | Go | Main text: 7 tables, 2 figures |
| Reproducibility artifacts checked | Go | Use data availability statement |
| Expert-coding strategy | Conditional go | Use boundary-only path unless expert review is added |
| Replication README | Conditional go | Needed before final supplement, not before drafting |
| Ollama model metadata | Conditional go | Capture before final release if possible |
| Reference status verification | Conditional go | Verify before final submission |
| Raw checksums | Optional | Useful for public archive |

## Final Assessment

There are **no major conceptual or data-related blockers** to writing the v3 manuscript.

The main improvements before or during manuscript drafting are:

1. adopt the boundary-only audit-valid coding strategy unless expert review is added;
2. keep aggregate coding summaries out of the main text;
3. create a submission-facing replication README before final packaging;
4. avoid vector/RDF/GraphRAG implementation claims;
5. verify recent reference status before final submission;
6. use appendix and table labels rather than local file paths.

## Final Decision

**Proceed to v3 manuscript drafting.**

The draft should be written under the controls in this memo. The manuscript will likely be weakened only if it drifts away from its final identity:

> A research-methodology paper on retrieval-environment validity and claim-level data/variable construction for LLM-based auditing research.
