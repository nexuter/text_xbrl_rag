# Phase 8 Tables and Figures Package

## Purpose

This file converts the Phase 8 manuscript architecture and demonstration evidence into manuscript-ready tables and figure specifications. The goal is to make the paper's methodological contribution visible to AJPT reviewers: the paper is not simply proposing another retrieval pipeline, but a validity framework for studying how retrieval design shapes LLM-based audit research inferences.

The tables below should be used in the main manuscript where they advance the core argument. Longer implementation and reporting tables can be moved to an online appendix.

## Post-Extension Status Note

This table package has been updated after the bounded six-filer extension documented in `plan/49_bounded_robustness_extension_filer_selection.md` through `plan/53_bounded_extension_manuscript_integration_package.md`.

The current manuscript package should use a two-layer demonstration design:

1. Main-text deep demonstration: three familiar filers, 24 outputs, and 94 preliminary coded claims.
2. Appendix bounded extension: six additional filers, 18 outputs, and 88 preliminary coded claims.

The extension should not be presented as a representative sample or a model-performance benchmark. It should be presented as a maximum-variation methodological check showing that the retrieval-environment validity protocol can be applied across varied reporting environments.

## Finalization Status Note

This Phase 8 tables and figures package is now superseded for submission-planning purposes by `plan/66_final_tables_and_figures_check.md`.

The final placement decision is:

1. keep Figure 1, Tables 1-5, the tiered reporting standard, Figure 2, and selected claim examples in the main text;
2. move the failure-mode taxonomy, preliminary coding summaries, detailed reporting map, data-structure tables, and bounded-extension diagnostics to the appendix;
3. treat all aggregate coding summaries as preliminary author-coded transparency artifacts, not performance evidence.

Use this file as the historical table package and `plan/66_final_tables_and_figures_check.md` as the current table and figure control document for v3 manuscript preparation.

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

Caption: Retrieval-environment validity concerns the correspondence between the audit construct a study intends to examine and the information environment actually supplied to the LLM through retrieval. The framework treats retrieval as part of research design, not merely as a technical preprocessing step.

Reviewer value: This figure makes the paper's methodological object clear. It separates the paper from studies that evaluate model output without specifying whether the model had access to an appropriate audit information environment.

## Figure 2. Demonstration Pipeline

```text
SEC 10-K filings and Inline XBRL
        |
        v
Two-layer case design:
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
Inference-shift analysis
```

Caption: Demonstration pipeline used to illustrate how different retrieval designs create different information environments for the same filer-construct task. The main cases support deep claim-level illustration, while the bounded extension checks whether the protocol remains applicable across varied reporting environments. The demonstration is intentionally framed as a methodological illustration rather than a final benchmark of LLM audit performance.

Reviewer value: This figure addresses reproducibility and transparency concerns by showing the complete chain from SEC source documents to claim-level coding.

## Table 1. Fixed Information Set Versus Dynamic Retrieval

| Feature | Fixed Information Set | Dynamic Retrieval Environment |
|---|---|---|
| Research object | LLM response to a known prompt package | LLM response conditional on a retrieval mechanism |
| Information boundary | Defined before inference | Constructed at query time |
| Replication target | Prompt, model, parameters, and supplied documents | Prompt, model, parameters, corpus, retrieval algorithm, retrieval settings, and returned evidence |
| Main validity threat | Incomplete or biased document package | Retrieval-created construct drift |
| Audit research implication | Researchers can inspect the supplied evidence directly | Researchers must validate whether retrieval supplied evidence appropriate to the audit construct |

Manuscript use: Place early in the framework section to justify why retrieval requires its own methodological treatment.

## Table 2. Five Dimensions of Retrieval-Environment Validity

