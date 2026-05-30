# Paper Development Project Plan

## Project Goal

Develop the current research idea into a publishable audit methodology paper for AJPT or a comparable top accounting/auditing journal.

Working title:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

Central research question:

> How does retrieval design affect the validity of inferences drawn from LLM-based audit research?

## Guiding Principle

The paper should remain a methodology paper, not a system-building or performance-benchmark paper.

The central contribution is **retrieval-environment validity**. All other components should operationalize this concept:

- retrieval typology
- claim-level correctness protocol
- failure mode taxonomy
- reporting checklist
- sensitivity check guidance
- SEC/XBRL-based methodological demonstration

## Phase 1: Stabilize the Paper Argument

### Objectives

- Lock the paper's central thesis.
- Define the core contribution hierarchy.
- Remove claims that sound like audit automation or RAG performance optimization.

### Tasks

- [x] Finalize title and subtitle.
- [x] Finalize central research question.
- [x] Finalize one-paragraph thesis.
- [x] Finalize contribution paragraph with three contributions:
  - retrieval-environment validity
  - operational tools
  - methodological demonstration
- [x] Finalize boundary statements:
  - XBRL is not audit evidence.
  - XBRL is not ground truth.
  - hybrid retrieval is not universally superior.
  - retrieval-environment validity is not a replacement for construct validity.

### Deliverables

- [x] One-page paper synopsis.
- [x] Final abstract draft.
- [x] Final contribution paragraph.

### Acceptance Criteria

- A reviewer can identify the paper as an audit methodology paper within the first page.
- The paper does not read like an XBRL ontology, GraphRAG, or LLM audit automation paper.

## Phase 2: Build the Literature Review

### Objectives

- Position the paper against the right comparison sets.
- Show that the novelty is retrieval as research design.
- Avoid overemphasizing computer science literature.

### Literature Buckets

1. AJPT methodology guidance papers
2. XBRL as structured reporting data
3. Textual analysis and LLM accounting research
4. Audit analytics, Big Data, and AI in auditing
5. Minimal technical background on RAG and graph retrieval

### Tasks

- [x] Compile full bibliographic details for core references.
- [x] Create an annotated bibliography.
- [x] Identify the key contribution and limitation of each literature stream.
- [x] Draft literature positioning table.
- [x] Draft literature review section.
- [x] Add citations for AJPT methodological paper tradition.
- [x] Add citations for XBRL review and XBRL-based variable construction.
- [x] Add citations for accounting textual analysis and LLM accounting papers.
- [x] Add citations for audit analytics and AI adoption/evidence papers.

### Deliverables

- [x] `plan/11_annotated_bibliography.md`
- [x] `plan/12_literature_review_blueprint.md`
- [x] `plan/13_phase2_literature_gap_validation.md`
- [x] Literature review outline.
- [x] Draft related literature section.

### Acceptance Criteria

- The literature review supports the claim:

  > We move from text as data and XBRL as data to retrieval as research design.

- The review makes clear that the paper's unit of analysis is the LLM study design, not the reporting firm, auditor, model, or benchmark.

## Phase 3: Develop the Methodological Framework

### Objectives

- Define retrieval-environment validity rigorously.
- Ground the framework in established audit and research design concepts.
- Make the five dimensions non-ad hoc.

### Tasks

- [x] Define retrieval-environment validity.
- [x] Explain why dynamic retrieval differs from fixed information-set experiments.
- [x] Ground each validity dimension:
  - selection validity -> relevance
  - representation validity -> reliability / faithful representation
  - stability -> reproducibility
  - traceability -> documentation / support
  - separability -> internal validity
- [x] Develop examples for each dimension.
- [x] Create a figure showing the framework:
  - intended audit construct
  - retrieval design
  - retrieval-created information environment
  - LLM output
  - inference validity
- [x] Draft the framework section.

### Deliverables

- [x] `plan/14_phase3_framework.md`
- [x] Framework figure.
- [x] Validity dimensions table.
- [x] Draft retrieval-environment validity section.

