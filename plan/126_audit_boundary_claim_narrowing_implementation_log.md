# Audit-Boundary Claim-Narrowing Implementation Log

## Purpose

This log documents implementation of `SR-08`: resolve the audit-boundary validation gate and apply the decision consistently across the manuscript, supplement, replication README, and coding documentation.

## Gate Decision

The revision adopts **claim narrowing rather than new audit-domain expert coding**.

Audit-boundary notes remain qualitative preliminary diagnostics. They identify where public filing text and management-reported XBRL support may end, but they are not final audit-judgment labels, audit evidence sufficiency findings, model-performance outcomes, or retrieval-method superiority evidence.

## Implemented Changes

1. Added `plan/125_gate_a_audit_boundary_validation_decision_memo.md`.
2. Copied the Gate A memo into `submission/replication_package/docs/`.
3. Added Appendix Table F4B, "Gate Decision For Audit-Boundary Validation."
4. Revised the main manuscript to state that the paper adopts a claim-narrowing approach for audit-boundary coding.
5. Revised replication README files to explain that legacy `audit_valid_prelim` columns should be interpreted as preliminary audit-boundary diagnostics.
6. Replaced sentence-level `audit-valid` wording in coding summaries and inference-shift diagnostics with audit-boundary terminology.
7. Regenerated checksum manifests.

## Files Updated

- `plan/125_gate_a_audit_boundary_validation_decision_memo.md`
- `submission/replication_package/docs/125_gate_a_audit_boundary_validation_decision_memo.md`
- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `data/processed/coding/claim_coding_summary.md`
- `data/processed/coding/claim_coding_summary_gemma4_31b.md`
- `data/processed/coding/claim_coding_summary_gemma4_31b_extension.md`
- `data/processed/coding/manuscript_selected_claim_table.md`
- `data/processed/coding/inference_shift_table_prelim*.csv`
- matching submission replication package coding files
- checksum manifests and summaries in root and submission replication package

## Column-Name Boundary

The processed claim-level CSV files retain legacy columns such as `audit_valid_prelim` and `audit_valid_rationale` for reproducibility with earlier scripts. The README and supplement now state that these fields should be read as preliminary audit-boundary diagnostics, not final audit-judgment labels.

## QA Notes

- Checksum manifests remain at 414 files.
- The core manuscript now states the claim-narrowing decision explicitly.
- Appendix F includes a dedicated gate-decision table.
- Replication README files explain legacy `audit_valid_*` column names.

## Status

`SR-08` is complete.
