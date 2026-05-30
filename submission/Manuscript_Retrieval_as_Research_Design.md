# Submission-Ready Manuscript Draft v3

## Title

Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval

## Abstract

Retrieval-augmented large language models are increasingly used in accounting and auditing research, yet retrieval is often treated as a technical implementation step rather than as part of research design. We introduce retrieval-environment validity: the extent to which the information dynamically retrieved for an LLM aligns with the audit construct a researcher intends to study. The framework identifies five dimensions: selection, representation, stability, traceability, and separability. We operationalize the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting guidance, and an SEC/XBRL-based methodological demonstration. The demonstration uses text retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline to show that retrieval-condition labels can mask different claim-level evidence bases. The paper provides guidance for designing, evaluating, and reporting LLM-based auditing research without treating XBRL as audit evidence or benchmarking model performance.

## Declaration Of Generative AI And AI-Assisted Technologies In The Writing Process

The authors used generative AI and AI-assisted tools to support manuscript drafting, editing, code development, and organization of reproducibility materials. The authors reviewed, revised, and are responsible for all manuscript content, analyses, source interpretations, and conclusions. The use of LLMs as part of the methodological demonstration is described in the demonstration section and supporting appendix materials.

## I. INTRODUCTION

Large language models (LLMs) are increasingly being studied in accounting and auditing research. Many research designs augment these models with external information through retrieval-augmented generation. In these designs, the model may receive financial filing text, accounting standards, structured reporting data, audit-workpaper-like materials, or other domain-specific sources before generating a response. The methodological problem is that retrieval is often described as an implementation step, even though it determines what information the model observes.

This paper contributes to auditing research methodology by treating retrieval as a research-design and data/variable-construction problem in LLM-based auditing studies. A retrieval system does not merely add information to a prompt. It constructs the information environment from which the model generates its response. It selects sources, ranks evidence units, traverses relations, filters contexts, truncates materials, formats evidence, and determines which parts of the source corpus are visible to the model. When researchers evaluate LLM outputs without validating this retrieval-created information environment, they may attribute differences in outputs to model capability, prompt quality, or audit reasoning when those differences arise from retrieval design.

This distinction matters because audit research constructs depend on the source, nature, and evidentiary status of information. Narrative disclosures may support analysis of management explanations, accounting policy language, or disclosed risk cues. XBRL tags, facts, contexts, and linkbase relations may support analysis of management-reported accounting relationships. Neither source is equivalent to audit evidence. A claim can be supported by retrieved text and consistent with XBRL facts while still overstating what the evidence can support as audit reasoning. Conversely, a response can appear weak because the retrieval pipeline failed to supply construct-relevant information.

We introduce retrieval-environment validity as a diagnostic framework for this problem. Retrieval-environment validity is the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct the researcher intends to study. The concept does not replace construct validity. It identifies a retrieval-specific mechanism through which construct validity can fail in studies where the model's information set is created at runtime.

[Insert Figure 1 about here]

The paper's central research question is:

> How does retrieval design affect the validity of inferences drawn from LLM-based auditing research?

The paper contributes to auditing research methodology in three ways. First, it defines retrieval-environment validity and identifies five dimensions: selection, representation, stability, traceability, and separability. Second, it operationalizes the framework through a retrieval typology, construct-to-retrieval mapping, claim-level correctness protocol, failure-mode taxonomy, reporting checklist, and reproducibility guidance. These tools speak directly to research design and data/variable construction for LLM-based auditing research by converting retrieval artifacts and model responses into study-level variables, including text-supported correctness, graph-valid correctness, audit-valid correctness, integrated correctness, evidence-use type, and failure-mode labels. Third, it provides a descriptive methodological demonstration using SEC filing text and Inline XBRL data to show how retrieval design changes the evidence basis of LLM-generated audit claims.

