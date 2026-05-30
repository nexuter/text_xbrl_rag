# Phase 6 Gemma 4 31B Model Fit Validation

## Purpose

This memo validates whether `gemma4:31b` is suitable as the primary LLM for the Phase 6 methodological demonstration.

## Local Verification

`gemma4:31b` is installed locally in Ollama.

Local model metadata:

| Field | Value |
|---|---|
| Model | `gemma4:31b` |
| Ollama ID | `6316f0629137` |
| Local size | 19 GB |
| Architecture | `gemma4` |
| Parameters | 31.3B |
| Context length | 262,144 |
| Embedding length | 5,376 |
| Quantization | `Q4_K_M` |
| Capabilities | completion, vision, tools, thinking |
| License | Apache 2.0 |

## External Positioning

Google's Gemma 4 announcement describes Gemma 4 as a recent open model family built for advanced reasoning and agentic workflows. Google identifies four model sizes: E2B, E4B, 26B MoE, and 31B Dense. Google also states that the larger models offer up to 256K context and that Gemma 4 is released under Apache 2.0.

Ollama's Gemma 4 library page lists `gemma4:31b` as the dense workstation-class variant and positions the family for reasoning, agentic workflows, coding, and multimodal understanding.

Sources:

- Google Blog, "Gemma 4: Byte for byte, the most capable open models": https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Ollama Gemma 4 library: https://registry.ollama.com/library/gemma4

## Smoke Test

A four-prompt smoke test was run on the Nike revenue-recognition case:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --limit 4 --run-label gemma4_31b_smoke
```

Completed prompts:

- text-only contextual retrieval
- XBRL relational retrieval
- hybrid text-plus-XBRL retrieval
- LLM-only diagnostic baseline

Outputs were stored separately from the earlier light-model run:

- `data/processed/llm_outputs/gemma4_31b_smoke/run_manifest.csv`
- `data/processed/llm_outputs/gemma4_31b_smoke/run_summary.md`
- `data/processed/llm_outputs/gemma4_31b_smoke/text/*_output.txt`
- `data/processed/llm_outputs/gemma4_31b_smoke/raw_json/*_raw.json`

Run result:

- provider: `ollama`
- model: `gemma4:31b`
- temperature: `0.0`
- completed rows: 4
- errors: none

## Smoke-Test Assessment

`gemma4:31b` passed the model-fit test for the Phase 6 design.

Strengths observed:

- It followed the claim-oriented response format.
- It separated factual claims from risk-cue/assertion-mapping claims.
- It differentiated text-only, XBRL-only, hybrid, and LLM-only conditions.
- It correctly used XBRL facts for numerical comparisons, such as refund liability and receivables changes.
- It did not treat the LLM-only condition as sufficient evidence; it explicitly stated that the missing context prevented audit-relevant inference.
- It is materially stronger than the light `gemma4:latest` candidate for the paper's audit-reasoning use case.

Observed caution:

- In the hybrid condition, some inferred risk-cue claims were marked with `Limitation: None`. This is too strong because audit-risk interpretation remains inferential even when source support is present.

Mitigation:

- Prompt instructions should require every risk-cue or assertion-mapping claim to state the inferential step and at least one evidence limitation.
- Claim-level coding should distinguish source-supported factual claims from audit-valid inference claims.

## Suitability Judgment

`gemma4:31b` is the best primary model among the currently installed Ollama models.

Reasons:

- It aligns with the motivation for using a recent open LLM family.
- It is the full 31B dense Gemma 4 variant rather than the lighter local default.
- It provides 256K context, which comfortably covers the current Phase 6 retrieval contexts and leaves room for appendix-level demonstrations.
- It is locally executable and reproducible through Ollama.
- It has enough capacity to reduce the reviewer concern that observed failures are merely small-model artifacts.
- It still allows the study to remain a retrieval-design methodology paper rather than a model benchmark.

## Comparison With Other Installed Models

| Model | Role | Reason |
|---|---|---|
| `gemma4:31b` | Primary model | Best alignment with recency, open-model motivation, larger capacity, long context, and local reproducibility |
| `gemma4:latest` | Lightweight sensitivity check | Useful to show whether retrieval-design effects remain visible under a smaller Gemma 4 model |
| `llama4:latest` | Cross-family sensitivity check | Larger installed model, useful if reviewer asks whether the finding is Gemma-specific |
| `llama3.3:70b` | Backup sensitivity check | Strong local model but older and less aligned with the paper's open-model recency rationale |
| `llama3.1:8b` / `llama3.2:3b` | Not recommended for main study | Too likely to create capacity-based confounding in audit reasoning |

## Recommended Decision

Use `gemma4:31b` as the main Phase 6 model.

Use `gemma4:latest` or `llama4:latest` only as limited sensitivity checks. The manuscript should not present the study as a model comparison. The model should be held fixed in the main analysis so that retrieval condition remains the central research-design variable.

