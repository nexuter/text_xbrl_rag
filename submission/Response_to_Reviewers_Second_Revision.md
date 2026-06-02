# Response to Reviewers

[Submission date]

Professor Michael S. Wilkins  
Senior Editor  
Auditing: A Journal of Practice & Theory

Dear Professor Wilkins and Reviewers:

Thank you for the careful and constructive second-round feedback on our manuscript, "Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval." The comments helped us sharpen the paper's contribution, narrow claims that exceeded the evidence, and make the demonstration more reviewer-evaluable.

The revision now frames the manuscript as a Tier 1 AJPT methodology paper about retrieval as research design in LLM-based audit research. We sharpen retrieval-environment validity as an audit-specific diagnostic lens for retrieval-related construct drift, expand and clarify the nine-filer protocol-validation package, report independent coding and disagreement-pattern evidence, add bounded retrieval-stage sensitivity diagnostics, and define audit task success in assertion-relevant public-reporting terms rather than as audit-valid engagement reasoning.

The revised framework gives reviewers a reusable decision rule for evaluating when retrieval-stage artifacts are sufficient for a Tier 1 methodology claim and when stronger Tier 2 evidence is required before interpreting model performance, retrieval superiority, or audit-judgment quality.

We also narrowed the manuscript in several important ways. We do not claim that the selected LLM is validated for audit tasks, that hybrid retrieval is superior, that XBRL improves audit reasoning, that the 8-of-89 hybrid-claim count generalizes, or that public filing/XBRL materials establish audit evidence sufficiency. The revised paper validates a retrieval-environment protocol and central source-use/integration measures; it does not validate model performance or audit-judgment quality.

Below we summarize the major changes and then respond to the major and minor comments.

## Summary of Major Revisions

1. We sharpened the contribution by positioning retrieval-environment validity as an audit-specific organizing framework and reviewer decision rule for retrieval-related construct drift, not as a new universal validity theory.
2. We reframed the demonstration as a nine-filer, 72-output, 281-claim protocol-validation package rather than a model-performance study.
3. We added independent coding evidence for a 120-claim sample, including all 89 hybrid claims and 31 non-hybrid anchors, and now report disagreement patterns rather than only agreement statistics.
4. We tightened audit construct definitions and task-success criteria for revenue recognition risk cues and inventory valuation assertion relevance in a public-reporting setting.
5. We added bounded retrieval-stage diagnostics, including context-volume diagnostics and source-environment perturbations, while explicitly stating that these are not output-level robustness tests.
6. We added non-accounting RAG and evidence-traceability positioning, a reader-facing retrieval mechanics example, and a compact early correctness-layer figure.

## Major Comment 1: Contribution and Boundary Against Existing Validity Concepts

**Reviewer concern.** The manuscript needed a sharper contribution claim and a clearer boundary against existing construct validity, measurement validity, documentation, reproducibility, and RAG-evaluation ideas.

**Response.** We agree. We revised the paper to clarify that retrieval-environment validity is grounded in construct validity but targets a retrieval-specific failure mode: the information environment observed by the LLM is dynamically created by the retrieval pipeline at runtime. The revised manuscript no longer presents the term as a standalone validity theory. Instead, it presents it as an audit-specific diagnostic lens and reviewer decision rule for retrieval-related construct drift.

**Revisions made.**

- The Introduction now states that retrieval-environment validity does not replace construct validity and is not a general theory of RAG evaluation.
- Section III defines the concept as a retrieval-specific diagnostic lens for construct drift.
- Table 2 compares retrieval-environment validity with construct validity, measurement validity, information-set design, audit evidence sufficiency, audit documentation, textual-analysis preprocessing, XBRL data quality, RAG evaluation, evidence traceability, and reproducibility.
- Table 3 provides reviewer decision rules for retrieval-environment validity problems.
- Section II now engages non-accounting RAG evaluation and evidence-traceability research more directly.

**Residual boundary.** We do not claim that retrieval-environment validity replaces existing validity concepts. The contribution is a reviewer-evaluable audit-methodology framework for cases where retrieval dynamically constructs the model's information set.

