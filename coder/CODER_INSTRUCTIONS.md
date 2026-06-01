# Independent Coder Instructions

## Assignment

You will code 120 LLM-generated audit-research claims. Each row is one claim. Your task is to evaluate the claim against the provided retrieval context and source references.

Do not evaluate the general quality of the LLM. Do not use outside company knowledge, internet searches, or professional assumptions not supported by the provided context. Code only from the claim text, source IDs, retrieval context, and LLM output included in the files you receive.

## Files To Use

Use these files:

1. `CODING_PROTOCOL.md`: full coding protocol.
2. `CODING_CODEBOOK.md`: allowed values and short definitions.
3. `claim_evidence_packet.csv`: retrieval context and LLM output for each claim.
4. `coder_coding_form_template.csv`: blank input form.

## Workflow

1. Open `coder_coding_form_template.csv` and save a personal working copy.
2. For each `global_claim_id`, find the same `global_claim_id` in `claim_evidence_packet.csv`.
3. Read the claim text.
4. Review the listed `text_source_ids`, `xbrl_source_ids`, retrieval context, and LLM output text.
5. Enter your coder identifier in `coder_id` for every row.
6. Enter codes only in the blank coding columns of your working copy.
7. Add a short note when a code is uncertain, partial, or ambiguous.
8. Do not change the fixed claim metadata columns.

## Columns To Complete

Complete these columns:

| Column | Required? | Allowed Values |
|---|---|---|
| `coder_id` | Yes | assigned coder identifier |
| `claim_segmentation_agreement` | Yes | `1`, `0`, `NA` |
| `claim_kind_code` | Yes | `factual`, `risk_assertion`, `integration`, `boundary`, `other` |
| `evidence_use_type_code` | Yes | `none`, `text_only`, `xbrl_only`, `text_xbrl_integrated`, `ambiguous` |
| `text_supported_code` | Yes | `1`, `0.5`, `0`, `NA` |
| `graph_valid_code` | Yes | `1`, `0.5`, `0`, `NA` |
| `integrated_code` | Yes | `1`, `0.5`, `0`, `NA` |
| `audit_boundary_note` | Yes for risk/assertion or uncertain claims | Free text |
| `confidence_code` | Yes | `high`, `medium`, `low` |
| `coder_notes` | Optional but encouraged | Free text |

## Important Coding Rules

- Code evidence use from the claim itself, not from the retrieval condition label.
- A hybrid condition does not automatically mean integrated evidence use.
- XBRL facts and relation paths are management-reported data, not independent audit evidence.
- Use `0.5` only when support is partial, incomplete, or inferentially extended.
- Use `audit_boundary_note` to flag overclaims, missing evidence, or claims that would require audit-domain judgment beyond the provided filing context.

Integrated-code rule:

- Code `integrated_code` for every claim.
- Use `0` when the claim uses only text, only XBRL, no source, conflicting sources, or does not connect available text and XBRL evidence.
- Do not use `NA` merely because the condition is text-only, XBRL-only, LLM-only, or because the claim uses one evidence type.
- For text-only, XBRL-only, and LLM-only claims, `integrated_code` should normally be `0`, not `NA`.
- Use `NA` only when the row cannot be evaluated for integration because it is not a substantive evidence-use claim, such as a pure segmentation error or unusable/ambiguous row.

Integrated-code examples:

| Scenario | Code |
|---|---|
| Hybrid condition, XBRL-only numeric claim | `0` |
| Hybrid condition, text-only risk claim | `0` |
| Hybrid condition, text plus XBRL jointly supporting one factual claim | `1` |
| Text and XBRL both mentioned but not connected | `0.5` |
| LLM-only insufficient-context claim | `0` |

## Return File

Return only your completed coding form.
