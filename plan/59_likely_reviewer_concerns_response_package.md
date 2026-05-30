# Likely Reviewer Concerns And Response Package

## Purpose

This file prepares responses to likely AJPT reviewer concerns before submission. The goal is not to write defensive rebuttals, but to ensure the manuscript, appendix, cover letter, and reproducibility package anticipate reviewer questions.

## Overall Reviewer Strategy

The manuscript should repeatedly communicate three ideas:

1. **Scope:** The paper is about LLM-based auditing research methodology, not audit-practice procedures.
2. **Contribution:** Retrieval is a research-design choice because it constructs the LLM's information environment.
3. **Evidence:** The demonstration illustrates claim-level evidence-use divergence; it does not benchmark LLM performance or prove that XBRL improves audit reasoning.

## Response Matrix

| Reviewer Concern | Why The Concern Is Plausible | Response Strategy | Manuscript / Appendix Location |
|---|---|---|---|
| The paper does not fit the AJPT Methodological Papers call because it is not statistical. | The call includes statistical methods, and reviewers may initially associate "methodological" with statistical techniques. | State that the paper fits the call topics on research design and data/variable construction. Emphasize that the call is broader than statistical technique evaluation. | Cover letter; Introduction first two pages; `plan/57`. |
| The paper sounds like an audit-practice tool. | LLM, RAG, XBRL, and audit workflow language can imply engagement-level recommendations. | State that the object is auditing research design, not audit engagement execution. Avoid "audit workflow" and "audit procedure" framing. | Abstract; Introduction; Discussion boundary conditions; cover letter. |
| Retrieval-environment validity is just construct validity with a new name. | Reviewers may see the five dimensions as a relabeling of established validity concepts. | Emphasize the dynamic materials-boundary problem: corpus, prompt, and model do not determine what the LLM sees; retrieval creates the information environment at runtime. | Section III; Figure 1; Table 1; contribution paragraph. |
| XBRL is not audit evidence or ground truth. | Audit reviewers will resist any claim that management-reported XBRL validates audit assertions. | Explicitly define XBRL as management-reported structured accounting data. Separate graph-valid correctness from audit-valid correctness. | Sections IV and V; Table 5; Discussion. |
| The paper overstates the value of XBRL relational retrieval. | The phrase "XBRL-augmented" may sound like XBRL improves LLM reasoning. | Present XBRL retrieval as construct-specific and useful for representation/traceability of reported relations, not as universally superior. | Retrieval typology; construct-to-retrieval mapping; demonstration interpretation. |
| The demonstration is too small. | Three deep cases and six extension cases are not representative of SEC filers. | Use two-layer framing: main cases for traceability, bounded extension for maximum-variation applicability. State no population inference. | Section VII; Appendix H; `plan/53`; `plan/54`. |
| The bounded extension was added opportunistically. | Reviewers may worry that extension cases were added after inspecting outputs. | Document the extension's purpose as a scope/generalizability response, not performance search. Separate main and extension roles in manifests and reports. | `config/filer_manifest.json`; Appendix A/H; `plan/49` through `plan/54`. |
| Claim-level audit-valid coding lacks external validation. | Audit-valid and integrated correctness involve professional judgment. | Keep audit-valid scores preliminary unless expert reviewed. Interpret main findings around evidence-use divergence and traceability. Add expert-review plan or limited expert review. | Section V; Section VII; Appendix F/G/I. |
| The aggregate coding table looks like performance evidence. | Means by condition can invite ranking of retrieval methods or model quality. | Move Table 9A/9B to appendix and label as transparency artifacts. In main text, use selected examples and qualitative inference shifts. | Table package; Appendix F/H; demonstration section. |
| The paper is too technical or systems-oriented. | XBRL relation paths, RDF/OWL, retrieval pipelines, and scripts may feel like information systems engineering. | Keep technical implementation in appendix. In main text, discuss retrieval as research design and source traceability. | Sections III-VI; appendix implementation specs. |
| The paper is a checklist rather than a theory contribution. | Many tables, reporting items, and protocols can make the paper feel procedural. | Anchor all tools to retrieval-environment validity and show how each tool addresses a validity dimension. | Section III framing; Table 2; Section VI. |
| The literature review does not establish novelty. | The paper overlaps XBRL, textual analysis, LLM accounting, and audit analytics. | Use contrast sentences: prior work studies data/model/tool; this paper studies retrieval-created information environments. | Section II; literature positioning table. |
| The prototype is not true vector RAG or GraphRAG. | Readers may expect embeddings, vector databases, RDF/OWL stores, or graph databases. | State prototype is keyword-ranked text and table-based XBRL relational retrieval. Discuss vector/RDF/graph stores as implementation extensions requiring reporting. | Abstract; Section VII; Appendix B/C/I. |
| The LLM choice threatens generalizability. | A local `gemma4:31b` run may not represent all LLMs. | Treat model as controlled demonstration environment. The method applies across models; model comparison is a Tier 2/3 sensitivity check, not required for the Tier 1 demonstration. | Section VII methods; Appendix E/I. |
| The demonstration uses familiar firms, so model pretraining may contaminate outputs. | Nike, Starbucks, and Target are likely known to LLMs. | Include LLM-only diagnostic baseline and evaluate only against retrieved evidence. Use bounded extension to reduce familiarity concern. | Section VII; Appendix D/E/F/H. |
| The paper lacks a clear "what should researchers do differently?" answer. | Methodological papers must change research practice. | State action list: define construct before retrieval, choose retrieval operator, log evidence, code claims, separate graph/text/audit validity, report sensitivity. | Introduction; Section VI; Conclusion. |

