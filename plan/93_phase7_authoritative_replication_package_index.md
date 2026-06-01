# Phase 7 Authoritative Replication Package Index

## Purpose

This log records the first implementation step from `plan/92_two_reviewer_reports_comprehensive_revise_plan.md`: making the replication package reviewer-usable by distinguishing authoritative manuscript evidence from pilot, smoke, dry-run, and deprecated artifacts.

## Reviewer Concern Addressed

Both reviewer reports raised concerns that the replication package contains multiple run artifacts and that reviewers should not need to infer which files correspond to manuscript tables and counts.

The most important ambiguity was the presence of:

- early `gemma4:latest` pilot runs,
- `gemma4:31b` smoke tests,
- dry-run manifests,
- reduced-extension dry-run artifacts,
- generic coding aliases alongside run-specific coding files.

## Changes Implemented

### 1. Added Authoritative File Index

Created:

- `submission/replication_package/AUTHORITATIVE_FILES.md`

This file identifies the manuscript-evidence sources for:

| Evidence Item | Authoritative File | Count |
|---|---|---:|
| Retrieval contexts | `data/processed/retrieval_contexts/context_manifest.csv` | 72 |
| Retrieval log rows | `data/processed/retrieval_logs/retrieval_log.csv` | 464 |
| Main outputs | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` | 24 |
| Extension outputs | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | 48 |
| Main claims | `data/processed/coding/claim_level_coding_gemma4_31b.csv` | 94 |
| Extension claims | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | 187 |
| Total claims | Main plus extension coding files | 281 |

### 2. Added Deprecated/Pilot Artifact Note

Created:

- `submission/replication_package/DEPRECATED_OR_PILOT_ARTIFACTS.md`

This file marks the following as non-authoritative:

- `data/processed/llm_outputs/run_manifest.csv`
- `data/processed/llm_outputs/run_summary.md`
- `data/processed/llm_outputs/run_manifest_dry_run.csv`
- `data/processed/llm_outputs/run_summary_dry_run.md`
- `data/processed/llm_outputs/gemma4_31b_smoke/`
- `data/processed/llm_outputs/gemma4_31b_drycheck/`
- `data/processed/llm_outputs/gemma4_31b_extension_dryrun/`

### 3. Updated Replication README Files

Updated:

- `README_REPLICATION.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`

Key corrections:

1. Added an authoritative-evidence section.
2. Directed reviewers to the new authoritative index.
3. Marked pilot/smoke/dry-run artifacts as provenance rather than manuscript evidence.
4. Corrected the context-building command to:

```powershell
python scripts/build_retrieval_contexts.py --manifest config/filer_manifest.json --extension-all-constructs --include-extension-baseline
```

5. Corrected the extension LLM command to include all four conditions by removing the old `--conditions text,xbrl,hybrid` reduced-extension filter.

### 4. Updated Submission Package Maps

Updated:

- `submission/Replication_Package_Manifest.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`

These now list the authoritative index and deprecated/pilot artifact note as part of the package documentation.

## Reviewer-Facing Interpretation

The package now aligns better with the paper's own traceability standard. Reviewers can identify which files reproduce the manuscript's reported counts without confusing provenance files with manuscript evidence.

## Remaining Phase 7 Work

Optional next step:

1. Physically remove pilot/smoke/dry-run artifacts from the submission-facing ZIP, or move them to a clearly labeled `non_authoritative_archive/` folder.

Current decision:

- Preserve the artifacts for provenance.
- Clearly mark them as non-authoritative.

This is sufficient for the reviewer concern unless the journal requires a minimal replication package with no development artifacts.
