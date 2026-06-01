# Post-Revision Polish Implementation Log

## Purpose

This log records implementation of the remaining improvements identified in `plan/110_post_revision_strict_reviewer_assessment.md`.

## Implemented Revisions

1. Revised the abstract to report the current evidence package: nine filers, 72 retrieval-conditioned outputs, 281 preliminary coded claims, and a 120-claim independent coding sample.
2. Softened the early contribution paragraph from "audit-valid correctness" to "preliminary audit-valid boundary diagnostics."
3. Added a main-text sentence explaining that the 31 non-hybrid comparison claims provide LLM-only, text-only, and XBRL-only anchors for applying source-use and correctness scales outside the hybrid condition.
4. Added the same non-hybrid anchor explanation to the root, submission, and replication-package READMEs.
5. Clarified in the online supplement that automated validation checks source-ID resolvability across the output set, while selected spot checks illustrate substantive source-to-claim traceability.
6. Added processed-only archive guidance to the README folder maps, explaining that `data/raw_sec/` is excluded by default and reconstructable from SEC EDGAR using the download script and accession metadata.
7. Removed the internal `Submission-Ready Manuscript Draft v3` label from the submission-facing and plan manuscript Markdown files.
8. Captured available local Ollama provenance:
   - `ollama show gemma4:31b` did not expose a full model digest or local model-file hash.
   - `ollama list` reported local model ID `6316f0629137`.
   - The model metadata note now records this ID and states the remaining digest boundary explicitly.
9. Copied the revised model metadata note into the replication package documentation.
10. Regenerated AJPT DOCX files and reran Word COM structural QA.

## DOCX QA After Revision

| File | Pages | Words | Tables | Required Markers |
|---|---:|---:|---:|---|
| `AJPT_Cover_Letter.docx` | 3 | 621 | 0 | Present |
| `AJPT_Main_Manuscript.docx` | 38 | 9,456 | 8 | Present |
| `AJPT_Online_Supplement.docx` | 19 | 4,778 | 27 | Present |
| `AJPT_Title_Page.docx` | 2 | 205 | 0 | Not expected |

## Remaining Boundary

The package still does not claim Tier 2 model-performance validation, audit-domain expert coding, matched-budget experiments, cross-model validation, or exact deterministic third-party LLM output reproduction. The model provenance is improved through the Ollama list ID and metadata note, but a full model digest or local model-file hash remains unavailable from the captured local commands.
