# V3 Main-Text Tables And Figures Packet

## Purpose

This file provides the final main-text tables and figure specifications for `plan/69_submission_ready_manuscript_v3.md`.

The packet is designed to resolve the v3 reviewer stress-test concern that the manuscript still used table and figure placeholders. These tables and figures are the operational core of the paper's methodological contribution. Longer implementation tables, preliminary aggregate coding summaries, and bounded-extension diagnostics remain in the appendix or online supplement.

## Placement Summary

| Final Label | Title | Manuscript Section |
|---|---|---|
| Figure 1 | Retrieval-Environment Validity Framework | Section III |
| Table 1 | Fixed Information Set Versus Dynamic Retrieval | Section III |
| Table 2 | Five Dimensions of Retrieval-Environment Validity | Section III |
| Table 3 | Retrieval Typology for LLM-Based Audit Research | Section IV |
| Table 4 | Construct-to-Retrieval Mapping | Section IV |
| Table 5 | Claim Correctness Layers | Section V |
| Table 6 | Tiered Reporting Standard | Section VI |
| Figure 2 | Methodological Demonstration Pipeline | Section VII |
| Table 7 | Selected Claim-Level Demonstration Examples | Section VII |

## Figure 1. Retrieval-Environment Validity Framework

```text
Intended audit construct
        |
        v
Retrieval design choice
        |
        v
Retrieval-created information environment
        |
        v
LLM-generated claims
        |
        v
Research inference
        |
        v
Retrieval-environment validity assessment
```

Caption:

Retrieval-environment validity concerns the correspondence between the audit construct a study intends to examine and the information environment actually supplied to the LLM through retrieval. The framework treats retrieval as part of research design, not as a technical preprocessing step.

Alt text:

Flow diagram showing that the intended audit construct drives retrieval design, which creates an information environment for the LLM; the LLM generates claims, researchers draw inferences, and retrieval-environment validity assesses whether the chain supports those inferences.

## Table 1. Fixed Information Set Versus Dynamic Retrieval

| Feature | Fixed Information Set | Dynamic Retrieval Environment |
|---|---|---|
| Research object | LLM response to a known prompt package | LLM response conditional on a retrieval mechanism |
| Information boundary | Defined before inference | Constructed at query time |
| Replication target | Prompt, model, parameters, and supplied documents | Prompt, model, parameters, corpus, retrieval algorithm, retrieval settings, and returned evidence |
| Main validity threat | Incomplete or biased document package | Retrieval-created construct drift |
| Audit research implication | Researchers can inspect the supplied evidence directly | Researchers must validate whether retrieval supplied evidence appropriate to the audit construct |

Note:

This table motivates why retrieval requires methodological treatment. In dynamic retrieval designs, the prompt and model do not fully define the information environment observed by the LLM.

## Table 2. Five Dimensions of Retrieval-Environment Validity

| Dimension | Audit/Method Anchor | Core Question | Observable Evidence | Failure Mode |
|---|---|---|---|---|
| Selection | Construct validity | Did retrieval select evidence relevant to the intended audit construct? | Retrieved chunks, facts, and paths map to the construct definition | Omission of relevant evidence |
| Representation | Measurement reliability | Did retrieval preserve the meaning of the source evidence? | Text chunks retain context; XBRL facts retain concept, context, unit, period, and sign | Distortion or mis-specified representation |
| Stability | Reproducibility | Would equivalent runs retrieve materially similar evidence? | Fixed corpus, retrieval parameters, model/version metadata, and returned evidence logs | Retrieval instability |
| Traceability | Audit documentation | Can each LLM claim be traced to source evidence? | Claim-to-source links, fact IDs, text chunk IDs, and source accession metadata | Attribution failure |
| Separability | Internal validity | Can retrieval effects be separated from model effects? | Controlled model, prompt, temperature, task, and diagnostic baseline across retrieval conditions | Model-retrieval confounding |

Note:

The dimensions adapt established audit and research-design concerns to the retrieval setting. They are diagnostic criteria for evaluating whether the retrieved information environment supports the intended audit-research inference.

## Table 3. Retrieval Typology for LLM-Based Audit Research