### Acceptance Criteria

- The framework reads as a diagnostic lens for construct validity, not as a new validity theory.
- The framework clearly explains what is unique about retrieval-augmented LLM studies.

## Phase 4: Operationalize Retrieval Designs

### Objectives

- Define retrieval designs in audit-research terms.
- Clarify when each retrieval design is appropriate.
- Keep the technical discussion minimal and audit-focused.

### Retrieval Designs

- LLM-only
- Text-based contextual retrieval
- XBRL-based relational retrieval
- Hybrid retrieval

### Tasks

- [x] Define each retrieval design.
- [x] Specify each retrieval operator.
- [x] Map retrieval designs to audit constructs.
- [x] Identify validity risks for each design.
- [x] Clarify XBRL framing:
  - XBRL encodes management-coded reported accounting relationships.
  - These relationships are relevant to, but not equivalent to, audit assertions.
- [x] Draft boundary conditions for XBRL-based relational retrieval.
- [x] Draft retrieval typology table.
- [x] Draft construct-to-retrieval decision tree.

### Deliverables

- [x] `plan/15_phase4_retrieval_designs.md`
- [x] Retrieval typology table.
- [x] Construct-to-retrieval decision tree.
- [x] Draft XBRL-augmented retrieval section.

### Acceptance Criteria

- Text-based and XBRL-based retrieval are distinguished by retrieval operator, not final prompt format.
- Hybrid retrieval is presented as construct-specific, not universally superior.

## Phase 5: Develop Correctness Protocol and Failure Modes

### Objectives

- Provide a practical evaluation protocol for LLM audit outputs.
- Avoid treating LLM outputs as simply right or wrong.
- Distinguish graph-valid, text-supported, and audit-valid claims.

### Tasks

- [x] Define claim as the unit of analysis.
- [x] Define four correctness layers:
  - text-supported
  - graph-valid
  - audit-valid
  - integrated
- [x] Develop coding rubric for each layer.
- [x] Develop audit-valid coding guide.
- [x] Specify coder requirements and reliability checks.
- [x] Define graph-valid spot-check procedures.
- [x] Develop failure mode taxonomy:
  - omission
  - distortion
  - retrieval instability
  - attribution failure
  - model-retrieval confounding
  - relation hallucination
  - source overreach
  - integration failure
- [x] Link each failure mode to validity dimensions and correctness layers.

### Deliverables

- [x] `plan/16_phase5_correctness_protocol.md`
- [x] Claim-level correctness protocol.
- [x] Audit-valid coding rubric.
- [x] Failure mode taxonomy table.
- [x] Draft correctness and failure modes section.

### Acceptance Criteria

- The protocol makes clear that a claim can be text-supported and graph-valid but still audit-invalid.
- Audit-valid correctness is framed as expert-coded judgment, not objective ground truth.

## Phase 6: Design the Methodological Demonstration

### Objectives

- Show that the framework changes research inference.
- Use actual SEC filing and Inline XBRL data.
- Keep the demonstration descriptive, not inferential.

### Demonstration Scope

- 3 familiar public SEC filers
- 3 consumer-facing business settings
- 2 audit constructs:
  - revenue recognition risk
  - inventory valuation assertion
- 3 retrieval designs:
  - text-based contextual retrieval
  - XBRL-based relational retrieval
  - hybrid retrieval
- required LLM-only diagnostic baseline for pretraining-contamination and traceability checks

### Tasks

- [x] Define filer selection criteria.
- [x] Select candidate SEC filers.
- [x] Define case selection memo requirement.
- [x] Define model reporting and knowledge-cutoff disclosure requirement.
- [x] Download filings and Inline XBRL data.
- [x] Extract relevant text sections:
  - MD&A
  - footnotes
  - accounting policies
  - revenue and inventory disclosures
- [x] Extract XBRL facts and relation paths:
  - concepts
  - facts
  - periods
  - units
  - dimensions
  - calculation links
  - presentation links
  - extension concepts
