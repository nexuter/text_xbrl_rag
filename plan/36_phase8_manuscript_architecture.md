# Phase 8 Manuscript Architecture

## Purpose

This file converts the phase-by-phase development materials into a manuscript architecture for an AJPT-style methodology paper.

The goal is to make the paper read as a coherent audit research methodology contribution, not as a collection of RAG, XBRL, ontology, and LLM implementation notes.

## Working Title

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

## Central Research Question

How does retrieval design affect the validity of inferences drawn from LLM-based audit research?

## One-Sentence Thesis

In LLM-based audit research, retrieval design is part of research design because retrieval systems dynamically construct the information environment from which researchers infer LLM capability, audit reasoning, or construct performance.

## Manuscript Identity

The manuscript should be positioned as:

- an audit research methodology paper;
- a construct-validity and research-design paper for LLM-RAG audit studies;
- a guidance paper for specifying, evaluating, and reporting retrieval-created information environments.

The manuscript should not be positioned as:

- an audit practice framework;
- an audit automation or AI-agent paper;
- a model benchmark;
- an XBRL ontology construction paper;
- a claim that XBRL is audit evidence;
- a claim that hybrid retrieval is generally superior.

## Reader Takeaway

After reading the paper, an audit researcher should know how to:

1. specify the audit construct before choosing retrieval design;
2. distinguish text retrieval, XBRL relational retrieval, and hybrid retrieval by operator;
3. evaluate LLM outputs at the claim level rather than with a single accuracy score;
4. diagnose retrieval-related failure modes;
5. report retrieval data structures, parameters, logs, prompts, and coding transparently;
6. avoid drawing audit-valid inferences from text-supported or graph-valid claims alone.

## Proposed Manuscript Structure

| Section | Role in Argument | Must Accomplish |
|---|---|---|
| 1. Introduction | Establish methodological problem and contribution | Make clear on page one that retrieval is research design. |
| 2. Related Literature | Position against existing streams | Show movement from text as data and XBRL as data to retrieval as research design. |
| 3. Retrieval-Environment Validity | Define central concept | Ground five dimensions in audit and research design concerns. |
| 4. Retrieval Designs for LLM Audit Research | Operationalize retrieval conditions | Distinguish LLM-only, text, XBRL, and hybrid retrieval by source, unit, operator, representation, and controls. |
| 5. Claim-Level Correctness and Failure Modes | Provide evaluation protocol | Separate text-supported, graph-valid, audit-valid, and integrated correctness. |
| 6. Methodological Guidance and Reporting | Make framework usable | Provide tiered reporting checklist, sensitivity guidance, and reproducibility standards. |
| 7. Methodological Demonstration | Show inference shift | Use SEC/Inline XBRL data and Gemma4:31b outputs to show why retrieval labels are insufficient. |
| 8. Discussion and Boundary Conditions | Bound claims | Clarify what XBRL, hybrid retrieval, and LLM outputs can and cannot support. |
| 9. Conclusion | Close methodology contribution | Return to what audit researchers should do differently. |

## Contribution Placement

The contribution should be stated three times with increasing specificity:

1. **Introduction:** high-level contribution to audit research methodology.
2. **Framework section:** conceptual contribution of retrieval-environment validity.
3. **Guidance/demonstration sections:** operational contribution through typology, coding protocol, reporting checklist, and demonstration.

Recommended contribution paragraph:

> This paper contributes to auditing methodology in three ways. First, it introduces retrieval-environment validity as a retrieval-specific diagnostic lens for construct validity in LLM-based audit research. Second, it operationalizes this concept through tools for mapping retrieval designs to audit constructs, coding LLM outputs at the claim level, diagnosing retrieval-related failure modes, and reporting retrieval conditions. Third, it provides a descriptive methodological demonstration using actual SEC filing and Inline XBRL data to show how retrieval design changes the inferences researchers can draw from LLM audit outputs.

## Main Tables and Figures

| Artifact | Section | Purpose |
|---|---|---|
| Figure 1: Retrieval-Environment Validity Framework | Section 3 | Shows path from audit construct to retrieval design, information environment, output, and inference. |
| Table 1: Fixed Information Set vs Dynamic Retrieval | Section 3 | Establishes why retrieval creates a distinct methodological problem. |
| Table 2: Five Validity Dimensions | Section 3 | Defines selection, representation, stability, traceability, and separability. |
| Table 3: Retrieval Typology | Section 4 | Distinguishes LLM-only, text, XBRL, and hybrid retrieval. |
| Table 4: Inferential Permissions and Limits | Section 4 | Prevents overclaiming from each retrieval design. |
| Table 5: Correctness Layers | Section 5 | Defines text-supported, graph-valid, audit-valid, and integrated correctness. |
| Table 6: Failure Mode Taxonomy | Section 5 | Links failure modes to validity dimensions. |
| Table 7: Tiered Reporting Checklist | Section 6 | Shows reporting standards scale with study claims. |
| Table 8: Selected Demonstration Examples | Section 7 | Shows inference shift using actual outputs. |

## Demonstration Placement

The demonstration should appear after the methodological guidance, not before.

Reason:

The reader needs the framework, retrieval typology, and correctness protocol before seeing the examples. Otherwise, the demonstration may be misread as a model performance experiment.

## Demonstration Narrative

The demonstration should make one point:

> Retrieval-condition labels do not reveal the evidence basis of LLM claims.

The demonstration should show:

- hybrid can produce integrated claims;
- hybrid can also produce text-only or XBRL-only claims;
- XBRL-supported claims can be graph-valid but not sufficient audit evidence;
- LLM-only can function as a traceability diagnostic;
- claim-level coding changes the inference relative to naive accuracy scoring.

## Boundary Language Required Throughout

The manuscript should repeat these boundaries at strategic points:

1. Retrieval-environment validity is a diagnostic lens for construct validity, not a replacement for construct validity.
2. XBRL represents management-coded reported accounting relationships, not independent audit evidence.
3. Hybrid retrieval supports narrative-numeric integration but reduces separability.
4. The demonstration is descriptive, not an inferential performance test.
5. Audit-valid correctness requires expert judgment.
6. Current implementation is an inspectable prototype, not a production vector RAG or graph database system.

## Citation Strategy

The literature section should cite four core streams:

1. Audit methodology and construct validity.
2. XBRL and structured reporting data in accounting research.
3. Textual analysis and LLM use in accounting and auditing research.
4. Audit analytics, Big Data, AI adoption, and evidence evaluation.

Technical RAG, graph retrieval, RDF/OWL, and ontology references should be used sparingly and mainly to explain terminology. They should not dominate the paper.

## Drafting Risks

| Risk | Manuscript Control |
|---|---|
| Paper reads like a technical RAG paper | Keep RAG implementation detail in guidance/appendix; foreground audit construct validity. |
| Paper overclaims XBRL | Repeat XBRL boundary and separate graph-valid from audit-valid correctness. |
| Checklist feels generic | Map checklist items to retrieval-environment validity dimensions. |
| Demonstration looks cherry-picked | State example-selection logic and provide full 94-claim table in appendix. |
| Hybrid appears superior | Emphasize integrated correctness and separability risk. |
| Current prototype appears underbuilt | Position as Tier 1 methodological demonstration; reserve vector/RDF details as implementation guidance. |

## Phase 8 Drafting Decision

The first manuscript draft should be a v0 integrated draft, not a polished submission draft.

The v0 draft should:

- include all major sections;
- preserve reviewer-safe boundary language;
- include table placeholders;
- include demonstration table and narrative;
- use citation placeholders where exact references need final verification;
- identify remaining expert review and citation work.