Answering the research question changes how researchers should design and evaluate LLM audit studies. Researchers should define the audit construct before retrieval, choose retrieval operators that fit that construct, preserve the retrieved information environment, evaluate output claims by correctness layer, distinguish management-reported XBRL relations from audit evidence, and report retrieval sensitivity proportional to the study's claims.

We illustrate the framework using a two-layer demonstration design. The main demonstration uses three familiar SEC filers for deep source tracing and claim-level illustration. The appendix reports a bounded six-filer extension selected for variation in industry, scale, reporting complexity, and construct fit. The demonstration's evidentiary contribution is not that one retrieval design performs better. It is that response-level retrieval labels are insufficient: claims within the same condition can rely on different evidence bases, and those differences change the research inference. A hybrid condition can produce integrated text-XBRL claims, but it can also produce claims that rely only on text, only on XBRL, or on insufficient retrieved evidence. The demonstration is not designed to rank retrieval methods, evaluate a model's audit expertise, or estimate population-level failure rates.

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

### Audit Analytics, Big Data, And AI In Auditing

Audit analytics and AI research examines how auditors and audit technologies process large, complex, or nontraditional data sources (Brown-Liburd, Issa, and Lombardi 2015; Yoon, Hoogduin, and Zhang 2015; Appelbaum, Kogan, and Vasarhelyi 2017, 2018; Fedyk et al. 2022). This literature shows that technology-enabled information environments matter for audit judgment, audit evidence, and audit process design. It also cautions that more data or more automation does not automatically produce better audit evidence.

Our paper is related but distinct. We do not propose an audit procedure, audit agent, or engagement workflow. We provide methodology for researchers studying LLM-based auditing tasks. The relevant object is not whether an LLM system can automate an audit procedure, but whether the retrieval-created information environment supports the inference a researcher draws from LLM outputs.

### Synthesis

Prior work studies data, tools, models, auditors, or outcomes. This paper studies the retrieval-created information environment that connects source data to LLM output in auditing research designs. Retrieval systems sit between data and output. They determine what the model sees, how evidence is represented, whether sources are traceable, and whether output differences can be separated from retrieval effects. This paper fills that gap by introducing retrieval-environment validity and by providing tools for retrieval design, claim-level correctness coding, failure-mode diagnosis, reporting, and sensitivity analysis.

## III. RETRIEVAL-ENVIRONMENT VALIDITY

Retrieval-augmented LLM audit studies differ from fixed-information-set studies because the information environment observed by the model is dynamically constructed. The retriever selects information, ranks it, renders it into a context window, and may transform or omit materials before the model produces an output. Observed LLM behavior is therefore a function of both the model and the retrieval-created information environment.

### Definition

We define retrieval-environment validity as the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study. The concept asks whether the retrieval-created information environment permits the researcher to draw the intended inference from the LLM output.

Retrieval-environment validity is grounded in construct validity, but existing validity language is not sufficient by itself because retrieval creates a dynamic materials boundary. In a fixed-information-set study, the researcher can define and inspect the information package supplied to a participant or model before inference. In a retrieval-augmented LLM study, the corpus, prompt, and model do not fully specify the information environment. The environment is created by a retrieval pipeline at runtime through source selection, ranking, relation traversal, context filtering, chunking, truncation, and formatting.

[Insert Table 1 about here]

Table 1 distinguishes fixed information sets from dynamic retrieval environments. In a fixed-information-set design, the researcher defines the evidence package before the study. In a dynamic retrieval design, the information boundary is constructed at query time. Replication therefore requires not only the prompt and model, but also the corpus, retrieval unit, retrieval operator, ranking or traversal rule, context rendering, and returned evidence logs.

### Five Validity Dimensions

Retrieval-environment validity has five dimensions.

Selection validity concerns whether retrieval selects evidence relevant to the intended audit construct. A revenue-recognition risk task may require contract-liability disclosures, variable consideration policy language, and related reported amounts. If retrieval supplies only generic risk-factor text, output differences may reflect retrieval omission rather than model audit reasoning.

