# Manuscript Draft v1 with Table and Figure Callouts

## Title

Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval

## Abstract

Retrieval-augmented large language models (LLMs) are increasingly relevant to audit research, yet retrieval is often treated as a technical implementation choice rather than as part of research design. We argue that this treatment is methodologically incomplete because retrieval systems dynamically construct the information environment observed by the model. They select, rank, transform, truncate, and render evidence before the LLM generates an output. As a result, researchers may attribute differences in LLM outputs to model capability or audit reasoning when those differences arise from the retrieval-created information environment.

We introduce retrieval-environment validity, defined as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. We ground the framework in five dimensions: selection, representation, stability, traceability, and separability. The paper operationalizes the framework through a retrieval typology, a construct-to-retrieval mapping, a claim-level correctness protocol, a failure mode taxonomy, reporting guidance, and a descriptive methodological demonstration using SEC filing text and Inline XBRL data. We use XBRL as a management-coded representation of reported accounting relationships relevant to, but not equivalent to, audit assertions. The demonstration shows that text retrieval, XBRL relational retrieval, and hybrid retrieval create different information environments and therefore support different research inferences. The contribution is not that one retrieval design is best; it is that audit researchers must align retrieval design with the intended construct, evaluate LLM outputs at the claim level, and report retrieval environments transparently.

## 1. Introduction

Large language models are increasingly being studied and used in accounting and auditing settings. Many proposed audit research designs augment LLMs with external information through retrieval-augmented generation (RAG), allowing the model to respond using financial filing text, accounting standards, audit workpaper-like materials, structured reporting data, or other domain-specific sources. These designs often describe retrieval as an implementation step: researchers specify a corpus, select a model, provide a prompt, and evaluate the output.

This paper argues that retrieval should instead be treated as part of research design. A retrieval system does not merely add information to an LLM. It constructs the information environment from which the model generates its response. The retriever selects sources, ranks evidence units, traverses relations, filters contexts, truncates materials, formats evidence, and determines which evidence is visible to the model. In retrieval-augmented LLM audit research, the object being evaluated is therefore not simply "the model." It is the model acting within a retrieval-created information environment.

This distinction matters because audit constructs depend on the source, nature, and evidentiary status of information. Narrative disclosures may support analysis of management explanations, accounting policy language, or disclosed risk cues. XBRL tags, facts, contexts, and linkbase relations may support analysis of reported accounting relationships. Neither source is equivalent to audit evidence. A claim can be supported by retrieved text, consistent with XBRL facts, and still overstate what the evidence can support as audit reasoning. Conversely, a response can appear weak because the retriever failed to supply construct-relevant information, even if the model could have reasoned appropriately with a better information environment.

We introduce retrieval-environment validity as a diagnostic lens for this problem. Retrieval-environment validity is the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. It is not a replacement for construct validity. Rather, it identifies retrieval-specific threats to construct validity in studies where the LLM's information set is created at runtime.

[Insert Figure 1 about here]

Figure 1 summarizes the framework. The intended audit construct should drive the retrieval design. The retrieval design creates the information environment observed by the LLM. The LLM produces claims from that environment, and the researcher draws inferences from those claims. Retrieval-environment validity asks whether that chain supports the inference the researcher intends to make.

The paper contributes to audit methodology in three ways. First, it defines retrieval-environment validity and identifies five dimensions: selection, representation, stability, traceability, and separability. Second, it operationalizes the concept through practical tools for audit researchers: a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure taxonomy, tiered reporting standard, and reproducibility guidance. Third, it provides a descriptive methodological demonstration using actual SEC filing text and Inline XBRL data to show how retrieval design changes the evidence basis of LLM-generated audit claims.

The central research question is:

> How does retrieval design affect the validity of inferences drawn from LLM-based audit research?

Answering this question changes what researchers should do when designing and evaluating LLM audit studies. Researchers should specify the audit construct before choosing a retrieval design, match retrieval operators to that construct, preserve retrieval logs and source identifiers, evaluate outputs at the claim level, and distinguish text-supported, graph-valid, audit-valid, and integrated correctness rather than collapsing outputs into a single accuracy measure.

