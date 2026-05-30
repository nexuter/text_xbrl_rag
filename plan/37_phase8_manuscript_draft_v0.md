# Manuscript Draft v0

## Title

Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval

## Abstract

Retrieval-augmented large language models (LLMs) are increasingly relevant to audit research, yet retrieval is often treated as a background implementation choice. We argue that, in retrieval-augmented LLM audit studies, retrieval design is part of the research design because retrieval systems dynamically select, rank, transform, and present the information environment observed by the model. This dynamic retrieval layer creates retrieval-specific threats to construct validity: researchers may attribute output differences to model capability when those differences arise from retrieval selection, representation, instability, weak traceability, or model-retrieval confounding. We introduce retrieval-environment validity as a diagnostic lens for evaluating whether the dynamically retrieved information environment aligns with the audit construct the researcher intends to study. We ground its five dimensions--selection validity, representation validity, stability, traceability, and separability--in audit and research design concerns of relevance, reliability, documentation, reproducibility, and internal validity. Using XBRL as a management-coded representation of reported accounting relationships relevant to, but not equivalent to, audit assertions, we show how text-based, XBRL-based, and hybrid retrieval designs support different audit constructs. The paper operationalizes the framework through a retrieval typology, claim-level correctness protocol, failure taxonomy, reporting checklist, sensitivity guidance, and a descriptive methodological demonstration using SEC filing and Inline XBRL data. The framework helps audit researchers bound what can validly be inferred from LLM outputs about narrative comprehension, reported relation preservation, and narrative-numeric integration.

## 1. Introduction

Large language models are increasingly being used and studied in accounting and auditing settings. Many proposed research designs augment LLMs with external information through retrieval-augmented generation (RAG), allowing the model to respond using filing text, standards, workpaper-like materials, structured data, or other domain-specific sources. In these studies, retrieval is often described as an implementation detail: researchers report the model, the prompt, and sometimes the external corpus, while the retrieval process itself remains in the background.

This paper argues that this treatment is methodologically incomplete. In LLM-based audit research, retrieval design is part of research design. A retrieval system does not merely provide more information to an LLM; it dynamically constructs the information environment from which the model generates its output. It selects sources, ranks units, traverses relations, filters contexts, truncates or reformats materials, and determines what retrieved materials are visible to the model. As a result, researchers may draw conclusions about LLM audit reasoning, model capability, or audit construct performance when the observed output instead reflects the retrieval-created information environment.

This problem is especially important in auditing research because audit-related constructs often depend on the nature, source, and evidentiary status of information. Narrative disclosures may support analysis of management explanations or accounting policy language. XBRL tags and linkbase relations may support analysis of reported accounting relationships. Neither is equivalent to audit evidence. A claim can be supported by retrieved text, consistent with XBRL relations, and still be professionally unreasonable as audit reasoning if it overstates what the retrieved information can support.

We introduce **retrieval-environment validity**, defined as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. Retrieval-environment validity is not a replacement for construct validity. It is a retrieval-specific diagnostic lens for construct validity in studies where the information set observed by the LLM is not fixed ex ante, but created by a retrieval system at runtime.

The paper contributes to auditing methodology in three ways. First, it introduces retrieval-environment validity as a framework for evaluating retrieval-created information environments in LLM-based audit research. Second, it operationalizes the framework through a retrieval typology, claim-level correctness protocol, failure mode taxonomy, and reporting guidance. Third, it provides a descriptive methodological demonstration using actual SEC filing and Inline XBRL data to show how retrieval design changes the inferences researchers can draw from LLM audit outputs.

The central research question is: How does retrieval design affect the validity of inferences drawn from LLM-based audit research? Answering this question changes what researchers should do when designing and evaluating LLM audit studies. Researchers should specify the audit construct before choosing a retrieval design, match retrieval operators to that construct, preserve retrieval logs and source identifiers, evaluate LLM outputs at the claim level, and distinguish text-supported, graph-valid, audit-valid, and integrated claims rather than collapsing outputs into a single accuracy measure.

Our demonstration uses Nike, Starbucks, and Target filings, two audit constructs, and four retrieval conditions: LLM-only, text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval. The purpose is not to rank retrieval methods or evaluate a model's audit expertise. Instead, the demonstration shows that retrieval-condition labels do not reveal the evidence basis of individual LLM claims. A hybrid condition can produce an integrated text-XBRL claim, but it can also produce text-only or XBRL-only claims. Claim-level coding therefore changes the inference relative to a simple answer-level accuracy evaluation.

