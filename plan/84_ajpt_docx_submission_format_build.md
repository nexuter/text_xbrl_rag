# AJPT DOCX Submission Format Build

## Purpose

This step converts the clean submission-facing markdown files into Word DOCX files organized according to the AAA Manuscript Preparation Guide.

Guide source: https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide

## Completed Work

Created the DOCX builder:

- `scripts/build_ajpt_submission_docx.ps1`

Generated submission DOCX files:

- `submission/AJPT_Title_Page.docx`
- `submission/AJPT_Main_Manuscript.docx`
- `submission/AJPT_Online_Supplement.docx`
- `submission/AJPT_Cover_Letter.docx`

Created format audit:

- `submission/AJPT_DOCX_Format_Audit.md`

## Formatting Decisions

The generated manuscript package uses:

- Separate title page.
- Main article file without author-identifying information.
- Times New Roman, 12-point font.
- Double spacing.
- 1-inch margins.
- Word tables.
- No table/figure insertion callouts.
- Main article sequence: title, abstract, AI disclosure, text, references, figure captions, numbered tables, appendix summary.

## Reviewer-Relevant Rationale

The conversion preserves the paper's methodological positioning while aligning the document package with submission expectations. The main article remains readable as a manuscript, while figure captions, numbered tables, and appendix summary appear in the manuscript order expected by the AAA guide. Detailed supplement materials remain in a separate online-supplement file.

## QA Results

Word COM structural QA confirmed that all generated DOCX files open in Word and use Times New Roman 12-point Normal style, double spacing, and 1-inch margins. The main manuscript contains seven Word tables; the online supplement contains twenty-one Word tables.

Automated text checks found no `Insert Table`, `Insert Figure`, or internal v3 draft labels in the generated DOCX files.

The documents renderer could not complete PNG render QA because the local environment is missing the Python `pdf2image` dependency. As a fallback, Word automation was used for repagination and structural checks.

## Remaining Items

- Fill author-specific title page and cover letter fields.
- Confirm final funding, conflict-of-interest, acknowledgments, data availability, and AI disclosure language.
- Prepare separate figure graphics files if the submission system requires them.
- Re-run render QA if the renderer dependency becomes available.
