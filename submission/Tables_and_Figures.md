# V3 Main-Text Tables And Figures Packet

## Purpose

This file provides the final main-text tables and figure specifications for `plan/69_submission_ready_manuscript_v3.md`.

The packet is designed to resolve the v3 reviewer stress-test concern that the manuscript still used table and figure placeholders. These tables and figures are the operational core of the paper's methodological contribution. Longer implementation tables, preliminary aggregate coding summaries, and bounded-extension diagnostics remain in the appendix or online supplement.

## Placement Summary

| Final Label | Title | Manuscript Section |
|---|---|---|
| Figure 1 | Retrieval-Environment Validity Framework | Section III |
| Figure 1A | Compact Example of Claim Correctness Layers | Section I |
| Table 1 | Fixed Information Set Versus Dynamic Retrieval | Section III |
| Table 2 | Retrieval-Environment Validity Versus Adjacent Validity Concepts | Section III |
| Table 3 | Reviewer Decision Rules for Retrieval-Environment Validity Problems | Section III |
| Table 4 | Five Dimensions of Retrieval-Environment Validity | Section III |
| Table 5 | Retrieval Typology for LLM-Based Audit Research | Section IV |
| Table 6 | Construct-to-Retrieval Mapping | Section IV |
| Table 7 | Claim Correctness Layers | Section V |
| Table 8 | Evidence Tiers for Retrieval-Based Audit Research | Section VI |
| Figure 2 | Methodological Demonstration Pipeline | Section VII |
| Table 9 | Selected Claim-Level Demonstration Examples | Section VII |

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

## Figure 1A. Compact Example of Claim Correctness Layers

```text
Retrieved public filing text:
  "Inventory reserves increased during the year."

Retrieved XBRL fact/path:
  InventoryValuationReserves = 233 million USD
  Period = FY2025; Unit = USD; relation path preserved

LLM claim:
  "The reserve increase is relevant to inventory valuation risk."

Correctness-layer reading:
  Text-supported?        Yes, if the text states the reserve change.
  Graph-valid?           Yes for the reported amount, period, unit, and path.
  Assertion-relevant?    Yes, as a valuation-risk cue from public reporting data.
  Integrated?            Yes only if the claim uses both the text and XBRL fact together.
  Audit conclusion?      No. Reserve adequacy or fair valuation requires additional audit evidence.
```

Caption:

Compact example showing why the paper separates text-supported correctness, graph-valid correctness, audit-boundary diagnostics, integrated correctness, and audit evidence sufficiency. The same retrieved public filing and XBRL materials can support a bounded assertion-relevant diagnostic while remaining insufficient for an audit conclusion.

Alt text:

Layered example using an inventory reserve disclosure and an XBRL reserve fact. The figure shows which claim layers are supported and emphasizes that source support and XBRL graph validity do not establish audit evidence sufficiency.

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

## Table 2. Retrieval-Environment Validity Versus Adjacent Validity Concepts

