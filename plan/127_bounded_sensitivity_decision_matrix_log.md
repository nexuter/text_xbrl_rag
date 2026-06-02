# Bounded Sensitivity Decision Matrix Log

## Purpose

This revision implements SR-09 from the second-revision workflow: bounded separability and stability diagnostics. The goal is to make retrieval-stage sensitivity reviewer-inspectable without converting the paper into a model-performance benchmark.

## Implemented Work

1. Added `scripts/analyze_bounded_sensitivity_decision_matrix.py`.
2. Generated cell-level and variant-level sensitivity decision outputs:
   - `data/processed/sensitivity/bounded_sensitivity_decision_matrix_by_cell.csv`
   - `data/processed/sensitivity/bounded_sensitivity_variant_decisions.csv`
   - `data/processed/sensitivity/bounded_sensitivity_decision_summary.md`
3. Copied the script and outputs into the replication package.
4. Revised the main manuscript sensitivity paragraph to report the bounded decision matrix.
5. Revised Appendix I to add a bounded sensitivity decision matrix and clarify interpretation boundaries.
6. Updated replication README files to describe the decision-matrix artifact.
7. Regenerated root and replication-package checksum manifests.

## Diagnostic Scope

- Filer-construct cells reviewed: 18
- Perturbation rows reviewed: 90
- Variants reviewed:
  - text top-3
  - text top-8
  - XBRL facts only, relation paths removed
  - XBRL fact budget reduced to top-8, paths unchanged
  - XBRL fact budget expanded to top-16 and path budget to top-15

## Key Results

| Variant | Cells | Mean Jaccard | Minimum Jaccard | Cells Below 0.60 | Decision Band |
|---|---:|---:|---:|---:|---|
| text_top3 | 18 | 0.600 | 0.600 | 0 | moderate_source_environment_change |
| text_top8 | 18 | 0.625 | 0.625 | 0 | moderate_source_environment_change |
| xbrl_fact_only | 18 | 0.594 | 0.524 | 16 | material_source_environment_change |
| xbrl_fact_top8_paths_current | 18 | 0.807 | 0.667 | 0 | bounded_source_environment_change |
| xbrl_expanded_fact16_path15 | 18 | 0.750 | 0.710 | 0 | moderate_source_environment_change |

At the cell level, 17 of 18 filer-construct cells receive a high separability-attention flag and one receives a moderate flag. These flags are not model-performance failure rates. They identify cells where future Tier 2 model-validation studies should add matched-budget, evidence-order, prompt-sensitivity, and output-level rerun checks before making claims about retrieval superiority or model performance.

## Reviewer-Facing Interpretation

The diagnostic strengthens the methodological claim that XBRL relational retrieval is separable from fact-only XBRL retrieval. Removing relation paths materially changes the XBRL source environment in most cells. The result supports retrieval-stage source-composition transparency and construct-alignment review.

The diagnostic does not show that relation paths improve LLM output quality. It does not estimate model performance, audit-judgment accuracy, or failure-mode prevalence.

## QA

- `python -m py_compile scripts/analyze_bounded_sensitivity_decision_matrix.py` passed.
- Root checksum manifest regenerated with 418 hashed files.
- Replication-package checksum manifest regenerated with 418 hashed files.
- New decision outputs were copied to `submission/replication_package/data/processed/sensitivity/`.
- New script was copied to `submission/replication_package/scripts/`.

## Remaining Boundary

The paper still should not claim completed matched-budget, evidence-order, prompt-variation, cross-model, or output-level sensitivity testing. Those remain Tier 2 model-validation requirements.
