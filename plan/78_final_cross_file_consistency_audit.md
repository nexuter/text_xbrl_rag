# Final Cross-File Consistency Audit

Revision note: This consistency audit was superseded by the full-scale extension revision in `plan/89_demonstration_scope_and_validation_revision_log.md`. The current submission package uses 72 outputs, 48 extension outputs, 281 preliminary coded claims, 464 retrieval-log rows, and 383 checksum rows.

## Purpose

This memo audits consistency across the final submission-facing materials:

1. main manuscript;
2. tables and figures packet;
3. online supplement;
4. replication README;
5. model metadata note;
6. checksum package;
7. cover letter template.

The audit checks whether the package uses consistent claims, counts, terminology, boundaries, and file-role descriptions.

## Audited Files

| File | Role |
|---|---|
| `plan/69_submission_ready_manuscript_v3.md` | Main manuscript |
| `plan/71_v3_main_tables_and_figures.md` | Main-text tables and figures |
| `plan/72_v3_appendix_supplement.md` | Online appendix/supplement |
| `README_REPLICATION.md` | Replication README |
| `plan/73_ollama_model_metadata_note.md` | Local model metadata note |
| `plan/74_checksum_manifest_package.md` | Checksum package note |
| `plan/77_final_cover_letter_submission_template.md` | Cover letter template |

## Consistency Verdict

The final submission-facing package is internally consistent after two cleanup revisions:

1. the manuscript appendix index was updated to match the supplement's section-based appendix table numbering;
2. the replication README was revised so internal reviewer-stress-test materials are not listed as main manuscript package files.

The remaining issues are not consistency problems. Two are final submission decisions and one has been resolved in the subsequent audit-validity strategy memo:

1. whether to submit tables and figures as a separate file or embed them in a v4 manuscript;
2. whether to preserve boundary-only audit-valid coding or add limited expert review, resolved by `plan/79_audit_validity_strategy_decision.md` in favor of the boundary-only path for the current submission package;
3. whether to update recent working-paper reference statuses immediately before submission.

## Count Consistency

| Item | Manuscript | Tables/Figures | Supplement | README | Status |
|---|---:|---:|---:|---:|---|
| Main outputs | 24 | Implied in Figure 2 | 24 | 24 | Consistent |
| Extension outputs | 18 | Implied in Figure 2 | 18 | 18 | Consistent |
| Total outputs | 42 | Implied in Figure 2 | 42 | 42 | Consistent |
| Main coded claims | 94 | Not applicable | 94 | 94 | Consistent |
| Extension coded claims | 88 | Not applicable | 88 | 88 | Consistent |
| Total coded claims | 182 | Table 7 note | 182 | 182 | Consistent |
| Hybrid claims using both sources | 7 of 60 | Noted as evidence-use divergence | 7 of 60 | Not applicable | Consistent |
| Hybrid text-only claims | 41 | Noted in manuscript/supplement | 41 | Not applicable | Consistent |
| Hybrid XBRL-only claims | 12 | Noted in manuscript/supplement | 12 | Not applicable | Consistent |
| Text chunk rows | Not main-text count | Not applicable | 1,377 | 1,377 | Consistent |
| XBRL fact rows | Not main-text count | Not applicable | 2,566 | 2,566 | Consistent |
| XBRL relation-path rows | Not main-text count | Not applicable | 1,619 | 1,619 | Consistent |
| Retrieval log rows | Not main-text count | Not applicable | 313 | 313 | Consistent |
| Checksum manifest rows | Not applicable | Not applicable | Not applicable | 1,379 | Consistent with checksum package |

## Boundary-Language Consistency

