# Second-Revision Comprehensive Revise Plan

## Purpose

This document translates the second-round referee reports into a comprehensive revision workflow for the AJPT methodological-paper submission:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval**

The plan is meant to:

1. identify exactly why the paper is still short of acceptance,
2. convert reviewer concerns into concrete revision workstreams,
3. track implementation status and newly arising tasks during the revise-and-resubmit process, and
4. prevent the next revision from becoming a rhetorical tightening exercise without enough evidentiary reinforcement.

This file should remain the authoritative workflow tracker for the second-revision cycle.

## Current Editorial Diagnosis

The second-round reports are encouraging in tone but still demanding in substance. Both reviewers agree that:

1. the core idea is timely and important,
2. the transparency package is unusually strong,
3. the paper fits AJPT's methodological call in principle,
4. but the current draft still does not justify acceptance because contribution distinctiveness and demonstration strength are not yet aligned tightly enough.

The paper is now beyond a "promising idea" problem. The remaining barrier is sharper:

> The reviewers want a clearer demonstration that retrieval-environment validity is not merely a sensible framing, but a reviewer-useful methodological construct with evidence, measurement discipline, and audit-specific relevance strong enough to guide actual research design decisions.

## Second-Revision Thesis

The revision should be organized around the following thesis:

> Retrieval-environment validity is a retrieval-specific diagnostic for construct drift in LLM-based audit research. It matters because the evidence environment actually observed by the model is endogenously created by retrieval design, and this can invalidate inference even when prompts, outputs, and source citations appear transparent. The contribution of the paper is not model benchmarking; it is a method for specifying, validating, tracing, and reporting retrieval environments so that auditing researchers and reviewers can distinguish valid design choices from construct-threatening retrieval failures.

Everything in the revision should reinforce this thesis.

## Strategic Choice For This Revision

The reviewers effectively offer two paths:

1. narrow further into a methodological essay with an illustrative package, or
2. strengthen the bounded demonstration enough that the evidence does more than illustrate feasibility.

### Recommended Path

Take a **middle path**:

- keep the paper firmly positioned as a **methodological paper rather than a model-performance paper**;
- but add enough **bounded empirical validation and measurement independence** that the framework is not vulnerable to being dismissed as an elegant but weakly tested idea.

This means the revision should **not** try to become a full-scale multi-model benchmark. Instead, it should add the specific kinds of evidence the reviewers repeatedly asked for:

1. sharper conceptual distinctiveness,
2. ex ante construct protocols,
3. stronger XBRL retrieval measurement validation,
4. stronger independent coding and audit-boundary validation,
5. bounded separability/stability sensitivity checks,
6. tighter wording around what the design-specific counts do and do not show.

The revision should also add a claim-governance layer:

1. classify every major manuscript claim by evidence level,
2. decide whether each claim should be kept, narrowed, moved, or removed,
3. red-team wording that makes bounded evidence sound broader than it is,
4. make reviewer decision rules visible in a table rather than only in prose.

## Shared Reviewer Diagnosis

### What Reviewers Already Buy

1. Retrieval is not a neutral implementation detail in LLM-based audit research.
2. Claim-level coding reveals information that response-level condition labels hide.
3. The transparency and replication orientation are real strengths.
4. The paper could become publishable in AJPT if the revision materially strengthens the weak points.

### What Still Prevents Acceptance

1. **Conceptual overlap risk**: retrieval-environment validity still risks reading like construct validity plus documentation plus RAG reporting.
2. **Demonstration identification risk**: the current evidence is still too bounded relative to the strength of some methodological claims.
3. **Measurement independence risk**: too much of the interpretive protocol still depends on author judgment.
4. **Audit-specificity risk**: parts of the paper still read like general LLM accounting/reporting methodology rather than auditing methodology.
5. **XBRL measurement risk**: relational retrieval is central to the paper, but its construct coverage and representation validity are not yet validated strongly enough.
6. **Overgeneralization risk**: some empirical counts may sound broader than the design supports.

## Revision Priorities

| Priority | Meaning |
|---|---|
| P0 | Required before the next submission |
| P1 | Strongly recommended; may determine whether reviewers move to accept/minor vs another major revision |
| P2 | Valuable polish and reviewer-risk reduction |

## Workstream 0. Claim-Evidence Calibration And Red-Team Wording Pass

**Priority:** P0  
**Core risk:** The paper's claims sometimes ask bounded evidence to carry broader methodological weight.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 2
- Reviewer 2 Major Comment 2
- Reviewer 2 Major Comment 4
- Reviewer 2 Major Comment 5
- Reviewer 2 Minor Comment 6

### Objective

Before revising prose or adding analyses, classify each major manuscript claim by the level of evidence currently supporting it and decide whether the claim should be retained, narrowed, moved to future guidance, or removed.

### Required Revisions

1. Create a claim-evidence calibration register with five evidence levels:
   - conceptual,
   - protocol-validation,
   - measurement-validation,
   - sensitivity-supported,
   - future guidance.
