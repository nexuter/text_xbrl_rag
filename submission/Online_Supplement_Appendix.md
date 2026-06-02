# V3 Appendix And Online Supplement

## Purpose

This appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration in:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval**

The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-boundary coding remains preliminary unless independently reviewed by audit-domain experts; source-use type and integrated correctness are independently coded in the 120-claim validation sample to evaluate protocol reliability.

## Reviewer-Facing Boundary Statement

The appendix supports three bounded manuscript claims:

1. Retrieval creates the information environment from which LLM audit-research inferences are drawn.
2. Text retrieval, XBRL relational retrieval, and hybrid retrieval create distinguishable evidence environments.
3. Retrieval-condition labels do not determine claim-level evidence use; claim-level coding is required.

The appendix does not support claims that a hybrid condition is superior, that XBRL improves audit reasoning, that the selected LLM has general audit expertise, or that preliminary author-coded audit-boundary diagnostics are final audit-judgment evidence.

## Appendix Map

| Appendix | Title | Reviewer Question | Validity Function |
|---|---|---|---|
| A | Source Corpus, Filer Manifest, and Construct Protocols | What filed documents created the source universe, and what construct boundaries govern revenue and inventory tasks? | Selection, construct alignment, and traceability |
| B | Text Retrieval Store and Chunking | How was narrative filing evidence represented and retrieved? | Selection, representation, and stability |
| C | XBRL Fact, Relation, and Construct-Coverage Store | How were reported accounting facts and relations represented, and did retrieved XBRL materials cover the ex ante construct families? | Representation, traceability, and construct alignment |
| D | Prompt and Retrieval Context Archive | What exactly did the LLM see? | Traceability and separability |
| E | LLM Run Configuration and Output Archive | Were outputs generated under controlled model settings? | Stability and separability |
| F | Claim-Level Coding Package | How were outputs converted into research variables? | Traceability and representation |
| G | Source Spot Checks and Selected Examples | Can selected claims be traced back to filed evidence? | Traceability |
| H | Bounded Extension Evidence | Does the protocol remain applicable beyond the deep cases? | Selection and boundary-condition assessment |
| I | Sensitivity Guidance and Boundary Conditions | What would stronger empirical claims require? | Stability and separability |

## Appendix A. Source Corpus, Filer Manifest, And Construct Protocols

Appendix A documents the public SEC 10-K and Inline XBRL source universe used to construct the retrieval environments. The filer manifest records company identity, ticker, CIK, filing year, accession metadata where available, sample role, and construct role. The appendix also states the ex ante construct protocols used for revenue recognition risk and inventory valuation assertion. Raw SEC files, download records, and extraction summaries are retained in the replication package.

### Appendix Table A1. Filer Manifest Summary

| Ticker | Company | Role | Constructs | Methodological Purpose |
|---|---|---|---|---|
| NKE | Nike | Main deep case | Revenue and inventory | Familiar consumer-facing filer for source tracing and evidence-use illustration |
| SBUX | Starbucks | Main deep case | Revenue and inventory | Familiar consumer-facing filer with interpretable inventory and revenue disclosures |
| TGT | Target | Main deep case | Revenue and inventory | Familiar retail filer with inventory and revenue reporting relevance |
| WMT | Walmart | Bounded extension | Revenue and inventory | Mega-scale retail extension case |
| HD | Home Depot | Bounded extension | Revenue and inventory | Specialty-retail extension case |
| CAT | Caterpillar | Bounded extension | Revenue and inventory | High-complexity industrial stress case |
| PFE | Pfizer | Bounded extension | Revenue and inventory | Pharma/product-risk reporting extension case |
| MSFT | Microsoft | Bounded extension | Revenue and inventory | Revenue-recognition setting and relation-path scarcity boundary case |
| CROX | Crocs | Bounded extension | Revenue and inventory | Mid-size consumer-product extension case |

What this supports: The demonstration uses actual public filing and Inline XBRL sources across nine active filers.

What this does not support: The sample is not representative of all SEC filers and does not establish audit evidence quality or population-level generalizability.

### Appendix Table A2. Ex Ante Construct Protocol: Revenue Recognition Risk

| Protocol Element | Specification |
|---|---|
| Construct label | Revenue recognition risk from public filing and XBRL materials |
| Audit-standard anchor | Assertion-level risk assessment and response design require identifying relevant assertions and obtaining sufficient appropriate audit evidence before an audit conclusion |
| Primary account / disclosure area | Revenue, contract liabilities, refund liabilities, return obligations, disaggregation, performance obligations, variable consideration, and revenue policy disclosures |
| Assertion relevance | Occurrence, completeness, accuracy, cut-off, classification, and presentation |
| Text retrieval should capture | Revenue recognition policy language, performance-obligation descriptions, variable consideration language, refund/return policy language, customer concentration or channel disclosures, and revenue risk-factor context where construct-relevant |
| XBRL retrieval should capture | Revenue amounts, disaggregated revenue tags where available, contract liabilities, refund liabilities, deferred revenue, revenue-related contexts, periods, units, dimensions, and relation paths linking revenue-related concepts |
| Claims supported by current evidence | Filing-supported factual claims about disclosed policies or reported amounts; graph-valid claims about retrieved XBRL facts/paths; assertion-relevant diagnostics about why a disclosed policy or reported relation could matter for revenue risk |
| Claims not supported by current evidence | Claims that revenue is materially misstated, that recognition is GAAP-noncompliant, that controls failed, that fraud occurred, or that the auditor obtained sufficient appropriate evidence |
| Task success criterion | Source-traceable identification of public-filing or XBRL-reported revenue information that is assertion-relevant, paired with explicit avoidance of misstatement, fraud, control-failure, GAAP-noncompliance, or audit-evidence-sufficiency conclusions |
| Valid claim example | "The filing describes multiple performance obligations and reports contract liabilities, which are assertion-relevant to timing and completeness considerations." |
| Invalid or overreaching claim example | "The company prematurely recognized revenue" unless supported by external audit evidence, expert review, and a design capable of testing misstatement |
| Coding boundary | Code factual and graph-valid support separately from audit-boundary diagnostics; do not aggregate audit-boundary scores as final audit-judgment evidence |

### Appendix Table A3. Ex Ante Construct Protocol: Inventory Valuation Assertion

