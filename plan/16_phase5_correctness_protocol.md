# Phase 5 Correctness Protocol and Failure Modes

## Purpose

This file develops the evaluation protocol for LLM audit outputs under different retrieval designs.

The goal is to prevent researchers from treating LLM outputs as simply right or wrong. In LLM-based audit research, a claim can be supported by retrieved text, consistent with XBRL relation paths, and still not be professionally reasonable as audit reasoning.

## Central Claim

LLM audit outputs require claim-level, multi-layered correctness assessment because different retrieval designs support different forms of validity.

Core sentence:

> A claim can be text-supported and graph-valid but still audit-invalid if it overstates risk, ignores evidence limitations, or treats management-coded reported relationships as independent audit evidence.

## Reviewer Accept-Level Standard

For this protocol to support an accept-level methodological contribution, it must satisfy four conditions:

1. Researchers can apply the protocol consistently enough for another team to reproduce the coding logic.
2. Correctness scores are interpreted as evidence about retrieval-created information environments, not as universal LLM performance scores.
3. The protocol separates support from retrieved sources, consistency with XBRL relations, and professional audit reasonableness.
4. The protocol changes the inference a researcher would draw compared with a simple right/wrong or overall accuracy evaluation.

## Unit of Analysis: Claim

### Definition

A **claim** is a discrete assertion in an LLM output that can be evaluated for support, validity, or reasoning quality.

Claims may include:

- factual statements
- reported relationship statements
- risk statements
- assertion mapping statements
- explanation statements
- conclusion statements
- recommendations or procedure-like statements

### Claim Segmentation Rule

Researchers should split LLM outputs into the smallest meaningful audit-relevant claims.

Example output:

> Contract liabilities increased during the year, which indicates a cutoff risk in revenue recognition.

Possible claims:

1. Contract liabilities increased during the year.
2. The increase is relevant to revenue recognition.
3. The increase indicates cutoff risk.

Why segmentation matters:

- Claim 1 may be graph-valid.
- Claim 2 may be text-supported or graph-valid.
- Claim 3 may require audit-valid expert judgment and may only be partially supported.

### Claim Segmentation Decision Rules

To improve reproducibility, coders should apply the following rules:

1. Split compound sentences when different parts require different evidence.
2. Split descriptive claims from inferential claims.
3. Split risk cues from audit conclusions.
4. Split reported relationship claims from professional judgment claims.
5. Keep purely stylistic or introductory text uncoded unless it makes an audit-relevant assertion.
6. Preserve the original wording of each claim where possible.

Examples:

| Output Text | Claim Type | Segmentation Decision |
|---|---|---|
| "Revenue increased, and deferred revenue also increased." | Factual / reported relationship | Split into two factual claims if each maps to separate facts |
| "The increase in deferred revenue suggests cutoff risk." | Inference / risk cue | Split into fact claim and risk inference if fact is not separately stated |
| "This proves revenue is misstated." | Audit conclusion | Code as separate high-risk audit-valid claim |
| "The company has complex revenue recognition." | Interpretive summary | Code if linked to a stated audit construct; otherwise mark as broad/uncoded |

### Claim Segmentation Reliability

For hypothesis-testing studies, researchers should report:

- who segmented claims
- whether a second coder reviewed segmentation
- how segmentation disagreements were resolved
- whether coding was performed on final agreed claims

For descriptive demonstrations, researchers should provide enough examples for readers to understand the segmentation logic.

### Claim Importance and Materiality Tags

Not all claims should have the same inferential weight. Researchers should therefore tag each coded claim before evaluating correctness:

| Tag | Meaning | Example |
|---|---|---|
| Core construct claim | Directly tied to the study's audit construct | Revenue cutoff risk is elevated |
| Supporting factual claim | Provides factual or reported-accounting support | Contract liabilities increased |
| Context claim | Provides background but is not central to the construct | The company operates subscription contracts |
| Procedure-like claim | Suggests audit work or follow-up | Inspect subsequent cash receipts |

For the main analysis, researchers should report correctness separately for core construct claims and supporting claims. This prevents a retrieval design from appearing valid because it produces many correct background statements while failing on the audit construct of interest.

Materiality tags should not be used to convert the protocol into an audit opinion model. They are used only to clarify which LLM claims matter most for the research inference.

