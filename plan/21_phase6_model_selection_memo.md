# Phase 6 Model Selection Memo

## Purpose

This memo evaluates whether the Phase 6 methodological demonstration should use one LLM or multiple LLMs, and whether a locally available model is sufficient for the study purpose.

## Reviewer-Facing Position

The main experiment should use one fixed LLM across all retrieval conditions.

The paper's methodological claim is not that a particular model is better than another model. The claim is that retrieval design changes the audit inference environment. Therefore, the independent variable should be the retrieval condition:

- text-only contextual retrieval
- XBRL relational retrieval
- hybrid text-plus-XBRL retrieval
- LLM-only diagnostic baseline

Holding the LLM constant makes the causal interpretation cleaner: observed differences are attributable to the retrieval environment rather than to model family, model scale, alignment policy, or training data.

## Why Multiple Models Are Not Required for the Main Test

Multiple-model benchmarking would weaken the methodological framing if it became the primary design. AJPT reviewers could reasonably ask whether the paper is about audit research methodology or about comparing proprietary and open models.

For the main paper, one model is sufficient if:

- the same model is used for every filer, construct, and retrieval condition;
- temperature and decoding settings are fixed;
- prompts and retrieved contexts are archived;
- outputs are coded using the same correctness protocol;
- the paper reports the model identity, runtime, access date, and relevant configuration.

This design directly tests retrieval-environment validity.

## Recommended Sensitivity Analysis

A second model may be added as a limited robustness check, but not as the main contribution.

Recommended sensitivity design:

- Run the full 24-prompt experiment on the primary model.
- Run a smaller subset on a second model, such as one familiar filer and two constructs across all four retrieval conditions.
- Report whether the direction of retrieval-condition effects is stable.
- Place model-sensitivity results in an appendix or supplemental analysis.

The sensitivity analysis should be framed as evidence that the retrieval-design insight is not entirely model-specific, not as a leaderboard.

## Local Model Feasibility

The local Ollama environment currently includes:

- `gemma4:31b`
- `gemma4:latest`
- `llama4:latest`
- `llama3.3:70b`
- `llama3.1:8b`
- `llama3.2:3b`

The local Ollama check now shows both `gemma4:31b` and `gemma4:latest` as installed. The strongest locally available candidate for the main demonstration is `gemma4:31b`; `gemma4:latest` should be treated as the lighter Gemma 4 variant, not the preferred primary model.

`ollama show gemma4:31b` reports:

- architecture: `gemma4`
- parameters: `31.3B`
- context length: `262144`
- quantization: `Q4_K_M`
- capabilities: completion, vision, tools, thinking
- license: Apache 2.0

`ollama show gemma4:latest` reports:

- architecture: `gemma4`
- parameters: `8.0B`
- context length: `131072`
- quantization: `Q4_K_M`
- capabilities: completion, vision, audio, tools, thinking
- license: Apache 2.0

`ollama show llama4:latest` reports:

- architecture: `llama4`
- parameters: `108.6B`
- quantization: `Q4_K_M`
- capabilities: completion, vision, tools
- reported context length: `10485760`

This is sufficient for the demonstration's context-size requirements, subject to output-quality smoke testing.

## Gemma Clarification

Official Google Gemma 4 documentation describes Gemma 4 as a recent open model family with E2B, E4B, 26B MoE, and 31B Dense variants. Google's announcement emphasizes advanced reasoning, agentic workflows, longer context, and Apache 2.0 licensing. Ollama's Gemma 4 library page lists `gemma4:31b` as the dense workstation-class variant.

For this project, the relevant practical point is:

- `gemma4:31b` is now locally available and is the preferred primary demonstration model.
- `gemma4:latest` is useful as a lighter-model sensitivity or efficiency check.
- If the intended model is `gemma4:26b`, it should be installed or connected before execution.
- If a model called `gemma4` is available through another runtime, it should be documented with its runtime, exact identifier, version, parameter size, quantization, and context window before use.

Sources consulted:

- Google Blog, "Gemma 4: Byte for byte, the most capable open models": https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Ollama Gemma 4 library page: https://registry.ollama.com/library/gemma4

## Acceptance Criteria for a Local Primary Model

Before using a local model as the primary model, run a two-prompt smoke test and verify that the model:

- follows the requested output structure;
- uses the supplied context rather than unsupported general knowledge;
- treats XBRL as management-reported relational data, not as independent audit evidence;
- flags insufficient evidence in the LLM-only baseline;
- produces claims that can be segmented and coded under the correctness protocol;
- does not add unsupported audit conclusions.

If the local model fails these criteria, use a stronger hosted model for the main run and optionally retain the local model as a sensitivity check.

## Recommended Decision

Use one model for the main Phase 6 demonstration.

Preferred path:

- Primary model: local `gemma4:31b`, if full-run runtime is acceptable.
- Sensitivity model: local `gemma4:latest`, local `llama4:latest`, or hosted frontier model on a limited subset.
- Main inference: retrieval design, not model comparison.

This choice best preserves the AJPT methodology contribution: retrieval design is a research-design variable in LLM-based audit research, and XBRL relational retrieval is a structured way to improve retrieval-environment validity.
