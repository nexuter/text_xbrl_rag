# Context-Volume Diagnostic Reinforcement

## Purpose

This reinforcement addresses the remaining reviewer concern that separability and token-budget issues were acknowledged but not sufficiently evidenced. The added diagnostic does not claim to be a full sensitivity test. It makes information-volume differences across retrieval conditions observable, which strengthens the paper's Tier 1 protocol-validation evidence and clarifies what Tier 2 model-validation studies must control.

## Files Created

- `scripts/analyze_context_diagnostics.py`
- `data/processed/retrieval_contexts/context_volume_diagnostics.csv`
- `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv`
- `data/processed/retrieval_contexts/context_volume_diagnostics_summary.md`

The script and outputs were copied into the submission replication package.

## Diagnostic Scope

The diagnostic covers all 72 retrieval contexts:

- 9 filers;
- 2 constructs;
- 4 retrieval conditions;
- 18 contexts per condition.

## Condition-Level Results

| Condition | Contexts | Mean Context Words | Median | Min | Max | Mean Prompt Words | Mean Text Chunks | Mean XBRL Facts | Mean XBRL Paths |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Hybrid | 18 | 691.3 | 718.5 | 278 | 885 | 862.9 | 5.0 | 11.9 | 8.9 |
| LLM-only | 18 | 10.0 | 10.0 | 10 | 10 | 181.6 | 0.0 | 0.0 | 0.0 |
| Text | 18 | 602.6 | 594.0 | 249 | 929 | 774.2 | 5.0 | 0.0 | 0.0 |
| XBRL | 18 | 524.2 | 542.5 | 192 | 666 | 695.8 | 0.0 | 11.9 | 8.9 |

## Hybrid Separability Result

Across the 18 hybrid contexts:

- mean text/XBRL word-imbalance ratio: 1.37;
- median ratio: 1.32;
- maximum ratio: 2.15.

This documents that hybrid contexts do not merely differ by label; they contain both narrative and structured information and are modestly larger than single-source retrieval contexts. That difference is a separability issue for performance studies, which is why the manuscript continues to avoid retrieval-superiority claims.

## Manuscript Changes

Updated:

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/README_REPLICATION.md`
- `README_REPLICATION.md`
- `submission/Replication_Package_Manifest.md`
- `submission/replication_package/README_REPLICATION.md`
- `submission/replication_package/AUTHORITATIVE_FILES.md`
- `submission/replication_package/PACKAGE_CONTENTS.md`

## Reviewer-Facing Interpretation

The added diagnostic moves the paper beyond purely verbal separability caveats. Reviewers can now inspect actual context and prompt volumes by retrieval condition. The evidence still does not support model-performance claims, but it gives reviewers a concrete basis for evaluating the current protocol-validation boundary and the Tier 2 matched-budget sensitivity recommendation.

## Remaining Boundary

The paper still does not include:

- matched-budget hybrid reruns;
- evidence-order reversal;
- prompt-variation sensitivity;
- top-k or traversal-depth perturbation;
- cross-model robustness.

These remain Tier 2 requirements for studies that claim model-performance effects, retrieval-method superiority, or failure-mode prevalence.