| Adjacent Concept | What It Already Covers | What It Misses In Dynamic Retrieval | Retrieval-Specific Failure | Consequence For LLM Audit Inference |
|---|---|---|---|---|
| Construct validity | Whether the study operationalizes the intended audit construct | Whether runtime retrieval actually supplies construct-relevant evidence | Construct-relevant source evidence exists but is not retrieved | Output differences may be misattributed to model reasoning rather than retrieval-created construct drift |
| Measurement validity | Whether variables measure the intended phenomenon | Whether retrieved evidence units preserve meaning after chunking, filtering, or rendering | Text chunks, XBRL contexts, periods, units, or relation paths are distorted | Claim-level variables may code model output against a misrepresented evidence environment |
| Information-set or case-material design | Whether the materials supplied to a participant or model are appropriate for the intended task | Whether the runtime retriever changed the effective materials from the corpus or case packet the researcher intended | The corpus contains construct-relevant evidence, but the query-time retriever supplies a different subset or ordering | A study may appear to use a well-designed information set while the model actually observes a different evidence environment |
| Internal validity | Whether causal inferences are separated from confounds | Whether retrieval-conditioned information differences are separable from model, prompt, token-budget, ordering, and salience effects | Retrieval condition differs in source type and information volume | A study may claim a retrieval-design effect when it observes context-budget or formatting differences |
| Audit evidence sufficiency | Whether evidence is enough to support an audit conclusion | Whether management-reported filing data are being overread as audit evidence | XBRL facts or disclosures are treated as audit truth | Graph-valid or text-supported claims may be incorrectly interpreted as audit-boundary or audit-judgment conclusions |
| Audit documentation | Whether evidence and conclusions are documented | Whether each LLM claim can be traced to the retrieved information actually shown to the model | Output claims lack source IDs or cite unavailable evidence | Reviewers cannot distinguish source-supported claims from unsupported model assertions |
| Textual-analysis preprocessing validation | Whether text is cleaned, tokenized, and measured appropriately | Whether query-time retrieval selects the right text units for the construct | Relevant chunks are omitted or severed from context | Text-based RAG output may appear construct-aligned while relying on generic or incomplete disclosure text |
| XBRL data-quality research | Whether structured reporting data are usable, comparable, complete, and affected by extensions, contexts, or tagging choices | Whether the selected XBRL facts and paths instantiate the audit construct for a specific LLM task | Mechanically available facts or extension concepts are retrieved without construct-relevance validation | XBRL retrieval may be graph-valid but still irrelevant or incomplete for the audit assertion being studied |
| RAG system evaluation | Whether a retrieval system performs well on retrieval or QA metrics such as context relevance, answer relevance, or answer faithfulness | Whether retrieved materials support the audit-research inference rather than generic answer quality | High retrieval relevance or answer faithfulness does not map to audit construct relevance | A technically strong RAG system may still create invalid audit-research inferences |
| Evidence traceability / answer faithfulness | Whether generated statements are grounded in retrieved context | Whether grounded statements stay within public-filing and XBRL audit-boundary limits | The answer is faithful to retrieved management-reported materials but overstates audit implications | A faithful RAG answer may still be invalid as an audit-research inference |
| Reproducibility | Whether another researcher can rerun or inspect the study | Whether the dynamic evidence environment can be reconstructed at the claim level | Corpus, index, ranking rule, or returned evidence is not preserved | Prompt and model replication is insufficient because the model's information set is unknown |

Note:

Retrieval-environment validity is not a replacement for these adjacent concepts. It identifies the retrieval-specific mechanism through which they can fail when the model's information set is dynamically constructed at runtime.

## Table 3. Reviewer Decision Rules for Retrieval-Environment Validity Problems

| Retrieval Problem Type | When It Matters | Reviewer Decision | Example In LLM-Based Audit Research |
|---|---|---|---|
| Inference-invalidating | The retrieved environment omits or misrepresents construct-critical material needed for the stated audit construct | Require redesign or reject the affected inference | A revenue-recognition risk task retrieves only generic risk-factor language and omits contract-liability disclosures, revenue policy text, or related XBRL facts |
| Design-confounding | Retrieval conditions differ in context volume, source ordering, salience, prompt wording, or model configuration in a way that prevents attribution | Require sensitivity analysis or narrow causal interpretation | A hybrid condition receives substantially more context than a text-only condition, so output differences cannot be attributed to source type alone |
| Measurement-threatening | Claim-level coding, source-use classification, or correctness layers cannot be applied reliably or independently | Require clearer coding rules, coder validation, or narrower measurement claims | Coders cannot consistently distinguish graph-valid reported-fact support from audit-boundary overreach |
| Disclosure-limiting | Retrieval details are incomplete, but the study makes only descriptive, illustrative, or protocol claims | Require disclosure, appendix support, or replication-package clarification | A methodological demonstration omits some retrieval tuning details but does not claim model-performance effects |
| Acceptable boundary | The limitation is disclosed and does not affect the specific claim being made | Accept with boundary statement | Public filing and XBRL data are used to illustrate source traceability, while the paper explicitly avoids audit-evidence sufficiency claims |

Note:

The table operationalizes retrieval-environment validity as a reviewer-facing decision rule. Not every retrieval limitation invalidates a study. The consequence depends on the claim being made and whether the retrieval problem changes the construct, confounds attribution, weakens measurement, limits disclosure, or remains within a clearly stated boundary.

## Table 4. Five Dimensions of Retrieval-Environment Validity

| Dimension | Audit/Method Anchor | Core Question | Observable Evidence | Failure Mode |
|---|---|---|---|---|
| Selection | Construct validity | Did retrieval select evidence relevant to the intended audit construct? | Retrieved chunks, facts, and paths map to the construct definition | Omission of relevant evidence |
| Representation | Measurement reliability | Did retrieval preserve the meaning of the source evidence? | Text chunks retain context; XBRL facts retain concept, context, unit, period, and sign | Distortion or mis-specified representation |
| Stability | Reproducibility | Would equivalent runs retrieve materially similar evidence? | Fixed corpus, retrieval parameters, model/version metadata, and returned evidence logs | Retrieval instability |
| Traceability | Audit documentation | Can each LLM claim be traced to source evidence? | Claim-to-source links, fact IDs, text chunk IDs, and source accession metadata | Attribution failure |
| Separability | Internal validity | Can retrieval-conditioned information differences be separated from model effects? | Controlled model, prompt, temperature, task, and diagnostic baseline across retrieval conditions | Model-retrieval confounding |