The remainder of the paper proceeds as follows. Section 2 positions the paper relative to audit methodology, XBRL research, textual analysis, LLM accounting research, and audit analytics. Section 3 develops retrieval-environment validity. Section 4 operationalizes retrieval designs. Section 5 presents the correctness protocol and failure modes. Section 6 provides methodological guidance and reporting standards. Section 7 presents the demonstration. Section 8 discusses boundary conditions. Section 9 concludes.

## 2. Related Literature

This paper sits at the intersection of audit research methodology, XBRL-based accounting research, textual analysis and LLM accounting research, and audit analytics. The novelty is not the use of XBRL data, text retrieval, or LLMs individually. The novelty is the shift in unit of analysis: from text as data, XBRL as data, or models as objects of evaluation to retrieval as research design.

The literature review is organized around this unit-of-analysis shift. Prior methodological papers show that auditing research benefits from guidance when emerging methods require clearer design and evaluation criteria. Prior XBRL and textual analysis studies show that accounting researchers can construct measures from structured and unstructured reporting data when validity and implementation choices are carefully specified. Prior audit analytics and AI studies show that technology-enabled information environments matter for audit research and practice. However, these streams do not directly address how retrieval systems dynamically construct the information environment observed by an LLM or how that retrieval-created environment bounds valid inference from LLM outputs.

### 2.1 Audit Methodology and Construct Validity

Audit research has long recognized that research design choices shape the validity of inferences about auditor judgment, audit evidence, and audit processes. AJPT has published methodological guidance papers that help researchers and reviewers evaluate qualitative audit research, field research, audit JDM research, and experimental design choices (e.g., Power and Gendron 2015; Malsch and Salterio 2016; Griffith, Kadous, and Young 2016; Hatfield and Saiewitz 2022). This paper follows that methodological tradition by addressing a new class of audit studies: retrieval-augmented LLM audit research.

LLM-based audit studies introduce a related but distinct problem. Traditional audit experiments usually define the information set before the study. In retrieval-augmented LLM studies, the information environment may be dynamically constructed at runtime. The researcher may not fully observe or report what the retriever selected, omitted, transformed, or ranked. This creates a retrieval-specific construct validity concern: the output may not reflect the audit construct the study claims to examine.

### 2.2 XBRL and Structured Reporting Data

Prior XBRL research uses structured reporting data to study financial reporting, disclosure quality, reporting complexity, disaggregation, tagging choices, and data usability. Hoitash, Hoitash, and Morris (2021) review XBRL research and emphasize the richness of XBRL data, including adoption, data quality, extensions, and potential auditor use and assurance. Hoitash and Hoitash (2018) use XBRL tags to construct a measure of accounting reporting complexity. Johnston, Reichelt, and Sapkota (2024) use XBRL to measure financial statement disaggregation. These studies establish XBRL as a valuable structured reporting data source for accounting and auditing research.

This paper uses XBRL differently. We do not use XBRL to construct firm-level variables or to validate audit conclusions. We use XBRL as a structured retrieval environment that can expose reported accounting relationships to an LLM. XBRL-based relational retrieval helps researchers examine whether LLM outputs preserve, distort, hallucinate, or over-rely on reported relationships. Importantly, XBRL is not independent audit evidence or ground truth. It is reported accounting information that may be relevant to audit constructs but is not equivalent to audit assertions.

### 2.3 Textual Analysis and LLM Accounting Research

Accounting and auditing researchers increasingly use textual analysis to analyze disclosures, summarize documents, classify accounting content, and construct text-based measures. Li (2010) surveys textual analysis of corporate disclosures, while Loughran and McDonald (2016) emphasize implementation challenges and the relative imprecision of textual methods in accounting and finance. Bochkay, Brown, Leone, and Tucker (2023) provide a broad review of textual analysis in accounting, including construct validity and implementation decisions. This stream establishes that text-based accounting measures require careful attention to representation, validation, and reporting.