## High-Priority Preemptive Wording

### Call Fit

> The manuscript fits the AJPT Methodological Papers call's topics on research design and data/variable construction. It evaluates retrieval as a research-design choice in LLM-based auditing studies and provides best-practice guidance for collecting retrieval evidence, constructing claim-level evidence-use variables, and reporting retrieval-created information environments.

### Novelty

> Prior work studies text as data, XBRL as data, audit analytics tools, or LLM outputs. This paper studies the retrieval-created information environment that connects data sources to LLM-generated claims and, therefore, to research inference.

### XBRL Boundary

> XBRL relation data are management-reported structured accounting data. They can support representation and traceability of reported relationships, but they are not audit evidence, ground truth, or substitutes for auditor judgment.

### Demonstration Boundary

> The demonstration is designed to illustrate how retrieval design changes the evidence basis of LLM-generated claims. It is not designed to rank retrieval methods, estimate population failure rates, or evaluate model audit expertise.

### Expert Coding Boundary

> Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics unless independently reviewed by audit-domain experts. The manuscript's main inference relies on source traceability and claim-level evidence-use divergence rather than on performance-like audit-validity rates.

## Reviewer Response Drafts

### Concern: This is not a statistical methodology paper.

Response:

> We agree that the manuscript does not introduce a new statistical estimator or evaluate existing statistical techniques. The AJPT Methodological Papers call, however, also identifies research design, modeling, variable selection, data collection, and variable construction as methodological topics. The manuscript contributes in those areas by treating retrieval as a research-design choice in LLM-based auditing research and by providing guidance for constructing claim-level evidence-use variables from retrieval logs, prompt contexts, XBRL facts and relation paths, and LLM outputs.

### Concern: The paper is about audit practice, not auditing research methodology.

Response:

> The manuscript is not intended to prescribe audit procedures, audit workflows, or auditor decision aids. Its object is the design and evaluation of LLM-based auditing research. The framework helps researchers specify audit constructs, choose retrieval designs, document the information environment supplied to the LLM, and evaluate output claims. We have revised the manuscript to use "auditing research" language consistently and to avoid practice-implementation claims.

### Concern: XBRL is management-reported information, so it cannot validate audit assertions.

Response:

> We agree. The manuscript explicitly treats XBRL as management-reported structured accounting data, not as audit evidence or ground truth. This is why the correctness protocol separates graph-valid correctness from audit-valid correctness. A claim may be consistent with XBRL facts and relations while still failing to support a valid audit inference.

### Concern: The demonstration sample is too small.

Response:

> The demonstration is not designed for population inference. The three main cases support deep source tracing and claim-level illustration. The bounded six-filer extension tests whether the protocol remains applicable across varied reporting environments. We do not estimate failure-mode prevalence or model performance from these cases.

### Concern: The paper needs expert validation.

Response:

> We agree that expert validation is necessary for strong audit-validity claims. The current manuscript treats audit-valid and integrated-correctness scores as preliminary diagnostics and does not interpret them as final expert evidence. The main methodological inference relies on traceability and evidence-use divergence. We also identify expert coding as required for studies that make stronger audit-judgment claims.

### Concern: Why use `gemma4:31b`?

Response:

> The model is used as a controlled local demonstration environment, not as the object of evaluation. Holding the model and temperature fixed helps isolate retrieval-created differences across conditions. The framework is model-agnostic; model comparisons are appropriate for stronger empirical or benchmarking studies but are not necessary for the paper's Tier 1 methodological demonstration.

### Concern: Why not implement full vector RAG or RDF/OWL graph retrieval?

Response:

> The demonstration uses an inspectable keyword-ranked text retrieval prototype and table-based XBRL relational retrieval to keep the information environment transparent. Vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions and reporting considerations. The manuscript's contribution is not a production retrieval system; it is a methodology for designing and evaluating retrieval-created information environments.

### Concern: The paper feels like a checklist.

Response:

> The checklist elements operationalize the paper's core validity framework. Each reporting item maps to one or more dimensions of retrieval-environment validity: selection, representation, stability, traceability, and separability. The practical guidance is included because the AJPT Methodological Papers call asks for recommendations and best practices, but the organizing contribution is the validity framework.

## Manuscript Hardening Checklist

| Action | Priority | Status |
|---|---|---|
| Include call-fit sentence in Introduction | High | Drafted in `plan/56`. |
| Keep XBRL boundary in abstract, retrieval section, and discussion | High | Drafted, must preserve in v3. |
| Move aggregate coding tables to appendix | High | Reflected in `plan/41` and `plan/56`. |
| Add expert-review limitation or plan | High | Needed in v3. |
| Replace internal file references with appendix labels in final manuscript | High | Needed in v3. |
| Create clean appendix index | High | Partially addressed in `plan/43`; finalize later. |
| Polish literature contrast sentences | Medium | Needed in v3. |
| Add final "what researchers should do differently" paragraph | Medium | Drafted in `plan/56`; preserve in v3. |
| Finalize AI disclosure and data availability statement | Medium | Needed before submission. |
| Confirm author declarations | Medium | Needed before submission. |

## Final Assessment

The likely reviewer concerns are manageable if the manuscript keeps a disciplined position. The most dangerous risks are overclaiming audit validity, sounding like an audit-practice tool, or letting aggregate coding appear as model-performance evidence. The strongest defense is not a rebuttal after review; it is a manuscript that repeatedly frames retrieval as a research-design and data/variable-construction problem in LLM-based auditing research.
