# Bounded Extension Manuscript Integration Package

## Purpose

This file converts the bounded six-filer robustness extension into manuscript-ready language and appendix tables.

The extension should strengthen the demonstration without changing the paper into an empirical benchmark. The main manuscript should use it as bounded methodological robustness evidence; detailed output and claim coding should remain in the appendix.

## Core Manuscript Claim

Recommended wording:

> The primary demonstration uses three familiar filers for deep source tracing and claim-level illustration. To reduce the concern that the framework reflects only those cases, we also conduct a bounded six-filer extension selected for variation in industry, scale, reporting complexity, and construct fit. The extension is not designed to estimate model performance or failure-mode prevalence. It tests whether the retrieval-environment validity protocol remains applicable across varied reporting environments.

## Where To Insert

Insert a short subsection after Section 7.2 Implementation Summary in `plan/46_phase9_manuscript_draft_v2_after_reviewer_revisions.md`.

Recommended heading:

```text
### 7.3 Bounded Robustness Extension
```

Then renumber the current selected-example section as 7.4 and aggregate-coding section as 7.5.

## Manuscript-Ready Subsection

```text
### 7.3 Bounded Robustness Extension

The primary demonstration uses three familiar filers to allow detailed source tracing and claim-level illustration. To reduce the risk that the demonstration reflects only those firms, we conduct a bounded robustness extension using six additional filers selected for variation in industry, scale, reporting complexity, and construct fit: Walmart, Home Depot, Caterpillar, Pfizer, Microsoft, and Crocs. The extension covers retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products.

The extension is not designed to estimate population-level performance, failure-mode prevalence, or retrieval-method superiority. Instead, it tests whether the retrieval-environment validity protocol can be applied across varied reporting environments. For each additional filer, we build retrieval contexts for one primary construct and three retrieval conditions: text, XBRL, and hybrid. This design generated 18 additional retrieval-conditioned outputs and 88 preliminary coded claims.

The extension supports three methodological points. First, the protocol scales beyond the three deep cases: source logs, prompt contexts, output claims, and correctness-layer coding can be maintained across different industries. Second, the extension preserves the main inference that retrieval condition labels do not reveal claim-level evidence use. Hybrid outputs still contain integrated, text-only, and XBRL-only claims. Third, the extension reveals boundary conditions. Caterpillar generated a much larger XBRL fact and relation environment than the other filers, making selection and representation validity more salient. Microsoft, by contrast, provided a strong revenue-recognition setting but no selected revenue relation paths under the current seed-pattern linkbase retrieval, illustrating why construct fit and retrieval diagnostics must precede inference.

We report the extension in the appendix as robustness evidence, not as model-performance evidence. Audit-valid and integrated scores remain preliminary author coding unless reviewed by audit-domain experts.
```

## Appendix Table A. Extension Filer Selection

| Ticker | Company | Industry / Setting | Sample Role | Primary Construct | Methodological Purpose |
|---|---|---|---|---|---|
| WMT | Walmart Inc. | Mega-scale retail | bounded extension | inventory | High-volume retail inventory setting |
| HD | Home Depot, Inc. | Specialty retail / home improvement | bounded extension | inventory | Specialty retail inventory and acquisition-related inventory context |
| CAT | Caterpillar Inc. | Industrial manufacturing | bounded extension | inventory | High-complexity inventory and LIFO reporting stress case |
| PFE | Pfizer Inc. | Pharma / healthcare products | bounded extension | inventory | Product/reserve/regulatory setting |
| MSFT | Microsoft Corp. | Software/cloud | bounded extension | revenue | Revenue-recognition and contract-liability boundary case |
| CROX | Crocs, Inc. | Mid-size consumer products / footwear | bounded extension | inventory | Size variation and consumer-product inventory setting |

## Appendix Table B. Extension Retrieval Diagnostics

| Ticker | Text Chunks | XBRL Facts | XBRL Relation Paths | Retrieval Diagnostic |
|---|---:|---:|---:|---|
| WMT | 120 | 141 | 109 | Strong retail extension case |
| HD | 125 | 173 | 174 | Strong specialty-retail extension case |
| CAT | 213 | 1,047 | 574 | High-complexity industrial/manufacturing case |
| PFE | 196 | 336 | 272 | Pharma/product-risk extension case |
| MSFT | 150 | 144 | 0 | Revenue-focused software/cloud boundary case; relation-path scarcity is informative |
| CROX | 164 | 123 | 102 | Mid-size consumer product extension case |

## Appendix Table C. Extension LLM and Coding Scope

| Ticker | Primary Construct | Conditions | Output Count | Coded Claims |
|---|---|---|---:|---:|
| WMT | inventory | text, XBRL, hybrid | 3 | 15 |
| HD | inventory | text, XBRL, hybrid | 3 | 15 |
| CAT | inventory | text, XBRL, hybrid | 3 | 14 |
| PFE | inventory | text, XBRL, hybrid | 3 | 15 |
| MSFT | revenue | text, XBRL, hybrid | 3 | 14 |
| CROX | inventory | text, XBRL, hybrid | 3 | 15 |
| Total | mixed | text, XBRL, hybrid | 18 | 88 |

