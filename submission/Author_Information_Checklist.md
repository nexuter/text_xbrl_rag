# Author Information Checklist

## Purpose

Use this checklist to complete the title page, cover letter, submission-system fields, and final disclosures before uploading the manuscript package.

## Required Author Fields

| Field | Needed For | Current Location | Status |
|---|---|---|---|
| Submission date | Cover letter; response letter | `Cover_Letter.md`; `Response_to_Reviewers_Second_Revision.md` | Needed |
| Full author names | Title page; submission system | `Title_Page_Template.md` | Needed |
| Author affiliations | Title page; submission system | `Title_Page_Template.md` | Needed |
| Author emails | Title page; submission system | `Title_Page_Template.md` | Needed |
| Corresponding author | Title page; cover letter; response letter; submission system | `Title_Page_Template.md`; `Cover_Letter.md`; `Response_to_Reviewers_Second_Revision.md` | Needed |
| Corresponding author address | Title page, if required | `Title_Page_Template.md` | Needed if journal requires |
| Corresponding author phone | Title page, if required | `Title_Page_Template.md` | Needed if journal requires |
| Author approval statement | Cover letter | `Cover_Letter.md` | Confirm |
| Conflict-of-interest statement | Title page; cover letter; submission system | `Title_Page_Template.md`; `Cover_Letter.md` | Needed |
| Funding statement | Title page; submission system | `Title_Page_Template.md` | Needed |
| Acknowledgments | Title page | `Title_Page_Template.md` | Needed or state none |
| Data availability statement | Title page; submission system | `Title_Page_Template.md` | Needs final repository wording |
| AI disclosure | Manuscript; title page; submission system if required | `Manuscript_Retrieval_as_Research_Design.md`; `Title_Page_Template.md` | Drafted, confirm final wording |
| Supplemental material statement | Cover letter; submission system | `Cover_Letter.md`; `00_SUBMISSION_README.md` | Drafted, confirm final file list |
| Repository / raw-source archive decision | Submission system; replication package note | `README_REPLICATION.md`; `Replication_Package_Manifest.md` | Confirm processed-only package or add raw-source archive |

## Recommended Default Wording Where Applicable

Use only if true for the final author team.

### Author Approval

All authors have approved the submission.

### Conflict Of Interest

The authors have no conflicts of interest to disclose.

### Funding

The authors received no specific funding for this work.

### Acknowledgments

The authors thank [names/workshop participants/reviewers] for helpful comments.

If there are no acknowledgments, use:

The authors have no acknowledgments to report.

### Data Availability

Replication materials include the filer manifest, extraction and retrieval scripts, processed text and XBRL retrieval artifacts, rendered prompts, raw LLM outputs, claim-level coding files, model metadata, and checksum files. Raw SEC filings are publicly available from the SEC EDGAR system. Repository details will be provided upon acceptance or as required by the journal.

If a repository is selected before submission, replace the final sentence with:

Replication materials are available at [repository name/link].

## Fields To Fill Before Final Export

| File | Line/Section | Required Action |
|---|---|---|
| `Cover_Letter.md` | `[Submission date]` | Insert final submission date |
| `Cover_Letter.md` | Bracketed author approval / COI / supplement sentence | Insert final wording and remove bracketed placeholders |
| `Cover_Letter.md` | Signature block | Insert corresponding author details |
| `Response_to_Reviewers_Second_Revision.md` | `[Submission date]` | Insert final submission date |
| `Response_to_Reviewers_Second_Revision.md` | Signature block | Insert corresponding author name and final on-behalf wording |
| `Title_Page_Template.md` | Authors | Insert all author names, affiliations, and emails |
| `Title_Page_Template.md` | Corresponding Author | Insert corresponding author details |
| `Title_Page_Template.md` | Acknowledgments | Insert final statement |
| `Title_Page_Template.md` | Funding | Insert final statement |
| `Title_Page_Template.md` | Conflicts Of Interest | Insert final statement |
| `Title_Page_Template.md` | Data Availability | Finalize repository/submission-system wording |
| `AJPT_Title_Page.docx` | Title page fields | Regenerate or manually update after author details are final |
| `AJPT_Cover_Letter.docx` | Cover letter fields | Regenerate or manually update after author details are final |
| `AJPT_Response_to_Reviewers_Second_Revision.docx` | Response letter fields | Regenerate or manually update after author details are final |

## Final Placeholder Audit

Author-specific placeholders intentionally remain in the title-page template, cover-letter template, response-letter template, and DOCX build script. Manuscript table and figure callouts such as `[Insert Table 1 about here]` are not author placeholders and are handled by the DOCX build process. Do not upload final title-page, cover-letter, or response-letter DOCX files until the author-specific fields above have been completed and the DOCX files have been regenerated or manually updated.

## Reviewer-Facing Caution

Do not weaken the core boundary statements during final formatting. The title page, cover letter, manuscript, supplement, and replication README should remain consistent that the paper is a research-methodology contribution, the demonstration is a methodological protocol-validation exercise rather than a model-performance benchmark, XBRL is management-reported data rather than audit evidence, and preliminary audit-boundary diagnostics are author-coded diagnostics unless independently reviewed.
