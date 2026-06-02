# Major Comment 2 Demonstration Validation Audit

Date: 2026-06-01

## Reviewer Comment Reviewed

Major Comment 2 argues that the demonstration does not yet validate the framework strongly enough on the paper's own terms because stability and separability are core dimensions, but the demonstration lacks matched-budget tests, evidence-order sensitivity, prompt variation, output-level reruns under retrieval perturbations, and multi-model evidence.

## Bottom-Line Assessment

The issue is now addressed through the conservative path, not through a Tier 2 empirical upgrade. The paper explicitly chooses a Tier 1 methodological protocol-validation / transparency path. It does not claim model-performance validation, retrieval-method superiority, or causal identification of retrieval-design effects.

The demonstration now supports:

- source-to-context-to-output-to-claim traceability;
- preservation of retrieval environments;
- claim-level source-use coding;
- independent reliability evidence for source-use and integration coding;
- context-volume transparency;
- retrieval-stage source-environment perturbation diagnostics;
- identification of where Tier 2 controls are needed.

It does not support:

- matched-budget output robustness;
- evidence-order robustness;
- prompt-sensitivity robustness;
- cross-model robustness;
- output-level reruns under retrieval perturbations;
- causal claims that observed claim patterns are caused solely by retrieval design.

## Actionable Fix Path Chosen

The reviewer offered two paths:

1. Reposition the paper as a conceptual/methodological essay with an illustrative transparency package and tone down empirical validation language.
2. Upgrade the demonstration with matched token budgets, evidence-order variation, prompt variation, and LLM reruns.

The revision takes Path 1.

## Evidence In The Revised Manuscript

| Reviewer Request | Current Manuscript Response | Status |
|---|---|---|
| Tone down empirical validation language | The manuscript repeatedly frames the demonstration as protocol-validation evidence, not model-performance evidence | Addressed |
| Make stability/separability limits explicit | Section VII states that context-volume and source-environment perturbation diagnostics make stability/separability concerns observable but do not resolve them | Addressed |
| Acknowledge no matched-budget tests | Section VII and Appendix I explicitly state that matched-budget sensitivity was not run | Addressed |
| Acknowledge no prompt-order or evidence-order tests | Section VII, Discussion, and Appendix I identify evidence-order and prompt sensitivity as Tier 2 requirements | Addressed |
| Acknowledge no output-level reruns | Appendix I states source perturbations were conducted without LLM reruns; Section VII states the diagnostic is not model-output robustness evidence | Addressed |
| Acknowledge no multi-model evidence | Discussion requires model variation for stronger studies; the current local model is treated as a controlled demonstration model | Addressed |
| Prevent causal overclaiming | Section VII now states that the positive result is protocol validation, not an identification claim that observed output patterns are caused solely by retrieval design | Addressed |

## Remaining Reviewer Risk

The likely follow-up concern is that a reviewer may still prefer Path 2. The response should not pretend that Path 2 was completed. The defense should be:

- AJPT methodological papers can make a methodological contribution through design criteria, examples, and reviewer-evaluable protocols.
- The paper's claim has been narrowed to protocol validation.
- The current diagnostics are sufficient for a Tier 1 methodology demonstration because they make the retrieval environment inspectable and show how to identify separability threats.
- The paper gives explicit Tier 2 requirements for studies making performance, superiority, or causal claims.

## Suggested Response-Letter Language

> We agree that the current demonstration does not provide matched-budget, evidence-order, prompt-sensitivity, cross-model, or output-level robustness evidence. We therefore revised the manuscript to take the first path suggested by the reviewer: a methodological protocol-validation and transparency package rather than a model-validation study. Section VII now states that the demonstration follows a Tier 1 transparency path, not a Tier 2 model-validation path. The context-volume and source-environment perturbation diagnostics make stability and separability concerns observable, but we do not claim that they resolve those concerns or identify causal effects of retrieval design. Appendix I specifies the Tier 2 design that would be required for stronger model-performance or retrieval-superiority claims, including matched-budget reruns, evidence-order variation, prompt sensitivity, model variation, broader sampling, and expert audit-domain coding.

## Recommendation For Next Submission

Treat this comment as addressed only if the response letter clearly acknowledges the limits. Do not claim:

- that the framework is empirically validated in a performance sense;
- that hybrid retrieval causes source-use divergence;
- that stability and separability were fully tested;
- that source-environment perturbations are output-level robustness checks.

Do claim:

- that the demonstration validates the protocol's inspectability and claim-level measurement workflow;
- that separability/stability threats are documented and made reviewer-evaluable;
- that stronger empirical claims require the Tier 2 design specified in Appendix I.

