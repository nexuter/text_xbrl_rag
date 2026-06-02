# Literature, Terminology, And Title Cleanup Log

Date: 2026-06-01

## Purpose

This log documents the Workstream 10 cleanup for the second-revision package. The goal was to remove avoidable credibility risks before the next submission by aligning the title, citation status, terminology, and submission-facing package language with the actual implemented methodology.

## Changes Implemented

1. Revised the submission-facing title from:

   `Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval`

   to:

   `Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval`

   Rationale: "XBRL-Augmented" could suggest a stronger ontology, graph database, or performance-improvement claim than the current implementation supports. "XBRL Relational Retrieval" better matches the implemented fact/path retrieval environment and the paper's construct-validity contribution.

2. Updated submission-facing files and DOCX generation script so future regenerated files use the revised title consistently.

3. Rechecked RAG/RAG evaluation citations. The manuscript already reflects the updated proceedings status for:

   - Es, James, Espinosa-Anke, and Schockaert (2024), RAGAS, EACL System Demonstrations.
   - Saad-Falcon, Khattab, Potts, and Zaharia (2024), ARES, NAACL Human Language Technologies.

   Rationale: leaving these as arXiv-only references would create an avoidable reviewer credibility issue because both now have ACL Anthology proceedings records.

4. Softened submission-facing audit-validity wording:

   - Replaced "preliminary audit-valid boundary language" with "preliminary audit-boundary language."
   - Replaced a checklist statement about "audit-valid scores" with "preliminary audit-boundary diagnostics."

   Rationale: the paper should not imply that author-coded diagnostics validate audit correctness. The current evidence supports protocol diagnostics and independently coded evidence-use/integration measures, not final audit-validity judgments.

5. Confirmed unresolved author-specific placeholders remain intentionally unresolved:

   - submission date;
   - author names and affiliations;
   - corresponding-author details;
   - conflict-of-interest statement;
   - funding statement;
   - final data availability and generative-AI disclosure wording.

## Files Updated

- `submission/FINAL_SUBMISSION_FILE_LIST.md`
- `submission/replication_package/scripts/build_ajpt_submission_docx.ps1`
- `submission/AJPT_DOCX_Format_Audit.md`
- `submission/Author_Information_Checklist.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## Verification

Search checks were run for:

- stale title wording in submission-facing files;
- old arXiv-only RAGAS/ARES reference wording;
- risky "audit-valid scores" language;
- unresolved author-specific placeholders.

Known remaining placeholders are restricted to author/submission metadata and are documented in the submission README and author checklist.

## Source Status Notes

- RAGAS proceedings record: https://aclanthology.org/2024.eacl-demo.16/
- ARES proceedings record: https://aclanthology.org/2024.naacl-long.20/