Note:

The dimensions adapt established audit and research-design concerns to the retrieval setting. They are diagnostic criteria for evaluating whether the retrieved information environment supports the intended audit-research inference.

## Table 5. Retrieval Typology for LLM-Based Audit Research

| Retrieval Design | Primary Source | Unit of Retrieval | Retrieval Operator | Best-Suited Audit-Research Use | Main Risk |
|---|---|---|---|---|---|
| LLM-only | Model pretraining | None | None | Baseline diagnostic or prior-knowledge comparison | Untraceable inference |
| Text retrieval | Narrative filings, audit documents, workpapers, standards | Text chunk | Semantic, keyword, or hybrid text search | Disclosure interpretation, policy descriptions, narrative risk cues | Missing numeric and relational structure |
| XBRL relational retrieval | XBRL facts, contexts, units, concepts, calculation/presentation/definition relations | Fact, concept, context, relation path | Concept lookup, relation traversal, ontology query | Reported accounting relationships, numeric consistency, source traceability | Overreading reported structure as audit evidence |
| Hybrid retrieval | Text plus XBRL relation data | Chunk plus fact/path bundle | Coordinated text and relation retrieval | Narrative-numeric integration and structured corroboration of reported disclosures | Integration failure and inconsistent evidence weighting |

Note:

The table distinguishes retrieval designs by source, unit, operator, construct fit, and validity risk. Hybrid retrieval is treated as construct-specific, not universally superior.

## Table 6. Construct-to-Retrieval Mapping

| Intended Construct | Most Appropriate Retrieval Design | Why | What Not To Claim |
|---|---|---|---|
| Understanding narrative disclosure | Text retrieval | The construct depends on language, disclosure framing, and explanation | That the retrieved text verifies underlying account balances |
| Preserving reported accounting relationships | XBRL relational retrieval | The construct depends on concepts, contexts, units, periods, taxonomy relations, and construct-family coverage diagnostics | That XBRL alone establishes audit truth |
| Connecting narrative risk language to reported amounts | Hybrid retrieval | The construct requires both disclosure meaning and structured accounting facts | That hybrid retrieval automatically improves correctness |
| Identifying assertion-level risk cues | Hybrid retrieval with explicit audit coding | Audit assertions require interpretation beyond filed relations | That retrieval substitutes for auditor judgment |
| Revenue recognition risk cues in the demonstration public-reporting setting | Text plus XBRL retrieval with claim-level audit-boundary coding | Revenue risk-cue analysis requires policy language, performance-obligation context, contract/refund liability amounts, periods, assertion mapping, and ex ante XBRL concept-family coverage checks | That the retrieved public filing/XBRL materials prove misstatement, GAAP noncompliance, fraud, or audit evidence sufficiency |
| Inventory valuation assertion relevance in the demonstration public-reporting setting | Text plus XBRL retrieval with claim-level audit-boundary coding | Inventory assertion-relevance analysis requires accounting policy language, reserve/write-down disclosures, reported balances, periods, relation paths, and ex ante XBRL concept-family coverage checks | That the retrieved public filing/XBRL materials prove physical existence, reserve adequacy, net realizable value, management bias, or audit evidence sufficiency |
| Detecting fraud, misstatement, or internal control failure | Retrieval plus external evidence and expert validation | These constructs require evidence outside management-reported filings | That XBRL relation paths are fraud evidence |

Note:

This table links retrieval design to construct definition and explicitly marks claims that the retrieval design does not support.

## Table 7. Claim Correctness Layers

| Layer | Applies To | Question Answered | Example Evidence | Reviewer Concern Addressed |
|---|---|---|---|---|
| Text-supported correctness | Claims using narrative text | Is the claim supported by the retrieved text? | Text chunk ID and source passage or paraphrase | RAG output may cite irrelevant or insufficient text |
| Graph-valid correctness | Claims using XBRL facts or relation paths | Is the claim consistent with the retrieved XBRL data and relation structure? | Fact ID, concept, context, period, unit, value, and relation path | XBRL-derived claims may misuse structured data |
| Audit-boundary diagnostic | Risk or assertion claims | Does the inference stay within what retrieved public filing and XBRL materials can support? | Inferential bridge, stated limitation, and expert or reviewer coding | Structured support is not the same as audit evidence sufficiency |
| Integrated correctness | Hybrid text-XBRL claims | Does the claim integrate narrative and structured evidence without contradiction? | Matched text chunk plus XBRL fact/path bundle | Hybrid retrieval may juxtapose evidence without synthesis |

