# Bounded Sensitivity Decision Summary

## Purpose

This diagnostic converts the context-volume and source-environment perturbation outputs into a reviewer-facing decision matrix.
It evaluates retrieval-stage separability and source-composition sensitivity; it does not re-run the LLM and should not be interpreted as model-output robustness evidence.

## Scope

- Filer-construct cells reviewed: `18`
- Perturbation rows reviewed: `90`
- Variants reviewed: text top-3, text top-8, XBRL fact-only, XBRL reduced fact budget, and XBRL expanded fact/path budget.

## Variant Decision Bands

| Variant | Cells | Mean Jaccard | Minimum Jaccard | Cells Below 0.60 | Decision Band |
|---|---:|---:|---:|---:|---|
| text_top3 | 18 | 0.600 | 0.600 | 0 | moderate_source_environment_change |
| text_top8 | 18 | 0.625 | 0.625 | 0 | moderate_source_environment_change |
| xbrl_expanded_fact16_path15 | 18 | 0.750 | 0.710 | 0 | moderate_source_environment_change |
| xbrl_fact_only | 18 | 0.594 | 0.524 | 16 | material_source_environment_change |
| xbrl_fact_top8_paths_current | 18 | 0.807 | 0.667 | 0 | bounded_source_environment_change |

## Cell-Level Separability Attention

| Attention Band | Cells |
|---|---:|
| high_separability_attention | 17 |
| moderate_separability_attention | 1 |

## High-Attention Cells

| Ticker | Construct | Hybrid Imbalance | Minimum Jaccard | Fact-Only Jaccard |
|---|---|---:|---:|---:|
| CAT | inventory | 1.460 | 0.545 | 0.545 |
| CAT | revenue | 1.030 | 0.545 | 0.545 |
| CROX | inventory | 1.030 | 0.545 | 0.545 |
| CROX | revenue | 1.200 | 0.545 | 0.545 |
| HD | inventory | 1.030 | 0.545 | 0.545 |
| HD | revenue | 1.000 | 0.545 | 0.545 |
| MSFT | revenue | 1.730 | 0.600 | 1.000 |
| NKE | inventory | 2.150 | 0.545 | 0.545 |
| NKE | revenue | 1.560 | 0.545 | 0.545 |
| PFE | inventory | 1.210 | 0.545 | 0.545 |
| PFE | revenue | 1.460 | 0.545 | 0.545 |
| SBUX | inventory | 1.440 | 0.545 | 0.545 |
| SBUX | revenue | 2.090 | 0.545 | 0.545 |
| TGT | inventory | 1.070 | 0.545 | 0.545 |
| TGT | revenue | 1.430 | 0.545 | 0.545 |
| WMT | inventory | 1.190 | 0.524 | 0.524 |
| WMT | revenue | 1.140 | 0.545 | 0.545 |

## Interpretation

- The diagnostic shows that relational XBRL evidence is methodologically separable from fact-only XBRL retrieval: removing relation paths creates a material source-environment change in most filer-construct cells.
- High-attention cells identify where future Tier 2 model-validation studies should add matched-budget, source-order, prompt-sensitivity, and output-level rerun checks before making performance claims.
- The current paper uses these results to validate protocol transparency and source-environment inspectability, not retrieval superiority.
