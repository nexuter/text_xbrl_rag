# Phase 8 Appendix Materials Package

## Purpose

This file defines the appendix and supplemental-materials package for the manuscript. The appendix should let an AJPT reviewer evaluate whether the demonstration is transparent, reproducible, and correctly bounded as a methodological illustration rather than a performance benchmark.

The organizing principle is retrieval-environment validity. Each appendix item should help readers inspect one or more of the five validity dimensions: selection, representation, stability, traceability, and separability.

## Post-Extension Status Note

This appendix package has been updated after the bounded six-filer extension. The appendix should now document both layers of the demonstration:

1. Main deep cases: NKE, SBUX, and TGT; 24 outputs; 94 preliminary coded claims.
2. Bounded extension: WMT, HD, CAT, PFE, MSFT, and CROX; 18 outputs; 88 preliminary coded claims.

The combined active demonstration archive therefore contains 42 outputs and 182 preliminary coded claims. These counts should be reported as transparency evidence, not as model-performance results.

## Finalization Status Note

This Phase 8 appendix package is now superseded for submission-planning purposes by `plan/65_final_appendix_package.md`.

The final package preserves the substance of this file but reorganizes it into a reviewer-facing evidence trail:

1. source corpus;
2. text and XBRL retrieval stores;
3. prompt and retrieval contexts;
4. LLM output archive;
5. claim-level coding;
6. source spot checks;
7. bounded extension evidence;
8. sensitivity limits and boundary conditions.

Use this file as the historical appendix materials package and `plan/65_final_appendix_package.md` as the current appendix structure for v3 manuscript preparation.

## Recommended Appendix Structure

| Appendix | Title | Primary Reviewer Question | Primary Validity Dimension |
|---|---|---|---|
| Appendix A | Source Corpus and Filing Manifest | What source documents created the information environment? | Selection, traceability |
| Appendix B | Text Retrieval Store and Chunking Specification | How was narrative evidence represented and selected? | Selection, representation, stability |
| Appendix C | XBRL Fact and Relation Store Specification | How were reported accounting relationships represented and retrieved? | Representation, traceability |
| Appendix D | Prompt and Retrieval Context Package | What exactly did the LLM see? | Traceability, separability |
| Appendix E | LLM Run Configuration and Output Archive | Were model settings and outputs reproducible? | Stability, separability |
| Appendix F | Claim-Level Coding Package | How were claims evaluated across correctness layers? | Traceability, representation |
| Appendix G | Source Spot Checks and Reviewer Validation | Do selected examples map back to real filing evidence? | Traceability, representation |
| Appendix H | Bounded Extension Evidence | Does the protocol remain applicable across varied reporting environments? | Selection, traceability, separability |
| Appendix I | Sensitivity Guidance and Unperformed Checks | What robustness checks would be required for stronger empirical claims? | Stability, separability |

## Appendix A. Source Corpus and Filing Manifest

### Contents

| Artifact | Path |
|---|---|
| Download manifest | `data/processed/download_manifest.md` |
| Download manifest, machine-readable | `data/processed/download_manifest.json` |
| Extraction summary | `data/processed/extraction_summary.md` |
| Extraction summary, machine-readable | `data/processed/extraction_summary.json` |
| Raw SEC filing data | `data/raw_sec/` |

### Minimum Disclosures

1. Filer name, ticker, CIK, form type, fiscal year, accession number, and source URL.
2. Download date and script used for download.
3. Raw filing files retained for source verification.
4. Any exclusions, failed downloads, or parsing exceptions.

### Manuscript Use

The main manuscript should state that the demonstration uses actual SEC filing text and Inline XBRL data. The three familiar filers provide deep main-text examples, and the bounded extension adds six additional filers for a maximum-variation methodological check. Appendix A provides the source trail so readers can verify that the retrieval environments were built from filed documents rather than manually assembled examples.

## Appendix B. Text Retrieval Store and Chunking Specification

### Contents

