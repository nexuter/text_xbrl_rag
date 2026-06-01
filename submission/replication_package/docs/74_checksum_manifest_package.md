# Checksum Manifest Package

## Purpose

This note documents the checksum manifest added to the replication package for the AJPT methodology manuscript.

The checksum manifest is an archival integrity control. It helps reviewers or future users verify whether raw SEC files, processed artifacts, scripts, the filer manifest, and the replication README have changed after the manifest was generated.

It is not evidence of audit validity, retrieval performance, model performance, or exact LLM output reproducibility.

## Generated Artifacts

| Artifact | Purpose |
|---|---|
| `scripts/build_checksum_manifest.py` | Rebuilds the checksum manifest using SHA-256 |
| `data/processed/checksums/checksum_manifest.csv` | File-level checksum manifest |
| `data/processed/checksums/checksum_summary.md` | Human-readable checksum summary |

## Current Manifest Summary

| Field | Value |
|---|---|
| Generated at UTC | `2026-05-31T22:13:12.339530+00:00` |
| Hash algorithm | SHA-256 |
| Total files hashed | 394 |

## Counts By Category

| Category | Files | Size Bytes |
|---|---:|---:|
| config | 1 | 4,128 |
| processed | 380 | 17,115,088 |
| root | 1 | 10,170 |
| script | 12 | 124,866 |

## Reviewer-Facing Interpretation

The checksum manifest strengthens the reproducibility package by adding a file-integrity layer. A reviewer can verify whether the archive used to build the manuscript evidence trail has changed since the manifest was generated.

The checksum manifest does not address the paper's substantive validity boundaries. It does not validate whether XBRL is audit evidence, whether preliminary audit-valid scores are correct, whether retrieval improves LLM reasoning, or whether `gemma4:31b` outputs can be exactly reproduced on another machine.

## How To Rebuild

Run from the project root:

```powershell
python scripts/build_checksum_manifest.py
```

The script excludes its own generated checksum CSV and summary so repeated runs do not recursively hash prior checksum outputs.

## Submission Use

This package resolves the optional raw-file checksum item identified in the v3 reviewer stress test. It should be referenced in the replication package, not in the main manuscript unless the journal asks for additional reproducibility detail.
