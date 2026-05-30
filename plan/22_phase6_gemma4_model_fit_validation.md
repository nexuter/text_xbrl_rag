# Phase 6 Gemma 4 Model Fit Validation

## Supersession Note

This memo documents the earlier validation of the lighter `gemma4:latest` model. It is retained for audit trail purposes, but the primary model recommendation has been superseded by `plan/23_phase6_gemma4_31b_model_fit_validation.md` after `gemma4:31b` was installed and smoke-tested.

## Purpose

This memo validates whether `gemma4:latest` is suitable for the Phase 6 methodological demonstration and identifies other Ollama-supported alternatives that may be preferable for sensitivity analysis.

## Local Model Inventory

The local Ollama environment now includes:

| Model | Local size | Parameters | Context | Capabilities | Preliminary role |
|---|---:|---:|---:|---|---|
| `gemma4:latest` | 9.6 GB | 8.0B | 128K | completion, vision, audio, tools, thinking | Primary candidate |
| `llama4:latest` | 67 GB | 108.6B | very large reported context | completion, vision, tools | Strong sensitivity candidate |
| `llama3.3:70b` | 42 GB | 70.6B | 128K | completion, tools | Strong but older sensitivity candidate |
| `llama3.1:8b` | 4.9 GB | 8.0B | 128K | completion, tools | Lightweight baseline only |
| `llama3.2:3b` | 2.0 GB | 3B class | not revalidated here | completion | Not recommended for main audit reasoning |

## External Model Context

Google describes Gemma 4 as its most capable open model family, with four sizes: E2B, E4B, 26B MoE, and 31B Dense. Google emphasizes reasoning, agentic workflows, code generation, multimodal processing, long context, and 140+ language coverage. It also states that Gemma 4 is released under Apache 2.0.

Ollama's Gemma 4 library page lists `gemma4:latest` as a 9.6 GB, 128K-context model and describes the family as suitable for reasoning, agentic workflows, coding, and multimodal understanding. Ollama also lists larger Gemma 4 variants: `gemma4:26b` and `gemma4:31b`.

Sources:

- Google Blog, "Gemma 4: Our most capable open models to date": https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Ollama Gemma 4 library: https://registry.ollama.com/library/gemma4

## Fit Against This Paper's Objective

The paper's objective is not to benchmark LLMs. The objective is to demonstrate that retrieval design affects the validity of audit-relevant LLM inferences.

For that purpose, `gemma4:latest` is a good primary model because it is:

- current and externally defensible as a recent open model;
- locally executable, reducing dependence on proprietary hosted APIs;
- permissively licensed under Apache 2.0;
- large-context enough for the prompt and retrieval-context design;
- capable of tool-style and structured instruction following;
- computationally practical enough to run the full 24-prompt Phase 6 design.

The main limitation is that the locally installed `gemma4:latest` is an 8B-class model. A reviewer could question whether failures reflect retrieval design or limited model capability. This risk is manageable if the paper frames the experiment as a methodological demonstration and includes a stronger-model sensitivity check.

## Smoke Test

A four-prompt smoke test was run on Nike revenue recognition:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:latest --temperature 0 --limit 4
```

Completed prompts:

- text-only contextual retrieval
- XBRL relational retrieval
- hybrid text-plus-XBRL retrieval
- LLM-only diagnostic baseline

Outputs were stored in:

- `data/processed/llm_outputs/text/nke_revenue_text_output.txt`
- `data/processed/llm_outputs/text/nke_revenue_xbrl_output.txt`
- `data/processed/llm_outputs/text/nke_revenue_hybrid_output.txt`
- `data/processed/llm_outputs/text/nke_revenue_llm_only_output.txt`

The run manifest records:

- provider: `ollama`
- model: `gemma4:latest`
- temperature: `0.0`
- completed rows: 4

## Smoke Test Assessment

`gemma4:latest` passed the minimum smoke test:

- It followed the requested claim-oriented structure.
- It differentiated text-only, XBRL-only, hybrid, and LLM-only conditions.
- It treated XBRL facts and relation paths as reported filing structure rather than as independent audit evidence.
- It identified limitations such as missing methodology, missing control evidence, missing aging schedules, and missing revenue-recognition timing details.
- In the LLM-only baseline, it explicitly stated that the provided context was insufficient to identify audit-relevant cues.

Reviewer-facing implication:

> The local Gemma 4 run is strong enough to support the Phase 6 methodological demonstration, provided the paper does not overclaim model performance or treat the output as audit ground truth.

## Recommended Main Model

Use `gemma4:latest` only as a lightweight sensitivity or efficiency check. The primary model recommendation is now `gemma4:31b`.

Rationale:

- It is the newest locally available open model.
- It is practical for full local execution.
- It supports the paper's reproducibility and transparency goals.
- Its smoke-test behavior is adequate for retrieval-design comparison.
- Its limitations can be handled through claim-level coding and a stronger-model sensitivity check.

## Recommended Alternative Models

### Best Installed Sensitivity Candidate: `llama4:latest`

Use `llama4:latest` for a limited sensitivity check if runtime is acceptable.

Rationale:

- It is much larger than `gemma4:latest`.
- It provides a useful test of whether the observed retrieval-condition effects survive under a stronger installed local model.
- It helps address the reviewer concern that Gemma 4 E4B-class capacity may be too limited for audit reasoning.

Recommended sensitivity scope:

- one filer;
- two constructs;
- four retrieval conditions;
- eight prompts total.

### Alternative Installed Sensitivity Candidate: `llama3.3:70b`

Use `llama3.3:70b` only if `llama4:latest` is too slow or unstable.

Rationale:

- It is a strong 70B-class local model with 128K context.
- It is older than Gemma 4 and therefore less aligned with the "recent open model" motivation.
- It is useful as a stable large-model comparator.

### Best Ollama-Supported But Not Yet Installed Candidates

If additional installation is acceptable, the most relevant Gemma 4 alternatives are:

- `gemma4:26b`: stronger than the local E4B-class `gemma4:latest` and designed for workstation use.
- `gemma4:31b`: strongest Gemma 4 dense variant, but likely heavier.

These are more attractive than switching model families if the goal is to keep the paper's open-model motivation centered on Gemma 4.

## Final Reviewer-Level Judgment

`gemma4:latest` is suitable for the main experiment because the study is about retrieval-condition effects, not frontier model performance.

However, to make the design reviewer-resilient, the paper should state:

- the primary inference holds the model constant;
- Gemma 4 is chosen because it is a recent, open, locally executable model;
- the model's 8B-class capacity is a limitation;
- a limited `llama4:latest` or `gemma4:26b` sensitivity check can be used to show that the retrieval-design insight is not merely a single-model artifact when `gemma4:31b` is used as the primary model.
