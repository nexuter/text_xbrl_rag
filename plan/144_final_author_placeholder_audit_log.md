# Final Author Placeholder Audit Log

Date: 2026-06-01

## Purpose

This log documents SR-18 of the second-revision workflow. The goal was to identify which placeholders can be resolved by Codex and which require final author-team information before resubmission.

## Status

Codex-side audit is complete. Final resolution requires author-provided information.

## Author-Specific Placeholders Still Needed

The following fields should remain unresolved until the author team provides final submission information:

- submission date;
- full author names;
- author affiliations;
- author emails;
- corresponding-author name;
- corresponding-author affiliation;
- corresponding-author email;
- corresponding-author mailing address and phone, if required by the journal;
- acknowledgments;
- funding statement;
- conflict-of-interest statement;
- final data-availability wording and repository decision;
- final supplemental-materials statement;
- final generative-AI disclosure wording if the submission system has a separate field.

## Files Containing Intentional Author Placeholders

- `submission/Title_Page_Template.md`
- `submission/Cover_Letter.md`
- `submission/Author_Information_Checklist.md`
- `submission/00_SUBMISSION_README.md`
- `submission/FINAL_SUBMISSION_FILE_LIST.md`
- `submission/replication_package/scripts/build_ajpt_submission_docx.ps1`

The DOCX build script still contains placeholder title-page fields because those values are not available. The script should be updated or the generated DOCX files should be manually edited once final author information is available.

## Non-Author Placeholders That Are Not Problems

The main manuscript contains table and figure callouts such as `[Insert Table 1 about here]` and `[Insert Figure 1 about here]`. These are manuscript composition callouts, not missing author data. The DOCX build script skips those callouts and inserts tables and figures separately.

## Revision Made In This Step

1. Updated the cover letter wording from `tiered reporting standard` to `tiered reporting guidance` and `reproducibility standards` to match the revised manuscript.
2. Replaced bracketed cover-letter alternatives with explicit final-action placeholders for author approval, conflict/disclosure, and supplemental-materials language.
3. Added repository/raw-source archive decision to the author checklist.
4. Added a final placeholder audit note to the author checklist.
5. Marked SR-18 in the second-revision plan as `Author action required` rather than fully completed.

## Pre-Upload Requirement

Before final upload:

1. Fill `Title_Page_Template.md` and `Cover_Letter.md`.
2. Update `build_ajpt_submission_docx.ps1` author fields or manually edit the generated DOCX files.
3. Regenerate or update:
   - `AJPT_Title_Page.docx`;
   - `AJPT_Cover_Letter.docx`;
   - any final submission package zip if file contents change.
4. Run one final placeholder search excluding manuscript table/figure callouts.

