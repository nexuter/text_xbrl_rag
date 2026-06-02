## Title

Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval

## Abstract

Retrieval-augmented large language models are increasingly used in accounting and auditing research, but the retrieved information environment is often under-specified even though it determines what evidence the model observes. We introduce retrieval-environment validity: the extent to which the information dynamically retrieved for an LLM aligns with the audit construct a researcher intends to study. The framework gives reviewers and researchers a practical decision rule: before interpreting an LLM output, determine whether retrieval selected construct-relevant evidence, preserved source meaning, produced stable and traceable materials, and separated retrieval effects from model or prompt effects. We operationalize the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting guidance, and an SEC/XBRL-based methodological demonstration. The nine-filer protocol-validation package, with 72 retrieval-conditioned outputs and 281 preliminary coded claims, illustrates claim-level source-use heterogeneity: within this design, 8 of 89 hybrid claims used both text and XBRL, while 61 used text only and 20 used XBRL only. A 120-claim independent coding sample provides reliability evidence for source-use and integration variables. The paper provides guidance for designing, evaluating, and reporting LLM-based auditing research while preserving the boundary between management-reported XBRL, public filing support, and audit evidence sufficiency.

## Declaration Of Generative AI And AI-Assisted Technologies In The Writing Process

The authors used generative AI and AI-assisted tools to support manuscript drafting, editing, code development, and organization of reproducibility materials. The authors reviewed, revised, and are responsible for all manuscript content, analyses, source interpretations, and conclusions. The use of LLMs as part of the methodological demonstration is described in the demonstration section and supporting appendix materials.

## I. INTRODUCTION

Large language models (LLMs) are increasingly being studied in accounting and auditing research. Many research designs augment these models with external information through retrieval-augmented generation. In these designs, the model may receive financial filing text, accounting standards, structured reporting data, audit-workpaper-like materials, or other domain-specific sources before generating a response. The methodological problem is direct: retrieval determines the evidence environment the model observes, yet it is often described as implementation detail.

This paper contributes to auditing research methodology by treating retrieval as a research-design and data/variable-construction problem in LLM-based auditing studies. A retrieval system does not merely add information to a prompt. It constructs the information environment from which the model generates its response. It selects sources, ranks source units, traverses relations, filters contexts, truncates materials, formats retrieved materials, and determines which parts of the source corpus are visible to the model. When researchers evaluate LLM outputs without logging and evaluating this retrieval-created information environment, they may attribute differences in outputs to model capability, prompt quality, or audit reasoning when those differences arise from retrieval design.

This is not an abstract implementation concern. A revenue-recognition prompt using top-5 text chunks may retrieve generic risk-factor language while omitting contract-liability disclosures, refund-liability amounts, or performance-obligation policy language. Increasing top-k may add relevant evidence, but it also changes the model's context volume. Adding XBRL relation paths may reveal reported links among concepts, but relation depth and filtering choices determine which paths the model sees. These retrieval choices create the effective information set for the LLM and therefore shape the research inference.

This distinction matters because audit research constructs depend on the source, nature, and evidentiary status of information. Narrative disclosures may support analysis of management explanations, accounting policy language, or disclosed risk cues. XBRL tags, facts, contexts, and linkbase relations may support analysis of management-reported accounting relationships. Neither source is equivalent to audit evidence. A claim can be supported by retrieved text and consistent with XBRL facts while still overstating what the evidence can support as audit reasoning. Conversely, a response can appear weak because the retrieval pipeline failed to supply construct-relevant information.

We introduce retrieval-environment validity as a diagnostic framework for this problem. Retrieval-environment validity is the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct the researcher intends to study. The concept does not replace construct validity, nor do we present it as a general theory of RAG evaluation. We use it as an audit-specific organizing framework for retrieval-related construct drift: it identifies a retrieval-specific mechanism through which construct validity can fail in studies where the model's information set is created at runtime.

[Insert Figure 1 about here]

The paper's central research question is:

> How does retrieval design affect the validity of inferences drawn from LLM-based auditing research?

The central empirical motivation is claim-level evidence divergence. In the demonstration reported below, responses labeled "hybrid" had access to both narrative and structured materials, but individual claims frequently used only one layer in this implementation. This is exactly the kind of validity issue that response-level accuracy or condition labels can miss. An audit researcher needs to know not only that the model answered, but what evidence environment the answer was drawn from and what claim-level inference that evidence supports.

The framework therefore separates claim layers early. A claim about an inventory reserve can be text-supported when the retrieved footnote states the policy or amount, graph-valid when retrieved XBRL facts preserve the concept, period, unit, and value, audit-boundary relevant when the claim maps that evidence to valuation risk, and integrated only when the claim uses narrative and structured evidence together. The same claim would still fall short of an audit conclusion about reserve adequacy unless the study adds evidence and expert judgment appropriate to that claim.

[Insert Figure 1A about here]

The paper contributes to auditing research methodology in three ways. First, it defines retrieval-environment validity and identifies five dimensions: selection, representation, stability, traceability, and separability. Second, it operationalizes the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, tiered reporting guidance, and reproducibility standards. These tools speak directly to research design and data/variable construction for LLM-based auditing research by converting retrieval artifacts and model responses into reviewer-evaluable design evidence and study-level variables, including text-supported correctness, graph-valid correctness, preliminary audit-boundary diagnostics, integrated correctness, source-use type, and failure-mode labels. Third, it provides a methodological protocol-validation demonstration using SEC filing text and Inline XBRL data to document how different retrieval designs produce different observed claim-level source-use profiles.

The framework changes how researchers should design and evaluate LLM audit studies. Researchers should define the audit construct before retrieval, choose retrieval operators that fit that construct, preserve the retrieved information environment, evaluate output claims by correctness layer, distinguish management-reported XBRL relations from audit evidence, and report retrieval sensitivity proportional to the study's claims.

The intended users are auditing researchers who use LLMs as measurement tools, audit analytics researchers who compare retrieval or agent designs, and judgment-and-decision-making researchers who study LLM-assisted audit judgments. For these users, the framework provides a way to specify the evidence environment that an LLM observed before interpreting its output. It does not provide a shortcut for concluding that audit evidence is sufficient and appropriate. Studies that seek to make that stronger claim need audit-domain expert judgment, external or engagement-specific evidence, reliability procedures, and controls appropriate to the claim.

We illustrate the framework using a nine-filer, two-layer protocol-validation design. Three familiar SEC filers support deep source tracing and claim-level illustration; six additional filers provide a bounded applicability check across varied reporting environments. The demonstration's evidentiary contribution is that response-level retrieval labels are insufficient: claims within the same condition can rely on different source bases, and those differences affect which inferences are justified. A hybrid condition can produce integrated text-XBRL claims, but it can also produce claims that rely only on text, only on XBRL, or on insufficient retrieved materials. We report these patterns as protocol-validation evidence rather than as performance rankings or population failure rates.

The implemented prototype is intentionally inspectable: it uses keyword-ranked text chunks and table-based XBRL fact/path retrieval, while vector indexes, RDF/OWL stores, graph databases, and GraphRAG are treated as reporting guidance and portability extensions rather than completed performance systems.

Emerging LLM/RAG audit studies increasingly evaluate systems, agents, compliance verification, or task performance (Berger et al. 2025; Wang et al. 2025; Xing and Meng 2026; Xiong, Han, and Zhang 2024). Our focus is different: we provide criteria for auditing researchers to evaluate whether the retrieval-created information environment supports the inference they draw from LLM outputs.

The remainder of the paper proceeds as follows. Section II positions the paper relative to audit methodology, XBRL research, textual analysis, LLM accounting research, and audit analytics. Section III develops retrieval-environment validity. Section IV operationalizes retrieval designs for LLM-based auditing research. Section V presents the claim-level correctness protocol and failure modes. Section VI provides reporting guidance and reproducibility standards. Section VII presents the methodological demonstration. Section VIII discusses boundary conditions. Section IX concludes.