Representation validity concerns whether retrieved information preserves the meaning of source evidence. Text chunks can distort meaning by severing a sentence from its footnote context. XBRL facts can be distorted if concepts, periods, units, dimensions, decimals, or signs are omitted. Relation paths can be distorted if arcroles or linkroles are collapsed into generic edges.

Stability concerns whether equivalent runs would retrieve materially similar information environments. A study that makes claims about model behavior needs to show that observed outputs are not artifacts of unstable retrieval rankings, variable query wording, changing corpora, or undocumented index versions.

Traceability concerns whether each LLM claim can be traced to retrieved source evidence. This dimension is especially important in audit research because documentation and support are central to evaluating evidence. A claim that cannot be linked to a retrieved text chunk, XBRL fact, or relation path should not be treated as retrieval-supported.

Separability concerns whether retrieval effects can be separated from model effects. If the text condition receives 500 words and the hybrid condition receives 1,500 words, output differences may reflect information volume rather than evidence type. If prompts, models, temperatures, or task wording differ across conditions, researchers cannot attribute output differences to retrieval design alone.

[Insert Table 2 about here]

Table 2 summarizes the five dimensions, their audit or method anchors, observable evidence, and associated failure modes. The table makes retrieval-environment validity usable as a reviewer-facing diagnostic framework rather than only a conceptual label.

## IV. RETRIEVAL DESIGNS FOR LLM-BASED AUDITING RESEARCH

Retrieval design should follow the intended audit construct. The same source corpus can support different research claims depending on the retrieval unit, operator, and evidence status. The relevant question is not whether retrieval adds information, but whether the retrieved information environment aligns with the construct being studied.

### Retrieval Typology

We distinguish four retrieval designs: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval.

LLM-only designs provide no external retrieved context. They can serve as diagnostic baselines for pretraining knowledge, task wording, and traceability. They should not be treated as audit evidence because the model's response is not source-linked.

Text retrieval supplies narrative evidence such as filings, audit documents, standards, or workpaper-like materials. Its retrieval unit is typically a text chunk. Its operators may include keyword search, semantic similarity, hybrid search, filtering, or reranking. Text retrieval is well suited to narrative disclosure interpretation, accounting policy language, management explanation, and qualitative risk cues.

XBRL relational retrieval supplies structured facts, contexts, concepts, units, and linkbase relations. Its retrieval unit may be a fact, concept, edge, or relation path. Its operators may include concept lookup, seed-pattern selection, relation traversal, taxonomy filtering, or ontology query. XBRL relational retrieval is well suited to studying reported accounting relationships, numeric traceability, and whether LLM outputs preserve management-reported structure.

Hybrid retrieval supplies narrative and structured evidence together. It is appropriate when the intended construct requires narrative-numeric integration. However, hybrid retrieval is not automatically superior. A hybrid condition can produce integrated claims, but it can also produce text-only claims, XBRL-only claims, or juxtaposed evidence without synthesis.

[Insert Table 3 about here]

Table 3 defines these retrieval designs by source, unit, operator, audit use, and risk.

### Construct-To-Retrieval Mapping

Different audit constructs require different retrieval environments. Understanding narrative disclosure generally requires text retrieval. Preserving reported accounting relationships may require XBRL relational retrieval. Connecting narrative risk language to reported amounts may require hybrid retrieval. Identifying assertion-level risk cues may require hybrid retrieval plus explicit audit coding. Detecting misstatement, fraud, or internal control failure requires evidence beyond management-reported filings and cannot be established from XBRL relations alone.

[Insert Table 4 about here]

Table 4 operationalizes construct-to-retrieval alignment. The "what not to claim" column is as important as the recommended retrieval design because it prevents construct drift. A study can use XBRL relational retrieval to evaluate graph-valid reported relationships; it should not claim that XBRL alone verifies audit assertions. A study can use hybrid retrieval to study narrative-numeric integration; it should not claim that hybrid retrieval automatically improves reasoning.

## V. CLAIM-LEVEL CORRECTNESS AND FAILURE MODES