Our demonstration uses Nike, Starbucks, and Target filings, two audit constructs, and four retrieval conditions: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval. The purpose is not to rank retrieval methods or evaluate a model's audit expertise. Instead, the demonstration shows that retrieval-condition labels do not reveal the evidence basis of individual LLM claims. A hybrid condition can produce an integrated text-XBRL claim, but it can also produce claims that rely only on text or only on XBRL. Claim-level coding therefore changes the inference relative to simple response-level evaluation.

The remainder of the paper proceeds as follows. Section 2 positions the paper relative to audit methodology, XBRL research, textual analysis, LLM accounting research, and audit analytics. Section 3 develops retrieval-environment validity. Section 4 operationalizes retrieval designs. Section 5 presents the correctness protocol and failure modes. Section 6 provides methodological guidance and reporting standards. Section 7 presents the demonstration. Section 8 discusses boundary conditions. Section 9 concludes.

## 2. Related Literature

This paper sits at the intersection of audit research methodology, XBRL-based accounting research, textual analysis and LLM accounting research, and audit analytics. The novelty is not the use of XBRL, text retrieval, or LLMs individually. The novelty is the shift in methodological unit of analysis: from text as data, XBRL as data, or models as objects of evaluation to retrieval as research design.

### 2.1 Audit Methodology and Construct Validity

Audit research has long recognized that design choices shape the validity of inferences about auditor judgment, audit evidence, and audit processes. AJPT methodological papers provide guidance when emerging methods require clearer evaluation criteria, including qualitative audit research, field research, judgment and decision-making research, and experimental designs. This paper follows that methodological tradition by addressing a new class of audit studies: retrieval-augmented LLM audit research.

Traditional audit experiments usually define the information set before the study. In retrieval-augmented LLM studies, the information environment may be constructed dynamically at runtime. The researcher may not fully observe or report what the retriever selected, omitted, transformed, ranked, or rendered into the model context. This creates a retrieval-specific construct validity problem: the output may not reflect the audit construct the study claims to examine.

### 2.2 XBRL and Structured Reporting Data

Prior XBRL research uses structured reporting data to study financial reporting, disclosure quality, reporting complexity, disaggregation, tagging choices, data usability, and potential auditor use. This literature establishes XBRL as a valuable accounting data source, especially when researchers carefully specify taxonomy choices, extensions, data quality, and measurement validity.

This paper uses XBRL differently. We do not use XBRL to construct firm-level variables or validate audit conclusions. We use XBRL as a structured retrieval environment that exposes reported accounting facts and relations to an LLM. XBRL-based relational retrieval can help researchers examine whether LLM outputs preserve, distort, hallucinate, or over-rely on reported relationships. Importantly, XBRL is not independent audit evidence or ground truth. It is management-reported structured accounting information that may be relevant to audit constructs but is not equivalent to audit assertions.

### 2.3 Textual Analysis and LLM Accounting Research

Accounting researchers have long used textual analysis to analyze disclosures, classify content, summarize documents, and construct text-based measures. This literature emphasizes that text-based measures require careful attention to construct validity, preprocessing, measurement choices, validation, and reproducibility. Recent LLM accounting research extends this tradition by using generative models for financial statement analysis, disclosure interpretation, and textual analysis tasks.

Text retrieval is useful when the construct depends on narrative meaning, policy language, risk disclosure, or management explanation. However, text retrieval may omit structured accounting relationships central to some audit-relevant constructs. Conversely, XBRL relational retrieval may preserve reported relations while omitting narrative context. This paper therefore distinguishes retrieval designs by source, unit, operator, and construct fit rather than treating all retrieved context as equivalent.

### 2.4 Audit Analytics, Big Data, and AI in Auditing

Audit analytics and AI research examines how auditors and audit technologies process large, complex, or nontraditional data sources. This literature shows that technology-enabled information environments matter for audit judgment, audit evidence, and audit process design. However, our paper focuses on research methodology rather than audit practice. We do not propose an audit procedure or AI audit agent. We provide guidance for researchers studying LLM-based audit tasks.

### 2.5 Synthesis: The Missing Methodological Object

Across these streams, prior research studies data sources, measures, auditors, analytics tools, AI adoption, or model capability. The missing methodological object is the retrieval-created information environment in LLM-based audit research. Retrieval systems sit between data and LLM output. They determine what the model sees, how evidence is represented, whether sources are traceable, and whether output differences can be separated from retrieval effects. This paper fills that gap by introducing retrieval-environment validity and by providing tools for retrieval design, claim-level correctness coding, failure-mode diagnosis, reporting, and sensitivity analysis.

