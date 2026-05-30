# Phase 6 LLM Output Execution Harness

## Purpose

This file records the preparation of the LLM output execution harness for Phase 6.

The next empirical step is to run the 24 prompt files generated in the retrieval-context step:

- 18 primary retrieval-condition prompts
- 6 LLM-only diagnostic baseline prompts

At this point, the execution harness is complete and verified. The script supports both hosted OpenAI-style execution and local Ollama execution. The 24-prompt Phase 6 main run has been completed with `gemma4:31b`.

## Script

The execution harness is:

- `scripts/run_llm_prompts.py`

Inputs:

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/prompts/*_prompt.txt`

Outputs when run:

- `data/processed/llm_outputs/run_manifest.csv`
- `data/processed/llm_outputs/run_summary.md`
- `data/processed/llm_outputs/raw_json/*_raw.json`
- `data/processed/llm_outputs/text/*_output.txt`

Dry-run outputs:

- `data/processed/llm_outputs/run_manifest_dry_run.csv`
- `data/processed/llm_outputs/run_summary_dry_run.md`

## Dry-Run Verification

Dry run command:

```text
python scripts/run_llm_prompts.py --dry-run
```

Dry run result:

- 24 prompt rows validated
- 24 output paths generated in the manifest
- no API calls made
- all statuses recorded as `dry_run`

## Execution Providers

The harness supports two providers:

- `openai`: calls the OpenAI Responses API.
- `ollama`: calls a local Ollama model through `http://localhost:11434/api/generate`.

The local environment currently lists the following Ollama models as available:

- `gemma4:31b`
- `gemma4:latest`
- `llama4:latest`
- `llama3.3:70b`
- `llama3.1:8b`
- `llama3.2:3b`

`gemma4:31b` is now installed and has passed a four-prompt local smoke test. The current recommended local execution command is:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0
```

## Required Environment Variables

Hosted OpenAI execution requires:

```text
OPENAI_API_KEY=<API key>
OPENAI_MODEL=<model identifier>
```

Optional:

```text
OPENAI_BASE_URL=https://api.openai.com/v1
```

The script uses the OpenAI Responses API endpoint:

```text
POST /v1/responses
```

Local Ollama execution can be run without an API key:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0
```

Optional:

```text
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma4:31b
```

## Recommended Execution Command

After setting hosted-provider environment variables:

```text
python scripts/run_llm_prompts.py --temperature 0
```

For a small smoke test:

```text
python scripts/run_llm_prompts.py --temperature 0 --limit 2
```

For a local Ollama smoke test:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --limit 2 --run-label gemma4_31b_smoke
```

To rerun and overwrite existing outputs:

```text
python scripts/run_llm_prompts.py --temperature 0 --force
```

## Model Reporting Fields

The run manifest records:

- run ID
- filer
- construct
- retrieval condition
- prompt file
- context file
- context word count
- output text file
- raw JSON file
- model
- base URL
- temperature
- access time UTC
- status
- provider
- error, if any

These fields support the Phase 6 model reporting requirement and reviewer concerns about reproducibility and pretraining contamination.

## Reviewer-Level Assessment

Strengths:

- Raw JSON and extracted text outputs are stored separately.
- Run manifest links every output to its prompt and retrieval context.
- LLM-only baseline prompts are included in the same execution process.
- Temperature defaults to `0` for reproducibility.
- Existing outputs are not overwritten unless `--force` is used.
- Local-model execution is now available, reducing dependence on proprietary API access.

Remaining decision:

> Choose the primary model before generating outputs. For this methodology paper, the main design should use one fixed model across all retrieval conditions; additional models should be reserved for sensitivity analysis rather than repositioning the paper as a model benchmark.

## Full-Run Verification

Main run command:

```text
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_full
```

Main run result:

- Rows: 24
- Completed: 24
- Errors: 0
- Output directory: `data/processed/llm_outputs/gemma4_31b_full`

The generated outputs include:

- `run_manifest.csv`
- `run_summary.md`
- `raw_json/*_raw.json`
- `text/*_output.txt`

## Next Step

Begin claim segmentation and correctness coding using the full-run outputs.