| Protocol Element | Specification |
|---|---|
| Construct label | Inventory valuation assertion from public filing and XBRL materials |
| Audit-standard anchor | Assertion-level risk assessment and response design require identifying relevant assertions and obtaining sufficient appropriate audit evidence before an audit conclusion |
| Primary account / disclosure area | Inventory, inventory reserves, write-downs, obsolescence, lower-of-cost-or-market or lower-of-cost-and-net-realizable-value policy, costing method, LIFO/FIFO disclosures, and related presentation |
| Assertion relevance | Valuation, existence, completeness, rights and obligations where disclosed, and presentation/classification |
| Text retrieval should capture | Inventory accounting policy, reserve and write-down descriptions, obsolescence discussion, costing-method disclosures, product-return or markdown discussion, and inventory-related risk context |
| XBRL retrieval should capture | Inventory balances, inventory components where available, inventory reserves or write-down concepts where tagged, cost-flow concepts, periods, units, dimensions, and relation paths linking inventory-related concepts |
| Claims supported by current evidence | Filing-supported factual claims about disclosed inventory policies or reported balances; graph-valid claims about retrieved inventory facts/paths; assertion-relevant diagnostics about valuation or presentation considerations |
| Claims not supported by current evidence | Claims that inventory physically exists, that net realizable value is correct, that reserves are sufficient, that management bias exists, or that the auditor obtained sufficient appropriate evidence |
| Task success criterion | Source-traceable identification of public-filing or XBRL-reported inventory information that is assertion-relevant, paired with explicit avoidance of physical-existence, reserve-adequacy, valuation-correctness, management-bias, or audit-evidence-sufficiency conclusions |
| Valid claim example | "The filing reports inventory balances and describes reserve or write-down policies, which are assertion-relevant to inventory valuation." |
| Invalid or overreaching claim example | "Inventory is fairly valued" unless supported by audit procedures, external evidence, expert review, and a design capable of testing valuation |
| Coding boundary | Code text support and graph validity separately; use audit-boundary diagnostics only to flag whether the claim stays within the limits of public filing and XBRL support |

## Appendix B. Text Retrieval Store And Chunking

Appendix B makes text retrieval inspectable at the chunk level. In the current Tier 1 demonstration, text retrieval is implemented as keyword-ranked contextual retrieval over extracted 10-K text chunks. Vector database construction, embedding model selection, chunk-size sensitivity, and overlap sensitivity are reported as guidance for future Tier 2 or Tier 3 studies, not as completed benchmark evidence in this paper.

### Appendix Table B1. Text Retrieval Store Diagnostics

| Ticker | Text Chunks | Retrieval Unit | Current Retrieval Operator |
|---|---:|---|---|
| NKE | 184 | Filing text chunk | Keyword-ranked contextual retrieval |
| SBUX | 122 | Filing text chunk | Keyword-ranked contextual retrieval |
| TGT | 103 | Filing text chunk | Keyword-ranked contextual retrieval |
| WMT | 120 | Filing text chunk | Keyword-ranked contextual retrieval |
| HD | 125 | Filing text chunk | Keyword-ranked contextual retrieval |
| CAT | 213 | Filing text chunk | Keyword-ranked contextual retrieval |
| PFE | 196 | Filing text chunk | Keyword-ranked contextual retrieval |
| MSFT | 150 | Filing text chunk | Keyword-ranked contextual retrieval |
| CROX | 164 | Filing text chunk | Keyword-ranked contextual retrieval |
| Total | 1,377 | Filing text chunk | Keyword-ranked contextual retrieval |

Minimum disclosure items for future text-retrieval studies include chunk identifier, source filer, source section where available, chunking rule, chunk size, overlap policy, tokenizer or word-count rule, embedding/index metadata if used, similarity metric, metadata filters, top-k rule, reranking policy, context budget, and prompt inclusion rule.

Reader-facing mechanics note: in the current demonstration, the baseline text environment is a keyword-ranked top-5 chunk design. Appendix I reports deterministic top-3 and top-8 perturbations to show how changing the text source budget changes the source environment before model inference. Chunk-size and overlap variation are not claimed as completed tests in this Tier 1 demonstration; they are listed as required design choices for Tier 2 empirical LLM audit studies and Tier 3 retrieval-system evaluations.

What this supports: Narrative retrieval units were constructed and logged consistently enough for source traceability and claim-level coding.

What this does not support: The current prototype does not claim production vector RAG performance or optimal text-retrieval settings.

## Appendix C. XBRL Fact, Relation, And Construct-Coverage Store

Appendix C documents XBRL facts and relation paths used as relational retrieval inputs. The current demonstration uses table-based fact and path retrieval. RDF/OWL and graph database formats are treated as portability and reporting extensions unless separately implemented. Appendix C also reports a construct-coverage diagnostic that links the ex ante revenue and inventory protocols in Appendix A to the XBRL facts and relation paths actually supplied to the LLM.

### Appendix Table C1. XBRL Fact And Relation Diagnostics

| Ticker | XBRL Facts | XBRL Relation Paths | Diagnostic Meaning |
|---|---:|---:|---|
| NKE | 365 | 99 | Main deep case with usable relation paths |
| SBUX | 135 | 210 | Main deep case with rich relation-path evidence |
| TGT | 102 | 79 | Main deep case with moderate relation-path evidence |
| WMT | 141 | 109 | Retail extension case |
| HD | 173 | 174 | Specialty-retail extension case |
| CAT | 1,047 | 574 | High-complexity industrial stress case |
| PFE | 336 | 272 | Pharma/product-risk extension case |
| MSFT | 144 | 0 | Revenue boundary case showing relation-path scarcity |
| CROX | 123 | 102 | Mid-size consumer-product extension case |
| Total | 2,566 | 1,619 | Full demonstration corpus |

### Appendix Table C2. Ex Ante XBRL Construct-Coverage Diagnostic By Filer

| Ticker | Construct | Covered Families | Missing Families | Diagnostic Status |
|---|---|---:|---|---|
| CAT | Inventory | 4/5 | Inventory movements | Partial family coverage |
| CAT | Revenue | 4/5 | Refunds, returns, or variable consideration | Partial family coverage |
| CROX | Inventory | 4/5 | Inventory components | Partial family coverage |
| CROX | Revenue | 5/5 | None | Complete family coverage |
| HD | Inventory | 2/5 | Inventory components; inventory movements; valuation reserve or obsolescence | Partial family coverage |
| HD | Revenue | 4/5 | Refunds, returns, or variable consideration | Partial family coverage |
| MSFT | Inventory | 3/5 | Inventory components; valuation reserve or obsolescence | Partial family coverage |
| MSFT | Revenue | 3/5 | Receivables or collectibility; refunds, returns, or variable consideration | Partial family coverage |
| NKE | Inventory | 5/5 | None | Complete family coverage |
| NKE | Revenue | 4/5 | Contract liability or deferred revenue | Partial family coverage |
| PFE | Inventory | 4/5 | Inventory movements | Partial family coverage |
| PFE | Revenue | 2/5 | Contract liability or deferred revenue; receivables or collectibility; refunds, returns, or variable consideration | Partial family coverage |
| SBUX | Inventory | 3/5 | Cost flow or COGS; inventory movements | Partial family coverage |
| SBUX | Revenue | 3/5 | Receivables or collectibility; refunds, returns, or variable consideration | Partial family coverage |
| TGT | Inventory | 4/5 | Inventory components | Partial family coverage |
| TGT | Revenue | 5/5 | None | Complete family coverage |
| WMT | Inventory | 2/5 | Inventory components; inventory movements; valuation reserve or obsolescence | Partial family coverage |
| WMT | Revenue | 4/5 | Refunds, returns, or variable consideration | Partial family coverage |

The diagnostic reviews 18 construct-filer cells. Three cells show complete expected-family coverage and 15 show partial coverage. This is not a model-performance result. It shows whether the XBRL retrieval environment surfaced expected construct families before LLM outputs are interpreted. Missing families are retrieval-design diagnostics; they do not show that the filer failed to disclose the topic, that the assertion is misstated, or that audit evidence is insufficient.

