# Authoritative Files For Manuscript Evidence

## Purpose

This file identifies the replication-package artifacts that correspond to the manuscript's reported demonstration counts, tables, and claims. These are the authoritative files for reviewer inspection.

The package also contains older pilot, smoke, and dry-run artifacts for provenance. Those files are not manuscript evidence and are listed separately in `DEPRECATED_OR_PILOT_ARTIFACTS.md`.

## Manuscript Evidence Counts

| Evidence Item | Authoritative Source | Count |
|---|---|---:|
| Active filers | `config/filer_manifest.json` | 9 |
| Retrieval contexts | `data/processed/retrieval_contexts/context_manifest.csv` | 72 |
| Retrieval log rows | `data/processed/retrieval_logs/retrieval_log.csv` | 464 |
| Main deep-case LLM outputs | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` | 24 |
| Bounded-extension LLM outputs | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | 48 |
| Total LLM outputs | Main plus extension manifests | 72 |
| Main deep-case coded claims | `data/processed/coding/claim_level_coding_gemma4_31b.csv` | 94 |
| Bounded-extension coded claims | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | 187 |
| Total coded claims | Main plus extension coding files | 281 |
| Independent coding validation sample | `data/processed/coding/independent_coding_sample.csv` | 120 |
| Hybrid-condition mechanism claims | `data/processed/coding/hybrid_integration_mechanisms.csv` | 89 |
| XBRL construct-coverage cells | `data/processed/xbrl_coverage/construct_coverage_by_filer.csv` | 18 |
| Retrieval perturbation rows | `data/processed/sensitivity/retrieval_perturbation_diagnostics.csv` | 90 |
| Bounded sensitivity decision-matrix cells | `data/processed/sensitivity/bounded_sensitivity_decision_matrix_by_cell.csv` | 18 |
| Checksum manifest rows | `data/processed/checksums/checksum_manifest.csv` | 418 |

## Authoritative Pipeline Inputs

| Artifact | Path | Use |
|---|---|---|
| Filer manifest | `config/filer_manifest.json` | Defines the nine-filer source universe and sample roles |
| Text chunks | `data/processed/text_chunks/text_chunks.csv` | Narrative retrieval source table |
| XBRL facts | `data/processed/xbrl_facts/xbrl_facts.csv` | Structured fact retrieval source table |
| XBRL relation paths | `data/processed/xbrl_paths/xbrl_paths.csv` | Structured relation retrieval source table |
| Retrieval context manifest | `data/processed/retrieval_contexts/context_manifest.csv` | Maps filer, construct, condition, context, and prompt files |
| Retrieval log | `data/processed/retrieval_logs/retrieval_log.csv` | Records retrieved text chunks, XBRL facts, and relation paths |
| Context-volume diagnostics | `data/processed/retrieval_contexts/context_volume_diagnostics.csv` | Reports context length, prompt length, and source counts for each filer/construct/condition |
| Context-volume summary | `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv` | Reports condition-level context-volume diagnostics for separability transparency |
| Retrieval perturbation diagnostics | `data/processed/sensitivity/retrieval_perturbation_diagnostics.csv` | Reports deterministic source-set perturbations by filer/construct/variant |
| Retrieval perturbation summary | `data/processed/sensitivity/retrieval_perturbation_summary_by_variant.csv` | Reports source-environment stability summary by variant |
| Bounded sensitivity decision matrix | `data/processed/sensitivity/bounded_sensitivity_decision_matrix_by_cell.csv` | Classifies filer-construct cells by retrieval-stage separability attention |
| Bounded sensitivity variant decisions | `data/processed/sensitivity/bounded_sensitivity_variant_decisions.csv` | Classifies source-set variants by decision band |
| XBRL construct coverage by filer | `data/processed/xbrl_coverage/construct_coverage_by_filer.csv` | Maps retrieved XBRL facts and paths to ex ante construct families by filer/construct |
| XBRL construct coverage by family | `data/processed/xbrl_coverage/construct_coverage_by_family.csv` | Reports concept-family coverage across filers |
| NKE XBRL worked example | `data/processed/xbrl_coverage/xbrl_worked_example_nke_inventory.md` | Links raw facts, relation paths, rendered context, LLM claims, and coding outcomes |

## Authoritative LLM Runs

| Manuscript Layer | Run Label | Manifest | Output Folder | Model |
|---|---|---|---|---|
| Main deep cases | `gemma4_31b_full` | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` | `data/processed/llm_outputs/gemma4_31b_full/` | `gemma4:31b` |
| Bounded extension | `gemma4_31b_extension` | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | `data/processed/llm_outputs/gemma4_31b_extension/` | `gemma4:31b` |

