# Phase 3 Methodological Framework

## Purpose

This file develops the paper's central methodological framework:

> Retrieval-environment validity in LLM-based audit research.

The goal of Phase 3 is to make the concept rigorous, audit-specific, and reviewer-safe. The framework must read as a diagnostic lens for construct validity, not as a new validity theory or a technical RAG framework.

## Central Research Question

How does retrieval design affect the validity of inferences drawn from LLM-based audit research?

## Core Framework Claim

In retrieval-augmented LLM audit studies, retrieval design is part of the research design because the retriever dynamically constructs the information environment observed by the model. This dynamic retrieval layer creates retrieval-specific threats to construct validity. Researchers therefore need a diagnostic lens for assessing whether the retrieval-created information environment aligns with the audit construct the study claims to examine.

## Accept-Level Framework Contribution

At an accept-level standard, the framework must do more than define terms. It must change how reviewers and researchers evaluate LLM-based audit studies.

The framework's accept-level contribution is:

> It identifies retrieval-created information environments as a distinct locus of construct validity risk and gives audit researchers a structured way to diagnose whether LLM outputs support the inference the study claims to make.

This contribution is strongest when stated as a shift in evaluation:

| Common evaluation question | Framework-based evaluation question |
|---|---|
| Did the LLM answer correctly? | What information environment produced the answer, and does that environment align with the intended audit construct? |
| Which retrieval design performs best? | Which retrieval design supports the construct being studied, and what inferential limits does it introduce? |
| Did XBRL improve reasoning? | Did XBRL-based retrieval improve graph-validity without creating source overreach or reducing audit-validity? |
| Did hybrid retrieval improve accuracy? | Did hybrid retrieval improve integrated correctness while reducing separability? |

## Definition

**Retrieval-environment validity** is the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study.

## What Counts as an Audit Construct?

For this paper, an **audit construct** is the specific audit-relevant capability, judgment, or reasoning object that the researcher claims to study through LLM outputs.

Examples include:

- narrative disclosure comprehension
- reported accounting relation preservation
- narrative-numeric integration
- assertion mapping
- risk cue identification
- calculation consistency reasoning
- evidence traceability

This definition is intentionally research-design oriented. It does not imply that the LLM is performing an audit procedure or that retrieved information constitutes audit evidence.

Reviewer-safe sentence:

> The framework does not evaluate whether an LLM performs an audit procedure; it evaluates whether the retrieval-created information environment supports the audit-relevant construct the researcher claims to study.

## Clarification

Retrieval-environment validity is not a replacement for construct validity. It is a retrieval-specific diagnostic lens for construct validity in LLM-based audit research.

The concept asks:

> Did the retrieval system construct an information environment that allows the researcher to make the intended inference from the LLM output?

## Why Dynamic Retrieval Creates a Distinct Methodological Problem

Traditional audit experiments often define the information set before the experiment. The researcher typically knows what information participants receive and can evaluate whether the treatment materials align with the construct of interest.

In retrieval-augmented LLM studies, the information environment is often produced at runtime. A retriever may:

- select sources
- rank sources
- traverse relations
- summarize or transform retrieved information
- omit relevant information
- add irrelevant information
- change retrieved output across runs
- make it difficult to separate retrieval quality from model capability

This creates a methodological problem:

> Differences in LLM output may reflect retrieval-created information environments rather than model reasoning or the intended experimental manipulation.

## Fixed Information Set vs Dynamic Retrieval Environment

| Traditional audit study information design | Retrieval-augmented LLM audit study |
|---|---|
| Researcher defines the information set before the study. | Retriever selects information at runtime. |
| Treatment materials are usually stable across participants or conditions. | Retrieved information may vary by query, index, ranking rule, traversal depth, model, or prompt. |
| Information content is directly inspectable before the study. | Information content may be selected, transformed, summarized, omitted, or reordered by the retrieval pipeline. |
| Output differences are interpreted in relation to participant judgment or treatment manipulation. | Output differences may reflect model behavior, retrieval quality, or model-retrieval interaction. |
| Documentation focuses on experimental materials. | Documentation must include retrieval source, unit, operator, logs, relation paths, and prompt context. |

