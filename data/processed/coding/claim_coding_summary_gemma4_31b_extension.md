# Phase 6 Claim-Level Preliminary Coding Summary

## Scope

- Run label: `gemma4_31b_extension`
- Model: `gemma4:31b`
- Segmented claims: `88`
- Coding status: `preliminary_author_code`

## Important Limitation

The scores are preliminary author codes generated from the structured LLM outputs. Audit-valid and integrated correctness require expert review before being treated as manuscript evidence.

## Summary by Condition and Construct

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 25 | 12 | 13 | 0 | 0.50 | 0.85 | 1.00 | 0.58 |
| hybrid | revenue | 5 | 2 | 3 | 0 | 0.50 | 1.00 | 1.00 | 0.50 |
| text | inventory | 24 | 10 | 14 | 0 | 0.71 | NA | 1.00 | NA |
| text | revenue | 5 | 2 | 3 | 0 | 0.70 | NA | 1.00 | NA |
| xbrl | inventory | 25 | 11 | 14 | 0 | NA | 0.72 | 1.00 | NA |
| xbrl | revenue | 4 | 2 | 2 | 0 | NA | 0.75 | 1.00 | NA |

## Output Files

- `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
- `data/processed/coding/coding_summary_by_condition_gemma4_31b_extension.csv`
- `data/processed/coding/inference_shift_table_prelim_gemma4_31b_extension.csv`
- `data/processed/coding/failure_mode_examples_prelim_gemma4_31b_extension.csv`