### Appendix Table C3. Ex Ante XBRL Construct-Coverage Diagnostic By Concept Family

| Construct | Concept Family | Filers With Any Hit | Filers With Fact Hit | Filers With Relation-Path Hit |
|---|---|---:|---|---|
| Revenue | Revenue or sales amount | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| Revenue | Contract liability or deferred revenue | 7/9 | CAT; CROX; HD; MSFT; SBUX; TGT; WMT | CAT; CROX; SBUX; TGT |
| Revenue | Refunds, returns, or variable consideration | 3/9 | CROX; NKE | NKE; TGT |
| Revenue | Receivables or collectibility | 6/9 | CROX; HD; NKE; WMT | CAT; TGT |
| Revenue | Disaggregation or customer dimension | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| Inventory | Inventory balance | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| Inventory | Inventory components | 4/9 | CAT; NKE; PFE; SBUX | CAT; NKE; PFE; SBUX |
| Inventory | Valuation reserve or obsolescence | 6/9 | CAT; CROX; NKE; PFE; SBUX; TGT | CAT; CROX; NKE; PFE; SBUX; TGT |
| Inventory | Cost flow or COGS | 8/9 | CAT; CROX; HD; MSFT; NKE; TGT; WMT | CROX; HD; NKE; PFE; TGT; WMT |
| Inventory | Inventory movements | 4/9 | CROX; MSFT; NKE; TGT | CROX; NKE; TGT |

The construct-coverage diagnostic is generated from the retrieval log and the XBRL fact/path stores. It evaluates coverage of reported XBRL concept families and relation paths, not model accuracy or audit evidence sufficiency.

### Appendix Table C4. Worked Example: Source-To-Claim Trace For NKE Inventory Valuation

| Trace Element | Example |
|---|---|
| Construct and filer | Inventory valuation assertion, NKE |
| Retrieval contexts | `nke_inventory_xbrl_context.txt` and `nke_inventory_hybrid_context.txt` |
| Key XBRL facts | `F-NKE-0026`, InventoryValuationReserves, 233 million USD, instant:2025-05-31; `F-NKE-0027`, InventoryValuationReserves, 155 million USD, instant:2024-05-31 |
| Key relation paths | `X-NKE-0067`, definition relation from `nke:SignificantAccountingPoliciesLineItems` to `us-gaap:InventoryValuationReserves`; `X-NKE-0015`, presentation relation to the same reserve concept |
| Rendered XBRL context | Fact IDs, concepts, values, units, periods, dimensions, path IDs, relation types, source and target concepts, arcroles, and role URIs |
| Hybrid text context | Retrieved filing text describing inventory reserve policy and the reported reserve increase from 2024 to 2025 |
| XBRL-only factual claim | Claim `C021`: 2025 inventory valuation reserves were 233 million USD, supported by `F-NKE-0026`; coded graph-valid as a bounded factual claim |
| XBRL-only risk-cue claim | Claim `C023`: the reserve increase is a risk cue for inventory valuation, supported by `F-NKE-0026` and `F-NKE-0027`; coded partly graph-valid because the numeric change is supported but the risk inference exceeds XBRL facts alone |
| Hybrid factual claim | Claim `C027`: the 2025 reserve was 233 million USD, up from 155 million USD in 2024, supported by text and XBRL; coded as integrated because both evidence layers support the same factual statement |
| Hybrid risk-cue claim | Claim `C029`: the reserve increase is a risk cue for reserve adequacy, supported by text and XBRL; coded as integrated, but reserve adequacy remains an audit-boundary diagnostic rather than an audit conclusion |

This example shows how the same reported XBRL facts can support different coding conclusions depending on claim type. A bounded factual claim can be graph-valid. A risk-cue claim can be source-traceable and assertion-relevant, but it still requires professional judgment and additional audit evidence before becoming an audit conclusion.

### Appendix Table C5. Representation-Risk Example: Period And Dimension Mismatch

| Risk Element | Example |
|---|---|
| Source facts | `F-NKE-0353`, `F-NKE-0354`, and `F-NKE-0355` report finished-goods inventory net of reserves by geography |
| Period | All three facts are instant:2023-05-31 |
| Dimensions | North America, Europe/Middle East/Africa, and Greater China segment members |
| Representation risk | These facts should not be used as current 2025 segment-level inventory evidence |
| Affected claim type | A claim that maps the 2025 inventory reserve increase to specific geographic segments using only these facts would require a period-mismatch warning |
| Design response | Preserve period, context, and dimension metadata in the rendered retrieval context; code claims at the claim level rather than accepting a response-level XBRL condition label |

This example illustrates why XBRL relational retrieval must preserve context metadata. Concept labels alone are insufficient. A retrieved concept can be construct-relevant but still unsuitable for a particular inference if the period, unit, dimension, or relation role does not match the claim.

Minimum disclosure items for future XBRL relational retrieval studies include fact identifier, concept QName, concept label, value, unit, decimals, period, dimensions, source context, relation path identifier, source concept, target concept, relation type, arcrole, role, traversal depth, taxonomy/linkbase source, taxonomy year or version, and extension-concept policy.

Reader-facing mechanics note: the current XBRL retrieval environment renders facts and relation paths as table-based source bundles rather than as an implemented RDF/OWL graph database. Appendix I reports a fact-only perturbation to show why relation paths matter: removing paths changes the retrieved source environment materially even when reported facts remain available. Relation traversal-depth and relation-filter sensitivity are therefore treated as required Tier 2 or Tier 3 checks when a study makes stronger claims about XBRL relational retrieval or GraphRAG performance.

What this supports: XBRL relational retrieval creates a distinct reported-structure information environment from narrative text retrieval, and construct-family diagnostics can show whether the retrieved XBRL environment aligns with the construct before LLM outputs are interpreted.

What this does not support: XBRL facts and relation paths are management-reported structured data. They do not establish audit evidence sufficiency, misstatement, fraud, or audit truth.

## Appendix D. Prompt And Retrieval Context Archive

Appendix D preserves the actual information environment supplied to the LLM. This is the central traceability archive for retrieval-environment validity because it documents what the model saw rather than what the researcher intended it to see.

### Appendix Table D1. Prompt And Retrieval Context Scope

| Item | Count |
|---|---:|
| Main deep-case prompt/context conditions | 24 |
| Bounded-extension prompt/context conditions | 48 |
| Total prompt/context conditions | 72 |
| Retrieval log rows | 464 |

Each run is identified by filer, construct, retrieval condition, and run identifier. The archive preserves rendered prompts, text chunks, XBRL fact identifiers, XBRL path identifiers, source IDs, and context assembly rules. The LLM-only condition is retained as a diagnostic baseline for traceability and possible pretraining-contamination concerns.

The full-scale extension now applies the same two-construct, four-condition grid to each additional filer. The resulting package includes nine filers, two constructs, and four retrieval conditions.

What this supports: Reviewers can inspect the information environment actually supplied to the LLM for each retrieval condition.

What this does not support: The archive does not establish that the supplied information was sufficient for an audit conclusion.

## Appendix E. LLM Run Configuration And Output Archive