## II. RELATED LITERATURE AND METHODOLOGICAL POSITIONING

This paper sits at the intersection of audit research methodology, XBRL and structured reporting data, textual analysis and LLM accounting research, and audit analytics. The novelty is not the use of XBRL, text retrieval, or LLMs individually. The novelty is the shift in methodological unit of analysis: from text as data, XBRL as data, or models as objects of evaluation to retrieval as research design.

### Audit Methodology

AJPT has a tradition of publishing methodological guidance when emerging approaches require clearer criteria for design, evidence, inference, and evaluation. Prior methodological papers provide guidance for qualitative audit research, audit field research, judgment and decision-making research, and experimental research design (Power and Gendron 2015; Malsch and Salterio 2016; Griffith, Kadous, and Young 2016; Hatfield and Saiewitz 2022). This paper follows that tradition by addressing a newer class of audit studies: LLM-based auditing research in which information is supplied to the model through retrieval.

In many audit research designs, the researcher can define the information set before the study. In a laboratory experiment, for example, participants receive a known case packet. In an archival study, variables are constructed from specified source data and measurement rules. In retrieval-augmented LLM studies, however, the model's information set may be created dynamically at runtime. The researcher may define a corpus, a prompt, and a model, yet still not know what evidence the model actually received unless the retrieval environment is logged and validated. This creates a research-design problem that prior audit methodology has not directly addressed.

### XBRL And Structured Reporting Data

Prior XBRL research establishes structured reporting data as a useful source for accounting and auditing research. XBRL has been used to study reporting complexity, disaggregation, data usability, tagging choices, and implications for future audit research (Hoitash and Hoitash 2018; Hoitash, Hoitash, and Morris 2021; Johnston, Reichelt, and Sapkota 2024). This literature shows that XBRL data can support accounting measurement when researchers carefully specify concepts, tags, extensions, periods, contexts, and data-quality limitations.

This paper uses XBRL differently. We do not use XBRL primarily to construct firm-level archival variables. We use it as a structured retrieval environment that exposes management-reported accounting facts and relations to an LLM. XBRL relational retrieval can help researchers examine whether LLM outputs preserve, distort, hallucinate, or overread reported accounting relationships. Importantly, XBRL is not independent audit evidence or ground truth. It is management-reported structured accounting information that may be relevant to audit constructs but is not equivalent to audit assertions.

### Textual Analysis And LLM Accounting Research

Accounting textual-analysis research has long emphasized that text-based measures require careful preprocessing, construct alignment, validation, and reproducibility (Li 2010; Loughran and McDonald 2016; Bochkay et al. 2023; Bae, Hung, and van Lent 2023). Recent LLM accounting research extends this tradition by using generative models for textual analysis, financial statement analysis, financial reporting tasks, and output reproducibility studies (de Kok 2025; Blankespoor, deHaan, and Li 2026; Kim, Muhn, and Nikolaev 2024; Li and Vasarhelyi 2024; Wang and Wang 2025).

These studies provide important evidence about how LLMs process accounting and financial information. However, many LLM-based designs evaluate model outputs without separately validating the retrieved information environment that made those outputs possible. In retrieval-augmented studies, this omission matters. A model may appear strong because retrieval supplied direct evidence, or weak because retrieval omitted construct-relevant evidence. A study may compare prompts, models, or conditions when the effective treatment is the evidence environment created by retrieval.

Text retrieval is useful when the construct depends on narrative meaning, policy language, risk disclosure, or management explanation. However, text retrieval may omit structured accounting relationships central to some audit-relevant constructs. Conversely, XBRL relational retrieval may preserve reported relations while omitting narrative context. The present paper therefore distinguishes retrieval designs by source, unit, operator, and construct fit rather than treating all retrieved context as equivalent.

### RAG Evaluation And Evidence Traceability

Non-accounting RAG research provides important tools for evaluating retrieval and generation systems. The original RAG architecture combines parametric language-model memory with a retrieved non-parametric memory source for knowledge-intensive generation (Lewis et al. 2020). Recent RAG evaluation frameworks separately assess dimensions such as context relevance, answer faithfulness, and answer relevance (Es et al. 2024; Saad-Falcon et al. 2024). Evidence-attribution and citation-generation research similarly emphasizes that generated statements should be linked to identified sources, citation quality should be evaluated, and source support cannot be assumed from fluent model output (Rashkin et al. 2023; Gao et al. 2023). These studies are directly relevant because they show that retrieval quality, source attribution, and answer faithfulness should be evaluated rather than assumed.

Those literatures also clarify the gap this paper addresses. In general RAG or citation-generation settings, source support often asks whether a generated answer is grounded in a retrieved passage or cited document. In auditing research, source support is necessary but not sufficient. The researcher must also ask whether the retrieved source environment corresponds to the intended audit construct, whether the source is public management-reported information or audit evidence, whether structured XBRL relations preserve the accounting relationship being invoked, and whether the generated claim stays within the inference that those sources can support.

Our contribution is different. Generic RAG evaluation asks whether retrieved passages are relevant and whether generated answers are faithful to retrieved context. Retrieval-environment validity asks an audit-methodological question: whether the retrieved environment instantiates the audit construct required for the research inference. A RAG system can retrieve relevant passages, cite them, and produce faithful answers while still failing an audit research design if the retrieved materials omit construct-critical assertion evidence, overread management-reported XBRL as audit evidence, or confound source type with context volume, ordering, or prompt salience. This is why the framework links retrieval diagnostics to audit constructs, correctness layers, and reviewer decision rules rather than treating RAG quality metrics or citation support as sufficient for audit inference.

### Audit Analytics, Big Data, And AI In Auditing

Audit analytics and AI research examines how auditors and audit technologies process large, complex, or nontraditional data sources (Brown-Liburd, Issa, and Lombardi 2015; Yoon, Hoogduin, and Zhang 2015; Appelbaum, Kogan, and Vasarhelyi 2017, 2018; Fedyk et al. 2022). This literature shows that technology-enabled information environments matter for audit judgment, audit evidence, and audit process design. It also cautions that more data or more automation does not automatically produce better audit evidence.

Our paper is related but distinct. We do not propose an audit procedure, audit agent, or engagement workflow. We provide methodology for researchers studying LLM-based auditing tasks. The relevant object is not whether an LLM system can automate an audit procedure, but whether the retrieval-created information environment supports the inference a researcher draws from LLM outputs.

### Synthesis

Prior work studies data, tools, models, auditors, or outcomes. This paper studies the retrieval-created information environment that connects source data to LLM output in auditing research designs. Retrieval systems sit between data and output. They determine what the model sees, how retrieved materials are represented, whether sources are traceable, and whether output differences can be separated from retrieval-conditioned information differences. The paper therefore complements RAG evaluation and XBRL data-quality research but adds an audit-specific validity question: whether the retrieved environment supports the audit construct and inference being studied. This paper fills that gap by introducing retrieval-environment validity and by providing tools for retrieval design, claim-level correctness coding, failure-mode diagnosis, reporting, and sensitivity analysis.

## III. RETRIEVAL-ENVIRONMENT VALIDITY

Retrieval-augmented LLM audit studies differ from fixed-information-set studies because the information environment observed by the model is dynamically constructed. The retriever selects information, ranks it, renders it into a context window, and may transform or omit materials before the model produces an output. Observed LLM behavior is therefore a function of both the model and the retrieval-created information environment.

### Definition

We define retrieval-environment validity as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. The concept asks whether the retrieval-created information environment permits the researcher to draw the intended inference from the LLM output.

