# Ollama Model Metadata Note

## Purpose

This note records the local model metadata available for the LLM used in the methodological demonstration. It addresses the reviewer-facing reproducibility concern that the manuscript identifies `gemma4:31b` but exact local model builds may vary.

## Model Metadata Captured

Command run from the project workspace:

```powershell
ollama show gemma4:31b
```

Observed metadata:

| Field | Value |
|---|---|
| Provider | Ollama |
| Model | `gemma4:31b` |
| Architecture | `gemma4` |
| Parameters | 31.3B |
| Context length | 262,144 |
| Embedding length | 5,376 |
| Quantization | Q4_K_M |
| Minimum Ollama requirement | 0.20.0 |
| Capabilities | completion, vision, tools, thinking |
| Model default temperature | 1 |
| Model default top_k | 64 |
| Model default top_p | 0.95 |
| License | Apache License 2.0 |

## Demonstration Run Configuration

The demonstration scripts overrode the model's default temperature by setting temperature to `0.0`.

| Run Label | Role | Expected Outputs | Output Status |
|---|---|---:|---|
| `gemma4_31b_full` | Main deep cases | 24 | 24 completed |
| `gemma4_31b_extension` | Bounded extension | 18 | 18 archived outputs; run manifest includes completed and skipped-existing statuses |

Main run summary:

- Provider: `ollama`
- Base URL: `http://localhost:11434`
- Model: `gemma4:31b`
- Temperature: `0.0`
- Access time UTC: `2026-05-29T02:55:38.587209+00:00`
- Status: 24 completed

Extension run summary:

- Provider: `ollama`
- Base URL: `http://localhost:11434`
- Model: `gemma4:31b`
- Temperature: `0.0`
- Access time UTC: `2026-05-29T15:57:47.190725+00:00`
- Status counts in run manifest: 8 completed, 10 skipped existing
- Interpretation: the archive contains the expected 18 extension outputs; skipped-existing rows reflect reuse of already generated output files rather than missing runs.

## Reviewer-Facing Interpretation

This metadata is sufficient for a Tier 1 methodological demonstration because the paper does not claim model-performance superiority or exact third-party determinism. The replication package preserves prompts, retrieval contexts, raw JSON outputs, text outputs, model name, provider, base URL, and temperature.

The metadata is not sufficient for a model benchmark or exact deterministic replication claim. Exact output replication may still vary across local Ollama builds, hardware, inference libraries, quantization releases, and serving settings.

## Recommended Manuscript Or Supplement Language

Use the following sentence in the final data availability or supplement note:

> The local LLM outputs were generated using Ollama with `gemma4:31b` at temperature 0. The local model reported a 31.3B-parameter `gemma4` architecture with Q4_K_M quantization and a 262,144-token context length. Because local Ollama builds and serving environments may differ, exact output replication should be interpreted with caution unless the model digest and environment are frozen.

## Remaining Reproducibility Improvement

Before public release, capture any available model digest or local model file hash if Ollama exposes it in the installed environment. If a digest cannot be captured, preserve this metadata note and the raw output archive as the reproducibility basis.