| Artifact | Path |
|---|---|
| Combined text chunks | `data/processed/text_chunks/text_chunks.csv` |
| Nike text chunks | `data/processed/text_chunks/nke_text_chunks.json` |
| Starbucks text chunks | `data/processed/text_chunks/sbux_text_chunks.json` |
| Target text chunks | `data/processed/text_chunks/tgt_text_chunks.json` |
| Walmart text chunks | `data/processed/text_chunks/wmt_text_chunks.json` |
| Home Depot text chunks | `data/processed/text_chunks/hd_text_chunks.json` |
| Caterpillar text chunks | `data/processed/text_chunks/cat_text_chunks.json` |
| Pfizer text chunks | `data/processed/text_chunks/pfe_text_chunks.json` |
| Microsoft text chunks | `data/processed/text_chunks/msft_text_chunks.json` |
| Crocs text chunks | `data/processed/text_chunks/crox_text_chunks.json` |
| Text retrieval specification | `plan/31_phase7_text_retrieval_specification.md` |

### Minimum Disclosures

1. Chunk identifier.
2. Filer and source filing.
3. Source section or inferred topic label.
4. Chunk text.
5. Chunking rule and approximate chunk size.
6. Overlap rule, if any.
7. Retrieval method used in the demonstration.
8. Whether embedding/vector retrieval was implemented.

### Current Demonstration Status

The demonstration uses keyword-ranked contextual retrieval over extracted 10-K chunks. It does not implement production vector RAG. The manuscript and appendix should state this clearly. Vector database details should be presented as reporting guidance for future Tier 2 or Tier 3 studies, not as a completed feature of the current demonstration.

### Reviewer Value

Appendix B addresses the concern that "text retrieval" is underspecified. It makes the narrative information environment inspectable at the chunk level.

## Appendix C. XBRL Fact and Relation Store Specification

### Contents

| Artifact | Path |
|---|---|
| Combined XBRL facts | `data/processed/xbrl_facts/xbrl_facts.csv` |
| Nike XBRL facts | `data/processed/xbrl_facts/nke_xbrl_facts.json` |
| Starbucks XBRL facts | `data/processed/xbrl_facts/sbux_xbrl_facts.json` |
| Target XBRL facts | `data/processed/xbrl_facts/tgt_xbrl_facts.json` |
| Walmart XBRL facts | `data/processed/xbrl_facts/wmt_xbrl_facts.json` |
| Home Depot XBRL facts | `data/processed/xbrl_facts/hd_xbrl_facts.json` |
| Caterpillar XBRL facts | `data/processed/xbrl_facts/cat_xbrl_facts.json` |
| Pfizer XBRL facts | `data/processed/xbrl_facts/pfe_xbrl_facts.json` |
| Microsoft XBRL facts | `data/processed/xbrl_facts/msft_xbrl_facts.json` |
| Crocs XBRL facts | `data/processed/xbrl_facts/crox_xbrl_facts.json` |
| Combined XBRL paths | `data/processed/xbrl_paths/xbrl_paths.csv` |
| Nike XBRL paths | `data/processed/xbrl_paths/nke_xbrl_paths.json` |
| Starbucks XBRL paths | `data/processed/xbrl_paths/sbux_xbrl_paths.json` |
| Target XBRL paths | `data/processed/xbrl_paths/tgt_xbrl_paths.json` |
| Walmart XBRL paths | `data/processed/xbrl_paths/wmt_xbrl_paths.json` |
| Home Depot XBRL paths | `data/processed/xbrl_paths/hd_xbrl_paths.json` |
| Caterpillar XBRL paths | `data/processed/xbrl_paths/cat_xbrl_paths.json` |
| Pfizer XBRL paths | `data/processed/xbrl_paths/pfe_xbrl_paths.json` |
| Microsoft XBRL paths | `data/processed/xbrl_paths/msft_xbrl_paths.json` |
| Crocs XBRL paths | `data/processed/xbrl_paths/crox_xbrl_paths.json` |
| XBRL relation/ontology specification | `plan/32_phase7_xbrl_relation_ontology_specification.md` |

### Minimum Disclosures