Retrieval-environment validity is grounded in construct validity, but existing validity language is not sufficient by itself because retrieval creates a dynamic materials boundary. In a fixed-information-set study, the researcher can define and inspect the information package supplied to a participant or model before inference. In a retrieval-augmented LLM study, the corpus, prompt, and model do not fully specify the information environment. The environment is created by a retrieval pipeline at runtime through source selection, ranking, relation traversal, context filtering, chunking, truncation, and formatting.

[Insert Table 1 about here]

Table 1 distinguishes fixed information sets from dynamic retrieval environments. In a fixed-information-set design, the researcher defines the evidence package before the study. In a dynamic retrieval design, the information boundary is constructed at query time. Replication therefore requires not only the prompt and model, but also the corpus, retrieval unit, retrieval operator, ranking or traversal rule, context rendering, and returned evidence logs.

### Relation To Adjacent Validity Concepts

Retrieval-environment validity is best understood as a retrieval-specific diagnostic lens for construct drift. It does not replace construct validity, measurement validity, internal validity, audit evidence sufficiency, RAG evaluation, XBRL data-quality assessment, or reproducibility. Instead, it identifies a mechanism through which those broader validity concepts can fail when the model's information set is created dynamically. A study can specify an appropriate audit construct, use a stable model, and report a complete prompt, yet still fail if retrieval supplies a different evidence environment from the one required by the construct.

[Insert Table 2 about here]

Table 2 distinguishes retrieval-environment validity from adjacent concepts. The key distinction is that conventional validity, information-set design, and documentation criteria often assume the researcher knows the information package supplied to the decision maker or model. In dynamic retrieval designs, that information package is an outcome of the retrieval pipeline. Conventional concepts govern whether the construct, measurement, case materials, documentation, and replication package are appropriate once the information set is known; retrieval-environment validity begins where the information set itself is created at query time. The inferential question therefore becomes not only whether the construct is well defined, but whether the retrieved materials actually instantiate the construct at runtime.

Two examples clarify the boundary. First, a study may claim to test revenue-recognition risk reasoning and may report the corpus, model, and prompt, but if the retriever supplies only generic risk-factor text and omits contract-liability disclosures, variable-consideration policy language, or related XBRL facts, the study has a retrieval-environment validity failure. The problem is not simply incomplete documentation; the model did not observe the evidence environment required by the construct. Second, a study may compare text, XBRL, and hybrid retrieval and attribute output differences to evidence type, but if hybrid prompts are longer, better labeled, or ordered differently, the study has a separability failure. The comparison confounds retrieval design with information volume and salience.

The framework is therefore evaluative, not only descriptive. A retrieval flaw is fatal to inference when it changes the construct being tested or prevents retrieval-conditioned information differences from being separated from model or prompt effects for a causal claim. It is fixable when logs, source identifiers, and retrieval parameters allow the researcher to reconstruct the environment and conduct bounded sensitivity checks. It is primarily a reporting gap when the study makes only illustrative claims and the omitted retrieval detail does not change the interpretation. These decision rules are intended to help reviewers distinguish between missing implementation detail and inference-threatening retrieval design.

[Insert Table 3 about here]

Table 3 translates retrieval-environment validity into reviewer decision rules. The purpose is not to make every retrieval limitation fatal. Instead, the table distinguishes inference-invalidating failures from design confounds, measurement threats, disclosure limitations, and acceptable boundaries. This distinction is central to the framework's incremental value: it helps audit researchers and reviewers decide whether a retrieval problem changes the study's conclusion, requires additional sensitivity analysis, calls for clearer measurement validation, or can be handled through transparent disclosure.

### Five Validity Dimensions

Retrieval-environment validity has five dimensions.

Selection validity concerns whether retrieval selects evidence relevant to the intended audit construct. A revenue-recognition risk task may require contract-liability disclosures, variable consideration policy language, and related reported amounts. If retrieval supplies only generic risk-factor text, output differences may reflect retrieval omission rather than model audit reasoning.

Representation validity concerns whether retrieved information preserves the meaning of source evidence. Text chunks can distort meaning by severing a sentence from its footnote context. XBRL facts can be distorted if concepts, periods, units, dimensions, decimals, or signs are omitted. Relation paths can be distorted if arcroles or linkroles are collapsed into generic edges.

Stability concerns whether equivalent runs would retrieve materially similar information environments. A study that makes claims about model behavior needs to show that observed outputs are not artifacts of unstable retrieval rankings, variable query wording, changing corpora, or undocumented index versions.

Traceability concerns whether each LLM claim can be traced to retrieved source evidence. This dimension is especially important in audit research because documentation and support are central to evaluating evidence. A claim that cannot be linked to a retrieved text chunk, XBRL fact, or relation path should not be treated as retrieval-supported.

Separability concerns whether retrieval-conditioned information differences can be separated from model effects. If the text condition receives 500 words and the hybrid condition receives 1,500 words, output differences may reflect information volume rather than source type. If prompts, models, temperatures, or task wording differ across conditions, researchers cannot attribute output differences to retrieval design alone.

[Insert Table 4 about here]

Table 4 summarizes the five dimensions, their audit or method anchors, observable evidence, and associated failure modes. The table makes retrieval-environment validity usable as a reviewer-facing diagnostic framework rather than only a conceptual label.

## IV. RETRIEVAL DESIGNS FOR LLM-BASED AUDITING RESEARCH

Retrieval design should follow the intended audit construct. The same source corpus can support different research claims depending on the retrieval unit, operator, and evidence status. The relevant question is not whether retrieval adds information, but whether the retrieved information environment aligns with the construct being studied.

### Retrieval Typology

We distinguish four retrieval designs: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval.

LLM-only designs provide no external retrieved context. They can serve as diagnostic baselines for pretraining knowledge, task wording, and traceability. They should not be treated as audit evidence because the model's response is not source-linked.

Text retrieval supplies narrative evidence such as filings, audit documents, standards, or workpaper-like materials. Its retrieval unit is typically a text chunk. Its operators may include keyword search, semantic similarity, hybrid search, filtering, or reranking. Text retrieval is well suited to narrative disclosure interpretation, accounting policy language, management explanation, and qualitative risk cues.

XBRL relational retrieval supplies structured facts, contexts, concepts, units, and linkbase relations. Its retrieval unit may be a fact, concept, edge, or relation path. Its operators may include concept lookup, seed-pattern selection, relation traversal, taxonomy filtering, or ontology query. XBRL relational retrieval is well suited to studying reported accounting relationships, numeric traceability, and whether LLM outputs preserve management-reported structure.

Hybrid retrieval supplies narrative and structured retrieved materials together. It is appropriate when the intended construct requires narrative-numeric integration. However, a hybrid condition is not automatically superior. It can produce integrated claims, but it can also produce text-only claims, XBRL-only claims, or juxtaposed materials without synthesis.

[Insert Table 5 about here]

Table 5 defines these retrieval designs by source, unit, operator, audit use, and risk.

### Mechanics Example

A simple mechanics example shows why retrieval design is part of research design rather than only implementation. Consider an inventory valuation prompt for one filer. In a text-retrieval condition, the corpus is first segmented into source-linked chunks. The retrieval operator ranks chunks using the construct query, applies any filer or section filters, and renders the top-k chunks into the prompt. If the design uses top-5 chunks, the model may see the inventory accounting policy, a reserve disclosure, and several generic risk paragraphs. If top-k is reduced to three, the reserve disclosure may drop out. If top-k is increased to eight, the model may receive more relevant context but also more total words, changing the prompt's information volume and salience.

The same task changes under XBRL relational retrieval. The retrieval operator starts from construct-relevant concept families, such as inventory balances, reserves, write-downs, cost flow, and inventory components. It then selects facts with period, unit, value, context, and dimension metadata and renders relation paths that preserve linkbase role, arcrole, source concept, target concept, and traversal information. If relation paths are omitted, the model may still see reported facts but lose the structured relationship among concepts. If relation filters or traversal depth change, the model may see a different accounting relationship environment. In a hybrid condition, both text chunks and XBRL fact/path bundles are rendered together, so researchers must also document source order, token budget, and whether claims actually integrate the two layers.

