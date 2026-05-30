# Phase 2 Literature Review Blueprint

## Purpose

This file converts the annotated bibliography into a literature review strategy for the manuscript.

The literature review must prove that the paper's contribution is distinct, audit-relevant, and aligned with AJPT's methodological paper call.

## Literature Review Thesis

Existing research provides strong foundations for XBRL data, textual analysis, audit analytics, AI in auditing, and LLM accounting applications. However, these streams do not address a central methodological issue in retrieval-augmented LLM audit research: retrieval systems dynamically construct the information environment from which audit-related LLM outputs are generated. This paper fills that gap by introducing retrieval-environment validity as a diagnostic lens for construct validity.

## Recommended Literature Review Structure

### Section 1: AJPT Methodological Guidance Tradition

Purpose:

Show that AJPT values papers that provide methodological guidance for emerging or difficult-to-evaluate research methods.

Core references:

- Power and Gendron (2015)
- Malsch and Salterio (2016)
- Griffith, Kadous, and Young (2016)
- Hatfield and Saiewitz (2022)

Argument:

These papers do not merely report empirical findings. They help researchers, reviewers, and editors evaluate how research should be designed, executed, and interpreted. The present paper follows this tradition for retrieval-augmented LLM audit studies.

Transition sentence:

> As LLM-based audit research emerges, a similar need exists for methodological guidance on how researchers design and evaluate the information environments supplied to LLMs.

### Section 2: XBRL as Structured Reporting Data

Purpose:

Show that XBRL is established in accounting and audit research, but prior work treats it primarily as a data source or measurement basis.

Core references:

- Hoitash, Hoitash, and Morris (2021)
- Hoitash and Hoitash (2018)
- Johnston, Reichelt, and Sapkota (2024)

Argument:

XBRL research shows that structured reporting data can support scalable measurement of accounting complexity, disclosure quality, and disaggregation. However, these studies use XBRL to construct firm-level or disclosure-level variables. The current paper uses XBRL differently: as a structured source for constructing and evaluating retrieval-created information environments in LLM audit studies.

Transition sentence:

> Thus, while XBRL research establishes the value of structured reporting data, it does not address how XBRL relations should be used, validated, and reported when they are retrieved for LLM-based audit research.

### Section 3: Textual Analysis and LLM Accounting Research

Purpose:

Show that accounting research has developed guidance for text-as-data and has begun examining LLMs, but has not yet treated retrieval as research design.

Core references:

- Loughran and McDonald (2016)
- Bae, Hung, and van Lent (2023)
- Blankespoor, deHaan, and Li (2026)
- Kim, Muhn, and Nikolaev (2024)

Argument:

Textual analysis literature emphasizes validation, measurement choices, and reporting when converting accounting narratives into measures. LLM accounting papers examine model capability or AI usage in financial reporting. The current paper complements these streams by asking what researchers can infer from LLM outputs given the retrieval-created information environment.

Transition sentence:

> The relevant methodological issue is no longer only how to measure accounting text, but how retrieved information shapes the construct that an LLM-based study can validly examine.

### Section 4: Audit Analytics, Big Data, and AI in Auditing

Purpose:

Show that audit research recognizes the importance of data relevance, reliability, documentation, and information processing, but has not yet focused on dynamic retrieval as a research design issue.

Core references:

- Appelbaum, Kogan, and Vasarhelyi (2017)
- Appelbaum, Kogan, and Vasarhelyi (2018)
- Brown-Liburd, Issa, and Lombardi (2015)
- Yoon, Hoogduin, and Zhang (2015)
- Fedyk, Hodson, Khimich, and Fedyk (2022)

Argument:

Audit analytics and Big Data research examines how auditors use, process, and evaluate large datasets and emerging technologies. These studies provide important anchors for relevance, reliability, documentation, and audit evidence. However, LLM-RAG studies introduce a distinct design issue: the retrieval system constructs the information environment before the model produces an output.

Transition sentence:

> This shifts the methodological concern from how auditors process data to how researchers validate the information environment dynamically constructed for an LLM.

### Section 5: Synthesis and Gap

Purpose:

Bring the literature streams together and state the gap sharply.

Synthesis paragraph:

Prior methodological papers show the value of research design guidance in auditing. XBRL research shows that structured reporting data can support scalable accounting and audit research measures. Textual analysis research shows the importance of method choice, validation, and reporting when using accounting narratives as data. Audit analytics and AI research show that data relevance, reliability, documentation, and technology adoption matter for audit research. Yet these streams do not address how retrieval systems dynamically construct the information environment in LLM-based audit studies or how researchers should validate the inferences drawn from LLM outputs under different retrieval designs.

Gap sentence:

> The missing methodological object is the retrieval-created information environment.

Contribution sentence:

> This paper introduces retrieval-environment validity to help audit researchers specify, validate, and report that object.

## Literature Positioning Table

| Literature Stream | What It Studies | What It Does Not Address | Current Paper's Contribution |
|---|---|---|---|
| AJPT methodology papers | How to design and evaluate specific audit research methods | Retrieval-created information environments in LLM studies | Extends methodology guidance to LLM-RAG audit research |
| XBRL research | Structured reporting data as firm/disclosure variables | XBRL relations as retrieved information environments | Uses XBRL relations to operationalize retrieval-environment validity |
| Textual analysis | Accounting narratives as data and measures | Retrieval as research design | Moves from text as data to retrieval as research design |
| Audit analytics / Big Data | Auditor use and evaluation of large datasets | Retriever-created information before LLM output | Shifts focus to dynamic construction of the model's information environment |
| LLM / AI accounting | Model capability, AI use, AI adoption | Validity of inference under retrieval-created environments | Provides diagnostic lens and tools for LLM audit study design |

## Draft Literature Review Paragraph

Audit research has a tradition of methodological papers that provide guidance when emerging methods require clearer design and evaluation criteria. Prior AJPT papers provide roadmaps and quality criteria for qualitative research, field research, audit JDM research, and auditor-client communication experiments. This paper follows that tradition by addressing a new class of studies: retrieval-augmented LLM audit research. The methodological challenge in these studies is that the information environment observed by the model is not fixed only by the researcher ex ante. It is dynamically selected, ranked, transformed, and presented by retrieval systems at runtime.

XBRL and textual analysis literatures provide important foundations but do not address this issue directly. XBRL research has shown that structured reporting data can support scalable measures of accounting reporting complexity, disclosure quality, and financial statement disaggregation. Textual analysis research has developed guidance for converting accounting narratives into measures and validating text-based evidence. However, LLM-RAG audit studies require a different methodological lens because retrieval design shapes the information environment from which model outputs are generated. The relevant question is not only whether text or XBRL data are useful, but what researchers can validly infer from LLM outputs given the retrieval environment created for the model.

Audit analytics, Big Data, and AI studies further underscore the importance of data relevance, reliability, documentation, and technology-enabled audit research. Yet these streams generally focus on auditor information processing, audit analytics techniques, AI adoption, or model capability. They do not provide guidance for evaluating whether a dynamically retrieved information environment aligns with the audit construct an LLM study claims to examine. This paper fills that gap by introducing retrieval-environment validity and operationalizing it through retrieval typology, claim-level correctness coding, failure mode diagnosis, reporting guidance, and a descriptive SEC/XBRL methodological demonstration.

## Reviewer Stress Test for Phase 2

### Risk 1: Literature review is too broad.

Response:

Keep each literature bucket tied to the central gap. Do not summarize technology papers for their own sake.

### Risk 2: Contribution looks like XBRL variable construction.

Response:

Emphasize the unit-of-analysis shift from reporting firm to LLM study design.

### Risk 3: Contribution looks like LLM capability evaluation.

Response:

Emphasize that the paper evaluates what researchers can infer under retrieval-created information environments, not whether the model performs well.

### Risk 4: Contribution looks like generic RAG methodology.

Response:

Ground the framework in audit constructs, XBRL-reported accounting relationships, audit-valid correctness, and audit research design concerns.

### Risk 5: Reviewers ask why AJPT should publish it.

Response:

Connect the paper to AJPT's methodological guidance tradition and to the call's focus on research design, variable construction, manipulation, measurement, and reporting guidance.

## Phase 2 Acceptance Criteria

The literature review is ready when it can support the following claim without appearing overstated:

> Existing accounting and auditing research has developed rich methods for using XBRL, text, analytics, and AI, but it has not yet specified how retrieval-created information environments affect construct validity in LLM-based audit research.