1. Fact identifier.
2. Concept QName and label.
3. Reported value, unit, decimals, and sign handling.
4. Context identifier and period.
5. Filing and filer metadata.
6. Relation source, relation target, arcrole, linkrole, and path depth where relation paths are used.
7. Extension-concept handling.
8. Taxonomy/linkbase source and taxonomy year/version.

### Current Demonstration Status

The demonstration uses table-based XBRL relational retrieval over extracted facts and relation paths. It does not claim a full RDF/OWL triple-store or graph database implementation. RDF/OWL should be described as a portability and compatibility mapping for future implementations.

### Reviewer Value

Appendix C addresses whether XBRL relational retrieval is auditable as a data structure. It also prevents overclaiming by distinguishing reported XBRL relations from audit assertions.

## Appendix D. Prompt and Retrieval Context Package

### Contents

| Artifact | Path |
|---|---|
| Retrieval context manifest | `data/processed/retrieval_contexts/context_manifest.csv` |
| Retrieval context manifest, machine-readable | `data/processed/retrieval_contexts/retrieval_context_manifest.json` |
| Retrieval context summary | `data/processed/retrieval_contexts/retrieval_context_summary.md` |
| Prompt files | `data/processed/prompts/` |
| Retrieval context files | `data/processed/retrieval_contexts/` |
| Retrieval log | `data/processed/retrieval_logs/retrieval_log.csv` |
| Hybrid context and workflow specification | `plan/33_phase7_hybrid_context_and_llm_workflow.md` |

### Current Counts

| Item | Count |
|---|---:|
| Main prompt/context conditions | 24 |
| Bounded-extension prompt/context conditions | 18 |
| Total prompt/context conditions | 42 |
| Retrieval log rows | 313 |

### Minimum Disclosures

1. Full prompt text for each run.
2. Full inserted retrieval context.
3. Retrieval condition, filer, construct, and run identifier.
4. Source IDs for retrieved text chunks and XBRL facts/paths.
5. Context ordering and formatting rule.
6. Top-k or selection rule.
7. Token or approximate context budget, if measured.

### Reviewer Value

Appendix D is the most important traceability appendix. It answers the question: "What exactly did the LLM see before producing the output?"

## Appendix E. LLM Run Configuration and Output Archive

### Contents

| Artifact | Path |
|---|---|
| Full-run summary | `data/processed/llm_outputs/gemma4_31b_full/run_summary.md` |
| Full-run manifest | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` |
| Raw JSON outputs | `data/processed/llm_outputs/gemma4_31b_full/raw_json/` |
| Text outputs | `data/processed/llm_outputs/gemma4_31b_full/text/` |
| Extension run summary | `data/processed/llm_outputs/gemma4_31b_extension/run_summary.md` |
| Extension run manifest | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` |
| Extension raw JSON outputs | `data/processed/llm_outputs/gemma4_31b_extension/raw_json/` |
| Extension text outputs | `data/processed/llm_outputs/gemma4_31b_extension/text/` |
| LLM output harness memo | `plan/20_phase6_llm_output_harness.md` |
| Model-selection memo | `plan/21_phase6_model_selection_memo.md` |
| gemma4:31b validation memo | `plan/23_phase6_gemma4_31b_model_fit_validation.md` |
| Full-run log memo | `plan/24_phase6_gemma4_31b_full_run_log.md` |
| Extension LLM and coding log | `plan/51_bounded_robustness_extension_llm_and_coding_log.md` |
| LLM results validation log | `plan/52_llm_results_validation_log.md` |

### Current Run Summary

| Field | Value |
|---|---|
| Provider | Ollama |
| Model | `gemma4:31b` |
| Temperature | 0.0 |
| Main completed outputs | 24 |
| Extension completed outputs | 18 |
| Total completed outputs | 42 |
| Errors | 0 |
| Access time UTC | 2026-05-29T02:55:38.587209+00:00 |

### Minimum Disclosures

1. Model name and version string available from the local provider.
2. Provider and local serving environment.
3. Temperature and other generation parameters.
4. Prompt and context file used for each run.
5. Raw output archive.
6. Run date/time.
7. Error handling and excluded outputs.

