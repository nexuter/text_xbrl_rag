# AJPT-Prefixed Submission File Classification Log

## Purpose

This log records the classification of files in `submission/` whose names begin with `AJPT_`. The goal is to avoid accidentally uploading QA artifacts or alternative-format files as primary journal submission files.

## Implemented Updates

Updated:

- `submission/FINAL_SUBMISSION_FILE_LIST.md`
- `submission/00_SUBMISSION_README.md`

The updated files now separate:

- primary submission files;
- conditional upload files;
- alternative-format files; and
- internal/support QA artifacts.

## AJPT-Prefixed File Classification

| File | Classification | Upload Guidance |
|---|---|---|
| `AJPT_Title_Page.docx` | Primary submission file | Upload after author fields are completed |
| `AJPT_Main_Manuscript.docx` | Primary submission file | Upload |
| `AJPT_Online_Supplement.docx` | Primary submission file | Upload if supplement is requested/allowed |
| `AJPT_Cover_Letter.docx` | Primary submission file | Upload after date/disclosure/signature fields are completed |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | Primary revision-response file | Upload if the system requests a response-to-reviewers file, after date/signature fields are completed |
| `AJPT_Replication_Package_processed_only.zip` | Primary or repository-support file | Upload if the journal/repository accepts replication files |
| `AJPT_Figure_Files_upload_formats.zip` | Conditional figure package | Upload only if separate figure files are required |
| `AJPT_Figure_Files_SVG.zip` | Alternative figure package | Usually do not upload; use only if SVG-only files are preferred |
| `AJPT_DOCX_Format_Audit.md` | Internal/support QA file | Do not upload unless requested |
| `AJPT_Response_to_Reviewers_Second_Revision.pdf` | Render QA artifact / optional PDF copy | Do not upload unless the system specifically requires PDF |

## Verification

All current `submission/AJPT_*` files are listed in either `FINAL_SUBMISSION_FILE_LIST.md` or `00_SUBMISSION_README.md`.

## Remaining Pre-Upload Edits

Author-specific fields remain required in:

- `AJPT_Title_Page.docx`
- `AJPT_Cover_Letter.docx`
- `AJPT_Response_to_Reviewers_Second_Revision.docx`

The blind main manuscript and online supplement remain clean of bracketed author placeholders.