## Framework Figure Draft

Textual figure for manuscript drafting:

```text
Intended Audit Construct
        |
        v
Retrieval Design Choice
  - no retrieval
  - text-based contextual retrieval
  - XBRL-based relational retrieval
  - hybrid retrieval
        |
        v
Retrieval-Created Information Environment
  - selected sources
  - represented context
  - relation paths
  - token budget
  - source traceability
        |
        v
LLM Output
  - claims
  - explanations
  - risk assessments
  - assertion mappings
        |
        v
Inference About Audit Construct
        |
        v
Retrieval-Environment Validity Assessment
  - selection validity
  - representation validity
  - stability
  - traceability
  - separability
```

Caption draft:

> Figure 1 illustrates retrieval-environment validity as a diagnostic lens between retrieval design and inference from LLM outputs. The framework emphasizes that researchers do not observe model reasoning directly; they observe LLM outputs generated from retrieval-created information environments.

## Core Propositions for the Manuscript

These propositions can be used to structure the framework section without making causal claims stronger than the paper can support.

### Proposition 1: Retrieval design shapes inferential validity.

In retrieval-augmented LLM audit studies, retrieval design shapes what researchers can validly infer from model outputs because it dynamically constructs the information environment observed by the model.

### Proposition 2: Construct-retrieval alignment is necessary for valid interpretation.

A retrieval design supports valid interpretation only to the extent that the retrieved information environment aligns with the audit construct the study claims to examine.

### Proposition 3: Retrieval-created information environments require multi-dimensional assessment.

No single metric is sufficient to evaluate retrieval-environment validity. Researchers should assess selection, representation, stability, traceability, and separability.

### Proposition 4: Better output quality does not imply better construct validity.

An LLM output may appear more accurate, detailed, or persuasive while still being weakly aligned with the intended audit construct if the retrieval environment omits relevant information, distorts retrieved information, lacks traceability, or confounds model and retrieval effects.

### Proposition 5: Retrieval design can change the appropriate inference without changing the observed output.

The same LLM output may support different research inferences depending on whether it is text-supported, graph-valid, audit-valid, and traceable to the retrieval-created information environment.

## Five Dimensions of Retrieval-Environment Validity

| Dimension | Definition | Audit/Method Anchor | Core Question | Failure Mode |
|---|---|---|---|---|
| Selection validity | The extent to which retrieval selects information relevant to the intended audit construct | Relevance | Did retrieval select construct-relevant information? | Omission |
| Representation validity | The extent to which retrieved information is faithfully represented to the LLM | Reliability / faithful representation | Was retrieved information accurately represented? | Distortion |
| Stability | The extent to which retrieval produces consistent information environments across equivalent runs | Reproducibility | Is retrieval stable under equivalent conditions? | Retrieval instability |
| Traceability | The extent to which LLM output claims can be linked to retrieved information | Documentation / support | Can claims be traced to retrieved sources or relation paths? | Attribution failure |
| Separability | The extent to which retrieval effects can be separated from model effects | Internal validity | Can researchers distinguish model behavior from retrieval-created environment effects? | Model-retrieval confounding |

## Dimension Boundaries

The five dimensions are related but distinct. The manuscript should define the boundary of each dimension clearly to avoid appearing ad hoc or overlapping.

| Dimension | What It Asks | What It Does Not Ask |
|---|---|---|
| Selection validity | Was the right kind of information retrieved for the construct? | Whether the retrieved information was accurately represented |
| Representation validity | Was retrieved information rendered faithfully to the LLM? | Whether enough relevant information was selected |
| Stability | Would equivalent retrieval settings produce similar information environments? | Whether retrieved information is relevant or correct |
| Traceability | Can output claims be linked back to retrieved information? | Whether those claims are professionally reasonable |
| Separability | Can retrieval effects be distinguished from model effects? | Whether any one retrieval design is superior |

Reviewer-safe sentence:

> Selection concerns what enters the information environment; representation concerns how it is rendered; stability concerns whether it is reproducible; traceability concerns whether output claims can be linked to it; separability concerns whether its effects can be isolated from model behavior.

## Dimension 1: Selection Validity

