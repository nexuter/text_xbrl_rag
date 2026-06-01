# Recoded Independent Coding Application Log

## Purpose

This log documents application of the revised independent-coding results after both coders recoded the 120-claim validation sample under the updated `integrated_code` instruction.

## Inputs

- `coder/coder_1_completed_coding_form.csv`
- `coder/coder2_completed_coding_form.csv`

## Generated Authoritative Outputs

- `data/processed/coding/independent_coding_results.csv`
- `data/processed/coding/independent_coding_disagreements.csv`
- `data/processed/coding/intercoder_reliability_summary.md`
- `data/processed/coding/independent_coding_reconciliation_notes.md`

The same updated files were copied into `submission/replication_package/data/processed/coding/`.

## Updated Reliability Results

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Manuscript And Package Files Updated

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/Replication_Package_Manifest.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`
- `submission/replication_package/AUTHORITATIVE_FILES.md`
- `README_REPLICATION.md`

## Reviewer-Facing Interpretation

The recoded evidence strengthens the methodological contribution because the core retrieval-validity variables now show very high reliability, including 100.0 percent agreement for evidence-use type and integrated correctness. The revised `integrated_code` rule eliminates the prior `0` versus `NA` ambiguity: ordinary non-integration is coded as `0`, while `NA` is reserved for non-substantive or unusable rows.

This strengthens the paper's claim that claim-level evidence-use and integrated-correctness variables can be applied consistently. It does not change the paper into a model-performance validation study or final audit-validity study.