## 3. Retrieval-Environment Validity

Retrieval-augmented LLM audit studies differ from fixed-information-set studies because the information environment observed by the model is dynamically constructed. The retriever selects information, ranks it, renders it into a context window, and may transform or omit materials before the model produces an output. Observed LLM behavior is therefore a function of both the model and the retrieval-created information environment.

We define retrieval-environment validity as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. The concept asks whether the retrieval-created information environment permits the researcher to draw the intended inference from the LLM output.

### 3.1 Fixed Information Sets Versus Dynamic Retrieval

[Insert Table 1 about here]

Table 1 clarifies why retrieval requires methodological attention. In a fixed-information-set design, the researcher defines the evidence package before the study. In a dynamic retrieval design, the information boundary is constructed at query time. Replication therefore requires not only the prompt and model, but also the corpus, retrieval unit, retrieval operator, ranking or traversal rule, context rendering, and returned evidence logs.

### 3.2 Five Dimensions

Retrieval-environment validity has five dimensions.

Selection concerns whether retrieval selects evidence relevant to the intended audit construct. Representation concerns whether retrieved information is faithfully rendered to the LLM. Stability concerns whether equivalent retrieval conditions produce materially similar information environments. Traceability concerns whether output claims can be linked to retrieved materials. Separability concerns whether observed differences can be attributed to model behavior, retrieval design, or their interaction.

[Insert Table 2 about here]

Table 2 is the core framework table. Each dimension adapts established audit and research design concerns to the retrieval setting: relevance, reliability, reproducibility, documentation, and internal validity. The table also links each dimension to observable evidence and a failure mode, making the framework usable as a reviewer checklist rather than only a conceptual vocabulary.

### 3.3 Audit Constructs

For this paper, an audit construct is the audit-relevant capability, judgment, or reasoning object that the researcher claims to study through LLM outputs. Examples include narrative disclosure comprehension, reported relation preservation, narrative-numeric integration, assertion mapping, risk cue identification, calculation consistency reasoning, and evidence traceability.

The framework does not evaluate whether an LLM performs an audit procedure. It evaluates whether the retrieval-created information environment supports the audit-relevant construct the researcher claims to study.

## 4. Retrieval Designs for LLM Audit Research

Retrieval-environment validity requires researchers to specify how retrieval design creates the information environment observed by the LLM. We distinguish four designs: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval.

[Insert Table 3 about here]

Table 3 distinguishes retrieval designs by source, unit, operator, construct fit, and risk. This distinction is important because a retrieval condition is not defined by the final prompt alone. Two studies may both provide "context" to an LLM but create very different information environments if one retrieves narrative chunks and the other retrieves XBRL fact-relation paths.

### 4.1 LLM-Only Baseline

An LLM-only condition provides no external retrieved information. It is useful as a diagnostic baseline for traceability and possible pretraining contamination. However, it provides weak source traceability and cannot support claims about retrieval-supported audit reasoning.

### 4.2 Text Retrieval

Text retrieval selects narrative information such as MD&A, footnotes, accounting policies, standards, or workpaper-like documentation. It can use keyword search, semantic embedding, hybrid retrieval, metadata filters, or reranking. Text retrieval is most appropriate when the construct depends on language: disclosure interpretation, policy classification, management explanation, narrative risk cues, or documentation quality.

The main risk is that text retrieval may not preserve structured accounting relationships. A text chunk may mention a policy or amount without preserving the concept, period, unit, context, calculation relation, or taxonomy relation needed for reported-relation reasoning.

### 4.3 XBRL Relational Retrieval

XBRL relational retrieval selects structured reported facts and relations. Relevant units include concepts, fact values, contexts, units, periods, dimensions, labels, calculation links, presentation links, definition links, and extension concepts. Retrieval operators may include concept lookup, relation traversal, taxonomy filtering, period matching, or ontology queries.

XBRL relational retrieval is most appropriate when the construct concerns reported accounting relationships, numeric consistency, source traceability, or preservation of concept-context-unit-period structure. Its main risk is source overreach. XBRL is management-coded reporting information, not audit evidence. Therefore, graph-valid correctness is not the same as audit-valid correctness.

### 4.4 Hybrid Retrieval