### Definition

Selection validity is the extent to which the retrieval system selects information relevant to the intended audit construct.

### Audit/Method Anchor

Relevance.

### Reviewer-Facing Explanation

If the intended construct is narrative comprehension, selecting relevant disclosure text may be appropriate. If the intended construct is reported accounting relation preservation, selecting only semantically similar text chunks may underrepresent the construct.

### Observable Indicators

- retrieved source types
- retrieval unit
- retrieval operator
- top-k results
- traversal depth
- omitted construct-relevant sources
- mismatch between intended construct and retrieved information

### Example

For a revenue recognition risk task, text retrieval may retrieve revenue policy disclosures but omit XBRL relations involving contract liabilities, contract assets, and deferred revenue. The LLM may produce a rich narrative answer while lacking the reported relationship information needed to evaluate relation preservation.

### Reviewer Question

> Did the retrieval system retrieve the information needed to study the stated audit construct?

### Minimal Assessment

At minimum, authors should report the intended construct, retrieval source, retrieval unit, retrieval operator, and a short rationale for why the retrieved information type is relevant to the construct.

## Dimension 2: Representation Validity

### Definition

Representation validity is the extent to which retrieved information is accurately and faithfully represented to the LLM.

### Audit/Method Anchor

Reliability and faithful representation.

### Reviewer-Facing Explanation

Even if the correct information is retrieved, it may be represented in a way that distorts its meaning. For example, an XBRL calculation relation may be rendered as an economic causal relation, or a presentation hierarchy may be interpreted as evidence of audit risk.

### Observable Indicators

- natural language rendering of graph paths
- preservation of typed relations
- source identifiers
- distinction between calculation, presentation, definition, and dimensional relations
- clear labeling of management-coded reported relationships

### Example

An XBRL calculation path showing that gross profit is calculated from revenue and cost of revenue should not be represented as evidence that cost of revenue caused a change in revenue.

### Reviewer Question

> Did the retrieval pipeline preserve the meaning and limits of the retrieved information?

### Minimal Assessment

At minimum, authors should provide examples of how retrieved information is represented in the prompt or context window, including source identifiers and relation labels when structured data are used.

## Dimension 3: Stability

### Definition

Stability is the extent to which equivalent retrieval requests produce consistent information environments.

### Audit/Method Anchor

Reproducibility.

### Reviewer-Facing Explanation

If retrieval outputs change materially across equivalent runs, researchers may not be able to reproduce or interpret LLM output differences. Instability can arise from stochastic retrieval, changing indexes, model-generated queries, API changes, prompt variations, or graph traversal settings.

### Observable Indicators

- repeated retrieval outputs
- retrieval overlap rates
- ranked result stability
- graph path stability
- prompt sensitivity
- index version
- taxonomy version

### Example

Two equivalent prompts for inventory valuation may retrieve different inventory reserve disclosures and different XBRL relation paths, producing different LLM risk assessments.

### Reviewer Question

> Would the same study produce materially similar retrieved information under equivalent retrieval conditions?

### Minimal Assessment

At minimum, authors should repeat retrieval for a subset of prompts or tasks and report whether retrieved sources or relation paths materially change.

## Dimension 4: Traceability

### Definition

Traceability is the extent to which LLM output claims can be traced to retrieved information.

### Audit/Method Anchor

Documentation and support.

### Reviewer-Facing Explanation

Traceability does not mean that retrieved information is audit evidence. It means the researcher can identify whether an output claim is supported by retrieved text, XBRL relation paths, or neither.

### Observable Indicators

- retrieval logs
- source identifiers
- text chunk citations
- XBRL concept IDs
- relation path IDs
- claim-to-source mapping
- unsupported claim rate

### Example

If an LLM states that "contract liabilities increased, indicating cutoff risk," the researcher should be able to trace the claim to specific text disclosures, XBRL facts, and relation paths. If no such sources exist, the claim may reflect model inference or hallucination rather than retrieved information.

### Reviewer Question

> Can researchers trace each material LLM claim to retrieved information?

### Minimal Assessment

At minimum, authors should map a sample of material output claims to retrieved text chunks, XBRL relation paths, or unsupported/model-generated claims.

