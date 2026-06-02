# Major Comment 4 Design-Specific Counts Audit

Date: 2026-06-01

## Reviewer Comment Reviewed

Major Comment 4 argues that the manuscript sometimes draws broader inferences from highly design-specific counts, especially the result that 8 of 89 hybrid claims used both text and XBRL. The reviewer notes that this result is contingent on one model, one retrieval implementation, one prompt architecture, and a purposive sample of firms and constructs.

## Bottom-Line Assessment

The issue is substantially addressed. The revised manuscript repeatedly frames the hybrid counts as design-specific diagnostics rather than population frequencies, model-performance evidence, or evidence about how hybrid retrieval generally behaves.

The remaining risk was wording drift: a few phrases could still sound broader than intended. I tightened those phrases by adding "in this implementation," "specified hybrid condition," and "within this hybrid package" where the counts or examples could otherwise be read as general hybrid-retrieval behavior.

## Actionable Fix Status

| Reviewer Request | Current Revision Response | Status |
|---|---|---|
| Frame counts as design-specific mechanism evidence | Abstract, Section VII, Appendix F6, Appendix H, and supplement conclusion state that counts are design-specific diagnostics | Addressed |
| Avoid frequency-like or generalizable language | Added explicit language: not population frequencies, not prevalence, not general hybrid-retrieval effects | Addressed |
| Avoid implying hybrid retrieval generally behaves this way | Added wording that the result is not an identification claim and not evidence that hybrid retrieval generally behaves this way | Addressed |
| If stronger claims are desired, vary model/prompt/retrieval systematically | Discussion and Appendix I state that stronger studies require model variation, prompt sensitivity, retrieval variation, matched budgets, and output-level reruns | Addressed as future Tier 2 design, not completed evidence |

## Evidence In The Revised Manuscript

| Location | Current Protective Language |
|---|---|
| Abstract | "within this design" before the 8/89, 61/89, and 20/89 counts |
| Introduction | "We report these patterns as protocol-validation evidence rather than as performance rankings or population failure rates" |
| Section VII | "in this model, prompt, and context architecture" |
| Section VII | "These counts are design-specific diagnostics, not estimated population frequencies" |
| Section VII | "not an identification claim that observed output patterns are caused solely by retrieval design or that hybrid retrieval generally behaves this way" |
| Section VIII | "The bounded six-filer extension is a maximum-variation methodological extension, not a representative sample" |
| Appendix H | "not to estimate how frequently particular LLM behaviors occur in the population of SEC filers" |
| Supplement conclusion | Counts are "design-specific diagnostics, not estimated population frequencies" |

## Remaining Reviewer Risk

The likely follow-up concern is whether the abstract still gives too much prominence to the 8/89 result. It is currently defensible because the abstract says "within this design" and immediately frames the evidence as a nine-filer protocol-validation package. If reviewers remain sensitive, the response letter should emphasize that the count is used as a mechanism illustration: it motivates claim-level source-use coding and does not estimate a rate of hybrid integration.

## Response-Letter Position

Use careful language:

> We agree that the hybrid-claim counts are contingent on the model, prompt, retrieval implementation, filers, and constructs used in the demonstration. We therefore revised the manuscript to describe the counts as design-specific mechanism diagnostics. We do not interpret them as population frequencies, model-performance evidence, retrieval-method superiority, or evidence of how hybrid retrieval generally behaves. Their purpose is to show why researchers should code claim-level evidence use rather than infer integration from a response-level hybrid label.

## Reviewer-Facing Follow-Up Questions To Preempt

1. Are the 8/89, 61/89, and 20/89 counts generalizable?
   - No. They are design-specific diagnostics from one model, prompt architecture, retrieval implementation, and purposive nine-filer package.

2. What do the counts support?
   - They support the methodological claim that response-level condition labels can hide claim-level source-use heterogeneity.

3. What do the counts not support?
   - They do not support population prevalence, retrieval superiority, model-performance effects, or claims about how hybrid retrieval generally behaves.

4. What would be required for stronger claims?
   - A Tier 2 design with systematic variation in model, prompt, retrieval settings, matched token budgets, evidence ordering, output-level reruns, and expert coding where audit-judgment claims are made.

## Implementation Log

- Tightened the introduction by specifying that one-layer use occurred "in this implementation."
- Tightened Section VII by stating that the result does not show that hybrid retrieval generally behaves this way.
- Tightened selected supplement examples by describing one-layer hybrid examples as occurring "within this hybrid package."