- [x] Build minimal text retrieval prototype.
- [x] Build minimal XBRL relational retrieval prototype.
- [x] Define prompts for each retrieval design.
- [x] Create LLM output execution harness.
- [x] Resolve primary model-selection logic.
- [x] Validate `gemma4:latest` model fit with a local smoke test.
- [x] Validate `gemma4:31b` model fit with a local smoke test.
- [x] Run LLM outputs under each design.
- [x] Produce claim-level coding table.
- [x] Identify failure modes.
- [x] Validate selected coded examples from a reviewer perspective.
- [x] Draft methodological demonstration subsection from actual outputs.
- [x] Spot-check selected text and XBRL sources against processed and raw filing data.
- [x] Stress-test the demonstration package from a reviewer perspective.
- [x] Produce inference shift table template.
- [x] Store retrieval log and example templates in appendix-ready format.
- [x] Define minimum manuscript and appendix evidence package.

### Deliverables

- [x] `plan/17_phase6_methodological_demonstration_design.md`
- [x] `plan/18_phase6_data_extraction_log.md`
- [x] Demonstration dataset design.
- [x] Case selection memo template requirement.
- [x] Model reporting and knowledge-cutoff disclosure requirement.
- [x] `plan/19_phase6_retrieval_context_log.md`
- [x] `plan/20_phase6_llm_output_harness.md`
- [x] `plan/21_phase6_model_selection_memo.md`
- [x] `plan/22_phase6_gemma4_model_fit_validation.md`
- [x] `plan/23_phase6_gemma4_31b_model_fit_validation.md`
- [x] `plan/24_phase6_gemma4_31b_full_run_log.md`
- [x] `plan/25_phase6_claim_coding_and_inference_shift_log.md`
- [x] `plan/26_phase6_reviewer_validation_of_coded_examples.md`
- [x] `plan/27_phase6_demonstration_subsection_draft.md`
- [x] `plan/28_phase6_source_graph_spot_check_memo.md`
- [x] `plan/29_phase6_demonstration_reviewer_stress_test.md`
- [x] Retrieval logs.
- [x] Retrieval log template.
- [x] Text chunk examples from actual filings.
- [x] XBRL relation path examples from actual filings.
- [x] LLM output examples.
- [x] LLM output run dry-run manifest.
- [x] Claim-level coding table template.
- [x] Claim-level coding table with actual outputs.
- [x] Failure mode examples from actual outputs.
- [x] Inference shift table template.
- [x] Inference shift table with actual results.
- [x] Draft methodological demonstration design section.
- [x] Prompt-ready retrieval contexts.

### Acceptance Criteria

- The demonstration does not rank retrieval methods.
- The demonstration shows that naive accuracy-based interpretation differs from framework-based interpretation.
- The demonstration uses actual SEC and Inline XBRL data.
- Familiar-company cases are defended through filing-specific prompts, retrieval logs, source mapping, and an LLM-only diagnostic baseline.
- The paper pre-specifies what counts as successful evidence and what will be concluded if expected correctness-layer divergence does not appear.

## Phase 7: Build Reproducibility and Reporting Materials

### Objectives

- Make the paper usable as methodological guidance.
- Provide clear reporting standards for future researchers.
- Specify implementation-transparent data structures for text retrieval and XBRL relational retrieval.
- Keep implementation guidance in service of retrieval-environment validity, not system optimization.

### Tasks

- [x] Verify whether the existing project plan explicitly covers text retrieval and XBRL relation retrieval implementation transparency.
- [x] Add a scoped work package for retrieval data structures, implementation parameters, and reproducibility artifacts.
- [x] Create core reporting checklist for main text.
- [x] Create extended reporting checklist for appendix.
- [x] Create text retrieval implementation specification:
  - source document normalization
  - chunk schema
  - chunk size and overlap
  - tokenizer / word-count rule
  - embedding model and embedding version
  - vector database or index type
  - similarity metric
  - metadata filters
  - top-k and reranking policy
  - prompt context budget
