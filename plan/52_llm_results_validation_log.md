# LLM Results Validation Log

## Purpose

This log validates completeness, parseability, source traceability, and coding separation for the main deep-case and bounded-extension LLM results.

## Retrieval Context Manifest Check

| Sample Role | Condition | Prompt/Context Count |
|---|---|---|
| bounded_extension | hybrid | 12 |
| bounded_extension | llm_only | 12 |
| bounded_extension | text | 12 |
| bounded_extension | xbrl | 12 |
| main_deep_case | hybrid | 6 |
| main_deep_case | llm_only | 6 |
| main_deep_case | text | 6 |
| main_deep_case | xbrl | 6 |

## Run Check: `gemma4_31b_full`

| Metric | Value |
|---|---|
| Expected output files | 24 |
| Text output files | 24 |
| Raw JSON files | 24 |
| Parsed/coded claims | 94 |
| Short output files under 25 words | 5 |
| Invalid source references | 0 |
| Manual-review-required claims | 94 |

### Run Manifest Status Counts

| Status | Count |
|---|---|
| completed | 24 |

### Claim Counts by Filer and Condition

| Ticker | Condition | Claims |
|---|---|---|
| NKE | hybrid | 10 |
| NKE | llm_only | 2 |
| NKE | text | 9 |
| NKE | xbrl | 10 |
| SBUX | hybrid | 10 |
| SBUX | llm_only | 2 |
| SBUX | text | 9 |
| SBUX | xbrl | 10 |
| TGT | hybrid | 10 |
| TGT | llm_only | 2 |
| TGT | text | 10 |
| TGT | xbrl | 10 |

## Run Check: `gemma4_31b_extension`

| Metric | Value |
|---|---|
| Expected output files | 48 |
| Text output files | 48 |
| Raw JSON files | 48 |
| Parsed/coded claims | 187 |
| Short output files under 25 words | 9 |
| Invalid source references | 0 |
| Manual-review-required claims | 187 |

### Run Manifest Status Counts

| Status | Count |
|---|---|
| skipped_existing | 48 |

### Claim Counts by Filer and Condition

| Ticker | Condition | Claims |
|---|---|---|
| CAT | hybrid | 10 |
| CAT | llm_only | 2 |
| CAT | text | 9 |
| CAT | xbrl | 10 |
| CROX | hybrid | 10 |
| CROX | llm_only | 2 |
| CROX | text | 10 |
| CROX | xbrl | 10 |
| HD | hybrid | 10 |
| HD | llm_only | 2 |
| HD | text | 10 |
| HD | xbrl | 10 |
| MSFT | hybrid | 9 |
| MSFT | llm_only | 2 |
| MSFT | text | 10 |
| MSFT | xbrl | 8 |
| PFE | hybrid | 10 |
| PFE | llm_only | 2 |
| PFE | text | 10 |
| PFE | xbrl | 10 |
| WMT | hybrid | 10 |
| WMT | llm_only | 2 |
| WMT | text | 10 |
| WMT | xbrl | 9 |

## Source Reference Validation

No invalid global source IDs or local text-chunk rank references were detected in coded source references.

## Validation Verdict

Pass for completeness, parseability, run separation, global source-ID traceability, and local text-chunk rank traceability.

## Important Limitation

This validation checks data integrity and traceability. It does not validate audit-valid or integrated correctness as expert audit judgments. Those scores remain preliminary author coding until audit-domain review is completed.