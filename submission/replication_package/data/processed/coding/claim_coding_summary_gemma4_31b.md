# Phase 6 Claim-Level Preliminary Coding Summary

## Scope

- Run label: `gemma4_31b_full`
- Model: `gemma4:31b`
- Segmented claims: `94`
- Coding status: `preliminary_author_code`

## Important Limitation

The scores are preliminary author codes generated from the structured LLM outputs. The aggregate table reports source-support and integration diagnostics only; audit-boundary coding remains claim-level and requires expert review before being treated as audit-judgment evidence.

## Summary by Condition and Construct

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Integrated Bridge Claims | Integrated Bridge Share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 15 | 6 | 9 | 0 | 0.63 | 0.88 | 3 | 0.20 |
| hybrid | revenue | 15 | 6 | 9 | 0 | 0.47 | 0.88 | 0 | 0.00 |
| llm_only | inventory | 3 | 0 | 0 | 3 | NA | NA | NA | NA |
| llm_only | revenue | 3 | 0 | 0 | 3 | NA | NA | NA | NA |
| text | inventory | 13 | 5 | 8 | 0 | 0.69 | NA | NA | NA |
| text | revenue | 15 | 6 | 9 | 0 | 0.70 | NA | NA | NA |
| xbrl | inventory | 15 | 7 | 7 | 1 | NA | 0.70 | NA | NA |
| xbrl | revenue | 15 | 7 | 8 | 0 | NA | 0.73 | NA | NA |

## Output Files

- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/coding_summary_by_condition_gemma4_31b.csv`
- `data/processed/coding/inference_shift_table_prelim_gemma4_31b.csv`
- `data/processed/coding/failure_mode_examples_prelim_gemma4_31b.csv`