# Final Submission Bundle Map

## Purpose

This file maps the current project artifacts into a coherent AJPT submission package. It is intended to prevent the final submission from reading as a collection of project files and to make clear which materials belong in the main submission, online supplement, replication package, and internal support archive.

## Recommended Submission Format

Use a **separate-file format** for the current package:

1. Main manuscript with table and figure callouts.
2. Separate main-text tables and figures file.
3. Separate online supplement / appendix file.
4. Separate replication package README and data/code archive.

This is the safest current format because `plan/69_submission_ready_manuscript_v3.md` still contains table and figure callouts. The tables and figures are fully prepared in `plan/71_v3_main_tables_and_figures.md`, and the appendix is fully prepared in `plan/72_v3_appendix_supplement.md`.

An integrated v4 manuscript should be created only if the journal, editor, or author team later requires a single combined file. The current package proceeds with the separate-file format.

## Primary Submission Files

| Submission Role | Current File | Submission Treatment | Status |
|---|---|---|---|
| Cover letter | `plan/58_cover_letter_draft_ajpt_methodological_call.md` | Finalize author/date/disclosure fields and submit as cover letter | Needs final author-specific details |
| Main manuscript | `plan/69_submission_ready_manuscript_v3.md` | Submit as main manuscript draft, with tables/figures submitted separately | Ready after final formatting check |
| Main-text tables and figures | `plan/71_v3_main_tables_and_figures.md` | Submit as tables/figures file or append after manuscript references depending on journal format | Ready |
| Online supplement / appendix | `plan/72_v3_appendix_supplement.md` | Submit as online appendix/supplement | Ready |
| Replication README | `README_REPLICATION.md` | Include in replication/data package | Ready |

## Supporting Reproducibility Files

| Component | File Or Folder | Submission Role | Status |
|---|---|---|---|
| Filer manifest | `config/filer_manifest.json` | Replication package | Ready |
| Raw SEC data | `data/raw_sec/` | Replication package or retained archive, subject to file-size policy | Ready |
| Processed data | `data/processed/` | Replication package | Ready |
| Pipeline scripts | `scripts/` | Replication package | Ready |
| Model metadata note | `plan/73_ollama_model_metadata_note.md` | Replication package documentation or supplement support | Ready |
| Checksum note | `plan/74_checksum_manifest_package.md` | Replication package documentation | Ready |
| Checksum manifest | `data/processed/checksums/checksum_manifest.csv` | Replication package integrity file | Ready |
| Checksum summary | `data/processed/checksums/checksum_summary.md` | Replication package integrity summary | Ready |

## Internal Support Files

The following files are useful for author review and response preparation but should not normally be submitted as standalone manuscript materials.

| File | Role |
|---|---|
| `plan/70_v3_reviewer_stress_test.md` | Internal reviewer stress test |
| `plan/75_overall_progress_and_reinforcement_review.md` | Internal progress and reinforcement review |
| `plan/59_likely_reviewer_concerns_response_package.md` | Source for future response-to-reviewers language |
| `plan/60_final_reference_package.md` | Internal reference and citation strategy |
| `plan/64_accept_level_reviewer_assessment.md` | Internal accept-level readiness assessment |
| `plan/67_final_reproducibility_materials_check.md` | Internal reproducibility verification |

## Final File Naming Recommendation

Before actual submission, create clean copies or exported versions using submission-facing names:

| Current File | Suggested Submission Name |
|---|---|
| `plan/69_submission_ready_manuscript_v3.md` | `Manuscript_Retrieval_as_Research_Design.docx` or `.pdf` |
| `plan/71_v3_main_tables_and_figures.md` | `Tables_and_Figures.docx` or `.pdf` |
| `plan/72_v3_appendix_supplement.md` | `Online_Supplement_Appendix.docx` or `.pdf` |
| `README_REPLICATION.md` | `README_REPLICATION.md` |
| `plan/58_cover_letter_draft_ajpt_methodological_call.md` | `Cover_Letter.docx` or `.pdf` |

## Submission Package Logic For Reviewers

The submitted materials should make this evidence trail visible:

| Step | Reviewer Question | Submission Location |
|---|---|---|
| 1 | What is the methodological contribution? | Main manuscript |
| 2 | How is retrieval-environment validity defined and operationalized? | Main manuscript; Tables 1-6 |
| 3 | What does the demonstration show? | Main manuscript; Figure 2; Table 7 |
| 4 | What did the LLM actually see? | Online supplement Appendix D |
| 5 | How were outputs coded into variables? | Online supplement Appendix F |
| 6 | Are selected examples source-traceable? | Online supplement Appendix G |
| 7 | Does the protocol apply beyond three cases? | Online supplement Appendix H |
| 8 | What should future researchers report? | Main manuscript Section VI; online supplement Appendix I |
| 9 | Can the package be reproduced or audited? | Replication README; scripts; data; checksums |

## Boundary Statements To Preserve Across Files

Every submitted file should preserve these boundaries:

1. The paper is a research-methodology paper, not an audit-practice system.
2. The demonstration is descriptive and methodological, not a performance benchmark.
3. XBRL is management-reported structured data, not audit evidence or ground truth.
4. Hybrid retrieval is construct-specific, not universally superior.
5. Audit-valid and integrated scores are preliminary author-coded diagnostics unless independently reviewed.
6. The main evidence claim is claim-level evidence-use divergence, not retrieval accuracy or model capability.

## Current Readiness Assessment By Component

| Component | Readiness | Remaining Action |
|---|---|---|
| Main manuscript | Near ready | Final formatting check; ensure table/figure file is clearly attached |
| Tables and figures | Ready | Preserve Table 7 boundary note |
| Online supplement | Ready | Submit as separate supplement rather than project log |
| Replication README | Ready | Include with data/code package |
| Model metadata | Ready | Include as reproducibility note |
| Checksum manifest | Ready | Include if data/code package is shared |
| Cover letter | Draft ready | Fill author-specific declarations and final date |
| Reference list | Near ready | Verify recent working-paper status before submission |
| Expert coding | Boundary-only ready | Use boundary-only strategy for current submission; limited expert review remains optional |

## Recommended Next Step

Finalize author-specific title page and cover letter fields next. If author details are not yet available, proceed to final format conversion planning while keeping placeholders visible.

After that, run a final cross-file consistency audit to ensure the manuscript, tables/figures file, supplement, README, model metadata note, and checksum package all use the same claims, counts, and boundaries.