| Dimension | Audit/Method Anchor | Core Question | Observable Evidence | Failure Mode |
|---|---|---|---|---|
| Selection | Construct validity | Did retrieval select evidence relevant to the intended audit construct? | Retrieved chunks, facts, and paths map to the construct definition | Omission of relevant evidence |
| Representation | Measurement reliability | Did retrieval preserve the meaning of the source evidence? | Text chunks retain context; XBRL facts retain concept, context, unit, period, and sign | Distortion or mis-specified representation |
| Stability | Reproducibility | Would equivalent runs retrieve materially similar evidence? | Fixed corpus, retrieval parameters, seeds, model/version metadata, and returned evidence logs | Retrieval instability |
| Traceability | Audit documentation | Can each LLM claim be traced to source evidence? | Claim-to-source links, fact IDs, text chunk IDs, and source accession metadata | Attribution failure |
| Separability | Internal validity | Can retrieval effects be separated from model effects? | Controlled model, prompt, and temperature across retrieval conditions | Model-retrieval confounding |

Manuscript use: This is a core contribution table. It should remain in the main text.

## Table 3. Retrieval Typology for LLM-Based Audit Research

| Retrieval Design | Primary Source | Unit of Retrieval | Retrieval Operator | Best-Suited Audit Use | Main Risk |
|---|---|---|---|---|---|
| LLM-only | Model pretraining | None | None | Baseline diagnostic or prior-knowledge comparison | Untraceable inference |
| Text retrieval | Narrative filings, audit documents, workpapers, standards | Text chunk | Semantic, keyword, or hybrid text search | Disclosure interpretation, policy descriptions, narrative risk cues | Missing numeric and relational structure |
| XBRL relational retrieval | XBRL facts, contexts, units, concepts, calculation/presentation/definition relations | Fact, concept, context, relation path | Concept lookup, relation traversal, ontology query | Reported accounting relationships, numeric consistency, source traceability | Overreading reported structure as audit evidence |
| Hybrid retrieval | Text plus XBRL relation data | Chunk plus fact/path bundle | Coordinated text and relation retrieval | Narrative-numeric integration and structured corroboration of reported disclosures | Integration failure and inconsistent evidence weighting |

Manuscript use: Place in the retrieval design section to define the design space.

## Table 4. Construct-to-Retrieval Mapping

| Intended Construct | Most Appropriate Retrieval Design | Why | What Not To Claim |
|---|---|---|---|
| Understanding narrative disclosure | Text retrieval | The construct depends on language, disclosure framing, and explanation | That the retrieved text verifies underlying account balances |
| Preserving reported accounting relationships | XBRL relational retrieval | The construct depends on concepts, contexts, units, periods, and taxonomy relations | That XBRL alone establishes audit truth |
| Connecting narrative risk language to reported amounts | Hybrid retrieval | The construct requires both disclosure meaning and structured accounting facts | That hybrid retrieval automatically improves correctness |
| Identifying assertion-level risk cues | Hybrid retrieval with explicit audit coding | Audit assertions require interpretation beyond filed relations | That retrieval substitutes for auditor judgment |
| Detecting fraud, misstatement, or internal control failure | Retrieval plus external evidence and expert validation | These constructs require evidence outside management-reported filings | That XBRL relation paths are fraud evidence |

Manuscript use: This table prevents overclaiming and directly answers reviewer concerns about construct fit.

## Table 5. Claim Correctness Layers

| Layer | Applies To | Question Answered | Example Evidence | Reviewer Concern Addressed |
|---|---|---|---|---|
| Text-supported correctness | Claims citing narrative text | Is the claim supported by the retrieved text? | Text chunk ID and quoted/paraphrased source passage | RAG output may cite irrelevant text |
| Graph-valid correctness | Claims citing XBRL facts or relation paths | Is the claim consistent with the retrieved XBRL data and relation structure? | Fact ID, concept, context, period, unit, value, relation path | XBRL-derived claims may misuse structured data |
| Audit-valid correctness | Risk or assertion claims | Is the inference appropriate for the audit construct? | Explicit inferential bridge, limitation, and reviewer coding | Structured support is not the same as audit evidence |
| Integrated correctness | Hybrid text-XBRL claims | Does the claim integrate narrative and structured evidence without contradiction? | Matched text chunk plus XBRL fact/path bundle | Hybrid retrieval may juxtapose evidence without synthesis |

