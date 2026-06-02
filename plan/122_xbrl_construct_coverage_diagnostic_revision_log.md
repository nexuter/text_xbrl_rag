# XBRL Construct-Coverage Diagnostic Revision Log

## Purpose

This log documents implementation of `SR-05` from the second-revision workflow: build an XBRL concept/relation coverage diagnostic that shows whether the XBRL retrieval environment aligns with the ex ante revenue and inventory construct protocols before LLM outputs are interpreted.

## Reviewer Concern Addressed

The diagnostic addresses the second-round concern that XBRL relational retrieval is central to the manuscript but could appear under-validated as a measurement layer. The revision makes the XBRL retrieval layer inspectable at the construct-family level rather than relying only on aggregate fact/path counts.

## Implemented Changes

1. Added `scripts/analyze_xbrl_construct_coverage.py`.
2. Generated:
   - `data/processed/xbrl_coverage/construct_coverage_by_filer.csv`
   - `data/processed/xbrl_coverage/construct_coverage_by_family.csv`
   - `data/processed/xbrl_coverage/xbrl_construct_coverage_summary.md`
3. Copied the script and outputs into the submission replication package.
4. Added Appendix Table C2, an 18-cell construct-filer coverage diagnostic.
5. Added Appendix Table C3, a concept-family coverage diagnostic.
6. Revised the main manuscript to explain why construct-family coverage must be checked before interpreting XBRL-conditioned LLM outputs.
7. Revised Table 6 to include ex ante XBRL concept-family coverage checks as part of construct-to-retrieval mapping.
8. Updated replication README files to document the new diagnostic step.

## Diagnostic Results

- Construct-filer cells reviewed: 18.
- Complete expected-family coverage cells: 3.
- Partial expected-family coverage cells: 15.
- Revenue or sales amount coverage: 9/9 filers.
- Revenue disaggregation or customer-dimension coverage: 9/9 filers.
- Revenue refunds, returns, or variable-consideration coverage: 3/9 filers.
- Inventory balance coverage: 9/9 filers.
- Inventory components coverage: 4/9 filers.
- Inventory movements coverage: 4/9 filers.

## Interpretation Boundary

The diagnostic supports retrieval-environment validity and construct alignment. It does not support model-performance validation, audit evidence sufficiency, misstatement detection, or claims that missing concept families are absent from a filing. Missing concept-family coverage is treated as a retrieval-design boundary condition.

## Files Updated

- `scripts/analyze_xbrl_construct_coverage.py`
- `data/processed/xbrl_coverage/construct_coverage_by_filer.csv`
- `data/processed/xbrl_coverage/construct_coverage_by_family.csv`
- `data/processed/xbrl_coverage/xbrl_construct_coverage_summary.md`
- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/Tables_and_Figures.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/scripts/analyze_xbrl_construct_coverage.py`
- `submission/replication_package/data/processed/xbrl_coverage/construct_coverage_by_filer.csv`
- `submission/replication_package/data/processed/xbrl_coverage/construct_coverage_by_family.csv`
- `submission/replication_package/data/processed/xbrl_coverage/xbrl_construct_coverage_summary.md`
- `data/processed/checksums/checksum_manifest.csv`
- `data/processed/checksums/checksum_summary.md`
- `submission/replication_package/data/processed/checksums/checksum_manifest.csv`
- `submission/replication_package/data/processed/checksums/checksum_summary.md`

## QA Notes

- The script passed Python AST parsing.
- The diagnostic was generated from `retrieval_log.csv`, `xbrl_facts.csv`, and `xbrl_paths.csv`.
- The manuscript wording frames the results as retrieval-design diagnostics, not as evidence of LLM superiority or final audit-judgment correctness.
- Checksum manifests were regenerated after adding the coverage script and three coverage outputs; each manifest now reports 412 files.

## Status

`SR-05` is complete.
