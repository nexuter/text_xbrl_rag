# Strict Reviewer Gap Revision Log

## Purpose

This log records the implementation of the strict reviewer gap checklist in `plan/108_strict_reviewer_gap_review_and_improvement_checklist.md`.

## Implemented Revisions

1. Corrected checksum manifest expected counts from 387 to 408 in:
   - root `README_REPLICATION.md`;
   - `submission/README_REPLICATION.md`;
   - `submission/replication_package/README_REPLICATION.md`.
2. Added first-page boundary language clarifying that the implemented prototype uses keyword-ranked text chunks and table-based XBRL fact/path retrieval, while vector indexes, RDF/OWL stores, graph databases, and GraphRAG remain guidance or portability extensions.
3. Strengthened the independent-coding paragraph by explaining why the 120-claim validation sample intentionally includes all 89 hybrid-condition claims and by clarifying that independent coding validates source-use and integration coding, not audit-domain expert judgment.
4. Replaced broad "no invalid source references" wording with "no unresolved source identifiers" and clarified that source-ID resolution is not audit-inference validation.
5. Replaced overstrong separability wording with a narrower statement that context-volume and source-environment perturbation diagnostics improve separability and source-composition transparency without replacing matched-budget, evidence-order, prompt-sensitivity, or output-level robustness tests.
6. Added a stability boundary: the demonstration provides stronger evidence for traceability, representation, separability documentation, and claim-level evidence-use coding than for temporal or stochastic retrieval stability.
7. Updated the online supplement closing note so it no longer says replication README or checksums still need to be added.
8. Updated the Ollama model metadata note to reflect the full-scale 48-output extension run rather than the earlier 18-output extension archive.
9. Copied the updated model metadata note into the replication package documentation.
10. Regenerated the AJPT DOCX files and reran DOCX structural QA.

## DOCX QA After Revision

| File | Pages | Words | Tables | Required Markers |
|---|---:|---:|---:|---|
| `AJPT_Cover_Letter.docx` | 3 | 621 | 0 | Present |
| `AJPT_Main_Manuscript.docx` | 38 | 9,456 | 8 | Present |
| `AJPT_Online_Supplement.docx` | 19 | 4,778 | 27 | Present |
| `AJPT_Title_Page.docx` | 2 | 205 | 0 | Not expected |

## Remaining Reviewer Boundary

The paper remains a Tier 1 methodological protocol-validation paper. The revision improves claim discipline but does not add Tier 2 model-output robustness, audit-domain expert coding, matched-budget experiments, or cross-model validation.