Appendix E documents model execution settings and output preservation. The paper uses a single controlled local model for the methodological demonstration. The model choice is not a claim of superiority.

### Appendix Table E1. LLM Run Configuration

| Field | Value |
|---|---|
| Provider | Ollama |
| Model | `gemma4:31b` |
| Temperature | 0.0 |
| Main outputs | 24 |
| Extension outputs | 48 |
| Total outputs | 72 |
| Output errors | 0 |

Exact third-party output replication may depend on local model builds, hardware, and serving environment. The replication package preserves the available local model metadata note; if a model digest is unavailable, exact third-party output replication should be interpreted with caution.

What this supports: Outputs were generated under a consistent local model configuration.

What this does not support: The appendix does not establish cross-model robustness or general audit expertise of the selected model.

## Appendix F. Claim-Level Coding Package

Appendix F shows how LLM outputs were converted into claim-level research variables. This is central to the paper's data and variable-construction contribution.

### Appendix Table F1. Claim-Level Coding Scope

| Item | Count |
|---|---:|
| Main coded claims | 94 |
| Extension coded claims | 187 |
| Total coded claims | 281 |
| Factual claims | 115 |
| Risk/assertion-mapping claims | 147 |
| Insufficient-context claims | 19 |
| Claims requiring manual or expert review for audit-boundary use | 281 |

### Appendix Table F1A. Audit-Evidence Hierarchy For Coding Boundaries

| Level | Meaning | Current Demonstration Status | Coding Implication |
|---|---|---|---|
| Public-filing support | The claim is supported by retrieved public SEC filing text | Demonstrated through preserved text chunks and source identifiers | Code as text-supported when the cited or used text supports the claim |
| XBRL graph/reporting support | The claim is consistent with retrieved management-reported XBRL facts, contexts, or relation paths | Demonstrated through fact/path identifiers and graph-valid coding | Code as graph-valid when concept, value, unit, period, context, and relation structure support the claim |
| Assertion relevance | The claim relates to a plausible audit assertion or risk area | Illustrated through revenue and inventory tasks, but strengthened by ex ante construct protocols | Code as risk/assertion-mapping only when the claim makes an assertion-relevant inference |
| Audit-boundary diagnostic | The claim is assessed for whether it overreaches beyond public filing and XBRL support | Preliminary author diagnostic unless independently reviewed by audit-domain experts | Use as a boundary flag, not as final audit-judgment evidence |
| Audit evidence sufficiency | The claim is supported by evidence sufficient and appropriate for an audit conclusion | Not demonstrated in the current public-filing/XBRL package | Do not code the current demonstration as establishing audit evidence sufficiency |

This hierarchy prevents source support from being overread as audit evidence. The current demonstration can show that a claim is text-supported, graph-valid, assertion-relevant, or within a preliminary audit boundary. It does not show that the claim is supported by sufficient appropriate audit evidence.

### Appendix Table F1B. Same Evidence Across Audit Interpretation Levels

| Retrieved Evidence | Claim Type | Supported Interpretation | Unsupported Interpretation |
|---|---|---|---|
| Inventory policy text and XBRL reserve facts | Bounded factual claim | The filing reports an inventory reserve amount and policy language for the relevant period | The reserve is sufficient |
| Inventory policy text and XBRL reserve facts | Assertion-relevant diagnostic | The reserve and policy are relevant to inventory valuation considerations | Inventory is fairly valued |
| Revenue policy text and contract-liability XBRL facts | Bounded factual claim | The filing reports contract-liability amounts and revenue-recognition policy language | Revenue is recognized correctly under GAAP |
| Revenue policy text and contract-liability XBRL facts | Assertion-relevant diagnostic | The evidence is relevant to cut-off, completeness, or accuracy considerations | Revenue is materially misstated or controls failed |
| Any public filing text or XBRL fact/path | Audit evidence sufficiency claim | Not supported by the current public-filing/XBRL package | The auditor obtained sufficient appropriate audit evidence |

This table is the audit-specific boundary condition for the coding protocol. Public filing text and management-reported XBRL can support research variables about source support, graph validity, assertion relevance, and preliminary audit-boundary diagnostics. They do not establish audit evidence sufficiency, misstatement, control failure, fraud, reserve adequacy, or valuation correctness.

### Appendix Table F2. Retrieval Failure Mode Taxonomy

| Failure Mode | Definition | Validity Dimension Most Directly Implicated |
|---|---|---|
| Omission | Relevant source evidence exists but is not retrieved or not used | Selection |
| Distortion | Retrieved evidence loses source meaning through extraction, chunking, formatting, or summarization | Representation |
| Retrieval instability | Similar retrieval requests produce materially different evidence environments | Stability |
| Attribution failure | An output claim cannot be traced to retrieved evidence | Traceability |
| Model-retrieval confounding | Output differences cannot be separated from retrieval differences, model behavior, or prompt effects | Separability |
| Relation hallucination | The model invents or misstates an XBRL fact, concept, or relation path | Representation and traceability |
| Source overreach | The model treats management-reported filing data as audit evidence or ground truth | Representation and audit-boundary discipline |
| Integration failure | A hybrid output places text and XBRL evidence together but does not reason across them | Separability and integrated correctness |

### Appendix Table F3. Main Deep-Case Preliminary Coding Summary

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Integrated Bridge Claims | Integrated Bridge Share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 15 | 6 | 9 | 0 | 0.63 | 0.88 | 3 | 0.20 |
| hybrid | revenue | 15 | 6 | 9 | 0 | 0.47 | 0.88 | 0 | 0.00 |
| llm_only | inventory | 3 | 0 | 0 | 3 | NA | NA | NA | NA |
| llm_only | revenue | 3 | 0 | 0 | 3 | NA | NA | NA | NA |
| text | inventory | 13 | 5 | 8 | 0 | 0.69 | NA | NA | NA |
| text | revenue | 15 | 6 | 9 | 0 | 0.70 | NA | NA | NA |
| xbrl | inventory | 15 | 7 | 7 | 1 | NA | 0.70 | NA | NA |
| xbrl | revenue | 15 | 7 | 8 | 0 | NA | 0.73 | NA | NA |

Note: These values are preliminary author-coded diagnostics. The aggregate table reports source-support means and integrated-bridge counts only. One-source hybrid claims are coded as non-integrated under the revised integrated-correctness rule. Audit-boundary coding remains claim-level and requires independent audit-domain review before being treated as audit-judgment evidence.

What this supports: The demonstration is claim-level rather than anecdotal and operationalizes output-to-variable construction.

What this does not support: Audit-boundary scores require independent audit-domain expert review before supporting stronger audit-judgment claims. Integrated correctness is supported as a protocol variable in the independent coding sample, not as evidence of final audit-judgment correctness.

### Appendix Table F4. Independent Coding Validation Evidence

| Item | Current Package |
|---|---|
| Coding protocol | `data/processed/coding/independent_coding_protocol.md` |
| Coded validation sample | `data/processed/coding/independent_coding_results.csv` |
| Reliability summary | `data/processed/coding/intercoder_reliability_summary.md` |
| Disagreement file | `data/processed/coding/independent_coding_disagreements.csv` |
| Sampled claims | 120 |
| Hybrid-condition claims included | 89 of 89 |
| Non-hybrid comparison claims included | 31 |
| Variables to code | Claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, integrated correctness, and confidence; qualitative audit-boundary notes are retained as transparency notes rather than expert audit-valid labels |