Hybrid retrieval combines narrative context and structured reported relations. It is most appropriate when the construct requires narrative-numeric integration, such as linking a disclosed risk factor or accounting policy to reported account balances, reserves, or contract liability information.

Hybrid retrieval is not automatically superior. It can increase context richness, but it can also reduce separability because output differences may reflect more total information, different ordering, conflicting evidence, or interaction between text and XBRL context. Researchers should therefore evaluate whether individual claims actually integrate both evidence layers.

[Insert Table 4 about here]

Table 4 maps constructs to retrieval designs and identifies what not to claim. This table is deliberately conservative. It prevents the paper from implying that XBRL retrieval provides audit evidence, that hybrid retrieval is universally better, or that retrieval can replace professional judgment.

## 5. Claim-Level Correctness and Failure Modes

Evaluating LLM audit outputs requires more than classifying responses as correct or incorrect. Retrieval designs create different information environments, and those environments support different types of claims. We therefore propose a claim-level correctness protocol.

The unit of analysis is a claim: a discrete assertion in an LLM output that can be evaluated for support, validity, or reasoning quality. A single response may contain factual claims, reported-relationship claims, risk cue claims, assertion mappings, explanations, and conclusions. These claims may differ in their evidence basis.

### 5.1 Four Correctness Layers

[Insert Table 5 about here]

Table 5 distinguishes four correctness layers. Text-supported correctness asks whether a claim is supported by retrieved narrative text. Graph-valid correctness asks whether a claim is consistent with retrieved XBRL facts or relation paths. Audit-valid correctness asks whether the claim is professionally reasonable as audit reasoning. Integrated correctness asks whether text support, graph validity, and audit logic are mutually consistent in the same claim.

This distinction is central to the paper. A claim can be graph-valid but audit-invalid if it treats management-coded XBRL as audit evidence. A claim can be text-supported but not graph-valid if it discusses narrative risk without using structured facts. A claim can appear in a hybrid condition but fail integrated correctness if it uses only one evidence layer.

### 5.2 Failure Modes

[Insert Table 6 about here]

Table 6 links failure modes to retrieval-environment validity. Omission threatens selection. Distortion threatens representation. Retrieval instability threatens reproducibility. Attribution failure threatens traceability. Model-retrieval confounding threatens separability. Relation hallucination, source overreach, and integration failure are especially important for XBRL and hybrid retrieval.

The key methodological point is that failures are not merely output errors. They diagnose how the retrieval-created information environment supports or undermines the researcher's intended inference.

## 6. Methodological Guidance and Reporting

The framework is useful only if researchers can apply it. We therefore provide reporting and reproducibility guidance that scales with the study's claims.

### 6.1 Tiered Reporting Standard

[Insert Table 7 about here]

Table 7 provides a tiered reporting standard. Tier 1 applies to descriptive methodological demonstrations. Researchers should disclose retrieval units, operators, source identifiers, context budgets, prompts, logs, claim coding, and selected spot-checks. Tier 2 applies to empirical LLM audit studies using RAG and requires additional embedding/index metadata, sensitivity checks, expert coding, and reliability evidence. Tier 3 applies to retrieval-system or GraphRAG evaluations and requires benchmark design, retrieval metrics, system parameters, and robustness evidence.

The current paper's demonstration is a Tier 1 methodological demonstration. It should not be read as a performance benchmark for vector RAG, graph databases, or LLM audit expertise.

### 6.2 Implementation Transparency

For text retrieval, researchers should report source document records, chunk schema, chunking rule, chunk size, overlap, embedding model when used, vector index when used, similarity metric, top-k, reranking policy, and retrieval logs.

For XBRL relational retrieval, researchers should report fact tables, concept identifiers, relation edge/path tables, taxonomy and linkbase sources, taxonomy version, extension-concept handling, traversal depth, relation type filters, period/unit/dimension handling, and any RDF/OWL-compatible mapping.

The RDF/OWL layer should be presented as a portability and compatibility schema, not as a claim that XBRL becomes audit evidence. Researchers should distinguish XBRL-coded reporting relations from researcher-coded audit construct or assertion mappings.

### 6.3 Sensitivity Guidance

Recommended sensitivity checks include chunk size, chunk overlap, top-k, query wording, embedding model, reranking, traversal depth, relation type filters, extension concept inclusion, period and dimension filters, token budget equalization, prompt variation, model variation, and repeated retrieval stability.