This example illustrates the mechanism behind the paper's validity dimensions. Top-k and relation traversal affect selection; chunking and XBRL context rendering affect representation; stable source identifiers affect traceability; repeated or perturbed retrieval affects stability; and matched context budgets affect separability. Appendix B documents the text retrieval store, Appendix C documents the XBRL fact/path and construct-coverage store, and Appendix I reports the bounded perturbation diagnostics used in the demonstration.

### Construct-To-Retrieval Mapping

Different audit constructs require different retrieval environments. Understanding narrative disclosure generally requires text retrieval. Preserving reported accounting relationships may require XBRL relational retrieval. Connecting narrative risk language to reported amounts may require hybrid retrieval. Identifying assertion-level risk cues may require hybrid retrieval plus explicit audit coding. Detecting misstatement, fraud, or internal control failure requires evidence beyond management-reported filings and cannot be established from XBRL relations alone.

The demonstration uses two ex ante construct protocols. For revenue recognition risk, the protocol asks whether retrieved public filing text and XBRL materials support source-traceable analysis of revenue policies, contract liabilities, variable consideration, refund or return obligations, disaggregation, and performance-obligation timing. The assertion-relevant focus is occurrence, completeness, accuracy, cut-off, and classification, but the demonstration does not test whether revenue is materially misstated. For inventory valuation assertion, the protocol asks whether retrieved materials support source-traceable analysis of inventory balances, reserves, write-downs, costing methods, obsolescence cues, and related reported amounts. The assertion-relevant focus is valuation, existence, completeness, and presentation, but the demonstration does not test physical inventory existence, realizable value, or management bias. This boundary follows the audit-standard distinction between assertion-level risk assessment and the need for sufficient appropriate audit evidence before reaching an audit conclusion (PCAOB 2024a, 2024b, 2024c).

For the current public-reporting demonstration, task success is therefore deliberately bounded. A successful revenue-recognition response identifies source-traceable disclosure language or XBRL-reported facts that are assertion-relevant to revenue timing, amount, classification, or completeness, while avoiding claims that revenue is misstated, noncompliant, fraudulent, or audit-verified. A successful inventory response identifies source-traceable policy language, reported balances, reserves, write-downs, or cost-flow information that is assertion-relevant to inventory valuation or presentation, while avoiding claims about physical existence, reserve adequacy, net realizable value, management bias, or audit evidence sufficiency. In this sense, the demonstration evaluates assertion-relevant reasoning from public reporting data, not audit-valid reasoning in an engagement evidence environment.

These protocols make construct-to-retrieval alignment evaluable before LLM output is interpreted. Text retrieval is expected to provide policy language, risk cues, and management explanations. XBRL relational retrieval is expected to provide reported facts, periods, units, contexts, concepts, and relation paths. Hybrid retrieval is expected to create an opportunity for narrative-numeric integration. None of these retrieval environments, by itself, provides audit evidence sufficiency.

For XBRL relational retrieval, construct alignment also requires a coverage diagnostic before model outputs are interpreted. We therefore map retrieved XBRL facts and relation paths to ex ante concept families for each construct. For revenue, the diagnostic considers revenue or sales amounts, contract liabilities or deferred revenue, refunds/returns or variable consideration, receivables or collectibility, and disaggregation or customer dimensions. For inventory, it considers inventory balances, inventory components, valuation reserves or obsolescence, cost flow or COGS, and inventory movements. Appendix C reports this diagnostic for all nine filers and 18 construct-filer cells and includes a worked NKE inventory example linking raw facts, relation paths, rendered context, LLM claims, and coding outcomes. The diagnostic is intentionally conservative: missing concept families are treated as retrieval-design boundaries, not as evidence of misstatement, non-disclosure, or model error.

[Insert Table 6 about here]

Table 6 operationalizes construct-to-retrieval alignment. The "what not to claim" column is as important as the recommended retrieval design because it prevents construct drift. A study can use XBRL relational retrieval to evaluate graph-valid reported relationships; it should not claim that XBRL alone verifies audit assertions. A study can use hybrid retrieval to study narrative-numeric integration; it should not claim that hybrid retrieval automatically improves reasoning.

## V. CLAIM-LEVEL CORRECTNESS AND FAILURE MODES

Response-level accuracy is too coarse for LLM-based auditing research because a single response may contain claims supported by different evidence bases. One claim may be directly supported by retrieved text. Another may be graph-valid against XBRL facts. A third may make an audit inference that exceeds both sources. A fourth may use no retrieved evidence despite being produced under a retrieval condition.

The protocol therefore separates five levels of evidentiary interpretation. At the first level, a claim may have public-filing support because retrieved SEC filing text supports the statement. At the second level, a claim may have XBRL graph or reporting support because it is consistent with management-reported XBRL facts, contexts, and relation paths. At the third level, a claim may have assertion relevance because it relates to an audit assertion or risk area. At the fourth level, an audit-boundary diagnostic asks whether the claim stays within what public filing text and management-reported XBRL materials can support. The fifth level, audit evidence sufficiency, requires evidence sufficient and appropriate for an audit conclusion. The current demonstration reaches the first four levels as a methodological diagnostic; it does not establish audit evidence sufficiency.

### Claim As The Unit Of Analysis

We define a claim as a separable assertion in an LLM output that can be evaluated against retrieved evidence and the intended audit construct. Claim-level analysis is necessary because retrieval-condition labels do not determine claim-level evidence use. A response labeled "hybrid" may contain integrated claims, text-only claims, XBRL-only claims, unsupported claims, or insufficient-context statements.

### Correctness Layers

We propose four correctness layers.

Text-supported correctness asks whether a claim is supported by retrieved narrative text. A claim can be text-supported if the cited or used text provides sufficient support for the claim's content.

Graph-valid correctness asks whether a claim is consistent with retrieved XBRL facts or relation paths. This includes checking concept, value, period, unit, context, and relation structure.

Audit-boundary diagnostics ask whether the inference is appropriate for the audit construct given the evidentiary limits of the retrieved materials. This layer requires professional judgment when used for stronger audit-judgment claims. A claim may be text-supported and graph-valid but still exceed the audit boundary if it treats management disclosure as audit evidence or overstates what the reported data can support.

Integrated correctness asks whether a hybrid claim uses text and XBRL evidence together without contradiction. A claim is not integrated merely because text and XBRL were both available in the prompt. Integration requires an inferential bridge between evidence types.

[Insert Table 7 about here]

Table 7 summarizes these layers. The key methodological point is that correctness is claim-type specific. Researchers should not collapse text support, graph validity, audit-boundary diagnostics, and integration into a single answer-level score.

This hierarchy also clarifies what the paper does not claim. Text-supported and graph-valid claims can support public-reporting analysis and assertion-relevant diagnostics, but they should not be treated as audit conclusions without additional audit evidence, professional judgment, and expert validation procedures.

A compact example illustrates the audit-specific boundary. Suppose a retrieved inventory footnote states that inventory reserves increased, and retrieved XBRL facts show the reserve amount, period, unit, and relation path. A claim that the reserve increased can be text-supported and graph-valid. A claim that the increase is relevant to the inventory valuation assertion can be an assertion-relevant audit-boundary diagnostic. But a claim that inventory is fairly valued, that reserves are sufficient, or that management bias exists would require evidence beyond management-reported filings, such as audit procedures, external corroboration, professional judgment, and expert validation. The same retrieved evidence can therefore be useful for audit research measurement while remaining insufficient for an audit conclusion.

### Failure Modes

