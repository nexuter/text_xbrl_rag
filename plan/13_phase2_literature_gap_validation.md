# Phase 2 Literature Gap Validation

## Purpose

This file critically validates whether the proposed paper's contribution is sufficiently distinct from AJPT and top accounting/auditing journal literature.

The test is reviewer-oriented:

> Would a reviewer agree that the paper overcomes a real limitation in prior literature, rather than repackaging XBRL, textual analysis, audit analytics, or LLM application papers?

## Bottom-Line Assessment

The contribution is potentially sufficient, but only if the manuscript keeps the unit of analysis fixed on the **LLM study design** and demonstrates that retrieval design changes valid inference.

The strongest novelty claim remains:

> We move from text as data and XBRL as data to retrieval as research design.

More specifically:

> Prior literature studies data sources, disclosure measures, audit analytics tools, AI adoption, or model capability. This paper studies the retrieval-created information environment that sits between data and LLM output in LLM-based audit research.

## Closest Literature Streams and Gap Validation

### 1. AJPT Methodological Guidance Literature

Relevant papers:

- Power and Gendron (2015), qualitative auditing research roadmap.
- Malsch and Salterio (2016), audit field research quality criteria.
- Griffith, Kadous, and Young (2016), methodological advice for audit JDM research.
- Hatfield and Saiewitz (2022), guidance for auditor-client communication experiments.

What these papers establish:

- AJPT publishes papers that help researchers and reviewers evaluate difficult or emerging audit research methods.
- Methodological guidance papers can be valuable even without large-sample empirical tests when they provide criteria, design choices, and pitfalls.

Remaining limitation:

- These papers do not address LLM-RAG studies.
- They do not address dynamic retrieval-created information environments.
- They do not provide guidance for separating model behavior from retrieval effects.

Current paper's contribution:

> Extends the AJPT methodological guidance tradition to retrieval-augmented LLM audit research.

Reviewer validation:

This is a legitimate AJPT positioning if the paper avoids sounding like a technical RAG paper and instead frames retrieval design as an audit research design problem.

### 2. XBRL Research

Relevant papers:

- Hoitash, Hoitash, and Morris (2021), XBRL review and future research.
- Hoitash and Hoitash (2018), accounting reporting complexity using XBRL.
- Johnston, Reichelt, and Sapkota (2024), financial statement disaggregation using XBRL.
- Related JIS and TAR papers using XBRL to examine reporting complexity, disclosure quality, disaggregation, expertise, or information environment effects.

What these papers establish:

- XBRL is a rich structured reporting data source.
- XBRL can support scalable variable construction.
- XBRL-derived measures can be validated against audit and financial reporting outcomes.

Remaining limitation:

- Prior XBRL studies generally treat XBRL as a firm-level or disclosure-level data source.
- They do not treat XBRL relations as a dynamically retrieved information environment for LLM-based audit studies.
- They do not address whether an LLM output claim is text-supported, graph-valid, audit-valid, or integrated.

Current paper's contribution:

> Moves XBRL from archival variable construction to retrieval-environment construction and evaluation.

Reviewer validation:

The distinction is convincing if the manuscript repeatedly emphasizes the unit-of-analysis shift:

| Prior XBRL literature | Current paper |
|---|---|
| Reporting firm or disclosure is the unit of analysis | LLM study design is the unit of analysis |
| XBRL tags become archival variables | XBRL relations become retrieval-created information environments |
| Validity concerns focus on measure validation | Validity concerns focus on inference from LLM outputs |

### 3. Textual Analysis and Text-as-Data Literature

Relevant papers:

- Loughran and McDonald (2016), textual analysis in accounting and finance.
- Bae, Hung, and van Lent (2023), mobilizing text as data.
- Related transfer learning and accounting disclosure analysis papers.

What these papers establish:

- Accounting research has mature concerns about text measurement, validation, and reporting.
- Researchers must be careful when converting unstructured text into measures.

Remaining limitation:

- Textual analysis literature focuses on converting text into measures.
- It does not focus on retrieval as a design condition that dynamically constructs an LLM's information environment.
- It does not distinguish narrative support from graph validity and audit validity.

Current paper's contribution:

> Extends text-as-data guidance into retrieval-as-research-design guidance.

Reviewer validation:

The novelty is clear if the manuscript avoids claiming that text retrieval is inferior. The better claim is:

> Text retrieval supports narrative comprehension constructs, but it is not sufficient for constructs that require reported relation preservation or narrative-numeric integration.

### 4. Audit Analytics, Big Data, and Data-Driven Auditing

Relevant papers:

- Appelbaum, Kogan, and Vasarhelyi (2017), Big Data and analytics in the modern audit engagement.
- Appelbaum, Kogan, and Vasarhelyi (2018), external audit analytics framework.
- Brown-Liburd, Issa, and Lombardi (2015), behavioral implications of Big Data for audit judgment.
- Yoon, Hoogduin, and Zhang (2015), Big Data as complementary audit evidence.
- O'Leary, Richardson, and Watson (2025), data-driven audits and general ledger analytics tools.
- Wang (2015), audit data analytics issues for research.

What these papers establish:

- Audit research recognizes the importance of relevance, reliability, sufficiency, documentation, and information processing.
- Data analytics and AI tools are important for audit research and practice.

Remaining limitation:

- These papers generally study auditor use of data, audit analytics tools, or data as audit evidence.
- They do not study retrieval systems as dynamic constructors of information environments in LLM research.
- They do not provide a protocol for separating retrieval quality from model capability in LLM audit studies.

Current paper's contribution:

> Shifts the methodological focus from auditor processing of large data to retriever construction of the information environment before LLM output.

Reviewer validation:

This is a meaningful distinction. However, the manuscript must be careful not to imply that retrieved XBRL data are audit evidence. Audit evidence concepts should be used as methodological anchors, not as claims about the evidential sufficiency of retrieved information.

### 5. AI and LLM Accounting/Audit Literature

Relevant papers:

- Kokina and Davenport (2017), AI and automation in auditing.
- Issa and Vasarhelyi (2016), AI research ideas in auditing.
- Fedyk, Hodson, Khimich, and Fedyk (2022), AI in the audit process.
- Li and Vasarhelyi (2024), applying LLMs in accounting.
- Blankespoor, deHaan, and Li (2026), generative AI in financial reporting.
- Kim, Muhn, and Nikolaev (2024), financial statement analysis with LLMs.
- Gu, Schreyer, Moffitt, and Vasarhelyi (2024), AI co-piloted auditing.
- Recent SSRN/working papers on LLMs, continuous auditing, MCP, and agentic auditing.

What these papers establish:

- AI and LLMs are increasingly relevant to accounting and auditing.
- Prior studies examine model capability, application examples, audit workflow integration, AI adoption, or financial reporting usage.

Remaining limitation:

- LLM application papers often evaluate whether LLMs can perform a task.
- Design-science papers often propose systems or prototypes.
- They rarely treat retrieval design as a research design condition that bounds valid inference.
- They rarely separate text-supported, graph-valid, audit-valid, and integrated correctness.

Current paper's contribution:

> Shifts the question from "Can LLMs perform accounting or audit tasks?" to "What can researchers validly infer from LLM outputs given the retrieval-created information environment?"

Reviewer validation:

This is the paper's strongest contrast with the fast-growing LLM audit literature. It must be front-loaded in the introduction.

### 6. Closest Threat: Financial Taxonomy / XBRL LLM Benchmarks

Relevant paper:

- FinAuditing (2025), a financial taxonomy-structured multi-document benchmark for evaluating LLMs using US-GAAP XBRL filings.

Why this is the closest threat:

- It uses XBRL filings.
- It evaluates LLM reasoning over structured financial/taxonomy documents.
- It includes semantic, relational, and numerical consistency tasks.

Remaining limitation:

- It is a benchmark paper.
- It evaluates model capability under taxonomy-structured tasks.
- It does not provide AJPT-style methodological guidance for audit researchers.
- It does not frame retrieval as research design.
- It does not define retrieval-environment validity.
- It does not develop audit-valid correctness as distinct from graph-valid correctness.

Current paper's contribution:

> Complements benchmarks by providing validity guidance for audit researchers designing retrieval-augmented LLM studies.

Critical reviewer note:

The manuscript should cite benchmark-style work as an important adjacent stream but clearly state that its own contribution is not another benchmark. The contribution is a framework for designing and interpreting LLM audit studies.

## Does the Current Paper Overcome Existing Limitations?

### Limitation 1: Prior studies treat retrieval or data provision as an implementation detail.

How the paper overcomes it:

- Defines retrieval-environment validity.
- Identifies selection, representation, stability, traceability, and separability as validity dimensions.

Assessment:

Strong, if the dynamic retrieval layer is made concrete.

### Limitation 2: Prior XBRL work uses structured data for firm/disclosure measurement, not LLM study design.

How the paper overcomes it:

- Uses XBRL relations to construct and evaluate retrieval-created information environments.

Assessment:

Strong, if the paper clearly maintains the unit-of-analysis shift.

### Limitation 3: Prior LLM audit/accounting work focuses on model performance or system prototypes.

How the paper overcomes it:

- Focuses on valid inference from LLM outputs under different retrieval designs.

Assessment:

Strong, especially if paired with an inference shift table.

### Limitation 4: Prior benchmark work treats correctness largely as task performance.

How the paper overcomes it:

- Distinguishes text-supported, graph-valid, audit-valid, and integrated correctness.

Assessment:

Very strong. This may be the most reviewer-compelling novelty point.

### Limitation 5: Prior audit analytics work focuses on auditor processing of data.

How the paper overcomes it:

- Focuses on retriever construction of the information environment before LLM output.

Assessment:

Moderately strong. Needs careful writing to avoid sounding like general AI evaluation.

## Reviewer-Level Novelty Test

Would a reviewer say this paper is "just XBRL + LLM"?

Response:

No, if the manuscript foregrounds:

- retrieval-created information environment
- dynamic retrieval layer
- construct validity diagnostic lens
- claim-level correctness layers
- inference shift rather than accuracy ranking

Would a reviewer say this paper is "just GraphRAG applied to audit"?

Response:

No, if the manuscript foregrounds:

- audit constructs
- XBRL as reported accounting relationships, not ground truth
- audit-valid correctness
- source overreach
- separability and model-retrieval confounding

Would a reviewer say this paper is "just a conceptual checklist"?

Response:

Possibly, unless the methodological demonstration is executed with actual SEC filing and Inline XBRL data.

## Required Strengthening Before Manuscript Draft

1. Add a strong opening contrast:

   > Prior LLM studies ask whether models can perform tasks. We ask what researchers can validly infer from model outputs given the retrieval-created information environment.

2. Emphasize the closest benchmark threat:

   > Unlike taxonomy-structured LLM benchmarks, this paper provides methodological guidance for audit researchers on retrieval design, correctness coding, and bounded inference.

3. Make multi-layered correctness central:

   > A claim may be text-supported and graph-valid but still audit-invalid.

4. Show inference shift in the demonstration:

   > Hybrid retrieval has the highest score is not equivalent to hybrid retrieval is best.

5. Keep XBRL bounded:

   > XBRL relationships are relevant to, but not equivalent to, audit assertions.

## Final Validation Conclusion

The literature search supports the paper's novelty, but only under a disciplined framing.

The contribution is sufficiently distinct if the manuscript consistently argues:

> The paper's object is not XBRL, text, analytics, or LLM capability. The object is the retrieval-created information environment in LLM-based audit research.

This object is under-specified in prior AJPT, XBRL, textual analysis, audit analytics, AI audit, and LLM accounting literatures.

The accept-level novelty will depend on the methodological demonstration showing that retrieval-environment validity changes what researchers can validly infer from LLM outputs.