Response-level accuracy is too coarse for LLM-based auditing research because a single response may contain claims supported by different evidence bases. One claim may be directly supported by retrieved text. Another may be graph-valid against XBRL facts. A third may make an audit inference that exceeds both sources. A fourth may use no retrieved evidence despite being produced under a retrieval condition.

### Claim As The Unit Of Analysis

We define a claim as a separable assertion in an LLM output that can be evaluated against retrieved evidence and the intended audit construct. Claim-level analysis is necessary because retrieval-condition labels do not determine claim-level evidence use. A response labeled "hybrid" may contain integrated claims, text-only claims, XBRL-only claims, unsupported claims, or insufficient-context statements.

### Correctness Layers

We propose four correctness layers.

Text-supported correctness asks whether a claim is supported by retrieved narrative text. A claim can be text-supported if the cited or used text provides sufficient support for the claim's content.

Graph-valid correctness asks whether a claim is consistent with retrieved XBRL facts or relation paths. This includes checking concept, value, period, unit, context, and relation structure.

Audit-valid correctness asks whether the inference is appropriate for the audit construct. This layer requires professional judgment when used for stronger claims. A claim may be text-supported and graph-valid but still not audit-valid if it treats management disclosure as audit evidence or overstates what the reported data can support.

Integrated correctness asks whether a hybrid claim uses text and XBRL evidence together without contradiction. A claim is not integrated merely because text and XBRL were both available in the prompt. Integration requires an inferential bridge between evidence types.

[Insert Table 5 about here]

Table 5 summarizes these layers. The key methodological point is that correctness is claim-type specific. Researchers should not collapse text support, graph validity, audit validity, and integration into a single answer-level score.

### Failure Modes

The claim-level protocol also supports failure-mode diagnosis. Omission occurs when relevant evidence exists but is not retrieved. Distortion occurs when retrieved evidence loses its source meaning. Retrieval instability occurs when similar queries return materially different evidence. Attribution failure occurs when an output claim cannot be traced to retrieved evidence. Model-retrieval confounding occurs when output differences cannot be attributed to retrieval design. Relation hallucination occurs when the model invents or misstates XBRL relations. Source overreach occurs when the model treats management-reported XBRL as audit evidence. Integration failure occurs when hybrid retrieval lists text and XBRL evidence but does not reason across them.

The taxonomy is reported in Appendix Table F2. It links failure modes to retrieval-environment validity dimensions and design responses.

## VI. REPORTING GUIDANCE AND REPRODUCIBILITY STANDARDS

The framework is useful only if researchers can apply it. We therefore provide reporting and reproducibility guidance that scales with the study's claims.

### Design Guidance

The framework changes LLM-based auditing research design in six practical ways. Researchers should define the audit construct before choosing a retrieval method. They should choose retrieval operators that match the construct: text retrieval for narrative meaning, XBRL relational retrieval for reported accounting structure, and hybrid retrieval for narrative-numeric integration. They should preserve the evidence actually supplied to the LLM, including retrieved chunks, facts, relation paths, prompts, and context rendering. They should evaluate LLM outputs at the claim level rather than only at the response level. They should distinguish reported XBRL relations from audit evidence and avoid converting graph-valid claims into audit-valid conclusions without professional judgment. Finally, they should report sensitivity checks proportional to the claims they make about retrieval, model behavior, and audit constructs.

[Insert Table 6 about here]

Table 6 provides a tiered reporting standard. Tier 1 applies to descriptive methodological demonstrations. Researchers should disclose retrieval units, operators, source identifiers, context budgets, prompts, logs, claim coding, and selected spot checks. Tier 2 applies to empirical LLM audit studies using RAG and requires additional embedding/index metadata, sensitivity checks, expert coding, and reliability evidence. Tier 3 applies to retrieval-system or GraphRAG evaluations and requires benchmark design, retrieval metrics, system parameters, and robustness evidence.

