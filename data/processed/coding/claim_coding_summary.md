# Phase 6 Claim-Level Preliminary Coding Summary

## Scope

- Run label: `gemma4_31b_full`
- Model: `gemma4:31b`
- Segmented claims: `94`
- Coding status: `preliminary_author_code`

## Important Limitation

The scores are preliminary author codes generated from the structured LLM outputs. Audit-valid and integrated correctness require expert review before being treated as manuscript evidence.

## Summary by Condition and Construct

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 15 | 6 | 9 | 0 | 0.63 | 0.88 | 1.00 | 0.60 |
| hybrid | revenue | 15 | 6 | 9 | 0 | 0.47 | 0.88 | 1.00 | 0.50 |
| llm_only | inventory | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| llm_only | revenue | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| text | inventory | 13 | 5 | 8 | 0 | 0.69 | NA | 1.00 | NA |
| text | revenue | 15 | 6 | 9 | 0 | 0.70 | NA | 1.00 | NA |
| xbrl | inventory | 15 | 7 | 7 | 1 | NA | 0.70 | 1.00 | NA |
| xbrl | revenue | 15 | 7 | 8 | 0 | NA | 0.73 | 1.00 | NA |

## Output Files

- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/coding_summary_by_condition.csv`
- `data/processed/coding/inference_shift_table_prelim.csv`
- `data/processed/coding/failure_mode_examples_prelim.csv`