# Raw SEC Reconstruction Note

## Policy Decision

The replication package does not include the full `data/raw_sec/` directory by default.

## Reason

The raw SEC source directory contains 1,119 files and is approximately 360 MB. The raw filings are publicly available from SEC EDGAR and can be reconstructed using the included filer manifest and download script. Excluding the raw files keeps the submission package smaller while preserving reproducibility through public-source reconstruction and checksum documentation.

## Included Instead

The package includes:

- `config/filer_manifest.json`
- `scripts/sec_download.py`
- `scripts/extract_demo_data.py`
- `scripts/build_retrieval_contexts.py`
- `scripts/run_llm_prompts.py`
- `scripts/code_llm_claims.py`
- `scripts/validate_llm_results.py`
- `scripts/build_checksum_manifest.py`
- `data/processed/`
- `data/processed/checksums/checksum_manifest.csv`
- `data/processed/checksums/checksum_summary.md`
- `docs/73_ollama_model_metadata_note.md`
- `docs/74_checksum_manifest_package.md`

## Reconstruction Procedure

From the project root:

```bash
python scripts/sec_download.py
python scripts/extract_demo_data.py
python scripts/build_retrieval_contexts.py
python scripts/run_llm_prompts.py --model gemma4:31b
python scripts/code_llm_claims.py
python scripts/validate_llm_results.py
python scripts/build_checksum_manifest.py
```

The local LLM output step depends on Ollama, the installed local `gemma4:31b` model, local model metadata, and hardware/runtime conditions. The package is therefore intended as a methodological reproducibility package, not as a guarantee of byte-identical LLM output replication across machines.

## If A Repository Allows Larger Uploads

If the final repository or journal submission system permits larger archives, the full `data/raw_sec/` directory can be added to a separate raw-source archive. The current checksum manifest records raw-source integrity for the local archive used to generate the processed artifacts.

## Boundary Statement

Raw SEC filings and Inline XBRL files are management-reported public filing data. They are not audit evidence, audit truth, or misstatement labels. The package supports source traceability, retrieval-environment reconstruction, and claim-level methodological inspection.