Manuscript use: Use in the methodological protocol section. This table is central to the paper's contribution because it makes evaluation conditional on claim type.

## Table 6. Retrieval Failure Mode Taxonomy

| Failure Mode | Definition | Likely Retrieval Source | Detection Method | Design Response |
|---|---|---|---|---|
| Omission | Relevant evidence exists but is not retrieved | Text, XBRL, hybrid | Compare returned evidence to construct-specific source inventory | Adjust retrieval scope, top-k, query expansion, or relation traversal |
| Distortion | Retrieved evidence loses its source meaning | Text, XBRL | Inspect chunk boundaries, concept/context/unit/period metadata, and sign handling | Preserve source metadata and chunk context |
| Retrieval instability | Similar queries return materially different evidence | Text, hybrid | Repeat retrieval under fixed corpus/settings and compare evidence sets | Report parameters and perform sensitivity checks |
| Attribution failure | Output claim cannot be traced to retrieved evidence | All designs | Claim-to-source coding | Require source-linked claims and reject unsupported claims |
| Model-retrieval confounding | Output differences cannot be attributed to retrieval design | All designs | Hold model, prompt, temperature, and task fixed across conditions | Controlled factorial design |
| Relation hallucination | LLM invents or misstates XBRL relations | XBRL, hybrid | Validate relation paths against extracted XBRL data | Provide explicit fact/path IDs and verify paths before prompting |
| Source overreach | LLM treats management-reported XBRL as audit evidence | XBRL, hybrid | Audit-validity coding of risk/assertion claims | Require limitations and distinguish reported facts from audit conclusions |
| Integration failure | Text and XBRL evidence are listed but not jointly reasoned | Hybrid | Integrated correctness coding | Prompt for explicit bridge and code integrated claims separately |

Manuscript use: Can appear in the main text if space permits; otherwise move to an appendix.

## Table 7. Tiered Reporting Standard

| Study Type | Minimum Reporting | Required Validity Evidence | Claims the Study Should Avoid |
|---|---|---|---|
| Tier 1: Methodological demonstration | Corpus, extraction process, retrieval conditions, prompt template, model/version, and claim-coding protocol | Evidence that retrieval conditions create distinguishable information environments | General claims about LLM audit performance |
| Tier 2: Empirical LLM audit study using RAG | Tier 1 items plus construct definition, retrieval tuning, sensitivity tests, and human/expert coding | Retrieval-environment validity for the specific construct and outcome | Treating retrieval as an implementation detail |
| Tier 3: Retrieval-system or GraphRAG evaluation | Tier 2 items plus benchmark tasks, gold labels or expert labels, indexing details, and robustness checks | Comparative retrieval and output evidence across systems | Declaring a retrieval architecture superior without construct-specific evaluation |

Manuscript use: This table aligns the paper with AJPT's methodological orientation by giving researchers a practical reporting standard.

## Table 8. Selected Claim-Level Demonstration Examples

