# Replication Package Raw SEC Policy And Package Build

## Purpose

This step applies the final submission-facing policy for raw SEC files in the replication package and creates a clean replication package under `submission/`.

## Data Size Assessment

| Component | File Count | Approximate Size |
|---|---:|---:|
| `data/raw_sec/` | 1,119 | 360 MB |
| `data/processed/` | 253 | 15 MB |

## Policy Decision

Exclude the full `data/raw_sec/` directory from the default submission-facing replication package.

## Rationale

The raw SEC filings and Inline XBRL files are publicly available through SEC EDGAR and can be reconstructed from the included filer manifest and download script. Including all raw files would materially increase package size without changing the methodological evidence trail. The processed artifacts, scripts, checksum manifest, and reconstruction note preserve reviewer inspection and reproducibility.

## Created Package

Created:

- `submission/replication_package/`
- `submission/AJPT_Replication_Package_processed_only.zip`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/RAW_SEC_RECONSTRUCTION_NOTE.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`
- `submission/replication_package/config/filer_manifest.json`
- `submission/replication_package/scripts/`
- `submission/replication_package/data/processed/`
- `submission/replication_package/docs/73_ollama_model_metadata_note.md`
- `submission/replication_package/docs/74_checksum_manifest_package.md`

## Reviewer-Relevant Boundary

The package supports source traceability, retrieval-environment reconstruction, and claim-level methodological inspection. It does not treat SEC filings or XBRL facts as audit evidence, audit truth, or misstatement labels.

## Remaining Item

The processed-only compressed archive has been created. If the selected repository permits larger uploads and the author team wants raw-source archiving, create a separate raw SEC archive rather than combining raw SEC files with the default processed replication package.

## Package Size Check

| Package | Files | Size |
|---|---:|---:|
| `submission/replication_package/` | 266 | 15.5 MB |
| `submission/AJPT_Replication_Package_processed_only.zip` | 1 archive | 1.7 MB |
