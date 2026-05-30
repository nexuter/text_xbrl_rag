# Phase 8 Citation Strengthening Memo

## Purpose

This memo strengthens the manuscript's literature positioning by replacing broad citation placeholders with targeted citation groups and sharpening the novelty claim against AJPT and top accounting/auditing literature.

The objective is not to create an exhaustive literature review. The objective is to support the paper's central contribution:

> We move from text as data and XBRL as data to retrieval as research design.

## AJPT Call Alignment

The AJPT methodological papers call is directly relevant because it invites papers that introduce new methods or make recommendations about existing methods applicable to auditing research. The call explicitly includes evaluation of research design, modeling, variable selection, data collection, variable construction, manipulation, and measurement, while excluding papers focused on audit procedures or audit methodologies themselves.

This paper aligns with that scope because it provides research-method guidance for LLM-based audit studies:

- retrieval design as a research design choice;
- retrieval-environment validity as a construct-validity diagnostic;
- claim-level correctness as a measurement protocol;
- reporting and reproducibility guidance for retrieval-created information environments.

## Citation Buckets and Positioning

### 1. AJPT Methodological Guidance

Core citations:

- Power and Gendron (2015)
- Malsch and Salterio (2016)
- Griffith, Kadous, and Young (2016)
- Hatfield and Saiewitz (2022)

Positioning:

These papers show that AJPT values methodological guidance when researchers and reviewers need better criteria for evaluating emerging or complex research methods. The current paper follows this tradition for retrieval-augmented LLM audit research.

Novelty relative to this stream:

Prior AJPT methodology papers do not address dynamic retrieval, LLM-RAG study design, or the separation of model behavior from retrieval-created information environments.

### 2. XBRL and Structured Reporting Data

Core citations:

- Hoitash, Hoitash, and Morris (2021)
- Hoitash and Hoitash (2018)
- Johnston, Reichelt, and Sapkota (2024)

Positioning:

XBRL research establishes that structured reporting data can support scalable accounting and auditing research. Prior work uses XBRL to review data opportunities, study data quality and extensions, and construct measures such as reporting complexity or disaggregation.

Novelty relative to this stream:

The current paper does not use XBRL to construct a firm-level or disclosure-level variable. It uses XBRL relations to construct and evaluate the retrieval-created information environment supplied to an LLM. The unit of analysis shifts from the reporting firm or disclosure to the LLM study design.

### 3. Textual Analysis and Text-as-Data

Core citations:

- Li (2010)
- Loughran and McDonald (2016)
- Bochkay, Brown, Leone, and Tucker (2023)
- Bae, Hung, and van Lent (2023)

Positioning:

Textual analysis research establishes that accounting narratives can be transformed into measures, but that implementation choices and construct validity matter. This literature is the closest analogue for treating representation, measurement, and validation as methodological problems.

Novelty relative to this stream:

Textual analysis studies focus on converting text into measures. The current paper focuses on retrieval as the design layer that determines what textual or structured information an LLM observes before generating output.

### 4. Generative LLMs in Accounting and Financial Reporting

Core citations:

- de Kok (2025)
- Kim, Muhn, and Nikolaev (2024)
- Blankespoor, deHaan, and Li (2026)
- Li and Vasarhelyi (2024)
- Wang and Wang (2025)

Positioning:

Generative LLM research in accounting examines model use for textual analysis, financial statement analysis, disclosure production, accounting applications, and output reproducibility.

Novelty relative to this stream:

These papers generally ask whether LLMs can perform tasks, how they should be used, or how consistent their outputs are. The current paper asks what researchers can validly infer from LLM outputs given the retrieval-created information environment.

### 5. Audit Analytics, Big Data, and AI in Auditing

Core citations:

- Brown-Liburd, Issa, and Lombardi (2015)
- Yoon, Hoogduin, and Zhang (2015)
- Appelbaum, Kogan, and Vasarhelyi (2017)
- Appelbaum, Kogan, and Vasarhelyi (2018)
- Fedyk, Hodson, Khimich, and Fedyk (2022)

