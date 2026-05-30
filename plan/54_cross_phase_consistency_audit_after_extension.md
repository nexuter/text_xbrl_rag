# Cross-Phase Consistency Audit After Bounded Extension

## Purpose

This memo checks whether the additional bounded-extension data have been applied consistently across the project materials. The goal is to prevent the manuscript package from mixing the original three-filer deep demonstration with the later six-filer extension in ways that would confuse reviewers.

## Current Canonical Demonstration State

| Component | Current Status |
|---|---|
| Main deep cases | NKE, SBUX, TGT |
| Bounded extension cases | WMT, HD, CAT, PFE, MSFT, CROX |
| Backup cases in manifest | DE, COST, WDAY |
| Active filer roles | `main_deep_case`, `bounded_extension`, `backup` |
| Main prompt/context conditions | 24 |
| Extension prompt/context conditions | 18 |
| Total active prompt/context conditions | 42 |
| Main LLM outputs | 24 |
| Extension LLM outputs | 18 |
| Total active LLM outputs | 42 |
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total preliminary coded claims | 182 |
| Main model | `gemma4:31b` through local Ollama |
| Extension model | `gemma4:31b` through local Ollama |

## Files Already Consistent With the Extension

| File or Artifact | Assessment |
|---|---|
| `config/filer_manifest.json` | Consistent. Filers are labeled by `sample_role`. |
| `scripts/sec_download.py` | Consistent. Supports role filtering and reuses existing files. |
| `scripts/extract_demo_data.py` | Consistent. Supports main and bounded-extension roles and writes role metadata. |
| `scripts/build_retrieval_contexts.py` | Consistent. Generates full main design and limited extension design. |
| `scripts/run_llm_prompts.py` | Consistent. Supports role, ticker, construct, and condition filters. |
| `scripts/code_llm_claims.py` | Consistent. Supports extension-specific run labels and output prefixes. |
| `scripts/validate_llm_results.py` | Consistent. Separately validates main and extension runs. |
| `plan/48_demonstration_scope_generalizability_assessment.md` | Consistent as the decision memo that motivated the extension. |
| `plan/49_bounded_robustness_extension_filer_selection.md` | Consistent as the selection memo. |
| `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md` | Consistent as the extraction and retrieval diagnostics log. |
| `plan/51_bounded_robustness_extension_llm_and_coding_log.md` | Consistent as the extension LLM and coding log. |
| `plan/52_llm_results_validation_log.md` | Consistent as the run validation log. |
| `plan/53_bounded_extension_manuscript_integration_package.md` | Consistent as the manuscript/appendix insertion package. |

## Files That Are Historical And Should Not Be Treated As Current

The following files correctly describe earlier phases but predate the bounded extension. They should remain as audit-trail records, not as current manuscript guidance:

| File | Reason |
|---|---|
| `plan/17_phase6_methodological_demonstration_design.md` | Original three-filer demonstration design. |
| `plan/24_phase6_gemma4_31b_full_run_log.md` | Original main-run execution log only. |
| `plan/25_phase6_claim_coding_and_inference_shift_log.md` | Original 94-claim main coding log only. |
| `plan/27_phase6_demonstration_subsection_draft.md` | Original three-filer demonstration subsection. |
| `plan/29_phase6_demonstration_reviewer_stress_test.md` | Original demonstration reviewer test before extension. |
| `plan/37_phase8_manuscript_draft_v0.md` | Superseded manuscript draft. |
| `plan/42_phase8_manuscript_draft_v1_with_table_callouts.md` | Superseded manuscript draft. |
| `plan/46_phase9_manuscript_draft_v2_after_reviewer_revisions.md` | Strong draft, but it predates extension integration and must be treated as v2 rather than final. |
| `plan/47_phase9_reviewer_stress_test_v2_accept_level.md` | Useful reviewer stress test, but it predates extension data. |

## Required Consistency Updates

| Area | Required Update | Status |
|---|---|---|
| Master project plan | Add cross-phase consistency audit and bounded-extension table/appendix updates as Phase 10 tasks. | Completed in `plan/09_project_plan.md`. |
| Tables and figures package | Add bounded-extension update to Figure 2, Table 8, Table 9 treatment, and appendix table placement. | Completed in `plan/41_phase8_tables_and_figures_package.md`. |
| Appendix package | Update counts, artifact paths, and appendix structure so reviewers see both the main and extension runs. | Completed in `plan/43_phase8_appendix_materials_package.md`. |
| Manuscript draft v2 | Mark v2 as pre-extension and route future drafting through the extension integration package. | Completed as a status note in `plan/46_phase9_manuscript_draft_v2_after_reviewer_revisions.md`. |

## Reviewer-Risk Assessment

The main risk after adding the extension is internal inconsistency. If the manuscript says the demonstration has only three filers, 24 outputs, and 94 claims while the appendix contains six additional filers, 18 additional outputs, and 88 additional claims, reviewers may infer that the demonstration expanded opportunistically after inspecting results.

The revised framing avoids that risk by using two clearly separated layers:

1. The three familiar filers remain the main-text deep demonstration.
2. The six additional filers are a bounded maximum-variation extension, reported as a robustness and boundary-condition check rather than as a representative empirical sample.

## Canonical Wording Going Forward

Use this wording in manuscript drafts and reviewer responses:

> The paper uses a two-layer demonstration design. The main text provides deep claim-level illustrations using three familiar SEC filers. To reduce the concern that the protocol is tailored to those cases, the appendix reports a bounded six-filer extension spanning retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. The extension adds 18 retrieval-conditioned outputs and 88 preliminary coded claims. It is not used to estimate model performance or population-level failure rates; it tests whether the retrieval-environment validity protocol remains applicable across varied reporting environments.

## Bottom Line

The additional data have been applied to the active data pipeline, retrieval logs, LLM output archive, coding files, validation memo, and extension integration package. The remaining issue was documentation consistency in older table, appendix, and manuscript-draft materials. Those materials have now been marked or updated so that future work can distinguish historical phase records from current manuscript guidance.
