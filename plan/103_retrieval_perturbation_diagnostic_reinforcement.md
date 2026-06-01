# Retrieval Perturbation Diagnostic Reinforcement

## Purpose

This note documents the added Tier 1 source-environment perturbation diagnostic. The purpose is to respond to reviewer concern that sensitivity guidance alone may look underdeveloped. The diagnostic varies retrieval-source selection without re-running the LLM, so it strengthens protocol validation while preserving the manuscript boundary that the paper is not a model-performance benchmark.

## Implemented Artifact

New script:

- `scripts/analyze_retrieval_perturbation_diagnostics.py`

New outputs:

- `data/processed/sensitivity/retrieval_perturbation_diagnostics.csv`
- `data/processed/sensitivity/retrieval_perturbation_summary_by_variant.csv`
- `data/processed/sensitivity/retrieval_perturbation_summary.md`

The same files are included in the submission replication package.

## Diagnostic Scope

The diagnostic covers 18 filer-construct cells: nine filers by two constructs. For each cell, it reconstructs the implemented source-selection environment and compares bounded retrieval variants:

| Variant Group | Variant | Purpose |
|---|---|---|
| Text | top-3 chunks instead of top-5 | Tests lower text source budget |
| Text | top-8 chunks instead of top-5 | Tests higher text source budget |
| XBRL | facts only; relation paths removed | Tests whether relational retrieval differs from fact retrieval alone |
| XBRL | fact budget reduced to top-8; paths unchanged | Tests lower fact source budget |
| XBRL | fact budget expanded to top-16 and path budget to top-15 | Tests higher structured source budget |

## Results

| Variant Group | Variant | Cells | Mean Jaccard | Mean Retained Share |
|---|---|---:|---:|---:|
| Text | top-3 chunks | 18 | 0.600 | 0.600 |
| Text | top-8 chunks | 18 | 0.625 | 1.000 |
| XBRL | facts only | 18 | 0.594 | 0.594 |
| XBRL | fact top-8, paths unchanged | 18 | 0.807 | 0.807 |
| XBRL | fact top-16, path top-15 | 18 | 0.750 | 1.000 |

## Reviewer-Facing Interpretation

The diagnostic strengthens the paper in two ways. First, it makes retrieval-stage source-composition changes observable: reviewers can see how much source selection changes under bounded perturbations before any LLM inference occurs. Second, it directly supports the novelty of XBRL relational retrieval. Removing relation paths lowers the mean source-set Jaccard to 0.594, showing that the implemented relational retrieval environment is materially different from fact retrieval alone.

## Boundary

This diagnostic is not an LLM output-sensitivity test. It does not show whether model-generated claims remain stable under changed prompts, matched token budgets, reversed evidence order, or different models. Those tests remain Tier 2 requirements for studies that claim model-performance effects, retrieval superiority, or audit-judgment quality. For the current AJPT methodology framing, the diagnostic is best described as retrieval-stage protocol-validation evidence.
