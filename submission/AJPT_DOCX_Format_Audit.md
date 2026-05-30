# AJPT DOCX Format Audit

## Source Guide

Primary formatting source: AAA Manuscript Preparation Guide, https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide

## Applied Requirements

The generated DOCX files apply the following submission-format requirements from the guide:

- Title page prepared as a separate Word file.
- Main article file begins with the manuscript title, abstract, generative AI disclosure, and manuscript text.
- Main article file uses the order: text, references, figure captions, numbered tables, appendix summary.
- `Insert Table/Figure here` callouts are removed.
- Main article does not contain author-identifying information.
- Manuscript DOCX files use Times New Roman, 12-point font, double spacing, and 1-inch margins.
- Tables are created as Word tables rather than pasted images or tabbed text.

## Generated DOCX Files

| File | Purpose |
|---|---|
| `AJPT_Title_Page.docx` | Separate title page with author-specific placeholders |
| `AJPT_Main_Manuscript.docx` | Main article file with title, abstract, AI disclosure, text, references, figure captions, tables, and appendix summary |
| `AJPT_Online_Supplement.docx` | Online appendix / supplement |
| `AJPT_Cover_Letter.docx` | Cover letter draft with author-specific placeholders |

## Word COM Structural QA

The files were opened through Microsoft Word automation, repaginated, and checked for page count, word count, Normal style, margin settings, and Word-table count.

| File | Pages | Words | Normal Font | Normal Size | Line Rule | Margins | Word Tables |
|---|---:|---:|---|---:|---:|---|---:|
| `AJPT_Cover_Letter.docx` | 3 | 566 | Times New Roman | 12 | 2 | 1 inch | 0 |
| `AJPT_Main_Manuscript.docx` | 31 | 7,617 | Times New Roman | 12 | 2 | 1 inch | 7 |
| `AJPT_Online_Supplement.docx` | 13 | 3,210 | Times New Roman | 12 | 2 | 1 inch | 21 |
| `AJPT_Title_Page.docx` | 2 | 205 | Times New Roman | 12 | 2 | 1 inch | 0 |

Line Rule 2 is Word's double-spacing rule. Margins were checked as 72 points on the top and left margins, corresponding to 1 inch; the builder applies 72 points on all four margins.

## Content QA

Automated text extraction from the DOCX files found:

- No `Insert Table` or `Insert Figure` callouts.
- No internal labels such as `Submission-Ready Manuscript Draft v3`.
- Main manuscript order confirmed as `REFERENCES`, `FIGURE CAPTIONS`, `TABLES`, `APPENDIX`.

## Visual Render QA Limitation

The documents skill's DOCX-to-PNG renderer was attempted, but the local renderer environment is missing the Python `pdf2image` dependency. Therefore, PNG-based visual QA could not be completed in this environment. As a fallback, the files were opened and repaginated through Microsoft Word automation, and structural formatting properties were checked directly in Word.

## Remaining Manual Items

- Fill author-specific title page and cover letter placeholders.
- Confirm conflict-of-interest, funding, acknowledgments, and data availability language.
- If the submission system requires separate figure graphics files, prepare final figure image files from the figure specifications.
- If the journal requires a single combined document, create an integrated version from the current separate-file package.