These checks should be tied to validity dimensions. For example, top-k and traversal depth affect selection validity, relation rendering affects representation validity, repeated retrieval affects stability, source IDs affect traceability, and token budget equalization affects separability.

## 7. Methodological Demonstration

To illustrate how retrieval-environment validity changes the interpretation of LLM-based audit outputs, we conduct a descriptive demonstration using actual SEC filing text and Inline XBRL data. The purpose is not to rank retrieval methods or estimate model performance. The purpose is to show how retrieval design changes the evidence basis of LLM-generated audit claims and therefore changes what researchers can validly infer from those claims.

[Insert Figure 2 about here]

Figure 2 summarizes the demonstration pipeline. We download SEC 10-K filings and Inline XBRL data, extract narrative text and structured facts, build text and XBRL retrieval contexts, run controlled prompts under retrieval conditions, segment responses into claims, and code claims using the correctness protocol.

### 7.1 Setting and Scope

We use three familiar public filers: Nike, Starbucks, and Target. Familiar firms make output claims easier for readers to interpret, but they also increase the risk that the model may rely on general pretraining knowledge. We therefore evaluate claims only against retrieved filing text, retrieved XBRL facts and relation paths, and a no-context diagnostic baseline.

The demonstration covers two audit constructs: revenue recognition risk and inventory valuation assertion. It uses four retrieval conditions: text retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline. The main run uses `gemma4:31b` through local Ollama with temperature set to zero. The full run produced 24 outputs and 94 segmented claims.

The coding is preliminary author coding. Expert review and inter-rater reliability are required before final audit-valid and integrated correctness claims. This limitation is not incidental; it reinforces the paper's argument that audit-valid correctness requires professional judgment rather than automatic scoring.

### 7.2 Implementation Summary

The demonstration uses an inspectable prototype. Text retrieval is keyword-ranked contextual retrieval over extracted 10-K chunks. XBRL retrieval uses extracted fact tables and direct relation paths from Inline XBRL and linkbase data. The demonstration does not claim to implement production vector RAG, RDF/OWL triple-store retrieval, or graph database performance. Instead, the paper uses the prototype to illustrate the reporting and validity issues that any retrieval-augmented LLM audit study should address.

### 7.3 Selected Claim-Level Examples

[Insert Table 8 about here]

Table 8 reports five selected examples chosen to illustrate pre-specified divergence patterns: integrated corroboration, XBRL-only use inside hybrid retrieval, text-only use inside hybrid retrieval, no-context diagnostic behavior, and additional filer coverage. The selected examples are illustrative rather than exhaustive; the full 94-claim coding table should be retained in the appendix or supplemental materials.

The first example shows the constructive role of hybrid retrieval. In the Starbucks inventory case, the model identifies a reported inventory reserve amount and cites both a narrative disclosure and a matching XBRL fact. The valid inference is narrow: hybrid retrieval can support direct narrative-XBRL corroboration for a bounded reported amount when both evidence layers are actually used in the claim.

The second, third, and fifth examples show why hybrid retrieval should not be interpreted as automatically superior. In the Nike revenue and Target inventory cases, the model receives both narrative and XBRL context, but individual claims rely on only one evidence layer. These claims may be useful, but they do not demonstrate integrated reasoning. A response-level evaluation might label them successful hybrid outputs. The correctness protocol leads to a different inference: the hybrid condition created an opportunity for integration, but the claim-level evidence use remained separated.

The fourth example illustrates the role of the LLM-only baseline. When no retrieved filing context is provided, the model states that the context is insufficient to identify filing-specific revenue risk cues. This output should not be interpreted as model failure. It functions as a traceability diagnostic.

### 7.4 Preliminary Coding Summary

[Insert Table 9 about here or move to appendix]

Table 9 summarizes preliminary author coding by retrieval condition and construct. The table should not be interpreted as a ranking of retrieval methods or model performance. The audit-validity means are high because prompts required risk/assertion claims to include inferential bridges and limitations. The more important pattern is that the correctness layers diagnose different properties. Text retrieval supports narrative traceability. XBRL retrieval supports graph-valid reported-fact traceability. Hybrid retrieval supports integrated correctness only when claims actually use both evidence layers.