## Major Comment 2: Demonstration Validation

**Reviewer concern.** The demonstration did not yet validate the framework strongly enough because stability and separability were core dimensions, yet the paper lacked matched-budget reruns, evidence-order sensitivity, prompt variation, output-level reruns under retrieval perturbations, and multi-model evidence.

**Response.** We agree that the original wording could imply stronger validation than the design supports. We therefore chose the conceptual/methodological path suggested by the reviewer: the revised manuscript is explicit that the demonstration is Tier 1 protocol validation, not Tier 2 model-performance validation.

**Revisions made.**

- Section VII now states that the demonstration provides protocol-validation evidence rather than model-performance evidence.
- Section VII and Appendix I report context-volume diagnostics and deterministic source-environment perturbation diagnostics.
- The sensitivity diagnostics make separability and stability concerns observable at the retrieval stage, but the manuscript explicitly states that they are not output-level robustness tests.
- Appendix I specifies the Tier 2 design required for stronger claims, including matched token budgets, evidence-order variation, prompt sensitivity, retrieval-parameter variation, model variation, output-level reruns, broader sampling, and expert coding where audit-judgment claims are made.

**Residual boundary.** The revised paper does not claim matched-budget output robustness, cross-model robustness, prompt-order robustness, or causal identification of retrieval-design effects.

## Major Comment 3: Coding Independence

**Reviewer concern.** The coding-based evidence was not sufficiently independent, and the manuscript needed disagreement patterns rather than only agreement statistics. The reviewer also noted that audit-valid correctness was not independently validated by audit-domain experts.

**Response.** We agree that coding credibility is central to the paper. We expanded and clarified the independent coding evidence for the central source-use and integration variables, and we narrowed audit-boundary notes so they are not treated as expert audit-valid labels.

**Revisions made.**

- Section VII and Appendix F now report a 120-claim independent coding sample, including all 89 hybrid-condition claims and 31 non-hybrid anchors.
- Coders received blank coding fields, coder instructions, a protocol, a codebook, and a claim evidence packet.
- Section VII now reports disagreement patterns in addition to agreement statistics.
- Appendix F reports that the disagreement file contains 22 variable-level disagreements: 3 claim-kind disagreements, 3 text-supported correctness disagreements, 1 graph-valid correctness disagreement, and 15 confidence-code disagreements.
- The substantive disagreements are concentrated in three accounting-policy claims where coders differed on whether the statement was factual or risk/assertion-oriented.
- Evidence-use type and integrated correctness have 100.0 percent agreement.
- Appendix F clarifies that qualitative audit-boundary notes are retained as transparency notes, not as expert audit-valid labels or reliability-tested audit-judgment outcomes.

**Residual boundary.** The independent coding evidence supports source-use and integration reliability. It does not independently validate audit-boundary judgments as audit-valid outcomes. Stronger audit-judgment claims would require audit-domain expert coding and reliability evidence targeted to those claims.

## Major Comment 4: Design-Specific Counts

**Reviewer concern.** The 8-of-89 hybrid-claim result is interesting but design-specific. The manuscript needed to avoid treating it as broader evidence about how hybrid retrieval generally behaves.

**Response.** We agree. We revised the manuscript to frame the hybrid counts as design-specific mechanism diagnostics from one model, one prompt architecture, one retrieval implementation, and a purposive nine-filer package.

**Revisions made.**

- The Abstract now says the hybrid-claim counts are "within this design."
- Section VII states that the counts arise "in this model, prompt, and context architecture."
- Section VII states that these counts are design-specific diagnostics, not estimated population frequencies.
- Section VII now explicitly states that the result is not evidence that hybrid retrieval generally behaves this way.
- Appendix H clarifies that the nine-filer package is purposive and layered, not representative of SEC filers.

**Residual boundary.** We do not interpret the 8-of-89 count as a rate estimate, failure prevalence estimate, retrieval-superiority result, model-performance result, or general statement about hybrid retrieval.

## Major Comment 5: Audit Construct and Audit Positioning

