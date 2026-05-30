# Phase 1 Argument Package

## Purpose of This File

This file stabilizes the paper's core argument before moving into literature review, framework development, and the SEC/XBRL methodological demonstration.

It is designed to ensure that the paper remains aligned with AJPT's methodological paper call and does not drift into an audit automation, XBRL ontology, or RAG performance paper.

## AJPT Call Alignment

AJPT's methodological paper call invites papers that introduce new methods or present recommendations regarding existing methods that are applicable to auditing research. The call is research-focused and does not extend to papers about audit procedures or audit methodologies themselves.

The current paper aligns with the call because it provides methodological guidance for auditing research on LLMs. Specifically, it contributes to:

- research design evaluation and recommendations
- variable construction and measurement guidance
- manipulation of retrieval conditions in LLM audit studies
- reporting and reproducibility guidance
- methodological safeguards for construct validity in LLM-based audit research

The paper should avoid presenting itself as:

- a new audit procedure
- an audit practice framework
- an LLM audit agent system
- a claim that XBRL constitutes audit evidence
- a claim that hybrid retrieval is universally superior

## Final Working Title

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

## Reviewer-Level Bottom Line

If executed as planned, the paper should give reviewers the following takeaway:

> This paper makes a methodological contribution by identifying retrieval-created information environments as an under-specified source of construct validity risk in LLM-based audit research and by providing concrete tools for designing, evaluating, and reporting those environments.

The paper is most likely to receive a positive review if the manuscript makes three things clear on the first page:

1. The unit of analysis is the LLM study design, not the reporting firm, audit firm, or LLM model.
2. The contribution is a research-methods contribution, not an audit practice recommendation.
3. The descriptive demonstration shows an inference shift that a simple accuracy comparison would miss.

## Central Research Question

How does retrieval design affect the validity of inferences drawn from LLM-based audit research?

## One-Paragraph Thesis

In retrieval-augmented LLM audit studies, retrieval design is part of the research design because retrieval systems dynamically select, rank, transform, and present the information environment observed by the model. This dynamic retrieval layer creates retrieval-specific threats to construct validity because researchers may attribute output differences to model capability even when those differences arise from retrieval selection, representation, stability, traceability, or model-retrieval confounding. This paper introduces **retrieval-environment validity** as a diagnostic lens for construct validity in LLM-based audit research and provides tools for specifying, validating, and reporting retrieval-created information environments.

## Core Contribution Hierarchy

The primary contribution is **retrieval-environment validity**.

Everything else in the paper is a supporting tool that operationalizes this concept.

| Level | Contribution | Purpose |
|---|---|---|
| Conceptual | Retrieval-environment validity | Defines the retrieval-specific validity problem |
| Methodological | Typology, correctness protocol, failure taxonomy, checklist, sensitivity checks | Operationalizes the concept for audit researchers |
| Demonstrative | SEC/XBRL methodological demonstration | Shows how retrieval design changes valid inference |

## What Would Researchers Do Differently?

This question is central for an accept-level methodology paper.

After reading the paper, audit researchers should:

- specify the intended audit construct before choosing retrieval design
- match retrieval operators to constructs rather than defaulting to generic text retrieval
- report retrieval source, retrieval unit, retrieval operator, and retrieval logs
- separate model capability from retrieval-created information environment effects
- avoid treating graph-valid or text-supported claims as audit-valid without expert judgment
- disclose when hybrid retrieval reduces separability
- run sensitivity checks on prompt, model, top-k, traversal depth, token budget, taxonomy version, and retrieval stability

## Before-and-After Design Improvement

| Common LLM Audit Study Practice | Improved Practice After This Framework |
|---|---|
| Reports only model accuracy | Reports retrieval design, correctness layers, and inference limits |
| Uses generic 10-K text retrieval | Matches retrieval operator to intended audit construct |
| Treats XBRL relation paths as ground truth | Treats XBRL as management-coded reported accounting relationships |
| Evaluates responses as right or wrong | Codes claims as text-supported, graph-valid, audit-valid, and integrated |
| Omits retrieval logs | Reports retrieval source, unit, operator, logs, and evidence paths |
| Attributes output differences to the model | Separates model behavior from retrieval-created information environment |
| Treats larger context as better context | Evaluates selection validity, representation validity, and separability |

## Final Contribution Paragraph

