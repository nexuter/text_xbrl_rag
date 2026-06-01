# Integrated-Correctness Consistency Revision Log

## Purpose

This log records the revision made after the final reviewer-style audit identified a high-risk inconsistency between the independent-coder rule for `integrated_code` and the preliminary author-coded manuscript summaries.

## Reviewer Risk Addressed

The prior draft risked implying that a hybrid-condition claim supported by only one evidence layer should receive partial integrated credit. That would conflict with the coder-facing rule: integration requires text and XBRL to be used together in an inferential bridge. One-layer use in a hybrid condition is evidence-use information, but it is not integrated evidence use.

## Implemented Changes

1. Revised `scripts/code_llm_claims.py` so hybrid one-layer claims receive `integrated_prelim = 0`, not `0.5`.
2. Kept `integrated_prelim = 1` only when a claim jointly uses text and XBRL in a coherent inferential bridge.
3. Kept `integrated_prelim = 0.5` only for weak or juxtaposed text-XBRL use; the current regenerated outputs contain no such author-preliminary cases.
4. Removed aggregate `integrated_prelim_mean` reporting from condition summaries.
5. Replaced mean-style integrated summaries with bridge-count diagnostics:
   - `integrated_bridge_claims`
   - `integrated_bridge_share`
   - `weak_or_juxtaposed_claims`
   - `text_only_hybrid_claims`
   - `xbrl_only_hybrid_claims`
   - `no_source_hybrid_claims`
6. Updated manuscript-facing selected-claim examples so one-source hybrid claims no longer show partial integrated credit.
7. Updated the online supplement and plan copies to report integrated bridge counts and shares rather than integrated means.
8. Copied the revised script and processed coding outputs into the processed-only replication package.
9. Regenerated the AJPT DOCX files and reran Word COM structural QA.
10. Regenerated the processed-data checksum manifest and rebuilt `submission/AJPT_Replication_Package_processed_only.zip`.
11. Ran final machine QA confirming that:
    - main hybrid claims have integrated counts `0 = 27`, `1 = 3`, and no `0.5`;
    - extension hybrid claims have integrated counts `0 = 54`, `1 = 5`, and no `0.5`;
    - condition summary files use bridge-count columns and no longer include `integrated_prelim_mean`;
    - main DOCX Table 8 examples E02, E03, and E05 report integrated diagnostic `0`;
    - the online supplement DOCX reports `Integrated Bridge Claims` and no longer reports `Integrated Mean`;
    - the processed-only replication zip contains the revised coding script and bridge-summary outputs.

## Updated Author-Preliminary Hybrid Integration Results

| Sample | Hybrid Claims | Integrated Bridge Claims | Integrated Bridge Share | One-Layer or No-Source Hybrid Claims |
|---|---:|---:|---:|---:|
| Main deep cases | 30 | 3 | 10.0% | 27 |
| Full-scale extension | 59 | 5 | 8.5% | 54 |
| Total | 89 | 8 | 9.0% | 81 |

## DOCX QA After Revision

| File | Pages | Words | Tables |
|---|---:|---:|---:|
| `AJPT_Cover_Letter.docx` | 3 | 621 | 0 |
| `AJPT_Main_Manuscript.docx` | 38 | 9,456 | 8 |
| `AJPT_Online_Supplement.docx` | 19 | 4,778 | 27 |
| `AJPT_Title_Page.docx` | 2 | 205 | 0 |

## Reviewer-Facing Interpretation

The corrected result sharpens the paper's contribution. The paper no longer appears to award partial integration for merely placing text and XBRL retrieval in the same prompt condition. Instead, it shows that the protocol can detect a substantive one-layer-use problem: hybrid retrieval often changes the available source environment without necessarily causing the model to integrate narrative and XBRL evidence in individual claims. This is a stronger methodological contribution because it turns retrieval design into an auditable variable-construction and validity problem rather than a broad claim about model superiority.

## Remaining Boundary

These integrated-bridge counts remain author-preliminary diagnostics for the full 281-claim output set. The independently coded 120-claim validation sample supports the reliability of the coding categories, while final audit-valid performance claims would still require a Tier 2 design with expert audit coding, broader sampling, and prompt/retrieval sensitivity checks.