The independent coding exercise makes the measurement protocol reviewer-evaluable. The protocol defines a claim as an independently assessable assertion in an LLM output and gives segmentation rules for factual statements, risk/assertion inferences, causal explanations, multi-account claims, caveats, and insufficient-context statements. The sample intentionally includes all hybrid-condition claims because the paper's most important measurement question is whether hybrid-condition outputs actually integrate text and XBRL evidence.

### Appendix Table F4A. Independent Coder Process Documentation

| Process Element | Implementation |
|---|---|
| Coding objective | Evaluate whether the claim-level measurement protocol can be applied consistently by coders using the provided instructions |
| Source archive | Full 281-claim archive from the nine-filer protocol-validation demonstration |
| Validation sample | 120 claims: all 89 hybrid-condition claims and 31 non-hybrid anchors |
| Non-hybrid anchors | 12 LLM-only, 10 XBRL-only, and 9 text-only claims |
| Coder independence | Two coders completed the same sample separately |
| Author-code blinding | Coders received blank coding fields and were not asked to copy or verify author codes |
| Condition visibility | Retrieval condition labels were visible because coders needed them to interpret source availability and integrated-correctness coding |
| Outside-information restriction | Coders were instructed to rely on the provided claim, source, and protocol materials rather than outside company knowledge |
| Materials supplied | Coder instructions, coding protocol, codebook, claim evidence packet, and blank coding form |
| Core variables independently coded | Claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, integrated correctness, and confidence |
| Qualitative audit-boundary notes | Coders could record boundary notes for transparency, but these notes are not treated as expert audit-valid labels or reliability-tested audit-judgment outcomes |
| Reconciliation procedure | Disagreements were preserved in a disagreement file and summarized in reconciliation notes; three focal disagreements involved the factual versus risk/assertion boundary |
| Boundary | Coders validate measurement consistency for source-use and correctness variables; they are not represented as audit-domain expert validators unless separately documented |

This process documentation distinguishes measurement reliability from audit-judgment validation. The independent coding exercise supports the reliability of source-use and correctness variables used in the methodological demonstration. It does not establish model performance, retrieval-method superiority, audit evidence sufficiency, or final audit-judgment correctness.

### Appendix Table F4B. Gate Decision For Audit-Boundary Validation

| Decision Element | Current Revision Position |
|---|---|
| Gate decision | Claim narrowing rather than new audit-domain expert coding |
| Reason | The paper is a retrieval-environment methodology paper, not an audit-judgment validation study |
| Variables with independent reliability evidence | Claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, integrated correctness, and confidence |
| Audit-boundary status | Qualitative preliminary author diagnostic |
| What audit-boundary notes support | Identifying where public filing and XBRL support may end, and where stronger audit evidence would be needed |
| What audit-boundary notes do not support | Final audit-judgment correctness, audit evidence sufficiency, model-performance effects, or retrieval-method superiority |
| Replication file note | Legacy columns such as `audit_valid_prelim` and `audit_valid_rationale` should be interpreted as preliminary audit-boundary diagnostics, not final audit-judgment labels |
| Future Tier 2 requirement | Audit-domain expert coding, expertise documentation, reconciliation, reliability evidence, and stronger retrieval/model sensitivity controls |

This gate decision preserves the paper's methodological scope. The independent coding evidence strengthens measurement credibility for source-use and correctness variables while preventing preliminary audit-boundary notes from being overread as expert audit judgments.

### Appendix Table F5. Independent Coding Reliability Results

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

What this supports: The independent coding results support the reliability of the claim-level measurement protocol for segmentation, claim-kind classification, source-use type, text-supported correctness, graph-valid correctness, and integrated correctness.

Reconciliation note: The disagreement file contains 22 variable-level disagreements: 3 claim-kind disagreements, 3 text-supported correctness disagreements, 1 graph-valid correctness disagreement, and 15 confidence-code disagreements. The three focal substantive disagreements all involve whether accounting-policy statements should be classified as factual claims or risk/assertion inferences; the text-support and graph-valid differences are attached to those same boundary calls. Evidence-use type and integrated correctness have 100.0 percent agreement. The revised `integrated_code` instruction resolves the prior ambiguity by treating ordinary non-integration as `0`, not `NA`.

What this does not support: The coding results do not establish model performance, retrieval-method superiority, or final audit-boundary conclusions. Audit-boundary notes remain qualitative diagnostics, and stronger audit-judgment claims would require additional expert review and reconciliation procedures.

### Appendix Table F6. Hybrid Integration Mechanism Diagnostic

| Mechanism | Claims | Share of Hybrid Claims | Interpretation |
|---|---:|---:|---|
| Integrated text-XBRL bridge | 8 | 9.0% | Claim uses both text and XBRL evidence with an inferential bridge. |
| Text-only within hybrid | 61 | 68.5% | Hybrid prompt was available, but the claim used narrative text only. |
| XBRL-only within hybrid | 20 | 22.5% | Hybrid prompt was available, but the claim used XBRL facts or paths only. |

The mechanism diagnostic decomposes the 89 hybrid-condition claims by the evidence type actually used in each claim. It shows that hybrid non-integration is not primarily a case of claims citing both evidence layers but failing to synthesize them. In the current demonstration, non-integrated hybrid claims primarily arise because the model selects one layer of the hybrid context for a given claim. By construct, inventory includes 7 integrated, 27 text-only, and 10 XBRL-only hybrid claims; revenue includes 1 integrated, 34 text-only, and 10 XBRL-only hybrid claims. These values support the paper's claim-level measurement argument while preserving the boundary that they are protocol diagnostics, not model-performance frequencies.

## Appendix G. Source Spot Checks And Selected Examples

Appendix G links selected manuscript examples back to raw and processed filing evidence. Selected examples are not intended to summarize all coded claims; they illustrate how source IDs, retrieval contexts, LLM outputs, and claim coding connect.

### Appendix Table G1. Selected Example Traceability Requirements

| Requirement | Purpose |
|---|---|
| Example ID | Preserves a stable manuscript-to-appendix link |
| Claim ID | Links the example to the claim-level coding table |
| Run ID | Identifies filer, construct, retrieval condition, and output |
| Retrieved text IDs | Shows whether narrative evidence was available and used |
| Retrieved XBRL fact/path IDs | Shows whether structured evidence was available and used |
| Source verification note | Records whether the processed source was checked against raw filing evidence where feasible |
| Validity lesson | States what the example demonstrates about retrieval-environment validity |

Automated validation checks source-ID resolvability across the output set, while the selected source spot-check archive illustrates substantive source-to-claim traceability for reviewer inspection. The source spot-check archive identified no unresolved source identifiers in the current output set. This supports source traceability by confirming that cited identifiers resolve to preserved retrieved materials, but it does not independently validate all audit-boundary inferences.

What this supports: Selected examples in the manuscript can be traced through source IDs and coding records.

