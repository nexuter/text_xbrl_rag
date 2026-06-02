# Independent Second-Revision Improvement Plan

## Purpose

This plan was developed independently from `plan/112_second_revision_comprehensive_revise_plan.md` by rereading only the two second-round referee reports and asking:

> If we did not already have a revision plan, what would the next revision need to do to earn an accept or minor-revision outcome?

The purpose is not to replace `plan/112`, but to create a second diagnostic view that can be merged with the existing workflow.

## Independent Reviewer Diagnosis

The reviewers are not rejecting the premise. They are saying that the paper's strongest insight is still surrounded by three unresolved tensions:

1. **Conceptual tension**: retrieval-environment validity is intuitively useful, but not yet proven distinct from existing validity and RAG-evaluation language.
2. **Evidence tension**: the manuscript describes a methodological framework but presents demonstration evidence that sometimes sounds stronger than the design warrants.
3. **Audit-positioning tension**: the paper is submitted to AJPT, yet its evidence base is public filing text and XBRL data, which are audit-relevant but not audit evidence in the strict sense.

The revision should therefore be organized around claim calibration:

> every major manuscript claim must be classified as conceptual, protocol-validation, measurement-validation, sensitivity-supported, or future guidance, and the evidence level must match that classification.

## Independent Revision Strategy

The most persuasive next revision should do four things:

1. **Make the paper's central claim smaller but sharper.**
   - The paper should not claim to validate hybrid retrieval, XBRL-augmented reasoning, or LLM audit performance.
   - It should claim to validate a research-design protocol for specifying and auditing retrieval environments.

2. **Turn reviewer skepticism into a visible design principle.**
   - The manuscript should explicitly say that the reviewers' concerns are exactly why retrieval-environment validity is needed: condition labels are not evidence environments, and source traceability is not audit validity.

3. **Add targeted evidence where the framework currently looks self-referential.**
   - Sensitivity diagnostics, XBRL coverage diagnostics, and coding independence should show the framework working on itself.

4. **Create an editor-facing response package that makes acceptance easier.**
   - The response should not just list edits. It should show a claim-evidence downgrading table, new evidence added, and residual boundaries.

## Independent Workstreams

### Workstream A. Claim-Evidence Calibration Register

**Priority:** P0

Create a table that lists every major empirical and methodological claim in the manuscript and assigns it one of five evidence levels:

| Evidence Level | Meaning |
|---|---|
| Conceptual | Supported by theory/literature reasoning |
| Protocol-validation | Supported by implemented artifacts, logs, traceability, and reproducibility |
| Measurement-validation | Supported by independent coding or reliability evidence |
| Sensitivity-supported | Supported by perturbation, rerun, or robustness diagnostics |
| Future guidance | Proposed as guidance, not completed evidence |

For each claim, record:

1. claim text or paraphrase,
2. current manuscript location,
3. current evidence,
4. appropriate evidence level,
5. action: keep, narrow, move to supplement, move to future guidance, or remove,
6. reviewer risk if unchanged.

This register should drive the revision before prose editing begins.

### Workstream B. Red-Team Paragraph Pass

**Priority:** P0

Conduct a paragraph-level scan of the manuscript for phrases that trigger the reviewers' concerns:

1. "validates the framework",
2. "shows retrieval effects",
3. "audit-valid correctness",
4. "hybrid retrieval improves",
5. "XBRL-augmented reasoning",
6. "model performance",
7. "generalizes",
8. "robust",
9. "evidence" when the source is only public filing or management-reported XBRL.

Each phrase should be classified:

- acceptable as written,
- revise for boundary discipline,
- relocate to future guidance,
- delete.

### Workstream C. Reviewer Decision-Rule Table

**Priority:** P0

Add a reviewer-facing table that answers the question both reviewers are effectively asking:

> When should retrieval problems change the conclusion of an LLM-based audit study?

The table should classify retrieval problems as:

1. **Inference-invalidating**: the retrieved information set omits or misrepresents construct-critical evidence.
2. **Design-confounding**: retrieval condition differs in context volume, order, salience, model, or prompt in a way that prevents causal interpretation.
3. **Measurement-threatening**: coding or source-use categories cannot be applied independently or reliably.
4. **Disclosure-limiting**: retrieval details are incomplete but the study makes only descriptive or illustrative claims.
5. **Acceptable boundary**: limitation is disclosed and does not affect the specific claim being made.

