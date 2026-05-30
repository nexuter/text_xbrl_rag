# AJPT Style Alignment and V3 Revision Package

## Purpose

This file converts the project from a strong pre-extension manuscript draft into an AJPT Methodological Papers submission package. The manuscript identity is now fixed:

> A research-methodology paper for LLM-based auditing research, not an audit-practice procedure paper and not a retrieval-system performance benchmark.

## Official Style And Call Anchors

| Source | Requirement or Signal | Manuscript Implication |
|---|---|---|
| AJPT journal page | AJPT centers original research that improves auditing theory or auditing methodology. | Emphasize contribution to auditing research methodology. |
| AJPT Methodological Papers call | The call is for studies that introduce methods or recommendations applicable to auditing research. | Frame retrieval-environment validity as research-design guidance. |
| AJPT Methodological Papers call | The call does not cover papers about recommendations for audit procedures or audit methodologies in practice. | Avoid sounding like an LLM audit tool or audit engagement workflow. |
| AAA Manuscript Preparation Guide | Abstract must be no more than 150 words. | Replace v2's long abstract with a concise AJPT-style abstract. |
| AAA Manuscript Preparation Guide | Article text begins after the abstract and generative AI disclosure with `I. INTRODUCTION`. | Convert numeric section headings to AJPT roman-numeral headings. |
| AAA Manuscript Preparation Guide | Initial submissions to most AAA journals should not exceed 55 pages including references, figures, tables, and appendices. | Move implementation tables, aggregate coding summaries, and detailed extension evidence to appendix/supplement. |
| AAA Manuscript Preparation Guide | Authors must disclose AI and AI-assisted tools; use in research design and analysis should be described in the methodology. | Include a disclosure statement after the abstract and describe `gemma4:31b` use in the demonstration methods. |
| AAA Manuscript Preparation Guide | Materials intended for peer review can be submitted as one file or multiple files, while non-review materials are separate. | Prepare manuscript, appendix, and reproducibility artifacts as review materials; keep cover letter and title page separate. |

Official sources:

- AJPT journal page: https://aaahq.org/Research/Journals/Auditing-A-Journal-of-Practice-and-Theory
- AJPT Methodological Papers call: https://aaahq.org/portals/0/documents/calls/2025/AJPT%20Methodological%20Papers.pdf
- AAA Manuscript Preparation Guide: https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide

## V2 To V3 Revision Diagnosis

| V2 Element | Problem For AJPT Methodological Call | V3 Treatment |
|---|---|---|
| Long abstract | Exceeds AJPT-style abstract length and reads like a compressed full paper. | Replace with a sub-150-word abstract. |
| Section numbering as `1`, `2`, `3` | Does not follow AAA first-level heading convention. | Use `I. INTRODUCTION`, `II. RELATED LITERATURE`, etc. |
| Demonstration limited in main draft to three filers | Predates bounded extension and may invite generalizability criticism. | Use two-layer design: three deep cases in main text; six-filer extension in appendix. |
| XBRL language occasionally sounds like an enhancement to LLM reasoning | Could be read as audit-technology advocacy. | Use "management-reported structured data" and "research-data construction" language. |
| Aggregate coding table in main manuscript | Could be misread as model performance evidence. | Move Table 9A/9B to appendix unless expert-coded reliability is completed. |
| No explicit AI writing/process disclosure | AAA now requires AI and AI-assisted tools disclosure. | Add disclosure after abstract and before Introduction. |
| Reproducibility materials described but not submission-packaged | Reviewers need a clean appendix route. | Reference updated appendix package in `plan/43_phase8_appendix_materials_package.md`. |

## AJPT-Aligned Title

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

This title remains appropriate. It foregrounds research design and validity rather than audit automation or model performance.

## AJPT-Aligned Abstract

Retrieval-augmented large language models are increasingly used in accounting and auditing research, yet retrieval is often treated as a technical implementation step rather than as part of research design. We introduce retrieval-environment validity: the extent to which the information dynamically retrieved for an LLM aligns with the audit construct a researcher intends to study. The framework identifies five dimensions: selection, representation, stability, traceability, and separability. We operationalize the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting guidance, and an SEC/XBRL-based methodological demonstration. The demonstration uses text retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline to show that retrieval-condition labels can mask different claim-level evidence bases. The paper provides guidance for designing, evaluating, and reporting LLM-based auditing research without treating XBRL as audit evidence or benchmarking model performance.

Word count: 135.

## Declaration Of Generative AI And AI-Assisted Technologies In The Writing Process

Draft disclosure to be finalized by the authors:

> The authors used generative AI and AI-assisted tools to support manuscript drafting, editing, code development, and organization of reproducibility materials. The authors reviewed, revised, and are responsible for all manuscript content, analyses, source interpretations, and conclusions. The use of LLMs as part of the methodological demonstration is described in the demonstration section and supporting appendix materials.

Reviewer note: this statement should be reviewed against the final authors' actual use of AI tools before submission.

## V3 Manuscript Structure

Use the following AJPT-style first-level headings.