The current paper's demonstration is a Tier 1 methodological demonstration. It should not be read as a performance benchmark for vector RAG, graph databases, or LLM audit expertise.

### Implementation Transparency

For text retrieval, researchers should report source document records, chunk schema, chunking rule, chunk size, overlap, embedding model when used, vector index when used, similarity metric, top-k, reranking policy, and retrieval logs.

For XBRL relational retrieval, researchers should report fact tables, concept identifiers, relation edge/path tables, taxonomy and linkbase sources, taxonomy version, extension-concept handling, traversal depth, relation type filters, period/unit/dimension handling, and any RDF/OWL-compatible mapping.

The RDF/OWL layer should be presented as a portability and compatibility schema, not as a claim that XBRL becomes audit evidence. Researchers should distinguish XBRL-coded reporting relations from researcher-coded audit construct or assertion mappings.

### Sensitivity Guidance

Recommended sensitivity checks include chunk size, chunk overlap, top-k, query wording, embedding model, reranking, traversal depth, relation type filters, extension concept inclusion, period and dimension filters, token budget equalization, prompt variation, model variation, and repeated retrieval stability.

These checks should be tied to validity dimensions. For example, top-k and traversal depth affect selection validity, relation rendering affects representation validity, repeated retrieval affects stability, source IDs affect traceability, and token budget equalization affects separability. Appendix I maps reporting items and sensitivity checks to the five validity dimensions.

## VII. METHODOLOGICAL DEMONSTRATION

The demonstration shows that retrieval-condition labels do not determine claim-level evidence use. To illustrate how retrieval-environment validity changes the interpretation of LLM-based audit outputs, we conduct a descriptive demonstration using actual SEC filing text and Inline XBRL data. The purpose is not to rank retrieval methods or estimate model performance. The purpose is to show how retrieval design changes the evidence basis of LLM-generated audit claims and therefore changes what researchers can validly infer from those claims.

[Insert Figure 2 about here]

Figure 2 summarizes the demonstration pipeline. We download SEC 10-K filings and Inline XBRL data, extract narrative text and structured facts, build text and XBRL retrieval contexts, run controlled prompts under retrieval conditions, segment responses into claims, and code claims using the correctness protocol.

### Data Sources And Case Design

The primary demonstration uses Nike, Starbucks, and Target. These familiar filers support deep source tracing and claim-level illustration. Familiar firms also increase the risk that a model may rely on general pretraining knowledge, so the design includes an LLM-only diagnostic baseline and evaluates claims only against retrieved filing text, retrieved XBRL facts and relation paths, and the claim-level coding protocol.

The main demonstration covers two audit constructs: revenue recognition risk and inventory valuation assertion. For each filer-construct pair, we construct four retrieval conditions: LLM-only, text retrieval, XBRL relational retrieval, and hybrid retrieval. The main run produced 24 outputs and 94 preliminary coded claims.

To reduce the concern that the framework reflects only three cases, we also conduct a bounded six-filer extension using Walmart, Home Depot, Caterpillar, Pfizer, Microsoft, and Crocs. The extension covers retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products. It is not designed to estimate population-level performance or failure-mode prevalence. It tests whether the protocol remains applicable across varied reporting environments. The extension produced 18 additional retrieval-conditioned outputs and 88 preliminary coded claims. Appendix H reports the extension design and diagnostics.

### Retrieval Conditions

The demonstration uses an inspectable keyword/text retrieval prototype and table-based XBRL relational retrieval over extracted facts and relation paths. Text retrieval selects narrative chunks relevant to the filer and construct. XBRL relational retrieval selects facts and relation paths relevant to the same construct. Hybrid retrieval combines narrative and XBRL contexts while preserving source identifiers. The LLM-only baseline supplies no filing-specific retrieved context and is used as a traceability diagnostic.

Vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions and reporting considerations, not as completed performance claims in this study.

### LLM Execution And Claim Coding