## Appendix Table D. Selected Extension Examples

| Example | Filer | Construct | Condition | Claim ID | Claim Role | Claim Summary | Sources | Preliminary Interpretation |
|---|---|---|---|---|---|---|---|---|
| EXT-01 | HD | inventory | hybrid | C026 | integrated factual claim | Merchandise inventories were $25.8 billion as of February 1, 2026. | T-HD-INVENTORY-020; F-HD-0004 | Demonstrates clean text-XBRL corroboration in a specialty retail setting. |
| EXT-02 | CAT | inventory | hybrid | C042 | integrated risk/assertion claim | Reliance on LIFO for approximately 70% of inventories and the LIFO reserve create an inventory valuation consideration. | T-CAT-INVENTORY-016; F-CAT-0048 | Shows that integration is possible in a high-complexity manufacturing setting, but audit-validity remains preliminary. |
| EXT-03 | PFE | inventory | hybrid | C057 | integrated risk/assertion claim | Historical inventory write-offs and product return adjustments indicate inventory valuation considerations. | T-PFE-REVENUE_INVENTORY-035; F-PFE-0134 | Extends the protocol to pharma/product-risk reporting. |
| EXT-04 | MSFT | revenue | hybrid | C069 | XBRL-only claim within hybrid condition | Current contract liability was $64.555 billion as of June 30, 2025. | F-MSFT-0028 | Demonstrates that a hybrid condition can produce XBRL-only claims. |
| EXT-05 | MSFT | revenue | hybrid | C071 | text-only risk/assertion claim within hybrid condition | Management estimates for SSP and timing of performance obligations create revenue accuracy and cut-off considerations. | T-MSFT-REVENUE-089 | Demonstrates that a hybrid condition can produce text-only audit reasoning. |

## Appendix Table E. Preliminary Extension Coding Summary

| Condition | Construct | Claims | Factual | Risk/Assertion | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 25 | 12 | 13 | 0.50 | 0.85 | 1.00 | 0.58 |
| hybrid | revenue | 5 | 2 | 3 | 0.50 | 1.00 | 1.00 | 0.50 |
| text | inventory | 24 | 10 | 14 | 0.71 | NA | 1.00 | NA |
| text | revenue | 5 | 2 | 3 | 0.70 | NA | 1.00 | NA |
| XBRL | inventory | 25 | 11 | 14 | NA | 0.72 | 1.00 | NA |
| XBRL | revenue | 4 | 2 | 2 | NA | 0.75 | 1.00 | NA |

Note: These values are preliminary author-coded diagnostics. They should not be interpreted as model-performance measures or audit-validity evidence.

## How To Use Extension Evidence In The Main Text

Use the extension for three claims only:

1. **Applicability:** The protocol can be applied beyond the three deep cases.
2. **Evidence-use divergence:** Hybrid condition labels still do not guarantee integrated text-XBRL reasoning.
3. **Boundary conditions:** Different industries create different retrieval-validity challenges, such as CAT's large XBRL environment and MSFT's relation-path scarcity.

Do not use the extension for:

1. performance comparison;
2. population-level inference;
3. claims that hybrid retrieval is superior;
4. claims that XBRL improves audit reasoning;
5. audit-valid conclusions without expert review.

## Recommended Revision To Section 8 Boundary Conditions

Add this paragraph:

```text
Seventh, the bounded six-filer extension is a maximum-variation methodological extension, not a representative sample. It increases confidence that the protocol can be applied across varied reporting environments, but it does not estimate the prevalence of retrieval failures across SEC filers. Studies that make prevalence or performance claims should use formal sampling, expert coding, and statistical inference appropriate to those claims.
```

## Reviewer-Facing Response

If a reviewer asks whether three companies are enough:

> The manuscript uses three familiar filers for deep traceability and claim-level illustration, then adds a bounded six-filer extension to test whether the protocol applies across varied reporting environments. The extension is not presented as a representative empirical sample; it is a maximum-variation methodological check.

If a reviewer asks why not run a larger sample:

> A larger sample would shift the paper toward performance benchmarking and prevalence estimation. Because the paper is a methodology paper, the bounded extension is designed to demonstrate applicability and boundary conditions while preserving source-level traceability.

## Files Supporting This Extension

| Artifact | Path |
|---|---|
| Filer selection memo | `plan/49_bounded_robustness_extension_filer_selection.md` |
| Data and diagnostics log | `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md` |
| LLM and coding log | `plan/51_bounded_robustness_extension_llm_and_coding_log.md` |
| LLM validation log | `plan/52_llm_results_validation_log.md` |
| Claim coding table | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` |
| Output archive | `data/processed/llm_outputs/gemma4_31b_extension/` |

## Final Assessment

The bounded extension should be included in the appendix and summarized briefly in the main text. It materially reduces the reviewer concern that the demonstration is hand-picked, while preserving the paper's identity as a methodology paper.
