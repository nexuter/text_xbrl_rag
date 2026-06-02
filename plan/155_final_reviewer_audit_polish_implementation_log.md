# Final Reviewer-Audit Polish Implementation Log

## Purpose

This log records the targeted polish implemented after the final reviewer-style audit in `plan/154_final_reviewer_critical_audit_before_next_revision.md`.

## Implemented Changes

### 1. Abstract Count Framing

Updated the abstract in `submission/Manuscript_Retrieval_as_Research_Design.md` so the hybrid-claim count is framed as an illustration of claim-level source-use heterogeneity rather than as a headline frequency result.

Revised framing:

- The nine-filer package "illustrates claim-level source-use heterogeneity."
- The `8 of 89`, `61`, and `20` counts remain, but they are explicitly introduced as within-design diagnostics.

### 2. Positive Contribution Sharpening

Updated the introduction's contribution paragraph to state that the framework converts retrieval artifacts and model responses into:

- reviewer-evaluable design evidence; and
- study-level variables.

This strengthens the positive AJPT methodology contribution and reduces the risk that the paper reads only as limitation management.

### 3. Tier 1 Success Criteria

Added a compact Tier 1 success-criteria paragraph at the beginning of Section VII:

- retrieval environment can be reconstructed;
- source identifiers resolve to preserved materials;
- LLM outputs can be segmented into claim-level variables;
- central source-use and integration variables can be coded reliably; and
- sensitivity boundaries are documented.

The paragraph explicitly states that these are protocol-validation criteria, not model-performance criteria.

### 4. Response Letter Positive Framing

Updated `submission/Response_to_Reviewers_Second_Revision.md` to say the revised framework gives reviewers a reusable decision rule for evaluating when retrieval-stage artifacts are sufficient for Tier 1 methodology claims and when Tier 2 evidence is required.

Also strengthened the closing paragraph to emphasize that the package helps audit researchers design, diagnose, and report retrieval-based LLM studies.

### 5. Replication CSV Terminology

Added duplicate audit-boundary columns to the processed coding files:

- `audit_boundary_prelim`
- `audit_boundary_rationale` where an audit-valid rationale column existed.

Updated files:

- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
- `submission/replication_package/data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `submission/replication_package/data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
- `data/processed/coding/independent_coding_sample.csv`
- `submission/replication_package/data/processed/coding/independent_coding_sample.csv`

Legacy `audit_valid_*` columns remain for compatibility with earlier scripts, but README files now describe them as deprecated aliases for preliminary audit-boundary diagnostics.

### 6. Independent Coding Row Count Documentation

Updated both replication READMEs to clarify:

- the validation sample contains 120 claims; and
- `independent_coding_results.csv` contains 240 coder-claim rows because two coders coded each validation claim.

Updated files:

- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`

### 7. Rebuilt Checksums, Replication Zip, And DOCX Files

Rebuilt checksum manifests in both root and submission replication-package contexts.

Rebuilt:

- `submission/AJPT_Replication_Package_processed_only.zip`
- `submission/AJPT_Title_Page.docx`
- `submission/AJPT_Cover_Letter.docx`
- `submission/AJPT_Main_Manuscript.docx`
- `submission/AJPT_Online_Supplement.docx`
- `submission/AJPT_Response_to_Reviewers_Second_Revision.docx`

Updated submission tracking files with latest structural QA counts:

- Main manuscript: 51 pages, 12,981 words, 9 Word tables.
- Response letter: 10 pages, 1,867 words.
- Replication zip: 429 entries.

Updated files:

- `submission/AJPT_DOCX_Format_Audit.md`
- `submission/FINAL_SUBMISSION_FILE_LIST.md`

## QA Results

### DOCX Structural QA

Latest `scripts/check_docx_revision.ps1` results:

| File | Pages | Words | Tables | Key Markers |
|---|---:|---:|---:|---|
| `AJPT_Cover_Letter.docx` | 3 | 602 | 0 | protocol, Tier 2, nine-filer, extension/count markers present |
| `AJPT_Main_Manuscript.docx` | 51 | 12,981 | 9 | protocol, Tier 2, nine-filer, extension/count markers present |
| `AJPT_Online_Supplement.docx` | 28 | 7,880 | 39 | protocol, Tier 2, nine-filer, extension/count markers present |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | 10 | 1,867 | 0 | protocol, Tier 2, nine-filer markers present |
| `AJPT_Title_Page.docx` | 2 | 206 | 0 | author-facing title page |

### Count QA

Verified from CSV files:

| Item | Count |
|---|---:|
| Total claims | 281 |
| Hybrid claims | 89 |
| Hybrid integrated claims | 8 |
| Hybrid text-only claims | 61 |
| Hybrid XBRL-only claims | 20 |

### Visual QA

The latest response letter was exported from Word to PDF and rendered to 10 PNG pages through PyMuPDF. The contact sheet was visually inspected. No blank page, clipping, or page-flow defect was observed.

## Remaining Manual Items

- Fill author-specific title page and cover letter fields.
- Confirm final disclosure, conflict-of-interest, funding, acknowledgments, and data availability wording.
- If the journal repository requires uncompressed replication files, upload the unzipped package rather than only the zip.