The bounded extension is full scale: six additional filers, two constructs, and four conditions, including the LLM-only diagnostic baseline.

## Authoritative Claim-Coding Files

| Layer | File | Use |
|---|---|---|
| Main deep cases | `data/processed/coding/claim_level_coding_gemma4_31b.csv` | Claim-level variables for 94 main-case claims |
| Bounded extension | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | Claim-level variables for 187 extension claims |
| Main coding summary | `data/processed/coding/claim_coding_summary_gemma4_31b.md` | Main-case source-support and integration diagnostic summary |
| Extension coding summary | `data/processed/coding/claim_coding_summary_gemma4_31b_extension.md` | Extension source-support and integration diagnostic summary |
| Independent coding protocol | `data/processed/coding/independent_coding_protocol.md` | Coder instructions for external validation |
| Independent coding sample | `data/processed/coding/independent_coding_sample.csv` | 120-claim validation sample including all 89 hybrid claims |
| Independent coding results | `data/processed/coding/independent_coding_results.csv` | Completed two-coder results, 240 coder-claim rows |
| Intercoder reliability summary | `data/processed/coding/intercoder_reliability_summary.md` | Completed reliability summary |
| Independent coding disagreements | `data/processed/coding/independent_coding_disagreements.csv` | 22 variable-level disagreement records after recoding |
| Independent coding reconciliation notes | `data/processed/coding/independent_coding_reconciliation_notes.md` | Documents three focal substantive reconciliation items |
| Hybrid integration mechanism details | `data/processed/coding/hybrid_integration_mechanisms.csv` | Decomposes all 89 hybrid claims by actual evidence-use mechanism |
| Hybrid integration mechanism summary | `data/processed/coding/hybrid_integration_mechanism_summary.csv` | Reports mechanism-level counts and shares |
| Selected manuscript examples | `data/processed/coding/selected_manuscript_examples_prelim.csv` | Main-text selected examples |
| Selected source spot checks | `data/processed/coding/selected_source_spot_check.csv` | Source traceability examples |

## Authoritative Scripts

| Script | Purpose |
|---|---|
| `scripts/sec_download.py` | Reconstruct public SEC source files |
| `scripts/extract_demo_data.py` | Extract text chunks, XBRL facts, and XBRL relation paths |
| `scripts/build_retrieval_contexts.py` | Build retrieval contexts and prompts |
| `scripts/analyze_context_diagnostics.py` | Build context-volume diagnostics |
| `scripts/analyze_retrieval_perturbation_diagnostics.py` | Build source-environment perturbation diagnostics |
| `scripts/analyze_bounded_sensitivity_decision_matrix.py` | Build reviewer-facing bounded sensitivity decision matrix |
| `scripts/analyze_xbrl_construct_coverage.py` | Build ex ante XBRL construct-family coverage diagnostics |
| `scripts/run_llm_prompts.py` | Run local Ollama prompts |
| `scripts/code_llm_claims.py` | Segment and preliminarily code claims |
| `scripts/analyze_hybrid_integration_mechanisms.py` | Build hybrid integration mechanism diagnostics |
| `scripts/validate_llm_results.py` | Validate output completeness and source-reference integrity |
| `scripts/build_checksum_manifest.py` | Rebuild SHA-256 checksum manifest |

## Reviewer Guidance

For manuscript verification, reviewers should start with this file, then inspect:

1. `data/processed/retrieval_contexts/context_manifest.csv`
2. `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv`
3. `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv`
4. `data/processed/coding/claim_level_coding_gemma4_31b.csv`
5. `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
6. `data/processed/coding/intercoder_reliability_summary.md`
7. `data/processed/xbrl_coverage/construct_coverage_by_filer.csv`
8. `data/processed/sensitivity/bounded_sensitivity_decision_summary.md`
9. `data/processed/checksums/checksum_manifest.csv`

Files listed in `DEPRECATED_OR_PILOT_ARTIFACTS.md` should not be used to verify manuscript counts, tables, or claims.