2. For each major claim, record:
   - claim text or paraphrase,
   - manuscript location,
   - current evidence,
   - appropriate evidence level,
   - action: keep, narrow, move to supplement, move to future guidance, or remove,
   - reviewer risk if unchanged.
3. Conduct a red-team wording pass for phrases that may overstate the evidence:
   - "validates the framework,"
   - "retrieval effects,"
   - "audit-valid correctness,"
   - "hybrid retrieval,"
   - "XBRL-augmented reasoning,"
   - "model performance,"
   - "generalizes,"
   - "robust,"
   - "evidence" when the source is public filing text or management-reported XBRL.
4. Add a reviewer-facing decision-rule table classifying retrieval problems as:
   - inference-invalidating,
   - design-confounding,
   - measurement-threatening,
   - disclosure-limiting,
   - acceptable boundary.
5. Add an audit-evidence hierarchy that distinguishes:
   - public-filing support,
   - XBRL graph/reporting support,
   - assertion relevance,
   - audit-boundary diagnostic,
   - audit evidence sufficiency.

### Output Files

- `plan/claim_evidence_calibration_register.md` or equivalent plan file
- revised manuscript decision-rule table
- revised terminology and boundary wording in manuscript and supplement

### Acceptance Criteria

- Every major empirical and methodological claim has a matching evidence level.
- No paragraph implies model-performance validation, audit-evidence sufficiency, or broad generalizability unless the evidence supports it.
- The revised manuscript makes clear that the current demonstration reaches public-filing support, XBRL graph/reporting support, assertion relevance, and audit-boundary diagnostics, but not audit evidence sufficiency.

## Workstream 1. Sharpen The Incremental Contribution

**Priority:** P0  
**Core risk:** The construct still looks incremental rather than necessary.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 1
- Reviewer 2 Major Comment 1
- Reviewer 2 Minor Comment 3

### Objective

Show exactly what existing validity language misses and what practical decision rule retrieval-environment validity adds.

### Required Revisions

1. Add a compact but forceful subsection distinguishing retrieval-environment validity from:
   - construct validity,
   - measurement validity,
   - reproducibility,
   - traceability/documentation,
   - RAG evaluation,
   - textual preprocessing validation,
   - XBRL data-quality research,
   - audit evidence sufficiency.
2. Add a comparison table that states:
   - what adjacent concepts already diagnose,
   - what they do **not** diagnose in dynamic retrieval settings,
   - what retrieval-environment validity newly captures,
   - what reviewer decision changes when retrieval-environment validity fails.
3. Add one or two short counterexamples where:
   - a study looks transparent but retrieves the wrong construct-relevant evidence,
   - a study appears to test retrieval but actually confounds retrieval with context volume or source order.
4. State directly whether retrieval-environment validity is:
   - a standalone validity family,
   - a retrieval-specific subtype/diagnostic within construct validity,
   - or an audit-methodological lens for construct drift.
5. Engage non-accounting retrieval-evaluation and evidence-traceability work directly enough that reviewers can see the paper is not reinventing generic RAG evaluation under an audit label.

### Preferred Position

The safest framing is:

> retrieval-environment validity is a retrieval-specific diagnostic lens for construct drift and inference risk in LLM-based audit research, not a wholesale replacement for traditional validity categories.

