# Final Submission Bundle Map

## Purpose

This file maps the current project artifacts into a coherent AJPT submission package. It is intended to prevent the final submission from reading as a collection of project files and to make clear which materials belong in the main submission, online supplement, replication package, and internal support archive.

## Recommended Submission Format

Use a **separate-file format** for the current package:

1. Main manuscript with table and figure callouts.
2. Separate main-text tables and figures file.
3. Separate online supplement / appendix file.
4. Separate replication package README and data/code archive.

This is the safest current format because the main manuscript uses table and figure callouts. The tables and figures are prepared as a separate submission-facing file, and the appendix is prepared as a separate online supplement.

An integrated v4 manuscript should be created only if the journal, editor, or author team later requires a single combined file. The current package proceeds with the separate-file format.

## Primary Submission Files

| Submission Role | Current File | Submission Treatment | Status |
|---|---|---|---|
| Cover letter | `submission/AJPT_Cover_Letter.docx` | Finalize author/date/disclosure fields and submit as cover letter | Needs final author-specific details |
| Main manuscript | `submission/AJPT_Main_Manuscript.docx` | Submit as main manuscript draft, with tables/figures submitted separately | Ready after author review |
| Main-text tables and figures | `submission/Tables_and_Figures.md` | Submit as tables/figures file or append after manuscript references depending on journal format | Ready; DOCX export optional if journal requires |
| Online supplement / appendix | `submission/AJPT_Online_Supplement.docx` | Submit as online appendix/supplement | Ready after author review |
| Replication README | `submission/README_REPLICATION.md` | Include in replication/data package | Ready |
| Processed replication package | `submission/AJPT_Replication_Package_processed_only.zip` | Upload as data/code package if permitted | Ready |

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
| 5 | How were outputs coded into variables? | Online supplement Appendix F, including independent coding and hybrid mechanism diagnostics |
| 6 | Are selected examples source-traceable? | Online supplement Appendix G |
| 7 | Does the protocol apply across the six bounded-extension cases? | Online supplement Appendix H |
| 8 | What sensitivity and boundary diagnostics are included? | Online supplement Appendix I; replication sensitivity files |
| 9 | What should future researchers report? | Main manuscript Section VI; online supplement Appendix I |
| 10 | Can the package be reproduced or audited? | Replication README; scripts; data; checksums |

## Boundary Statements To Preserve Across Files

Every submitted file should preserve these boundaries:

1. The paper is a research-methodology paper, not an audit-practice system.
2. The demonstration is a full-scale nine-filer methodological protocol-validation exercise, not a performance benchmark.
3. XBRL is management-reported structured data, not audit evidence or ground truth.
4. Hybrid retrieval is construct-specific, not universally superior.
5. Audit-valid scores remain preliminary diagnostics unless independently reviewed by audit-domain experts.
6. Evidence-use type and integrated correctness have independent coding reliability evidence in the 120-claim validation sample.
7. The main evidence claim is claim-level evidence-use divergence, not retrieval accuracy or model capability.
8. Hybrid mechanism counts are protocol diagnostics, not population-level failure frequencies.
9. Context-volume and source-environment perturbation diagnostics are retrieval-stage diagnostics, not output-level robustness tests.

## Current Readiness Assessment By Component

| Component | Readiness | Remaining Action |
|---|---|---|
| Main manuscript | Near ready | Author review; ensure table/figure file is clearly attached |
| Tables and figures | Ready | Preserve Table 7 boundary note |
| Online supplement | Ready | Submit as separate supplement rather than project log |
| Replication README | Ready | Include with data/code package |
| Model metadata | Ready | Include as reproducibility note |
| Checksum manifest | Ready | Include if data/code package is shared |
| Cover letter | Draft ready | Fill author-specific declarations and final date |
| Reference list | Near ready | Verify recent working-paper status before submission |
| Independent coding | Ready for protocol-validation claim | Evidence-use type and integrated correctness have reliability evidence; audit-valid judgment remains boundary-only |

## Recommended Next Step

Finalize author-specific title page and cover letter fields next. If author details are not yet available, preserve placeholders and run one final cross-file consistency audit before upload.