What this does not support: Selected examples do not provide independent expert validation of all 281 coded claims.

## Appendix H. Bounded Extension Evidence

Appendix H addresses the concern that the framework might depend on three familiar deep-case filers. The extension is a maximum-variation methodological check, not a representative empirical sample.

The extension now uses the full two-construct, four-condition design for all six additional filers. Each extension filer contributes revenue and inventory tasks under LLM-only, text, XBRL, and hybrid retrieval conditions, producing 48 extension outputs. The expanded design removes ambiguity about whether the extension is a reduced demonstration while retaining the paper's methodological boundary: the added outputs are used to test protocol applicability and boundary conditions, not to estimate model performance or failure prevalence.

### Appendix Table H1. Demonstration Evidence Layers And Permitted Inferences

| Evidence Layer | Design Scope | What It Supports | What It Does Not Support |
|---|---|---|---|
| Deep source-tracing cases | Three familiar filers, two constructs, four retrieval conditions, 24 outputs, 94 preliminary coded claims | Source-to-context-to-output-to-claim traceability; selected claim-level examples; illustration of correctness layers | Population prevalence, model performance, or general hybrid-retrieval effects |
| Full-scale extension cases | Six additional filers, two constructs, four retrieval conditions, 48 outputs, 187 preliminary coded claims | Bounded protocol applicability across varied reporting environments; visibility of boundary cases such as relation-path scarcity and large XBRL environments | Representative inference about SEC filers or failure-mode frequencies |
| Retrieval-stage sensitivity diagnostics | Eighteen filer-construct cells, context-volume diagnostics, and five source-set perturbation variants | Source-environment separability, context-volume transparency, and identification of cells needing Tier 2 controls | Output-level robustness, prompt sensitivity, cross-model robustness, or retrieval-method superiority |
| Independent coding sample | 120 claims, including all 89 hybrid-condition claims and 31 non-hybrid anchors | Reliability of source-use type, text support, graph validity, and integrated-correctness coding | Audit-domain expert validation of audit-boundary diagnostics or final audit-judgment accuracy |

This design map is the appropriate way to read the nine-filer package. The package is deliberately purposive and layered. It is intended to make the protocol reviewer-evaluable, not to estimate how frequently particular LLM behaviors occur in the population of SEC filers.

### Appendix Table H2. Bounded-Extension Filer Selection

| Ticker | Company | Industry / Setting | Constructs | Methodological Purpose |
|---|---|---|---|---|
| WMT | Walmart | Mega-scale retail | Revenue and inventory | High-volume retail reporting setting |
| HD | Home Depot | Specialty retail / home improvement | Revenue and inventory | Specialty-retail reporting setting |
| CAT | Caterpillar | Industrial manufacturing | Revenue and inventory | High-complexity industrial and LIFO reporting stress case |
| PFE | Pfizer | Pharma / healthcare products | Revenue and inventory | Product, reserve, and regulatory reporting setting |
| MSFT | Microsoft | Software/cloud | Revenue and inventory | Revenue-recognition setting and inventory boundary case |
| CROX | Crocs | Mid-size consumer products / footwear | Revenue and inventory | Size variation and consumer-product reporting setting |

### Appendix Table H3. Bounded-Extension Retrieval Diagnostics

| Ticker | Text Chunks | XBRL Facts | XBRL Relation Paths | Retrieval Diagnostic |
|---|---:|---:|---:|---|
| WMT | 120 | 141 | 109 | Strong retail extension case |
| HD | 125 | 173 | 174 | Strong specialty-retail extension case |
| CAT | 213 | 1,047 | 574 | High-complexity industrial/manufacturing case |
| PFE | 196 | 336 | 272 | Pharma/product-risk extension case |
| MSFT | 150 | 144 | 0 | Revenue-focused boundary case; relation-path scarcity is informative |
| CROX | 164 | 123 | 102 | Mid-size consumer-product extension case |

### Appendix Table H4. Bounded-Extension LLM And Coding Scope

| Ticker | Constructs | Conditions | Output Count | Coded Claims |
|---|---|---|---:|---:|
| WMT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 31 |
| HD | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| CAT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 31 |
| PFE | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| MSFT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 29 |
| CROX | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| Total | Revenue and inventory | LLM-only, text, XBRL, hybrid | 48 | 187 |

### Appendix Table H5. Selected Bounded-Extension Examples

| Example | Filer | Construct | Condition | Claim ID | Claim Role | Claim Summary | Sources | Preliminary Interpretation |
|---|---|---|---|---|---|---|---|---|
| EXT-01 | HD | Inventory | Hybrid | C058 | Integrated factual claim | Merchandise inventories were $25.8 billion as of February 1, 2026. | T-HD-INVENTORY-020; F-HD-0004 | Demonstrates clean text-XBRL corroboration in a specialty retail setting. |
| EXT-02 | CAT | Inventory | Hybrid | C091 | Integrated risk/assertion claim | LIFO use and the LIFO reserve create an inventory valuation consideration. | T-CAT-INVENTORY-016; F-CAT-0048 | Shows possible integration in a high-complexity manufacturing setting; audit-boundary interpretation remains preliminary. |
| EXT-03 | PFE | Inventory | Hybrid | C123 | Integrated risk/assertion claim | Historical inventory write-offs and product return adjustments indicate inventory valuation considerations. | T-PFE-REVENUE_INVENTORY-035; F-PFE-0134 | Extends the protocol to pharma/product-risk reporting. |
| EXT-04 | MSFT | Revenue | Hybrid | C136 | XBRL-only claim within hybrid condition | Current contract liability was $64.555 billion as of June 30, 2025. | F-MSFT-0028 | Demonstrates an XBRL-only claim within this hybrid package. |
| EXT-05 | MSFT | Revenue | Hybrid | C138 | Text-only risk/assertion claim within hybrid condition | SSP estimates and performance-obligation timing create revenue accuracy and cut-off considerations. | T-MSFT-REVENUE-089 | Demonstrates a text-only risk/assertion claim within this hybrid package. |

### Appendix Table H6. Bounded-Extension Preliminary Coding Summary

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Integrated Bridge Claims | Integrated Bridge Share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 29 | 14 | 15 | 0 | 0.45 | 0.85 | 4 | 0.14 |
| hybrid | revenue | 30 | 13 | 17 | 0 | 0.53 | 0.86 | 1 | 0.03 |
| llm_only | inventory | 6 | 0 | 0 | 6 | NA | NA | NA | NA |
| llm_only | revenue | 6 | 0 | 0 | 6 | NA | NA | NA | NA |
| text | inventory | 29 | 12 | 17 | 0 | 0.71 | NA | NA | NA |
| text | revenue | 30 | 12 | 18 | 0 | 0.70 | NA | NA | NA |
| xbrl | inventory | 29 | 13 | 16 | 0 | NA | 0.72 | NA | NA |
| xbrl | revenue | 28 | 14 | 14 | 0 | NA | 0.75 | NA | NA |

Note: These values are preliminary author-coded diagnostics. The table does not aggregate audit-boundary scores because those judgments require independent audit-domain review before supporting audit-judgment claims.

