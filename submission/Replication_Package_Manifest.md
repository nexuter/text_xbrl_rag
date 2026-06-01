# Replication Package Manifest

## Purpose

This manifest identifies the files and folders that should accompany the submission if replication materials are uploaded with the manuscript or deposited in a repository.

## Core Reproducibility Files

| Component | Path | Include In Package | Notes |
|---|---|---|---|
| Filer manifest | `config/filer_manifest.json` | Yes | Defines filer sample and accession targets |
| SEC download script | `scripts/sec_download.py` | Yes | Downloads source filings from SEC EDGAR |
| Data extraction script | `scripts/extract_demo_data.py` | Yes | Extracts text chunks, XBRL facts, and XBRL relation paths |
| Retrieval context builder | `scripts/build_retrieval_contexts.py` | Yes | Creates text, XBRL, hybrid, and baseline contexts |
| Context diagnostics script | `scripts/analyze_context_diagnostics.py` | Yes | Builds context-volume diagnostics for separability transparency |
| Retrieval perturbation diagnostics script | `scripts/analyze_retrieval_perturbation_diagnostics.py` | Yes | Builds deterministic source-environment perturbation diagnostics |
| LLM prompt runner | `scripts/run_llm_prompts.py` | Yes | Runs demonstration prompts with local Ollama model |
| Claim coding script | `scripts/code_llm_claims.py` | Yes | Converts outputs into claim-level coding file |
| Hybrid mechanism diagnostics script | `scripts/analyze_hybrid_integration_mechanisms.py` | Yes | Decomposes hybrid claims by actual evidence-use mechanism |
| Validation script | `scripts/validate_llm_results.py` | Yes | Checks source references and coding consistency |
| Checksum script | `scripts/build_checksum_manifest.py` | Yes | Generates SHA-256 checksum manifest |
| Processed data | `data/processed/` | Yes | Main replication artifacts |
| Raw SEC data | `data/raw_sec/` | No, by default | Publicly reconstructable from SEC EDGAR; include separately only if repository policy permits |
| Authoritative file index | `submission/replication_package/AUTHORITATIVE_FILES.md` | Yes | Identifies manuscript-evidence files and counts |
| Deprecated/pilot artifact note | `submission/replication_package/DEPRECATED_OR_PILOT_ARTIFACTS.md` | Yes | Separates pilot, smoke, dry-run, and non-authoritative artifacts from manuscript evidence |
| Checksum manifest | `data/processed/checksums/checksum_manifest.csv` | Yes | 408 file checksums |
| Checksum summary | `data/processed/checksums/checksum_summary.md` | Yes | Category-level checksum summary |
| Replication README | `submission/README_REPLICATION.md` | Yes | Reproduction instructions |
| Context-volume diagnostics | `data/processed/retrieval_contexts/context_volume_diagnostics.csv` | Yes | Context and prompt volume by filer/construct/condition |
| Context-volume summary | `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv` | Yes | Condition-level context-volume summary |
| Retrieval perturbation diagnostics | `data/processed/sensitivity/retrieval_perturbation_diagnostics.csv` | Yes | Source-set perturbation results by filer/construct/variant |
| Retrieval perturbation summary | `data/processed/sensitivity/retrieval_perturbation_summary_by_variant.csv` | Yes | Source-environment stability summary by variant |
| Independent coding protocol | `data/processed/coding/independent_coding_protocol.md` | Yes | Defines claim segmentation and coding variables |
| Independent coding sample | `data/processed/coding/independent_coding_sample.csv` | Yes | 120-claim validation sample |
| Independent coding results | `data/processed/coding/independent_coding_results.csv` | Yes | Completed two-coder results, 240 coder-claim rows |
| Intercoder reliability summary | `data/processed/coding/intercoder_reliability_summary.md` | Yes | Completed reliability summary |
| Independent coding disagreements | `data/processed/coding/independent_coding_disagreements.csv` | Yes | 22 variable-level disagreement records after recoding |
| Independent coding reconciliation notes | `data/processed/coding/independent_coding_reconciliation_notes.md` | Yes | Documents three focal substantive reconciliation items |
| Hybrid integration mechanism details | `data/processed/coding/hybrid_integration_mechanisms.csv` | Yes | Decomposes all 89 hybrid claims by actual evidence-use mechanism |
| Hybrid integration mechanism summary | `data/processed/coding/hybrid_integration_mechanism_summary.csv` | Yes | Reports mechanism-level counts and shares |

## Documentation Files

| Component | Path | Include In Package | Notes |
|---|---|---|---|
| Model metadata note | `plan/73_ollama_model_metadata_note.md` | Yes | Documents `gemma4:31b` local model metadata |
| Checksum package note | `plan/74_checksum_manifest_package.md` | Yes | Documents checksum package scope |
| Online supplement | `submission/Online_Supplement_Appendix.md` | Yes | Reviewer-facing methodological evidence trail |

## Expected Demonstration Counts

| Item | Expected Count |
|---|---:|
| Active filers | 9 |
| Retrieval contexts | 72 |
| Context-volume diagnostic rows | 72 |
| Retrieval perturbation diagnostic rows | 90 |
| Retrieval log rows | 464 |
| Main LLM outputs | 24 |
| Extension LLM outputs | 48 |
| Total LLM outputs | 72 |
| Main coded claims | 94 |
| Extension coded claims | 187 |
| Total coded claims | 281 |
| Independent coding validation sample | 120 |
| Independent coder rows | 240 |
| Independent coding disagreement records | 22 |
| Hybrid integration mechanism rows | 89 |
| Text chunk rows | 1,377 |
| XBRL fact rows | 2,566 |
| XBRL path rows | 1,619 |

## Packaging Note

The current submission-facing package excludes the full raw SEC archive by default because it contains 1,119 files and is approximately 360 MB. The package includes processed artifacts, source accession metadata, download scripts, checksums, and `replication_package/RAW_SEC_RECONSTRUCTION_NOTE.md`. If the final repository permits larger deposits, raw SEC files can be uploaded as a separate raw-source archive.
