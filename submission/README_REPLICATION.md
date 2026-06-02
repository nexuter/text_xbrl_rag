# Replication README

## Project Purpose

This replication package supports the methodological demonstration for:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval**

The package documents how SEC 10-K and Inline XBRL source files were converted into text chunks, XBRL facts, XBRL relation paths, retrieval contexts, rendered prompts, local LLM outputs, and preliminary claim-level coding.

This package is intended to support transparency and reproducibility for a Tier 1 methodological demonstration. It is not a retrieval benchmark, model benchmark, audit automation tool, or audit-evidence validation package.

## Boundary Statement

XBRL facts and relations are management-reported structured accounting data. They are not treated as audit evidence, audit truth, or misstatement labels. Audit-boundary notes in the coding files remain preliminary author-coded diagnostics unless independently reviewed by audit-domain experts. Evidence-use type and integrated correctness are independently coded in the 120-claim validation sample to evaluate protocol reliability.

The current implementation uses keyword-ranked text retrieval and table-based XBRL relational retrieval. Vector RAG, RDF/OWL export, graph databases, and GraphRAG are discussed as reporting guidance and possible extensions, not as completed performance implementations in this package.

## Authoritative Evidence Files

For manuscript verification, use `submission/replication_package/AUTHORITATIVE_FILES.md` in the submission package. That file identifies the run manifests, output folders, coding files, and count sources used for the manuscript's 72-output and 281-claim evidence package.

For a claim-by-claim reviewer map, use `submission/replication_package/REVIEWER_FILE_MAP.md`. That file links manuscript claims, tables, and appendix diagnostics to the specific evidence files reviewers should inspect.

Pilot, smoke, dry-run, and early `gemma4:latest` artifacts are not manuscript evidence. They are listed in `submission/replication_package/DEPRECATED_OR_PILOT_ARTIFACTS.md` so reviewers do not confuse provenance files with authoritative results.

## Folder Map

The processed-only submission archive excludes `data/raw_sec/` by default. Raw SEC files are publicly reconstructable using the download script, filer manifest, accession metadata, and SEC EDGAR; a separate raw-source archive can be deposited if repository size policy permits.

| Path | Purpose |
|---|---|
| `config/filer_manifest.json` | Filer, filing, construct, and sample-role manifest |
| `data/raw_sec/` | Downloaded SEC filing and Inline XBRL source files |
| `data/processed/download_manifest.*` | Download records |
| `data/processed/extraction_summary.*` | Extraction diagnostics |
| `data/processed/text_chunks/` | Extracted narrative filing chunks |
| `data/processed/xbrl_facts/` | Extracted XBRL fact tables |
| `data/processed/xbrl_paths/` | Extracted XBRL relation-path tables |
| `data/processed/xbrl_coverage/` | XBRL construct-family coverage diagnostics and NKE inventory worked example |
| `data/processed/retrieval_logs/` | Retrieval log rows |
| `data/processed/retrieval_contexts/` | Final contexts supplied to prompts |
| `data/processed/retrieval_contexts/context_volume_diagnostics.csv` | Context-volume diagnostics for separability transparency |
| `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv` | Condition-level context-volume summary |
| `data/processed/sensitivity/` | Source-environment perturbation diagnostics and bounded sensitivity decision matrix |
| `data/processed/prompts/` | Rendered LLM prompts |
| `data/processed/llm_outputs/` | Raw JSON and text LLM outputs |
| `data/processed/coding/` | Preliminary claim-level coding, independent-coding instrument, hybrid mechanism diagnostics, coder-ready sample, and summaries |
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
python scripts/build_retrieval_contexts.py --manifest config/filer_manifest.json --extension-all-constructs --include-extension-baseline
```

This writes:

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/retrieval_contexts/retrieval_context_manifest.json`
- `data/processed/retrieval_contexts/*_context.txt`
- `data/processed/prompts/*_prompt.txt`
- `data/processed/retrieval_logs/retrieval_log.csv`

The two extension flags are required to reproduce the manuscript's full-scale extension: revenue and inventory constructs for all bounded-extension filers, including the LLM-only diagnostic baseline.

### 4. Build XBRL Construct-Coverage Diagnostics

```powershell
python scripts/analyze_xbrl_construct_coverage.py
```

This writes construct-family coverage diagnostics under `data/processed/xbrl_coverage/`. These diagnostics link the ex ante revenue and inventory protocols to the XBRL facts and relation paths actually supplied in the retrieval environment. They are retrieval-environment validity diagnostics, not model-performance or audit-evidence-sufficiency tests.

### 5. Run Main Deep-Case LLM Outputs

Start Ollama locally, confirm that `gemma4:31b` is installed, then run:

```powershell
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_full --roles main_deep_case
```

Expected main outputs: 24.

### 6. Run Bounded-Extension LLM Outputs

```powershell
python scripts/run_llm_prompts.py --provider ollama --model gemma4:31b --temperature 0 --run-label gemma4_31b_extension --roles bounded_extension
```

Expected extension outputs: 48.

The extension is full scale: six additional filers, two constructs, and four conditions, including the LLM-only diagnostic baseline. It is a bounded maximum-variation methodological extension, not a representative sample or performance benchmark.

### 7. Code Main Deep-Case Claims

```powershell
python scripts/code_llm_claims.py --run-label gemma4_31b_full --output-prefix gemma4_31b --roles main_deep_case
```

Expected main coded claims: 94.

### 8. Code Bounded-Extension Claims