Recent work extends this tradition to generative LLMs. de Kok (2025) provides guidance on using generative LLMs in accounting textual analysis and emphasizes model selection, prompt engineering, construct validity, bias, replicability, and data sharing. Kim, Muhn, and Nikolaev (2024) evaluate LLMs for financial statement analysis. Blankespoor, deHaan, and Li (2026) examine generative AI usage in financial reporting disclosures. These papers show that LLMs are becoming important tools and objects of study in accounting research.

Text retrieval is useful when the construct depends on narrative meaning, policy language, risk disclosure, or management explanation. However, text retrieval may omit structured accounting relationships that are central to some audit-relevant constructs. Conversely, XBRL relation retrieval may preserve reported relationships while omitting narrative context. This paper therefore distinguishes retrieval designs by operator and construct fit rather than treating all retrieved context as equivalent.

### 2.4 Audit Analytics, Big Data, and AI in Auditing

Audit analytics and AI research examines how auditors and audit technologies process large, complex, or nontraditional data sources. Brown-Liburd, Issa, and Lombardi (2015) discuss how Big Data affects audit judgment and decision making through information overload, relevance, pattern recognition, and ambiguity. Yoon, Hoogduin, and Zhang (2015) evaluate Big Data as complementary audit evidence using relevance, reliability, and sufficiency considerations. Appelbaum, Kogan, and Vasarhelyi (2017, 2018) identify research needs and frameworks for audit analytics. Fedyk, Hodson, Khimich, and Fedyk (2022) provide large-scale evidence on AI adoption in audit firms and audit outcomes. Together, this literature shows that technology-enabled data environments matter for audit research.

Our paper contributes to this stream by focusing on research methodology rather than audit practice. We do not propose an audit procedure or AI audit agent. Instead, we provide guidance for researchers studying LLM-based audit tasks. The key methodological issue is whether retrieval-created information environments support the inferences researchers draw from LLM outputs.

### 2.5 Synthesis: The Missing Methodological Object

Across these streams, prior research studies data sources, measures, auditors, audit analytics tools, AI adoption, or model capability. The missing methodological object is the retrieval-created information environment in LLM-based audit research. Retrieval systems sit between data and LLM output. They determine what the model sees, how reported information is represented, whether sources are traceable, and whether output differences can be separated from retrieval effects. This paper fills that gap by introducing retrieval-environment validity and by providing tools for retrieval design, claim-level correctness coding, failure-mode diagnosis, reporting, and sensitivity analysis.

## 3. Retrieval-Environment Validity

Retrieval-augmented LLM audit studies differ from fixed-information-set studies because the information environment observed by the model is dynamically constructed. The retriever selects information, ranks it, renders it into a context window, and may transform or omit materials before the model produces an output. This means that observed LLM behavior is a function of both the model and the retrieval-created information environment.

We define retrieval-environment validity as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. The concept asks whether the retrieval-created information environment permits the researcher to draw the intended inference from the LLM output.

### 3.1 Fixed Information Sets Versus Dynamic Retrieval

The methodological issue arises because retrieval-augmented LLM studies differ from traditional fixed-information-set designs.

| Traditional audit study information design | Retrieval-augmented LLM audit study |
|---|---|
| Researcher defines the information set before the study. | Retriever selects information at runtime. |
| Treatment materials are usually stable across participants or conditions. | Retrieved information may vary by query, index, ranking rule, traversal depth, model, or prompt. |
| Information content is directly inspectable before the study. | Information content may be selected, transformed, summarized, omitted, or reordered by the retrieval pipeline. |
| Output differences are interpreted in relation to participant judgment or treatment manipulation. | Output differences may reflect model behavior, retrieval quality, or model-retrieval interaction. |
| Documentation focuses on experimental materials. | Documentation must include retrieval source, unit, operator, ranking, traversal, context rendering, logs, and source mappings. |

### 3.2 Five Dimensions

Retrieval-environment validity has five dimensions:

1. **Selection validity:** whether retrieval selects information relevant to the intended audit construct.
2. **Representation validity:** whether retrieved information is faithfully represented to the LLM.
3. **Stability:** whether equivalent retrieval conditions produce consistent information environments.
4. **Traceability:** whether output claims can be linked to retrieved information.
5. **Separability:** whether model behavior can be distinguished from retrieval-created information environment effects.

