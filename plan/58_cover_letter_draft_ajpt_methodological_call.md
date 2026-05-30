# Cover Letter Draft: AJPT Methodological Papers Call

## Purpose

This file drafts the cover letter for submission to **Auditing: A Journal of Practice & Theory** under the **Methodological Papers** call. The letter positions the manuscript as a research-methodology paper for LLM-based auditing research, not as an audit-practice procedure paper or technology benchmark.

## Cover Letter Draft

```text
[Date]

Professor Michael S. Wilkins
Senior Editor
Auditing: A Journal of Practice & Theory

Dear Professor Wilkins and Methodological Papers Call Editors:

We are pleased to submit our manuscript, "Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval," for consideration under AJPT's Methodological Papers call.

The manuscript fits the call's topics on research design and data/variable construction. It evaluates retrieval as a research-design choice in LLM-based auditing studies and provides best-practice guidance for collecting retrieval evidence, constructing claim-level evidence-use variables, and reporting retrieval-created information environments. The paper's central premise is that retrieval systems dynamically construct the information environment observed by an LLM; therefore, researchers may draw invalid inferences if they evaluate LLM outputs without validating what the retrieval pipeline selected, omitted, represented, and supplied to the model.

The manuscript introduces retrieval-environment validity, defined as the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct a researcher intends to study. We operationalize the framework through five validity dimensions: selection, representation, stability, traceability, and separability. The paper also provides a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting checklist, and reproducibility guidance.

The manuscript is designed as an auditing research methodology contribution. It does not propose an audit procedure, audit engagement workflow, auditor decision aid, or model-performance benchmark. XBRL is treated as management-reported structured accounting data that can support research-data construction and source traceability, not as audit evidence or ground truth. Similarly, the SEC/XBRL demonstration is descriptive and methodological: it illustrates how text retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline create different evidence environments for LLM-based auditing research.

To support reviewer inspection, the manuscript includes a two-layer demonstration design. The main text uses three familiar SEC filers for deep claim-level illustration, while the appendix reports a bounded six-filer extension spanning retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. The extension is not used to estimate population-level performance or failure-mode prevalence; it tests whether the retrieval-environment validity protocol remains applicable across varied reporting environments.

We believe the manuscript contributes to AJPT's methodological call in three ways. First, it identifies retrieval as a distinct research-design validity issue in LLM-based auditing research. Second, it shows how retrieval artifacts and LLM outputs can be converted into auditable claim-level evidence-use variables. Third, it provides practical reporting and reproducibility guidance that audit researchers and reviewers can use when evaluating future LLM/RAG studies.

[The manuscript has not been published and is not under consideration elsewhere.] [All authors have approved the submission.] [The authors have no conflicts of interest to disclose / Disclosures are provided on the title page.] [The manuscript includes supplemental materials intended for reviewer inspection and potential publication.] [A generative AI and AI-assisted technology disclosure is included in the manuscript.]

Thank you for considering our manuscript for AJPT's Methodological Papers call.

Sincerely,

[Author names and affiliations]
```

## Short Positioning Paragraph For Editorial Manager

Use this if the submission system asks for a brief manuscript description:

> This manuscript is submitted to AJPT's Methodological Papers call. It develops retrieval-environment validity as a research-design framework for LLM-based auditing research and provides best-practice guidance for retrieval design, evidence logging, claim-level variable construction, and reproducibility reporting. The paper does not propose an audit procedure or benchmark LLM performance; it addresses how researchers should design and evaluate LLM/RAG studies when the model's information environment is dynamically constructed through text retrieval, XBRL relational retrieval, or hybrid retrieval.

## Scope-Safeguard Sentences

Use these sentences if the cover letter needs to be shortened or if editors ask for clarification.

| Risk | Sentence |
|---|---|
| Editor reads the paper as audit-practice guidance | The manuscript addresses auditing research design, not audit engagement procedures. |
| Editor reads the paper as a systems paper | The retrieval prototype is used only to illustrate methodological issues; the contribution is the validity framework and reporting protocol. |
| Editor reads XBRL as an audit-evidence claim | XBRL is treated as management-reported structured accounting data, not as audit evidence or ground truth. |
| Editor reads the demonstration as a benchmark | The demonstration is descriptive and methodological, not a model-performance comparison. |
| Editor asks why it fits the call without statistical methods | The call includes research design, modeling, data collection, and variable construction; this manuscript addresses those areas for LLM-based auditing research. |

## Submission Checklist Items To Finalize

| Item | Status |
|---|---|
| Author names and affiliations | Needed |
| Date | Needed |
| Conflict-of-interest language | Needed from authors |
| Prior publication / concurrent submission statement | Needed from authors |
| Supplemental material statement | Needed after final appendix/repository decision |
| Generative AI disclosure statement | Drafted in `plan/56_ajpt_style_alignment_and_v3_revision_package.md`; authors must finalize |
| Title page | Needed as separate submission file |
| Data availability statement | Needed after final reproducibility-package decision |

## Reviewer-Facing Logic Embedded In The Letter

The cover letter deliberately repeats three ideas that should survive desk screening:

1. **Call fit:** research design and data/variable construction.
2. **Boundary:** not audit-practice procedures and not performance benchmarking.
3. **Contribution:** retrieval-environment validity plus claim-level evidence-use variables.

## Final Assessment

This cover letter should help the editor route the manuscript as an AJPT Methodological Papers submission rather than as a technology paper. The main remaining work is to fill in author-specific declarations and ensure the manuscript abstract, introduction, appendix, and AI disclosure match the same positioning.
