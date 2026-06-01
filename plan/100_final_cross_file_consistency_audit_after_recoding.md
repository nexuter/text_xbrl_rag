# Final Cross-File Consistency Audit After Recoding

## Purpose

This audit checks that the recoded independent-coding results are consistently reflected across the manuscript, online supplement, replication README, replication package, DOCX files, checksum files, and compressed submission archive.

## Actions Completed

1. Regenerated independent coding outputs from:
   - `coder/coder_1_completed_coding_form.csv`
   - `coder/coder2_completed_coding_form.csv`
2. Updated manuscript-facing reliability language in:
   - `submission/Manuscript_Retrieval_as_Research_Design.md`
   - `submission/Online_Supplement_Appendix.md`
   - `submission/README_REPLICATION.md`
   - `README_REPLICATION.md`
3. Updated submission package maps and boundary statements in:
   - `submission/00_SUBMISSION_README.md`
   - `submission/Submission_Bundle_Map.md`
   - `submission/Replication_Package_Manifest.md`
   - `submission/replication_package/PACKAGE_CONTENTS.md`
   - `submission/replication_package/AUTHORITATIVE_FILES.md`
4. Regenerated DOCX files using `scripts/build_ajpt_submission_docx.ps1`.
5. Ran DOCX structural QA using `scripts/check_docx_revision.ps1`.
6. Ran LLM-result validation using `scripts/validate_llm_results.py`.
7. Regenerated checksums using `scripts/build_checksum_manifest.py`.
8. Rebuilt `submission/AJPT_Replication_Package_processed_only.zip`.
9. Added a context-volume diagnostic for separability transparency after the two-reviewer reflection audit.

## Authoritative Independent-Coding Counts

| Item | Count |
|---|---:|
| Validation sample claims | 120 |
| Coder rows | 240 |
| Disagreement records | 22 |
| Focal substantive reconciliation items | 3 |
| Context-volume diagnostic rows | 72 |
| Checksum manifest rows | 408 |

## Authoritative Reliability Results

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Boundary Language Audit

The submission files now distinguish:

- audit-valid scores: preliminary author-coded diagnostics unless independently reviewed by audit-domain experts;
- evidence-use type and integrated correctness: independently coded in the 120-claim validation sample to evaluate protocol reliability;
- model performance and final audit-validity conclusions: not claimed.

Search checks found no remaining submission-facing references to the superseded independent-coding statistics, prior disagreement count, or prior checksum-row count.

## DOCX QA

`scripts/check_docx_revision.ps1` reported:

| File | Pages | Words | Tables | Key Checks |
|---|---:|---:|---:|---|
| `AJPT_Cover_Letter.docx` | 3 | 621 | 0 | protocol, Tier 2, nine-filer, extension/output, and 281-claim markers present |
| `AJPT_Main_Manuscript.docx` | 38 | 9,456 | 8 | protocol, Tier 2, nine-filer, extension/output, and 281-claim markers present |
| `AJPT_Online_Supplement.docx` | 19 | 4,778 | 27 | protocol, Tier 2, nine-filer, extension/output, and 281-claim markers present |
| `AJPT_Title_Page.docx` | 2 | 205 | 0 | title-page file only; content markers not expected |

DOCX text checks confirmed:

- no old superseded integrated-correctness reliability values;
- no old "audit-valid and integrated scores are preliminary" phrase;
- no old aggregate "Integrated Mean" summaries or one-source hybrid claims coded as partially integrated;
- main manuscript includes 100.0 percent evidence-use and integrated-correctness agreement;
- online supplement includes weighted kappa = 1.000 for integrated correctness;
- revised audit-valid boundary language appears in main manuscript and supplement.
- strict-reviewer revisions appear in the main manuscript and supplement: table-based prototype boundary, hybrid-heavy validation-sample rationale, source-ID resolvability language, and updated appendix closing note.

## Replication Package QA

The compressed processed-only replication package contains:

- `independent_coding_reconciliation_notes.md`;
- `checksum_manifest.csv`;
- updated independent-coding results and disagreements;
- updated checksum summary.
- context-volume diagnostics and context-volume summary files.
- source-environment perturbation diagnostic files.
- hybrid integration mechanism diagnostic files.

The checksum manifest has 408 rows in both root processed data and the submission replication package.

## Remaining Author-Specific Items

The package is technically consistent after recoding. Remaining tasks are author-specific rather than methodological:

- fill title-page author details;
- fill cover-letter date, author, disclosure, conflict, funding, and data-availability fields;
- decide whether to upload raw SEC files as a separate archive if repository size permits;
- perform final human read-through before upload.
