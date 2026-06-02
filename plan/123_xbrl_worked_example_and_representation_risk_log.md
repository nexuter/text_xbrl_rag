# XBRL Worked Example And Representation-Risk Revision Log

## Purpose

This log documents implementation of `SR-06`: add an XBRL worked example and representation-risk example so reviewers can see how the relational retrieval layer moves from raw XBRL artifacts to rendered context and claim-level coding.

## Reviewer Concern Addressed

The revision addresses the concern that XBRL relational retrieval could appear as a mechanical fact dump. The added example demonstrates source-to-claim traceability and shows why period, dimension, relation-role, and claim-type distinctions matter for retrieval-environment validity.

## Implemented Changes

1. Added a NKE inventory worked example artifact:
   - `data/processed/xbrl_coverage/xbrl_worked_example_nke_inventory.md`
2. Copied the worked example into the submission replication package.
3. Added Appendix Table C4, a source-to-claim trace for NKE inventory valuation.
4. Added Appendix Table C5, a period/dimension representation-risk example.
5. Revised the main manuscript to point readers to the worked example in Appendix C.
6. Updated replication README files to list `data/processed/xbrl_coverage/`.
7. Regenerated checksum manifests after adding the worked example.

## Worked Example Summary

The example traces:

- XBRL facts `F-NKE-0026` and `F-NKE-0027` for inventory valuation reserves;
- relation paths `X-NKE-0067` and `X-NKE-0015` linking the reserve concept to significant-accounting-policy structures;
- the rendered XBRL-only and hybrid retrieval contexts;
- claim `C021`, a graph-valid bounded factual claim;
- claim `C023`, a risk-cue claim that is only partly graph-valid because the risk inference exceeds XBRL facts alone;
- claim `C027`, an integrated factual hybrid claim;
- claim `C029`, an integrated risk-cue hybrid claim that remains an audit-boundary diagnostic rather than an audit conclusion.

## Representation-Risk Example

The representation-risk example uses NKE segment-level finished-goods inventory facts `F-NKE-0353`, `F-NKE-0354`, and `F-NKE-0355`. These facts are relevant to inventory balance and component coverage but are dated `instant:2023-05-31`. They should not be used as current 2025 segment-level inventory evidence. The example shows why period and dimension metadata must be preserved in rendered retrieval context and claim coding.

## Files Updated

- `data/processed/xbrl_coverage/xbrl_worked_example_nke_inventory.md`
- `submission/replication_package/data/processed/xbrl_coverage/xbrl_worked_example_nke_inventory.md`
- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `data/processed/checksums/checksum_manifest.csv`
- `data/processed/checksums/checksum_summary.md`
- `submission/replication_package/data/processed/checksums/checksum_manifest.csv`
- `submission/replication_package/data/processed/checksums/checksum_summary.md`

## QA Notes

- Checksum manifests now report 413 files.
- The worked example is included in the root processed data and in the submission replication package.
- The example preserves the paper's boundary: source traceability and representation checks do not establish audit evidence sufficiency.

## Status

`SR-06` is complete.
