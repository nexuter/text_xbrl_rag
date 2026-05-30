# LLM Results Validation Log

## Purpose

This log validates completeness, parseability, source traceability, and coding separation for the main deep-case and bounded-extension LLM results.

## Retrieval Context Manifest Check

| Sample Role | Condition | Prompt/Context Count |
|---|---|---|
| bounded_extension | hybrid | 6 |
| bounded_extension | text | 6 |
| bounded_extension | xbrl | 6 |
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
| Expected output files | 18 |
| Text output files | 18 |
| Raw JSON files | 18 |
| Parsed/coded claims | 88 |
| Short output files under 25 words | 0 |
| Invalid source references | 0 |
| Manual-review-required claims | 88 |

### Run Manifest Status Counts

| Status | Count |
|---|---|
| completed | 8 |
| skipped_existing | 10 |

### Claim Counts by Filer and Condition

| Ticker | Condition | Claims |
|---|---|---|
| CAT | hybrid | 5 |
| CAT | text | 4 |
| CAT | xbrl | 5 |
| CROX | hybrid | 5 |
| CROX | text | 5 |
| CROX | xbrl | 5 |
| HD | hybrid | 5 |
| HD | text | 5 |
| HD | xbrl | 5 |
| MSFT | hybrid | 5 |
| MSFT | text | 5 |
| MSFT | xbrl | 4 |
| PFE | hybrid | 5 |
| PFE | text | 5 |
| PFE | xbrl | 5 |
| WMT | hybrid | 5 |
| WMT | text | 5 |
| WMT | xbrl | 5 |

## Source Reference Validation

No invalid global source IDs or local text-chunk rank references were detected in coded source references.

## Validation Verdict

Pass for completeness, parseability, run separation, global source-ID traceability, and local text-chunk rank traceability.

## Important Limitation

This validation checks data integrity and traceability. It does not validate audit-valid or integrated correctness as expert audit judgments. Those scores remain preliminary author coding until audit-domain review is completed.