# Second-Revision Plan Coverage Audit

## Purpose

This memo rechecks the two second-round referee reports against `plan/112_second_revision_comprehensive_revise_plan.md` to verify whether the improvement plan faithfully covers the reviewers' concerns.

The audit focuses on coverage, not implementation. Its purpose is to identify whether any reviewer concern is missing, under-specified, or too broadly captured to be useful in the revision workflow.

## Bottom-Line Assessment

The second-revision plan is directionally strong and covers the major reviewer concerns. The original version of `plan/112` captured all five major concerns from both reviewers. However, several minor but reviewer-visible items were initially captured only implicitly.

Those implicit items have now been added directly to `plan/112`:

1. XBRL data-quality research as an adjacent literature for contribution positioning.
2. Non-accounting RAG evaluation and evidence-traceability literature engagement.
3. A reader-facing retrieval mechanics example covering top-k, chunking, ordering, or relation-path depth.
4. Table consolidation to reduce checklist feel.
5. Final author/title-page/disclosure placeholder cleanup.

After these additions, the plan is comprehensive enough to guide the second revision.

## Major Comment Coverage Matrix

| Reviewer Concern | Coverage In Plan 112 | Assessment |
|---|---|---|
| R1 MC1: sharper incremental contribution beyond construct validity, measurement validity, reproducibility, RAG documentation, audit documentation, XBRL data-quality research | Workstream 1; strengthened to include XBRL data-quality research and non-accounting RAG/evidence-traceability work | Covered |
| R1 MC2: demonstration too weak for some claims; add Tier 2-style sensitivity or narrow claims | Workstreams 5 and 6; Gates B; Go/No-Go criteria | Covered |
| R1 MC3: audit constructs too broad; define source sufficiency and assertion mapping ex ante | Workstream 2; Gate A; Go/No-Go criteria | Covered |
| R1 MC4: XBRL relational retrieval needs coverage/measurement validation | Workstream 3 | Covered |
| R1 MC5: coding reliability promising but incomplete; coder independence, expertise, blinding, unitization, disagreement resolution | Workstream 4 | Covered |
| R2 MC1: clearer boundary against validity/RAG concepts; strengthen audit-specific angle | Workstreams 1 and 7; strengthened literature component | Covered |
| R2 MC2: separability/stability not validated; context length, order, prompt, model confounds | Workstream 5; Gate B | Covered |
| R2 MC3: core coding evidence not independent enough; audit-valid dimension not independently validated | Workstream 4; Gate A | Covered |
| R2 MC4: broader inferences from design-specific counts | Workstream 6 | Covered |
| R2 MC5: audit construct not tight enough; public filing data distant from actual audit evidence | Workstreams 2 and 7; Gate A | Covered |

## Minor Comment Coverage Matrix

| Reviewer Concern | Coverage In Plan 112 | Assessment |
|---|---|---|
| R1 minor 1: reduce repeated boundary statements | Workstream 8 | Covered |
| R1 minor 2: move 8-of-89 hybrid integration result earlier | Workstream 8 | Covered |
| R1 minor 3: replace title-page placeholders | Workstream 10 and SR-18 added | Covered after update |
| R1 minor 4: verify 2025-2026 citations | Workstream 10 | Covered |
| R1 minor 5: clarify gemma4:31b model name/digest and reproducibility | Workstream 9 | Covered |
| R1 minor 6: rename audit-valid correctness unless expert validation is added | Workstreams 2, 4, 10; Gate A | Covered |
| R1 minor 7: consolidate tables to reduce checklist feel | Workstream 8 and SR-17 added | Covered after update |
| R2 minor 1: reduce repetition | Workstream 8 | Covered |
| R2 minor 2: engage non-accounting retrieval evaluation and evidence traceability literature | Workstreams 1 and 10; SR-15 added | Covered after update |
| R2 minor 3: acknowledge retrieval-environment validity may be subtype/diagnostic of construct validity | Workstream 1 | Covered |
| R2 minor 4: add compact visual/example separating text-supported, graph-valid, audit-valid, integrated correctness | Workstream 8 | Covered |
| R2 minor 5: explain what nine-filer extension teaches beyond applicability | Workstream 6 | Covered |
| R2 minor 6: avoid model-performance benchmark wording | Workstreams 5 and 6 | Covered |
| R2 minor 7: short example of top-k/chunking/relation-path choices altering model information set | Workstream 8 and SR-16 added | Covered after update |

## Items Strengthened In Plan 112 During This Audit

### 1. XBRL Data-Quality Literature

Reviewer 1 explicitly named XBRL data-quality research in the contribution-positioning comment. The plan already had a separate XBRL validation workstream, but the adjacent-literature comparison in Workstream 1 did not name XBRL data-quality research directly. This has been added.

### 2. Non-Accounting RAG And Evidence-Traceability Literature

Reviewer 2 asked for direct engagement with non-accounting retrieval evaluation and evidence traceability. This was implicit in the conceptual workstream but not a standalone task. The plan now includes this in Workstreams 1 and 10 and adds SR-15.

### 3. Reader-Facing Retrieval Mechanics Example

Reviewer 2 specifically asked for a short example showing how top-k, chunking, or relation-path choices alter the model's effective information set. Workstream 5 covered sensitivity testing, but not the reader-facing exposition need. Workstream 8 now includes this, and SR-16 tracks it.

### 4. Table Consolidation

Reviewer 1 noted that several tables could be consolidated. The original plan emphasized stronger tables and examples but did not explicitly require table reduction. Workstream 8 and SR-17 now track this.

### 5. Submission Placeholder Cleanup

Reviewer 1 mentioned placeholder title-page fields. The plan focused primarily on manuscript substance, but final author-field cleanup is reviewer-visible and submission-critical. Workstream 10 and SR-18 now track it.

## Remaining Strategic Judgment

The plan intentionally does not commit to a full benchmark study. That is appropriate. Both reviewers framed benchmark-level expansion as one possible route, but the manuscript's best path remains a methodology paper with bounded validation.

The highest-risk unresolved decision is **Gate A: audit-boundary validation**.

If no audit-domain expert coding is added, then the revision must be strict about using audit-boundary diagnostics only as a bounded interpretive layer. If the author can add even limited expert audit-domain coding for the audit-boundary dimension, it would materially reduce the chance of another major revision.

The second-highest-risk decision is **Gate B: additional model evidence**.

A narrow additional-model sensitivity run is not absolutely necessary if the claims are tightly framed, but adding one would give the response letter a stronger answer to the repeated "one model" concern.

## Revised Evaluation Of Plan 112

Current status:

| Area | Status |
|---|---|
| Major comments | Fully covered |
| Minor comments | Fully covered after update |
| Reviewer decision-rule concerns | Covered |
| Empirical validation concerns | Covered as planned work, not yet implemented |
| Audit-specificity concerns | Covered |
| Replication and metadata concerns | Covered |
| Final submission housekeeping | Covered after update |

## Recommendation

Use `plan/112_second_revision_comprehensive_revise_plan.md` as the authoritative second-revision workflow tracker.

Implementation should start with:

1. Workstream 1: contribution distinctiveness and adjacent-literature table.
2. Workstream 2: ex ante audit construct protocols.
3. Workstream 3: XBRL retrieval coverage diagnostic.

These three workstreams address the deepest "why is this publishable in AJPT?" concern. The sensitivity and coding workstreams should follow closely because they determine whether the revision can credibly move from another major revision toward accept or minor revision.
