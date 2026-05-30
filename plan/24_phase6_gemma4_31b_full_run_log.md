# Phase 6 Gemma 4 31B Full LLM Run Log

## Purpose

This file records the completion of the full Phase 6 LLM output generation step using `gemma4:31b`.

## Prompt Update Before Full Run

Before the full run, the prompt template was revised to address a reviewer-relevant issue observed in the smoke test: some inferred risk-cue claims were marked with `Limitation: None`.

The revised prompt now requires:

- an inferential bridge for every risk-cue or assertion-mapping claim;
- at least one missing audit evidence item, missing control detail, or source-bound limitation for every risk-cue or assertion-mapping claim;
- period, source, or measurement limitations for factual claims.

The prompt/context files were regenerated with:

```text
python scripts/build_retrieval_contexts.py
```

## Execution Command

The full run was executed locally through Ollama:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_full
```

## Model and Run Configuration

| Field | Value |
|---|---|
| Provider | `ollama` |
| Model | `gemma4:31b` |
| Temperature | `0.0` |
| Base URL | `http://localhost:11434` |
| Run label | `gemma4_31b_full` |
| Access time UTC | `2026-05-29T02:55:38.587209+00:00` |

## Outputs

Output directory:

- `data/processed/llm_outputs/gemma4_31b_full`

Generated files:

- `run_manifest.csv`
- `run_summary.md`
- `raw_json/*_raw.json`
- `text/*_output.txt`

The run generated 24 text outputs:

- 3 filers
- 2 audit constructs
- 4 retrieval conditions

## Completion Check

Run summary:

- Rows: 24
- Completed: 24
- Errors: 0

All 24 expected output text files were generated.

## Prompt-Mitigation Check

A text scan for `Limitation: None` in the full-run outputs returned no matches.

This suggests the revised prompt successfully reduced the overconfident limitation pattern observed in the earlier smoke test.

## Reviewer-Level Assessment

The full-run outputs are suitable for the next phase of analysis.

Strengths:

- The same model was held constant across all retrieval conditions.
- The run used a recent open model with local reproducibility.
- Outputs were stored with raw JSON, extracted text, manifest metadata, and prompt/context links.
- The LLM-only diagnostic baseline was included for every filer-construct pair.
- The revised prompt better separates source-supported factual claims from audit-risk inferences.

Remaining work:

- Segment outputs into claim-level units.
- Code each claim by correctness layer:
  - text-supported
  - graph-valid
  - audit-valid
  - integrated
- Identify retrieval-condition failure modes.
- Build the inference-shift table.