| Example ID | Filer | Construct | Condition | Claim ID | Claim type | Claim excerpt | Sources | Text support | Graph validity | Audit validity | Integrated correctness |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|
| E01 | SBUX | inventory | hybrid | C058 | risk_assertion | The combination of persistent supply chain disruptions, commodity volatility, and the identified $56.6 million inventory valuation reserve indicates a meaningful risk that inventory valuation could be misstated if reserve assumptions fail to reflect current cost and spoilage conditions. | T-SBUX-INVENTORY-015, XBRL F-SBUX-0034 | 1 | 1 | 1 | 1 |
| E02 | NKE | revenue | hybrid | C013 | risk_assertion | Refund liability increased from $799 million to $1.277 billion, which may indicate heightened revenue recognition risk around estimates of returns and variable consideration. | XBRL F-NKE-0253, F-NKE-0252 | 0 | 0.5 | 1 | 0.5 |
| E03 | NKE | revenue | hybrid | C014 | risk_assertion | The digital commerce platform is described as business-critical, and system failure or cyber disruption could affect transaction processing and revenue completeness. | T-NKE-REVENUE-021 | 1 | NA | 1 | 0.5 |
| E04 | NKE | revenue | llm_only | C016 | insufficient_context | Based on the provided information, I cannot identify Nike's key revenue-related risk indicators for FY2025. | None | NA | NA | 1 | NA |
| E05 | TGT | inventory | hybrid | C090 | risk_assertion | Target reported net inventory of $12.740 billion as of February 1, 2025, making inventory a quantitatively significant account for audit attention. | XBRL F-TGT-0007 | 0 | 1 | 1 | 0.5 |

Notes: Scores are preliminary author coding and are used to illustrate the proposed correctness protocol. They should not be presented as final expert validation. Example E02 is intentionally retained as a cautionary example because graph validity depends on whether the relation between two fact values is treated as a valid comparison rather than a taxonomy relation.

Manuscript use: Use as the main demonstration table. It shows what text retrieval, XBRL relational retrieval, hybrid retrieval, and LLM-only baselines make visible or invisible.

## Table 9. Preliminary Coding Summary by Retrieval Condition

Recommended placement: appendix. In the main text, summarize only the design implication: retrieval-condition labels are insufficient because individual claims can rely on text only, XBRL only, both, or neither. If aggregate coding is shown, split the table into Table 9A for the main deep cases and Table 9B for the bounded extension.

### Table 9A. Main Deep Cases

| Condition | Construct | Claims | Text Support Mean | Graph Validity Mean | Audit Validity Mean | Integrated Correctness Mean | Interpretation |
|---|---|---:|---:|---:|---:|---:|---|
| Hybrid | Inventory | 15 | 0.63 | 0.88 | 1.00 | 0.60 | Hybrid retrieval produced integrative claims, but integration quality varied. |
| Hybrid | Revenue | 15 | 0.47 | 0.88 | 1.00 | 0.50 | Hybrid outputs often used structured facts while only partially connecting them to narrative evidence. |
| LLM-only | Inventory | 3 | NA | NA | 1.00 | NA | The model appropriately acknowledged insufficient context in the controlled prompts. |
| LLM-only | Revenue | 3 | NA | NA | 1.00 | NA | The baseline is useful as a traceability diagnostic, not as an audit-performance benchmark. |
| Text | Inventory | 13 | 0.69 | NA | 1.00 | NA | Text retrieval supported narrative risk claims but did not preserve structured numeric relations. |
| Text | Revenue | 15 | 0.70 | NA | 1.00 | NA | Text retrieval captured disclosure context while leaving reported accounting relations implicit. |
| XBRL | Inventory | 15 | NA | 0.70 | 1.00 | NA | XBRL retrieval supported structured reported facts but required caution for audit inferences. |
| XBRL | Revenue | 15 | NA | 0.73 | 1.00 | NA | XBRL retrieval improved traceability of reported values but did not provide independent audit evidence. |

Notes: These results are preliminary author-coded demonstration evidence. The audit-validity means are high because prompts required risk/assertion claims to include inferential bridges and limitations; therefore, these values should not be interpreted as evidence that the model achieved high audit judgment performance. The table should be used to illustrate how the correctness layers produce different diagnostics by retrieval condition.

Manuscript use: Include only if the manuscript clearly labels the table as methodological demonstration evidence. Otherwise, move to an appendix and keep Table 8 in the main text.

### Table 9B. Bounded Extension