Note:

Audit-boundary diagnostics are not objective audit ground truth. The current demonstration distinguishes public-filing support, XBRL graph/reporting support, assertion relevance, and preliminary audit-boundary diagnostics from audit evidence sufficiency. Strong audit-judgment claims require audit-domain expert judgment, coder independence, and reliability procedures appropriate to the study's claims.

## Table 8. Evidence Tiers for Retrieval-Based Audit Research

| Study Type | Intended Use | Core Artifacts | Validity Evidence Needed | Claims The Study Should Avoid |
|---|---|---|---|---|
| Tier 1: Methodological demonstration | Shows how retrieval environments can be specified, preserved, and linked to claim-level source use | Corpus, extraction process, retrieval conditions, prompt template, model/version, and claim-coding protocol | Evidence that retrieval conditions create distinguishable information environments | General claims about LLM audit performance |
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
Source-use divergence assessment
```

Caption:

Demonstration pipeline used to illustrate how different retrieval designs create different information environments for the same filer-construct task. The full-scale nine-filer package combines three deep cases for claim-level illustration with six bounded-extension cases that apply the same two-construct, four-condition grid across varied reporting environments. The demonstration is a methodological illustration of source-to-context-to-output-to-claim traceability. It is not designed to evaluate model performance, retrieval-method superiority, or population-level failure-mode prevalence.

Alt text:

Flow diagram showing SEC 10-K and Inline XBRL sources feeding a two-layer case design, text and XBRL extraction, retrieval conditions, controlled LLM prompts, claim-level coding, and source-use divergence assessment.

## Table 9. Selected Claim-Level Demonstration Examples

| Example | Claim ID | Filer | Construct | Condition | Claim Summary | Text Source | XBRL Source | Text Support | Graph Validity | Audit Boundary Diagnostic | Integrated Diagnostic | Inference Consequence |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| E01 | C058 | Starbucks | Inventory | Hybrid | Inventory reserves were $56.6 million as of September 28, 2025. | T-SBUX-INVENTORY-015 | F-SBUX-0034 | 1 | 1 | 1 | 1 | Hybrid retrieval supports direct narrative-XBRL corroboration for a bounded factual claim. |
| E02 | C013 | Nike | Revenue | Hybrid | Refund liability increased from $799 million to $1.277 billion and may be a revenue valuation risk cue. | None | F-NKE-0253; F-NKE-0252 | 0 | 0.5 | 1 prelim. | 0 | The claim is graph-grounded but effectively XBRL-only despite the hybrid condition. |
| E03 | C014 | Nike | Revenue | Hybrid | Digital commerce platform failure risk may map to revenue completeness and occurrence. | T-NKE-REVENUE-021 | None | 0.5 | NA | 1 prelim. | 0 | The claim is text-supported but does not use XBRL despite the hybrid condition. |
| E04 | C016 | Nike | Revenue | LLM-only | Context is insufficient to identify filing-specific revenue risk cues. | None | None | NA | NA | 1 prelim. | NA | The no-context baseline supports traceability diagnosis rather than performance comparison. |
| E05 | C090 | Target | Inventory | Hybrid | Net inventory was $12.740 billion as of February 1, 2025. | None | F-TGT-0007 | 0 | 1 | 1 prelim. | 0 | The claim is graph-grounded but does not integrate the available Target inventory narrative context. |

Note:

Examples are selected from the full 281-claim coding archive and are included to illustrate correctness layers and source-use types. Scores are preliminary author-coded diagnostics used to illustrate the claim-level correctness protocol. They are not final expert audit-boundary evidence and should not be interpreted as model-performance measures. Audit-boundary diagnostics require audit-domain expert review before being used for stronger audit-judgment claims; source-use type and integrated correctness are separately evaluated for protocol reliability in the independent coding sample.

## Appendix Location Note

The main-text tables are limited to the conceptual argument, claim-evidence calibration, and selected demonstration examples. Detailed implementation and validation materials remain in the online supplement, including failure-mode coding, preliminary coding summaries, independent-coder evidence, bounded-extension diagnostics, sensitivity diagnostics, text/XBRL data structures, and the reproducibility checklist.

## Reviewer-Facing Boundary Statement

The tables and figures support the paper's methodological contribution. They do not rank retrieval methods, estimate model performance, validate audit judgment quality, or imply that XBRL is audit evidence.