**Reviewer concern.** The audit constructs were not tight enough, and the paper's audit positioning sometimes exceeded what public filing text and management-reported XBRL data can support.

**Response.** We agree that public filing text and management-reported XBRL cannot support audit conclusions. We therefore tightened the ex ante construct definitions and revised task-success criteria to focus on source-traceable, assertion-relevant reasoning from public reporting data.

**Revisions made.**

- Section IV defines the current task success criteria for revenue recognition risk cues and inventory valuation assertion relevance.
- Appendix A adds task-success criteria for both constructs.
- Table 6 now labels the demonstration constructs as public-reporting risk-cue and assertion-relevance settings.
- Section V separates public-filing support, XBRL graph/reporting support, assertion relevance, audit-boundary diagnostics, and audit evidence sufficiency.
- Section VIII states that the current package is an audit-research methodology demonstration using public reporting inputs, not an audit-practice evidence environment.
- Section VIII also identifies what an engagement-like extension would require, including standards passages, internal-control narratives, auditor workpaper excerpts, confirmations, reperformance evidence, expert-reviewed case materials, expert coding, and reliability evidence.

**Residual boundary.** The demonstration is audit-specific because its construct definitions, assertion mappings, evidence hierarchy, and overreach boundaries are drawn from audit research and auditing standards. It is not an audit-practice validation study and does not establish audit evidence sufficiency.

## Minor Comments

**Minor Comment 1: Boundary statements were repetitive.**  
We tightened several statements and moved some boundary logic into tables and appendix materials. We retained some repetition intentionally because the major comments focused on overclaiming, public-filing/XBRL evidence boundaries, model-performance inference, and design-specific counts.

**Minor Comment 2: Literature review should engage non-accounting retrieval evaluation and evidence traceability.**  
Section II now includes a RAG Evaluation and Evidence Traceability subsection. It discusses RAG architecture, context relevance, answer faithfulness, answer relevance, attribution, and citation grounding, and explains why those concepts are necessary but not sufficient for audit-research inference.

**Minor Comment 3: Retrieval-environment validity may be seen as a subtype of construct validity.**  
We now state directly that retrieval-environment validity is grounded in construct validity and is best understood as a retrieval-specific diagnostic lens for construct drift, not a replacement for construct validity.

**Minor Comment 4: A compact visual example would help readers understand the correctness layers.**  
We added Figure 1A near the beginning of the paper. The figure uses an inventory reserve example to show the distinction among text-supported correctness, graph-valid correctness, assertion relevance/audit-boundary diagnostics, integrated correctness, and audit evidence sufficiency.

**Minor Comment 5: The nine-filer extension needed a cleaner statement of what is learned beyond applicability.**  
Section VII now states that the extension supports three methodological points: protocol maintenance across varied reporting environments, continued visibility of claim-level source-use heterogeneity, and boundary-condition detection such as large XBRL environments and relation-path scarcity.

**Minor Comment 6: Avoid wording that sounds like model-performance benchmarking.**  
We revised the manuscript to repeatedly frame the demonstration as Tier 1 protocol validation, not model-performance benchmarking, retrieval-method superiority testing, or failure-prevalence estimation.

**Minor Comment 7: AJPT readers need a short retrieval mechanics example.**  
Section IV now includes a mechanics example showing how top-k, chunking, relation-path omission, traversal/filtering choices, source order, token budget, and relation rendering alter the model's effective information set.

## Closing

Taken together, these revisions narrow the manuscript where the evidence is bounded and strengthen it where the methodological contribution is central. The revised paper does not ask the demonstration to prove model performance or audit-judgment quality. Instead, it provides a reviewer-evaluable framework, evidence hierarchy, retrieval diagnostics, independent source-use coding evidence, and reproducibility package that audit researchers can use to design, diagnose, and report retrieval-based LLM studies.

We appreciate the reviewers' guidance and believe the revised manuscript is now clearer, more disciplined, and better aligned with AJPT's methodological-paper objectives.

Sincerely,

[Corresponding author name]  
[On behalf of all authors]