- [x] Create XBRL relation retrieval implementation specification:
  - fact node schema
  - concept node schema
  - relation edge schema
  - taxonomy and linkbase source
  - taxonomy year / version
  - extension-concept handling
  - calculation, presentation, and definition relations
  - traversal depth and relation filters
  - period, unit, and dimension handling
  - RDF / OWL mapping for portability and compatibility
- [x] Create hybrid retrieval context assembly specification:
  - text-context budget
  - relation-context budget
  - source ID preservation
  - ordering and formatting rules
  - token-budget equalization approach
- [x] Create LLM demonstration implementation workflow:
  - SEC filing download
  - text and Inline XBRL extraction
  - text retrieval store construction
  - XBRL relation store construction
  - retrieval execution
  - prompt rendering
  - LLM run configuration
  - output parsing and claim-level coding
  - source and graph spot-checking
- [x] Create reproducibility package checklist:
  - source filing manifest
  - extraction scripts
  - chunk table
  - embedding/index metadata
  - XBRL fact table
  - XBRL relation edge table
  - RDF/OWL export or mapping specification
  - retrieval logs
  - prompt files
  - model configuration
  - coded outputs
- [x] Create sensitivity check guidance:
  - model variation
  - prompt variation
  - text chunk size
  - text chunk overlap
  - embedding model
  - vector similarity metric
  - retrieval top-k / reranking
  - XBRL traversal depth
  - XBRL relation type filters
  - token budget equalization
  - taxonomy version
  - extension-concept inclusion
  - period and dimension filters
  - graph extraction spot-check
  - repeated retrieval stability
- [x] Create appendix templates:
  - retrieval log template
  - text chunk and vector-store reporting template
  - XBRL fact and relation-store reporting template
  - RDF/OWL mapping template
  - claim coding template
  - failure mode coding template
  - prompt reporting template
- [x] Stress-test Phase 7 materials from an AJPT reviewer perspective.
- [x] Revise Phase 7 materials to distinguish minimum prototypes from extended vector/RDF implementations.
- [x] Tie the reporting checklist directly to retrieval-environment validity dimensions.

### Deliverables

- [x] `plan/30_phase7_retrieval_implementation_transparency_scope.md`
- [x] `plan/31_phase7_text_retrieval_specification.md`
- [x] `plan/32_phase7_xbrl_relation_ontology_specification.md`
- [x] `plan/33_phase7_hybrid_context_and_llm_workflow.md`
- [x] `plan/34_phase7_reporting_checklist_and_sensitivity_table.md`
- [x] `plan/35_phase7_reviewer_stress_test.md`
- [x] Reporting checklist.
- [x] Sensitivity check table.
- [x] Text retrieval data structure specification.
- [x] XBRL relational retrieval data structure specification.
- [x] Hybrid context assembly specification.
- [x] LLM demonstration implementation workflow.
- [x] Reproducibility package checklist.
- [x] Appendix templates.

### Acceptance Criteria

- A future audit researcher could use the checklist to report an LLM-RAG audit study transparently.
- A future researcher could reproduce the text retrieval environment from disclosed chunks, embedding/index metadata, retrieval parameters, prompts, and logs.
- A future researcher could reproduce the XBRL relational retrieval environment from disclosed fact tables, relation edges, taxonomy/linkbase sources, traversal rules, RDF/OWL mapping, prompts, and logs.
- Reviewers can distinguish the paper's methodological contribution from engineering claims about retrieval performance.

## Phase 8: Draft the Manuscript

### Objectives

- Produce a coherent first full draft.
- Keep the manuscript focused on methodology.

### Proposed Sections

1. Introduction
2. Related Literature
3. Retrieval-Environment Validity
4. XBRL-Augmented Retrieval Designs
5. Correctness Protocol and Failure Modes
6. Methodological Guidance
7. Methodological Demonstration
8. Discussion and Boundary Conditions
9. Conclusion

### Tasks