This paper contributes to auditing methodology in three ways. First, it introduces **retrieval-environment validity** as a retrieval-specific diagnostic lens for construct validity in LLM-based audit research. Second, it operationalizes this concept through tools for mapping retrieval designs to audit constructs, coding LLM outputs at the claim level, diagnosing retrieval-related failure modes, reporting retrieval conditions, and conducting sensitivity checks. Third, it provides a descriptive methodological demonstration using actual SEC filing and Inline XBRL data to show how retrieval design changes the inferences researchers can draw from LLM audit outputs.

## Final Abstract Draft

Retrieval-augmented large language models (LLMs) are increasingly relevant to audit research, yet retrieval is often treated as a background implementation choice. We argue that, in retrieval-augmented LLM audit studies, retrieval design is part of the research design because retrieval systems dynamically select, rank, transform, and present the information environment observed by the model. This dynamic retrieval layer creates retrieval-specific threats to construct validity: researchers may attribute output differences to model capability when those differences arise from retrieval selection, representation, instability, weak traceability, or model-retrieval confounding. We introduce retrieval-environment validity as a diagnostic lens for evaluating whether the dynamically retrieved information environment aligns with the audit construct the researcher intends to study. We ground its five dimensions--selection validity, representation validity, stability, traceability, and separability--in audit and research design concerns of relevance, reliability, documentation, reproducibility, and internal validity. Using XBRL as a management-coded representation of reported accounting relationships relevant to, but not equivalent to, audit assertions, we show how text-based, XBRL-based, and hybrid retrieval designs support different audit constructs. The paper operationalizes the framework through a claim-level correctness protocol, failure taxonomy, reporting guidance, and a descriptive methodological demonstration using SEC filing and Inline XBRL data. The framework helps audit researchers bound what can validly be inferred from LLM outputs about narrative comprehension, reported relation preservation, and narrative-numeric integration.

## One-Page Synopsis

### Motivation

LLM-based audit research is growing quickly, and many studies use retrieval-augmented generation to supply models with accounting and audit-related information. However, retrieval is often treated as an implementation detail rather than a research design choice. This creates a methodological problem: in RAG-based studies, the information environment is dynamically constructed by the retrieval system at runtime. Researchers may therefore draw conclusions about LLM audit reasoning without validating whether the retrieved information environment aligns with the construct they intended to study.

### Gap

Prior XBRL studies use structured reporting data to construct firm- or disclosure-level variables. Prior textual analysis studies convert accounting narratives into measures. Prior audit analytics studies examine how auditors process large and complex data. Prior LLM accounting studies evaluate model capabilities or AI use in reporting. This paper differs by moving the unit of analysis to the LLM study design itself and showing that retrieval systems dynamically construct the information environment from which audit-related inferences are drawn.

### Proposed Concept

The paper introduces retrieval-environment validity: the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. The concept is not a replacement for construct validity. It is a retrieval-specific diagnostic lens for construct validity in LLM-based audit research.

### Dimensions

Retrieval-environment validity has five dimensions:

- selection validity, anchored in relevance
- representation validity, anchored in reliability and faithful representation
- stability, anchored in reproducibility
- traceability, anchored in documentation and support
- separability, anchored in internal validity

### XBRL Role

XBRL is used as a scalable example of structured retrieval because it encodes management-coded reported accounting relationships. These relationships are relevant to, but not equivalent to, audit assertions. XBRL is not independent audit evidence or ground truth. XBRL-based relational retrieval helps researchers examine whether LLMs preserve, distort, hallucinate, or over-rely on reported accounting relationships.

### Methodological Tools

The framework is operationalized through:

- a retrieval typology distinguishing text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval
- a claim-level correctness protocol distinguishing text-supported, graph-valid, audit-valid, and integrated correctness
- a failure mode taxonomy covering omission, distortion, retrieval instability, attribution failure, model-retrieval confounding, relation hallucination, source overreach, and integration failure
- a reporting checklist and sensitivity check guidance

### Demonstration

The paper will include a descriptive methodological demonstration using actual SEC filing and Inline XBRL data. The demonstration will compare text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval across audit constructs such as revenue recognition risk and inventory valuation assertion. The purpose is not to rank retrieval methods, but to show how retrieval design changes what researchers can validly infer from LLM outputs.

### Expected Contribution

The paper contributes to auditing methodology by reframing retrieval as research design in LLM-based audit research. It helps researchers avoid inferential overreach by specifying, validating, and reporting retrieval-created information environments.