Positioning:

Audit analytics and Big Data research establishes that relevance, reliability, information overload, pattern recognition, ambiguity, and audit evidence concepts matter when auditors and audit technologies interact with complex data environments.

Novelty relative to this stream:

Prior work generally focuses on auditor use of data, audit analytics methods, technology adoption, or audit outcomes. The current paper focuses on the retrieval system as the mechanism that constructs the information environment before an LLM generates an audit-related output.

## Updated Literature Review Contribution

The revised literature review should support the following paragraph:

> Prior methodological papers show that audit research benefits from guidance when emerging methods require clearer design and evaluation criteria. Prior XBRL and textual analysis studies show that structured and unstructured reporting data can support accounting research when validity and implementation choices are carefully specified. Prior audit analytics and AI studies show that technology-enabled information environments matter for audit research and practice. However, these streams do not directly address how retrieval systems dynamically construct the information environment observed by an LLM or how that retrieval-created environment bounds valid inference from LLM outputs.

## Reviewer-Facing Novelty Table

| Literature Stream | Prior Unit of Analysis | Main Contribution of Prior Work | Remaining Gap | Current Paper's Novelty |
|---|---|---|---|---|
| AJPT methodology | Research method or design | Guidance for evaluating audit research methods | No guidance for LLM-RAG retrieval environments | Extends methodology guidance to retrieval-augmented LLM audit studies |
| XBRL research | Firm, filing, tag, disclosure | Structured reporting data and scalable variable construction | Does not treat XBRL relations as retrieved LLM information environments | Uses XBRL relations to operationalize retrieval-environment validity |
| Textual analysis | Text document or text-derived measure | Text-as-data measurement and validation | Does not treat retrieval as a dynamic research design layer | Moves from text as data to retrieval as research design |
| LLM accounting | Model, task, prompt, output | Capability, textual analysis, disclosure production, consistency | Does not isolate retrieval-created information environments | Shifts from "can LLMs do the task?" to "what can researchers infer?" |
| Audit analytics / AI | Auditor, technology, audit outcome | Data analytics, AI adoption, audit evidence implications | Does not study retriever-created information before LLM output | Focuses on retrieval as the pre-output information environment |

## Revisions Made to Draft v0

The related literature section in `plan/37_phase8_manuscript_draft_v0.md` was revised to:

1. replace broad citation placeholders with named citation groups;
2. add an explicit unit-of-analysis framing;
3. distinguish XBRL-as-variable from XBRL-as-retrieval-environment;
4. distinguish text-as-data from retrieval-as-research-design;
5. distinguish LLM capability evaluation from inference validity under retrieval;
6. add a synthesis subsection identifying the missing methodological object.

## Remaining Citation Work

Before submission, the manuscript still needs:

1. final verification of every citation's bibliographic details;
2. selection of the final target journal style;
3. a complete reference list;
4. possible addition of a small number of benchmark/RAG citations, kept subordinate to audit methodology;
5. final review to ensure the literature section is not too broad.

## Reviewer Stress Test

Would a reviewer say the paper is merely XBRL plus LLM?

No, if the manuscript keeps the unit of analysis on LLM study design and explains that XBRL is used to instantiate relational retrieval, not to construct a firm-level variable or audit evidence proxy.

Would a reviewer say the paper is merely textual analysis with LLMs?

No, if the manuscript emphasizes that text retrieval dynamically constructs the information environment and that the key issue is valid inference from LLM outputs, not text measurement alone.

Would a reviewer say the paper is merely an AI audit application?

No, if the manuscript continues to state that it is not proposing an audit procedure, audit agent, or model benchmark. It is a research-method paper.

Would a reviewer see publication-level novelty?

Potentially yes. The novelty is strongest when stated as:

> Prior accounting and auditing research studies data, tools, models, auditors, or outcomes. This paper studies the retrieval-created information environment that connects source data to LLM output in audit research designs.

