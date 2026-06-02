# Independent Claim-Coding Protocol

## Purpose

This protocol converts the preliminary author-coded claim archive into an independent coding instrument. It is designed for reviewer-evaluable validation of the measurement protocol used in the methodological demonstration. It should not be used to claim final audit-judgment correctness unless coders have appropriate audit-domain expertise and the study reports reliability and reconciliation evidence.

## Coding Sample

The coder-ready sample is stored in the file named `independent_coding_sample.csv`.

The sample contains 120 claims from the 281-claim archive:

- all 89 hybrid-condition claims;
- 12 LLM-only claims;
- 10 XBRL-only claims;
- 9 text-only claims.

This sampling design intentionally oversamples hybrid claims because the paper's most reviewer-sensitive measurement question is whether claims in a hybrid retrieval condition actually integrate text and XBRL evidence.

## Definition Of A Claim

A claim is an independently assessable assertion in an LLM output. Coders should apply the following segmentation rules:

1. Split factual amount, date, period, or account-balance statements from audit-risk interpretations.
2. Split causal explanations from factual premises when they require different evidence.
3. Split multi-account or multi-assertion sentences when source requirements differ.
4. Preserve caveats and limitations as part of the claim when they determine the audit-boundary assessment.
5. Code insufficient-context statements as claims only when they make a source-boundary assertion, such as stating that the supplied context is insufficient to identify a filing-specific risk.

## Variables To Code

### Claim Segmentation Agreement

Code whether the provided claim text is an independently assessable assertion.

- `1`: agree with the segmentation.
- `0`: disagree with the segmentation.
- `NA`: cannot assess from the provided output/context references.

If `0`, explain whether the claim should be split, merged, or excluded.

### Claim Kind

Code the dominant claim type.

- `factual`: a bounded factual statement about an amount, date, period, policy, or disclosed event.
- `risk_assertion`: an audit-risk, assertion-level, or control-relevant inference.
- `integration`: a claim that explicitly connects narrative text and XBRL/fact evidence.
- `boundary`: a claim about insufficient context, missing evidence, or limits of inference.
- `other`: use only when no category fits; explain in notes.

### Evidence-Use Type

Code the evidence actually used by the claim, not the retrieval condition label.

- `none`: no filing-specific source is used.
- `text_only`: the claim relies on text evidence only.
- `xbrl_only`: the claim relies on XBRL fact or relation evidence only.
- `text_xbrl_integrated`: the claim uses text and XBRL together in the same inferential bridge.
- `ambiguous`: source use cannot be determined from the claim and references.

### Text-Supported Correctness

Code whether the claim is supported by the cited or supplied text source.

- `1`: supported.
- `0.5`: partially supported or inferentially extended beyond the text.
- `0`: unsupported or contradicted.
- `NA`: no text evidence is relevant or available.

### Graph-Valid Correctness

Code whether the claim is consistent with the supplied XBRL fact, context, concept, unit, period, or relation path.

- `1`: graph-valid.
- `0.5`: partially graph-valid, incomplete, or requires additional context.
- `0`: not graph-valid or contradicted by the supplied structured data.
- `NA`: no XBRL evidence is relevant or available.

### Integrated Correctness

Code whether the claim integrates text and XBRL evidence. This variable applies to every claim in the validation sample. Do not infer integration from a hybrid condition label, and do not use `NA` merely because the retrieval condition is text-only, XBRL-only, LLM-only, or because the claim uses only one evidence type. For text-only, XBRL-only, and LLM-only claims, `integrated_code` should normally be `0`, not `NA`.

- `1`: text and XBRL evidence are jointly used in a coherent inferential bridge.
- `0.5`: text and XBRL both appear, but the bridge is incomplete, mostly juxtaposed, or weakly connected.
- `0`: the claim uses only text, only XBRL, no source, conflicting sources, or the available evidence types are not integrated.
- `NA`: use only when the row cannot be evaluated for integration because it is not a substantive evidence-use claim, such as a pure segmentation error or unusable/ambiguous row.

Examples:

| Scenario | Integrated Code |
|---|---|
| Hybrid condition, XBRL-only numeric claim | `0` |
| Hybrid condition, text-only risk claim | `0` |
| Hybrid condition, text plus XBRL jointly supporting one factual claim | `1` |
| Text and XBRL both mentioned but not connected | `0.5` |
| LLM-only insufficient-context claim | `0` |

### Audit Boundary Note

Audit-boundary assessment should be coded qualitatively unless coders are audit-domain experts and the study reports reliability evidence for stronger audit-judgment claims. Coders should note whether the claim:

- stays within source-supported or graph-valid boundaries;
- overreads management-reported XBRL as audit evidence;
- makes an audit-risk inference that would require additional evidence;
- appropriately states a limitation.

## Reliability And Reconciliation

The minimum reviewer-facing validation exercise should use two independent coders.

Report:

- percent agreement for claim segmentation, claim kind, evidence-use type, and integrated correctness;
- Cohen's kappa for nominal variables with sufficient category variation;
- weighted agreement or Krippendorff's alpha for ordinal correctness variables where feasible;
- reconciliation procedures and examples of ambiguous claims.

Do not report audit-boundary means as model-performance or audit-judgment evidence unless audit-domain expert coding, reliability evidence, and reconciliation procedures are completed.

## Current Status

The coding instrument has been completed by two independent coders for a 120-claim validation sample. The completed results and reliability summary are reported in the independent coding results file and intercoder reliability summary. The results support use of the claim-level coding protocol as a methodological diagnostic, while preserving the boundary that the demonstration is not a model-performance validation or final audit-judgment study.