## Dimension 5: Separability

### Definition

Separability is the extent to which researchers can distinguish model behavior from retrieval-created information environment effects.

### Audit/Method Anchor

Internal validity.

### Reviewer-Facing Explanation

In LLM-RAG studies, performance differences can arise from model ability, retrieval quality, retrieval volume, source type, token budget, or prompt design. Without separability, researchers may over-attribute output differences to the model.

### Observable Indicators

- LLM-only baseline
- text retrieval condition
- XBRL retrieval condition
- hybrid condition
- token budget controls
- top-k or traversal-depth sensitivity
- prompt sensitivity
- model variation

### Example

Hybrid retrieval may yield higher integrated correctness because it gives the model both narrative context and relation paths. However, researchers cannot infer that hybrid retrieval produces better audit reasoning unless they account for lower separability and larger information volume.

### Reviewer Question

> Can the study distinguish whether observed output differences arise from the model, the retrieval environment, or their interaction?

### Minimal Assessment

At minimum, authors should include baseline or comparison conditions and report retrieval volume, token budget, and retrieval operator differences across conditions.

## Validity Dimensions and Audit Constructs

| Intended Audit Construct | Primary Retrieval-Environment Risk | Relevant Validity Dimension |
|---|---|---|
| Narrative comprehension | Retrieved text may omit relevant disclosure context | Selection validity |
| Reported relation preservation | Text retrieval may omit accounting relation paths | Selection validity |
| Narrative-numeric integration | Text and relation inputs may be jointly introduced | Separability |
| Assertion mapping | Reported relationships may be treated as audit assertions | Representation validity / audit-valid coding |
| Risk identification | Risk cue may be overstated as audit conclusion | Traceability / audit-valid coding |
| Calculation consistency | Calculation relations may be rendered as economic causality | Representation validity |

## Minimal Reporting Checklist for the Framework

This checklist is the minimum needed for a reader to evaluate retrieval-environment validity.

- intended audit construct
- retrieval design and comparison conditions
- retrieval source
- retrieval unit
- retrieval operator
- ranking or traversal rule
- prompt/context representation of retrieved information
- retrieval logs or examples
- source identifiers or relation path identifiers
- token budget or context length
- repeated retrieval or stability check
- claim-to-source mapping for a sample of outputs
- explanation of how model effects and retrieval effects are separated or bounded

## Accept-Level Framework Criteria

For the framework section to support an accept-level review, it must satisfy these criteria:

1. It explains why dynamic retrieval is methodologically different from fixed information-set design.
2. It defines audit construct narrowly enough to guide retrieval choices.
3. It grounds all five dimensions in established audit or research design concepts.
4. It clarifies that the dimensions are related but not interchangeable.
5. It provides observable indicators or minimal assessment steps for each dimension.
6. It avoids claiming that retrieval-environment validity is a new validity theory.
7. It avoids implying that retrieved information is sufficient appropriate audit evidence.
8. It prepares the reader for later operational tools: retrieval typology, correctness coding, failure modes, checklist, and methodological demonstration.

## What Would Trigger an Accept Recommendation?

From a reviewer perspective, the framework section could support an accept recommendation if it achieves the following:

- The reader understands why retrieval-created information environments are not covered adequately by ordinary descriptions of prompts or model settings.
- The five dimensions feel necessary and grounded, not decorative.
- The framework gives reviewers a practical way to diagnose flawed LLM audit studies.
- The framework can be applied beyond XBRL, while the XBRL application remains audit-specific.
- The manuscript makes clear that output quality, model capability, and construct validity are not the same thing.

Reviewer-level accept statement:

> I would view the framework as a meaningful methodological contribution if it helps researchers and reviewers identify when an LLM audit study's reported performance reflects the retrieval-created information environment rather than the audit construct the study claims to measure.

## Draft Framework Section

Retrieval-augmented LLM audit studies introduce a methodological challenge because the information environment observed by the model is not simply fixed by the researcher before the study. Instead, it is dynamically constructed by retrieval systems that select, rank, transform, and present information at runtime. This dynamic retrieval layer creates retrieval-specific threats to construct validity. Researchers may interpret LLM output differences as evidence of model capability or audit reasoning when those differences instead reflect retrieval selection, representation, instability, weak traceability, or model-retrieval confounding.

