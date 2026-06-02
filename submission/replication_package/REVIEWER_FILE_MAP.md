# Reviewer File Map

## Purpose

This file maps the manuscript's major methodological claims to the specific replication-package artifacts reviewers should inspect. It is intended to reduce ambiguity about which files are authoritative evidence and which files are provenance, pilot, or development artifacts.

For manuscript count verification, also see `AUTHORITATIVE_FILES.md`. For non-authoritative pilot artifacts, see `DEPRECATED_OR_PILOT_ARTIFACTS.md`.

## Manuscript Claim To Evidence Map

| Manuscript Claim Or Table | Primary Evidence Files | What The Files Support | What The Files Do Not Support |
|---|---|---|---|
| Nine-filer protocol-validation package with 72 retrieval-conditioned outputs | `data/processed/retrieval_contexts/context_manifest.csv`; `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv`; `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv` | Output count, filer/construct/condition coverage, prompt/context traceability | Population inference, model-performance validation, or retrieval superiority |
| 281 preliminary coded claims | `data/processed/coding/claim_level_coding_gemma4_31b.csv`; `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` | Claim-level variables used for protocol illustration | Final audit-judgment correctness or expert audit-validity evidence |
| Hybrid-condition labels do not guarantee integrated source use | `data/processed/coding/hybrid_integration_mechanisms.csv`; `data/processed/coding/hybrid_integration_mechanism_summary.csv`; `data/processed/coding/intercoder_reliability_summary.md` | Design-specific source-use divergence and reliability of integration coding | Population frequency of hybrid non-integration or proof that hybrid retrieval is inferior |
| Independent coding reliability for source-use and integration variables | `data/processed/coding/independent_coding_sample.csv`; `data/processed/coding/independent_coding_results.csv`; `data/processed/coding/intercoder_reliability_summary.md`; `data/processed/coding/independent_coding_disagreements.csv`; `data/processed/coding/independent_coding_reconciliation_notes.md`; `data/processed/coding/independent_coder_process_documentation.md` | Measurement reliability for segmentation, source-use type, text support, graph validity, and integrated correctness | Audit-domain expert validation of audit-boundary diagnostics |
| XBRL relational retrieval is construct-dependent | `data/processed/xbrl_coverage/construct_coverage_by_filer.csv`; `data/processed/xbrl_coverage/construct_coverage_by_family.csv`; `data/processed/xbrl_coverage/xbrl_construct_coverage_summary.md` | Ex ante construct-family coverage of retrieved XBRL facts and paths | Evidence of misstatement, nondisclosure, or audit evidence sufficiency |
| XBRL source-to-claim traceability and representation risk | `data/processed/xbrl_coverage/xbrl_worked_example_nke_inventory.md`; `data/processed/retrieval_logs/retrieval_log.csv`; `data/processed/xbrl_facts/xbrl_facts.csv`; `data/processed/xbrl_paths/xbrl_paths.csv` | How raw facts and relation paths map to rendered contexts and selected claims | Proof that XBRL facts are audit evidence or that inventory reserves are sufficient |
| Context-volume separability transparency | `data/processed/retrieval_contexts/context_volume_diagnostics.csv`; `data/processed/retrieval_contexts/context_volume_summary_by_condition.csv`; `data/processed/retrieval_contexts/context_volume_diagnostics_summary.md` | Condition-level context size, source counts, and hybrid text/XBRL imbalance | Matched-budget output sensitivity or model-performance robustness |
| Source-environment perturbation diagnostics | `data/processed/sensitivity/retrieval_perturbation_diagnostics.csv`; `data/processed/sensitivity/retrieval_perturbation_summary_by_variant.csv`; `data/processed/sensitivity/retrieval_perturbation_summary.md` | Deterministic source-set changes under text top-k and XBRL fact/path perturbations | Output-level robustness or prompt/model sensitivity |
| Bounded sensitivity decision matrix | `data/processed/sensitivity/bounded_sensitivity_decision_matrix_by_cell.csv`; `data/processed/sensitivity/bounded_sensitivity_variant_decisions.csv`; `data/processed/sensitivity/bounded_sensitivity_decision_summary.md` | Reviewer-facing classification of source-environment changes and separability-attention cells | Evidence that any retrieval method improves LLM output quality |
| Selected claim examples in the manuscript | `data/processed/coding/selected_manuscript_examples_prelim.csv`; `data/processed/coding/selected_source_spot_check.csv`; `data/processed/coding/manuscript_selected_claim_table.md` | Source-traceable examples for correctness-layer illustration | Independent expert validation of all 281 claims |
| Model configuration and reproducibility boundary | `docs/73_ollama_model_metadata_note.md`; `data/processed/llm_outputs/gemma4_31b_full/run_manifest.csv`; `data/processed/llm_outputs/gemma4_31b_extension/run_manifest.csv`; raw JSON outputs under `data/processed/llm_outputs/` | Provider, model name, local ID, temperature, run labels, output preservation | Exact third-party deterministic replication without a frozen model digest and environment |
| File integrity and package completeness | `data/processed/checksums/checksum_manifest.csv`; `data/processed/checksums/checksum_summary.md`; `docs/74_checksum_manifest_package.md` | SHA-256 integrity checks for included package files | Substantive audit validity, model reproducibility, or output correctness |

## Fast Reviewer Path

1. Start with `AUTHORITATIVE_FILES.md` for counts.
2. Inspect `context_manifest.csv` and the two LLM run manifests for the 72-output package.
3. Inspect the two claim-level coding files for the 281-claim archive.
4. Inspect `intercoder_reliability_summary.md` for independent coding reliability.
5. Inspect `construct_coverage_by_filer.csv` and `xbrl_worked_example_nke_inventory.md` for XBRL construct alignment and traceability.
6. Inspect `bounded_sensitivity_decision_summary.md` for retrieval-stage sensitivity boundaries.
7. Inspect `DEPRECATED_OR_PILOT_ARTIFACTS.md` to avoid using pilot artifacts as manuscript evidence.

## Boundary Reminder

The replication package supports protocol validation, source traceability, source-use coding reliability, XBRL construct-coverage diagnostics, and retrieval-stage sensitivity transparency. It does not support model-performance claims, audit evidence sufficiency claims, retrieval-method superiority claims, or population prevalence claims.
