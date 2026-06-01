# Intercoder Reliability Summary

## Completed Coding Exercise

- Coders: `coder1`, `coder2`
- Claims coded by each coder: `120`
- Combined coder rows: `240`
- Disagreement records across coded variables: `19`

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
| evidence_use_type_code | 120 | 119 | 99.2% | 0.986 | NA |
| text_supported_code | 120 | 117 | 97.5% | NA | 0.919 |
| graph_valid_code | 120 | 118 | 98.3% | NA | 0.891 |
| integrated_code | 120 | 115 | 95.8% | NA | 0.880 |
| confidence_code | 120 | 115 | 95.8% | 0.917 | NA |

## Interpretation

The independent coding exercise provides reliability evidence for the claim-level measurement protocol. Agreement is strongest for claim segmentation, evidence-use type, text support, graph validity, integrated correctness, and confidence coding. Claim-kind agreement is lower but still indicates substantial consistency after chance adjustment; remaining differences primarily reflect boundary cases between factual claims and risk/assertion inferences.

Audit-boundary notes are qualitative diagnostics and are not included in kappa statistics. They should be used to identify reconciliation examples and refine the wording of the coding protocol.

## Output Files

- Combined coder results: `[insert combined results file name]`
- Disagreement file: `[insert disagreement file name]`
