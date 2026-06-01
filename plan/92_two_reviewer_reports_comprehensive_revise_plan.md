# Comprehensive Revise Plan Based On Two Reviewer Reports

## Purpose

This plan translates the two reviewer reports into a comprehensive revision roadmap for the AJPT methodological-paper manuscript:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

The plan is intended to guide the next revision cycle, track all required changes, and prevent reviewer concerns from being addressed only rhetorically. The target revision should move the paper from a promising protocol-validation demonstration to a more reviewer-evaluable AJPT methodology contribution.

## Overall Reviewer Diagnosis

Both reviewers are favorable but demanding. Their shared recommendation is **Major Revision**.

The paper's strongest assets are:

1. A timely audit-methodology problem: retrieval constructs the information environment observed by LLMs.
2. A useful core construct: retrieval-environment validity.
3. Reviewer-facing tools: five validity dimensions, tiered reporting, claim-level evidence-use coding, and XBRL boundary discipline.
4. A transparent nine-filer protocol-validation package with 72 outputs and 281 preliminary coded claims.

The paper's main weaknesses are:

1. The conceptual contribution still risks looking like construct validity plus documentation.
2. Claim-level coding remains preliminary and author-coded.
3. Sensitivity evidence is too limited, especially for stability and separability.
4. The retrieval prototype is intentionally inspectable but technically narrower than contemporary RAG systems.
5. XBRL relational retrieval needs more concrete technical examples.
6. Boundary statements are strong but sometimes crowd out positive evidence.
7. The replication package needs an authoritative-file index that clearly separates manuscript evidence from pilot, smoke, dry-run, or deprecated artifacts.

## Revision Thesis

The revised paper should be organized around a tighter thesis:

> Retrieval-environment validity is a retrieval-specific mechanism of construct drift in LLM-based audit research. It arises when the dynamically constructed evidence environment supplied to an LLM differs from the information environment required by the intended audit construct. The framework helps researchers and reviewers identify when retrieval flaws are fatal to inference, fixable through design changes, or merely reporting limitations.

This thesis should become the spine of the introduction, theory section, demonstration, and conclusion.

## Priority Levels

| Priority | Meaning |
|---|---|
| P0 | Required for a credible major revision response |
| P1 | Strongly recommended; likely to affect reviewer confidence |
| P2 | Helpful refinement; can be scoped if time or resources are constrained |

## Phase 1. Conceptual Sharpening Of Retrieval-Environment Validity

**Priority:** P0

### Reviewer Concerns Addressed

- Reviewer 1, Major Comment 1: distinguish retrieval-environment validity from construct validity, measurement validity, audit documentation, and reproducibility.
- Reviewer 2, Major Comment 1: show why existing validity and RAG evaluation concepts are insufficient.
- Reviewer 2, Minor Comment 3: clarify whether retrieval-environment validity is a form of construct validity, diagnostic lens, or distinct validity category.

### Revision Objective

Make retrieval-environment validity conceptually distinct and evaluative rather than merely descriptive.

### Planned Manuscript Changes

1. Add a new subsection in Section III, tentatively titled:
   **Retrieval-Environment Validity Relative To Adjacent Validity Concepts**

2. Add a new main-text table:
   **Table X. Retrieval-Environment Validity Versus Adjacent Validity Concepts**

   Required columns:
   - Adjacent concept
   - What it already covers
   - What it misses in dynamic retrieval
   - Retrieval-specific failure mode
   - Consequence for LLM audit inference

   Required comparison rows:
   - Construct validity
   - Measurement validity
   - Internal validity
   - Audit evidence sufficiency
   - Audit documentation/source traceability
   - Textual-analysis preprocessing validation
   - RAG system evaluation
   - Reproducibility

3. Add two short counterexamples:
   - A study appears valid because corpus, prompt, model, and output are reported, but the retrieved environment omitted construct-relevant evidence.
   - A study appears to compare model reasoning across retrieval conditions, but the conditions differ in token budget, source ordering, or evidence salience.