- [x] Create manuscript architecture and section-level argument map.
- [x] Create integrated manuscript draft v0 from Phase 1-7 materials.
- [x] Stress-test manuscript draft v0 from an AJPT reviewer perspective.
- [x] Revise draft v0 to replace planning placeholders with manuscript-ready tables.
- [x] Strengthen literature positioning with citation groups from AJPT methodology, XBRL, textual analysis, LLM accounting, and audit analytics.
- [x] Create draft reference list and add references draft to manuscript v0.
- [x] Create manuscript-ready tables and figures package.
- [x] Draft introduction.
- [x] Draft related literature.
- [x] Draft framework section.
- [x] Draft retrieval typology section.
- [x] Draft correctness protocol section.
- [x] Draft methodological guidance section.
- [x] Draft demonstration section.
- [x] Draft discussion and limitations.
- [x] Draft conclusion.
- [x] Align all sections with central research question.

### Deliverables

- [x] `plan/36_phase8_manuscript_architecture.md`
- [x] `plan/37_phase8_manuscript_draft_v0.md`
- [x] `plan/38_phase8_manuscript_v0_reviewer_stress_test.md`
- [x] `plan/39_phase8_citation_strengthening_memo.md`
- [x] `plan/40_phase8_reference_list_draft.md`
- [x] `plan/41_phase8_tables_and_figures_package.md`
- [x] `plan/42_phase8_manuscript_draft_v1_with_table_callouts.md`
- [x] `plan/43_phase8_appendix_materials_package.md`
- [x] Full manuscript draft.
- [x] Tables and figures.
- [x] Appendix materials.

### Acceptance Criteria

- The first page makes clear that this is an audit methodology paper.
- Every section connects back to retrieval-environment validity.
- The manuscript avoids overclaiming XBRL, LLMs, or hybrid retrieval.

## Phase 9: Reviewer Stress Test

### Objectives

- Evaluate the manuscript as an AJPT reviewer would.
- Identify desk-reject or major-revision risks before submission.

### Tasks

- [x] Review for methodology contribution clarity.
- [x] Review for overclaiming.
- [x] Review for audit-specific grounding.
- [x] Review for demonstration rigor.
- [x] Review for literature positioning.
- [x] Review for checklist-vs-theory risk.
- [x] Review whether the demonstration changes inference.
- [x] Review whether XBRL is clearly not treated as audit evidence.
- [x] Review whether audit-valid correctness has reliability safeguards.
- [x] Implement Priority 1 reviewer revisions in manuscript draft v2.
- [x] Re-test manuscript draft v2 from an accept-level reviewer perspective.

### Deliverables

- [x] `plan/44_phase9_reviewer_stress_test_v1.md`
- [x] `plan/45_phase9_revision_action_list.md`
- [x] `plan/46_phase9_manuscript_draft_v2_after_reviewer_revisions.md`
- [x] `plan/47_phase9_reviewer_stress_test_v2_accept_level.md`
- [x] Reviewer-style critique memo.
- [x] Revision action list.

### Acceptance Criteria

- The manuscript can answer:

  > What would an audit researcher do differently after reading this paper?

## Phase 10: Submission Preparation

### Objectives

- Prepare the manuscript for AJPT methodology submission or another target outlet.
- Resolve pre-submission demonstration scope and generalizability concerns.

### Tasks

