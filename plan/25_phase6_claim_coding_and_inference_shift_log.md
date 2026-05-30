# Phase 6 Claim Coding and Inference Shift Log

## Purpose

This file records the first claim-level segmentation, preliminary correctness coding, failure-mode identification, and inference-shift table generated from the `gemma4:31b` full run.

## Execution

Script:

```text
python scripts/code_llm_claims.py
```

Input:

- `data/processed/llm_outputs/gemma4_31b_full/text/*_output.txt`
- `data/processed/retrieval_contexts/context_manifest.csv`

Outputs:

- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/coding_summary_by_condition.csv`
- `data/processed/coding/inference_shift_table_prelim.csv`
- `data/processed/coding/failure_mode_examples_prelim.csv`
- `data/processed/coding/claim_coding_summary.md`

## Coding Status

The coding is preliminary author coding.

This is sufficient for developing the methodological demonstration, identifying candidate examples, and preparing the next expert-review step. It is not yet sufficient for final manuscript claims about audit-valid or integrated correctness.

Reviewer-facing language:

> We use automated segmentation and preliminary author coding to organize the demonstration outputs. Audit-valid and integrated correctness are then subject to expert review before being treated as evidence in the manuscript.

## Claim Segmentation Result

The script segmented and preliminarily coded 94 claims from the 24 full-run outputs.

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 15 | 6 | 9 | 0 | 0.63 | 0.88 | 1.00 | 0.60 |
| hybrid | revenue | 15 | 6 | 9 | 0 | 0.47 | 0.88 | 1.00 | 0.50 |
| llm_only | inventory | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| llm_only | revenue | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| text | inventory | 13 | 5 | 8 | 0 | 0.69 | NA | 1.00 | NA |
| text | revenue | 15 | 6 | 9 | 0 | 0.70 | NA | 1.00 | NA |
| xbrl | inventory | 15 | 7 | 7 | 1 | NA | 0.70 | 1.00 | NA |
| xbrl | revenue | 15 | 7 | 8 | 0 | NA | 0.73 | 1.00 | NA |

Important interpretation:

- The `Audit Mean` is high because the prompt forced qualified risk-cue language, inferential bridges, and limitations.
- This should not be reported as "model accuracy."
- The more important methodological signal is the divergence across text, graph, and integrated correctness.

## Failure Mode Result

Preliminary failure-mode counts:

| Failure mode | Count |
|---|---:|
| none | 71 |
| integration failure | 23 |

No relation-hallucination examples were identified by the preliminary parser after correction. Earlier false positives were caused by treating hybrid text-only claims as graph failures. These are better classified as integration failures because the claim may be useful but does not demonstrate narrative-XBRL integration.

## Inference Shift

The preliminary inference-shift table shows that retrieval condition changes what can be inferred from the same LLM task:

- LLM-only outputs usually produced a single context-limited statement rather than traceable audit claims.
- Text retrieval produced narrative-traceable claims but no graph-valid evidence layer.
- XBRL retrieval produced fact/path-traceable claims but lacked narrative context.
- Hybrid retrieval did not automatically integrate both evidence layers; in several cases it generated useful claims supported by only one layer.

This directly supports the paper's methodological argument:

> Hybrid retrieval is not automatically better. It creates an opportunity for integrated correctness, but the output still has to demonstrate that text, XBRL relations, and audit reasoning are actually reconciled.

## Candidate Demonstration Examples

Strong positive case:

- Starbucks inventory hybrid condition.
- Preliminary result after parser correction: 1 fully integrated claim.
- Use: Demonstrates when hybrid retrieval can support direct narrative-XBRL corroboration.

Strong cautionary case:

- Nike revenue hybrid condition.
- Preliminary result: 0 fully integrated claims despite having both text and XBRL context.
- Use: Demonstrates why hybrid retrieval must be evaluated through claim-level coding rather than assumed superior.

Additional cautionary case:

- Starbucks inventory hybrid condition.
- Preliminary result: 4 of 5 claims use hybrid context only partially.
- Use: Demonstrates that a hybrid prompt can produce useful text-supported risk cues without actually integrating XBRL facts or relation paths.

LLM-only diagnostic case:

- All six LLM-only outputs produced context-limited claims.
- Use: Demonstrates that the prompt and model respected the no-context condition, reducing pretraining-contamination concern for this descriptive demonstration.

## Reviewer-Level Assessment

Strengths:

- The full output set has been converted into a claim-level table.
- Each claim is linked to filer, construct, retrieval condition, output file, prompt file, and context file.
- Preliminary scores are separated by correctness layer rather than collapsed into a single accuracy score.
- Failure-mode examples are drawn from actual outputs, not hypothetical examples.
- The inference-shift table now has actual results.

Remaining weaknesses:

- Audit-valid and integrated coding require expert review.
- Automated support detection cannot substitute for manual source checking.
- The manuscript should report selected examples rather than overemphasizing preliminary means.
- The high preliminary audit-valid score may reflect conservative prompt design and should be interpreted as prompt compliance, not audit expertise.

## Next Step

Conduct a reviewer-style validation of the preliminary coding:

- manually inspect selected claims from each condition;
- verify cited text chunks and XBRL facts;
- select manuscript-ready examples;
- revise the inference-shift narrative around those examples;
- decide whether a second expert coder is needed for the final paper package.
