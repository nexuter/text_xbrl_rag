# Final Submission File List

## Submission Package Status

The `submission/` folder contains the current submission-facing package for:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval**

The core manuscript, online supplement, processed-only replication package, and figure upload files are prepared. The required pre-upload edits are author-specific fields in the title page, cover letter, and response letter.

## Primary Files To Upload

| Upload Role | File | Status | Notes |
|---|---|---|---|
| Title page | `AJPT_Title_Page.docx` | Needs author details | Separate AAA-formatted title page; fill author names, affiliations, corresponding author, acknowledgments, funding, conflict, and data availability fields before upload |
| Main manuscript | `AJPT_Main_Manuscript.docx` | Ready after author review | Main article file; no author-identifying information; 51 pages, 12,981 words, 9 Word tables |
| Online supplement | `AJPT_Online_Supplement.docx` | Ready after author review | Online appendix/supplement; 28 pages, 7,880 words, 39 Word tables |
| Cover letter | `AJPT_Cover_Letter.docx` | Needs author/date/disclosure fields | Fill submission date, corresponding author details, disclosure/conflict/funding language |
| Response to reviewers | `AJPT_Response_to_Reviewers_Second_Revision.docx` | Needs date/signature fields | 10 pages, 1,867 words; fill submission date and corresponding-author signature block before upload |
| Replication package | `AJPT_Replication_Package_processed_only.zip` | Ready | Processed-only package; excludes full raw SEC archive by default; contains scripts, processed data, outputs, coding, checksums, and documentation |
| Figure files | `AJPT_Figure_Files_upload_formats.zip` | Ready if separate figure upload is required | Includes SVG, PNG, PDF versions of Figures 1, 1A, and 2 plus figure README |

## AJPT-Prefixed File Classification

Not every file beginning with `AJPT_` is a journal-upload file. Use the classification below.

| File | Classification | Upload? | Notes |
|---|---|---|---|
| `AJPT_Title_Page.docx` | Primary submission file | Yes, after author fields are completed | Separate title page |
| `AJPT_Main_Manuscript.docx` | Primary submission file | Yes | Blind main manuscript |
| `AJPT_Online_Supplement.docx` | Primary submission file | Yes, if online supplement is requested/allowed | Online appendix/supplement |
| `AJPT_Cover_Letter.docx` | Primary submission file | Yes, after date/disclosure/signature fields are completed | Cover letter |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | Primary submission file for revision | Yes, after date/signature fields are completed | Upload if the system requests a response-to-reviewers file |
| `AJPT_Replication_Package_processed_only.zip` | Primary or repository-support file | Yes, if the journal/repository accepts a replication upload | Processed-only replication package |
| `AJPT_Figure_Files_upload_formats.zip` | Conditional figure upload package | Upload only if separate figure files are required | Contains SVG, PNG, and PDF versions |
| `AJPT_Figure_Files_SVG.zip` | Alternative figure upload package | Usually no | Use only if SVG-only figure upload is preferred |
| `AJPT_DOCX_Format_Audit.md` | Internal/support QA file | No, unless requested | Documents formatting and structural QA |
| `AJPT_Response_to_Reviewers_Second_Revision.pdf` | Render QA artifact / optional PDF copy | No, unless the system specifically requires PDF | DOCX is the submission-facing response file |

## Optional Or System-Dependent Files

| Use Case | File | Status | Notes |
|---|---|---|---|
| Figure upload if SVG-only preferred | `AJPT_Figure_Files_SVG.zip` | Ready | Smaller SVG-only figure archive |
| Replication documentation as separate upload | `README_REPLICATION.md` | Ready | Human-readable replication instructions |
| Replication manifest as separate upload | `Replication_Package_Manifest.md` | Ready | Describes included/excluded materials and expected counts |
| Format QA support | `AJPT_DOCX_Format_Audit.md` | Ready | Internal/support file documenting Word COM structural QA and manuscript-preparation checks |
| Pre-upload placeholder audit | `PRE_UPLOAD_AUTHOR_PLACEHOLDER_AUDIT.md` | Ready for final manual pass | Identifies DOCX files that still require author/date/signature fields before upload |
| Submission map | `Submission_Bundle_Map.md` | Ready | Explains file roles and boundary statements |
| Author checklist | `Author_Information_Checklist.md` | Ready for author completion | Use before upload to fill required author-specific fields |

## Source Markdown Files

These files are clean submission-facing source copies, but the journal upload should normally use the DOCX files above unless the submission system requests source files.

| Source File | Purpose |
|---|---|
| `Manuscript_Retrieval_as_Research_Design.md` | Markdown source for main manuscript |
| `Tables_and_Figures.md` | Markdown source for main tables and figure specifications |
| `Online_Supplement_Appendix.md` | Markdown source for online supplement |
| `Response_to_Reviewers_Second_Revision.md` | Draft response letter for second revision |
| `Title_Page_Template.md` | Editable title-page source with author placeholders |
| `Cover_Letter.md` | Editable cover-letter source with author/date placeholders |

## Folders

| Folder | Purpose | Upload Guidance |
|---|---|---|
| `figures/` | Individual SVG, PNG, and PDF figure files | Use only if the journal requests individual figure files rather than the figure zip |
| `replication_package/` | Unzipped processed-only replication package | Upload the zip unless the repository asks for uncompressed files |
| `render_qa_main/` | Local render QA artifacts | Internal only; not needed for journal upload |

## Final Manual Items Before Upload

1. Fill author details in `AJPT_Title_Page.docx`.
2. Fill submission date, corresponding author, and disclosure language in `AJPT_Cover_Letter.docx`.
3. Confirm conflict-of-interest, funding, acknowledgments, and data availability wording.
4. Fill `AJPT_Response_to_Reviewers_Second_Revision.docx` response-letter date and corresponding-author signature fields.
5. Decide whether to upload the processed-only replication zip alone or also deposit a separate raw SEC archive if repository size policy permits.
6. Upload separate figure files only if the submission system requires them.

## QA Snapshot

| File | QA Result |
|---|---|
| `AJPT_Main_Manuscript.docx` | Word COM structural QA passed; no internal draft label; required protocol, Tier 2, nine-filer, 72-output, and 281-claim markers present |
| `AJPT_Online_Supplement.docx` | Word COM structural QA passed; supplement markers present |
| `AJPT_Replication_Package_processed_only.zip` | Zip opens successfully; contains 429 entries |
| `AJPT_Figure_Files_upload_formats.zip` | Zip opens successfully; contains SVG, PNG, and PDF files for Figures 1, 1A, and 2 |
| `AJPT_Figure_Files_SVG.zip` | Zip opens successfully; contains SVG files for Figures 1, 1A, and 2 |