| Boundary | Manuscript | Tables/Figures | Supplement | README | Cover Letter | Status |
|---|---|---|---|---|---|---|
| Methodology paper, not audit-practice tool | Yes | Implied | Yes | Yes | Yes | Consistent |
| Demonstration, not benchmark | Yes | Yes | Yes | Yes | Yes | Consistent |
| XBRL is not audit evidence or ground truth | Yes | Yes | Yes | Yes | Yes | Consistent |
| Hybrid retrieval is not universally superior | Yes | Yes | Yes | Yes | Implied | Consistent |
| Audit-valid/integrated scores are preliminary | Yes | Yes | Yes | Yes | Implied | Consistent |
| `gemma4:31b` is not claimed superior | Yes | Yes | Yes | Yes | Implied | Consistent |
| Vector/RDF/GraphRAG are not completed benchmarks | Yes | Yes | Yes | Yes | Implied | Consistent |

## Terminology Consistency

| Term | Package Treatment | Status |
|---|---|---|
| Retrieval-environment validity | Central construct throughout | Consistent |
| Text retrieval | Keyword-ranked contextual retrieval in the demonstration; vector retrieval as future reporting guidance | Consistent |
| XBRL relational retrieval | Table-based fact/path retrieval in the demonstration; RDF/OWL as portability guidance | Consistent |
| Hybrid retrieval | Construct-specific narrative-numeric integration condition | Consistent |
| Claim-level coding | Unit of output-to-variable construction | Consistent |
| Audit-valid correctness | Requires expert judgment for stronger claims | Consistent |
| Integrated correctness | Requires actual use of both evidence types, not merely hybrid prompt availability | Consistent |

## Cleanup Actions Completed During Audit

### 1. Appendix Table Numbering

Issue:

The manuscript appendix index used an older `A1`, `A2`, `A8`, `A9`, `A10` table-numbering scheme, while the final supplement uses section-based numbering such as `F1`, `F2`, `H1`, and `I5`.

Resolution:

Updated `plan/69_submission_ready_manuscript_v3.md` so:

- failure-mode taxonomy points to Appendix Table F2;
- claim-level coding scope and preliminary coding summary point to Appendix Tables F1-F3;
- bounded-extension materials point to Appendix Tables H1-H5;
- sensitivity and reproducibility materials point to Appendix Tables I1-I5.

### 2. Replication README File-Role Description

Issue:

`README_REPLICATION.md` listed `plan/70_v3_reviewer_stress_test.md` under "Main Manuscript Package Files," which could imply that an internal stress-test memo belongs in the submitted manuscript package.

Resolution:

Renamed the section to "Manuscript And Supplement Package Files" and removed the internal stress-test file. Added `plan/74_checksum_manifest_package.md` as a reproducibility-support file.

## Remaining Non-Consistency Decisions

### 1. Separate Tables/Figures File Versus Integrated V4

Current state:

The manuscript contains callouts, and `plan/71_v3_main_tables_and_figures.md` contains the final tables and figures.

Recommendation:

Separate-file format remains acceptable and safest. If a v4 manuscript is created later, it should embed or append the same tables without changing titles, notes, or boundary statements.

### 2. Boundary-Only Audit-Validity Path Versus Limited Expert Review

Current state:

All files consistently state that audit-valid and integrated scores are preliminary author-coded diagnostics.

Recommendation:

Boundary-only is defensible for the current methodology paper. This path is adopted for the current submission package in `plan/79_audit_validity_strategy_decision.md`. Limited expert review would strengthen credibility but is not required unless the manuscript begins making stronger audit-judgment claims.

### 3. Recent Reference Status

Current state:

Recent and working-paper references are internally consistent.

Recommendation:

Recheck publication status immediately before actual submission because LLM/RAG audit-system literature is moving quickly.

## Final Reviewer-Facing Assessment

The package now reads as one coherent submission bundle. The manuscript states the contribution; the tables and figures operationalize it; the supplement provides the source-to-context-to-output-to-claim evidence trail; the README provides replication orientation; the model metadata and checksum files support reproducibility boundaries; and the cover letter frames the paper for the AJPT Methodological Papers call.

No material cross-file inconsistency remains that would prevent submission preparation.