### Reviewer Value

Appendix E supports stability and separability. It documents that output differences are compared under a controlled model and parameter setting.

## Appendix F. Claim-Level Coding Package

### Contents

| Artifact | Path |
|---|---|
| Full claim-level coding table | `data/processed/coding/claim_level_coding_gemma4_31b.csv` |
| Coding summary | `data/processed/coding/claim_coding_summary.md` |
| Coding summary by condition | `data/processed/coding/coding_summary_by_condition.csv` |
| Inference shift table | `data/processed/coding/inference_shift_table_prelim.csv` |
| Failure mode examples | `data/processed/coding/failure_mode_examples_prelim.csv` |
| Extension claim-level coding table | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` |
| Extension coding summary | `data/processed/coding/claim_coding_summary_gemma4_31b_extension.md` |
| Extension summary by condition | `data/processed/coding/coding_summary_by_condition_gemma4_31b_extension.csv` |
| Extension inference shift table | `data/processed/coding/inference_shift_table_prelim_gemma4_31b_extension.csv` |
| Extension failure mode examples | `data/processed/coding/failure_mode_examples_prelim_gemma4_31b_extension.csv` |
| Correctness protocol memo | `plan/16_phase5_correctness_protocol.md` |
| Claim coding and inference shift log | `plan/25_phase6_claim_coding_and_inference_shift_log.md` |

### Current Counts

| Item | Count |
|---|---:|
| Main segmented claims | 94 |
| Bounded-extension segmented claims | 88 |
| Total preliminary coded claims | 182 |
| Retrieval conditions | 4 |
| Main filers | 3 |
| Bounded-extension filers | 6 |
| Constructs | 2 |

### Minimum Disclosures

1. Claim identifier.
2. Source output/run identifier.
3. Claim type.
4. Retrieved source IDs cited or used.
5. Text-supported score and rationale.
6. Graph-valid score and rationale.
7. Audit-valid score and rationale.
8. Integrated-correctness score and rationale.
9. Failure mode labels, if applicable.
10. Coder qualifications, independence, and reliability procedures.

### Current Limitation

The current coding is preliminary author coding. The manuscript should not treat audit-valid or integrated correctness scores as final expert evidence. Before submission, selected claims should be reviewed by at least one audit-domain expert, and ideally coded by two independent coders with reconciliation.

### Reviewer Value

Appendix F prevents the demonstration from looking anecdotal. It shows that the five selected examples in the manuscript are drawn from a full claim-level coding trail.

## Appendix G. Source Spot Checks and Reviewer Validation

### Contents

| Artifact | Path |
|---|---|
| Selected manuscript examples | `data/processed/coding/selected_manuscript_examples_prelim.csv` |
| Manuscript selected claim table | `data/processed/coding/manuscript_selected_claim_table.md` |
| Source spot-check table | `data/processed/coding/selected_source_spot_check.csv` |
| Reviewer validation memo | `plan/26_phase6_reviewer_validation_of_coded_examples.md` |
| Source graph spot-check memo | `plan/28_phase6_source_graph_spot_check_memo.md` |
| Demonstration reviewer stress test | `plan/29_phase6_demonstration_reviewer_stress_test.md` |

### Minimum Disclosures

1. Selected example ID and claim ID.
2. Text chunk IDs and XBRL fact IDs used in the example.
3. Raw filing location or processed-source location.
4. Spot-check status.
5. Reviewer concern addressed.

### Reviewer Value

Appendix G is the credibility bridge between the manuscript examples and the raw SEC/XBRL evidence. It is especially important because reviewers may distrust LLM examples that are not source-verified.

## Appendix H. Bounded Extension Evidence

### Contents

| Artifact | Path |
|---|---|
| Demonstration scope and generalizability assessment | `plan/48_demonstration_scope_generalizability_assessment.md` |
| Bounded-extension filer selection memo | `plan/49_bounded_robustness_extension_filer_selection.md` |
| Bounded-extension data and diagnostics log | `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md` |
| Bounded-extension LLM and coding log | `plan/51_bounded_robustness_extension_llm_and_coding_log.md` |
| LLM results validation log | `plan/52_llm_results_validation_log.md` |
| Manuscript integration package | `plan/53_bounded_extension_manuscript_integration_package.md` |

### Reviewer Value

Appendix H reduces the concern that the demonstration is tailored to only three familiar filers. It should be framed as a maximum-variation methodological extension rather than as a representative empirical sample.

## Appendix I. Sensitivity Guidance and Unperformed Checks

### Contents

| Artifact | Path |
|---|---|
| Reporting checklist and sensitivity table | `plan/34_phase7_reporting_checklist_and_sensitivity_table.md` |
| Phase 7 reviewer stress test | `plan/35_phase7_reviewer_stress_test.md` |
| Tables and figures package | `plan/41_phase8_tables_and_figures_package.md` |

### Sensitivity Checks Proposed But Not Fully Executed

| Check | Relevance | Current Status |
|---|---|---|
| Chunk size variation | Selection and representation validity | Proposed, not executed |
| Chunk overlap variation | Representation validity | Proposed, not executed |
| Embedding model variation | Selection and stability | Not applicable to current keyword prototype |
| Top-k variation | Selection validity | Proposed, not executed |
| XBRL traversal depth variation | Selection and representation validity | Proposed, not executed |
| XBRL relation type filters | Representation validity | Proposed, not executed |
| Token budget equalization | Separability | Partially addressed conceptually, not executed as formal sensitivity |
| Model variation | Separability and generalizability | Model-selection reviewed; full comparison not executed |
| Prompt variation | Stability | Proposed, not executed |
| Expert coder reliability | Audit-valid correctness | Needed before final submission claims |

### Manuscript Boundary Statement

The demonstration is a Tier 1 methodological demonstration. It illustrates how retrieval design changes the evidence basis of LLM claims. It does not establish general LLM audit performance, vector-RAG performance, GraphRAG performance, or superiority of hybrid retrieval.

## What Belongs in the Main Manuscript Versus Appendix

| Item | Main Manuscript | Appendix/Supplement |
|---|---|---|
| Framework figure | Yes | Optional |
| Five validity dimensions table | Yes | Optional |
| Retrieval typology | Yes | Optional |
| Construct-to-retrieval mapping | Yes | Optional |
| Correctness layer table | Yes | Optional |
| Selected five claim examples | Yes | Yes, with source detail |
| Preliminary coding summary | Optional | Yes |
| Full 94-claim main coding table | No | Yes |
| Full 88-claim bounded-extension coding table | No | Yes |
| Full prompt files | No | Yes |
| Full retrieval context files | No | Yes |
| Raw LLM outputs | No | Yes |
| Raw filing files | No | Yes, via repository package |
| Source spot checks | Briefly summarized | Yes |
| Sensitivity guidance | Brief table or summary | Yes |

## Appendix Readiness Assessment

The appendix package is strong enough to support a methodology manuscript if it is framed correctly.

Strengths:

1. The package preserves source-to-prompt-to-output-to-claim traceability.
2. It distinguishes actual implemented prototype artifacts from future implementation guidance.
3. It gives reviewers access to the full 94-claim coding trail rather than only selected examples.
4. It explicitly labels preliminary coding and unperformed sensitivity checks.
5. It ties appendices to retrieval-environment validity dimensions.
6. It now distinguishes main deep cases from the bounded extension.

Remaining gaps before submission:

1. Expert review is needed for audit-valid and integrated correctness scores.
2. A cleaner appendix index should be generated once the manuscript's final table numbering is known.
3. If the paper claims embedding-based RAG implications, at least one vector retrieval sensitivity run should be added or the language should remain clearly scoped to text retrieval guidance.
4. If the paper emphasizes ontology/RDF contribution, an RDF/OWL export example should be generated or the language should remain at the specification level.

## Recommended Next Step

The next step is a full AJPT reviewer stress test of manuscript draft v1 plus the appendix package. The reviewer test should ask whether the full package is now strong enough to avoid the two largest risks: sounding like a technical systems paper, and overclaiming what the preliminary demonstration proves.