| Condition | Construct | Claims | Text Support Mean | Graph Validity Mean | Audit Validity Mean | Integrated Correctness Mean | Interpretation |
|---|---|---:|---:|---:|---:|---:|---|
| Hybrid | Inventory | 25 | 0.58 | 0.86 | 1.00 | 0.58 | Hybrid retrieval remained inspectable across additional retail, industrial, pharma, and consumer-product settings, but integrated correctness still varied by claim. |
| Hybrid | Revenue | 5 | 0.50 | 1.00 | 1.00 | 0.50 | The MSFT revenue boundary case shows that hybrid prompts can still yield evidence-use separation rather than full integration. |
| Text | Inventory | 24 | 0.71 | NA | 1.00 | NA | Text retrieval supported narrative inventory-policy and risk-cue claims while leaving structured reported relationships implicit. |
| Text | Revenue | 5 | 0.70 | NA | 1.00 | NA | Text retrieval captured revenue-disclosure context but did not provide relation-level verification. |
| XBRL | Inventory | 25 | NA | 0.72 | 1.00 | NA | XBRL retrieval supported source-traceable reported facts and relations, but still required audit-validity caution. |
| XBRL | Revenue | 4 | NA | 0.75 | 1.00 | NA | The software/cloud revenue case demonstrates both structured-fact usefulness and relation-path scarcity as an informative boundary condition. |

Notes: The bounded-extension coding is preliminary author coding. The extension adds breadth to the methodological demonstration but does not estimate population-level model performance, retrieval accuracy, or failure-mode prevalence.

## Table 10. Reporting Items Mapped to Validity Dimensions

| Reporting Item | Selection | Representation | Stability | Traceability | Separability |
|---|---:|---:|---:|---:|---:|
| Corpus scope and filing accession metadata | 1 | 1 | 1 | 1 | 0 |
| Text chunking rule, chunk size, and overlap | 1 | 1 | 1 | 1 | 0 |
| Embedding model or keyword retrieval method | 1 | 0 | 1 | 0 | 1 |
| Vector index or retrieval backend configuration | 1 | 0 | 1 | 0 | 1 |
| XBRL fact schema: concept, context, unit, period, value, decimals | 1 | 1 | 1 | 1 | 0 |
| XBRL relation schema: source, target, arcrole, linkrole, depth/path | 1 | 1 | 1 | 1 | 0 |
| Retrieval query templates and top-k settings | 1 | 0 | 1 | 0 | 1 |
| Returned evidence logs for each prompt | 1 | 1 | 1 | 1 | 1 |
| Model, version, temperature, context length, and prompt template | 0 | 0 | 1 | 0 | 1 |
| Claim-level coding protocol and coder qualifications | 0 | 1 | 1 | 1 | 1 |

Manuscript use: This table is best suited for an appendix or online supplement because it is practical and detailed.

## Appendix Table A1. Text Retrieval Data Structure

| Field | Description | Reproducibility Role |
|---|---|---|
| document_id | Filing, standard, audit document, or other source identifier | Defines source boundary |
| accession_or_source_id | SEC accession number or source-system identifier | Enables source lookup |
| chunk_id | Stable chunk identifier | Enables claim-level traceability |
| section_label | Filing section or document heading | Helps interpret chunk context |
| chunk_text | Retrieved text content | Provides evidence inspected by the LLM |
| token_count | Approximate token length | Supports prompt-budget analysis |
| chunk_size | Target chunk length | Supports retrieval sensitivity analysis |
| overlap | Number of overlapping tokens/characters | Supports context preservation analysis |
| embedding_model | Embedding model used, if applicable | Supports replication |
| retrieval_score | Similarity, keyword, or hybrid score | Supports selection diagnostics |
| rank | Returned rank for query | Supports top-k analysis |

## Appendix Table A2. XBRL Relational Retrieval Data Structure