The LLM runs use `gemma4:31b` served locally through Ollama with temperature set to zero. The model choice is not a claim that this model is superior for audit research. It provides a controlled local model for the methodological demonstration. Exact output replication may depend on local model build and serving environment; the replication package preserves prompts, contexts, raw outputs, and model configuration metadata.

Responses are segmented into claims and coded using the correctness protocol. Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics. The demonstration supports claims about source traceability and claim-level evidence-use divergence, not final audit-judgment quality.

### Main Deep Cases

The main cases demonstrate why response-level condition labels are insufficient. A hybrid prompt may give the model both narrative and structured evidence, but individual claims within the response may use only one evidence layer. This distinction matters because a researcher who evaluates output at the response level may conclude that hybrid retrieval supports integrated reasoning. Claim-level coding can show a different inference: the condition created an opportunity for integration, but the actual claim did not integrate both sources.

[Insert Table 7 about here]

Table 7 reports selected claim-level examples. The examples are selected from the full 182-claim coding archive and are included to illustrate correctness layers and evidence-use types. Scores are preliminary author-coded diagnostics used to illustrate the protocol. They are not final expert audit-validity evidence and should not be interpreted as model-performance measures.

The Starbucks inventory example shows direct narrative-XBRL corroboration for a bounded factual claim: inventory reserves were supported by both narrative text and an XBRL fact. The Nike revenue example involving refund liabilities shows a graph-grounded claim within a hybrid condition that was effectively XBRL-only. The Nike digital-commerce example shows a text-supported risk/assertion claim within a hybrid condition that did not use XBRL. The Nike LLM-only example shows that the model appropriately identified insufficient filing-specific context when none was supplied. The Target inventory example shows a graph-grounded claim that did not integrate available narrative inventory context.

### Bounded Extension

The bounded extension supports three methodological points. First, the protocol scales beyond the three deep cases: source logs, prompt contexts, output claims, and correctness-layer coding can be maintained across different industries. Second, the extension preserves the main inference that retrieval-condition labels do not reveal claim-level evidence use. Third, the extension reveals boundary conditions. Caterpillar generated a much larger XBRL fact and relation environment than other filers, making selection and representation validity more salient. Microsoft provided a strong revenue-recognition setting but no selected revenue relation paths under the current retrieval design, illustrating why construct fit and retrieval diagnostics must precede inference.

The extension is reported in the appendix as robustness evidence, not as model-performance evidence. Audit-valid and integrated scores remain preliminary author coding unless reviewed by audit-domain experts.

### What The Demonstration Shows

Across 42 retrieval-conditioned outputs and 182 preliminary coded claims, the demonstration shows that retrieval-condition labels do not determine claim-level evidence use. In hybrid conditions, only 7 of 60 claims used both text and XBRL sources, while 41 used text only and 12 used XBRL only. This pattern supports the methodological need for claim-level evidence-use coding rather than response-level retrieval-condition evaluation.

The demonstration also shows that XBRL relational retrieval creates a distinct information environment from narrative text retrieval. Text retrieval supports narrative traceability. XBRL retrieval supports graph-valid reported-fact traceability. Hybrid retrieval supports integrated correctness only when claims actually use both evidence layers.

### What The Demonstration Does Not Show

The demonstration does not show that hybrid retrieval is superior to text or XBRL retrieval. It does not show that XBRL improves audit reasoning. It does not show that `gemma4:31b` has general audit expertise. It does not estimate failure-mode prevalence across SEC filers. It does not implement production vector RAG, a full RDF/OWL triple store, or GraphRAG performance evaluation. These boundaries are necessary because the demonstration is a methodological illustration, not an empirical benchmark.

## VIII. DISCUSSION AND BOUNDARY CONDITIONS

Retrieval-environment validity is a diagnostic lens for construct validity in studies where retrieval systems dynamically create the information environment observed by LLMs. It is not a replacement for construct validity, external validity, internal validity, or measurement validity. Its incremental role is to make the retrieval-created information environment itself observable and evaluable.

