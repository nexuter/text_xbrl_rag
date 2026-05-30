# Bounded Robustness Extension Data and Retrieval Diagnostics Log

## Purpose

This log records the implementation of the six-filer bounded robustness extension selected in `plan/49_bounded_robustness_extension_filer_selection.md`.

The goal is appendix-level methodological robustness, not population-level empirical inference.

## Implementation Completed

### Shared Filer Manifest

Created:

- `config/filer_manifest.json`

The manifest distinguishes:

- `main_deep_case`
- `bounded_extension`
- `backup`

It also records:

- ticker;
- company;
- CIK;
- accession;
- fiscal year;
- report period;
- primary document;
- raw-data folder;
- extension primary construct.

### Script Refactoring

Updated:

- `scripts/sec_download.py`
- `scripts/extract_demo_data.py`
- `scripts/build_retrieval_contexts.py`

Key changes:

1. Scripts now read from `config/filer_manifest.json`.
2. Scripts can filter by `sample_role`.
3. Main deep cases and bounded extension cases are preserved in the same pipeline but labeled separately.
4. Bounded extension prompt generation uses one primary construct per filer and three retrieval conditions: text, XBRL, and hybrid.
5. Main deep cases retain the original full design: two constructs and four conditions, including LLM-only baseline.

## SEC Download Status

Downloaded or reused SEC filing files for nine active filers:

| Ticker | Company | Sample Role |
|---|---|---|
| NKE | Nike, Inc. | main_deep_case |
| SBUX | Starbucks Corporation | main_deep_case |
| TGT | Target Corporation | main_deep_case |
| WMT | Walmart Inc. | bounded_extension |
| HD | Home Depot, Inc. | bounded_extension |
| CAT | Caterpillar Inc. | bounded_extension |
| PFE | Pfizer Inc. | bounded_extension |
| MSFT | Microsoft Corp. | bounded_extension |
| CROX | Crocs, Inc. | bounded_extension |

Download manifest:

- `data/processed/download_manifest.md`
- `data/processed/download_manifest.json`

Raw filing directories:

- `data/raw_sec/nke_2025_10k/`
- `data/raw_sec/sbux_2025_10k/`
- `data/raw_sec/tgt_2025_10k/`
- `data/raw_sec/wmt_2026_10k/`
- `data/raw_sec/hd_2026_10k/`
- `data/raw_sec/cat_2025_10k/`
- `data/raw_sec/pfe_2025_10k/`
- `data/raw_sec/msft_2025_10k/`
- `data/raw_sec/crox_2025_10k/`

## Extraction Diagnostics

Extraction output:

- `data/processed/extraction_summary.md`
- `data/processed/extraction_summary.json`
- `data/processed/text_chunks/text_chunks.csv`
- `data/processed/xbrl_facts/xbrl_facts.csv`
- `data/processed/xbrl_paths/xbrl_paths.csv`

| Ticker | Sample Role | Text Chunks | XBRL Facts | XBRL Relation Paths | Diagnostic Interpretation |
|---|---|---:|---:|---:|---|
| NKE | main_deep_case | 184 | 365 | 99 | Existing deep case retained |
| SBUX | main_deep_case | 122 | 135 | 210 | Existing deep case retained |
| TGT | main_deep_case | 103 | 102 | 79 | Existing deep case retained |
| WMT | bounded_extension | 120 | 141 | 109 | Strong retail extension case |
| HD | bounded_extension | 125 | 173 | 174 | Strong specialty-retail extension case |
| CAT | bounded_extension | 213 | 1047 | 574 | High-complexity industrial/manufacturing case |
| PFE | bounded_extension | 196 | 336 | 272 | Pharma/product-risk extension case |
| MSFT | bounded_extension | 150 | 144 | 0 | Revenue-focused software/cloud boundary case; relation-path scarcity is informative |
| CROX | bounded_extension | 164 | 123 | 102 | Mid-size consumer product extension case |

## Retrieval Context Diagnostics

Generated:

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/retrieval_contexts/retrieval_context_manifest.json`
- `data/processed/retrieval_contexts/retrieval_context_summary.md`
- `data/processed/retrieval_logs/retrieval_log.csv`
- `data/processed/prompts/`

Counts:

| Item | Count |
|---|---:|
| Prompt/context conditions | 42 |
| Retrieval log rows | 313 |

Design:

| Sample Role | Filers | Constructs | Conditions | Prompt/Context Count |
|---|---:|---|---|---:|
| main_deep_case | 3 | revenue, inventory | text, XBRL, hybrid, LLM-only | 24 |
| bounded_extension | 6 | one primary construct per filer | text, XBRL, hybrid | 18 |
| Total | 9 | mixed | mixed | 42 |

## Retrieval Context Summary

| Filer | Role | Construct | Text Words | XBRL Words | Hybrid Words | Baseline Words |
|---|---|---|---:|---:|---:|---:|
| NKE | main_deep_case | revenue | 537 | 624 | 748 | 10 |
| NKE | main_deep_case | inventory | 422 | 628 | 715 | 10 |
| SBUX | main_deep_case | revenue | 478 | 708 | 764 | 10 |
| SBUX | main_deep_case | inventory | 521 | 514 | 560 | 10 |
| TGT | main_deep_case | revenue | 566 | 577 | 761 | 10 |
| TGT | main_deep_case | inventory | 786 | 556 | 742 | 10 |
| WMT | bounded_extension | inventory | 629 | 568 | 676 | NA |
| HD | bounded_extension | inventory | 732 | 569 | 807 | NA |
| CAT | bounded_extension | inventory | 511 | 535 | 579 | NA |
| PFE | bounded_extension | inventory | 624 | 585 | 772 | NA |
| MSFT | bounded_extension | revenue | 601 | 224 | 555 | NA |
| CROX | bounded_extension | inventory | 733 | 589 | 761 | NA |

## Methodological Interpretation

The bounded extension strengthens the paper in three ways.

1. It reduces the risk that the demonstration appears hand-picked around three familiar consumer-facing companies.
2. It introduces variation in industry, scale, reporting complexity, and construct fit.
3. It preserves the paper's methodology identity by limiting extension runs to appendix-level diagnostics rather than expanding into a population-level benchmark.

MSFT is especially useful as a boundary case. It has sufficient revenue text and XBRL facts, but no selected revenue relation paths under the current seed-pattern linkbase retrieval. This demonstrates that XBRL relational retrieval may be sparse or less informative in some settings and that retrieval-environment validity requires construct-specific diagnostics before inference.

CAT is useful as a high-complexity stress case because it produced many more XBRL facts and relation paths than the other filers. This will help demonstrate selection and representation validity concerns in complex manufacturing settings.

## Reviewer-Facing Claim Now Supported

The paper can now state:

> We retain the three familiar filers for deep claim-level illustration and add a bounded six-filer robustness extension spanning retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. The extension is used to assess whether the retrieval-environment validity protocol remains applicable across varied reporting environments, not to estimate population-level model performance.

## Remaining Work

1. Run limited LLM outputs for the 18 bounded-extension prompt/context conditions.
2. Add run filtering to `scripts/run_llm_prompts.py` if needed so extension runs can be separated from main deep-case runs.
3. Add run-label support to claim coding so extension coding does not overwrite main deep-case coding.
4. Code a limited claim subset from the extension outputs.
5. Produce an appendix-level robustness summary table.