These dimensions adapt established audit and research design concerns--relevance, reliability, reproducibility, documentation, and internal validity--to the dynamic retrieval setting. Selection concerns what enters the information environment. Representation concerns how it is rendered. Stability concerns whether it is reproducible. Traceability concerns whether output claims can be linked back to retrieved materials. Separability concerns whether observed output differences can be attributed to model behavior, retrieval design, or their interaction.

| Dimension | Audit/Method Anchor | Core Question |
|---|---|---|
| Selection validity | Relevance | Did retrieval select construct-relevant information? |
| Representation validity | Reliability / faithful representation | Was retrieved information accurately represented to the LLM? |
| Stability | Reproducibility | Would equivalent retrieval conditions produce similar information environments? |
| Traceability | Documentation / support | Can output claims be traced to retrieved sources or relation paths? |
| Separability | Internal validity | Can researchers distinguish model behavior from retrieval-created environment effects? |

### 3.3 Audit Constructs

For this paper, an audit construct is the audit-relevant capability, judgment, or reasoning object that the researcher claims to study through LLM outputs. Examples include narrative disclosure comprehension, reported relation preservation, narrative-numeric integration, assertion mapping, risk cue identification, calculation consistency reasoning, and evidence traceability.

The framework does not evaluate whether an LLM performs an audit procedure. It evaluates whether the retrieval-created information environment supports the audit-relevant construct the researcher claims to study.

## 4. Retrieval Designs for LLM Audit Research

Retrieval-environment validity requires researchers to specify how retrieval design creates the information environment observed by the LLM. We distinguish four retrieval designs: LLM-only, text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval.

A retrieval condition is not defined by the final prompt alone. It is defined by source, unit, operator, representation, and controls.

| Retrieval Design | Retrieval Operator | Information Environment | Best-Suited Construct | Key Risk |
|---|---|---|---|---|
| LLM-only | None | Prompt and model-internal information | Baseline model reasoning | Pretraining contamination |
| Text-based contextual retrieval | Semantic similarity or keyword search | Narrative disclosures | Narrative comprehension | Relation hallucination |
| XBRL-based relational retrieval | Typed accounting-relation selection or traversal | Reported accounting relationships | Reported relation preservation | Source overreach |
| Hybrid retrieval | Text retrieval plus relation retrieval | Narrative text and reported relationships | Narrative-numeric integration | Reduced separability |

### 4.1 LLM-Only Baseline

An LLM-only condition provides no external retrieved information. It is useful as a diagnostic baseline for traceability and possible pretraining contamination. However, it provides weak source traceability and cannot support claims about retrieval-supported reasoning.

### 4.2 Text-Based Contextual Retrieval

Text-based contextual retrieval selects narrative text chunks using semantic similarity, keyword search, or another text ranking method. It is well suited for constructs such as narrative disclosure comprehension, policy interpretation, and qualitative risk cue identification. Its primary validity risk is omission of structured accounting relationships.

### 4.3 XBRL-Based Relational Retrieval

XBRL-based relational retrieval selects information through typed accounting-relation traversal or selection over XBRL facts, concepts, contexts, dimensions, units, and linkbase relations. It is well suited for constructs such as reported relation preservation, calculation consistency, taxonomy extension interpretation, and relation hallucination detection.

XBRL-based retrieval must be bounded carefully. XBRL encodes management-coded reported accounting relationships. These relationships may be relevant to audit constructs, but they are not independent audit evidence and are not equivalent to audit assertions.

### 4.4 Hybrid Retrieval

Hybrid retrieval combines text-based contextual retrieval and XBRL-based relational retrieval. It is appropriate when the construct explicitly involves narrative-numeric integration. Hybrid retrieval may provide richer context, but it reduces separability because text and relation effects are jointly introduced. A hybrid condition should therefore be interpreted alongside text-only and XBRL-only conditions when possible.

### 4.5 Inferential Permissions

Each retrieval design permits different inferences. Text retrieval supports claims about narrative traceability. XBRL retrieval supports claims about reported relation traceability. Hybrid retrieval supports claims about integration only when the output actually reconciles narrative, structured reported facts, and audit reasoning. No retrieval condition by itself permits conclusions that an audit assertion is satisfied or that a misstatement exists.