## Four Correctness Layers

| Layer | Coding Question | Primary Evidence Source | Main Risk |
|---|---|---|---|
| Text-supported correctness | Is the claim supported by retrieved disclosure text? | Text chunks, footnotes, MD&A, policies | Narrative overreach |
| Graph-valid correctness | Does the claim match retrieved XBRL facts or relation paths? | XBRL concepts, facts, dimensions, calculation/presentation paths | Relation hallucination |
| Audit-valid correctness | Is the claim professionally reasonable as audit reasoning? | Expert auditor judgment | Source overreach |
| Integrated correctness | Are text, graph, and audit logic mutually consistent? | Combined review | Integration failure |

## Handling Contradictory or Missing Evidence

Correctness coding should account for both supporting and contradicting evidence.

Researchers should distinguish:

- **supported**: retrieved evidence directly supports the claim
- **unsupported**: retrieved evidence does not support the claim
- **contradicted**: retrieved evidence conflicts with the claim
- **not assessable**: available retrieval logs are insufficient to evaluate the claim

Contradicted claims should normally receive `0` for the relevant layer. Not assessable claims should be reported separately rather than silently treated as incorrect. This distinction matters because a not assessable claim may reflect weak traceability, whereas a contradicted claim reflects a stronger correctness failure.

## Layer 1: Text-Supported Correctness

### Definition

Text-supported correctness evaluates whether a claim is supported by retrieved narrative disclosure text.

### Coding Scale

| Score | Meaning |
|---|---|
| 1 | The claim is directly supported by retrieved text. |
| 0.5 | The claim is partially supported, inferential, or missing important caveats. |
| 0 | The claim is unsupported or contradicted by retrieved text. |

### Examples

- `1`: Retrieved revenue policy states that revenue is recognized over time; LLM claims revenue is recognized over time.
- `0.5`: Retrieved text discusses contract liabilities; LLM infers cutoff risk without explicit textual support.
- `0`: Retrieved text discusses subscription revenue; LLM claims product revenue drives the increase without support.

### Minimum Reporting

- retrieved text chunk ID
- filing section
- claim-to-text mapping
- coding rationale for partial support

## Layer 2: Graph-Valid Correctness

### Definition

Graph-valid correctness evaluates whether a claim is consistent with retrieved XBRL facts or relation paths.

### Coding Scale

| Score | Meaning |
|---|---|
| 1 | The claim matches retrieved XBRL facts or typed relation paths. |
| 0.5 | The claim is directionally consistent but incomplete, imprecise, or missing context. |
| 0 | The claim invents, misstates, or contradicts XBRL facts or relation paths. |

### Examples

- `1`: XBRL facts show contract liabilities increased; LLM claims contract liabilities increased.
- `0.5`: XBRL shows increase in current contract liabilities only; LLM claims total contract liabilities increased.
- `0`: No XBRL relation links inventory reserve to revenue; LLM claims such a relation exists.

### Graph-Valid Spot-Check Procedure

Researchers should not rely entirely on automated graph extraction. At minimum:

- spot-check a sample of relation paths against the original filing or taxonomy
- verify concept IDs and labels
- verify calculation or presentation relation types
- verify periods, units, and dimensions
- verify company extension concept handling
- document extraction errors or ambiguous paths

### Minimum Reporting

- concept IDs
- fact values and periods when relevant
- relation path IDs or relation descriptions
- relation type labels
- taxonomy version
- parser or extraction method
- spot-check procedure

## Layer 3: Audit-Valid Correctness

### Definition

Audit-valid correctness evaluates whether a claim is professionally reasonable as audit reasoning.

It is expert-coded judgment, not objective ground truth.

### Coding Scale

| Score | Meaning |
|---|---|
| 1 | Professionally reasonable, linked to relevant assertion or risk, and appropriately qualified. |
| 0.5 | Plausible but incomplete, overgeneralized, insufficiently qualified, or missing important evidence limitations. |
| 0 | Unsupported, misleading, professionally unreasonable, or treats management-coded information as independent audit evidence. |

### Examples

- `1`: LLM identifies that a large increase in contract liabilities may be a revenue recognition risk cue and qualifies that further audit evidence is needed.
- `0.5`: LLM states that increased contract liabilities indicate cutoff risk but does not qualify the claim or discuss alternative explanations.
- `0`: LLM concludes that revenue is misstated solely because contract liabilities changed.