## Boundary Statements

These statements should appear in the introduction or early framework section.

1. Retrieval-environment validity is not a replacement for construct validity; it is a retrieval-specific diagnostic lens for construct validity.
2. XBRL encodes management-coded reported accounting relationships that are relevant to, but not equivalent to, audit assertions.
3. XBRL is not independent audit evidence or ground truth.
4. Hybrid retrieval is not universally superior; it supports narrative-numeric integration but may reduce separability.
5. The methodological demonstration is descriptive, not inferential.
6. The paper does not prescribe a universally preferred retrieval architecture.

## Why This Is Not Merely Traditional Construct Validity

Reviewer risk:

> Information environments have always mattered in audit research. Why does this paper need a new concept?

Core response:

Retrieval-environment validity is not a new validity theory. It is a retrieval-specific diagnostic lens for construct validity in studies where the information environment is dynamically produced by a retrieval system rather than fixed by the researcher ex ante.

| Traditional audit study information design | Retrieval-augmented LLM audit study |
|---|---|
| Researcher defines the information set before the study. | Retriever selects information at runtime. |
| Treatment materials are usually stable across participants or conditions. | Retrieved information may vary by query, model, index, ranking, or traversal rule. |
| Information content is directly inspectable before the experiment. | Information content may be selected, transformed, summarized, or omitted by the retrieval pipeline. |
| Differences in output are often attributed to participant judgment or treatment manipulation. | Differences in output may reflect model behavior, retrieval quality, or model-retrieval interaction. |
| Documentation focuses on experimental materials. | Documentation must include retrieval source, unit, operator, logs, and evidence paths. |

This comparison should appear early in the paper to make clear why the dynamic retrieval layer creates a distinct methodological problem.

## Critical Reviewer Assessment of Phase 1

### Strengths

- The paper's identity is now clearly methodological rather than technical.
- The central contribution is focused on retrieval-environment validity.
- The argument is aligned with AJPT's call for research design, measurement, variable construction, and reporting guidance.
- Boundary statements reduce the risk of overclaiming XBRL, hybrid retrieval, or LLM audit capability.

### Remaining Weaknesses

- The abstract still depends on the reader accepting that dynamic retrieval creates a distinct validity issue. The paper must make this difference concrete in the introduction.
- The demonstration is doing heavy lifting. Without actual SEC filing and Inline XBRL data, the contribution may look like a conceptual checklist.
- The phrase "audit construct" must be defined carefully in Phase 3 to avoid sounding too broad.
- The paper must avoid a long technical explanation of RAG, GraphRAG, or implementation architecture.

### Required Improvements in Later Phases

- Add a fixed-information-set versus dynamic-retrieval comparison early in the manuscript.
- Build a real methodological demonstration, not a hypothetical example.
- Keep the literature review focused on audit methodology, XBRL, textual analysis, audit analytics, and LLM accounting research.
- Treat audit-valid correctness as expert-coded judgment, not objective truth.
- Include an inference shift table in the demonstration.

## Reviewer Stress Test

### Reviewer Concern 1: Is this just construct validity with new terminology?

Response:

The paper does not claim to replace construct validity. It identifies retrieval-specific threats to construct validity that arise because RAG systems dynamically construct the information environment observed by the LLM. Traditional audit studies often fix the information set ex ante; LLM-RAG studies introduce runtime selection, ranking, transformation, and presentation of information.

### Reviewer Concern 2: Is this an audit practice paper rather than an audit research methodology paper?

Response:

The paper provides guidance for researchers designing LLM-based audit studies. It does not prescribe audit procedures, audit evidence evaluation procedures, or audit practice workflows. The key outputs are research design typologies, validity dimensions, coding protocols, and reporting guidance.

### Reviewer Concern 3: Does XBRL really represent audit assertions?

Response:

The paper does not claim equivalence. It states that XBRL encodes reported accounting relationships that are relevant to, but not equivalent to, audit assertions. The purpose is to study whether LLMs preserve, distort, hallucinate, or over-rely on those reported relationships.

### Reviewer Concern 4: Is hybrid retrieval being presented as the best method?

Response:

No. Hybrid retrieval supports a different construct: narrative-numeric integration. It may improve integrated correctness but reduce separability because narrative and relational inputs are jointly introduced.