4. Add reviewer decision rules:
   - Fatal if retrieval omission changes the construct being tested.
   - Fatal if retrieval effects cannot be separated from model or prompt effects for a causal claim.
   - Fixable if source IDs and retrieval parameters allow reconstruction and sensitivity checks.
   - Reporting gap if retrieval details are incomplete but the study makes only limited illustrative claims.

### Files To Update

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Tables_and_Figures.md`
- `plan/69_submission_ready_manuscript_v3.md`
- `plan/71_v3_main_tables_and_figures.md`

### Acceptance Criteria

- The introduction clearly states what the literature loses without this construct.
- Section III explicitly defines retrieval-environment validity as a retrieval-specific diagnostic lens for construct drift, not a replacement for construct validity.
- The new comparison table makes the incremental contribution visible to an AJPT reviewer.

## Phase 2. Independent Claim-Coding Validation

**Priority:** P0

### Reviewer Concerns Addressed

- Reviewer 1, Major Comment 2: claim-level coding is central but author-coded and insufficiently validated.
- Reviewer 2, Major Comment 4: measurement contribution requires reliability evidence.
- Reviewer 2, Minor Comment 6: define claim segmentation more operationally.
- Reviewer 2, Minor Comment 7: clarify or avoid partial scores.

### Revision Objective

Convert claim-level coding from author illustration into a reviewer-evaluable measurement protocol.

### Planned Validation Design

Add a limited independent coding exercise.

Minimum feasible design:

1. Sample 120 claims from the 281-claim archive.
2. Oversample:
   - hybrid claims,
   - risk/assertion claims,
   - claims with both text and XBRL sources,
   - claims with one-source use inside hybrid conditions,
   - insufficient-context claims.
3. Use two independent coders with audit/accounting domain familiarity.
4. Code the following variables:
   - claim segmentation agreement,
   - claim kind,
   - evidence-use type,
   - text-supported correctness,
   - graph-valid correctness,
   - integrated correctness.
5. Treat audit-valid correctness separately:
   - either code as exploratory only,
   - or include qualitative disagreement examples rather than using it as a quantitative outcome.
6. Report:
   - percent agreement,
   - Cohen's kappa or Krippendorff's alpha where appropriate,
   - reconciliation procedure,
   - examples of ambiguous claims and final rules.

Preferred stronger design:

1. Code all 89 hybrid-condition claims plus a stratified comparison sample from text, XBRL, and LLM-only conditions.
2. Include all risk/assertion claims selected in main-text examples and appendix examples.
3. Add a coder instruction appendix.

### Claim Segmentation Rules To Add

The supplement should define a claim as an independently assessable assertion in an LLM output. Rules should cover:

1. Split factual amount/date/period statements from audit-risk interpretations.
2. Split causal explanations from factual premises.
3. Split multi-account or multi-assertion sentences when evidence requirements differ.
4. Preserve caveats and limitations as part of the claim when they determine audit-valid boundary.
5. Code insufficient-context statements as claims only when they make a source-boundary assertion.

### Files To Create Or Update

- New coding instrument:
  - `data/processed/coding/independent_coding_protocol.md`
  - `data/processed/coding/independent_coding_sample.csv`
  - `data/processed/coding/independent_coding_results.csv`
  - `data/processed/coding/intercoder_reliability_summary.md`

- Manuscript and supplement:
  - `submission/Manuscript_Retrieval_as_Research_Design.md`
  - `submission/Online_Supplement_Appendix.md`
  - `submission/README_REPLICATION.md`

### Acceptance Criteria

- The manuscript no longer relies only on preliminary author coding to support evidence-use divergence.
- At least source-use and integrated-correctness coding have independent reliability evidence.
- Audit-valid correctness remains clearly bounded unless expert audit-domain coding is completed.

## Phase 3. Separability And Token-Budget Sensitivity

**Priority:** P0

### Reviewer Concerns Addressed

- Reviewer 1, Major Comment 4: separability and token-budget confounding remain under-addressed.
- Reviewer 2, Major Comment 3: hybrid condition may differ by volume, order, salience, and formatting.
- Reviewer 2, Major Comment 2: demonstration is strongest on traceability but weaker on separability and stability.

### Revision Objective

Show that the paper applies its own separability criterion and does not simply name it.

### Planned Analyses

1. Add context-volume diagnostics by condition:
   - prompt word count,
   - context word count,
   - number of text chunks,
   - number of XBRL facts,
   - number of XBRL relation paths,
   - source ordering.

2. Report distributions:
   - mean,
   - median,
   - minimum,
   - maximum,
   - by retrieval condition and construct.

3. Add a compact sensitivity test on a subset of filer-construct cells.

Minimum sensitivity design:

| Sensitivity | Scope | Purpose |
|---|---|---|
| Token-budget matched hybrid | 3 filer-construct cells | Test whether source integration changes when total context length is constrained |
| Evidence order reversal | Same 3 cells | Test whether text-first versus XBRL-first ordering changes evidence use |
| Explicit integration instruction | Same 3 cells | Test whether hybrid non-integration reflects prompt instruction rather than retrieval environment |

Suggested cells:

1. SBUX inventory: clean narrative-XBRL factual case.
2. NKE revenue: mixed text-only/XBRL-only hybrid claims.
3. MSFT revenue: boundary case with revenue relevance and relation-path scarcity.

4. Report sensitivity findings as methodological diagnostics, not performance results.

### Files To Create Or Update

- Scripts:
  - `scripts/analyze_context_diagnostics.py`
  - `scripts/build_sensitivity_contexts.py`
  - `scripts/run_sensitivity_prompts.py`
  - `scripts/code_sensitivity_claims.py`

- Data:
  - `data/processed/retrieval_contexts/context_volume_diagnostics.csv`
  - `data/processed/sensitivity/separability_sensitivity_manifest.csv`
  - `data/processed/sensitivity/separability_sensitivity_claims.csv`
  - `data/processed/sensitivity/separability_sensitivity_summary.md`

- Manuscript/supplement:
  - Section VII demonstration
  - Section VIII boundary conditions
  - Appendix I sensitivity evidence

### Acceptance Criteria

- The manuscript reports actual context-volume diagnostics.
- Separability is no longer only future guidance.
- The sensitivity test is explicitly framed as a diagnostic check, not as model-performance evidence.

## Phase 4. Stability Sensitivity And Retrieval Variation

**Priority:** P1

### Reviewer Concerns Addressed

- Reviewer 2, Major Comment 2: stability dimension is proposed but not stress-tested.
- Reviewer 1, Major Comment 3: current retrieval prototype is limited relative to broader RAG claims.

### Revision Objective

Add minimal evidence that the protocol can diagnose retrieval variation.

### Planned Analyses

Minimum design:

1. Vary text retrieval `top-k` for selected cells:
   - current `top-k`,
   - lower `top-k`,
   - higher `top-k`.
2. Vary XBRL relation retrieval depth or relation filters:
   - current selection,
   - direct facts only,
   - facts plus relation paths.
3. Track:
   - source overlap,
   - context length,
   - claim evidence-use type,
   - whether the main inference changes.

Optional design:

1. Add a vector-retrieval variant using an embedding model available locally.
2. Keep it as a subset demonstration, not a benchmark.

### Files To Create Or Update

- `data/processed/sensitivity/retrieval_stability_manifest.csv`
- `data/processed/sensitivity/retrieval_stability_summary.md`
- Appendix I
- Replication README

### Acceptance Criteria

- Stability is supported by at least one completed diagnostic rather than only guidance.
- If vector retrieval is not implemented, the manuscript narrows claims to inspectable retrieval prototypes and describes vector/RAG architecture applicability as conceptual guidance.

## Phase 5. Mechanism Of Hybrid Integration Failure

**Priority:** P1

### Reviewer Concerns Addressed

- Reviewer 1, Major Comment 5: strongest empirical pattern is under-theorized.
- Reviewer 2, Major Comment 6: paper should state positive evidence more forcefully.

### Revision Objective

Move from descriptive evidence-use divergence to a mechanism-based explanation of why hybrid retrieval does not automatically create integrated reasoning.

### Planned Mechanism Taxonomy

Classify hybrid non-integration into categories:

1. One evidence layer unavailable: hybrid context lacks construct-relevant text or XBRL.
2. Evidence available but unused: both sources present, claim cites only one.
3. Prompt did not require integration: model had no instruction to reconcile sources.
4. Evidence redundancy: one source alone was sufficient for the claim.
5. Representation friction: XBRL facts/paths were too technical or poorly rendered.
6. Ordering/salience effect: model attended to earlier or more readable evidence.
7. Audit bridge missing: claim combined sources but did not bridge to an audit construct.

### Planned Output

1. Add a hybrid-failure mechanism table.
2. Code all hybrid-condition claims or a stratified subset into mechanism categories.
3. Report frequencies cautiously as diagnostic frequencies in the sample.
4. Link each mechanism to design remedies.

### Files To Create Or Update

- `data/processed/coding/hybrid_integration_failure_mechanisms.csv`
- `data/processed/coding/hybrid_integration_failure_summary.md`
- Section VII demonstration
- Appendix H or Appendix I

### Acceptance Criteria

- The paper explains why hybrid labels fail rather than merely reporting that they fail.
- The revised manuscript provides design remedies for each mechanism.

## Phase 6. XBRL Technical Specificity And Boundary Discipline

**Priority:** P1

### Reviewer Concerns Addressed

- Reviewer 2, Major Comment 5: XBRL component needs concrete technical examples.
- Reviewer 1, Major Comment 3: technical prototype is narrower than the broader RAG framing.
- Reviewer 2, Minor Comment 11: avoid implying RDF/OWL or GraphRAG implementation.

### Revision Objective

Make the XBRL contribution technically credible while preserving the boundary that XBRL is management-reported data, not audit evidence.

### Planned Manuscript Changes

1. Add one detailed XBRL walk-through in the main text or supplement:
   - raw fact ID,
   - concept QName,
   - label,
   - value,
   - unit,
   - decimals,
   - period,
   - dimensions,
   - relation path,
   - rendered retrieval context,
   - LLM claim,
   - graph-valid coding,
   - audit-valid boundary.

2. Add one representation-risk example:
   - sign convention,
   - period mismatch,
   - dimensional context mismatch,
   - extension concept,
   - relation-path interpretation.

3. Move RDF/OWL, ontology storage, and GraphRAG language mostly to future-implementation guidance unless implemented.

4. Revise title or subtitle if reviewers perceive `XBRL-Augmented Retrieval` as overemphasizing a not-fully-implemented ontology contribution.

### Files To Update

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `submission/Tables_and_Figures.md`
- `README_REPLICATION.md`

### Acceptance Criteria

- A reader can see exactly how XBRL facts and relation paths enter retrieval and claim coding.
- The manuscript no longer invites an expectation that RDF/OWL/GraphRAG has been implemented.

## Phase 7. Authoritative Replication Package Index

**Priority:** P0

### Reviewer Concerns Addressed

- Reviewer 1, Major Comment 6: package includes multiple run artifacts; authoritative files must be clear.
- Reviewer 2, Minor Comments 12 and 13: data availability and model metadata need more precision.

### Revision Objective

Make the replication package easy to audit and align it with the paper's own traceability standard.

### Planned Changes

1. Add an authoritative-file index:
   - manuscript tables,
   - main run manifest,
   - extension run manifest,
   - claim coding files,
   - selected examples,
   - sensitivity files,
   - checksum files.

2. Add a deprecated/pilot artifact note:
   - smoke runs,
   - dry runs,
   - `gemma4:latest` pilot files,
   - non-authoritative manifests.

3. Decide whether to remove pilot/smoke artifacts from the submission-facing replication package or clearly place them in an excluded/archive folder.

4. Add model metadata:
   - Ollama model name,
   - model digest if available,
   - Ollama version if available,
   - local hardware/software note,
   - temperature and endpoint.

### Files To Create Or Update

- `submission/replication_package/AUTHORITATIVE_FILES.md`
- `submission/replication_package/DEPRECATED_OR_PILOT_ARTIFACTS.md`
- `submission/README_REPLICATION.md`
- `README_REPLICATION.md`
- `submission/Replication_Package_Manifest.md`
- `plan/73_ollama_model_metadata_note.md`

### Acceptance Criteria

- A reviewer can identify which files reproduce manuscript counts and tables without guessing.
- Pilot artifacts cannot be confused with manuscript evidence.

## Phase 8. Positive Contribution Reframing And Redundancy Reduction

**Priority:** P1

### Reviewer Concerns Addressed

- Reviewer 2, Major Comment 6: boundary statements are helpful but sometimes substitute for positive evidence.
- Reviewer 1, Minor Comment 7: repeated boundary statements could be consolidated.
- Reviewer 2, Minor Comment 1: abstract is dense.
- Reviewer 2, Minor Comment 8: clarify practical reviewer decisions changed by the framework.

### Revision Objective

Make the paper more confident and less defensive while preserving claim boundaries.

### Planned Changes

1. Revise abstract:
   - state positive contribution earlier,
   - reduce list density,
   - include one sentence on what reviewer decision changes.

2. Revise introduction contribution paragraph:
   - emphasize retrieval-specific construct drift,
   - auditable retrieval artifacts,
   - claim-level coding that separates source support from audit-valid inference,
   - reviewer decision rules.

3. Consolidate repeated boundary statements:
   - keep strong boundary section in Section VIII,
   - reduce repetitive caveats in earlier sections.

4. Add practical significance paragraph:
   - applying the framework changes whether reviewers accept claims about model reasoning, retrieval effects, construct validity, and audit inference.

### Files To Update

- Main manuscript
- Cover letter
- Submission README if needed

### Acceptance Criteria

- The manuscript clearly states affirmative contributions, not only limitations.
- Boundary statements remain visible but less repetitive.

## Phase 9. AJPT Fit And Audit-Specific Logic

**Priority:** P1

### Reviewer Concerns Addressed

- Reviewer 2, Major Comment 7: paper sometimes reads like a general RAG/LLM methodology paper with audit examples.
- Reviewer 1, Minor Comment 8: report practical methodological significance.

### Revision Objective

Make the paper unmistakably an auditing research methodology contribution.

### Planned Changes

1. Add audit-specific logic in theory:
   - relevance,
   - reliability,
   - sufficiency,
   - documentation,
   - assertion-level reasoning,
   - management-reported data versus audit evidence.

2. Add example showing the same retrieved evidence supports:
   - a disclosure claim,
   - a graph-valid reported-structure claim,
   - but not an audit assertion conclusion without additional evidence.

3. Distinguish intended audiences:
   - researchers using LLMs as measurement tools,
   - researchers studying auditors using LLMs,
   - researchers evaluating LLM audit agents or systems.

4. Map reporting requirements to study type:
   - archival LLM audit studies,
   - audit judgment/experiment studies,
   - audit analytics/system studies.

### Files To Update

- Section II
- Section III
- Section VI
- Appendix I

### Acceptance Criteria

- AJPT reviewers see the paper as audit methodology, not generic AI methodology.
- Audit evidence and assertion logic are integrated throughout the framework.

## Phase 10. Minor Comments And Editorial Cleanup

**Priority:** P2

### Items To Address

1. Consider shorter title options:
   - `Retrieval as Research Design in LLM-Based Audit Research`
   - `Retrieval-Environment Validity in LLM-Based Audit Research`
   - `Retrieval as Research Design: Validating LLM Evidence Environments in Audit Research`

2. Narrow research question:
   - from LLM-based auditing research generally
   - to LLM-based audit research using dynamic retrieval.

3. Clarify `LLM-only`:
   - describe as a no-retrieval diagnostic baseline, not a retrieval condition.

4. Add pretraining contamination discussion:
   - describe whether LLM-only outputs showed filer familiarity,
   - explain why familiar firms are useful for interpretability but create pretraining concerns.

5. Add source detail to Table 7:
   - enough source detail for reader to understand coding without opening supplement.

6. Review all 2025/2026 references:
   - published/forthcoming/working paper status,
   - DOIs,
   - journal issue information.

7. Finalize author placeholders:
   - title page,
   - cover letter,
   - author checklist,
   - conflict/funding statements.

8. Data availability:
   - specify raw SEC files,
   - processed XBRL/text files,
   - prompts,
   - raw outputs,
   - coding files,
   - model output/licensing boundary.

### Acceptance Criteria

- Minor comments can be explicitly checked off in a response-to-reviewers document.
- No author placeholders remain in submission-ready files.

## Proposed Revision Sequence

| Step | Phase | Output |
|---:|---|---|
| 1 | Phase 7 | Authoritative replication package index and deprecated artifact note |
| 2 | Phase 1 | Conceptual distinctiveness section and table |
| 3 | Phase 3 | Context-volume diagnostics and separability analysis |
| 4 | Phase 4 | Stability or retrieval-variation sensitivity |
| 5 | Phase 2 | Independent coding protocol, sample, and reliability evidence |
| 6 | Phase 5 | Hybrid integration-failure mechanism coding |
| 7 | Phase 6 | XBRL technical walk-through examples |
| 8 | Phase 8 | Abstract/introduction/conclusion reframing |
| 9 | Phase 9 | Audit-specific theory and reporting guidance |
| 10 | Phase 10 | Minor comments, references, author fields, final QA |

## Response-To-Reviewers Structure

The eventual response letter should be organized by shared themes rather than only by reviewer.

Suggested headings:

1. Conceptual distinctiveness of retrieval-environment validity.
2. Independent validation of claim-level coding.
3. Separability, token-budget, and retrieval-stability diagnostics.
4. Mechanism analysis for hybrid integration failure.
5. XBRL technical specificity and boundary discipline.
6. Replication package authority and reviewer usability.
7. Audit-specific contribution and AJPT fit.
8. Minor and editorial revisions.

Each response should include:

- Reviewer concern,
- Revision made,
- Manuscript location,
- New evidence or table,
- Boundary preserved.

## Go / No-Go Criteria Before Resubmission

The revised manuscript should not be resubmitted until the following are complete:

1. A comparison table distinguishes retrieval-environment validity from adjacent validity concepts.
2. At least one independent coding or reliability exercise is completed, or claims are explicitly narrowed to proof-of-concept.
3. Context-volume diagnostics are reported.
4. At least one separability or stability sensitivity check is completed.
5. Hybrid integration failure is explained mechanistically.
6. XBRL walk-through examples are added.
7. Replication package authoritative files are clearly indexed.
8. Pilot/smoke/dry-run artifacts are either removed from the submission package or clearly marked non-authoritative.
9. Author placeholders are resolved.
10. All revised counts, run labels, and file paths pass final sanity checks.

## Current Strategic Recommendation

Do not respond by merely adding caveats. The reviewers already recognize that the paper is cautious. The revision should add positive evidence:

- a sharper concept,
- a small reliability exercise,
- a small separability/stability analysis,
- a mechanism analysis,
- and concrete XBRL examples.

These additions would directly address the shared major-revision concerns and give AJPT reviewers a stronger basis to view the paper as a methodological contribution rather than a well-organized RAG reporting checklist.