### Expert Coding Requirements

For hypothesis-testing studies:

- at least two independent expert coders
- coder expertise disclosed
- coding guide provided
- training or calibration round documented
- inter-rater agreement reported
- disagreement resolution procedure described
- coding uncertainty disclosed

For descriptive methodological demonstrations:

- at least one primary coder and one reviewer, if feasible
- coded examples for each score
- transparent rationale for disputed or partial scores

### Coder Blinding and Bias Controls

Researchers should blind coders where feasible:

- Audit-valid coders should evaluate claim reasonableness without knowing whether the claim came from text retrieval, XBRL retrieval, hybrid retrieval, or an LLM-only condition.
- Text-supported coders may need access to retrieved text, but should not need to know the experimental hypothesis.
- Graph-valid coders may need access to XBRL paths, but should not need to know whether the authors expect XBRL retrieval to perform better.
- Failure-mode coding can be performed after layer-level correctness coding to avoid contaminating initial correctness judgments.

When blinding is infeasible, the manuscript should disclose why and explain how coding bias was mitigated.

### Audit-Valid Rubric Criteria

Coders should consider:

- assertion relevance
- risk logic
- evidence sufficiency caution
- source reliability caution
- absence of overclaiming
- consideration of alternative explanations
- distinction between risk cue and audit conclusion

## Layer 4: Integrated Correctness

### Definition

Integrated correctness evaluates whether text support, graph validity, and audit logic are mutually consistent.

Integrated correctness is not the average of text-supported, graph-valid, and audit-valid correctness. It is a separate judgment about whether the evidence layers are reconciled in the LLM's claim.

### Coding Scale

| Score | Meaning |
|---|---|
| 1 | Text, graph, and audit reasoning are mutually consistent and appropriately qualified. |
| 0.5 | Evidence layers are partially aligned but incomplete, ambiguous, or insufficiently reconciled. |
| 0 | Text, graph, and audit reasoning conflict or are not reconciled. |

### Examples

- `1`: Text disclosure and XBRL facts both support a qualified risk cue, and the LLM avoids treating the cue as a conclusion.
- `0.5`: Text and XBRL both mention contract liabilities, but the LLM does not reconcile timing or context differences.
- `0`: Text suggests one business driver, XBRL facts suggest another pattern, and the LLM ignores the conflict.

### Integrated Correctness Decision Rules

Coders should assign integrated correctness after the other three layers are coded.

Use these decision rules:

- Assign `1` when text, graph, and audit reasoning are aligned and the claim is appropriately qualified.
- Assign `0.5` when two layers support the claim but the third is missing, partial, ambiguous, or insufficiently reconciled.
- Assign `0` when layers conflict, when the claim ignores a material contradiction, or when the claim converts a risk cue into an unsupported audit conclusion.

Important:

> High graph-valid and text-supported scores do not automatically imply high integrated correctness.

### Minimum Reporting

- text-supported score
- graph-valid score
- audit-valid score
- explanation of whether evidence layers align or conflict

## Coding Workflow

Recommended workflow:

1. Preserve the full LLM output.
2. Segment the output into audit-relevant claims.
3. Assign claim IDs.
4. Map each claim to retrieved text chunks, XBRL paths, or unsupported status.
5. Code text-supported correctness.
6. Code graph-valid correctness.
7. Code audit-valid correctness.
8. Code integrated correctness.
9. Identify failure modes.
10. Resolve coder disagreements.
11. Report inter-rater agreement where applicable.

## Disagreement Resolution

For hypothesis-testing studies, disagreements should be resolved through a documented process:

1. Independent coders first assign scores.
2. Disagreements are identified at the claim-layer level.
3. Coders discuss disagreements using the coding guide.
4. If disagreement remains, a third expert adjudicator or pre-specified rule is used.
5. Both pre-resolution and final agreement statistics should be reported where feasible.

For descriptive demonstrations, the manuscript should at least disclose disputed claims and explain final coding decisions.

## Recommended Reliability Metrics

Researchers should report reliability metrics appropriate to the coding design:

- Cohen's kappa for two coders and categorical scores.
- Weighted kappa when treating `0`, `0.5`, and `1` as ordered categories.
- Krippendorff's alpha when there are more than two coders or missing ratings.
- Percent agreement may be reported as supplementary information but should not be the only reliability metric in hypothesis-testing studies.

## Scoring Interpretation and Aggregation

The `0`, `0.5`, and `1` scores should be treated as ordered diagnostic categories, not precise interval measures.

Recommended reporting:

- Report score distributions by retrieval condition and correctness layer.
- Report results separately for core construct claims and supporting factual claims.
- Avoid collapsing all layers into a single overall correctness score.
- If an aggregate measure is used, pre-specify it and explain what inference it supports.
- Report the number of not assessable claims separately.

Reviewer-facing rule:

> The paper should not claim that one retrieval design is "more accurate" unless it specifies which correctness layer, which claim type, and which audit construct the comparison concerns.

## Claim-Level Coding Template

| Claim ID | Claim Text | Retrieval Condition | Text Source ID | XBRL Path ID | Text-Supported | Graph-Valid | Audit-Valid | Integrated | Failure Mode | Notes |
|---|---|---|---|---|---:|---:|---:|---:|---|---|
| C1 | Contract liabilities increased during the year. | XBRL | N/A | P1 | 0 | 1 | 1 | 0.5 | None / partial integration | Graph-valid but no text support in this condition |
| C2 | The increase indicates cutoff risk. | Hybrid | T3 | P1 | 0.5 | 1 | 0.5 | 0.5 | Source overreach | Plausible cue, not conclusion |

## Illustrative Divergence Patterns

The demonstration should include at least one case where correctness layers diverge.

| Pattern | Interpretation |
|---|---|
| High text-supported, low graph-valid | Narrative support exists, but structured relation preservation is weak |
| Low text-supported, high graph-valid | Reported relation support exists, but narrative context is missing |
| High graph-valid, low audit-valid | Claim matches reported relationships but overstates audit implication |
| High text-supported and graph-valid, low integrated | Evidence layers exist but are not reconciled |
| High integrated, low separability | Hybrid condition may support integration but confounds text and relation effects |

## Failure Mode Taxonomy

| Failure Mode | Definition | Linked Validity Issue | Linked Correctness Layer | Example |
|---|---|---|---|---|
| Omission | Construct-relevant information is not retrieved | Selection validity | Text-supported / graph-valid | Revenue policy retrieved but contract liability relation omitted |
| Distortion | Retrieved information is rendered misleadingly | Representation validity | Graph-valid / integrated | Calculation path rendered as causal relation |
| Retrieval instability | Equivalent retrieval conditions produce materially different information | Stability | Any layer | Same task retrieves different relation paths across runs |
| Attribution failure | Output claim cannot be traced to retrieved information | Traceability | Text-supported / graph-valid | LLM asserts cutoff risk without text or XBRL support |
| Model-retrieval confounding | Output difference cannot be attributed to model or retrieval | Separability | Integrated | Hybrid performs better because it received more context |
| Relation hallucination | LLM invents a non-existing accounting relation | Graph-valid | Graph-valid | LLM claims inventory reserve is calculated from revenue |
| Source overreach | LLM treats management-coded reported information as independent audit evidence | Audit-valid | Audit-valid | LLM concludes no misstatement because XBRL relation exists |
| Integration failure | LLM fails to reconcile text and graph evidence | Integrated | Integrated | MD&A explanation and XBRL trend conflict but LLM ignores conflict |

## Full vs Light Protocol

| Protocol | Use Case | Components | Minimum Reviewer Expectation |
|---|---|---|---|
| Full protocol | Hypothesis-testing studies | Independent expert coding, graph validation, text support coding, inter-rater reliability | Required when making comparative performance or inference claims |
| Light protocol | Descriptive demonstration or large-scale screening | Sampled claim audit, automated graph validation, retrieval log inspection | Acceptable when claims are illustrative and bounded |

## How Correctness Layers Support Retrieval-Environment Validity

| Retrieval-Environment Validity Dimension | Correctness Evidence |
|---|---|
| Selection validity | Claims unsupported because relevant text or graph paths were not retrieved |
| Representation validity | Graph-validity failures caused by distorted relation representation |
| Stability | Correctness changes across repeated retrieval runs |
| Traceability | Claims lacking text source or XBRL path mapping |
| Separability | Correctness differences confounded by retrieval condition, token budget, or model effects |