- [x] Assess whether the three-filer demonstration is sufficient for methodological generalization.
- [x] Decide whether to add a six-filer bounded robustness extension.
- [x] If expanding, select additional filers by firm size, industry, reporting complexity, and construct fit.
- [x] If expanding, run appendix-level retrieval diagnostics for additional filers.
- [x] If expanding, run limited LLM/coding checks for selected additional filer-construct conditions.
- [x] Validate LLM output completeness, parseability, run separation, and source traceability.
- [x] Create bounded-extension manuscript and appendix integration package.
- [x] Audit whether the additional bounded-extension data have been applied consistently across earlier phase materials.
- [x] Update current tables and figures package for the two-layer demonstration design.
- [x] Update current appendix package for main and bounded-extension artifacts.
- [x] Mark pre-extension manuscript drafts as historical or not submission-current.
- [x] Confirm target journal and submission category.
- [x] Align manuscript with journal style.
- [x] Stress-test target positioning against the specific AJPT Methodological Papers call topics.
- [x] Prepare cover letter.
- [x] Prepare response to likely reviewer concerns.
- [x] Finalize references.
- [x] Critically assess whether the contribution is sufficient relative to existing literature.
- [x] Implement contribution-sharpening revisions from the reviewer sufficiency assessment.
- [x] Assess whether the claimed contributions are sufficiently covered by the current data.
- [x] Assess whether the current package is strong enough for an accept-level reviewer recommendation.
- [x] Finalize appendix.
- [x] Check all tables and figures.
- [x] Check reproducibility materials.
- [x] Audit whether any revisions or improvements are needed before v3 manuscript drafting.
- [x] Draft submission-ready v3 manuscript.
- [x] Stress-test v3 manuscript from an AJPT reviewer perspective.
- [x] Create final main-text tables and figures packet for v3.
- [x] Create final appendix and online supplement manuscript file for v3.
- [x] Create replication README for the reproducibility package.
- [x] Capture local Ollama model metadata for `gemma4:31b`.
- [x] Add cited emerging audit-system contrast to v3 manuscript and reference package.
- [x] Add checksum manifest script and generate checksum manifest for raw and key replication files.
- [x] Document checksum manifest package for submission-readiness tracking.
- [x] Review overall progress and identify remaining reinforcement needs.
- [x] Create final submission bundle map.
- [x] Create final cover letter submission template.
- [x] Run final cross-file consistency audit and fix identified package inconsistencies.
- [x] Decide audit-validity strategy for current submission package.
- [x] Verify recent-reference publication status and update reference metadata.
- [x] Prepare final clean submission-format files.
- [x] Prepare author-specific submission field checklist.
- [x] Decide whether to create an optional integrated v4 manuscript or keep the separate-file submission format.
- [x] Convert clean submission `.md` files to AJPT/AAA-formatted DOCX files.
- [x] Apply the final repository or submission-system policy for raw SEC files in the replication package.
- [x] Prepare separate figure graphics files if the submission system requires them.
- [x] Convert SVG figure files to PNG/PDF upload formats.

### Deliverables