This table should make the construct practical rather than abstract.

### Workstream D. Audit-Evidence Boundary Rebuild

**Priority:** P0

Rebuild the audit-language layer around a strict hierarchy:

1. public-filing support,
2. XBRL graph/reporting support,
3. assertion relevance,
4. audit-boundary diagnostic,
5. audit evidence sufficiency.

The manuscript should state that the current demonstration reaches levels 1-4, but not level 5.

This hierarchy should replace ambiguous use of "audit-valid correctness."

### Workstream E. Minimal But Real Sensitivity Package

**Priority:** P0

The sensitivity package should be small but visibly responsive to reviewers. It should include:

1. matched or normalized context budget for selected cells,
2. evidence-order reversal,
3. prompt integration instruction,
4. top-k or relation-depth variation,
5. one optional second-model rerun if feasible.

The output should not be framed as performance evidence. It should be framed as a demonstration that the protocol can diagnose whether claims are sensitive to retrieval-environment perturbations.

### Workstream F. XBRL Retrieval Coverage As Measurement Validity

**Priority:** P0

Treat XBRL retrieval not as a technical appendix but as a measurement-validity problem.

For each construct:

1. identify ex ante XBRL concepts and relation types,
2. document retrieved coverage,
3. explain missing or excluded concepts,
4. flag extension concepts,
5. show whether relation paths are construct-relevant or merely available.

The key point should be:

> XBRL relational retrieval must itself be validated before downstream LLM outputs can be interpreted.

### Workstream G. Independent Coding Boundary

**Priority:** P0

Make a direct decision:

1. Add audit-domain expert coding for audit-boundary judgments; or
2. explicitly remove all aggregate audit-validity implications and present audit-boundary coding as a preliminary diagnostic.

The revision should not remain halfway between these positions.

### Workstream H. Paper Architecture Reset

**Priority:** P1

The paper should be reorganized around a clearer narrative:

1. LLM audit studies create an observed evidence environment through retrieval.
2. Existing validity language does not force researchers to validate that observed environment.
3. Retrieval-environment validity supplies the missing diagnostic layer.
4. The framework operationalizes this through construct protocols, retrieval diagnostics, claim coding, and sensitivity checks.
5. The demonstration shows the protocol in action, not model superiority.
6. The revised manuscript gives researchers and reviewers decision rules.

This architecture should reduce repetition and make the paper feel like an argument rather than a checklist.

### Workstream I. Response-Letter Evidence Map

**Priority:** P1

Prepare the response letter around an evidence map:

| Reviewer Concern | New Evidence Added | Claim Narrowed? | Manuscript Location | Residual Boundary |
|---|---|---|---|---|

This is important because the reviewers explicitly respect the paper's transparency. The response should turn that transparency into editorial confidence.

### Workstream J. Acceptance-Level Final QA

**Priority:** P1

Before resubmission, conduct an acceptance-level QA pass:

1. Can a skeptical reviewer state the unique contribution in one sentence?
2. Does every major empirical claim have a matching evidence level?
3. Does the paper avoid all model-performance implications?
4. Does the public-filing/XBRL setting remain clearly bounded?
5. Are coding and sensitivity additions visible in the abstract/introduction, not buried in the supplement?
6. Does the response letter make it easy for the editor to see substantial progress?

## What This Independent Plan Adds Beyond The Existing Plan

The existing plan is strong on workstreams and reviewer comment coverage. This independent plan adds a stronger **claim-governance layer**:

1. a claim-evidence calibration register,
2. a red-team paragraph pass,
3. a reviewer decision-rule table,
4. an audit-evidence hierarchy,
5. an evidence-map structure for the response letter,
6. acceptance-level QA questions.

These additions are important because the reviewers' deepest concern is not simply that some analyses are missing. Their deeper concern is that the manuscript sometimes asks bounded evidence to carry broader methodological claims.

## Recommendation For Merger

Merge this independent plan into `plan/112` by adding:

1. a new claim-evidence calibration workstream,
2. a required red-team wording pass,
3. a reviewer decision-rule table deliverable,
4. an audit-evidence hierarchy deliverable,
5. response-letter evidence-map requirements,
6. final acceptance-level QA criteria.

These additions should make the revision process more disciplined and improve the chance that the next submission receives an accept or minor-revision recommendation rather than another major revision.