The claim-level protocol also supports failure-mode diagnosis. Omission occurs when relevant source material exists but is not retrieved. Distortion occurs when retrieved material loses its source meaning. Retrieval instability occurs when similar queries return materially different retrieved environments. Attribution failure occurs when an output claim cannot be traced to retrieved materials. Model-retrieval confounding occurs when output differences cannot be attributed to retrieval design. Relation hallucination occurs when the model invents or misstates XBRL relations. Source overreach occurs when the model treats management-reported XBRL as audit evidence. Integration failure occurs when a hybrid condition presents text and XBRL materials but the claim does not reason across them.

The taxonomy is reported in Appendix Table F2. It links failure modes to retrieval-environment validity dimensions and design responses.

## VI. REPORTING GUIDANCE AND REPRODUCIBILITY STANDARDS

The framework is useful only if researchers can apply it. The reporting guidance is therefore organized around evidentiary tiers rather than a flat parameter inventory. A methodological demonstration, an empirical LLM audit study, and a retrieval-system benchmark do not need the same evidence. They do need a clear match between what the study claims and what retrieval artifacts it preserves.

### Design Guidance

The framework changes LLM-based auditing research design in six practical ways. Researchers should define the audit construct before choosing a retrieval method. They should choose retrieval operators that match the construct: text retrieval for narrative meaning, XBRL relational retrieval for reported accounting structure, and hybrid retrieval for narrative-numeric integration. They should preserve the retrieved materials actually supplied to the LLM, including retrieved chunks, facts, relation paths, prompts, and context rendering. They should evaluate LLM outputs at the claim level rather than only at the response level. They should distinguish reported XBRL relations from audit evidence and avoid converting graph-valid claims into audit-boundary or audit-judgment conclusions without professional judgment. Finally, they should report sensitivity checks proportional to the claims they make about retrieval, model behavior, and audit constructs.

[Insert Table 8 about here]

Table 8 summarizes this tiered logic. Tier 1 asks whether the retrieval environment can be specified, preserved, and linked to claim-level source use. Tier 2 asks whether retrieval-supported LLM outputs can support empirical audit-research claims under stronger sensitivity, coding, and reliability requirements. Tier 3 asks whether a retrieval architecture or GraphRAG system can be evaluated as a system against benchmarks or gold labels. The table is intended as a claim-evidence calibration device: stronger claims require stronger retrieval and validation evidence.

The current paper's demonstration is a Tier 1 methodological demonstration. It should not be read as a performance benchmark for vector RAG, graph databases, or LLM audit expertise.

### Implementation Transparency

Implementation transparency rests on three artifacts. The first is a source inventory: source documents, text chunks, XBRL facts, relation paths, taxonomy/linkbase sources, and stable identifiers. The second is a retrieval recipe: chunking and ranking rules for text, concept-family selection and relation traversal for XBRL, metadata filters, context budgets, and rendering rules. The third is an output linkage file: prompts, returned source identifiers, raw outputs, and claim-level coding that allow a reader to reconstruct what the model observed before each claim was evaluated.

Appendix I provides field-level schemas for researchers who want to implement the approach. In the main text, the methodological point is narrower: a reader should be able to identify the source universe, the retrieval operator, the retrieved environment shown to the model, and the claim-level evidence link. RDF/OWL-compatible representations can improve portability and interoperability, but they should be presented as representation choices rather than as evidence that XBRL becomes audit evidence. Researchers should distinguish XBRL-coded reporting relations from researcher-coded audit construct or assertion mappings.

### Sensitivity Guidance

Sensitivity analysis should be proportional to the inference. A study that only illustrates a protocol can report bounded retrieval-stage diagnostics, as this paper does. A study that claims one retrieval design improves LLM audit output quality should add matched-budget reruns, evidence-order variation, prompt sensitivity, retrieval-parameter variation, model variation where relevant, and expert or human coding appropriate to the claim. The choice of sensitivity check should map to a validity dimension: top-k and traversal depth affect selection, relation rendering affects representation, repeated retrieval affects stability, source identifiers affect traceability, and token-budget equalization affects separability. Appendix I reports the completed Tier 1 diagnostics and separates them from checks required for stronger Tier 2 or Tier 3 claims.

## VII. METHODOLOGICAL DEMONSTRATION

The demonstration provides protocol-validation evidence rather than model-performance evidence. To illustrate how retrieval-environment validity can change the interpretation of LLM-based audit outputs, we use actual SEC filing text and Inline XBRL data to construct, preserve, and inspect retrieval-created information environments. The purpose is not to rank retrieval methods or estimate model performance. The purpose is to show that retrieval environments can be specified, logged, reconstructed, and linked to claim-level source use, and that those source-use differences help determine what researchers can validly infer from LLM-generated audit claims.

The Tier 1 demonstration is successful if the retrieval environment can be reconstructed, source identifiers resolve to preserved materials, LLM outputs can be segmented into claim-level variables, central source-use and integration variables can be coded reliably, and remaining sensitivity boundaries are explicitly documented. These are protocol-validation criteria, not model-performance criteria.

[Insert Figure 2 about here]

Figure 2 summarizes the demonstration pipeline. We download SEC 10-K filings and Inline XBRL data, extract narrative text and structured facts, build text and XBRL retrieval contexts, run controlled prompts under retrieval conditions, segment responses into claims, and code claims using the correctness protocol.

The demonstration has four evidentiary layers, each with a different purpose. The three deep cases support source-tracing examples and claim-level illustration. The six extension cases test whether the same protocol can be maintained across varied reporting environments. The sensitivity diagnostics examine retrieval-stage source-composition and context-volume differences before model inference. The independent coding sample evaluates whether source-use and integration variables can be applied consistently. These layers jointly support protocol validation; none is used to estimate population prevalence, model performance, or retrieval-method superiority.

The demonstration therefore follows a Tier 1 transparency path rather than a Tier 2 model-validation path. It makes stability and separability concerns observable by preserving deterministic retrieval artifacts, reporting context-volume differences, and perturbing source sets before model inference. It does not claim to resolve those concerns through matched-budget output reruns, evidence-order variation, prompt sensitivity, or cross-model testing.

### Data Sources And Case Design

The primary demonstration uses Nike, Starbucks, and Target. These familiar filers support deep source tracing and claim-level illustration. Familiar firms also increase the risk that a model may rely on general pretraining knowledge, so the design includes an LLM-only diagnostic baseline and evaluates claims only against retrieved filing text, retrieved XBRL facts and relation paths, and the claim-level coding protocol.

The main deep-case layer covers two audit constructs: revenue recognition risk and inventory valuation assertion. For each filer-construct pair, we construct four retrieval conditions: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval. This layer produced 24 outputs and 94 preliminary coded claims.

To reduce the concern that the framework reflects only three familiar cases, we also conduct a bounded six-filer extension using Walmart, Home Depot, Caterpillar, Pfizer, Microsoft, and Crocs. The extension covers retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. It applies the same two-construct, four-condition grid used in the main layer: revenue, inventory, LLM-only, text, XBRL, and hybrid. The extension is not designed to estimate population-level performance or failure-mode prevalence. It tests whether the protocol remains applicable across varied reporting environments. This full-scale extension produced 48 additional retrieval-conditioned outputs and 187 preliminary coded claims. Appendix H reports the extension design and diagnostics.

Because XBRL relational retrieval is central to the paper, the demonstration also includes a construct-coverage diagnostic rather than only aggregate fact/path counts. Across 18 construct-filer cells, three cells show complete expected-family coverage and 15 show partial coverage. At the concept-family level, revenue or sales amounts and revenue disaggregation/customer dimensions are retrieved for all nine filers, while refunds, returns, or variable consideration are retrieved for three. Inventory balances are retrieved for all nine filers, while inventory components and inventory movements are retrieved for four. These patterns illustrate why retrieval-environment validity must be evaluated at the construct-family level: an XBRL condition can be traceable and graph-valid while still omitting construct-relevant concept families.

### Retrieval Conditions

