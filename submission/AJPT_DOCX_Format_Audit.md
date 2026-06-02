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
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | Second-revision response letter draft |

## Word COM Structural QA

The files were opened through Microsoft Word automation, repaginated, and checked for page count, word count, Normal style, margin settings, and Word-table count.

| File | Pages | Words | Normal Font | Normal Size | Line Rule | Margins | Word Tables |
|---|---:|---:|---|---:|---:|---|---:|
| `AJPT_Cover_Letter.docx` | 3 | 602 | Times New Roman | 12 | 2 | 1 inch | 0 |
| `AJPT_Main_Manuscript.docx` | 51 | 12,981 | Times New Roman | 12 | 2 | 1 inch | 9 |
| `AJPT_Online_Supplement.docx` | 28 | 7,880 | Times New Roman | 12 | 2 | 1 inch | 39 |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | 10 | 1,867 | Times New Roman | 12 | 2 | 1 inch | 0 |
| `AJPT_Title_Page.docx` | 2 | 206 | Times New Roman | 12 | 2 | 1 inch | 0 |

Line Rule 2 is Word's double-spacing rule. Margins were checked as 72 points on the top and left margins, corresponding to 1 inch; the builder applies 72 points on all four margins.

## Content QA

Automated text extraction from the DOCX files found:

- No `Insert Table` or `Insert Figure` callouts.
- No internal labels such as `Submission-Ready Manuscript Draft v3`.
- Main manuscript order confirmed as `REFERENCES`, `FIGURE CAPTIONS`, `TABLES`, `APPENDIX`.
- New Table 2 on retrieval-environment validity versus adjacent validity concepts confirmed in the main manuscript.
- Revised conceptual distinctiveness language confirmed in the main manuscript, including the retrieval-specific diagnostic lens framing and fatal/fixable/reporting-gap decision rules.
- Completed independent coding reliability evidence confirmed in the main manuscript and online supplement.
- Hybrid integration mechanism diagnostic confirmed in the main manuscript and online supplement.
- Context-volume and source-environment perturbation diagnostics confirmed in the main manuscript and online supplement.
- Revised protocol-validation language confirmed in the main manuscript, online supplement, and cover letter.
- Tier 2 model-validation design language confirmed in the main manuscript, online supplement, and cover letter.
- Nine-filer protocol-validation package language confirmed in the main manuscript, online supplement, and cover letter.
- Full-scale extension language confirmed in the main manuscript, online supplement, and cover letter.
- Updated count language confirmed in the main manuscript, online supplement, and cover letter: 48 extension outputs, 72 total retrieval-conditioned outputs, and 281 preliminary coded claims.
- Reviewer-risk revisions confirmed: the main manuscript clarifies the inspectable table-based XBRL fact/path prototype, the hybrid-heavy 120-claim validation sample rationale, the independent-coding boundary, source-ID resolvability, and the limited stability evidence.
- Post-review polish confirmed: the abstract reports the nine-filer, 72-output, 281-claim, and 120-claim independent-coding evidence package; the contribution paragraph uses preliminary audit-boundary language; and replication documentation clarifies processed-only raw SEC reconstruction.
- Integrated-correctness language confirmed as bridge-based coding rather than an average-score performance claim; one-source hybrid claims are treated as non-integrated rather than partially integrated.
- Online supplement and replication documentation use the verified retrieval-log row count of 464.
- Reviewer-risk revisions confirmed: aggregate appendix tables no longer report audit-valid means, extension filer constructs are labeled as revenue and inventory, and main-text language describes limited applicability evidence rather than generalized scalability.

## Visual Render QA

The documents skill's DOCX-to-PNG renderer was attempted after installing `pdf2image`, but the local renderer environment does not have LibreOffice/soffice in PATH. A later fallback attempt to export the revised main manuscript through Microsoft Word automation timed out in the local environment. The current final QA therefore relies on Microsoft Word structural checks plus DOCX XML content checks rather than a completed latest-render PNG pass.

- Latest structurally checked files: title page, cover letter, main manuscript, online supplement, and response letter.
- Latest main manuscript structural page count: 51
- Latest main manuscript structural word count: 12,981
- Response letter visual QA: DOCX-to-PNG renderer could not find LibreOffice/soffice, so the response letter was exported to PDF through Microsoft Word automation and rendered to PNG pages through PyMuPDF. The ten-page contact sheet was visually inspected; no clipping, overlap, or page-flow defect was observed.
- Result: Word COM structural QA passed for page count, word count, table count, margins, double spacing, and required content markers. LibreOffice-based renderer remains unavailable in this environment.

## Remaining Manual Items

- Fill author-specific title page and cover letter placeholders.
- Fill response-letter date and corresponding-author signature placeholders.
- Confirm conflict-of-interest, funding, acknowledgments, and data availability language.
- If the submission system requires separate figure graphics files, prepare final figure image files from the figure specifications.
- If the journal requires a single combined document, create an integrated version from the current separate-file package.
