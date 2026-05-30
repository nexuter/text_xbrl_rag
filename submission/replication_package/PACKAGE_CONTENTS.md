# Replication Package Contents

## Package Scope

This folder is the submission-facing replication package for:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

The package includes processed retrieval artifacts, scripts, model metadata, checksums, and documentation. It excludes the full raw SEC archive by default because raw filings are public and the local raw archive is approximately 360 MB.

## Directory Map

| Path | Purpose |
|---|---|
| `README_REPLICATION.md` | End-to-end reproduction instructions |
| `RAW_SEC_RECONSTRUCTION_NOTE.md` | Explains raw SEC exclusion and reconstruction |
| `config/filer_manifest.json` | Filer sample and accession/source manifest |
| `scripts/` | Download, extraction, retrieval, LLM, coding, validation, and checksum scripts |
| `data/processed/` | Processed text chunks, XBRL facts, relation paths, prompts, outputs, logs, coding, checksums |
| `docs/73_ollama_model_metadata_note.md` | Local `gemma4:31b` model metadata |
| `docs/74_checksum_manifest_package.md` | Checksum scope note |

## Expected Counts

| Item | Count |
|---|---:|
| Active filers | 9 |
| Text chunk rows | 1,377 |
| XBRL fact rows | 2,566 |
| XBRL path rows | 1,619 |
| Retrieval contexts | 42 |
| Retrieval log rows | 313 |
| LLM outputs | 42 |
| Claim-level coded claims | 182 |
| Checksum manifest rows | 1,379 |

## Raw SEC Archive Policy

The raw SEC source files are excluded from this submission-facing package by default. The package preserves:

1. Public source reconstruction through `sec_download.py`.
2. Filer/source specification through `config/filer_manifest.json`.
3. Processed artifacts generated from the local raw archive.
4. Checksum records for integrity review.

If the final repository supports larger deposits, the full raw SEC directory can be uploaded as a separate raw-source archive.