The demonstration uses an inspectable keyword/text retrieval prototype and table-based XBRL relational retrieval over extracted facts and relation paths. Text retrieval selects narrative chunks relevant to the filer and construct. XBRL relational retrieval selects facts and relation paths relevant to the same construct. Hybrid retrieval combines narrative and XBRL contexts while preserving source identifiers. The LLM-only baseline supplies no filing-specific retrieved context and is used as a traceability diagnostic.

Vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions and reporting considerations, not as completed performance claims in this study.

To make separability concerns observable, the replication package also reports a context-volume diagnostic for all 72 retrieval contexts. Across the 18 contexts per condition, mean context length is 603 words for text retrieval, 524 words for XBRL retrieval, 691 words for hybrid retrieval, and 10 words for the LLM-only baseline. Hybrid contexts include both narrative chunks and structured facts/paths, with a median text/XBRL word-imbalance ratio of 1.32. These diagnostics do not eliminate separability concerns or constitute a matched-budget sensitivity test. Instead, they document the information-volume differences that future Tier 2 studies should control through token-budget equalization, evidence-order variation, and prompt sensitivity checks.

The package further reports a deterministic source-environment perturbation diagnostic over the 18 filer-construct cells. This diagnostic varies text top-k source selection and XBRL fact/path inclusion without re-running the LLM. Text top-3 and top-8 variants produce mean source-set Jaccard values of 0.600 and 0.625 relative to the implemented top-5 text design. Removing XBRL relation paths produces a mean Jaccard of 0.594 relative to the implemented fact-plus-path design, with 16 of 18 cells below a 0.60 source-set Jaccard threshold. A bounded sensitivity decision matrix classifies the fact-only XBRL variant as a material source-environment change, the text top-k variants as moderate source-environment changes, and the reduced fact-budget XBRL variant as a bounded source-environment change. These results indicate that relational retrieval supplies a materially different source environment from fact retrieval alone and identify cells where future Tier 2 studies should add matched-budget, source-order, prompt-sensitivity, and output-level rerun checks. The diagnostic supports retrieval-stage source-composition transparency; it is not evidence of model-output robustness.

### LLM Execution And Claim Coding

The LLM runs use `gemma4:31b` served locally through Ollama with temperature set to zero. The model choice is not a claim that this model is superior for audit research. It provides a controlled local model for the methodological demonstration. Exact output replication may depend on local model build and serving environment; the replication package preserves prompts, contexts, raw outputs, and model configuration metadata.

Responses are segmented into claims and coded using the correctness protocol. The full 281-claim archive uses author coding for protocol application, and a 120-claim validation sample was independently coded by two coders to evaluate whether the coding categories can be applied consistently. Coders received blank coding fields, coder instructions, a protocol, a codebook, and a claim evidence packet; they were instructed to rely on the provided materials rather than outside company knowledge. Retrieval-condition labels were visible because coders needed them to interpret source availability and integrated-correctness coding, so the exercise validates measurement consistency rather than blinded treatment effects. The independent sample includes all 89 hybrid-condition claims and 31 non-hybrid comparison claims. This design intentionally overweights hybrid claims because the central methodological question is whether a hybrid retrieval condition actually produces integrated text-XBRL source use. The 31 non-hybrid claims provide LLM-only, text-only, and XBRL-only anchors for applying the source-use and correctness scales outside the hybrid condition. The independent coding exercise evaluates the consistency of source-use and integration coding; it does not substitute for audit-domain expert validation of audit-boundary diagnostics. Agreement is high for the main measurement variables: claim segmentation agreement is 100.0 percent, source-use type agreement is 100.0 percent (Cohen's kappa = 1.000), text-supported correctness agreement is 97.5 percent (weighted kappa = 0.919), graph-valid correctness agreement is 99.2 percent (weighted kappa = 0.934), and integrated correctness agreement is 100.0 percent (weighted kappa = 1.000). Claim-kind agreement is 97.5 percent (Cohen's kappa = 0.957). The disagreement pattern is narrow: source-use type and integrated correctness have no disagreements; remaining substantive disagreements are concentrated in three accounting-policy claims where coders differed on whether the statement was factual or risk/assertion-oriented, with associated text-support and one graph-valid boundary difference. The recoding protocol clarifies that ordinary non-integration is coded as `0`, not `NA`, so the integrated-correctness evidence evaluates whether a claim actually uses text and XBRL sources together rather than whether the retrieval condition was labeled hybrid.

These reliability results support the paper's use of claim-level source-use and correctness variables as methodological diagnostics. They do not convert XBRL facts into audit evidence, and they do not establish model-performance effects. We therefore adopt a claim-narrowing approach for audit-boundary coding in the current revision: audit-boundary notes remain qualitative diagnostics rather than expert-validated audit-judgment outcomes. Stronger audit-judgment claims would require additional audit-domain expert review, reconciliation of qualitative audit-boundary notes, and a Tier 2 model-validation design.

### Main Deep Cases

The main cases demonstrate why response-level condition labels are insufficient. A hybrid prompt may give the model both narrative and structured materials, but individual claims within the response may use only one source layer. This distinction matters because a researcher who evaluates output at the response level may conclude that a hybrid condition supports integrated reasoning. Claim-level coding can show a different conclusion: the condition created an opportunity for integration, but the actual claim did not integrate both sources.

[Insert Table 9 about here]

Table 9 reports selected claim-level examples. The examples are selected from the full 281-claim coding archive and are included to illustrate correctness layers and source-use types. Scores are preliminary author-coded diagnostics used to illustrate the protocol. They are not final expert audit-boundary evidence and should not be interpreted as model-performance measures.

The Starbucks inventory example shows direct narrative-XBRL corroboration for a bounded factual claim: inventory reserves were supported by both narrative text and an XBRL fact. The Nike revenue example involving refund liabilities shows a graph-grounded claim within a hybrid condition that was effectively XBRL-only. The Nike digital-commerce example shows a text-supported risk/assertion claim within a hybrid condition that did not use XBRL. The Nike LLM-only example shows that the model appropriately identified insufficient filing-specific context when none was supplied. The Target inventory example shows a graph-grounded claim that did not integrate available narrative inventory context.

### Bounded Extension

The bounded extension supports three methodological points in this retrieval implementation. First, the protocol can be applied beyond the three deep cases: source logs, prompt contexts, output claims, and correctness-layer coding can be maintained across different industries in this purposive sample. Second, the extension is consistent with the claim-level source-use concern: retrieval-condition labels do not by themselves reveal claim-level evidence use. Third, the extension reveals boundary conditions. Caterpillar generated a much larger XBRL fact and relation environment than other filers, making selection and representation validity more salient. Microsoft provided a strong revenue-recognition setting but no selected revenue relation paths under the current retrieval design, illustrating why construct fit and retrieval diagnostics must precede inference.

The extension is reported in the appendix as a full-scale maximum-variation methodological check, not as model-performance evidence or failure-prevalence evidence. Audit-boundary notes remain preliminary author diagnostics unless reviewed by audit-domain experts; source-use type and integrated correctness are independently coded in the 120-claim validation sample to evaluate protocol reliability.

### What The Demonstration Shows

Across the full nine-filer package, comprising 72 retrieval-conditioned outputs and 281 preliminary coded claims, the demonstration documents that retrieval-condition labels do not determine claim-level source use in this model, prompt, and context architecture. In hybrid conditions, 8 of 89 claims used both text and XBRL sources, while 61 used text only and 20 used XBRL only. These counts are design-specific diagnostics, not estimated population frequencies. A mechanism diagnostic indicates that hybrid non-integration in this design is mainly a one-layer-use problem rather than a case of claims citing both layers without synthesis. This pattern supports the methodological need for claim-level source-use coding rather than response-level retrieval-condition evaluation.