```text
I. INTRODUCTION
II. RELATED LITERATURE AND METHODOLOGICAL POSITIONING
III. RETRIEVAL-ENVIRONMENT VALIDITY
IV. RETRIEVAL DESIGNS FOR LLM-BASED AUDITING RESEARCH
V. CLAIM-LEVEL CORRECTNESS AND FAILURE MODES
VI. REPORTING GUIDANCE AND REPRODUCIBILITY STANDARDS
VII. METHODOLOGICAL DEMONSTRATION
VIII. DISCUSSION AND BOUNDARY CONDITIONS
IX. CONCLUSION
REFERENCES
APPENDIX
```

This structure keeps the paper in the methodological call. The demonstration comes after the framework and reporting guidance, making it an illustration of the method rather than the paper's main empirical contribution.

## V3 First Page Draft

### I. INTRODUCTION

Large language models are increasingly being studied in accounting and auditing research. Many research designs augment these models with external information through retrieval-augmented generation. In these designs, the model may receive financial filing text, accounting standards, structured reporting data, audit-workpaper-like materials, or other domain-specific sources before generating a response. The methodological problem is that retrieval is often described as an implementation step, even though it determines what information the model observes.

The paper aligns with AJPT's Methodological Papers call by evaluating a research-design problem in LLM-based auditing research: how retrieval choices construct the information environment from which LLM outputs are generated, and how researchers should collect, represent, and code retrieval artifacts so that audit-related inferences are valid and reproducible.

This paper argues that retrieval should be treated as part of research design in LLM-based auditing research. A retrieval system does not merely add information to a prompt. It constructs the information environment from which the model generates its response. It selects sources, ranks evidence units, traverses relations, filters contexts, truncates materials, formats evidence, and determines which parts of the source corpus are visible to the model. When researchers evaluate LLM outputs without validating this retrieval-created information environment, they may attribute differences in outputs to model capability, prompt quality, or audit reasoning when those differences arise from retrieval design.

This distinction matters because audit research constructs depend on the source, nature, and evidentiary status of information. Narrative disclosures may support analysis of management explanations, accounting policy language, or disclosed risk cues. XBRL tags, facts, contexts, and linkbase relations may support analysis of management-reported accounting relationships. Neither source is equivalent to audit evidence. A claim can be supported by retrieved text and consistent with XBRL facts while still overstating what the evidence can support as audit reasoning. Conversely, a response can appear weak because the retrieval pipeline failed to supply construct-relevant information.

We introduce retrieval-environment validity as a diagnostic framework for this problem. Retrieval-environment validity is the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct the researcher intends to study. The concept does not replace construct validity. It identifies a retrieval-specific mechanism through which construct validity can fail in studies where the model's information set is created at runtime.

The paper contributes to auditing research methodology in three ways. First, it defines retrieval-environment validity and identifies five dimensions: selection, representation, stability, traceability, and separability. Second, it operationalizes the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting checklist, and reproducibility guidance. These tools speak directly to research design and data/variable construction for LLM-based auditing research by converting retrieval artifacts and model responses into study-level variables, including text-supported correctness, graph-valid correctness, audit-valid correctness, integrated correctness, evidence-use type, and failure-mode labels. Third, it provides a descriptive methodological demonstration using SEC filing text and Inline XBRL data to show how retrieval design changes the evidence basis of LLM-generated audit claims.

The central research question is:

> How does retrieval design affect the validity of inferences drawn from LLM-based auditing research?

Answering this question changes how researchers should design and evaluate LLM audit studies. Researchers should define the audit construct before retrieval, choose retrieval operators that fit that construct, log the evidence actually supplied to the model, evaluate output claims by correctness layer, distinguish management-reported XBRL relations from audit evidence, and report retrieval sensitivity proportional to the study's claims.

We illustrate the framework using a two-layer demonstration design. The main demonstration uses three familiar SEC filers for deep source tracing and claim-level illustration. The appendix reports a bounded six-filer extension selected for variation in industry, scale, reporting complexity, and construct fit. The demonstration's evidentiary contribution is not that one retrieval design performs better. It is that response-level retrieval labels are insufficient: claims within the same condition can rely on different evidence bases, and those differences change the research inference. A hybrid condition can produce integrated text-XBRL claims, but it can also produce claims that rely only on text, only on XBRL, or on insufficient retrieved evidence. The demonstration is not designed to rank retrieval methods, evaluate a model's audit expertise, or estimate population-level failure rates.

Emerging LLM/RAG audit studies increasingly evaluate systems, agents, or task performance. Our focus is different: we provide criteria for auditing researchers to evaluate whether the retrieval-created information environment supports the inference they draw from LLM outputs.

## V3 Demonstration Section Treatment

### VII. METHODOLOGICAL DEMONSTRATION

Recommended subsection structure:

```text
Data Sources And Case Design
Retrieval Conditions
LLM Execution And Claim Coding
Main Deep Cases
Bounded Extension
What The Demonstration Shows
What The Demonstration Does Not Show
```

Key wording:

> The demonstration uses an inspectable keyword/text retrieval prototype and table-based XBRL relational retrieval over extracted facts and relation paths. Vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions and reporting considerations, not as completed performance claims in this study.

Demonstration claim to preserve:

> The demonstration's evidentiary contribution is not that one retrieval design performs better. It is that response-level retrieval labels are insufficient: claims within the same condition can rely on different evidence bases, and those differences change the research inference.

Bounded extension wording:

> The primary demonstration uses three familiar filers for deep source tracing and claim-level illustration. To reduce the concern that the framework reflects only those cases, we also conduct a bounded six-filer extension selected for variation in industry, scale, reporting complexity, and construct fit. The extension is not designed to estimate model performance or failure-mode prevalence. It tests whether the retrieval-environment validity protocol remains applicable across varied reporting environments.

Expert-coding boundary wording:

> Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics unless independently reviewed by audit-domain experts. The main demonstration supports claims about source traceability and claim-level evidence-use divergence. Studies that make stronger claims about audit judgment quality should use expert coding, coder independence, and reliability procedures appropriate to those claims.

## Main-Text Table And Figure Placement

| Main Text Item | Placement | Reason |
|---|---|---|
| Figure 1. Retrieval-Environment Validity Framework | Section III | Core conceptual contribution. |
| Table 1. Fixed Information Set Versus Dynamic Retrieval | Section III | Explains why retrieval requires methodological treatment. |
| Table 2. Five Dimensions of Retrieval-Environment Validity | Section III | Central framework table. |
| Table 3. Retrieval Typology | Section IV | Operationalizes retrieval designs. |
| Table 4. Construct-to-Retrieval Mapping | Section IV | Prevents overclaiming and supports research design choices. |
| Table 5. Claim Correctness Layers | Section V | Core evaluation protocol. |
| Table 7. Tiered Reporting Standard | Section VI | Practical AJPT methodology contribution. |
| Figure 2. Demonstration Pipeline | Section VII | Shows reproducibility chain. |
| Table 8. Selected Claim-Level Demonstration Examples | Section VII | Shows how the framework changes inference. |

Move the following to appendix or online supplement unless the final manuscript has space and expert-coded reliability:

- Table 6. Retrieval Failure Mode Taxonomy
- Table 9A. Main Preliminary Coding Summary
- Table 9B. Bounded Extension Preliminary Coding Summary
- Table 10. Reporting Items Mapped to Validity Dimensions
- Appendix Tables A1-A6

## Appendix And Supplement Placement

| Appendix Item | Contents |
|---|---|
| Appendix A | Source corpus and filing manifest |
| Appendix B | Text retrieval store and chunking specification |
| Appendix C | XBRL fact and relation store specification |
| Appendix D | Prompt and retrieval context package |
| Appendix E | LLM run configuration and output archive |
| Appendix F | Claim-level coding package |
| Appendix G | Source spot checks and reviewer validation |
| Appendix H | Bounded extension evidence |
| Appendix I | Sensitivity guidance and unperformed checks |

## Style Compliance Checklist

| Requirement | Current Status | Next Action |
|---|---|---|
| AJPT target and call category identified | Complete | Use cover-letter wording from `plan/55_target_journal_and_submission_alignment.md`. |
| Abstract under 150 words | Complete in this package | Replace v2 abstract in next full draft. |
| AI disclosure after abstract | Drafted | Authors must finalize exact wording. |
| First-level roman numeral headings | Complete in this package | Apply to next full draft. |
| Nontechnical introduction | Improved | Keep first page focused on research-design problem. |
| 55-page discipline | Planned | Move long implementation and coding tables to appendix/supplement. |
| Two-layer demonstration integrated | Complete conceptually | Use main deep cases in text; extension in appendix. |
| Aggregate coding not framed as performance | Complete | Keep Table 9A/9B appendix-only unless expert coding is added. |
| XBRL boundary | Complete | Continue using management-reported structured data language. |
| Data availability statement | Needed | Draft after finalizing repository/supplement policy. |
| Title page | Needed | Prepare separately at submission stage. |
| Conflict of interest statement | Needed | Prepare separately at submission stage. |
| Alt-text for figures | Needed | Add during final table/figure polishing. |

## Reviewer-Style Assessment

After this alignment, the paper is much closer to the AJPT Methodological Papers call. The contribution now reads as a method for improving inference in LLM-based auditing research, not as an LLM audit tool. The abstract, introduction, and demonstration framing all foreground retrieval as research design. The remaining risks are manageable:

1. The final manuscript must keep the demonstration descriptive.
2. The appendix must be clean enough that reviewers can inspect the evidence trail without getting lost.
3. Expert coding is still needed if the paper wants to make stronger audit-validity claims.
4. The final cover letter must explicitly state that the manuscript is for the AJPT Methodological Papers call.

## Bottom Line

The manuscript should proceed to a full v3 draft using this package as the style and structure control document. V3 should integrate the bounded extension, replace the abstract, add the AI disclosure, convert headings to AJPT format, and move aggregate preliminary results to the appendix.
