# Deprecated Or Pilot Artifacts

## Purpose

This file identifies artifacts preserved for provenance but not used as manuscript evidence. These files should not be used to verify manuscript counts, tables, or claims.

The authoritative manuscript-evidence files are listed in `AUTHORITATIVE_FILES.md`.

## Non-Authoritative LLM Output Artifacts

| Path | Status | Reason Not Authoritative |
|---|---|---|
| `data/processed/llm_outputs/run_manifest.csv` | Pilot | Early four-output pilot run using `gemma4:latest`; superseded by `gemma4_31b_full` and `gemma4_31b_extension` |
| `data/processed/llm_outputs/run_summary.md` | Pilot | Summary for early `gemma4:latest` pilot |
| `data/processed/llm_outputs/run_manifest_dry_run.csv` | Dry run | Prompt/rendering dry run; no manuscript LLM outputs |
| `data/processed/llm_outputs/run_summary_dry_run.md` | Dry run | Dry-run summary |
| `data/processed/llm_outputs/gemma4_31b_smoke/` | Smoke test | Four-output smoke test used to verify local Ollama execution before full runs |
| `data/processed/llm_outputs/gemma4_31b_drycheck/` | Dry check | Single-row dry check used to validate command configuration |
| `data/processed/llm_outputs/gemma4_31b_extension_dryrun/` | Dry run | Earlier reduced-extension dry run; superseded by full-scale extension |

## Non-Authoritative Coding Aliases

The package includes both generic and run-specific coding summaries. The run-specific files are preferred for manuscript verification:

| Generic Alias | Preferred Run-Specific File |
|---|---|
| `data/processed/coding/claim_coding_summary.md` | `data/processed/coding/claim_coding_summary_gemma4_31b.md` |
| `data/processed/coding/coding_summary_by_condition.csv` | `data/processed/coding/coding_summary_by_condition_gemma4_31b.csv` |
| `data/processed/coding/inference_shift_table_prelim.csv` | `data/processed/coding/inference_shift_table_prelim_gemma4_31b.csv` |
| `data/processed/coding/failure_mode_examples_prelim.csv` | `data/processed/coding/failure_mode_examples_prelim_gemma4_31b.csv` |

The generic aliases currently duplicate the main deep-case run-specific files, but reviewers should cite the run-specific files to avoid ambiguity.

## Interpretation

Preserving these files makes the development trail transparent, but they are not part of the manuscript's 72-output, 281-claim evidence package.

Authoritative manuscript evidence consists of:

1. `gemma4_31b_full` for the 24 main deep-case outputs;
2. `gemma4_31b_extension` for the 48 bounded-extension outputs;
3. `claim_level_coding_gemma4_31b.csv` for 94 main claims;
4. `claim_level_coding_gemma4_31b_extension.csv` for 187 extension claims.