The demonstration also documents that, in this implementation, XBRL relational retrieval creates a distinct information environment from narrative text retrieval. Text retrieval supports narrative traceability. XBRL retrieval supports graph-valid reported-fact traceability. A hybrid condition supports integrated correctness only when claims actually use both source layers.

The demonstration provides protocol-validation evidence on three properties required for LLM-based auditing research. First, the source-to-context-to-output-to-claim chain is observable because the replication package preserves retrieved chunks, XBRL facts, relation paths, prompts, raw outputs, claim coding, and source identifiers. Second, the protocol detects inference-relevant differences that response-level labels obscure, as shown by the hybrid-condition source-use divergence. Third, source traceability can be inspected: the coded output validation identified no unresolved source identifiers in the analyzed set. This source-ID check confirms that cited identifiers resolve to preserved retrieved materials; it does not establish that every cited source independently supports the audit-boundary inference.

Together, these artifacts show that audit researchers can preserve the retrieval-created information environment, convert LLM outputs into claim-level source-use variables, evaluate the reliability of central coding categories with independent coders, and diagnose whether a specified hybrid condition produces actual narrative-XBRL integration or one-layer use. That is the paper's positive methodological result. The result is a protocol-validation result, not an identification claim that observed output patterns are caused solely by retrieval design or that hybrid retrieval generally behaves this way.

### What The Demonstration Does Not Show

The demonstration does not show that hybrid retrieval is superior to text or XBRL retrieval. It does not show that XBRL improves audit reasoning. It does not show that `gemma4:31b` has general audit expertise. It does not estimate failure-mode prevalence across SEC filers. It does not implement production vector RAG, a full RDF/OWL triple store, or GraphRAG performance evaluation. These boundaries are necessary because the demonstration is a methodological illustration, not an empirical benchmark.

## VIII. DISCUSSION AND BOUNDARY CONDITIONS

Retrieval-environment validity is a diagnostic lens for construct validity in studies where retrieval systems dynamically create the information environment observed by LLMs. It is not a replacement for construct validity, external validity, internal validity, or measurement validity. Its incremental role is to make the retrieval-created information environment itself observable and evaluable.

Two design implications follow. First, XBRL relational retrieval should be evaluated as management-reported structured evidence, not as audit evidence. It can support graph-validity, reported relation preservation, and narrative-numeric consistency checks; stronger audit conclusions require evidence beyond the public filing and XBRL environment. Second, hybrid retrieval should be evaluated as a construct-specific design for narrative-numeric integration, not as a default improvement over single-source retrieval. Researchers should test whether claims actually integrate sources and should document whether output differences reflect source type, context volume, ordering, or prompt salience.

The current demonstration provides the first evidentiary layer for that design logic. It shows that retrieval environments, prompts, outputs, source references, and claim-level variables can be constructed and inspected. The context-volume and source-environment perturbation diagnostics make separability concerns visible by showing how much information each condition supplied and how source sets change under bounded retrieval perturbations. They do not show that prompt construction, token allocation, evidence ordering, or model-specific behavior had no role in the observed claim patterns. The independent coding sample shows that central source-use and integration variables can be applied reliably. Stronger empirical studies that estimate model performance, retrieval superiority, failure-mode prevalence, or audit-judgment quality should add matched-budget reruns, evidence-order variation, prompt sensitivity, broader sampling, expert audit-domain coding, and reliability evidence.

Audit-boundary diagnostics require professional judgment when used for stronger audit-judgment claims. Text support and graph validity are not substitutes for audit reasoning or evidence sufficiency. Studies that make stronger claims about audit judgment quality should use expert coding, coder independence, reconciliation procedures, and reliability evidence.

The framework is most directly applicable to three classes of audit research. First, archival or textual audit studies can use LLMs as measurement tools if they document how retrieval-created source environments become variables. Second, audit analytics and system-design studies can compare retrieval architectures if they report source selection, representation, traceability, and separability checks. Third, judgment-and-decision-making studies can examine LLM-assisted audit judgments if they distinguish retrieved source support from the sufficiency and appropriateness of audit evidence. These uses share an audit-methodological requirement: the researcher must show what evidence the model observed and what audit inference that evidence can support.

The current package occupies the first of these settings: an audit-research methodology demonstration using public reporting inputs. It is audit-specific because the construct definitions, assertion mappings, evidence hierarchy, and overreach boundaries are drawn from audit research questions and auditing standards. It is not an audit-practice evidence environment. A study that places the framework in an engagement-like setting could add standards passages, internal-control narratives, auditor workpaper excerpts, confirmations, reperformance evidence, or expert-reviewed case materials; that stronger design would support audit-judgment validation only if it also added expert coding and appropriate reliability evidence.

The current prototype is intentionally inspectable rather than architecturally complete. It uses keyword-ranked text retrieval and table-based XBRL relational retrieval. Studies claiming vector-RAG, RDF/OWL, graph database, or GraphRAG performance should provide additional implementation details, benchmarks, and sensitivity checks.

The bounded six-filer extension is a maximum-variation methodological extension, not a representative sample. This sample design follows the logic of AJPT methodological guidance papers that use examples, best-practice illustrations, and design criteria to make a method reviewer-evaluable rather than to estimate population effects (Power and Gendron 2015; Malsch and Salterio 2016; Griffith et al. 2016; Hatfield and Saiewitz 2022). The extension provides limited applicability evidence across varied reporting environments, but it does not estimate the prevalence of retrieval failures across SEC filers. Studies that make prevalence or performance claims should use formal sampling, expert coding, and statistical inference appropriate to those claims.

## IX. CONCLUSION

LLM-based auditing research increasingly depends on retrieval systems that construct the information environment observed by the model. This paper argues that retrieval should be treated as part of research design. Without specifying and validating retrieval-created information environments, researchers risk drawing conclusions about LLM capability, audit reasoning, or construct performance that are actually driven by retrieval selection, representation, instability, weak traceability, or model-retrieval confounding.

We introduce retrieval-environment validity as a diagnostic lens for this problem and operationalize it through retrieval designs, correctness layers, failure modes, reporting guidance, and an SEC/XBRL protocol-validation demonstration. The central lesson is not that one retrieval design is best. The lesson is that different retrieval designs support different inferences.

In LLM-based auditing research, retrieval is not an implementation detail. It is part of the research design that determines the information environment from which output-based inferences are drawn. Audit researchers using LLMs should define the audit construct before retrieval, choose retrieval operators that match that construct, preserve the retrieved information environment, code outputs at the claim level, distinguish text-supported, graph-valid, audit-boundary, and integrated claims, and report retrieval sensitivity proportional to the study's claims.

This framing is intentionally audit-specific. The paper's central contribution is not that retrieval should be documented in general. It is that auditing researchers need reviewer-evaluable rules for deciding whether dynamically retrieved materials support the audit construct, preserve evidence meaning, remain traceable, avoid source overreach, and stop short of audit evidence sufficiency when the data are only public filings and management-reported XBRL.

## DATA AVAILABILITY

The demonstration uses publicly available SEC filing and Inline XBRL data. The replication package preserves the filer manifest, download records, extraction scripts, text chunks, XBRL fact and relation-path tables, retrieval logs, rendered prompts, LLM output files, claim-level coding, and selected source spot checks. The local LLM outputs were generated using Ollama with `gemma4:31b` at temperature 0. Because local model builds and hardware environments may differ, exact output replication may require recording the local model digest and environment configuration. The demonstration should be interpreted as a methodological reproducibility package rather than a benchmark archive.

## REFERENCES

Appelbaum, D., A. Kogan, and M. A. Vasarhelyi. 2017. Big Data and analytics in the modern audit engagement: Research needs. *Auditing: A Journal of Practice & Theory* 36 (4): 1-27. https://doi.org/10.2308/ajpt-51684

