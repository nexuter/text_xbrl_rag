# Independent Coding Reconciliation Notes

## Purpose

This note documents the limited reconciliation review conducted after two independent coders recoded the 120-claim validation sample under the revised `integrated_code` instruction. The purpose is to preserve transparency before applying the recoded reliability results to the manuscript and online supplement.

## Recoded Reliability Snapshot

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Integrated-Code Resolution

The revised instruction resolved the prior ambiguity between `0` and `NA`.

| Integrated Code | Coder 1 | Coder 2 |
|---|---:|---:|
| `0` | 112 | 112 |
| `1` | 8 | 8 |
| `0.5` | 0 | 0 |
| `NA` | 0 | 0 |

The coders agreed that text-only, XBRL-only, LLM-only, and hybrid-but-one-source claims should normally receive `integrated_code = 0`, not `NA`.

## Focal Reconciliation Items

| Claim ID | Claim | Coder Difference | Reconciliation Assessment |
|---|---|---|---|
| `MAIN-C043` | Revenue recognition for the Nestle prepaid royalty depends on the assessment of performance obligations. | Coder 1 coded `risk_assertion`, text support `0.5`; Coder 2 coded `factual`, text support `1`. | Reconcile as a factual accounting-policy statement: `factual`, text support `1`, graph validity `NA`, integrated correctness `0`. |
| `EXT-C044` | The recognition of gift card breakage income is based on an estimate of the portion of outstanding gift card balances not expected to be redeemed. | Coder 1 coded `risk_assertion`, text support `0.5`; Coder 2 coded `factual`, text support `1`. | Reconcile as a factual accounting-policy statement: `factual`, text support `1`, graph validity `NA`, integrated correctness `0`. |
| `EXT-C045` | Revenue for gift cards is recognized upon redemption, which generally occurs within six months of issuance. | Coder 1 coded `risk_assertion`, text support `0.5`, graph validity `0.5`; Coder 2 coded `factual`, text support `1`, graph validity `1`. | Reconcile as a factual source-supported claim: `factual`, text support `1`, graph validity `1`, integrated correctness `1`. |

## Manuscript Implication

The recoded evidence supports the manuscript's claim that the measurement protocol is reliably applicable by independent coders for the paper's core retrieval-validity variables. It does not convert the demonstration into a model-performance test or final audit-validity study.

