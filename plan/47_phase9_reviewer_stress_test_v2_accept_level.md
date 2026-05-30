# Phase 9 Reviewer Stress Test of Manuscript Draft v2

## Purpose

This memo evaluates `plan/46_phase9_manuscript_draft_v2_after_reviewer_revisions.md` from the perspective of an AJPT reviewer after the Priority 1 revisions were implemented.

Reviewer question:

> Has the manuscript moved from major-revision risk to a credible AJPT methodology submission, and what remaining issues would prevent an accept-style recommendation?

## Overall Verdict

Conditional favorable, but not yet accept-ready.

The v2 draft is materially stronger than v1. It now clearly states why retrieval-environment validity is more than renamed construct validity, explains what audit researchers should do differently, bounds the prototype, moves aggregate preliminary coding away from performance interpretation, and adds expert-coding requirements. These changes substantially reduce desk-reject risk and make the paper look like an AJPT methodology paper rather than a technical RAG/XBRL implementation paper.

However, I would not yet give an accept recommendation. The remaining weaknesses are mostly execution and evidence-readiness issues rather than conceptual flaws. The paper needs final table integration, a clean appendix index, stronger reference polish, and either limited expert review of selected audit-valid claims or even more explicit language that audit-valid scores are illustrative only.

## Reviewer Recommendation

Revise and resubmit, with a favorable trajectory.

If I were reviewing this manuscript for an AJPT methodology call, I would likely write:

> The paper identifies an important methodological problem for LLM-based audit research and offers a useful framework that future researchers and reviewers could apply. I encourage revision. The core contribution is promising, but the manuscript should further polish its presentation, finalize tables and appendices, and strengthen the evidentiary treatment of the demonstration before publication.

## What Improved Since v1

### 1. Novelty is now more defensible.

The new Section 3.1, "Why Existing Validity Language Is Not Enough," directly addresses the strongest reviewer objection. The dynamic materials-boundary argument is persuasive:

- corpus, prompt, and model do not fully specify what the LLM sees;
- retrieval creates the information environment at runtime;
- therefore, researchers must validate the retrieval-created environment itself.

This makes retrieval-environment validity a useful audit-methodology construct rather than a relabeling exercise.

### 2. AJPT fit is clearer.

The paper now explicitly tells researchers and reviewers how to use the framework. The reviewer-facing sentence in the introduction and the Section 6.1 implications list make the paper more obviously methodological.

The strongest AJPT fit is:

> The paper provides criteria for designing, documenting, and reviewing LLM-based audit research when retrieval systems create the model's information environment.

### 3. Demonstration overclaiming risk is lower.

Moving aggregate coding to appendix/transparency-artifact status is the right choice. The demonstration now has a better headline:

> Retrieval condition labels do not reveal claim-level evidence use.

That is a methodological inference, not a model-performance claim.

### 4. XBRL boundary is now reviewer-safe.

The manuscript repeatedly states that XBRL is reported accounting information, not audit evidence. It distinguishes graph-valid from audit-valid correctness. This should reduce the risk that audit reviewers object to XBRL being treated as ground truth.

### 5. Prototype scope is clearer.

The abstract and introduction now state that the demonstration uses keyword/text and table-based XBRL relational retrieval. This reduces the risk that reviewers expect vector RAG, RDF/OWL triple stores, or GraphRAG performance evidence.

## Remaining Reviewer Concerns

### Concern 1. The manuscript still needs final table execution.

The current v2 draft uses table callouts and references `plan/41` for table content. This is fine for internal development, but a reviewer-facing manuscript must include final numbered tables and figures, or at least a complete table package in manuscript order.

Risk:

The paper may feel unfinished despite a strong argument.

Required action:

Create a final table-and-figure manuscript package with numbered tables, figure captions, and appendix placement. Table 9 should be clearly marked appendix-only unless expert coding is completed.

### Concern 2. The demonstration still lacks external audit-domain validation.

The manuscript now discloses this limitation well. Still, audit-valid and integrated correctness are central enough that some reviewers may ask for at least limited expert review.

Risk:

Reviewers may accept the framework but question whether the selected examples are coded credibly.

Required action:

Minimum acceptable path:

1. Keep all audit-valid and integrated scores labeled preliminary.
2. In the main text, interpret only source-traceability and evidence-use divergence, not audit performance.
3. Add an expert-review plan in the appendix.

Stronger path:

Obtain one audit-domain expert review of the five selected examples and report agreement/disagreement qualitatively.

### Concern 3. Literature positioning still needs citation-level integration.

The new literature-positioning table is useful, but the prose still reads somewhat compressed. It should more explicitly name how the paper differs from specific prior studies.

Risk:

Reviewers may agree with the framework but ask whether the novelty relative to existing XBRL, textual analysis, LLM, and audit analytics literature is sufficiently demonstrated.

