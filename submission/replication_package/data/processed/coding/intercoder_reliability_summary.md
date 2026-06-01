# Intercoder Reliability Summary

## Completed Coding Exercise

- Coders: `Coder 2`, `coder_1`
- Claims coded by each coder: `120`
- Combined coder rows: `240`
- Disagreement records across coded variables: `22`

## Sample Composition

| Condition | Claims |
|---|---:|
| hybrid | 89 |
| llm_only | 12 |
| text | 9 |
| xbrl | 10 |

## Reliability Results

| Variable | N | Agreement | Percent Agreement | Cohen's Kappa | Weighted Kappa |
|---|---:|---:|---:|---:|---:|
| claim_segmentation_agreement | 120 | 120 | 100.0% | 1.000 | NA |
| claim_kind_code | 120 | 117 | 97.5% | 0.957 | NA |
| evidence_use_type_code | 120 | 120 | 100.0% | 1.000 | NA |
| text_supported_code | 120 | 117 | 97.5% | NA | 0.919 |
| graph_valid_code | 120 | 119 | 99.2% | NA | 0.934 |
| integrated_code | 120 | 120 | 100.0% | NA | 1.000 |
| confidence_code | 120 | 105 | 87.5% | 0.754 | NA |

## Interpretation

The independent coding exercise provides reliability evidence for the claim-level measurement protocol. Agreement is perfect for claim segmentation, evidence-use type, and integrated correctness. Agreement is also high for claim kind, text-supported correctness, graph-valid correctness, and confidence coding. The recoded `integrated_code` results show that the revised instruction resolved the prior ambiguity between ordinary non-integration (`0`) and non-evaluable rows (`NA`): both coders coded all text-only, XBRL-only, LLM-only, and hybrid-but-one-source claims as `0` rather than `NA`.

Remaining differences primarily reflect boundary cases between factual accounting-policy descriptions and risk/assertion inferences. Audit-boundary notes are qualitative diagnostics and are not included in kappa statistics.

## Reconciliation Note

Three claims remain focal substantive disagreements after recoding:

| Claim ID | Issue | Reconciliation Assessment |
|---|---|---|
| `MAIN-C043` | Factual accounting-policy statement versus risk/assertion inference | Reconcile as factual, text-supported, graph validity not applicable, integrated correctness `0`. |
| `EXT-C044` | Factual gift-card breakage policy statement versus risk/assertion inference | Reconcile as factual, text-supported, graph validity not applicable, integrated correctness `0`. |
| `EXT-C045` | Gift-card recognition timing and six-month redemption-period claim | Reconcile as factual, text-supported, graph-valid, integrated correctness `1`. |

These reconciliation items do not affect the core retrieval-validity conclusion because evidence-use type and integrated correctness have 100.0 percent agreement.

## Output Files

- Combined coder results: `data/processed/coding/independent_coding_results.csv`
- Disagreement file: `data/processed/coding/independent_coding_disagreements.csv`
