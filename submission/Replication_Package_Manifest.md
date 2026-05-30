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
| LLM prompt runner | `scripts/run_llm_prompts.py` | Yes | Runs demonstration prompts with local Ollama model |
| Claim coding script | `scripts/code_llm_claims.py` | Yes | Converts outputs into claim-level coding file |
| Validation script | `scripts/validate_llm_results.py` | Yes | Checks source references and coding consistency |
| Checksum script | `scripts/build_checksum_manifest.py` | Yes | Generates SHA-256 checksum manifest |
| Processed data | `data/processed/` | Yes | Main replication artifacts |
| Raw SEC data | `data/raw_sec/` | No, by default | Publicly reconstructable from SEC EDGAR; include separately only if repository policy permits |
| Checksum manifest | `data/processed/checksums/checksum_manifest.csv` | Yes | 1,379 file checksums |
| Checksum summary | `data/processed/checksums/checksum_summary.md` | Yes | Category-level checksum summary |
| Replication README | `submission/README_REPLICATION.md` | Yes | Reproduction instructions |

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
| Retrieval contexts | 42 |
| Retrieval log rows | 313 |
| Main LLM outputs | 24 |
| Extension LLM outputs | 18 |
| Total LLM outputs | 42 |
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total coded claims | 182 |
| Text chunk rows | 1,377 |
| XBRL fact rows | 2,566 |
| XBRL path rows | 1,619 |

## Packaging Note

The current submission-facing package excludes the full raw SEC archive by default because it contains 1,119 files and is approximately 360 MB. The package includes processed artifacts, source accession metadata, download scripts, checksums, and `replication_package/RAW_SEC_RECONSTRUCTION_NOTE.md`. If the final repository permits larger deposits, raw SEC files can be uploaded as a separate raw-source archive.