### Reviewer Concern 5: Is the framework too checklist-like?

Response:

The central contribution is retrieval-environment validity. The typology, correctness protocol, failure taxonomy, reporting checklist, and methodological demonstration are supporting tools that operationalize this single concept.

### Reviewer Concern 6: Will the demonstration be strong enough?

Response:

The demonstration must use actual SEC filing and Inline XBRL data, provide retrieval logs, show text chunks and XBRL relation paths, code LLM claims at the claim level, and present an inference shift table. The demonstration's goal is to show how retrieval design changes valid inference, not to rank methods.

### Reviewer Concern 7: What is the paper's minimum empirical burden?

Response:

The paper does not need a large-sample performance test because it is a methodological paper. However, it does need a concrete methodological demonstration with actual SEC filing and Inline XBRL data. The demonstration must show that the framework changes interpretation relative to a naive accuracy-based comparison. Without this demonstration, the paper risks reading as a conceptual checklist.

### Reviewer Concern 8: Is the contribution sufficiently general beyond XBRL?

Response:

Yes, if XBRL is framed as the scalable instantiation rather than the boundary of the framework. Retrieval-environment validity applies to any LLM audit study in which a retrieval system constructs the information environment. XBRL is used because it provides a structured and institutionally embedded example of management-coded reported accounting relationships.

### Reviewer Concern 9: Is the paper too broad?

Response:

The paper should keep retrieval-environment validity as the single primary contribution. The typology, correctness protocol, failure taxonomy, checklist, and demonstration should be presented only as operational tools for this concept.

## Accept-Level Reviewer Criteria

For a reviewer to recommend acceptance, the manuscript should satisfy all of the following:

- The first page clearly identifies the paper as an auditing research methodology paper.
- The paper explains why dynamic retrieval creates a distinct validity problem beyond ordinary information-set design.
- The paper defines retrieval-environment validity as a diagnostic lens for construct validity, not a replacement for construct validity.
- The paper grounds the five dimensions in established audit and research design concerns.
- The paper treats XBRL as management-coded reported accounting relationships, not audit evidence or ground truth.
- The paper shows what researchers should do differently after reading it.
- The methodological demonstration uses actual SEC filing and Inline XBRL data.
- The demonstration includes an inference shift table, not merely an accuracy table.
- The manuscript avoids presenting hybrid retrieval as the best method.
- The manuscript avoids excessive technical discussion of RAG architecture, GraphRAG, ontology tooling, or MCP.

## Remaining Accept-Level Gaps

The Phase 1 argument is accept-level only if later phases deliver the following:

1. A literature review that proves the unit-of-analysis shift from firm/model to LLM study design.
2. A rigorous framework section that makes the dynamic retrieval layer concrete.
3. A real methodological demonstration using SEC filing and Inline XBRL data.
4. Claim-level coding examples that distinguish text-supported, graph-valid, audit-valid, and integrated correctness.
5. A clear inference shift table showing that the framework changes what researchers can validly conclude.

## AJPT Call Alignment Checklist

| AJPT Call Emphasis | Alignment in This Paper |
|---|---|
| New or improved methods applicable to auditing research | Retrieval-environment validity for LLM-based audit studies |
| Research design recommendations | Retrieval typology and construct-to-retrieval mapping |
| Variable construction and measurement guidance | Claim-level correctness protocol and failure mode taxonomy |
| Effective manipulation and measurement | Retrieval conditions and correctness layers |
| Reproducibility and transparency | Reporting checklist, retrieval logs, sensitivity checks |
| Not audit procedures or audit methodologies | Explicit boundary: paper guides research design, not audit practice |

## Phase 1 Decision Log

### Decisions Made

- The paper will be framed as an audit methodology paper.
- The central concept is retrieval-environment validity.
- The central research question is fixed as: How does retrieval design affect the validity of inferences drawn from LLM-based audit research?
- XBRL will be framed as management-coded reported accounting relationships, not audit evidence.
- Hybrid retrieval will be framed as construct-specific, not universally superior.
- The demonstration will be descriptive and inference-focused.

### Open Decisions for Later Phases

- Final target journal: AJPT methodology call vs alternative outlet.
- Final filer selection for the methodological demonstration.
- Exact LLM model(s) and retrieval implementation for the demonstration.
- Whether to build a minimal prototype locally or use curated retrieval outputs for the demonstration.
- Final bibliography and citation style.
