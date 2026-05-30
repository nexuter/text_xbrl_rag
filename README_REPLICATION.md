# Replication README

## Project Purpose

This replication package supports the methodological demonstration for:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

The package documents how SEC 10-K and Inline XBRL source files were converted into text chunks, XBRL facts, XBRL relation paths, retrieval contexts, rendered prompts, local LLM outputs, and preliminary claim-level coding.

This package is intended to support transparency and reproducibility for a Tier 1 methodological demonstration. It is not a retrieval benchmark, model benchmark, audit automation tool, or audit-evidence validation package.

## Boundary Statement

XBRL facts and relations are management-reported structured accounting data. They are not treated as audit evidence, audit truth, or misstatement labels. Audit-valid and integrated-correctness scores in the coding files are preliminary author-coded diagnostics unless independently reviewed by audit-domain experts.

The current implementation uses keyword-ranked text retrieval and table-based XBRL relational retrieval. Vector RAG, RDF/OWL export, graph databases, and GraphRAG are discussed as reporting guidance and possible extensions, not as completed performance implementations in this package.

## Folder Map

| Path | Purpose |
|---|---|
| `config/filer_manifest.json` | Filer, filing, construct, and sample-role manifest |
| `data/raw_sec/` | Downloaded SEC filing and Inline XBRL source files |
| `data/processed/download_manifest.*` | Download records |
| `data/processed/extraction_summary.*` | Extraction diagnostics |
| `data/processed/text_chunks/` | Extracted narrative filing chunks |
| `data/processed/xbrl_facts/` | Extracted XBRL fact tables |
| `data/processed/xbrl_paths/` | Extracted XBRL relation-path tables |
| `data/processed/retrieval_logs/` | Retrieval log rows |
| `data/processed/retrieval_contexts/` | Final contexts supplied to prompts |
| `data/processed/prompts/` | Rendered LLM prompts |
| `data/processed/llm_outputs/` | Raw JSON and text LLM outputs |
| `data/processed/coding/` | Preliminary claim-level coding and summaries |
| `data/processed/checksums/` | SHA-256 checksum manifest and checksum summary |
| `scripts/` | Pipeline scripts |
| `plan/` | Manuscript-development, validation, appendix, and reviewer-stress-test materials |

## Software Requirements

- Python 3
- `requests` Python package for local Ollama or API calls in `scripts/run_llm_prompts.py`
- Ollama running locally for the demonstrated LLM runs
- Local model used in the demonstration: `gemma4:31b`

Most extraction and retrieval scripts use the Python standard library. SEC downloads require internet access and may be subject to SEC rate limits and user-agent requirements.

## Pipeline Execution Order

Run commands from the project root.

### 1. Download SEC Source Files

```powershell
python scripts/sec_download.py --manifest config/filer_manifest.json
```

This creates or reuses raw filing materials under `data/raw_sec/` and writes download manifests under `data/processed/`.

### 2. Extract Text, XBRL Facts, And XBRL Relation Paths

```powershell
python scripts/extract_demo_data.py --manifest config/filer_manifest.json
```

This writes:

- `data/processed/text_chunks/text_chunks.csv`
- `data/processed/xbrl_facts/xbrl_facts.csv`
- `data/processed/xbrl_paths/xbrl_paths.csv`
- filer-level JSON files for text chunks, facts, and paths
- extraction summaries

### 3. Build Retrieval Contexts And Prompts

```powershell
python scripts/build_retrieval_contexts.py --manifest config/filer_manifest.json
```

This writes:

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/retrieval_contexts/retrieval_context_manifest.json`
- `data/processed/retrieval_contexts/*_context.txt`
- `data/processed/prompts/*_prompt.txt`
- `data/processed/retrieval_logs/retrieval_log.csv`

### 4. Run Main Deep-Case LLM Outputs

Start Ollama locally, confirm that `gemma4:31b` is installed, then run:

```powershell
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_full --roles main_deep_case
```

Expected main outputs: 24.

### 5. Run Bounded-Extension LLM Outputs

```powershell
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_extension --roles bounded_extension --conditions text,xbrl,hybrid
```

Expected extension outputs: 18.

The extension excludes the LLM-only baseline by design. It is a bounded maximum-variation methodological extension, not a representative sample or performance benchmark.

### 6. Code Main Deep-Case Claims

```powershell
python scripts/code_llm_claims.py --run-label gemma4_31b_full --output-prefix gemma4_31b --roles main_deep_case
```

Expected main coded claims: 94.

### 7. Code Bounded-Extension Claims

```powershell
python scripts/code_llm_claims.py --run-label gemma4_31b_extension --output-prefix gemma4_31b_extension --roles bounded_extension
```

Expected extension coded claims: 88.

### 8. Validate Output Completeness And Source References

```powershell
python scripts/validate_llm_results.py
```

This writes `plan/52_llm_results_validation_log.md`.

The validation checks completeness, parseability, run separation, global source-ID traceability, and local text-chunk rank traceability. It does not validate audit-valid or integrated correctness as expert audit judgments.

### 9. Build Checksum Manifest

```powershell
python scripts/build_checksum_manifest.py
```

This writes:

- `data/processed/checksums/checksum_manifest.csv`
- `data/processed/checksums/checksum_summary.md`

The checksum manifest supports archival integrity checks for raw SEC files, key processed artifacts, scripts, the filer manifest, and the replication README. It does not validate audit evidence or LLM output correctness.

## Expected Artifact Counts

| Artifact | Expected Count |
|---|---:|
| Active filers | 9 |
| Text chunk rows | 1,377 |
| XBRL fact rows | 2,566 |
| XBRL relation-path rows | 1,619 |
| Prompt files | 42 |
| Retrieval context files | 42 |
| Retrieval log rows | 313 |
| Main raw JSON outputs | 24 |
| Main text outputs | 24 |
| Extension raw JSON outputs | 18 |
| Extension text outputs | 18 |
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total coded claims | 182 |
| Checksum manifest rows | 1,379 |

## Manuscript And Supplement Package Files

| File | Role |
|---|---|
| `plan/69_submission_ready_manuscript_v3.md` | Current v3 manuscript draft |
| `plan/71_v3_main_tables_and_figures.md` | Final main-text tables and figures packet |
| `plan/72_v3_appendix_supplement.md` | Final appendix and online supplement |
| `plan/73_ollama_model_metadata_note.md` | Local model metadata note |
| `plan/74_checksum_manifest_package.md` | Checksum package note |

## Data Availability Statement

The demonstration uses publicly available SEC filing and Inline XBRL data. The replication package preserves the filer manifest, download records, extraction scripts, text chunks, XBRL fact and relation-path tables, retrieval logs, rendered prompts, LLM output files, claim-level coding, and selected source spot checks.

The local LLM outputs were generated using Ollama with `gemma4:31b` at temperature 0. Because local model builds, hardware, and serving environments may differ, exact output replication may require recording local model metadata or digest and environment configuration.

## Known Limitations

1. The package supports a methodological demonstration, not population-level inference.
2. The package does not include independent audit-domain expert coding.
3. The package does not include completed vector-retrieval, RDF/OWL, graph database, or GraphRAG performance artifacts.
4. The package does not include completed chunk-size, overlap, top-k, traversal-depth, prompt-variation, or cross-model sensitivity runs.
5. Exact output replication may vary across local Ollama builds unless model metadata and environment details are frozen.
6. Checksums support file-integrity verification, but they do not substitute for source interpretation, expert coding, or model reproducibility controls.
