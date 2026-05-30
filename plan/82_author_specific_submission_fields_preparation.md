# Author-Specific Submission Fields Preparation

## Purpose

This step prepares the author-specific submission fields that cannot be completed from the current project files alone. The goal is to make the next author-input step mechanical rather than interpretive.

## Reviewer-Relevant Rationale

The author and disclosure fields are not only administrative. They also affect reviewer interpretation of the paper's transparency claims. The title page, cover letter, data availability statement, AI disclosure, and replication package statement should be consistent with the manuscript's methodological positioning.

## Completed Work

Created:

- `submission/Author_Information_Checklist.md`

Reviewed:

- `submission/Title_Page_Template.md`
- `submission/Cover_Letter.md`
- `submission/00_SUBMISSION_README.md`

## Current Status

The author-specific step cannot be fully completed without author-provided information. The remaining fields are:

| Field | Status | Notes |
|---|---|---|
| Submission date | Needed | Should reflect actual journal upload date |
| Full author list | Needed | Required for title page and submission system |
| Author affiliations and emails | Needed | Required for title page and submission system |
| Corresponding author details | Needed | Required for cover letter and title page |
| Acknowledgments | Needed | Use "none" language if no acknowledgments |
| Funding statement | Needed | Use no-funding language only if true |
| Conflict-of-interest statement | Needed | Use no-conflict language only if true |
| Data availability statement | Partly drafted | Final wording depends on repository and raw SEC file upload policy |
| AI disclosure | Drafted | Confirm against the journal's submission-system field |

## Recommended Defaults If Factually Accurate

- Author approval: "All authors have approved the submission."
- Conflict of interest: "The authors have no conflicts of interest to disclose."
- Funding: "The authors received no specific funding for this work."
- Data availability: "Replication materials include the filer manifest, extraction and retrieval scripts, processed text and XBRL retrieval artifacts, rendered prompts, raw LLM outputs, claim-level coding files, model metadata, and checksum files. Raw SEC filings are publicly available from the SEC EDGAR system. Repository details will be provided upon acceptance or as required by the journal."

## Completion Criteria

This step will be complete when:

1. `submission/Title_Page_Template.md` has been converted into a final title page.
2. `submission/Cover_Letter.md` has no bracketed placeholders.
3. The data availability statement matches the final repository or submission-system policy.
4. The AI disclosure is consistent across the manuscript, title page, and submission system.

## Next Step

Collect the author-specific information and update the title page and cover letter. If those details are not yet available, proceed to the optional integrated manuscript decision or final format conversion while keeping the placeholders visible.