## From Correctness Scores to Research Inference

The purpose of the protocol is not to produce a leaderboard. It is to discipline the inference drawn from LLM outputs.

| Observed Pattern | Naive Inference | Protocol-Based Inference |
|---|---|---|
| Hybrid retrieval has more correct factual claims | Hybrid retrieval is best | Hybrid may increase available context, but separability and core construct performance must be assessed |
| XBRL retrieval has high graph-valid scores | XBRL improves audit reasoning | XBRL preserves reported relationships; audit-valid correctness must be evaluated separately |
| Text retrieval has high text-supported scores | Text retrieval is sufficient | Text support may not preserve structured accounting relationships |
| LLM-only produces plausible audit language | LLM has audit expertise | Output may be professionally plausible but weakly traceable to retrieved evidence |
| Core construct claims fail while background claims pass | Overall accuracy is acceptable | Retrieval design does not support the intended audit construct |

## Inference Guidance

Correctness scores should not be interpreted as universal model performance. They indicate what type of support exists for claims under a retrieval-created information environment.

Examples:

- High text-supported correctness does not imply graph-valid correctness.
- High graph-valid correctness does not imply audit-valid correctness.
- High integrated correctness may still have low separability in hybrid retrieval.
- Low LLM-only traceability does not necessarily imply poor model reasoning; it indicates weak source attribution.

## Draft Manuscript Section

Evaluating LLM audit outputs requires more than classifying responses as right or wrong. Retrieval designs create different information environments, and those environments support different types of claims. We therefore propose a claim-level correctness protocol that distinguishes text-supported, graph-valid, audit-valid, and integrated correctness.

The unit of analysis is a claim, defined as a discrete assertion in an LLM output that can be evaluated for support, validity, or reasoning quality. A single LLM response may contain factual claims, reported relationship claims, risk claims, assertion mapping claims, explanations, and conclusions. These claims may differ in the type of support they receive. For example, a claim that contract liabilities increased may be graph-valid if it matches XBRL facts, while a claim that the increase indicates cutoff risk may require expert audit judgment and may be only partially audit-valid.

Text-supported correctness evaluates whether a claim is supported by retrieved disclosure text. Graph-valid correctness evaluates whether a claim matches retrieved XBRL facts or relation paths. Audit-valid correctness evaluates whether a claim is professionally reasonable as audit reasoning and should be treated as expert-coded judgment rather than objective ground truth. Integrated correctness evaluates whether text support, graph validity, and audit logic are mutually consistent.

This distinction is central to the paper's methodological contribution. A claim can be text-supported and graph-valid but still audit-invalid if it overstates risk, ignores evidence limitations, or treats management-coded reported relationships as independent audit evidence. Conversely, a claim may be professionally plausible but weakly traceable to retrieved information, limiting what the researcher can infer about retrieval-supported reasoning.

## Reviewer Stress Test

### Concern 1: The coding protocol is too subjective.

Response:

Audit-valid correctness is explicitly framed as expert-coded judgment rather than objective truth. The protocol requires coder expertise, coding guidance, inter-rater agreement, and disagreement resolution for hypothesis-testing studies.

### Concern 2: Four correctness layers are too complex.

Response:

The layers are necessary because retrieval designs support different kinds of inference. Text support, graph validity, audit validity, and integration can diverge. Collapsing them into one score would hide the paper's central methodological issue.

### Concern 3: Graph-valid correctness may depend on extraction errors.

Response:

The protocol requires graph-valid spot-checks against original filings or taxonomies, including concept IDs, relation types, periods, units, dimensions, and extension handling.

### Concern 4: Integrated correctness is vague.

Response:

Integrated correctness is coded only after text-supported, graph-valid, and audit-valid correctness are assessed. It is not an average of the other scores. It evaluates whether the evidence layers are mutually consistent, partially aligned, or conflicting in the specific claim.

### Concern 5: This looks like model benchmarking.

Response:

Correctness layers are not presented as universal model performance scores. They are diagnostic indicators of what kind of support exists for claims under a retrieval-created information environment.