XBRL relational retrieval does not convert XBRL into audit evidence. XBRL facts and relations are management-reported accounting information. They may support graph-validity, reported relation preservation, or narrative-numeric consistency checks, but they do not establish that an audit assertion is satisfied.

Hybrid retrieval is not universally superior. It supports a different construct: integration of narrative and reported relational information. Hybrid retrieval can reduce separability because output differences may reflect more total information, different ordering, or interaction between text and relation context. Researchers should evaluate whether claims actually integrate evidence rather than assuming integration from the condition label.

The current demonstration is descriptive. It illustrates inference shifts rather than testing a hypothesis about model performance. Hypothesis-testing studies should use fuller sensitivity checks, expert coding, reliability evidence, and stronger controls over token budget and retrieval variation.

Audit-valid correctness requires professional judgment. Text support and graph validity are not substitutes for audit reasoning or evidence sufficiency. Studies that make stronger claims about audit judgment quality should use expert coding, coder independence, reconciliation procedures, and reliability evidence.

The current prototype is intentionally inspectable rather than architecturally complete. It uses keyword-ranked text retrieval and table-based XBRL relational retrieval. Studies claiming vector-RAG, RDF/OWL, graph database, or GraphRAG performance should provide additional implementation details, benchmarks, and sensitivity checks.

The bounded six-filer extension is a maximum-variation methodological extension, not a representative sample. It increases confidence that the protocol can be applied across varied reporting environments, but it does not estimate the prevalence of retrieval failures across SEC filers. Studies that make prevalence or performance claims should use formal sampling, expert coding, and statistical inference appropriate to those claims.

## IX. CONCLUSION

LLM-based auditing research increasingly depends on retrieval systems that construct the information environment observed by the model. This paper argues that retrieval should be treated as part of research design. Without specifying and validating retrieval-created information environments, researchers risk drawing conclusions about LLM capability, audit reasoning, or construct performance that are actually driven by retrieval selection, representation, instability, weak traceability, or model-retrieval confounding.

We introduce retrieval-environment validity as a diagnostic lens for this problem and operationalize it through retrieval designs, correctness layers, failure modes, reporting guidance, and a descriptive SEC/XBRL demonstration. The central lesson is not that one retrieval design is best. The lesson is that different retrieval designs support different inferences.

In LLM-based auditing research, retrieval is not an implementation detail. It is part of the research design that determines the information environment from which output-based inferences are drawn. Audit researchers using LLMs should define the audit construct before retrieval, choose retrieval operators that match that construct, preserve the retrieved information environment, code outputs at the claim level, distinguish text-supported, graph-valid, audit-valid, and integrated claims, and report retrieval sensitivity proportional to the study's claims.

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

Fedyk, A., J. Hodson, N. Khimich, and T. Fedyk. 2022. Is artificial intelligence improving the audit process? *Review of Accounting Studies* 27: 938-985. https://doi.org/10.1007/s11142-022-09697-x

Griffith, E. E., K. Kadous, and D. Young. 2016. How insights from the "new" JDM research can improve auditor judgment: Fundamental research questions and methodological advice. *Auditing: A Journal of Practice & Theory* 35 (2): 1-22. https://doi.org/10.2308/ajpt-51347

Hatfield, R. C., and A. Saiewitz. 2022. Theoretical and practical guidance for incorporating auditor-client communication in experimental research. *Auditing: A Journal of Practice & Theory* 41 (4): 163-177. https://doi.org/10.2308/AJPT-2019-520

Hoitash, R., and U. Hoitash. 2018. Measuring accounting reporting complexity with XBRL. *The Accounting Review* 93 (1): 259-287. https://doi.org/10.2308/accr-51762

Hoitash, R., U. Hoitash, and L. Morris. 2021. eXtensible Business Reporting Language (XBRL): A review and implications for future research. *Auditing: A Journal of Practice & Theory* 40 (2): 107-132. https://doi.org/10.2308/AJPT-2019-517

