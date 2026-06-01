# Context Volume Diagnostics

## Purpose

This diagnostic addresses separability concerns by documenting the information volume supplied under each retrieval condition. It is a Tier 1 transparency diagnostic, not a completed model-performance sensitivity test.

## Files

- Detail diagnostics: `data/processed/retrieval_contexts/context_volume_diagnostics.csv`
- Condition summary: `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv`

## Summary By Condition

| Condition | Contexts | Mean Context Words | Median | Min | Max | Mean Prompt Words | Mean Text Chunks | Mean XBRL Facts | Mean XBRL Paths |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | 18 | 691.3 | 718.5 | 278 | 885 | 862.9 | 5.0 | 11.9 | 8.9 |
| llm_only | 18 | 10.0 | 10.0 | 10 | 10 | 181.6 | 0.0 | 0.0 | 0.0 |
| text | 18 | 602.6 | 594.0 | 249 | 929 | 774.2 | 5.0 | 0.0 | 0.0 |
| xbrl | 18 | 524.2 | 542.5 | 192 | 666 | 695.8 | 0.0 | 11.9 | 8.9 |

## Hybrid Separability Diagnostic

- Hybrid contexts reviewed: `18`
- Hybrid text/XBRL word-imbalance ratio mean: `1.37`
- Hybrid text/XBRL word-imbalance ratio median: `1.32`
- Hybrid text/XBRL word-imbalance ratio maximum: `2.15`

Interpretation: hybrid retrieval supplies more total information than text-only or XBRL-only retrieval because it combines narrative chunks and structured facts/paths. This supports the manuscript boundary that hybrid outputs should not be interpreted as model-performance evidence unless future studies add token-budget equalization, evidence-order sensitivity, and prompt sensitivity checks.

## Reviewer-Facing Use

These diagnostics strengthen the separability discussion by making context-volume differences observable. They do not eliminate separability concerns; instead, they document why the current paper remains a protocol-validation demonstration and why Tier 2 studies should add matched-budget and retrieval-variation sensitivity tests.