We define retrieval-environment validity as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. Retrieval-environment validity is not a replacement for construct validity. Rather, it is a retrieval-specific diagnostic lens for construct validity in LLM-based audit research. It asks whether the retrieval-created information environment permits the researcher to draw the intended inference from the LLM output.

The framework includes five dimensions. Selection validity concerns whether the retrieval system selects information relevant to the intended audit construct. Representation validity concerns whether retrieved information is faithfully represented to the LLM. Stability concerns whether equivalent retrieval requests produce consistent information environments. Traceability concerns whether LLM output claims can be linked to retrieved information. Separability concerns whether researchers can distinguish model behavior from retrieval-created information environment effects. These dimensions adapt established audit and research design concerns--relevance, reliability, documentation, reproducibility, and internal validity--to the dynamic retrieval setting of LLM-based audit research.

## Reviewer Stress Test

### Concern 1: This is just construct validity.

Response:

The framework does not replace construct validity. It specifies how construct validity is threatened in LLM-RAG settings where the information environment is dynamically constructed by retrieval systems rather than fixed by the researcher ex ante.

### Concern 2: The five dimensions are ad hoc.

Response:

Each dimension is grounded in established audit and research design concerns: relevance, reliability, documentation, reproducibility, and internal validity.

### Concern 3: This is generic AI evaluation, not audit research.

Response:

The framework is tied to audit constructs such as narrative comprehension, reported relation preservation, assertion mapping, risk identification, and narrative-numeric integration. It also uses audit concepts such as relevance, reliability, documentation, and professional judgment.

### Concern 4: The framework overclaims what XBRL can do.

Response:

Phase 3 defines the general retrieval-environment validity framework. XBRL is only an instantiation used later to operationalize reported accounting relationships relevant to, but not equivalent to, audit assertions.

### Concern 5: The framework is too theoretical.

Response:

The five dimensions are connected to observable indicators, examples, reviewer questions, and later operational tools such as correctness coding, failure modes, reporting checklists, and the methodological demonstration.

### Concern 6: The framework does not say what changes in research evaluation.

Response:

The framework changes the evaluation target. Instead of asking only whether the LLM output is correct, reviewers ask whether the retrieval-created information environment supports the inference the study draws from that output. This is why the paper later emphasizes claim-level correctness and inference-shift analysis.

### Concern 7: The framework may be too general to be an auditing paper.

Response:

The framework is intentionally general enough to apply beyond XBRL, but it is audit-specific in three ways: it focuses on audit-relevant constructs, grounds validity dimensions in audit evidence and research design concepts, and requires audit-valid correctness to be evaluated through professional judgment rather than graph or text support alone.

## Phase 3 Reviewer-Level Assessment

### Strengths

- The framework now clearly explains why dynamic retrieval differs from fixed information-set experiments.
- The five dimensions are grounded in recognizable audit and research design concepts.
- The framework gives reviewers concrete questions to ask.
- The framework is broad enough to apply beyond XBRL but audit-specific enough to fit AJPT.
- The framework now includes propositions that can structure the manuscript's theoretical contribution.
- The framework clarifies how reviewer evaluation changes after adopting retrieval-environment validity.

### Remaining Weaknesses

- The manuscript must avoid turning the framework into a generic AI evaluation checklist.
- The figure should be visually simple in the final paper.
- Later phases must show how XBRL-based retrieval operationalizes the framework without overclaiming XBRL as audit evidence.
- The methodological demonstration must show that these dimensions change interpretation, not merely describe retrieval settings.
- The framework must define "audit construct" clearly enough that retrieval choices can be evaluated.
- The manuscript must show that the five dimensions are distinct and not simply a renamed checklist of good research practices.

## Phase 3 Deliverables

- Framework definition: complete.
- Fixed-information-set vs dynamic retrieval table: complete.
- Validity dimensions table: complete.
- Observable indicators and examples for each dimension: complete.
- Framework figure draft: complete.
- Draft retrieval-environment validity section: complete.