Overall, the demonstration shows that retrieval design changes the evidence basis of LLM audit claims. A simple answer-level accuracy metric would obscure these differences. Claim-level coding reveals whether the model's output is text-supported, graph-valid, audit-valid, integrated, or merely produced under a retrieval condition label.

## 8. Discussion and Boundary Conditions

The framework has several boundary conditions.

First, retrieval-environment validity is not a new general theory of validity. It is a diagnostic lens for construct validity in studies where retrieval systems dynamically create the information environment observed by LLMs.

Second, XBRL relational retrieval does not convert XBRL into audit evidence. XBRL facts and relations are reported accounting information. They may support graph-validity, reported relation preservation, or narrative-numeric consistency checks, but they do not establish that an audit assertion is satisfied.

Third, hybrid retrieval is not universally superior. It supports a different construct: integration of narrative and reported relational information. Hybrid retrieval can reduce separability because output differences may reflect more total information, different ordering, or interaction between text and relation context.

Fourth, the current demonstration is descriptive. It illustrates inference shifts rather than testing a hypothesis about model performance. Hypothesis-testing studies should use fuller sensitivity checks, expert coding, reliability evidence, and stronger controls over token budget and retrieval variation.

Fifth, audit-valid correctness requires professional judgment. Text support and graph validity are not substitutes for audit reasoning or evidence sufficiency.

## 9. Conclusion

LLM-based audit research increasingly depends on retrieval systems that construct the information environment observed by the model. This paper argues that retrieval should be treated as part of research design. Without specifying and validating retrieval-created information environments, researchers risk drawing conclusions about LLM capability, audit reasoning, or construct performance that are actually driven by retrieval selection, representation, instability, weak traceability, or model-retrieval confounding.

We introduce retrieval-environment validity as a diagnostic lens for this problem and operationalize it through retrieval designs, correctness layers, failure modes, reporting guidance, and a descriptive SEC/XBRL demonstration. The central lesson is not that one retrieval design is best. The lesson is that different retrieval designs support different inferences. Audit researchers should therefore align retrieval design with the intended construct, evaluate output claims at the appropriate correctness layer, and report retrieval environments transparently.

## Main Tables and Figures

The table and figure package is maintained separately in `plan/41_phase8_tables_and_figures_package.md`. The current recommended main-text placement is:

| Manuscript Section | Visual |
|---|---|
| Introduction | Figure 1. Retrieval-Environment Validity Framework |
| Framework | Table 1. Fixed Information Set Versus Dynamic Retrieval; Table 2. Five Dimensions of Retrieval-Environment Validity |
| Retrieval Designs | Table 3. Retrieval Typology; Table 4. Construct-to-Retrieval Mapping |
| Correctness Protocol | Table 5. Claim Correctness Layers; Table 6. Retrieval Failure Mode Taxonomy |
| Reporting Guidance | Table 7. Tiered Reporting Standard |
| Demonstration | Figure 2. Demonstration Pipeline; Table 8. Selected Claim-Level Demonstration Examples; Table 9. Preliminary Coding Summary |

## References Draft

American Accounting Association. 2025. "Call for Papers: Auditing: A Journal of Practice & Theory (AJPT) Methodological Papers." https://aaahq.org/portals/0/documents/calls/2025/AJPT%20Methodological%20Papers.pdf

Appelbaum, D., A. Kogan, and M. A. Vasarhelyi. 2017. "Big Data and Analytics in the Modern Audit Engagement: Research Needs." *Auditing: A Journal of Practice & Theory* 36 (4): 1-27. https://doi.org/10.2308/ajpt-51684

Appelbaum, D. A., A. Kogan, and M. A. Vasarhelyi. 2018. "Analytical Procedures in External Auditing: A Comprehensive Literature Survey and Framework for External Audit Analytics." *Journal of Accounting Literature* 40: 83-101. https://doi.org/10.1016/j.acclit.2018.01.001

Bae, J., C.-Y. Hung, and L. van Lent. 2023. "Mobilizing Text As Data." *European Accounting Review* 32 (5): 1085-1106. https://doi.org/10.1080/09638180.2023.2218423

Blankespoor, E., E. deHaan, and Q. Li. 2026. "Generative AI in Financial Reporting." *Journal of Accounting Research*, accepted. https://doi.org/10.2139/ssrn.4986017

