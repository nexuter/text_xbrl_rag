# Recoded Independent Coding Pre-Application Review

## Purpose

This note reviews the two newly completed independent coder files before replacing the manuscript-facing independent-coding results. The review focuses on whether the revised `integrated_code` instruction solved the prior `0` versus `NA` ambiguity and whether any remaining disagreements should be reconciled before manuscript application.

## Files Reviewed

- `coder/coder_1_completed_coding_form.csv`
- `coder/coder2_completed_coding_form.csv`
- `coder/claim_evidence_packet.csv`

## Completeness And Format Checks

| Check | Result |
|---|---:|
| Rows per coder | 120 / 120 |
| Missing claim IDs | 0 |
| Duplicate claim IDs | 0 |
| Blank required coding cells | 0 |
| Invalid allowed-value codes | 0 |
| Coder 1 identifier | `coder_1` |
| Coder 2 identifier | `Coder 2` |

The recoded files are structurally usable. Before final analysis output, coder identifiers can either remain as entered or be normalized for cleaner reporting.

## Main Reliability Results From Recoded Files

| Variable | N | Agreement | Percent Agreement | Kappa / Weighted Kappa |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Integrated-Code Review

The revised instruction appears to have solved the prior ambiguity.

| Integrated Code | Coder 1 | Coder 2 |
|---|---:|---:|
| `0` | 112 | 112 |
| `1` | 8 | 8 |
| `0.5` | 0 | 0 |
| `NA` | 0 | 0 |

Condition-level distribution is also consistent:

| Condition | Coder 1 | Coder 2 |
|---|---|---|
| Hybrid | 81 coded `0`, 8 coded `1` | 81 coded `0`, 8 coded `1` |
| LLM-only | 12 coded `0` | 12 coded `0` |
| Text-only | 9 coded `0` | 9 coded `0` |
| XBRL-only | 10 coded `0` | 10 coded `0` |

This is exactly the intended behavior under the revised protocol: non-integrated claims receive `0`, not `NA`, even when the retrieval condition is text-only, XBRL-only, LLM-only, or hybrid-but-one-source.

## Remaining Disagreements

Only three substantive claim-level disagreements remain outside confidence coding.

| Claim ID | Disagreement | Review Assessment |
|---|---|---|
| `MAIN-C043` | Coder 1: `risk_assertion`, text support `0.5`; Coder 2: `factual`, text support `1` | The claim states an accounting-policy dependency: revenue recognition for the Nestle prepaid royalty depends on performance obligations. It does not itself make an audit-risk assertion. Reconcile to `factual`, text support `1`, graph validity `NA`, integrated `0`. |
| `EXT-C044` | Coder 1: `risk_assertion`, text support `0.5`; Coder 2: `factual`, text support `1` | The claim states disclosed gift-card breakage accounting policy. It is source-supported and does not itself make an audit-risk assertion. Reconcile to `factual`, text support `1`, graph validity `NA`, integrated `0`. |
| `EXT-C045` | Coder 1: `risk_assertion`, text support `0.5`, graph validity `0.5`; Coder 2: `factual`, text support `1`, graph validity `1` | The claim states the gift-card revenue recognition timing and is supported by both narrative text and XBRL fact `F-HD-0044` for the six-month redemption period. Reconcile to `factual`, text support `1`, graph validity `1`, integrated `1`. |

The disagreements are not threatening to the paper's core contribution. They show that accounting-policy descriptions can be miscoded as audit-risk assertions when the coder reads "depends on" or "estimate" as implying audit risk. The coding protocol can mention this boundary in the reconciliation discussion if needed.

## Comparison To Previous Independent Coding Results

The prior combined results had substantial `integrated_code = NA` usage:

| Integrated Code | Prior Combined Results | Recoded Combined Results |
|---|---:|---:|
| `0` | 163 | 224 |
| `1` | 10 | 16 |
| `0.5` | 5 | 0 |
| `NA` | 62 | 0 |

The new results are more internally consistent with the revised instruction and should replace the prior independent-coding results after reconciliation.

## Recommendation Before Manuscript Application

Use the recoded files as the authoritative independent coding input, but do not simply overwrite manuscript-facing reliability tables without documenting reconciliation.

Recommended sequence:

1. Normalize coder identifiers only for clean output labels if desired.
2. Create updated independent-coding combined results from the two recoded files.
3. Produce a disagreement file showing only the remaining focal disagreements.
4. Add a short reconciliation note for `MAIN-C043`, `EXT-C044`, and `EXT-C045`.
5. Update manuscript/supplement reliability language to emphasize:
   - 100% agreement on evidence-use type and integrated correctness;
   - the revised protocol eliminates the prior `0`/`NA` ambiguity;
   - remaining disagreements involve factual versus risk/assertion classification for accounting-policy statements, not the relational-retrieval construct.

## Reviewer-Facing Interpretation

The recoded evidence is strong enough to support the methodological claim that the paper's claim-level measurement protocol can be applied reliably by independent coders. It is especially strong for the paper's central construct, integrated text-XBRL evidence use. The remaining differences are minor, explainable, and useful for refining the coding protocol rather than undermining it.

