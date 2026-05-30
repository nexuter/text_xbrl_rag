# Final Cover Letter Submission Template

## Purpose

This file provides the final submission-facing cover letter template for the AJPT Methodological Papers call. It updates the earlier cover letter draft to reflect the completed v3 submission package, including the separate tables/figures file, online supplement, replication README, model metadata note, and checksum manifest.

Author-specific fields remain in brackets because they require final author confirmation.

## Cover Letter

```text
[Submission date]

Professor Michael S. Wilkins
Senior Editor
Auditing: A Journal of Practice & Theory

Dear Professor Wilkins and Methodological Papers Call Editors:

We are pleased to submit our manuscript, "Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval," for consideration under AJPT's Methodological Papers call.

The manuscript fits the call's focus on research design, modeling, variable selection, data collection, and variable construction. It addresses a methodological problem that arises when audit researchers use large language models (LLMs) with retrieval-augmented information environments: retrieval systems dynamically select, omit, rank, transform, and present the information observed by the model. If researchers evaluate LLM outputs without validating the retrieval-created information environment, they may attribute output differences to model capability, prompt quality, or audit reasoning when those differences arise from retrieval design.

The manuscript introduces retrieval-environment validity, defined as the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct a researcher intends to study. We operationalize the framework through five validity dimensions: selection, representation, stability, traceability, and separability. The paper also provides a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, tiered reporting standard, and reproducibility guidance.

The manuscript is designed as an auditing research methodology contribution. It does not propose an audit procedure, audit engagement workflow, auditor decision aid, or model-performance benchmark. XBRL is treated as management-reported structured accounting data that can support research-data construction and source traceability, not as audit evidence or ground truth. The SEC/XBRL demonstration is descriptive and methodological: it illustrates how text retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline create different evidence environments for LLM-based auditing research.

The submission package includes a two-layer methodological demonstration. The main manuscript uses three familiar SEC filers for deep claim-level illustration. The online supplement reports a bounded six-filer extension spanning retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. The extension is not used to estimate population-level performance or failure-mode prevalence; it tests whether the retrieval-environment validity protocol remains applicable across varied reporting environments.

To support reviewer inspection, we submit the manuscript with a separate tables and figures file, an online appendix/supplement, and replication materials. The supplement documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, selected source spot checks, bounded-extension diagnostics, and sensitivity guidance. The replication materials include the filer manifest, extraction and retrieval scripts, text chunks, XBRL fact and relation-path tables, retrieval logs, rendered prompts, raw LLM outputs, claim-level coding files, a replication README, a local model metadata note, and a SHA-256 checksum manifest.

We believe the manuscript contributes to AJPT's methodological call in three ways. First, it identifies retrieval as a distinct research-design validity issue in LLM-based auditing research. Second, it shows how retrieval artifacts and LLM outputs can be converted into claim-level evidence-use variables. Third, it provides reporting and reproducibility guidance that audit researchers and reviewers can use when evaluating future LLM/RAG studies.

The manuscript has not been published and is not under consideration elsewhere. [All authors have approved the submission.] [The authors have no conflicts of interest to disclose / Disclosures are provided on the title page.] [The manuscript includes supplemental materials intended for reviewer inspection and potential publication.] A generative AI and AI-assisted technology disclosure is included in the manuscript.

Thank you for considering our manuscript for AJPT's Methodological Papers call.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
[On behalf of all authors]
```

## Short Submission-System Description

Use this paragraph if the submission system requests a brief manuscript description:

> This manuscript is submitted to AJPT's Methodological Papers call. It develops retrieval-environment validity as a research-design framework for LLM-based auditing research and provides guidance for retrieval design, evidence logging, claim-level variable construction, and reproducibility reporting. The paper does not propose an audit procedure or benchmark LLM performance; it addresses how researchers should design and evaluate LLM/RAG studies when the model's information environment is dynamically constructed through text retrieval, XBRL relational retrieval, or hybrid retrieval.

## Submission Package Statement

Use this concise statement if the submission system asks about supplemental materials:

> The submission includes a separate tables and figures file, an online appendix/supplement, and replication materials. The online supplement documents the source-to-context-to-output-to-claim evidence trail. The replication materials include source manifests, extraction and retrieval scripts, processed retrieval artifacts, rendered prompts, LLM outputs, claim-level coding files, model metadata, and checksum files.

## Fields Requiring Author Confirmation

| Field | Status | Action |
|---|---|---|
| Submission date | Placeholder | Fill at submission |
| Corresponding author | Placeholder | Fill at submission |
| Author names and affiliations | Placeholder | Fill at submission |
| Author approval statement | Drafted | Confirm with all authors |
| Conflict-of-interest statement | Alternative language provided | Select final wording |
| Prior publication / concurrent submission statement | Drafted | Confirm with all authors |
| Supplemental material statement | Drafted | Confirm final file package |
| Generative AI disclosure | Included in manuscript | Confirm final wording |

## Editorial Positioning Safeguards

| Possible Editorial Misreading | Cover Letter Safeguard |
|---|---|
| The paper is an audit-practice tool | States that the manuscript is an auditing research methodology contribution |
| The paper is a model benchmark | States that the demonstration is descriptive and methodological |
| The paper treats XBRL as audit evidence | States that XBRL is management-reported structured data, not audit evidence or ground truth |
| The paper is a retrieval-system architecture paper | Frames retrieval as research design and variable construction |
| The paper lacks AJPT call fit | Explicitly links the manuscript to research design, data collection, and variable construction |

## Final Assessment

This cover letter is submission-ready except for author-specific declarations. It should help the editor route the manuscript as an AJPT Methodological Papers submission rather than as an audit-automation, RAG-system, or XBRL-ontology paper.