| Field | Description | Reproducibility Role |
|---|---|---|
| fact_id | Stable identifier assigned to extracted fact | Enables claim-to-fact traceability |
| concept_qname | XBRL concept, including namespace | Preserves accounting meaning |
| label | Human-readable concept label | Supports interpretability |
| value | Reported fact value | Supports numeric verification |
| unit | Monetary, shares, pure, or other unit | Prevents unit errors |
| period_start | Beginning of period, if duration context | Preserves context |
| period_end | End date or instant date | Preserves context |
| entity | Reporting entity identifier | Preserves filer boundary |
| decimals | XBRL decimals attribute | Supports precision interpretation |
| balance | Debit/credit attribute where available | Supports sign interpretation |
| context_id | Original XBRL context identifier | Supports source verification |
| relation_source | Source concept in relation edge | Supports graph traversal |
| relation_target | Target concept in relation edge | Supports graph traversal |
| arcrole | Calculation, presentation, definition, or other relation type | Preserves relation semantics |
| linkrole | Extended link role | Preserves statement/disclosure context |
| path_depth | Number of relation edges traversed | Supports retrieval scope analysis |

## Appendix Table A3. Reproducibility Package Checklist

| Artifact | Required Contents |
|---|---|
| Source corpus manifest | Filers, form types, fiscal years, accession numbers, download date, source URLs |
| Extraction scripts | Text extraction, XBRL extraction, relation extraction, and preprocessing code |
| Retrieval logs | Query, returned chunks/facts/paths, ranks, scores, and timestamps |
| Prompt files | Full system/user prompts and inserted retrieval context |
| Model run metadata | Model name, version, provider, temperature, context window, and run date |
| Output archive | Raw LLM responses and parsed claim files |
| Coding files | Coding rubric, claim-level coding, coder notes, and adjudication rules |
| Sensitivity checks | Chunk-size, overlap, top-k, traversal-depth, and model-comparison results where applicable |

## Appendix Table A4. Bounded Extension Filer Selection

Use the filer-selection table from `plan/53_bounded_extension_manuscript_integration_package.md`. This appendix table should document the six extension filers, their industries, construct focus, and selection rationale.

## Appendix Table A5. Bounded Extension Retrieval Diagnostics

Use the retrieval-diagnostic table from `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md` or `plan/53_bounded_extension_manuscript_integration_package.md`. This appendix table should show extracted text chunks, XBRL facts, and relation paths for all main and extension filers.

## Appendix Table A6. Bounded Extension Selected Examples

Use the selected examples from `plan/53_bounded_extension_manuscript_integration_package.md`. This appendix table should demonstrate how the protocol handles extension cases, including MSFT's relation-path scarcity boundary case.

## Recommended Main-Text Placement

| Manuscript Section | Recommended Visual |
|---|---|
| Introduction | Figure 1 |
| Framework | Table 1 and Table 2 |
| Retrieval Designs | Table 3 and Table 4 |
| Correctness Protocol | Table 5 and Table 6 |
| Reporting Guidance | Table 7 |
| Demonstration | Figure 2 and Table 8 |
| Appendix | Table 9A, Table 9B, Table 10, and Appendix Tables A1-A6 |

## Reviewer-Facing Design Choices

1. The tables avoid claiming that XBRL relational retrieval is inherently superior to text retrieval. The more defensible claim is that each retrieval design creates a different information environment.
2. XBRL is explicitly characterized as management-reported structured data, not independent audit evidence.
3. The demonstration tables are labeled as preliminary methodological evidence rather than final performance benchmarks.
4. The reporting tables make implementation transparency concrete, which directly supports the AJPT methodological call.
5. The framework distinguishes graph-valid, text-supported, audit-valid, and integrated correctness so that reviewers do not have to infer the evaluation logic.
6. The bounded extension is clearly separated from the main deep cases so reviewers do not read the demonstration as a representative empirical sample.

## Next Manuscript Task

The next step is to convert these tables into a polished manuscript draft with explicit table callouts, tighter transitions, and a shorter demonstration narrative. The demonstration should emphasize what the tables reveal about retrieval-created information environments rather than presenting the results as model performance.
