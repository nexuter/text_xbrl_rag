# Coder Package Preparation

## Purpose

This step creates standalone coder-facing files for independent claim-coding validation. The files are intended to be distributed individually to two independent coders, while the author-only README and manifest preserve a clear record of the package.

## Files Created

- `coder/README.md`
- `coder/CODER_INSTRUCTIONS.md`
- `coder/CODING_PROTOCOL.md`
- `coder/CODING_CODEBOOK.md`
- `coder/CODER_PACKAGE_MANIFEST.md`
- `coder/independent_coding_sample.csv`
- `coder/claim_evidence_packet.csv`
- `coder/coder_coding_form_template.csv`
- `coder/independent_coding_results_template.csv`
- `coder/intercoder_reliability_summary_template.md`

## Coder Inputs

Each coder receives the shared instruction files, the 120-claim sample, the evidence packet, and one coder-specific input form.

The evidence packet includes:

- `global_claim_id`;
- filer and construct metadata;
- claim text;
- text and XBRL source IDs;
- retrieval context text;
- LLM output text.

This prevents coders from needing to navigate the full replication package while still allowing them to evaluate text support, graph validity, evidence-use type, and integrated correctness from the materials actually supplied to the model.

The coder-facing CSV files no longer include internal workspace file-path columns. The author can distribute the individual files directly.

## QA Results

- `coder/independent_coding_sample.csv`: 120 rows.
- `coder/claim_evidence_packet.csv`: 120 rows.
- `coder/coder_coding_form_template.csv`: 120 rows with blank coding fields.

## Boundary

The coder package is ready for distribution, but reliability evidence is not complete until both coders return completed forms and the results are merged and analyzed.