| Retrieval Design | Permitted Inference | Inference Not Permitted Without Additional Evidence |
|---|---|---|
| LLM-only | How the model responds without external retrieval under the specified prompt. | That the model used reliable audit-relevant information. |
| Text-based contextual retrieval | How narrative context supports LLM output claims. | That the model preserved structured accounting relations. |
| XBRL-based relational retrieval | How reported accounting relationships support or constrain LLM claims. | That the model made audit-valid judgments or obtained independent audit evidence. |
| Hybrid retrieval | How the model integrates narrative and reported relational information. | That hybrid retrieval is generally superior or that text and relation effects are separable. |

## 5. Claim-Level Correctness and Failure Modes

Evaluating LLM audit outputs requires more than classifying responses as right or wrong. Retrieval designs create different information environments, and those environments support different types of claims. We therefore propose a claim-level correctness protocol.

The unit of analysis is a claim: a discrete assertion in an LLM output that can be evaluated for support, validity, or reasoning quality. A single response may contain factual claims, reported relationship claims, risk cue claims, assertion mapping claims, explanations, and conclusions. These claims may differ in their evidence basis.

### 5.1 Four Correctness Layers

The protocol distinguishes four layers:

1. **Text-supported correctness:** whether the claim is supported by retrieved narrative disclosure text.
2. **Graph-valid correctness:** whether the claim matches retrieved XBRL facts or relation paths.
3. **Audit-valid correctness:** whether the claim is professionally reasonable as audit reasoning.
4. **Integrated correctness:** whether text support, graph validity, and audit logic are mutually consistent.

Audit-valid correctness is expert-coded judgment, not objective ground truth. Integrated correctness is not an average of the other layers. It asks whether the evidence layers are reconciled in the claim.

| Layer | Coding Question | Primary Evidence Source | Main Risk |
|---|---|---|---|
| Text-supported correctness | Is the claim supported by retrieved disclosure text? | Text chunks, footnotes, MD&A, policies | Narrative overreach |
| Graph-valid correctness | Does the claim match retrieved XBRL facts or relation paths? | XBRL concepts, facts, dimensions, relation paths | Relation hallucination |
| Audit-valid correctness | Is the claim professionally reasonable as audit reasoning? | Expert auditor judgment | Source overreach |
| Integrated correctness | Are text, graph, and audit logic mutually consistent? | Combined review | Integration failure |

### 5.2 Failure Modes

The failure mode taxonomy links output problems back to retrieval-environment validity. Omission threatens selection validity. Distortion threatens representation validity. Retrieval instability threatens reproducibility. Attribution failure threatens traceability. Model-retrieval confounding threatens separability. Relation hallucination, source overreach, and integration failure are especially important for XBRL and hybrid retrieval.

The key methodological point is that correctness layers can diverge. A claim can be graph-valid but audit-invalid if it treats management-coded XBRL relations as audit evidence. A claim can be useful but not integrated if it appears in a hybrid condition but relies only on text or only on XBRL.

## 6. Methodological Guidance and Reporting

The framework is useful only if researchers can apply it. We therefore provide reporting and reproducibility guidance that scales with the study's claims.

### 6.1 Tiered Reporting Standard

Tier 1 applies to descriptive methodological demonstrations. Researchers should disclose retrieval units, operators, source IDs, context budgets, prompts, logs, claim coding, and selected spot-checks. Tier 2 applies to empirical LLM audit studies using RAG and requires additional embedding/index metadata, sensitivity checks, expert coding, and reliability evidence. Tier 3 applies to retrieval-system or GraphRAG evaluations and requires benchmark design, retrieval metrics, system parameters, and scalability or latency evidence.

The current paper's demonstration is a Tier 1 methodological demonstration. It should not be read as a performance benchmark for vector RAG or graph databases.

### 6.2 Implementation Transparency

For text retrieval, researchers should report source document records, chunk schema, chunking rule, chunk size, overlap, embedding model when used, vector index when used, similarity metric, top-k, reranking policy, and retrieval logs.

For XBRL relation retrieval, researchers should report fact tables, concept identifiers, relation edge/path tables, taxonomy and linkbase sources, taxonomy version, extension-concept handling, traversal depth, relation type filters, period/unit/dimension handling, and any RDF/OWL-compatible mapping.

