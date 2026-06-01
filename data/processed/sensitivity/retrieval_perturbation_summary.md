# Retrieval Perturbation Diagnostic Summary

This diagnostic varies deterministic retrieval-source selection without re-running the LLM.
It evaluates whether source environments are reconstructable and how much they change under bounded source-selection perturbations.
The results support protocol transparency and stability assessment at the retrieval stage; they are not model-performance sensitivity results.

Diagnostic cells: 18
Diagnostic rows: 90

| Variant Group | Variant | Cells | Mean Jaccard | Median Jaccard | Mean Retained Share | Mean Baseline Sources | Mean Variant Sources | Mean Added | Mean Removed |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| text | text_top3 | 18 | 0.600 | 0.600 | 0.600 | 5.000 | 3.000 | 0.000 | 2.000 |
| text | text_top8 | 18 | 0.625 | 0.625 | 1.000 | 5.000 | 8.000 | 3.000 | 0.000 |
| xbrl | xbrl_expanded_fact16_path15 | 18 | 0.750 | 0.710 | 1.000 | 20.778 | 28.167 | 7.389 | 0.000 |
| xbrl | xbrl_fact_only | 18 | 0.594 | 0.545 | 0.594 | 20.778 | 11.889 | 0.000 | 8.889 |
| xbrl | xbrl_fact_top8_paths_current | 18 | 0.807 | 0.818 | 0.807 | 20.778 | 16.889 | 0.000 | 3.889 |

Interpretation:

- `text_top3` and `text_top8` vary the text-retrieval source budget around the implemented top-5 rule.
- `xbrl_fact_only` removes relation-path evidence and therefore measures how much of the XBRL source environment depends on linkbase relations rather than instance facts alone.
- `xbrl_expanded_fact16_path15` expands facts from 12 to 16 and relation paths from 10 to 15 when available.
- Because no LLM outputs are regenerated, these diagnostics should be reported as source-environment perturbation evidence rather than output-level robustness evidence.