| Retrieval Design | Primary Source | Unit of Retrieval | Retrieval Operator | Best-Suited Audit-Research Use | Main Risk |
|---|---|---|---|---|---|
| LLM-only | Model pretraining | None | None | Baseline diagnostic or prior-knowledge comparison | Untraceable inference |
| Text retrieval | Narrative filings, audit documents, workpapers, standards | Text chunk | Semantic, keyword, or hybrid text search | Disclosure interpretation, policy descriptions, narrative risk cues | Missing numeric and relational structure |
| XBRL relational retrieval | XBRL facts, contexts, units, concepts, calculation/presentation/definition relations | Fact, concept, context, relation path | Concept lookup, relation traversal, ontology query | Reported accounting relationships, numeric consistency, source traceability | Overreading reported structure as audit evidence |
| Hybrid retrieval | Text plus XBRL relation data | Chunk plus fact/path bundle | Coordinated text and relation retrieval | Narrative-numeric integration and structured corroboration of reported disclosures | Integration failure and inconsistent evidence weighting |

Note:

The table distinguishes retrieval designs by source, unit, operator, construct fit, and validity risk. Hybrid retrieval is treated as construct-specific, not universally superior.

## Table 4. Construct-to-Retrieval Mapping

| Intended Construct | Most Appropriate Retrieval Design | Why | What Not To Claim |
|---|---|---|---|
| Understanding narrative disclosure | Text retrieval | The construct depends on language, disclosure framing, and explanation | That the retrieved text verifies underlying account balances |
| Preserving reported accounting relationships | XBRL relational retrieval | The construct depends on concepts, contexts, units, periods, and taxonomy relations | That XBRL alone establishes audit truth |
| Connecting narrative risk language to reported amounts | Hybrid retrieval | The construct requires both disclosure meaning and structured accounting facts | That hybrid retrieval automatically improves correctness |
| Identifying assertion-level risk cues | Hybrid retrieval with explicit audit coding | Audit assertions require interpretation beyond filed relations | That retrieval substitutes for auditor judgment |
| Detecting fraud, misstatement, or internal control failure | Retrieval plus external evidence and expert validation | These constructs require evidence outside management-reported filings | That XBRL relation paths are fraud evidence |

Note:

This table links retrieval design to construct definition and explicitly marks claims that the retrieval design does not support.

## Table 5. Claim Correctness Layers

| Layer | Applies To | Question Answered | Example Evidence | Reviewer Concern Addressed |
|---|---|---|---|---|
| Text-supported correctness | Claims using narrative text | Is the claim supported by the retrieved text? | Text chunk ID and source passage or paraphrase | RAG output may cite irrelevant or insufficient text |
| Graph-valid correctness | Claims using XBRL facts or relation paths | Is the claim consistent with the retrieved XBRL data and relation structure? | Fact ID, concept, context, period, unit, value, and relation path | XBRL-derived claims may misuse structured data |
| Audit-valid correctness | Risk or assertion claims | Is the inference appropriate for the audit construct? | Inferential bridge, stated limitation, and expert or reviewer coding | Structured support is not the same as audit evidence |
| Integrated correctness | Hybrid text-XBRL claims | Does the claim integrate narrative and structured evidence without contradiction? | Matched text chunk plus XBRL fact/path bundle | Hybrid retrieval may juxtapose evidence without synthesis |

Note:

Audit-valid correctness is not objective ground truth. Strong audit-validity claims require audit-domain expert judgment, coder independence, and reliability procedures appropriate to the study's claims.

## Table 6. Tiered Reporting Standard

| Study Type | Intended Use | Minimum Reporting | Required Validity Evidence | Claims The Study Should Avoid |
|---|---|---|---|---|
| Tier 1: Methodological demonstration | Shows how retrieval design changes valid inference | Corpus, extraction process, retrieval conditions, prompt template, model/version, and claim-coding protocol | Evidence that retrieval conditions create distinguishable information environments | General claims about LLM audit performance |
| Tier 2: Empirical LLM audit study using RAG | Tests LLM outputs under retrieval-augmented conditions | Tier 1 items plus construct definition, retrieval tuning, sensitivity tests, and human/expert coding | Retrieval-environment validity for the specific construct and outcome | Treating retrieval as an implementation detail |
| Tier 3: Retrieval-system or GraphRAG evaluation | Evaluates retrieval architecture or system performance | Tier 2 items plus benchmark tasks, gold labels or expert labels, indexing details, and robustness checks | Comparative retrieval and output evidence across systems | Declaring a retrieval architecture superior without construct-specific evaluation |

Note:

The current paper's demonstration is Tier 1. Tier 2 and Tier 3 requirements are provided as guidance for studies making stronger empirical or system-performance claims.

