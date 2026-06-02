# Phase 6 Claim-Level Preliminary Coding Summary

## Scope

- Run label: `gemma4_31b_extension`
- Model: `gemma4:31b`
- Segmented claims: `187`
- Coding status: `preliminary_author_code`

## Important Limitation

The scores are preliminary author codes generated from the structured LLM outputs. The aggregate table reports source-support and integration diagnostics only; audit-boundary coding remains claim-level and requires expert review before being treated as audit-judgment evidence.

## Summary by Condition and Construct

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Integrated Bridge Claims | Integrated Bridge Share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 29 | 14 | 15 | 0 | 0.45 | 0.85 | 4 | 0.14 |
| hybrid | revenue | 30 | 13 | 17 | 0 | 0.53 | 0.86 | 1 | 0.03 |
| llm_only | inventory | 6 | 0 | 0 | 6 | NA | NA | NA | NA |
| llm_only | revenue | 6 | 0 | 0 | 6 | NA | NA | NA | NA |
| text | inventory | 29 | 12 | 17 | 0 | 0.71 | NA | NA | NA |
| text | revenue | 30 | 12 | 18 | 0 | 0.70 | NA | NA | NA |
| xbrl | inventory | 29 | 13 | 16 | 0 | NA | 0.72 | NA | NA |
| xbrl | revenue | 28 | 14 | 14 | 0 | NA | 0.75 | NA | NA |

## Output Files

- `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
- `data/processed/coding/coding_summary_by_condition_gemma4_31b_extension.csv`
- `data/processed/coding/inference_shift_table_prelim_gemma4_31b_extension.csv`
- `data/processed/coding/failure_mode_examples_prelim_gemma4_31b_extension.csv`