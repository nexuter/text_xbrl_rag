# Independent Coder Process Documentation Revision Log

## Purpose

This log documents implementation of `SR-07`: expand independent coder-process documentation so reviewers can evaluate the measurement-validation procedure behind the 120-claim independent coding sample.

## Reviewer Concern Addressed

The revision addresses the concern that the claim-level coding protocol could depend too heavily on author judgment. The added documentation clarifies coder independence, author-code blinding, sample construction, materials supplied, variables coded, reconciliation procedures, and the boundary between measurement reliability and audit-judgment validation.

## Implemented Changes

1. Added `data/processed/coding/independent_coder_process_documentation.md`.
2. Copied the process documentation into the submission replication package.
3. Added Appendix Table F4A, "Independent Coder Process Documentation."
4. Revised the manuscript's independent-coding paragraph to disclose:
   - blank coding fields,
   - coder instructions/protocol/codebook/evidence packet,
   - no outside company research,
   - condition-label visibility,
   - measurement-consistency rather than blinded-treatment validation.
5. Revised coding-protocol language from `audit-valid` to audit-boundary or audit-judgment wording.
6. Updated replication README files to list the new process documentation.
7. Regenerated checksum manifests.

## Key Process Clarifications

| Issue | Clarification Added |
|---|---|
| Independence | Two coders completed the same 120-claim sample separately |
| Author-code blinding | Coders received blank coding fields and were not asked to copy or verify author codes |
| Condition visibility | Retrieval condition labels were visible because coders needed them for source-availability and integration coding |
| Outside information | Coders were instructed to rely on provided materials rather than outside company knowledge |
| Sample composition | 120 claims: all 89 hybrid-condition claims plus 31 non-hybrid anchors |
| Expert boundary | Coders validate measurement consistency; they are not represented as audit-domain expert validators unless separately documented |

## Reliability Evidence Preserved

- Claim segmentation agreement: 100.0 percent, Cohen's kappa = 1.000.
- Evidence-use type agreement: 100.0 percent, Cohen's kappa = 1.000.
- Integrated correctness agreement: 100.0 percent, weighted kappa = 1.000.
- Text-supported correctness agreement: 97.5 percent, weighted kappa = 0.919.
- Graph-valid correctness agreement: 99.2 percent, weighted kappa = 0.934.
- Claim-kind agreement: 97.5 percent, Cohen's kappa = 0.957.
- Confidence agreement: 87.5 percent, Cohen's kappa = 0.754.

## Files Updated

- `data/processed/coding/independent_coder_process_documentation.md`
- `data/processed/coding/independent_coding_protocol.md`
- `data/processed/coding/independent_coding_reconciliation_notes.md`
- `coder/CODING_PROTOCOL.md`
- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/data/processed/coding/independent_coder_process_documentation.md`
- `submission/replication_package/data/processed/coding/independent_coding_protocol.md`
- `submission/replication_package/data/processed/coding/independent_coding_reconciliation_notes.md`
- checksum manifests and summaries in root and submission replication package

## QA Notes

- Checksum manifests now report 414 files.
- The new process documentation is included in both root processed data and the submission replication package.
- Remaining audit-boundary language is framed as qualitative diagnostic or expert-validation boundary, not final audit-judgment evidence.

## Status

`SR-07` is complete.
