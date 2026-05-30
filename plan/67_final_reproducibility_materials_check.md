# Final Reproducibility Materials Check

## Purpose

This memo evaluates whether the project's reproducibility materials are strong enough for an AJPT Methodological Papers submission.

The review stance is that of a critical AJPT reviewer asking:

> Can I follow the source-to-context-to-output-to-claim evidence trail, and are the limitations of the reproducibility package clear?

## Reviewer Verdict

The reproducibility materials are **near accept-level for a Tier 1 methodological demonstration**.

The project preserves the core evidence trail from SEC filing source materials to text chunks, XBRL facts, relation paths, retrieval contexts, prompts, LLM outputs, and claim-level coding. The remaining gaps are not fatal for a methodology paper, but they should be disclosed clearly:

1. no final packaged replication README yet;
2. no raw-file hash manifest yet;
3. no exact local Ollama model digest captured in the submission-facing package;
4. no independent audit-domain expert-coding file yet;
5. no completed vector-index, RDF/OWL export, or retrieval-sensitivity benchmark.

These gaps are acceptable if the paper is framed as a Tier 1 methodological demonstration and if the appendix states what was implemented versus what is recommended for stronger future studies.

## Actual File Existence Check

The following core files were checked and exist in the workspace.

| Reproducibility Component | File Or Folder | Status |
|---|---|---|
| Filer manifest | `config/filer_manifest.json` | Present |
| Download manifest | `data/processed/download_manifest.json` | Present |
| Extraction summary | `data/processed/extraction_summary.json` | Present |
| Combined text chunks | `data/processed/text_chunks/text_chunks.csv` | Present |
| Combined XBRL facts | `data/processed/xbrl_facts/xbrl_facts.csv` | Present |
| Combined XBRL relation paths | `data/processed/xbrl_paths/xbrl_paths.csv` | Present |
| Retrieval context manifest | `data/processed/retrieval_contexts/context_manifest.csv` | Present |
| Machine-readable context manifest | `data/processed/retrieval_contexts/retrieval_context_manifest.json` | Present |
| Retrieval log | `data/processed/retrieval_logs/retrieval_log.csv` | Present |
| Main LLM run manifest | `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv` | Present |
| Extension LLM run manifest | `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | Present |
| Main claim-level coding | `data/processed/coding/claim_level_coding_gemma4_31b.csv` | Present |
| Extension claim-level coding | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | Present |
| Selected source spot checks | `data/processed/coding/selected_source_spot_check.csv` | Present |

## Actual Count Check

The observed artifact counts match the current manuscript and appendix claims.

| Artifact | Observed Count | Expected Manuscript Count | Status |
|---|---:|---:|---|
| Prompt files | 42 | 42 | Match |
| Retrieval context files | 42 | 42 | Match |
| Retrieval context manifest rows | 42 | 42 | Match |
| Retrieval log rows | 313 | 313 | Match |
| Main raw JSON outputs | 24 | 24 | Match |
| Main text outputs | 24 | 24 | Match |
| Extension raw JSON outputs | 18 | 18 | Match |
| Extension text outputs | 18 | 18 | Match |
| Main coded claims | 94 | 94 | Match |
| Extension coded claims | 88 | 88 | Match |
| Total coded claims | 182 | 182 | Match |
| Combined text chunk rows | 1,377 | Used as appendix diagnostic | Present |
| Combined XBRL fact rows | 2,566 | Used as appendix diagnostic | Present |
| Combined XBRL relation-path rows | 1,619 | Used as appendix diagnostic | Present |

## Raw Source Coverage

The raw SEC source folders exist for the nine active demonstration filers:

| Raw Folder | Role |
|---|---|
| `data/raw_sec/nke_2025_10k/` | Main deep case |
| `data/raw_sec/sbux_2025_10k/` | Main deep case |
| `data/raw_sec/tgt_2025_10k/` | Main deep case |
| `data/raw_sec/wmt_2026_10k/` | Bounded extension |
| `data/raw_sec/hd_2026_10k/` | Bounded extension |
| `data/raw_sec/cat_2025_10k/` | Bounded extension |
| `data/raw_sec/pfe_2025_10k/` | Bounded extension |
| `data/raw_sec/msft_2025_10k/` | Bounded extension |
| `data/raw_sec/crox_2025_10k/` | Bounded extension |

Reviewer interpretation:

The raw-source coverage is sufficient for the current methodological demonstration. Before public release or submission supplement preparation, a raw-file manifest with checksums would strengthen reproducibility.

## Script Coverage

The core pipeline scripts are present.

| Script | Function | Reproducibility Role |
|---|---|---|
| `scripts/sec_download.py` | Download SEC filing materials | Source acquisition |
| `scripts/extract_demo_data.py` | Extract text, XBRL facts, and relation paths | Source-to-data transformation |
| `scripts/build_retrieval_contexts.py` | Build retrieval contexts and prompts | Retrieval environment construction |
| `scripts/run_llm_prompts.py` | Execute LLM runs through Ollama | Output generation |
| `scripts/code_llm_claims.py` | Create claim-level coding artifacts | Output-to-variable construction |
| `scripts/validate_llm_results.py` | Validate run and source-reference consistency | Traceability check |

Reviewer interpretation:

The script coverage supports the paper's data/variable-construction contribution. The final submission package should include a short README specifying the intended execution order and required local dependencies.

## Source-To-Claim Evidence Trail

The reproducibility package supports the following chain:

| Step | Artifact | Location | Status |
|---|---|---|---|
| 1 | Source filer definition | `config/filer_manifest.json` | Present |
| 2 | Downloaded SEC filing records | `data/processed/download_manifest.*` | Present |
| 3 | Raw SEC files | `data/raw_sec/` | Present |
| 4 | Extracted text chunks | `data/processed/text_chunks/` | Present |
| 5 | Extracted XBRL facts | `data/processed/xbrl_facts/` | Present |
| 6 | Extracted XBRL relation paths | `data/processed/xbrl_paths/` | Present |
| 7 | Retrieval logs | `data/processed/retrieval_logs/retrieval_log.csv` | Present |
| 8 | Retrieval contexts | `data/processed/retrieval_contexts/` | Present |
| 9 | Rendered prompts | `data/processed/prompts/` | Present |
| 10 | Raw and text LLM outputs | `data/processed/llm_outputs/` | Present |
| 11 | Claim-level coding | `data/processed/coding/` | Present |
| 12 | Source spot checks | `data/processed/coding/selected_source_spot_check.csv` | Present |

This evidence trail is sufficient for a reviewer to inspect what the LLM saw and how selected outputs were converted into claim-level variables.

## What The Reproducibility Materials Support

The current materials support these manuscript claims:

1. The demonstration uses actual SEC filing and Inline XBRL source data.
2. Retrieval environments are preserved through source IDs, logs, contexts, and prompts.
3. The LLM outputs were generated under a documented local model configuration.
4. The paper's main and bounded-extension counts are internally consistent.
5. Claim-level coding files exist for all 182 preliminary coded claims.
6. Selected examples can be traced back through source IDs and spot-check files.

## What The Reproducibility Materials Do Not Support

The materials do not support these claims:

1. exact third-party replication without local dependency setup;
2. exact model-level replication without an Ollama model digest or frozen model artifact;
3. audit-validity conclusions without independent expert coding;
4. retrieval-performance benchmarking without sensitivity runs;
5. vector database performance or embedding-based retrieval claims;
6. RDF/OWL graph-store performance or GraphRAG implementation claims.

## Required Submission-Facing README

Before submission or public supplement release, create a concise README with this structure:

```text
1. Project purpose
2. Folder map
3. Source filing manifest
4. Pipeline execution order
   a. sec_download.py
   b. extract_demo_data.py
   c. build_retrieval_contexts.py
   d. run_llm_prompts.py
   e. code_llm_claims.py
   f. validate_llm_results.py