### Concern 6: Claim segmentation may be subjective.

Response:

The protocol includes claim segmentation rules, examples, and reliability reporting. For hypothesis-testing studies, segmentation should be reviewed by a second coder and disagreements should be resolved before final correctness coding.

### Concern 7: Reliability metrics are underspecified.

Response:

The protocol recommends Cohen's kappa, weighted kappa, or Krippendorff's alpha depending on the coding design. Percent agreement may supplement but should not replace reliability metrics in hypothesis-testing studies.

### Concern 8: The scoring scale invites false precision.

Response:

The protocol treats `0`, `0.5`, and `1` as ordered diagnostic categories, not precise interval measures. The manuscript should report distributions by layer, retrieval condition, and claim type rather than relying on a single aggregate accuracy score.

### Concern 9: Correct background claims may hide failure on the audit construct.

Response:

The protocol requires claim importance tags and separate reporting for core construct claims. A retrieval design should not be judged valid merely because it supports many background or factual claims while failing on the construct-relevant audit inference.

### Concern 10: Coder expectations may bias audit-valid scoring.

Response:

The protocol recommends coder blinding where feasible. Audit-valid coders should not know the retrieval condition or the author's directional expectation. If blinding is not feasible, the manuscript should disclose the limitation and describe mitigation procedures.

### Concern 11: Unsupported and not assessable claims are conflated.

Response:

The protocol separates supported, unsupported, contradicted, and not assessable claims. Not assessable claims are reported separately because they indicate traceability limits rather than necessarily incorrect reasoning.

## Phase 5 Reviewer-Level Assessment

### Strengths

- The protocol makes clear why right/wrong scoring is insufficient.
- The unit of analysis is explicit.
- Audit-valid correctness is bounded as expert-coded judgment.
- Graph-valid correctness includes spot-check requirements.
- Failure modes are linked to validity dimensions and correctness layers.
- The protocol prepares the methodological demonstration for inference-shift analysis.
- Claim segmentation rules now improve reproducibility.
- Integrated correctness is clarified as a separate judgment rather than an average.
- Disagreement resolution and reliability metrics are specified.
- Claim importance tags prevent background factual accuracy from masking construct-level failure.
- Scoring interpretation rules reduce the risk of false precision.
- Coder blinding guidance strengthens the credibility of audit-valid correctness.
- The protocol now shows how correctness coding changes research inference, not just output evaluation.

### Remaining Weaknesses

- The final manuscript must provide concrete coded examples.
- Coding burden may be high; full and light protocols should be clearly distinguished.
- The demonstration must show at least one case where correctness layers diverge.
- The final manuscript should keep detailed reliability procedures concise, with extended protocol in an appendix.
- The final paper should avoid reporting a headline "accuracy" number unless it is clearly tied to a specific correctness layer and construct.
- The demonstration should include at least one core construct claim failure that would be hidden by aggregate scoring.

### Accept-Level Reviewer Verdict

Phase 5 is now strong enough to support a favorable reviewer assessment if the methodological demonstration delivers concrete coded examples. The protocol is no longer merely a checklist; it functions as a validity-preserving measurement method for LLM audit outputs.

An AJPT reviewer could reasonably view this section as publishable methodology because it:

- defines the evaluative unit of analysis
- separates source support from audit reasonableness
- provides reproducible coding rules
- guards against coder bias and false precision
- links correctness failures back to retrieval-environment validity
- clarifies how output evaluation changes research inference

The remaining accept risk is empirical illustration, not conceptual design. Without a convincing Phase 6 demonstration, Phase 5 may still read as a well-designed proposal. With concrete SEC/XBRL examples, it can become a usable audit research methodology.

## Phase 5 Deliverables

- Claim as unit of analysis: complete.
- Four correctness layers: complete.
- Coding rubrics: complete.
- Audit-valid coding guide: complete.
- Coder requirements and reliability checks: complete.
- Graph-valid spot-check procedures: complete.
- Failure mode taxonomy: complete.
- Linkage to retrieval-environment validity dimensions: complete.
- Draft correctness and failure modes section: complete.
- Claim importance and materiality tagging: complete.
- Scoring interpretation and aggregation guidance: complete.
- Coder blinding and bias-control guidance: complete.
- Reviewer accept-level assessment: complete.