## Figure 2. Methodological Demonstration Pipeline

```text
SEC 10-K filings and Inline XBRL
        |
        v
Two-layer case design
  - Deep main cases: NKE, SBUX, TGT
  - Bounded extension: WMT, HD, CAT, PFE, MSFT, CROX
        |
        v
Text and XBRL extraction
        |
        +----------------------------+
        |                            |
        v                            v
Text chunks                  XBRL facts and relation paths
        |                            |
        +-------------+--------------+
                      |
                      v
Retrieval conditions: LLM-only, text, XBRL, hybrid
                      |
                      v
Controlled prompts using gemma4:31b
                      |
                      v
Claim-level coding
                      |
                      v
Evidence-use divergence assessment
```

Caption:

Demonstration pipeline used to illustrate how different retrieval designs create different information environments for the same filer-construct task. The main cases support deep claim-level illustration, while the bounded extension checks whether the protocol remains applicable across varied reporting environments. The demonstration is a methodological illustration of source-to-context-to-output-to-claim traceability. It is not designed to evaluate model performance, retrieval-method superiority, or population-level failure-mode prevalence.

Alt text:

Flow diagram showing SEC 10-K and Inline XBRL sources feeding a two-layer case design, text and XBRL extraction, retrieval conditions, controlled LLM prompts, claim-level coding, and evidence-use divergence assessment.

## Table 7. Selected Claim-Level Demonstration Examples

| Example | Claim ID | Filer | Construct | Condition | Claim Summary | Text Source | XBRL Source | Text Support | Graph Validity | Audit Diagnostic | Integrated Diagnostic | Inference Consequence |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| E01 | C058 | Starbucks | Inventory | Hybrid | Inventory reserves were $56.6 million as of September 28, 2025. | T-SBUX-INVENTORY-015 | F-SBUX-0034 | 1 | 1 | 1 | 1 | Hybrid retrieval supports direct narrative-XBRL corroboration for a bounded factual claim. |
| E02 | C013 | Nike | Revenue | Hybrid | Refund liability increased from $799 million to $1.277 billion and may be a revenue valuation risk cue. | None | F-NKE-0253; F-NKE-0252 | 0 | 0.5 | 1 prelim. | 0.5 | The claim is graph-grounded but effectively XBRL-only despite the hybrid condition. |
| E03 | C014 | Nike | Revenue | Hybrid | Digital commerce platform failure risk may map to revenue completeness and occurrence. | T-NKE-REVENUE-021 | None | 0.5 | NA | 1 prelim. | 0.5 | The claim is text-supported but does not use XBRL despite the hybrid condition. |
| E04 | C016 | Nike | Revenue | LLM-only | Context is insufficient to identify filing-specific revenue risk cues. | None | None | NA | NA | 1 prelim. | NA | The no-context baseline supports traceability diagnosis rather than performance comparison. |
| E05 | C090 | Target | Inventory | Hybrid | Net inventory was $12.740 billion as of February 1, 2025. | None | F-TGT-0007 | 0 | 1 | 1 prelim. | 0.5 | The claim is graph-grounded but does not integrate the available Target inventory narrative context. |

Note:

Examples are selected from the full 182-claim coding archive and are included to illustrate correctness layers and evidence-use types. Scores are preliminary author-coded diagnostics used to illustrate the claim-level correctness protocol. They are not final expert audit-validity evidence and should not be interpreted as model-performance measures. Audit-valid and integrated diagnostics require audit-domain expert review before being used for stronger audit-judgment claims.

## Submission Use

This packet should accompany `plan/69_submission_ready_manuscript_v3.md` as the final main-text tables and figures file. It resolves the main placeholder concern identified in `plan/70_v3_reviewer_stress_test.md`.

The following materials remain appendix-only:

1. Retrieval Failure Mode Taxonomy;
2. Main Deep-Case Preliminary Coding Summary;
3. Bounded-Extension Preliminary Coding Summary;
4. Reporting Items Mapped to Validity Dimensions;
5. Text Retrieval Data Structure;
6. XBRL Relational Retrieval Data Structure;
7. Reproducibility Package Checklist;
8. Bounded-Extension Filer Selection;
9. Bounded-Extension Retrieval Diagnostics;
10. Bounded-Extension Selected Examples.

## Reviewer-Facing Boundary Statement

The tables and figures support the paper's methodological contribution. They do not rank retrieval methods, estimate model performance, validate audit judgment quality, or imply that XBRL is audit evidence.