5. Local model configuration
6. Expected artifact counts
7. Known limitations
8. Data availability and SEC source links
```

The README should explicitly state that the current demonstration uses keyword-ranked text retrieval and table-based XBRL relational retrieval, not production vector RAG or a full RDF/OWL triple store.

## Recommended Data Availability Statement

Use the following language in the manuscript draft and adjust after the final repository decision:

> The demonstration uses publicly available SEC filing and Inline XBRL data. The replication package preserves the filer manifest, download records, extraction scripts, text chunks, XBRL fact and relation-path tables, retrieval logs, rendered prompts, LLM output files, claim-level coding, and selected source spot checks. The local LLM outputs were generated using Ollama with `gemma4:31b` at temperature 0. Because local model builds and hardware environments may differ, exact output replication may require recording the local model digest and environment configuration. The demonstration should be interpreted as a methodological reproducibility package rather than a benchmark archive.

## Reviewer Stress Test

### Concern 1. Can reviewers reproduce the evidence environment?

Assessment:

Mostly yes. The prompts, retrieval contexts, and source IDs are preserved for all 42 runs.

Remaining risk:

The package needs a single README to prevent reviewers from having to infer execution order from multiple planning documents.

### Concern 2. Can reviewers reproduce the LLM outputs exactly?

Assessment:

Partially. The provider, model name, temperature, run time, and raw outputs are preserved. Exact replication may still vary because local Ollama model builds and serving environments can differ.

Mitigation:

Capture the exact model digest or `ollama show` metadata before final release.

### Concern 3. Are source files verifiable?

Assessment:

Yes at the folder and manifest level. Stronger if raw file hashes are added.

Mitigation:

Add a checksum manifest for raw and key processed files before public supplement release.

### Concern 4. Is expert audit coding reproducible?

Assessment:

Not yet. Claim-level coding files exist, but audit-valid and integrated scores remain preliminary author-coded diagnostics.

Mitigation:

Either add limited expert review or keep the coding boundary explicit in the manuscript, appendix, and table notes.

### Concern 5. Does the package overclaim vector/RDF implementation?

Assessment:

No, if the final manuscript follows the appendix and table guidance. Current artifacts support a keyword/text prototype and table-based XBRL relational retrieval.

Mitigation:

Keep vector DB, RDF/OWL, and GraphRAG language in the reporting-guidance/future-extension category unless additional artifacts are generated.

## Accept-Level Reproducibility Checklist

| Requirement | Status | Final Action |
|---|---|---|
| Source manifest present | Ready | Verify final filing metadata and URLs |
| Raw source folders present | Ready | Add checksum manifest if releasing package |
| Extraction scripts present | Ready | Add README execution order |
| Text chunks present | Ready | Keep chunking boundary clear |
| XBRL facts and paths present | Ready | Keep management-reported-data boundary clear |
| Retrieval logs present | Ready | Confirm final examples cite source IDs |
| Prompt/context files present | Ready | Include appendix index |
| Raw LLM outputs present | Ready | Add exact model digest if available |
| Claim coding files present | Ready with boundary | Add expert review or keep preliminary-coding limitation |
| Source spot checks present | Ready | Use source-verified examples in main text |
| Sensitivity tests | Not required for Tier 1 | Do not imply completed benchmark |
| Vector/RDF artifacts | Not implemented | Frame as guidance/specification only |
| Submission README | Needed | Create before final supplement release |

## Final Reviewer Assessment

The reproducibility materials are strong enough to support the paper's bounded methodological contribution. They make the retrieval-created information environment observable and preserve the transformation from filed source data to claim-level variables.

The package is not yet a polished public replication archive. To reach submission-ready form, the authors should add a short README, capture local model metadata, and decide whether to add raw-file checksums. These are presentation and archival improvements, not fundamental threats to the manuscript's methodological contribution.

## Final Decision

**Reproducibility materials are ready for v3 manuscript integration with minor packaging actions.**

The next major task is to produce the submission-ready v3 manuscript using:

1. `plan/56_ajpt_style_alignment_and_v3_revision_package.md`;
2. `plan/65_final_appendix_package.md`;
3. `plan/66_final_tables_and_figures_check.md`;
4. this reproducibility check.