The RDF/OWL layer should be presented as a portability and compatibility schema, not as a claim that XBRL becomes audit evidence. Researchers should distinguish XBRL-coded reporting relations from researcher-coded audit construct or assertion mappings.

### 6.3 Sensitivity Guidance

Recommended sensitivity checks include chunk size, chunk overlap, top-k, query wording, embedding model, reranking, traversal depth, relation type filters, extension concept inclusion, period and dimension filters, token budget equalization, prompt variation, model variation, and repeated retrieval stability.

These checks should be tied to validity dimensions. For example, top-k and traversal depth affect selection validity, relation rendering affects representation validity, repeated retrieval affects stability, source IDs affect traceability, and token budget equalization affects separability.

| Validity Dimension | Reporting Items That Operationalize It | Reviewer Question Addressed |
|---|---|---|
| Selection validity | Retrieval unit, query/seed, filters, top-k, traversal depth | Did the retriever select construct-relevant information? |
| Representation validity | Chunking rule, XBRL fact schema, relation edge schema, taxonomy version, dimensions | Was the selected information faithfully represented? |
| Stability | Retrieval logs, repeated retrieval checks, index metadata, taxonomy version | Would equivalent retrieval runs create the same information environment? |
| Traceability | Source IDs, prompt files, raw outputs, spot-checks | Can claims be traced back to retrieved information? |
| Separability | Context budgets, hybrid assembly rule, LLM-only baseline, token equalization | Can retrieval effects be distinguished from model or prompt effects? |

## 7. Methodological Demonstration

To illustrate how retrieval-environment validity changes the interpretation of LLM-based audit outputs, we conduct a descriptive demonstration using actual SEC filing text and Inline XBRL data. The purpose is not to rank retrieval methods or estimate model performance. Instead, the demonstration shows how the same audit task supports different research inferences depending on the retrieved information environment.

We use three familiar SEC filers: Nike, Starbucks, and Target. Familiar firms make output claims easier for readers to interpret, but they also increase the risk that the model may rely on general pretraining knowledge. We therefore evaluate claims only against retrieved filing text, retrieved XBRL facts and relation paths, and a no-context diagnostic baseline.

The main run uses `gemma4:31b` through local Ollama with temperature set to zero. The run covers three filers, two audit constructs, and four retrieval conditions: text-only retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline. The full run produced 24 outputs and 94 segmented claims. The coding is preliminary author coding and requires expert review before final audit-valid and integrated correctness claims.

### 7.1 Implementation Summary

The demonstration uses an inspectable prototype. Text retrieval is keyword-ranked contextual retrieval over extracted 10-K chunks. XBRL retrieval uses extracted fact tables and direct relation paths from Inline XBRL and linkbase data. The demonstration does not claim to implement production vector RAG, RDF/OWL triple-store retrieval, or graph database performance. Instead, the appendix reports how those data structures should be disclosed when used.

### 7.2 Selected Examples

Table 8 reports selected examples chosen to illustrate pre-specified divergence patterns: integrated corroboration, XBRL-only use inside hybrid retrieval, text-only use inside hybrid retrieval, no-context diagnostic behavior, and additional filer coverage. The selected examples are illustrative rather than exhaustive; the full 94-claim coding table should be retained in the appendix or supplemental materials so readers can evaluate the broader coding trail.

| Example | Claim ID | Filer | Construct | Condition | Claim Summary | Text Source | XBRL Source | Text | Graph | Audit | Integrated | Inference Consequence |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| E01 | C058 | Starbucks | Inventory | Hybrid | Inventory reserves were $56.6 million as of September 28, 2025. | T-SBUX-INVENTORY-015 | F-SBUX-0034 | 1 | 1 | 1 | 1 | Hybrid retrieval supports direct narrative-XBRL corroboration for a bounded factual claim. |
| E02 | C013 | Nike | Revenue | Hybrid | Refund liability increased from $799 million to $1.277 billion and may be a revenue valuation risk cue. | None | F-NKE-0253; F-NKE-0252 | 0 | 0.5 | 1 prelim. | 0.5 | The claim is graph-grounded but effectively XBRL-only despite the hybrid condition. |
| E03 | C014 | Nike | Revenue | Hybrid | Digital commerce platform failure risk may map to revenue completeness and occurrence. | T-NKE-REVENUE-021 | None | 0.5 | NA | 1 prelim. | 0.5 | The claim is text-supported but does not use XBRL despite the hybrid condition. |
| E04 | C016 | Nike | Revenue | LLM-only | Context is insufficient to identify filing-specific revenue risk cues. | None | None | NA | NA | 1 | NA | The no-context baseline supports traceability diagnosis rather than performance comparison. |
| E05 | C090 | Target | Inventory | Hybrid | Net inventory was $12.740 billion as of February 1, 2025. | None | F-TGT-0007 | 0 | 1 | 1 prelim. | 0.5 | The claim is graph-grounded but does not integrate the available Target inventory narrative context. |

