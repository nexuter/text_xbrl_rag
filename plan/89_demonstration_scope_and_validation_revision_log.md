# Demonstration Scope And Validation Revision Log

## Purpose

This log records the revision that reframes the evidence package as a **full-scale nine-filer protocol-validation demonstration** rather than a three-filer model-validation study.

## Count Verification

The source files support the following counts:

| Evidence Layer | Source File | Verified Count |
|---|---|---:|
| Main deep-case outputs | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` | 24 |
| Bounded-extension outputs | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | 48 |
| Main deep-case coded claims | `data/processed/coding/claim_level_coding_gemma4_31b.csv` | 94 |
| Bounded-extension coded claims | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | 187 |
| Retrieval log rows | `data/processed/retrieval_logs/retrieval_log.csv` | 464 |
| Total outputs | Main plus extension | 72 |
| Total coded claims | Main plus extension | 281 |

## Interpretation

The extension is now full scale. The main layer uses three filers, two constructs, and four conditions, including the LLM-only diagnostic baseline. The bounded extension now applies the same two-construct, four-condition grid to six additional filers, producing 48 outputs.

The extension was generated through resumable local Ollama runs. Earlier bounded-extension attempts produced partial output sets before timeout; the final full-scale pass reused existing completed files and filled the remaining filer/construct/condition cells. The final bounded-extension manifest contains all 48 rows, and all 48 text outputs and raw JSON files are present. The final manifest records `skipped_existing = 48` because it was rerun after the artifacts had been completed, not because outputs are missing.

## Manuscript Position

The revised manuscript should be read as follows:

1. The paper uses three familiar filers for deep source tracing and claim-level illustration.
2. The paper uses six additional filers as a full-scale bounded maximum-variation applicability check.
3. The full nine-filer package validates the protocol's inspectability, source traceability, and claim-level evidence-use coding.
4. The current evidence does not validate model performance, retrieval superiority, audit-judgment quality, or failure-mode prevalence.

## Preliminary Coding Boundary

Preliminary author-coded claims remain acceptable for the current methodological purpose because the central evidence rests on traceability and evidence-use divergence. Audit-valid and integrated-correctness scores should not be interpreted as final audit-validity evidence or model-performance measures.

Stronger audit-judgment or model-performance claims would require independent audit-domain coding, reliability evidence, retrieval sensitivity checks, prompt sensitivity checks, and a larger Tier 2 validation design.

## Files Revised

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/Cover_Letter.md`
- `submission/00_SUBMISSION_README.md`
- `submission/Submission_Bundle_Map.md`
- `submission/Tables_and_Figures.md`
- `submission/README_REPLICATION.md`
- `submission/Replication_Package_Manifest.md`
- `plan/69_submission_ready_manuscript_v3.md`
- `plan/77_final_cover_letter_submission_template.md`
- `plan/74_checksum_manifest_package.md`
- `plan/52_llm_results_validation_log.md`