- [x] `plan/48_demonstration_scope_generalizability_assessment.md`
- [x] `plan/49_bounded_robustness_extension_filer_selection.md`
- [x] `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md`
- [x] `plan/51_bounded_robustness_extension_llm_and_coding_log.md`
- [x] `plan/52_llm_results_validation_log.md`
- [x] `plan/53_bounded_extension_manuscript_integration_package.md`
- [x] `plan/54_cross_phase_consistency_audit_after_extension.md`
- [x] `plan/55_target_journal_and_submission_alignment.md`
- [x] `plan/56_ajpt_style_alignment_and_v3_revision_package.md`
- [x] `plan/57_ajpt_call_topic_alignment_stress_test.md`
- [x] `plan/58_cover_letter_draft_ajpt_methodological_call.md`
- [x] `plan/59_likely_reviewer_concerns_response_package.md`
- [x] `plan/60_final_reference_package.md`
- [x] `plan/61_reviewer_contribution_sufficiency_assessment.md`
- [x] `plan/62_contribution_sharpening_development_package.md`
- [x] `plan/63_reviewer_data_coverage_assessment.md`
- [x] `plan/64_accept_level_reviewer_assessment.md`
- [x] `plan/65_final_appendix_package.md`
- [x] `plan/66_final_tables_and_figures_check.md`
- [x] `plan/67_final_reproducibility_materials_check.md`
- [x] `plan/68_pre_manuscript_revision_audit.md`
- [x] `plan/69_submission_ready_manuscript_v3.md`
- [x] `plan/70_v3_reviewer_stress_test.md`
- [x] `plan/71_v3_main_tables_and_figures.md`
- [x] `plan/72_v3_appendix_supplement.md`
- [x] `README_REPLICATION.md`
- [x] `plan/73_ollama_model_metadata_note.md`
- [x] `scripts/build_checksum_manifest.py`
- [x] `data/processed/checksums/checksum_manifest.csv`
- [x] `data/processed/checksums/checksum_summary.md`
- [x] `plan/74_checksum_manifest_package.md`
- [x] `plan/75_overall_progress_and_reinforcement_review.md`
- [x] `plan/76_final_submission_bundle_map.md`
- [x] `plan/77_final_cover_letter_submission_template.md`
- [x] `plan/78_final_cross_file_consistency_audit.md`
- [x] `plan/79_audit_validity_strategy_decision.md`
- [x] `plan/80_recent_reference_status_check.md`
- [x] `plan/81_final_clean_submission_format_package.md`
- [x] `submission/00_SUBMISSION_README.md`
- [x] `submission/Title_Page_Template.md`
- [x] `submission/Cover_Letter.md`
- [x] `submission/Author_Information_Checklist.md`
- [x] `submission/Format_Decision_Note.md`
- [x] `submission/AJPT_Title_Page.docx`
- [x] `submission/AJPT_Main_Manuscript.docx`
- [x] `submission/AJPT_Online_Supplement.docx`
- [x] `submission/AJPT_Cover_Letter.docx`
- [x] `submission/AJPT_DOCX_Format_Audit.md`
- [x] `submission/Manuscript_Retrieval_as_Research_Design.md`
- [x] `submission/Tables_and_Figures.md`
- [x] `submission/Online_Supplement_Appendix.md`
- [x] `submission/README_REPLICATION.md`
- [x] `submission/Replication_Package_Manifest.md`
- [x] `submission/replication_package/`
- [x] `submission/AJPT_Replication_Package_processed_only.zip`
- [x] `submission/replication_package/RAW_SEC_RECONSTRUCTION_NOTE.md`
- [x] `submission/replication_package/PACKAGE_CONTENTS.md`
- [x] `submission/figures/Figure_1_Retrieval_Environment_Validity.svg`
- [x] `submission/figures/Figure_2_Methodological_Demonstration_Pipeline.svg`
- [x] `submission/figures/Figure_1_Retrieval_Environment_Validity.png`
- [x] `submission/figures/Figure_2_Methodological_Demonstration_Pipeline.png`
- [x] `submission/figures/Figure_1_Retrieval_Environment_Validity.pdf`
- [x] `submission/figures/Figure_2_Methodological_Demonstration_Pipeline.pdf`
- [x] `submission/figures/Figure_Files_README.md`
- [x] `submission/figures/Figure_Export_Audit.md`
- [x] `submission/AJPT_Figure_Files_SVG.zip`
- [x] `submission/AJPT_Figure_Files_upload_formats.zip`
- [x] `submission/Submission_Bundle_Map.md`
- [x] `plan/82_author_specific_submission_fields_preparation.md`
- [x] `plan/83_integrated_v4_vs_separate_file_decision.md`
- [x] `plan/84_ajpt_docx_submission_format_build.md`
- [x] `plan/85_replication_package_raw_sec_policy.md`
- [x] `plan/86_separate_figure_graphics_package.md`
- [x] `scripts/build_ajpt_submission_docx.ps1`
- [x] `scripts/export_submission_figures_edge.ps1`
- [x] Submission-ready manuscript.
- [x] Cover letter template.
- [x] Supplementary materials.
- [x] Replication/reproducibility package, if appropriate.

### Acceptance Criteria

- The manuscript is framed as a methodology paper.
- The contribution is clear, bounded, and distinct from prior XBRL, textual analysis, audit analytics, and LLM accounting research.

## Immediate Next Steps

1. Fill author-specific cover-letter and title-page fields once author details are available.
2. Create any additional compressed submission archives after final author/repository decisions.
3. Re-run recent-reference status check immediately before actual submission if more than a few weeks pass.
