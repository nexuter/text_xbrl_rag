# Pre-Upload Author Placeholder Audit

## Purpose

This audit identifies which submission-facing DOCX files still contain author-specific placeholders. It is intended for the final manual pass before journal upload.

## Placeholder Audit Result

| DOCX File | Placeholder Status | Upload Readiness |
|---|---|---|
| `AJPT_Main_Manuscript.docx` | No bracketed author placeholders detected | Ready after final author review |
| `AJPT_Online_Supplement.docx` | No bracketed author placeholders detected | Ready after final author review |
| `AJPT_Title_Page.docx` | Author, affiliation, email, corresponding-author, acknowledgments, funding, and conflict placeholders remain | Fill before upload |
| `AJPT_Cover_Letter.docx` | Submission date, author approval, conflict/disclosure, supplement statement, and signature placeholders remain | Fill before upload |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | Submission date and signature placeholders remain | Fill before upload |

## Required Final Edits

1. Fill the title page with all author names, affiliations, emails, corresponding-author information, acknowledgments, funding, conflict-of-interest, and final data-availability language.
2. Fill the cover letter with submission date, author approval statement, conflict/disclosure statement, supplemental-materials statement, and corresponding-author signature block.
3. Fill the response letter with submission date and corresponding-author signature block.
4. Regenerate the DOCX files or manually update the DOCX files after the author-specific information is final.
5. Re-run the placeholder audit before upload.

## Current Clean Files

The blind manuscript and online supplement are currently clean of bracketed author placeholders. This supports blind review because no author-specific placeholders were detected in:

- `AJPT_Main_Manuscript.docx`
- `AJPT_Online_Supplement.docx`

## Caution

Manuscript table and figure callouts such as `[Insert Table 1 about here]` are handled by the DOCX build process and are not author placeholders. The current generated main manuscript and online supplement DOCX files do not contain those bracketed callouts.