```powershell
python scripts/code_llm_claims.py --run-label gemma4_31b_extension --output-prefix gemma4_31b_extension --roles bounded_extension
```

Expected extension coded claims: 187.

### 9. Build Context-Volume Diagnostics

```powershell
python scripts/analyze_context_diagnostics.py
```

This writes context-volume diagnostics under `data/processed/retrieval_contexts/`. These diagnostics support separability transparency; they are not matched-budget model-output sensitivity tests.

### 10. Build Source-Environment Perturbation Diagnostics

```powershell
python scripts/analyze_retrieval_perturbation_diagnostics.py
python scripts/analyze_bounded_sensitivity_decision_matrix.py
```

These scripts write deterministic source-set perturbation diagnostics and the bounded sensitivity decision matrix under `data/processed/sensitivity/`. They evaluate retrieval-stage source-composition sensitivity, not output-level robustness.

### 11. Build Hybrid Integration Mechanism Diagnostics

```powershell
python scripts/analyze_hybrid_integration_mechanisms.py
```

This writes hybrid-condition mechanism diagnostics under `data/processed/coding/`, including the decomposition of all 89 hybrid claims by actual evidence use.

### 12. Validate Output Completeness And Source References

```powershell
python scripts/validate_llm_results.py
```

This writes `plan/52_llm_results_validation_log.md`.

The validation checks completeness, parseability, run separation, global source-ID traceability, and local text-chunk rank traceability. It does not validate audit-boundary or integrated correctness as expert audit judgments.

## Independent Coding Evidence

The package includes completed independent-coding evidence for the claim-level measurement protocol:

- `data/processed/coding/independent_coding_protocol.md`
- `data/processed/coding/independent_coder_process_documentation.md`
- `data/processed/coding/independent_coding_results.csv`
- `data/processed/coding/intercoder_reliability_summary.md`
- `data/processed/coding/independent_coding_disagreements.csv`

The validation sample contains 120 claims, including all 89 hybrid-condition claims and 31 non-hybrid comparison claims. The non-hybrid claims provide LLM-only, text-only, and XBRL-only anchors for applying the source-use and correctness scales outside the hybrid condition. Two independent coders completed the sample, so `independent_coding_results.csv` contains 240 coder-claim rows: two coder observations for each of the 120 validation claims. Agreement is 100.0 percent for claim segmentation, evidence-use type, and integrated correctness; 97.5 percent for claim kind and text-supported correctness; 99.2 percent for graph-valid correctness; and 87.5 percent for confidence coding. Cohen's kappa or weighted kappa ranges from 0.754 to 1.000 where reported, with the core retrieval-validity variables ranging from 0.919 to 1.000. These results validate the claim-level measurement protocol as a methodological diagnostic; they do not establish model-performance effects or final audit-judgment conclusions.

Claim-level files now include `audit_boundary_prelim` and `audit_boundary_rationale` fields to match the manuscript's terminology. Legacy aliases such as `audit_valid_prelim` and `audit_valid_rationale` are retained only for compatibility with earlier processing scripts and should be interpreted as deprecated names for preliminary audit-boundary diagnostics, not final audit-judgment labels or model-performance outcomes.

### 13. Build Checksum Manifest

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
| Prompt files | 72 |
| Retrieval context files | 72 |
| Retrieval log rows | 464 |
| Main raw JSON outputs | 24 |
| Main text outputs | 24 |
| Extension raw JSON outputs | 48 |
| Extension text outputs | 48 |
| Main coded claims | 94 |
| Extension coded claims | 187 |
| Total coded claims | 281 |
| XBRL construct-coverage filer-construct rows | 18 |
| Bounded sensitivity decision-matrix rows | 18 |
| Checksum manifest rows | 418 |

## Manuscript And Supplement Package Files

| File | Role |
|---|---|
| `plan/69_submission_ready_manuscript_v3.md` | Current v3 manuscript draft |
| `plan/71_v3_main_tables_and_figures.md` | Final main-text tables and figures packet |
| `plan/72_v3_appendix_supplement.md` | Final appendix and online supplement |
| `docs/73_ollama_model_metadata_note.md` | Local model metadata note |
| `docs/74_checksum_manifest_package.md` | Checksum package note |
| `docs/125_gate_a_audit_boundary_validation_decision_memo.md` | Gate A decision memo for audit-boundary claim narrowing |

## Data Availability Statement

The demonstration uses publicly available SEC filing and Inline XBRL data. The replication package preserves the filer manifest, download records, extraction scripts, text chunks, XBRL fact and relation-path tables, retrieval logs, rendered prompts, LLM output files, claim-level coding, and selected source spot checks.

The local LLM outputs were generated using Ollama with `gemma4:31b` at temperature 0. Because local model builds, hardware, and serving environments may differ, exact output replication may require recording local model metadata or digest and environment configuration.

## Known Limitations

1. The package supports a methodological demonstration, not population-level inference.
2. The package does not include independent audit-domain expert coding.
3. The package does not include completed vector-retrieval, RDF/OWL, graph database, or GraphRAG performance artifacts.
4. The package includes context-volume, source-environment perturbation, and bounded sensitivity decision-matrix diagnostics for retrieval-stage transparency, but it does not include completed chunk-size, overlap, matched-budget, evidence-order, prompt-variation, cross-model, or output-level sensitivity runs.
5. Exact output replication may vary across local Ollama builds unless model metadata and environment details are frozen.
6. Checksums support file-integrity verification, but they do not substitute for source interpretation, expert coding, or model reproducibility controls.
