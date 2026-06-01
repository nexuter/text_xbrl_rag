# Coding Codebook

## Claim Segmentation Agreement

| Code | Meaning |
|---|---|
| `1` | The claim is an independently assessable assertion. |
| `0` | The claim should be split, merged, or excluded. Explain in notes. |
| `NA` | Cannot assess from the provided materials. |

## Claim Kind

| Code | Meaning |
|---|---|
| `factual` | Bounded factual statement about an amount, date, period, policy, account balance, or disclosed event. |
| `risk_assertion` | Audit-risk, assertion-level, control-relevant, or audit-planning inference. |
| `integration` | Claim explicitly connects narrative text and XBRL/fact evidence. |
| `boundary` | Claim states insufficient context, missing evidence, or limits of inference. |
| `other` | No category fits. Explain in notes. |

## Evidence-Use Type

| Code | Meaning |
|---|---|
| `none` | No filing-specific source is used. |
| `text_only` | Claim relies on narrative text evidence only. |
| `xbrl_only` | Claim relies on XBRL fact or relation evidence only. |
| `text_xbrl_integrated` | Claim uses text and XBRL together in the same inferential bridge. |
| `ambiguous` | Source use cannot be determined. |

## Text-Supported Correctness

| Code | Meaning |
|---|---|
| `1` | Claim is supported by the supplied/cited text. |
| `0.5` | Claim is partially supported or extends beyond the text. |
| `0` | Claim is unsupported or contradicted by the text. |
| `NA` | Text support is not applicable. |

## Graph-Valid Correctness

| Code | Meaning |
|---|---|
| `1` | Claim is consistent with the supplied XBRL fact, context, period, unit, concept, or relation path. |
| `0.5` | Claim is partially graph-valid, incomplete, or requires additional context. |
| `0` | Claim is not graph-valid or is contradicted by the structured data. |
| `NA` | Graph validity is not applicable. |

## Integrated Correctness

Use `integrated_code` for every claim in the validation sample. Do not use `NA` merely because the retrieval condition is text-only, XBRL-only, LLM-only, or because the claim uses only one evidence type.

| Code | Meaning |
|---|---|
| `1` | Text and XBRL evidence are jointly used in a coherent inferential bridge. |
| `0.5` | Text and XBRL both appear, but integration is incomplete, mostly juxtaposed, or weakly connected. |
| `0` | The claim uses only text, only XBRL, no source, conflicting sources, or available evidence types are not integrated. |
| `NA` | Use only when the row cannot be evaluated for integration because it is not a substantive evidence-use claim, such as a pure segmentation error or unusable/ambiguous row. |

Examples:

| Scenario | Code |
|---|---|
| Hybrid condition, XBRL-only numeric claim | `0` |
| Hybrid condition, text-only risk claim | `0` |
| Hybrid condition, text plus XBRL jointly supporting one factual claim | `1` |
| Text and XBRL both mentioned but not connected | `0.5` |
| LLM-only insufficient-context claim | `0` |

## Confidence Code

| Code | Meaning |
|---|---|
| `high` | Code is clear from the provided materials. |
| `medium` | Code is reasonable but involves some judgment. |
| `low` | Code is uncertain; explain in notes. |