Johnston, J. A., K. J. Reichelt, and P. Sapkota. 2024. Measuring financial statement disaggregation using XBRL. *Journal of Information Systems* 38 (1): 119-147. https://doi.org/10.2308/ISYS-2021-004

Kim, A. G., M. Muhn, and V. V. Nikolaev. 2024. Financial statement analysis with large language models. Working paper. https://arxiv.org/abs/2407.17866

Li, F. 2010. Textual analysis of corporate disclosures: A survey of the literature. *Journal of Accounting Literature* 29: 143-165.

Li, H., and M. A. Vasarhelyi. 2024. Applying large language models in accounting: A comparative analysis of different methodologies and off-the-shelf examples. *Journal of Emerging Technologies in Accounting* 21 (2): 133-152. https://doi.org/10.2308/JETA-2023-065

Loughran, T., and B. McDonald. 2016. Textual analysis in accounting and finance: A survey. *Journal of Accounting Research* 54 (4): 1187-1230. https://doi.org/10.1111/1475-679X.12123

Malsch, B., and S. E. Salterio. 2016. "Doing good field research": Assessing the quality of audit field research. *Auditing: A Journal of Practice & Theory* 35 (1): 1-22. https://doi.org/10.2308/ajpt-51170

Power, M. K., and Y. Gendron. 2015. Qualitative research in auditing: A methodological roadmap. *Auditing: A Journal of Practice & Theory* 34 (2): 147-165. https://doi.org/10.2308/ajpt-10423

Wang, J. J., and V. X. Wang. 2025. Assessing consistency and reproducibility in the outputs of large language models: Evidence across diverse finance and accounting tasks. Working paper. https://arxiv.org/abs/2503.16974

Wang, R., J. Liu, W. Zhao, S. Li, and D. Zhang. 2025. Automating financial statement audits with large language models. Working paper. https://arxiv.org/abs/2506.17282

Xing, C., and H. Meng. 2026. DC-RAG: A dual-channel retrieval-augmented generation framework for audit analysis. *Scientific Reports* 16. https://doi.org/10.1038/s41598-026-50062-8

Xiong, F., Q. Han, and C. Zhang. 2024. Performance improvement for large language models: Retrieval-augmented generation AI agent for tabular data processing in auditing procedures. Working paper. https://doi.org/10.2139/ssrn.5100205

Yoon, K., L. Hoogduin, and L. Zhang. 2015. Big Data as complementary audit evidence. *Accounting Horizons* 29 (2): 431-438. https://doi.org/10.2308/acch-51076

## APPENDIX

Appendix A. Source Corpus and Filer Manifest.

Appendix B. Text Retrieval Store and Chunking.

Appendix C. XBRL Fact and Relation Store.

Appendix D. Prompt and Retrieval Context Archive.

Appendix E. LLM Run Configuration and Output Archive.

Appendix F. Claim-Level Coding Package, including Appendix Table F1, Claim-Level Coding Scope, Appendix Table F2, Retrieval Failure Mode Taxonomy, and Appendix Table F3, Main Deep-Case Preliminary Coding Summary.

Appendix G. Source Spot Checks and Selected Examples.

Appendix H. Bounded Extension Evidence, including Appendix Table H1, Bounded-Extension Filer Selection, Appendix Table H2, Bounded-Extension Retrieval Diagnostics, Appendix Table H3, Bounded-Extension LLM and Coding Scope, Appendix Table H4, Selected Bounded-Extension Examples, and Appendix Table H5, Bounded-Extension Preliminary Coding Summary.

Appendix I. Sensitivity Guidance and Boundary Conditions, including Appendix Table I1, Sensitivity Checks Not Claimed As Completed, Appendix Table I2, Reporting Items Mapped to Validity Dimensions, Appendix Table I3, Text Retrieval Data Structure, Appendix Table I4, XBRL Relational Retrieval Data Structure, and Appendix Table I5, Reproducibility Package Checklist.

The appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration. The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-valid and integrated-correctness coding is preliminary unless independently reviewed by audit-domain experts.
