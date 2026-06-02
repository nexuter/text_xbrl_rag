# Second-Revision Plan Merge Log

## Purpose

This log records the requested process:

1. review the second-round referee reports independently from the existing plan,
2. create a separate independent improvement plan,
3. merge the independent plan with the existing second-revision workflow,
4. document what changed and why.

## Files Created Or Updated

| File | Role |
|---|---|
| `plan/114_independent_second_revision_improvement_plan.md` | Independent zero-base improvement plan based only on reviewer reports |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Authoritative second-revision workflow, now strengthened with independent-plan additions |
| `plan/115_second_revision_plan_merge_log.md` | This merge log |

## Independent Plan Diagnosis

The independent review found that the current plan was strong on reviewer-comment coverage but needed a stronger claim-governance layer.

The independent diagnosis was:

1. Reviewers are persuaded by the topic but not fully persuaded that the manuscript's claims and evidence are aligned.
2. The paper should not merely add caveats or more analyses; it should calibrate every claim to the evidence level supporting it.
3. The next revision needs to make it easy for reviewers to see which claims are conceptual, which are protocol-validated, which are measurement-validated, which are sensitivity-supported, and which are future guidance.

## Main Additions Merged Into Plan 112

### 1. New Workstream 0

Added:

**Workstream 0. Claim-Evidence Calibration And Red-Team Wording Pass**

This workstream now precedes all other revision work. It requires:

1. a claim-evidence calibration register,
2. evidence-level classification for every major claim,
3. a keep/narrow/move/remove decision,
4. red-team wording scan,
5. reviewer decision-rule table,
6. audit-evidence hierarchy.

### 2. Claim-Evidence Register

Added requirement to classify major claims as:

1. conceptual,
2. protocol-validation,
3. measurement-validation,
4. sensitivity-supported,
5. future guidance.

This directly addresses the reviewers' concern that some evidence is bounded while some wording sounds broader.

### 3. Red-Team Wording Pass

Added explicit scan for terms that could trigger another major-revision concern:

1. "validates the framework,"
2. "retrieval effects,"
3. "audit-valid correctness,"
4. "hybrid retrieval,"
5. "XBRL-augmented reasoning,"
6. "model performance,"
7. "generalizes,"
8. "robust,"
9. "evidence" when referring only to public filing text or management-reported XBRL.

### 4. Reviewer Decision-Rule Table

Added a required table classifying retrieval problems as:

1. inference-invalidating,
2. design-confounding,
3. measurement-threatening,
4. disclosure-limiting,
5. acceptable boundary.

This strengthens the practical contribution: reviewers should see how the framework changes manuscript evaluation decisions.

### 5. Audit-Evidence Hierarchy

Added a hierarchy distinguishing:

1. public-filing support,
2. XBRL graph/reporting support,
3. assertion relevance,
4. audit-boundary diagnostic,
5. audit evidence sufficiency.

This is important because both reviewers are concerned that public filing/XBRL material is audit-relevant but not audit evidence in the strict sense.

### 6. Response Letter Evidence Map

Added requirement that the response letter be guided by:

| Reviewer Concern | New Evidence Added | Claim Narrowed? | Manuscript Location | Residual Boundary |
|---|---|---|---|---|

This should make the second revision easier for reviewers and the editor to evaluate.

### 7. Revised Revision Sequence

The proposed revision sequence now starts with:

1. Workstream 0: Claim-evidence calibration,
2. Workstream 1: Incremental contribution,
3. Workstream 2: Audit construct protocols,
4. Workstream 3: XBRL retrieval validation.

This ordering is deliberate. Claim calibration should govern the rest of the revision, not follow it.

### 8. New Workflow Tracker Items

Added:

| ID | Task |
|---|---|
| SR-00 | Build claim-evidence calibration register |
| SR-00A | Complete red-team wording pass for overclaiming language |
| SR-00B | Add reviewer decision-rule table |
| SR-00C | Add audit-evidence hierarchy |

### 9. Expanded Go / No-Go Criteria

Added final resubmission criteria:

1. every major claim must be classified in the claim-evidence calibration register,
2. a final red-team wording pass must find no unsupported model-performance, audit-evidence, or broad-generalization implications.

## Assessment After Merge

The merged plan is stronger than either plan alone.

The original `112` plan was strong on:

1. reviewer-comment coverage,
2. workstream structure,
3. P0/P1/P2 prioritization,
4. planned empirical reinforcement,
5. replication and submission tracking.

The independent `114` plan added:

1. claim-level governance,
2. stronger evidence-to-claim alignment,
3. response-letter strategy,
4. audit-evidence hierarchy,
5. red-team language discipline.

Together, the merged plan should better protect the next revision from the central reviewer concern:

> The idea is promising, but the manuscript must align its claims, evidence, and audit setting more tightly before acceptance.

## Current Recommendation

Use `plan/112_second_revision_comprehensive_revise_plan.md` as the authoritative tracker.

Use `plan/114_independent_second_revision_improvement_plan.md` as a conceptual backup memo explaining why the claim-governance additions were necessary.

Begin implementation with SR-00 through SR-00C before revising the manuscript prose. This will keep the revision disciplined and reduce the risk of another round of reviewer concern about overclaiming.
