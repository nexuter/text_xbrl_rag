# Bounded Robustness Extension LLM and Coding Log

## Purpose

This log records the limited LLM and preliminary claim-coding checks for the six-filer bounded robustness extension.

The purpose is not to estimate model performance or retrieval-method superiority. The purpose is to test whether the retrieval-environment validity protocol can be applied beyond the three main deep cases and whether claim-level evidence-use divergence appears across varied reporting environments.

## Extension Run Scope

Run label:

- `gemma4_31b_extension`

Model:

- `gemma4:31b`

Provider:

- Local Ollama

Temperature:

- `0.0`

Sample role:

- `bounded_extension`

Filers:

| Ticker | Company | Primary Construct | Conditions |
|---|---|---|---|
| WMT | Walmart Inc. | inventory | text, XBRL, hybrid |
| HD | Home Depot, Inc. | inventory | text, XBRL, hybrid |
| CAT | Caterpillar Inc. | inventory | text, XBRL, hybrid |
| PFE | Pfizer Inc. | inventory | text, XBRL, hybrid |
| MSFT | Microsoft Corp. | revenue | text, XBRL, hybrid |
| CROX | Crocs, Inc. | inventory | text, XBRL, hybrid |

Total prompt/output conditions:

- 18

Output archive:

- `data/processed/llm_outputs/gemma4_31b_extension/`

Run manifest:

- `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv`

Note:

The run was completed in two passes because the first execution reached the command timeout after writing 10 output files. The second execution reused existing outputs and completed the remaining 8. All 18 text outputs and raw JSON files are present.

## Claim Coding Output

Coding command used:

```text
python scripts/code_llm_claims.py --run-label gemma4_31b_extension --output-prefix gemma4_31b_extension --roles bounded_extension
```

Coding files:

| Artifact | Path |
|---|---|
| Claim-level coding | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` |
| Coding summary | `data/processed/coding/claim_coding_summary_gemma4_31b_extension.md` |
| Summary by condition | `data/processed/coding/coding_summary_by_condition_gemma4_31b_extension.csv` |
| Inference shift table | `data/processed/coding/inference_shift_table_prelim_gemma4_31b_extension.csv` |
| Failure mode examples | `data/processed/coding/failure_mode_examples_prelim_gemma4_31b_extension.csv` |

Segmented claims:

- 88

Coding status:

- preliminary author code

## Claim Count by Filer and Condition

| Filer | Condition | Claims |
|---|---|---:|
| WMT | text | 5 |
| WMT | XBRL | 5 |
| WMT | hybrid | 5 |
| HD | text | 5 |
| HD | XBRL | 5 |
| HD | hybrid | 5 |
| CAT | text | 4 |
| CAT | XBRL | 5 |
| CAT | hybrid | 5 |
| PFE | text | 5 |
| PFE | XBRL | 5 |
| PFE | hybrid | 5 |
| MSFT | text | 5 |
| MSFT | XBRL | 4 |
| MSFT | hybrid | 5 |
| CROX | text | 5 |
| CROX | XBRL | 5 |
| CROX | hybrid | 5 |

## Preliminary Coding Summary

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 25 | 12 | 13 | 0 | 0.50 | 0.85 | 1.00 | 0.58 |
| hybrid | revenue | 5 | 2 | 3 | 0 | 0.50 | 1.00 | 1.00 | 0.50 |
| text | inventory | 24 | 10 | 14 | 0 | 0.71 | NA | 1.00 | NA |
| text | revenue | 5 | 2 | 3 | 0 | 0.70 | NA | 1.00 | NA |
| XBRL | inventory | 25 | 11 | 14 | 0 | NA | 0.72 | 1.00 | NA |
| XBRL | revenue | 4 | 2 | 2 | 0 | NA | 0.75 | 1.00 | NA |

Important limitation:

These means are not model-performance evidence. Audit-valid and integrated scores remain preliminary author coding and require expert review before they can support audit-judgment claims.

## Methodological Interpretation

The bounded extension supports the paper's methodological claim in three ways.

First, the retrieval-environment validity protocol scaled beyond the original Nike, Starbucks, and Target cases. It was applied to retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products.

Second, the extension preserves the main demonstration's core inference: retrieval condition labels do not fully describe claim-level evidence use. Hybrid conditions still require claim-level coding to determine whether claims actually integrate text and XBRL evidence.

Third, the extension identifies boundary conditions. MSFT's revenue-focused setting produced adequate text and fact context but no selected relation paths under the current seed-pattern linkbase retrieval. CAT generated a much larger XBRL fact and relation environment, showing that selection and representation validity become more salient in high-complexity filings.

## Reviewer-Facing Claim Supported

The manuscript can now state:

> In addition to the three deep cases, we conducted a bounded six-filer extension covering retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. The extension generated 18 additional retrieval-conditioned LLM outputs and 88 preliminary coded claims. The results are not used to estimate performance; they show that the retrieval-environment validity protocol can be applied across varied reporting environments and that claim-level evidence-use divergence remains observable beyond the main cases.

## What Not To Claim

Do not claim:

1. hybrid retrieval is superior;
2. XBRL retrieval improves audit reasoning;
3. audit-valid means indicate model audit expertise;
4. failure-mode frequencies are population estimates;
5. the six-filer extension is representative of SEC filers.

## Remaining Work

1. Select two or three extension examples for appendix illustration.
2. Decide whether any extension examples should be mentioned in the main manuscript.
3. Add a concise extension paragraph to the demonstration section of v2.
4. Add appendix tables for extension filer selection, retrieval diagnostics, and preliminary coding summary.
5. Consider expert review of selected main and extension claims before submission.