What this supports: The protocol can be applied across varied reporting environments, and boundary cases are visible through retrieval diagnostics.

What this does not support: The extension does not estimate population-level performance, failure-mode prevalence, or retrieval-method superiority.

## Appendix I. Sensitivity Guidance And Boundary Conditions

Appendix I separates the current Tier 1 methodological protocol-validation demonstration from the additional evidence required for stronger empirical, model-performance, or system-performance claims. The current paper documents the inspectability of the retrieval protocol; it does not estimate model-performance effects. Appendix Table I1A specifies the additional design features that would be required if future studies use this framework to test whether retrieval design improves LLM audit outputs.

### Appendix Table I1A. Tier 2 Model-Validation Extension Design

| Design Component | Minimum Model-Validation Design | Stronger Design | Why It Matters |
|---|---:|---:|---|
| Filers | 12 | 20-24 | Creates cross-filer variation without claiming full SEC representativeness |
| Constructs | 2: revenue and inventory | 2 or more, pre-specified | Separates construct-specific retrieval fit from general model behavior |
| Retrieval conditions | 4: LLM-only, text, XBRL, hybrid | Same across all sampled filers | Treats retrieval as an experimental research-design factor |
| Base outputs | 96 | 160-192 | Provides enough task-output observations across filer, construct, and condition cells |
| Prompt/retrieval sensitivity outputs | 48-96 | 88-160 or targeted subset | Tests stability without turning the study into an unrestricted benchmark |
| Expected coded claims | 384-576 | 700-1,200 | Provides claim-level variation while preserving nesting within outputs |
| Independent expert-coded claims | At least 120 | 200-300 or all risk/assertion claims | Supports audit-boundary and integrated correctness claims |
| Expert coders | Two audit-domain coders | Two or more, with adjudication | Provides reliability evidence and reduces author-coding concern |
| Reliability evidence | Percent agreement and kappa or alpha where appropriate | Same plus disagreement taxonomy | Makes audit-boundary coding reviewer-evaluable |
| Statistical structure | Claims nested within task outputs and filers | Mixed or clustered models plus sensitivity tables | Avoids treating multiple claims from one output as independent |
| Primary outcomes | Source-reference validity, unsupported/overreaching claims, evidence-use type, construct-relevant retrieval coverage | Same plus pre-registered secondary outcomes | Aligns evidence with retrieval-environment validity rather than broad model quality |

The minimum design is not a universal sample-size rule. It is a design threshold based on the number of factors a model-validation claim would need to cover: retrieval condition, audit construct, filer, industry or reporting environment, prompt variation, retrieval variation, and expert-coded audit-boundary judgments. Smaller samples may be appropriate for qualitative or protocol-validation claims; broader samples are necessary when researchers claim model-performance effects or failure-mode prevalence.

### Appendix Table I1. Context-Volume Diagnostics By Retrieval Condition

| Condition | Contexts | Mean Context Words | Median | Min | Max | Mean Prompt Words | Mean Text Chunks | Mean XBRL Facts | Mean XBRL Paths |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Hybrid | 18 | 691.3 | 718.5 | 278 | 885 | 862.9 | 5.0 | 11.9 | 8.9 |
| LLM-only | 18 | 10.0 | 10.0 | 10 | 10 | 181.6 | 0.0 | 0.0 | 0.0 |
| Text | 18 | 602.6 | 594.0 | 249 | 929 | 774.2 | 5.0 | 0.0 | 0.0 |
| XBRL | 18 | 524.2 | 542.5 | 192 | 666 | 695.8 | 0.0 | 11.9 | 8.9 |

The context-volume diagnostic makes separability concerns inspectable. Hybrid contexts contain both narrative chunks and structured facts/paths and therefore supply more total information on average than either single-source retrieval condition. Across the 18 hybrid contexts, the mean text/XBRL word-imbalance ratio is 1.37, the median is 1.32, and the maximum is 2.15. These values are reported as a Tier 1 transparency diagnostic. They do not constitute a matched-budget sensitivity test, but they identify the specific information-volume differences that Tier 2 model-validation studies should control.

### Appendix Table I2. Source-Environment Perturbation Diagnostics

| Variant Group | Variant | Cells | Mean Jaccard | Median Jaccard | Mean Retained Share | Mean Baseline Sources | Mean Variant Sources | Mean Added | Mean Removed |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Text | Top-3 chunks instead of top-5 | 18 | 0.600 | 0.600 | 0.600 | 5.000 | 3.000 | 0.000 | 2.000 |
| Text | Top-8 chunks instead of top-5 | 18 | 0.625 | 0.625 | 1.000 | 5.000 | 8.000 | 3.000 | 0.000 |
| XBRL | Facts only; relation paths removed | 18 | 0.594 | 0.545 | 0.594 | 20.778 | 11.889 | 0.000 | 8.889 |
| XBRL | Fact budget reduced to top-8; paths unchanged | 18 | 0.807 | 0.818 | 0.807 | 20.778 | 16.889 | 0.000 | 3.889 |
| XBRL | Fact budget expanded to top-16 and path budget to top-15 | 18 | 0.750 | 0.710 | 1.000 | 20.778 | 28.167 | 7.389 | 0.000 |

Appendix Table I2 reports a deterministic source-environment perturbation diagnostic over the same 18 filer-construct cells used to build the retrieval conditions. The diagnostic varies text source budget and XBRL fact/path inclusion without re-running the LLM. This diagnostic supports retrieval-stage source-composition transparency because it shows exactly how much the retrieved source set changes before model inference. It is not an output-level robustness test. The fact-only XBRL variant is especially important for this paper's contribution: removing relation paths lowers the mean source-set Jaccard to 0.594, showing that XBRL relational retrieval is not equivalent to retrieving reported facts alone.

### Appendix Table I3. Bounded Sensitivity Decision Matrix

| Variant | Cells | Mean Jaccard | Minimum Jaccard | Cells Below 0.60 | Decision Band |
|---|---:|---:|---:|---:|---|
| Text top-3 chunks instead of top-5 | 18 | 0.600 | 0.600 | 0 | Moderate source-environment change |
| Text top-8 chunks instead of top-5 | 18 | 0.625 | 0.625 | 0 | Moderate source-environment change |
| XBRL facts only; relation paths removed | 18 | 0.594 | 0.524 | 16 | Material source-environment change |
| XBRL fact budget reduced to top-8; paths unchanged | 18 | 0.807 | 0.667 | 0 | Bounded source-environment change |
| XBRL fact budget expanded to top-16 and path budget to top-15 | 18 | 0.750 | 0.710 | 0 | Moderate source-environment change |

The decision matrix translates perturbation outputs into reviewer-facing diagnostic bands. The fact-only XBRL variant is classified as a material source-environment change because removing relation paths pushes 16 of 18 filer-construct cells below a 0.60 source-set Jaccard threshold. This supports the methodological claim that XBRL relational retrieval is separable from fact-only XBRL retrieval. It does not show that relation paths improve LLM output quality.

At the cell level, 17 of 18 filer-construct cells receive a high separability-attention flag and one receives a moderate flag. These flags are not failure rates or performance outcomes. They identify where a future Tier 2 model-validation study should add matched-budget, evidence-order, prompt-sensitivity, and output-level rerun checks before making claims about retrieval superiority or model performance.