Appelbaum, D. A., A. Kogan, and M. A. Vasarhelyi. 2018. Analytical procedures in external auditing: A comprehensive literature survey and framework for external audit analytics. *Journal of Accounting Literature* 40: 83-101. https://doi.org/10.1016/j.acclit.2018.01.001

Bae, J., C.-Y. Hung, and L. van Lent. 2023. Mobilizing text as data. *European Accounting Review* 32 (5): 1085-1106. https://doi.org/10.1080/09638180.2023.2218423

Berger, A., L. Hillebrand, D. Leonhard, T. Deusser, T. B. F. de Oliveira, T. Dilmaghani, M. Khaled, B. Kliem, R. Loitz, C. Bauckhage, and R. Sifa. 2025. Towards automated regulatory compliance verification in financial auditing with large language models. Working paper. https://arxiv.org/abs/2507.16642

Blankespoor, E., E. deHaan, and Q. Li. 2026. Generative AI in financial reporting. *Journal of Accounting Research*. https://doi.org/10.1111/1475-679X.70050

Bochkay, K., S. V. Brown, A. J. Leone, and J. W. Tucker. 2023. Textual analysis in accounting: What's next? *Contemporary Accounting Research* 40 (2): 765-805. https://doi.org/10.1111/1911-3846.12825

Brown-Liburd, H., H. Issa, and D. Lombardi. 2015. Behavioral implications of Big Data's impact on audit judgment and decision making and future research directions. *Accounting Horizons* 29 (2): 451-468. https://doi.org/10.2308/acch-51023

de Kok, T. 2025. ChatGPT for textual analysis? How to use generative LLMs in accounting research. *Management Science* 71 (9): 7888-7906. https://doi.org/10.1287/mnsc.2023.03253

Es, S., J. James, L. Espinosa-Anke, and S. Schockaert. 2024. RAGAS: Automated evaluation of retrieval augmented generation. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, 150-158. Association for Computational Linguistics. https://aclanthology.org/2024.eacl-demo.16

Fedyk, A., J. Hodson, N. Khimich, and T. Fedyk. 2022. Is artificial intelligence improving the audit process? *Review of Accounting Studies* 27: 938-985. https://doi.org/10.1007/s11142-022-09697-x

Gao, T., H. Yen, J. Yu, and D. Chen. 2023. Enabling large language models to generate text with citations. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, 6465-6488. Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-main.398

Griffith, E. E., K. Kadous, and D. Young. 2016. How insights from the "new" JDM research can improve auditor judgment: Fundamental research questions and methodological advice. *Auditing: A Journal of Practice & Theory* 35 (2): 1-22. https://doi.org/10.2308/ajpt-51347

Hatfield, R. C., and A. Saiewitz. 2022. Theoretical and practical guidance for incorporating auditor-client communication in experimental research. *Auditing: A Journal of Practice & Theory* 41 (4): 163-177. https://doi.org/10.2308/AJPT-2019-520

Hoitash, R., and U. Hoitash. 2018. Measuring accounting reporting complexity with XBRL. *The Accounting Review* 93 (1): 259-287. https://doi.org/10.2308/accr-51762

Hoitash, R., U. Hoitash, and L. Morris. 2021. eXtensible Business Reporting Language (XBRL): A review and implications for future research. *Auditing: A Journal of Practice & Theory* 40 (2): 107-132. https://doi.org/10.2308/AJPT-2019-517

Johnston, J. A., K. J. Reichelt, and P. Sapkota. 2024. Measuring financial statement disaggregation using XBRL. *Journal of Information Systems* 38 (1): 119-147. https://doi.org/10.2308/ISYS-2021-004

Kim, A. G., M. Muhn, and V. V. Nikolaev. 2024. Financial statement analysis with large language models. Working paper. https://arxiv.org/abs/2407.17866

Li, F. 2010. Textual analysis of corporate disclosures: A survey of the literature. *Journal of Accounting Literature* 29: 143-165.

Li, H., and M. A. Vasarhelyi. 2024. Applying large language models in accounting: A comparative analysis of different methodologies and off-the-shelf examples. *Journal of Emerging Technologies in Accounting* 21 (2): 133-152. https://doi.org/10.2308/JETA-2023-065

Lewis, P., E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Kuttler, M. Lewis, W.-t. Yih, T. Rocktaschel, S. Riedel, and D. Kiela. 2020. Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems* 33: 9459-9474.

Loughran, T., and B. McDonald. 2016. Textual analysis in accounting and finance: A survey. *Journal of Accounting Research* 54 (4): 1187-1230. https://doi.org/10.1111/1475-679X.12123

Malsch, B., and S. E. Salterio. 2016. "Doing good field research": Assessing the quality of audit field research. *Auditing: A Journal of Practice & Theory* 35 (1): 1-22. https://doi.org/10.2308/ajpt-51170

Power, M. K., and Y. Gendron. 2015. Qualitative research in auditing: A methodological roadmap. *Auditing: A Journal of Practice & Theory* 34 (2): 147-165. https://doi.org/10.2308/ajpt-10423

Public Company Accounting Oversight Board (PCAOB). 2024a. AS 1105: Audit Evidence. Available at: https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105

Public Company Accounting Oversight Board (PCAOB). 2024b. AS 2110: Identifying and Assessing Risks of Material Misstatement. Available at: https://pcaobus.org/Standards/Auditing/Pages/AS2110.aspx

Public Company Accounting Oversight Board (PCAOB). 2024c. AS 2301: The Auditor's Responses to the Risks of Material Misstatement. Available at: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2301

Rashkin, H., V. Nikolaev, M. Lamm, L. Aroyo, M. Collins, D. Das, S. Petrov, G. S. Tomar, I. Turc, and D. Reitter. 2023. Measuring attribution in natural language generation models. *Computational Linguistics* 49 (4): 777-840. https://doi.org/10.1162/coli_a_00486

Saad-Falcon, J., O. Khattab, C. Potts, and M. Zaharia. 2024. ARES: An automated evaluation framework for retrieval-augmented generation systems. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, 338-354. Association for Computational Linguistics. https://aclanthology.org/2024.naacl-long.20

Wang, J. J., and V. X. Wang. 2025. Assessing consistency and reproducibility in the outputs of large language models: Evidence across diverse finance and accounting tasks. Working paper. https://arxiv.org/abs/2503.16974

Wang, R., J. Liu, W. Zhao, S. Li, and D. Zhang. 2025. Automating financial statement audits with large language models. Working paper. https://arxiv.org/abs/2506.17282

Xing, C., and H. Meng. 2026. DC-RAG: A dual-channel retrieval-augmented generation framework for audit analysis. *Scientific Reports* 16. https://doi.org/10.1038/s41598-026-50062-8

Xiong, F., Q. Han, and C. Zhang. 2024. Performance improvement for large language models: Retrieval-augmented generation AI agent for tabular data processing in auditing procedures. Working paper. https://doi.org/10.2139/ssrn.5100205

Yoon, K., L. Hoogduin, and L. Zhang. 2015. Big Data as complementary audit evidence. *Accounting Horizons* 29 (2): 431-438. https://doi.org/10.2308/acch-51076

## APPENDIX

Appendix A. Source Corpus, Filer Manifest, and Ex Ante Construct Protocols.

Appendix B. Text Retrieval Store and Chunking.

Appendix C. XBRL Fact, Relation, and Construct-Coverage Store.

Appendix D. Prompt and Retrieval Context Archive.

Appendix E. LLM Run Configuration and Output Archive.

Appendix F. Claim-Level Coding Package.

Appendix G. Source Spot Checks and Selected Examples.

Appendix H. Bounded Extension Evidence.

Appendix I. Sensitivity Guidance and Boundary Conditions.

The appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration. The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-boundary coding remains preliminary unless independently reviewed by audit-domain experts; source-use type and integrated correctness are independently coded in the 120-claim validation sample to evaluate protocol reliability.
