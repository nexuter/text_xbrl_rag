# Additional Reviewer Gap Audit And Hybrid Mechanism Reinforcement

## Purpose

This note records the additional reviewer-facing improvement made after adding context-volume and source-environment perturbation diagnostics. The remaining P1 reviewer risk was that hybrid integration failure might still look under-theorized or anecdotal.

## Additional Gap Identified

The revised manuscript already reported that, among 89 hybrid-condition claims, 8 used both text and XBRL, 61 used text only, and 20 used XBRL only. However, the reviewer audit still flagged the absence of a separate mechanism diagnostic file. Without such a file, a reviewer could argue that the integration-failure claim is descriptive rather than systematically coded.

## Improvement Implemented

New script:

- `scripts/analyze_hybrid_integration_mechanisms.py`

New outputs:

- `data/processed/coding/hybrid_integration_mechanisms.csv`
- `data/processed/coding/hybrid_integration_mechanism_summary.csv`
- `data/processed/coding/hybrid_integration_mechanism_by_construct.csv`
- `data/processed/coding/hybrid_integration_mechanism_summary.md`

The same files are included in the submission replication package.

## Key Result

| Mechanism | Claims | Share |
|---|---:|---:|
| Integrated text-XBRL bridge | 8 | 9.0% |
| Text-only within hybrid | 61 | 68.5% |
| XBRL-only within hybrid | 20 | 22.5% |

By construct, inventory has 7 integrated, 27 text-only, and 10 XBRL-only hybrid claims. Revenue has 1 integrated, 34 text-only, and 10 XBRL-only hybrid claims.

## Reviewer-Facing Value

This reinforcement addresses the concern that hybrid integration failure was under-theorized. It shows that non-integration is mainly a one-layer-use mechanism rather than a case of claims citing both layers but failing to synthesize them. This supports the paper's central measurement argument: response-level condition labels are insufficient because evidence use must be coded at the claim level.

## Boundary

The mechanism counts are protocol diagnostics. They should not be framed as population-level failure frequencies or evidence that a model is generally bad at integration. Stronger model-performance claims would require broader sampling, prompt/retrieval sensitivity, expert coding, and nested statistical analysis.