### Output Files

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Tables_and_Figures.md`
- corresponding DOCX outputs

### Acceptance Criteria

- A reviewer can explain in one paragraph why existing validity language is insufficient by itself.
- The manuscript states what changes in study evaluation when retrieval-environment validity fails.

## Workstream 2. Tighten Audit Construct Protocols Ex Ante

**Priority:** P0  
**Core risk:** The demonstration traces sources, but not always against a tightly predeclared audit construct.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 3
- Reviewer 2 Major Comment 5

### Objective

Define the revenue and inventory constructs in advance so the retrieval protocol can be judged against an explicit audit target.

### Required Revisions

1. Add construct protocol subsections for:
   - revenue recognition risk,
   - inventory valuation assertion.
2. For each construct, specify:
   - audit objective,
   - relevant assertions,
   - expected evidence types,
   - what public filing/XBRL evidence can support,
   - what it cannot support,
   - examples of valid factual claims,
   - examples of valid assertion-relevant claims,
   - examples of claims that exceed the available evidence.
3. Anchor the protocols to audit standards or standard audit-method language where possible.
4. Clarify the distinction between:
   - filing-supported factual correctness,
   - graph-valid structured-reporting correctness,
   - audit-boundary diagnostics,
   - actual audit-evidence sufficiency.

### Output Files

- main manuscript methods/framework sections
- online supplement construct appendix
- tables or figure showing construct-to-evidence mapping

### Acceptance Criteria

- A reviewer can evaluate whether retrieved evidence was construct-relevant before looking at the LLM output.
- "Audit-valid" wording is either narrowed or backed by stronger validation.

## Workstream 3. Strengthen XBRL Relational Retrieval Validation

**Priority:** P0  
**Core risk:** XBRL retrieval is conceptually central but still under-validated as a measurement layer.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 4
- Reviewer 2 Major Comment 5
- Reviewer 2 Minor Comment 7

### Objective

Show that the XBRL fact/path retrieval layer is construct-relevant, inspectable, and not merely a mechanical fact dump.

### Required Revisions

1. Build an ex ante construct-relevant XBRL concept inventory for each construct.
2. Report a retrieval-coverage diagnostic:
   - candidate concepts,
   - selected concepts,
   - extension concepts,
   - relation-path types,
   - inclusion/exclusion logic,
   - coverage gaps.
3. Clarify:
   - taxonomy version,
   - extension concept handling,
   - period filters,
   - dimension filters,
   - relation-path construction logic,
   - rendering rules from XBRL facts/paths into LLM-readable context.
4. Add at least one detailed worked example:
   - raw fact,
   - label,
   - concept QName,
   - context,
   - period,
   - unit,
   - dimensions,
   - relation path,
   - rendered retrieval context,
   - downstream claim,
   - coding outcome.
5. Add at least one representation-risk example:
   - sign convention,
   - period mismatch,
   - dimension mismatch,
   - extension concept ambiguity,
   - missing relation-path interpretability.

### Output Files

- XBRL method section in manuscript
- online supplement technical appendix
- replication documentation for XBRL processing logic

### Acceptance Criteria

- A reviewer can see how XBRL retrieval was measured, not just that it existed.
- The paper no longer sounds as if ontology/GraphRAG implementation has already been completed if it has not.

## Workstream 4. Upgrade Measurement Independence And Coding Credibility

**Priority:** P0  
**Core risk:** The coding protocol is promising, but too much still depends on author interpretation.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 5
- Reviewer 2 Major Comment 3

### Objective

Make the coding protocol usable and believable beyond the author team.

### Required Revisions

1. Fully document coder process:
   - coder independence,
   - coder backgrounds,
   - training materials,
   - blinding procedures,
   - segmentation rules,
   - disagreement resolution,
   - disagreement taxonomy.
2. Strengthen independent coding coverage for core variables, prioritizing:
   - claim segmentation,
   - source-use type,
   - text-supported correctness,
   - graph-valid correctness,
   - integrated correctness,
   - audit-boundary coding if feasible.
3. Decide explicitly between:
   - adding audit-domain expert coding for the audit-boundary dimension, or
   - removing/softening any aggregate audit-valid empirical claims from the main text.
4. Report disagreement patterns, not only reliability statistics.
5. Add coder-facing materials to the supplement or replication package in reviewer-usable form.

### Minimum Acceptable Position

If independent expert coding for the audit-boundary dimension is not feasible in this cycle, then the paper must:

1. move that dimension more clearly into a bounded diagnostic role,
2. stop using it as if it were validated performance evidence, and
3. show that the main measurement contribution survives through the better-validated variables.

### Output Files

- coding protocol documentation
- supplement measurement appendix
- replication README and coder materials

### Acceptance Criteria

- The main findings do not depend on opaque author-only interpretation.
- Reviewers can distinguish protocol reliability from substantive audit-expert validation.

## Workstream 5. Add Bounded Separability And Stability Tests

**Priority:** P0  
**Core risk:** The paper names separability and stability but still under-demonstrates them.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 2
- Reviewer 2 Major Comment 2

### Objective

Demonstrate that the framework can detect retrieval-environment perturbations rather than only describe them conceptually.

### Required Revisions

1. Add context diagnostics by condition:
   - token or word count,
   - number of text chunks,
   - number of XBRL facts,
   - number of relation paths,
   - ordering structure,
   - construct/filer-level spread.
2. Run a bounded sensitivity matrix on selected filer-construct cells:
   - matched or closer-matched context budgets,
   - evidence-order reversal,
   - top-k variation,
   - prompt integration instruction variation,
   - if feasible, at least one additional model rerun on a narrow subset.
3. Report sensitivity results as methodological diagnostics:
   - what changed,
   - what remained stable,
   - which validity dimensions were implicated.
4. Be disciplined in wording:
   - no benchmarking claims,
   - no broad prevalence claims,
   - no "method X is better" conclusion unless the design truly supports it.

### Recommended Scope

Do not attempt full-scale cross-model benchmarking. Use a small but reviewer-relevant diagnostic grid instead.

### Output Files

- sensitivity scripts and manifests
- supplement diagnostic appendix
- revised tables/figure or compact sensitivity summary

### Acceptance Criteria

- Separability and stability are evidenced, not merely proposed.
- Reviewers can see that the paper applies its own validity dimensions to the demonstration.

## Workstream 6. Reframe The Nine-Filer Demonstration More Precisely

**Priority:** P0  
**Core risk:** Design-specific counts may still sound more general than the evidence supports.

### Reviewer Concerns Addressed

- Reviewer 1 Major Comment 2
- Reviewer 2 Major Comment 4
- Reviewer 2 Minor Comment 5

### Objective

State exactly what the nine-filer package demonstrates and what it does not.

### Required Revisions

1. Reframe the demonstration as evidence for:
   - protocol feasibility,
   - traceable retrieval environments,
   - claim-level evidence heterogeneity,
   - bounded mechanism diagnosis,
   - bounded sensitivity diagnostics.
2. Avoid framing the 8-of-89 result or similar counts as general frequency claims.
3. Explain what is learned from:
   - the deep cases,
   - the extension cases,
   - the sensitivity subset,
   - the independent coding subset.
4. Add explicit language such as:
   - "in this design,"
   - "within this retrieval implementation,"
   - "for this model/prompt/context architecture,"
   - where broader generalization is not supported.
5. State the design purpose of the extension sample:
   - not representativeness,
   - not prevalence estimation,
   - but bounded transferability of the protocol across filer settings.

### Output Files

- main demonstration section
- supplement design map
- response-to-reviewers outline

### Acceptance Criteria

- No reviewer can reasonably say the manuscript overreads design-specific counts as universal facts.

## Workstream 7. Increase Audit-Specific Fit

**Priority:** P1  
**Core risk:** The paper can still be read as general AI/accounting methods with audit-themed examples.

### Reviewer Concerns Addressed

- Reviewer 2 Major Comment 5
- Reviewer 2 Major Comment 1

### Objective

Make the paper unmistakably an auditing-methodology contribution.

### Required Revisions

1. Strengthen audit-specific logic throughout:
   - sufficiency,
   - appropriateness,
   - reliability,
   - assertion-level reasoning,
   - management-reported data versus audit evidence,
   - documentation and inspectability.
2. Add one compact example showing that the same retrieved evidence can be:
   - filing-supported,
   - graph-valid,
   - yet insufficient for an audit conclusion.
3. Use the audit-evidence hierarchy from Workstream 0 to prevent public filing/XBRL evidence from being mistaken for audit evidence sufficiency.
4. Clarify intended use cases:
   - archival audit research using LLMs as measurement tools,
   - audit analytics/system studies,
   - studies of LLM-assisted audit judgment,
   - but not claims about real audit evidence sufficiency unless additional evidence exists.
5. If feasible, add a clearly audit-specific vignette using standards language or internal-control framing, even if the main demonstration remains public-filing based.

### Output Files

- introduction
- theory/framework section
- discussion/conclusion

### Acceptance Criteria

- An AJPT reviewer sees the paper as method guidance for audit research, not generic RAG documentation.

## Workstream 8. Improve Positive Framing And Reduce Defensive Repetition

**Priority:** P1  
**Core risk:** The manuscript sometimes sounds more careful than confident.

### Reviewer Concerns Addressed

- Reviewer 1 Minor Comment 1
- Reviewer 1 Minor Comment 2
- Reviewer 2 Minor Comment 1
- Reviewer 2 Minor Comment 4

### Objective

Keep the boundary discipline while making the contribution easier to feel early.

### Required Revisions

1. Move the claim-level evidence divergence result earlier in the paper.
2. Add an early visual or compact example separating:
   - text-supported,
   - graph-valid,
   - audit-boundary,
   - integrated evidence use.
3. Reduce repeated caveat language in early sections.
4. Rewrite abstract and introduction so they lead with:
   - the problem,
   - the methodological contribution,
   - the practical reviewer decision rule,
   - the evidence package.
5. Add a short reader-facing retrieval mechanics example showing how top-k, chunk size, source ordering, or relation-path depth changes the model's effective information set.
6. Consolidate or relocate tables that create a checklist feel, preserving core tables that support contribution, measurement, and evidence.

### Output Files

- abstract
- introduction
- first figure or example table

### Acceptance Criteria

- The manuscript reads as assertive and bounded, not cautious and repetitive.

## Workstream 9. Replication Package And Reproducibility Cleanup

**Priority:** P1  
**Core risk:** Strong package quality can still be undermined by ambiguity or stale metadata.

### Reviewer Concerns Addressed

- Reviewer 1 Minor Comment 5
- Reviewer 1 Minor Comment 7
- Reviewer 2 Minor Comment 6

### Objective

Keep the package aligned with the paper's own traceability standard.

### Required Revisions

1. Verify all model metadata:
   - model name,
   - local ID,
   - digest boundary if unavailable,
   - runtime version,
   - parameter settings.
2. Verify all counts appearing in:
   - manuscript,
   - supplement,
   - README,
   - manifests,
   - response letter.
3. Ensure authoritative and deprecated artifacts remain clearly separated.
4. Add or update a reviewer-facing file map showing where to find:
   - manuscript evidence files,
   - coding materials,
   - sensitivity outputs,
   - construct protocol materials,
   - XBRL diagnostics.

### Output Files

- replication README
- file index / manifest
- metadata note

### Acceptance Criteria

- The package cannot be attacked for preventable inconsistency or ambiguity.

## Workstream 10. Literature, Citation, And Title/Terminology Cleanup

**Priority:** P2  
**Core risk:** Smaller credibility leaks remain possible.

### Reviewer Concerns Addressed

- Reviewer 1 Minor Comment 4
- Reviewer 1 Minor Comment 6
- Reviewer 2 Minor Comment 2

### Required Revisions

1. Recheck all 2025-2026 citations and statuses.
2. Strengthen literature engagement with non-accounting retrieval evaluation, evidence traceability, and RAG reproducibility work, while explaining what the audit setting adds.
3. Review terminology:
   - consider whether "audit-valid correctness" should now be consistently replaced by softer language,
   - ensure XBRL/ontology terminology does not imply unimplemented architecture.
4. Consider whether the title should stay as is or simplify if the XBRL-augmented wording overpromises relative to the implemented prototype.
5. Resolve submission-specific fields before the final upload:
   - title-page placeholders,
   - author names and affiliations,
   - corresponding-author details,
   - acknowledgments,
   - funding,
   - conflict-of-interest disclosure,
   - data-availability wording.

### Acceptance Criteria

- No terminology invites an avoidable reviewer objection.

## Reviewer-Issue Matrix

| Theme | Reviewer 1 | Reviewer 2 | Required Response Type |
|---|---|---|---|
| Incremental contribution unclear | Major 1 | Major 1 | theory rewrite + comparison table + decision rule |
| Demonstration too bounded | Major 2 | Major 2, 4 | bounded sensitivity + tighter wording |
| Audit constructs underspecified | Major 3 | Major 5 | ex ante construct protocols + audit-boundary cleanup |
| XBRL retrieval under-validated | Major 4 | Major 5 | coverage diagnostic + technical walk-through |
| Coding independence incomplete | Major 5 | Major 3 | stronger independent coding documentation and/or audit-boundary narrowing |
| Overgeneralization risk | implied | Major 4 | redesign phrasing of counts and claims |
| Audit-specific fit needs strengthening | implied | Major 1, 5 | stronger auditing logic throughout |

## Proposed Revision Sequence

| Step | Workstream | Status | Notes |
|---:|---|---|---|
| 0 | Workstream 0: Claim-evidence calibration | Completed | Claim-evidence register, red-team wording pass, decision-rule table, and audit-evidence hierarchy completed |
| 1 | Workstream 1: Incremental contribution | Completed | Adjacent-validity and RAG/evidence-traceability positioning strengthened |
| 2 | Workstream 2: Audit construct protocols | Completed | Revenue and inventory ex ante construct protocols added |
| 3 | Workstream 3: XBRL retrieval validation | Completed | Construct-family coverage diagnostics, worked examples, and mechanics notes added |
| 4 | Workstream 4: Coding independence | Completed | Independent coder documentation and reliability evidence strengthened; audit-boundary claims narrowed |
| 5 | Workstream 5: Separability/stability tests | Completed | Context-volume and source-environment perturbation diagnostics added |
| 6 | Workstream 6: Demonstration reframing | Completed | Nine-filer protocol-validation framing and design-specific count boundaries added |
| 7 | Workstream 7: Audit-specific fit | Completed | Audit use cases, same-evidence boundary example, and AJPT positioning strengthened |
| 8 | Workstream 8: Positive framing cleanup | Completed | Abstract/introduction/discussion sharpened and caveat repetition reduced |
| 9 | Workstream 9: Replication cleanup | Completed | Replication README, file map, checksum notes, and reviewer file map refreshed |
| 10 | Workstream 10: Citation/terminology polish | Completed | Title, citation status, terminology, and submission placeholders checked |

## Workflow Tracker

Use this table during implementation.

| ID | Task | Priority | Owner | Status | Evidence / Output | Notes |
|---|---|---|---|---|---|---|
| SR-00 | Build claim-evidence calibration register | P0 | Codex | Completed | `plan/116_claim_evidence_calibration_register.md` | independent-plan addition |
| SR-00A | Complete red-team wording pass for overclaiming language | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `plan/117_red_team_wording_pass_log.md` | overclaiming language narrowed |
| SR-00B | Add reviewer decision-rule table | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/118_reviewer_decision_rule_table_log.md` | inference-invalidating vs design-confounding vs disclosure-limiting |
| SR-00C | Add audit-evidence hierarchy | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/119_audit_evidence_hierarchy_implementation_log.md` | public filing support through audit evidence sufficiency |
| SR-01 | Draft adjacent-validity comparison section and table | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/120_adjacent_validity_positioning_revision_log.md` | added RAG evaluation, evidence traceability, and XBRL data-quality positioning |
| SR-02 | Add reviewer decision rule for retrieval-environment validity failures | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/118_reviewer_decision_rule_table_log.md` | completed through SR-00B |
| SR-03 | Write ex ante construct protocol for revenue | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/121_ex_ante_construct_protocol_revision_log.md` | revenue protocol added |
| SR-04 | Write ex ante construct protocol for inventory | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/121_ex_ante_construct_protocol_revision_log.md` | inventory protocol added |
| SR-05 | Build XBRL concept/relation coverage diagnostic | P0 | Codex | Completed | Added construct-family coverage script, Appendix C2/C3, manuscript/Table 6 linkage, and replication package outputs | `plan/122_xbrl_construct_coverage_diagnostic_revision_log.md` |
| SR-06 | Add XBRL worked example and representation-risk example | P0 | Codex | Completed | Added NKE inventory source-to-claim trace, period/dimension representation-risk example, and replication package artifact | `plan/123_xbrl_worked_example_and_representation_risk_log.md` |
| SR-07 | Expand coder-process documentation | P0 | Codex | Completed | Added coder-process documentation, Appendix F4A, manuscript process disclosure, coding protocol wording cleanup, and replication package copy | `plan/124_independent_coder_process_documentation_log.md` |
| SR-08 | Decide expert audit-boundary coding vs claim narrowing | P0 | Author + Codex | Completed | Gate A resolved as claim narrowing; added decision memo, Appendix F4B, manuscript boundary wording, README legacy-column note | `plan/125_gate_a_audit_boundary_validation_decision_memo.md`; `plan/126_audit_boundary_claim_narrowing_implementation_log.md` |
| SR-09 | Run bounded separability/stability sensitivity set | P0 | Codex | Completed | `data/processed/sensitivity/bounded_sensitivity_decision_summary.md`; `plan/127_bounded_sensitivity_decision_matrix_log.md` | retrieval-stage decision matrix added; no model-output robustness claim |
| SR-10 | Reframe nine-filer demonstration and design-specific counts | P0 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `plan/128_nine_filer_demonstration_scope_reframing_log.md`; `plan/129_response_to_reviewers_demonstration_scope_outline.md` | added evidence-layer design map and design-specific count boundary |
| SR-11 | Strengthen audit-specific contribution language | P1 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `plan/130_audit_specific_contribution_strengthening_log.md`; `plan/131_response_to_reviewers_audit_specific_fit_outline.md` | added intended audit use cases and same-evidence audit-boundary example |
| SR-12 | Move empirical motivation earlier and reduce caveat repetition | P1 | Codex | Completed | `submission/Manuscript_Retrieval_as_Research_Design.md`; `plan/132_positive_framing_and_motivation_revision_log.md`; `plan/133_response_to_reviewers_positive_framing_outline.md` | abstract/intro rewritten; early retrieval mechanics and claim-layer examples added |
| SR-13 | Refresh replication manifests, metadata, and file map | P1 | Codex | Completed | `submission/replication_package/REVIEWER_FILE_MAP.md`; `submission/replication_package/AUTHORITATIVE_FILES.md`; `submission/replication_package/README_REPLICATION.md`; `plan/134_replication_package_cleanup_log.md`; `plan/135_response_to_reviewers_replication_cleanup_outline.md` | counts, file map, checksum note, and diagnostic pipeline steps refreshed |
| SR-14 | Recheck citations, terminology, and title alignment | P2 | Codex | Completed | title revised to XBRL relational retrieval; RAGAS/ARES citation status checked; terminology cleaned | plan/136; plan/137 |
| SR-15 | Add non-accounting RAG/evidence-traceability literature positioning | P1 | Codex | Completed | Literature review / theory text | added AIS/citation-generation positioning and audit-specific boundary |
| SR-16 | Add reader-facing retrieval mechanics example | P1 | Codex | Completed | Intro/framework example | added Section IV mechanics example and Appendix B/C mechanics notes |
| SR-17 | Consolidate tables and reduce checklist feel | P2 | Codex | Completed | Tables/figures package | main-text reporting section reframed around evidence tiers; appendix table listings shortened |
| SR-18 | Resolve final title-page and author placeholders | P2 | Author + Codex | Author action required | Title page / cover letter | Codex placeholder audit completed; final author data needed before DOCX regeneration |
| SR-19 | Audit Major Comment 1 contribution positioning | P0 | Codex | Completed | `plan/147_major_comment_1_contribution_positioning_audit.md`; manuscript Sections I-III; Tables 2-3 | framed retrieval-environment validity as an audit-specific organizing framework / diagnostic lens, not a universal validity category |
| SR-20 | Audit Major Comment 2 demonstration validation | P0 | Codex | Completed | `plan/148_major_comment_2_demonstration_validation_audit.md`; manuscript Sections VII-VIII; Appendix I | confirmed Tier 1 protocol-validation path and explicit non-claim of model validation |
| SR-21 | Audit Major Comment 3 coding independence | P0 | Codex | Completed | `plan/149_major_comment_3_coding_independence_audit.md`; manuscript Section VII; Appendix F4-F5 | added disagreement-pattern reporting and clarified audit-boundary notes are not expert audit-valid labels |
| SR-22 | Audit Major Comment 4 design-specific counts | P0 | Codex | Completed | `plan/150_major_comment_4_design_specific_counts_audit.md`; manuscript Sections I and VII; Appendix H | tightened 8/89 count as design-specific mechanism evidence, not population or general hybrid-retrieval evidence |
| SR-23 | Audit Major Comment 5 audit construct positioning | P0 | Codex | Completed | `plan/151_major_comment_5_audit_construct_positioning_audit.md`; manuscript Sections IV and VIII; Appendix A; Table 6 | added task-success criteria and distinguished public-reporting audit-research methodology from audit-practice evidence environments |
| SR-24 | Audit Minor Comments coverage | P1 | Codex | Completed | `plan/152_minor_comments_coverage_audit.md`; manuscript Introduction; Tables/Figures packet | added Figure 1A compact correctness-layer example and documented minor-comment coverage |
| SR-25 | Prepare response-letter master outline | P1 | Codex | Completed | `plan/153_second_revision_response_letter_master_outline.md`; updated crosswalk | consolidated reviewer-facing narrative and response positions |
| SR-26 | Draft second-revision response letter | P1 | Codex | Completed | `submission/Response_to_Reviewers_Second_Revision.md`; submission file list/readme | drafted response letter organized by Major Comments 1-5 and Minor Comments |

## Key Decision Gates

These decisions should be made explicitly rather than drifting during revision.

### Gate A. Audit-Boundary Validation

Choose one:

1. **Preferred**: add audit-domain expert coding for the audit-boundary dimension, or
2. **Fallback**: retain audit-boundary as a bounded diagnostic and remove any wording that makes it sound like validated audit-performance evidence.

### Gate B. Additional Model Evidence

Choose one:

1. add one bounded cross-model sensitivity rerun on a narrow subset, or
2. keep the single-model design but tighten the manuscript wherever generality might otherwise be inferred.

### Gate C. Title Scope

Choose one:

1. keep current title if XBRL validation becomes materially stronger, or
2. simplify title/subtitle if the current wording still suggests a broader XBRL/ontology implementation than the manuscript shows.

## Response-To-Reviewers Architecture

The next response letter should be organized around shared methodological themes, not just reviewer-by-reviewer line items.

Suggested headings:

1. Calibrating manuscript claims to their evidence level
2. Sharpening the distinct contribution of retrieval-environment validity
3. Tightening audit-construct specification and audit-boundary language
4. Validating the XBRL relational retrieval layer
5. Strengthening coding independence and measurement credibility
6. Adding bounded separability and stability diagnostics
7. Reframing the demonstration to avoid overgeneralization
8. Strengthening AJPT fit and audit-specific relevance
9. Replication and metadata clarifications

Each response should state:

1. the concern,
2. the revision made,
3. where it appears,
4. what new evidence was added,
5. what boundary was preserved.

The response letter should also include or be guided by an evidence map:

| Reviewer Concern | New Evidence Added | Claim Narrowed? | Manuscript Location | Residual Boundary |
|---|---|---|---|---|

## Go / No-Go Criteria Before Resubmission

Do **not** resubmit until the following are true:

1. Every major claim has been classified in the claim-evidence calibration register.
2. The manuscript clearly distinguishes retrieval-environment validity from adjacent validity concepts.
3. Revenue and inventory constructs are defined ex ante with evidence sufficiency boundaries.
4. XBRL concept/relation coverage and representation logic are documented.
5. Core coding variables have stronger independent validation, or claims are narrowed accordingly.
6. At least one bounded separability/stability diagnostic is completed and reported.
7. Design-specific counts are framed without overgeneralization.
8. Audit-specific contribution is visible throughout the manuscript, not only in the conclusion.
9. Replication docs, metadata, and counts are fully synchronized.
10. Response-to-reviewers language can point to substantive additions rather than only rewording.
11. Title page, cover letter, disclosures, and data-availability statements contain no placeholders.
12. The final table package is lean enough that the paper reads as an argument rather than a checklist.
13. A final red-team wording pass finds no unsupported model-performance, audit-evidence, or broad-generalization implications.

## Additional Task Log

Record any new tasks that arise during implementation here.

| Date | New Task | Trigger | Priority | Status | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Revision Log

Record completed actions here as work progresses.

| Date | Workstream / Task ID | Action Taken | Files Updated | QA / Verification |
|---|---|---|---|---|
| 2026-05-31 | SR-00 | Created claim-evidence calibration register classifying major manuscript claims by evidence level and action required | `plan/116_claim_evidence_calibration_register.md`; `plan/112_second_revision_comprehensive_revise_plan.md` | SR-00 marked completed |
| 2026-05-31 | SR-00A | Applied red-team wording pass to narrow overclaiming language in manuscript and supplement | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `plan/117_red_team_wording_pass_log.md` | Search QA found no remaining direct `audit-valid`, `retrieval effects`, `changes the evidence basis`, or `What this validates` wording in checked files |
| 2026-05-31 | SR-00B | Added reviewer decision-rule table and renumbered main-text tables | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/118_reviewer_decision_rule_table_log.md` | Table callouts/headings aligned from Table 1 to Table 9; risky phrase QA passed for checked manuscript/tables files |
| 2026-05-31 | SR-00C | Added audit-evidence hierarchy to distinguish public-filing support, XBRL graph/reporting support, assertion relevance, audit-boundary diagnostics, and audit evidence sufficiency | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/119_audit_evidence_hierarchy_implementation_log.md` | QA confirmed hierarchy language appears as boundary framing and does not claim audit evidence sufficiency |
| 2026-06-01 | SR-01 | Strengthened adjacent-validity positioning against construct validity, RAG evaluation, evidence traceability, and XBRL data-quality research | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/120_adjacent_validity_positioning_revision_log.md` | New RAG references cited and listed; Table 2 expanded; audit-specific contribution preserved |
| 2026-06-01 | SR-03 / SR-04 | Added ex ante construct protocols for revenue recognition risk and inventory valuation assertion | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/121_ex_ante_construct_protocol_revision_log.md` | PCAOB standards cited; Appendix Tables A2/A3 added; Table 6 expanded; audit evidence sufficiency boundary preserved |
| 2026-06-01 | SR-15 | Added non-accounting RAG, attribution, and citation-generation positioning | `submission/Manuscript_Retrieval_as_Research_Design.md`; `plan/138_non_accounting_rag_traceability_positioning_log.md`; `plan/139_response_to_reviewers_rag_traceability_positioning_outline.md` | Rashkin et al. (2023) and Gao et al. (2023) cited and listed; manuscript clarifies that source attribution and citation support are necessary but not sufficient for audit-research inference |
| 2026-06-01 | SR-16 | Added reader-facing retrieval mechanics example and supplement mechanics notes | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `plan/140_reader_facing_retrieval_mechanics_example_log.md`; `plan/141_response_to_reviewers_retrieval_mechanics_example_outline.md` | QA confirmed top-k, chunking, relation-path, source-order, token-budget, Appendix B/C/I linkages, and Tier 1 versus Tier 2/Tier 3 boundaries |
| 2026-06-01 | SR-17 | Reduced checklist tone in main-text reporting and table package | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Tables_and_Figures.md`; `plan/142_table_consolidation_and_checklist_tone_reduction_log.md`; `plan/143_response_to_reviewers_table_consolidation_outline.md` | Table 8 reframed as evidence tiers; Section VI reorganized around source inventory, retrieval recipe, and output linkage; appendix table listings shortened |
| 2026-06-01 | SR-18 | Audited final title-page and author placeholders | `submission/Cover_Letter.md`; `submission/Author_Information_Checklist.md`; `plan/144_final_author_placeholder_audit_log.md`; `plan/145_response_to_reviewers_author_placeholder_and_submission_cleanup_outline.md` | Author-specific placeholders identified; manuscript table/figure callouts separated from author placeholders; DOCX regeneration deferred until author data are final |
| 2026-06-01 | Response evidence crosswalk | Consolidated reviewer concerns, revisions, evidence added, narrowed claims, locations, and residual boundaries | `plan/146_second_revision_reviewer_response_evidence_crosswalk.md`; `plan/112_second_revision_comprehensive_revise_plan.md` | Workstream status table updated; remaining tasks limited to author metadata, DOCX regeneration, package rebuild, and final QA |
| 2026-06-01 | SR-19 to SR-24 | Audited Major Comments 1-5 and Minor Comments against the revised manuscript; added targeted wording fixes and Figure 1A | `submission/Manuscript_Retrieval_as_Research_Design.md`; `submission/Online_Supplement_Appendix.md`; `submission/Tables_and_Figures.md`; `plan/147_major_comment_1_contribution_positioning_audit.md` through `plan/152_minor_comments_coverage_audit.md` | Major comments now have reviewer-facing evidence logs; remaining risk is mostly response-letter framing and final style/metadata QA |
| 2026-06-01 | SR-25 | Prepared master response-letter outline and updated reviewer evidence crosswalk | `plan/153_second_revision_response_letter_master_outline.md`; `plan/146_second_revision_reviewer_response_evidence_crosswalk.md`; `plan/112_second_revision_comprehensive_revise_plan.md` | Response narrative now organized around claim calibration, conceptual contribution, demonstration scope, coding reliability, audit-boundary discipline, and minor-comment coverage |
| 2026-06-01 | SR-26 | Drafted second-revision response letter and added it to submission tracking | `submission/Response_to_Reviewers_Second_Revision.md`; `submission/FINAL_SUBMISSION_FILE_LIST.md`; `submission/00_SUBMISSION_README.md`; `plan/112_second_revision_comprehensive_revise_plan.md` | Response letter remains in Markdown draft form; convert/regenerate if the final submission package requires DOCX |

## Current Recommendation

The reviewers are not asking for a wholesale redesign of the paper. They are asking for a cleaner and better-evidenced version of the paper's strongest idea.

That means the next revision should avoid two traps:

1. **Do not respond mainly with more caveats.** The paper is already cautious.
2. **Do not overreact into a full benchmark study.** That would dilute the methodological contribution and likely create new execution risk.

The right move is a disciplined second revision that adds:

1. clearer conceptual distinctiveness,
2. tighter audit-construct protocols,
3. more defensible XBRL validation,
4. stronger measurement independence,
5. a bounded but real sensitivity package,
6. more precise interpretation of what the demonstration establishes.

If those pieces are implemented well, the paper's path to acceptance becomes much more credible.
