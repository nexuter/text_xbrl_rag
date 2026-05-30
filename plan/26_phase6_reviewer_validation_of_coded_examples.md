# Phase 6 Reviewer Validation of Coded Examples

## Purpose

This memo performs a reviewer-style validation of selected claim-level coding examples from the `gemma4:31b` full run.

The goal is to identify manuscript-ready examples and remove overclaimed interpretations before drafting the demonstration section.

## Validation Approach

The validation checked:

- whether the claim appears in the LLM output;
- whether the cited source IDs appear in the retrieved context;
- whether the preliminary correctness coding is defensible;
- whether the example supports the paper's methodological argument;
- whether the example would survive an AJPT-style reviewer challenge.

## Example 1: Hybrid Retrieval Can Support Direct Text-XBRL Corroboration

Claim:

> As of September 28, 2025, inventory reserves were $56.6 million.

Coding metadata:

| Field | Value |
|---|---|
| Claim ID | C058 |
| Filer | Starbucks |
| Construct | Inventory valuation |
| Retrieval condition | Hybrid |
| Text source | `T-SBUX-INVENTORY-015` |
| XBRL source | `F-SBUX-0034` |
| Text-supported | 1 |
| Graph-valid | 1 |
| Audit-valid | 1 |
| Integrated | 1 |

Source verification:

- The text chunk states that inventory reserves were $56.6 million as of September 28, 2025.
- The XBRL fact `F-SBUX-0034` reports `InventoryValuationReserves` of 56.6 million for `2025-09-28`.

Reviewer assessment:

This is a strong, bounded integrated-correctness example. It should be used as a factual corroboration example, not as evidence that hybrid retrieval improves audit reasoning generally.

Manuscript use:

> Hybrid retrieval can support direct narrative-XBRL corroboration when the model cites both a disclosure text chunk and a matching XBRL fact for the same accounting item and period.

## Example 2: Hybrid Retrieval Does Not Guarantee Integrated Reasoning

Claim:

> The increase in the current refund liability from $799 million (as of 2024-05-31) to $1.277 billion (as of 2025-05-31) presents a risk cue for the valuation assertion of revenue.

Coding metadata:

| Field | Value |
|---|---|
| Claim ID | C013 |
| Filer | Nike |
| Construct | Revenue recognition |
| Retrieval condition | Hybrid |
| Text source | none |
| XBRL sources | `F-NKE-0253`; `F-NKE-0252` |
| Text-supported | 0 |
| Graph-valid | 0.5 |
| Audit-valid | 1, preliminary |
| Integrated | 0.5 |
| Failure mode | Integration failure |

Source verification:

- `F-NKE-0253` reports current refund liability of $799 million as of 2024-05-31.
- `F-NKE-0252` reports current refund liability of $1.277 billion as of 2025-05-31.
- The hybrid context also contains Nike revenue narrative, but the claim does not use that narrative.

Reviewer assessment:

This is a useful cautionary example. The claim is graph-grounded and professionally plausible as a risk cue, but it does not demonstrate narrative-XBRL integration. It should not be coded as fully integrated merely because the prompt condition was hybrid.

Manuscript use:

> Hybrid retrieval creates the opportunity for integration, but claim-level coding can show that an output remains effectively XBRL-only.

## Example 3: Hybrid Retrieval Can Produce Text-Only Risk Cues

Claim:

> The stated risk that failures in providing reliable, secure, and user-friendly digital commerce platforms could result in the loss of digital commerce sales indicates a risk cue for the completeness and occurrence assertions of revenue.

Coding metadata:

| Field | Value |
|---|---|
| Claim ID | C014 |
| Filer | Nike |
| Construct | Revenue recognition |
| Retrieval condition | Hybrid |
| Text source | `T-NKE-REVENUE-021` |
| XBRL source | none |
| Text-supported | 0.5 |
| Graph-valid | NA |
| Audit-valid | 1, preliminary |
| Integrated | 0.5 |
| Failure mode | Integration failure |

Source verification:

- `T-NKE-REVENUE-021` describes digital commerce platform risk and potential loss of digital commerce and other sales.
- The claim maps this business risk to revenue completeness and occurrence assertions.
- No XBRL fact or relation path is used in the claim.

Reviewer assessment:

This is a useful example of text-supported audit reasoning that appears in a hybrid condition but does not use XBRL. It supports the separability dimension of retrieval-environment validity.

Manuscript use:

> Coding by retrieval condition alone is insufficient. A hybrid prompt can produce a text-only claim, so researchers must code the evidence actually used by each claim.

## Example 4: LLM-Only Baseline Supports Traceability Diagnosis

Claim:

> The provided context is insufficient to identify any audit-relevant risk cues or assertion-mapping considerations for revenue recognition for Nike, Inc. for the specified period.

Coding metadata:

| Field | Value |
|---|---|
| Claim ID | C016 |
| Filer | Nike |
| Construct | Revenue recognition |
| Retrieval condition | LLM-only |
| Text source | none |
| XBRL source | none |
| Audit-valid | 1 |

Source verification:

- The LLM-only baseline prompt contains no retrieved filing context.
- The model appropriately refuses to generate filing-specific risk cues.

Reviewer assessment:

This is a strong diagnostic example. It reduces concern that the main demonstration is driven entirely by model pretraining or general company knowledge. It does not eliminate pretraining risk, but it shows that the prompt/model configuration respected the no-context condition.

Manuscript use:

> The no-context baseline functions as a traceability diagnostic rather than a performance baseline.

## Corrected Interpretation

The earlier preliminary interpretation that Starbucks inventory hybrid retrieval produced five integrated claims was too generous. After correcting source-ID parsing, the better interpretation is:

- One Starbucks inventory hybrid claim directly integrates text and XBRL.
- Other Starbucks inventory hybrid claims are text-supported risk cues produced under a hybrid condition.
- This strengthens, rather than weakens, the paper's methodological contribution because it shows why claim-level evidence-use coding is necessary.

## Reviewer-Level Verdict

The selected examples are strong enough to support the methodological demonstration if the manuscript uses them carefully.

Acceptable claims:

- Hybrid retrieval can support integrated correctness in bounded factual corroboration cases.
- Hybrid retrieval does not guarantee integrated reasoning.
- XBRL relational retrieval can ground reported-accounting facts and risk cues, but audit-valid inference still requires qualification.
- LLM-only baselines are useful traceability diagnostics.

Claims to avoid:

- Hybrid retrieval is more accurate.
- Hybrid retrieval is generally superior.
- XBRL improves audit reasoning by itself.
- The high preliminary audit-valid score proves the model has audit expertise.

## Required Next Step

Use these validated examples to draft the demonstration subsection and construct a manuscript-ready table that reports selected claims, source mapping, correctness-layer coding, and inference consequences.