Required action:

In Section 2, add one or two sharper sentences per literature stream. For example:

- XBRL studies use structured reporting data to construct measures; this paper studies XBRL as part of an LLM retrieval environment.
- Textual analysis studies validate text-based measures; this paper validates the dynamically retrieved text environment supplied to a generative model.
- LLM accounting studies evaluate outputs; this paper evaluates the retrieval-created evidence basis of those outputs.

### Concern 4. The current paper may still be slightly long on framework artifacts.

The tables are useful, but the manuscript risks feeling like a toolkit if all tables are placed in the main text.

Risk:

Checklist-vs-theory concern may return.

Required action:

Keep only the highest-contribution visuals in the main text:

1. Figure 1: framework.
2. Table 2: validity dimensions.
3. Table 3 or Table 4: retrieval typology or construct mapping.
4. Table 5: correctness layers.
5. Table 8: selected claim examples.

Move Table 6, Table 7, Table 9, Table 10, and implementation tables to appendix unless journal space permits.

### Concern 5. The contribution statement could be more memorable.

The paper currently lists three contributions clearly, but the core takeaway could be sharper.

Suggested one-sentence contribution:

> We show that in LLM-based audit research, retrieval is not merely a way to supply context; it is a research-design choice that creates the information environment from which audit-related inferences are drawn.

This sentence should appear in the introduction and conclusion.

### Concern 6. Minor polish issues remain.

Examples:

1. Reference entry typo: "M. A Vasarhelyi" should be "M. A. Vasarhelyi."
2. The draft should replace internal references to `plan/41` with manuscript-friendly wording.
3. The phrase "keyword/text" in the abstract could be simplified to "keyword-ranked text."
4. Table callouts should be converted to final numbered table references.
5. The appendix should not read like a project file index in the final manuscript; paths can be moved to a reproducibility package note.

## Accept-Level Assessment by Criterion

| Criterion | Assessment | Reviewer Judgment |
|---|---|---|
| Clear methodology contribution | Strong | Accept-level after polish |
| Distinct from prior literature | Good but needs citation-level sharpening | Minor to moderate revision |
| Audit-specific grounding | Strong | Accept-level |
| XBRL boundary | Strong | Accept-level |
| Demonstration rigor | Adequate for methodology illustration, not empirical evidence | Conditional |
| Expert reliability safeguards | Conceptually stated, not executed | Remaining weakness |
| Reproducibility package | Strong | Accept-level for methodology paper |
| Risk of sounding technical | Reduced but still present in appendix | Manageable |
| Risk of checklist paper | Moderate if too many tables stay in main text | Manageable with table triage |

## Would I Recommend Acceptance?

Not yet.

I would not reject the paper, and I would not view it as merely speculative. The v2 draft has a real methodological contribution. But an accept-style recommendation would require either:

1. a cleaner, submission-formatted manuscript with final tables and appendix; and
2. at least minimal expert validation or a more conservative treatment of all audit-valid scores.

Without those changes, I would recommend revise-and-resubmit.

## Minimum Revisions Needed Before Submission

1. Create a final manuscript table package in publication order.
2. Decide which tables remain in the main text and which move to appendix.
3. Replace internal development-file references with manuscript-appropriate appendix references.
4. Add a final appendix index organized by appendix title, not file path.
5. Correct reference-list typos and citation style.
6. Add a stronger one-sentence contribution statement in the introduction and conclusion.
7. Add a paragraph clarifying that selected examples support evidence-use divergence, while audit-valid scoring remains illustrative unless expert-reviewed.

## Strongest Submission Framing

The strongest version of the paper should be framed as:

> A methodological framework for designing and evaluating retrieval-created information environments in LLM-based audit research.

The paper should not be framed primarily as:

- XBRL ontology for audit;
- GraphRAG for audit;
- LLM audit agent design;
- performance comparison of text versus XBRL retrieval;
- benchmark of `gemma4:31b`.

## Reviewer-Facing Summary

The v2 manuscript is now credible as an AJPT methodology paper under revision. It makes a clear and timely contribution by treating retrieval as a research-design choice that shapes the LLM's information environment. The remaining work is to make the paper look finished, disciplined, and evidence-conscious. The most important unresolved issue is not the framework; the framework is strong enough. The unresolved issue is how much evidentiary weight the demonstration can carry without external audit-domain coding.

## Recommended Next Development Step

Proceed to Phase 10 preparation, but begin with a "pre-submission polish package" rather than a cover letter. The immediate next deliverable should be:

`plan/48_phase10_pre_submission_polish_plan.md`

That plan should specify:

1. final table/figure integration;
2. appendix index cleanup;
3. reference finalization;
4. expert-review decision;
5. manuscript wording cleanup;
6. reproducibility package check.