Bochkay, K., S. V. Brown, A. J. Leone, and J. W. Tucker. 2023. "Textual Analysis in Accounting: What's Next?" *Contemporary Accounting Research* 40 (2): 765-805. https://doi.org/10.1111/1911-3846.12825

Brown-Liburd, H., H. Issa, and D. Lombardi. 2015. "Behavioral Implications of Big Data's Impact on Audit Judgment and Decision Making and Future Research Directions." *Accounting Horizons* 29 (2): 451-468. https://doi.org/10.2308/acch-51023

de Kok, T. 2025. "ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research." *Management Science* 71 (9): 7888-7906. https://doi.org/10.1287/mnsc.2023.03253

Fedyk, A., J. Hodson, N. Khimich, and T. Fedyk. 2022. "Is Artificial Intelligence Improving the Audit Process?" *Review of Accounting Studies* 27: 938-985. https://doi.org/10.1007/s11142-022-09697-x

Griffith, E. E., K. Kadous, and D. Young. 2016. "How Insights from the 'New' JDM Research Can Improve Auditor Judgment: Fundamental Research Questions and Methodological Advice." *Auditing: A Journal of Practice & Theory* 35 (2): 1-22. https://doi.org/10.2308/ajpt-51347

Hatfield, R. C., and A. Saiewitz. 2022. "Theoretical and Practical Guidance for Incorporating Auditor-Client Communication in Experimental Research." *Auditing: A Journal of Practice & Theory* 41 (4): 163-177. https://doi.org/10.2308/AJPT-2019-520

Hoitash, R., and U. Hoitash. 2018. "Measuring Accounting Reporting Complexity with XBRL." *The Accounting Review* 93 (1): 259-287. https://doi.org/10.2308/accr-51762

Hoitash, R., U. Hoitash, and L. Morris. 2021. "eXtensible Business Reporting Language (XBRL): A Review and Implications for Future Research." *Auditing: A Journal of Practice & Theory* 40 (2): 107-132. https://doi.org/10.2308/AJPT-2019-517

Johnston, J. A., K. J. Reichelt, and P. Sapkota. 2024. "Measuring Financial Statement Disaggregation Using XBRL." *Journal of Information Systems* 38 (1): 119-147. https://doi.org/10.2308/ISYS-2021-004

Kim, A. G., M. Muhn, and V. V. Nikolaev. 2024. "Financial Statement Analysis with Large Language Models." Working paper. https://arxiv.org/abs/2407.17866

Li, F. 2010. "Textual Analysis of Corporate Disclosures: A Survey of the Literature." *Journal of Accounting Literature* 29: 143-165.

Li, H., and M. A. Vasarhelyi. 2024. "Applying Large Language Models in Accounting: A Comparative Analysis of Different Methodologies and Off-the-Shelf Examples." *Journal of Emerging Technologies in Accounting* 21 (2): 133-152. https://doi.org/10.2308/JETA-2023-065

Loughran, T., and B. McDonald. 2016. "Textual Analysis in Accounting and Finance: A Survey." *Journal of Accounting Research* 54 (4): 1187-1230. https://doi.org/10.1111/1475-679X.12123

Malsch, B., and S. E. Salterio. 2016. "'Doing Good Field Research': Assessing the Quality of Audit Field Research." *Auditing: A Journal of Practice & Theory* 35 (1): 1-22. https://doi.org/10.2308/ajpt-51170

Power, M. K., and Y. Gendron. 2015. "Qualitative Research in Auditing: A Methodological Roadmap." *Auditing: A Journal of Practice & Theory* 34 (2): 147-165. https://doi.org/10.2308/ajpt-10423

Wang, J. J., and V. X. Wang. 2025. "Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and Accounting Tasks." Working paper. https://arxiv.org/abs/2503.16974

Yoon, K., L. Hoogduin, and L. Zhang. 2015. "Big Data as Complementary Audit Evidence." *Accounting Horizons* 29 (2): 431-438. https://doi.org/10.2308/acch-51076

## Remaining Work Before Submission Draft

1. Insert the final formatted tables and figures from `plan/41_phase8_tables_and_figures_package.md`.
2. Prepare appendix materials for the full 94-claim coding table, retrieval logs, prompt templates, and source spot checks.
3. Obtain expert review for selected audit-valid and integrated correctness scores.
4. Finalize reference details and target-journal citation style.
5. Conduct a full AJPT reviewer stress test of manuscript draft v1.