### Appendix Table I4. Sensitivity Checks Not Claimed As Completed

| Check | Why It Matters | Current Treatment |
|---|---|---|
| Chunk-size variation | Affects text selection and boundary omissions | Guidance only |
| Chunk-overlap variation | Affects continuity of narrative retrieval | Guidance only |
| Embedding model variation | Affects vector-retrieval stability | Not applicable to current keyword prototype |
| Top-k variation | Affects evidence volume and selection | Source-environment perturbation diagnostic completed for text top-k; no LLM rerun |
| XBRL traversal-depth variation | Affects relation coverage and noise | Fact/path perturbation diagnostic completed; no LLM rerun |
| Relation-type filters | Affects construct alignment of relation retrieval | Relation-path removal diagnostic completed; no relation-type-specific filter test |
| Token-budget equalization | Affects separability across retrieval conditions | Context-volume diagnostic completed; matched-budget sensitivity not run |
| Model variation | Affects model-specific output behavior | Not claimed |
| Prompt variation | Affects stability and output framing | Guidance only |
| Independent expert coding | Required for stronger audit-boundary conclusions | Not yet completed |

For the current paper, these items are reported as sensitivity guidance and boundary conditions. For a Tier 2 model-validation study, the researcher should pre-specify a bounded sensitivity matrix. A minimum version would vary text top-k, XBRL traversal depth or relation filters, hybrid context budget, and prompt wording while holding the model and task constant. The study should then report whether the main qualitative inference changes under those variants.

### Appendix Table I5. Reporting Items Mapped To Validity Dimensions

| Reporting Item | Selection | Representation | Stability | Traceability | Separability |
|---|---|---|---|---|---|
| Corpus and filer manifest | Yes | No | Yes | Yes | No |
| Chunk/fact/path schema | Yes | Yes | Yes | Yes | No |
| Retrieval parameters | Yes | Yes | Yes | Yes | Yes |
| Rendered prompt and context | Yes | Yes | Yes | Yes | Yes |
| Source IDs in outputs/coding | No | Yes | No | Yes | No |
| LLM configuration | No | No | Yes | No | Yes |
| Claim-level coding protocol | No | Yes | No | Yes | Yes |
| Sensitivity checks | Yes | Yes | Yes | No | Yes |

### Appendix Table I6. Text Retrieval Data Structure For Future Studies

| Field | Description |
|---|---|
| chunk_id | Stable chunk identifier |
| filer_id | Company or filing identifier |
| source_document | Filing, report, workpaper, or standard source |
| source_section | Section label where available |
| chunk_text | Retrieved text unit |
| chunking_rule | Rule used to create the unit |
| chunk_size | Token, word, or character size |
| overlap | Token, word, or character overlap |
| embedding_model | Required if vector retrieval is used |
| index_type | Vector database or search index type |
| similarity_metric | Similarity or ranking metric |
| retrieved_rank | Rank returned by retrieval |
| prompt_inclusion_flag | Whether the chunk was included in the final prompt |

### Appendix Table I7. XBRL Relational Retrieval Data Structure For Future Studies

| Field | Description |
|---|---|
| fact_id | Stable fact identifier |
| concept_qname | XBRL concept QName |
| concept_label | Human-readable label |
| value | Reported value |
| unit | Unit of measure |
| decimals | Decimal precision |
| period | Reporting period or instant |
| dimensions | Segment or dimensional context |
| path_id | Stable relation-path identifier |
| source_concept | Starting concept in relation path |
| target_concept | Ending concept in relation path |
| relation_type | Calculation, presentation, definition, or other relation type |
| arcrole | XBRL arcrole |
| role | Link role |
| depth | Traversal depth |
| taxonomy_version | Taxonomy or linkbase version |
| rdf_owl_mapping | Optional portability mapping, if implemented |

### Appendix Table I8. Reproducibility Package Checklist

| Component | Current Status | Final Packaging Action |
|---|---|---|
| Source filer manifest | Present | Verify filing metadata and URLs |
| Raw SEC source folders | Present | Add checksum manifest if releasing public package |
| Download and extraction scripts | Present | Add execution-order README |
| Text chunks | Present | Preserve chunk IDs and retrieval parameters |
| XBRL facts and paths | Present | Preserve fact/path IDs and taxonomy boundary |
| Retrieval logs | Present | Confirm final examples cite source IDs |
| Rendered prompts and contexts | Present | Include in supplement archive |
| Raw LLM outputs | Present | Preserve local model metadata; capture model digest if available |
| Claim-level coding | Present with boundary | Add expert review or retain preliminary limitation |
| Source spot checks | Present | Use only source-verified examples in main text |
| Sensitivity results | Context-volume and source-environment perturbation diagnostics present | Do not imply completed model-output benchmark |
| Vector/RDF artifacts | Not implemented | Present as guidance/specification only |

## Cross-Appendix Evidence Trail

| Step | Evidence Object | Appendix |
|---|---|---|
| 1 | SEC filing and Inline XBRL source | A |
| 2 | Extracted text chunk or XBRL fact/path | B or C |
| 3 | Retrieved evidence selected for a run | D |
| 4 | Final prompt shown to the LLM | D |
| 5 | Raw LLM output | E |
| 6 | Segmented claim | F |
| 7 | Claim-level evidence-use and correctness coding | F |
| 8 | Selected source spot check | G |
| 9 | Extension and boundary-condition evidence | H |
| 10 | Sensitivity limits and future reporting requirements | I |

## What The Supplement Supports

The supplement supports the manuscript's Tier 1 methodological demonstration by documenting a source-to-context-to-output-to-claim evidence trail across a nine-filer package with 72 retrieval-conditioned outputs and 281 preliminary coded claims. It supports the claim that hybrid condition labels do not guarantee integrated evidence use in this design: in hybrid conditions, 8 of 89 claims used both text and XBRL sources, 61 used text only, and 20 used XBRL only. These counts are design-specific diagnostics, not estimated population frequencies.

The supplement also specifies the additional Tier 2 design needed for model-validation claims. That design is guidance for future empirical LLM audit studies, not completed evidence in the current paper.

## What The Supplement Does Not Support

The supplement does not support claims that a hybrid condition is superior, XBRL retrieval improves audit reasoning, `gemma4:31b` has general audit expertise, failure-mode frequencies generalize to SEC filers, preliminary audit-boundary scores are final expert evidence, or the current prototype implements production vector RAG, RDF/OWL graph storage, or GraphRAG performance evaluation. It also does not support model-performance validation claims, which would require the Tier 2 design features summarized in Appendix Table I1A.

## Final Reviewer Assessment

This appendix is submission-ready for a bounded AJPT methodology paper if the main manuscript preserves the same claim boundaries. It gives reviewers a coherent route from source filings to retrieval contexts, LLM outputs, claim-level variables, selected examples, boundary-condition diagnostics, replication documentation, and checksum-based file-integrity checks. Remaining items are author-specific or optional repository decisions: finalize author/disclosure fields, decide whether to distribute raw SEC downloads separately, and capture a local model digest if the serving environment exposes one.