Note: Audit-valid and integrated scores marked preliminary require expert review before final manuscript claims.

The first example shows the constructive role of hybrid retrieval. In the Starbucks inventory case, the model identifies a reported inventory reserve amount and cites both a narrative disclosure and a matching XBRL fact. The valid inference is narrow: hybrid retrieval can support direct narrative-XBRL corroboration for a bounded reported amount.

The second, third, and fifth examples show why hybrid retrieval should not be interpreted as automatically superior. In the Nike revenue and Target inventory cases, the model receives both narrative and XBRL context, but individual claims rely on only one evidence layer. These claims may be useful, but they do not demonstrate integrated reasoning. A naive evaluation might label them successful hybrid outputs. The correctness protocol leads to a different inference: the hybrid condition created an opportunity for integration, but the claim-level evidence use remained separated.

The fourth example illustrates the role of the LLM-only baseline. When no retrieved filing context is provided, the model states that the context is insufficient to identify filing-specific revenue risk cues. This output should not be interpreted as model failure. It functions as a traceability diagnostic.

Overall, the demonstration shows that retrieval design changes the evidence basis of LLM audit claims. Text retrieval supports narrative traceability, XBRL retrieval supports reported-relation traceability, and hybrid retrieval supports integrated correctness only when the model actually uses both evidence layers in the same claim.

## 8. Discussion and Boundary Conditions

The framework has several boundary conditions.

First, retrieval-environment validity is not a new general theory of validity. It is a diagnostic lens for construct validity in studies where retrieval systems dynamically create the information environment observed by LLMs.

Second, XBRL-based relational retrieval does not convert XBRL into audit evidence. XBRL facts and relations are reported accounting information. They may support graph-validity, reported relation preservation, or narrative-numeric consistency checks, but they do not establish that an audit assertion is satisfied.

Third, hybrid retrieval is not universally superior. It supports a different construct: integration of narrative and reported relational information. Hybrid retrieval can reduce separability because output differences may reflect more total information, different ordering, or interaction between text and relation context.

Fourth, the current demonstration is descriptive. It illustrates inference shifts rather than testing a hypothesis about model performance. Hypothesis-testing studies should use fuller sensitivity checks, expert coding, reliability evidence, and stronger controls over token budget and retrieval variation.

Fifth, audit-valid correctness requires professional judgment. Text support and graph validity are not substitutes for audit reasoning or evidence sufficiency.

## 9. Conclusion

LLM-based audit research increasingly depends on retrieval systems that construct the information environment observed by the model. This paper argues that retrieval should be treated as part of research design. Without specifying and validating retrieval-created information environments, researchers risk drawing conclusions about LLM capability, audit reasoning, or construct performance that are actually driven by retrieval selection, representation, instability, weak traceability, or model-retrieval confounding.

We introduce retrieval-environment validity as a diagnostic lens for this problem and operationalize it through retrieval designs, correctness layers, failure modes, reporting guidance, and a descriptive SEC/XBRL demonstration. The central lesson is not that one retrieval design is best. The lesson is that different retrieval designs support different inferences. Audit researchers should therefore align retrieval design with the intended construct, evaluate output claims at the appropriate correctness layer, and report retrieval environments transparently.

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

1. Finalize reference details and citation style for the target journal.
2. Decide final journal and formatting style.
3. Convert draft tables into polished manuscript tables and figures.
4. Obtain expert review for selected audit-valid and integrated correctness scores.
5. Prepare the full 94-claim table for appendix or supplemental materials.
6. Add final source/retrieval package appendix.
7. Review manuscript for overclaiming around XBRL, hybrid retrieval, and LLM capability.
