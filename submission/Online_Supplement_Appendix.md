# V3 Appendix And Online Supplement

## Purpose

This appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration in:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-valid coding remains preliminary unless independently reviewed by audit-domain experts; evidence-use type and integrated correctness are independently coded in the 120-claim validation sample to evaluate protocol reliability.

## Reviewer-Facing Boundary Statement

The appendix supports three bounded manuscript claims:

1. Retrieval creates the information environment from which LLM audit-research inferences are drawn.
2. Text retrieval, XBRL relational retrieval, and hybrid retrieval create distinguishable evidence environments.
3. Retrieval-condition labels do not determine claim-level evidence use; claim-level coding is required.

The appendix does not support claims that hybrid retrieval is superior, that XBRL improves audit reasoning, that the selected LLM has general audit expertise, or that preliminary author-coded audit-valid scores are final audit-judgment evidence.

## Appendix Map

| Appendix | Title | Reviewer Question | Validity Function |
|---|---|---|---|
| A | Source Corpus and Filer Manifest | What filed documents created the source universe? | Selection and traceability |
| B | Text Retrieval Store and Chunking | How was narrative filing evidence represented and retrieved? | Selection, representation, and stability |
| C | XBRL Fact and Relation Store | How were reported accounting facts and relations represented? | Representation and traceability |
| D | Prompt and Retrieval Context Archive | What exactly did the LLM see? | Traceability and separability |
| E | LLM Run Configuration and Output Archive | Were outputs generated under controlled model settings? | Stability and separability |
| F | Claim-Level Coding Package | How were outputs converted into research variables? | Traceability and representation |
| G | Source Spot Checks and Selected Examples | Can selected claims be traced back to filed evidence? | Traceability |
| H | Bounded Extension Evidence | Does the protocol remain applicable beyond the deep cases? | Selection and boundary-condition assessment |
| I | Sensitivity Guidance and Boundary Conditions | What would stronger empirical claims require? | Stability and separability |

## Appendix A. Source Corpus And Filer Manifest

Appendix A documents the public SEC 10-K and Inline XBRL source universe used to construct the retrieval environments. The filer manifest records company identity, ticker, CIK, filing year, accession metadata where available, sample role, and construct role. Raw SEC files, download records, and extraction summaries are retained in the replication package.

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

What this validates: The demonstration uses actual public filing and Inline XBRL sources across nine active filers.

What this does not validate: The sample is not representative of all SEC filers and does not establish audit evidence quality or population-level generalizability.

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

What this validates: Narrative retrieval units were constructed and logged consistently enough for source traceability and claim-level coding.

What this does not validate: The current prototype does not claim production vector RAG performance or optimal text-retrieval settings.

## Appendix C. XBRL Fact And Relation Store

Appendix C documents XBRL facts and relation paths used as relational retrieval inputs. The current demonstration uses table-based fact and path retrieval. RDF/OWL and graph database formats are treated as portability and reporting extensions unless separately implemented.

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

Minimum disclosure items for future XBRL relational retrieval studies include fact identifier, concept QName, concept label, value, unit, decimals, period, dimensions, source context, relation path identifier, source concept, target concept, relation type, arcrole, role, traversal depth, taxonomy/linkbase source, taxonomy year or version, and extension-concept policy.

What this validates: XBRL relational retrieval creates a distinct reported-structure information environment from narrative text retrieval.

What this does not validate: XBRL facts and relation paths are management-reported structured data. They do not establish audit evidence sufficiency, misstatement, fraud, or audit truth.

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

What this validates: Reviewers can inspect the information environment actually supplied to the LLM for each retrieval condition.

What this does not validate: The archive does not establish that the supplied information was sufficient for an audit conclusion.

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

What this validates: Outputs were generated under a consistent local model configuration.

What this does not validate: The appendix does not establish cross-model robustness or general audit expertise of the selected model.

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
| Claims requiring manual or expert review for audit-valid use | 281 |

### Appendix Table F2. Retrieval Failure Mode Taxonomy

| Failure Mode | Definition | Validity Dimension Most Directly Implicated |
|---|---|---|
| Omission | Relevant source evidence exists but is not retrieved or not used | Selection |
| Distortion | Retrieved evidence loses source meaning through extraction, chunking, formatting, or summarization | Representation |
| Retrieval instability | Similar retrieval requests produce materially different evidence environments | Stability |
| Attribution failure | An output claim cannot be traced to retrieved evidence | Traceability |
| Model-retrieval confounding | Output differences cannot be separated from retrieval differences, model behavior, or prompt effects | Separability |
| Relation hallucination | The model invents or misstates an XBRL fact, concept, or relation path | Representation and traceability |
| Source overreach | The model treats management-reported filing data as audit evidence or ground truth | Representation and audit-validity boundary |
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

Note: These values are preliminary author-coded diagnostics. The aggregate table reports source-support means and integrated-bridge counts only. One-source hybrid claims are coded as non-integrated under the revised integrated-correctness rule. Audit-valid coding remains claim-level and requires independent audit-domain review before being treated as audit-judgment evidence.

What this validates: The demonstration is claim-level rather than anecdotal and operationalizes output-to-variable construction.

What this does not validate: Audit-valid scores require independent audit-domain expert review before supporting stronger audit-judgment claims. Integrated correctness is validated as a protocol variable in the independent coding sample, not as evidence of final audit-judgment correctness.

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
| Variables to code | Claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, integrated correctness, and qualitative audit-boundary notes |

The independent coding exercise makes the measurement protocol reviewer-evaluable. The protocol defines a claim as an independently assessable assertion in an LLM output and gives segmentation rules for factual statements, risk/assertion inferences, causal explanations, multi-account claims, caveats, and insufficient-context statements. The sample intentionally includes all hybrid-condition claims because the paper's most important measurement question is whether hybrid-condition outputs actually integrate text and XBRL evidence.

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

What this validates: The independent coding results support the reliability of the claim-level measurement protocol for segmentation, claim-kind classification, evidence-use type, text-supported correctness, graph-valid correctness, and integrated correctness.

Reconciliation note: Three focal disagreements remain after recoding, all involving whether accounting-policy statements should be classified as factual claims or risk/assertion inferences. Evidence-use type and integrated correctness have 100.0 percent agreement. The revised `integrated_code` instruction resolves the prior ambiguity by treating ordinary non-integration as `0`, not `NA`.

What this does not validate: The coding results do not establish model performance, retrieval-method superiority, or final audit-valid conclusions. Audit-boundary notes remain qualitative diagnostics, and stronger audit-judgment claims would require additional expert review and reconciliation procedures.

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

Automated validation checks source-ID resolvability across the output set, while the selected source spot-check archive illustrates substantive source-to-claim traceability for reviewer inspection. The source spot-check archive identified no unresolved source identifiers in the current output set. This supports source traceability by confirming that cited identifiers resolve to preserved retrieved materials, but it does not independently validate all audit-valid inferences.

What this validates: Selected examples in the manuscript can be traced through source IDs and coding records.

What this does not validate: Selected examples do not provide independent expert validation of all 281 coded claims.

## Appendix H. Bounded Extension Evidence

Appendix H addresses the concern that the framework might depend on three familiar deep-case filers. The extension is a maximum-variation methodological check, not a representative empirical sample.

The extension now uses the full two-construct, four-condition design for all six additional filers. Each extension filer contributes revenue and inventory tasks under LLM-only, text, XBRL, and hybrid retrieval conditions, producing 48 extension outputs. The expanded design removes ambiguity about whether the extension is a reduced demonstration while retaining the paper's methodological boundary: the added outputs are used to test protocol applicability and boundary conditions, not to estimate model performance or failure prevalence.

### Appendix Table H1. Bounded-Extension Filer Selection

| Ticker | Company | Industry / Setting | Constructs | Methodological Purpose |
|---|---|---|---|---|
| WMT | Walmart | Mega-scale retail | Revenue and inventory | High-volume retail reporting setting |
| HD | Home Depot | Specialty retail / home improvement | Revenue and inventory | Specialty-retail reporting setting |
| CAT | Caterpillar | Industrial manufacturing | Revenue and inventory | High-complexity industrial and LIFO reporting stress case |
| PFE | Pfizer | Pharma / healthcare products | Revenue and inventory | Product, reserve, and regulatory reporting setting |
| MSFT | Microsoft | Software/cloud | Revenue and inventory | Revenue-recognition setting and inventory boundary case |
| CROX | Crocs | Mid-size consumer products / footwear | Revenue and inventory | Size variation and consumer-product reporting setting |

### Appendix Table H2. Bounded-Extension Retrieval Diagnostics

| Ticker | Text Chunks | XBRL Facts | XBRL Relation Paths | Retrieval Diagnostic |
|---|---:|---:|---:|---|
| WMT | 120 | 141 | 109 | Strong retail extension case |
| HD | 125 | 173 | 174 | Strong specialty-retail extension case |
| CAT | 213 | 1,047 | 574 | High-complexity industrial/manufacturing case |
| PFE | 196 | 336 | 272 | Pharma/product-risk extension case |
| MSFT | 150 | 144 | 0 | Revenue-focused boundary case; relation-path scarcity is informative |
| CROX | 164 | 123 | 102 | Mid-size consumer-product extension case |

### Appendix Table H3. Bounded-Extension LLM And Coding Scope

| Ticker | Constructs | Conditions | Output Count | Coded Claims |
|---|---|---|---:|---:|
| WMT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 31 |
| HD | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| CAT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 31 |
| PFE | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| MSFT | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 29 |
| CROX | Revenue and inventory | LLM-only, text, XBRL, hybrid | 8 | 32 |
| Total | Revenue and inventory | LLM-only, text, XBRL, hybrid | 48 | 187 |

### Appendix Table H4. Selected Bounded-Extension Examples

| Example | Filer | Construct | Condition | Claim ID | Claim Role | Claim Summary | Sources | Preliminary Interpretation |
|---|---|---|---|---|---|---|---|---|
| EXT-01 | HD | Inventory | Hybrid | C058 | Integrated factual claim | Merchandise inventories were $25.8 billion as of February 1, 2026. | T-HD-INVENTORY-020; F-HD-0004 | Demonstrates clean text-XBRL corroboration in a specialty retail setting. |
| EXT-02 | CAT | Inventory | Hybrid | C091 | Integrated risk/assertion claim | LIFO use and the LIFO reserve create an inventory valuation consideration. | T-CAT-INVENTORY-016; F-CAT-0048 | Shows possible integration in a high-complexity manufacturing setting; audit-validity remains preliminary. |
| EXT-03 | PFE | Inventory | Hybrid | C123 | Integrated risk/assertion claim | Historical inventory write-offs and product return adjustments indicate inventory valuation considerations. | T-PFE-REVENUE_INVENTORY-035; F-PFE-0134 | Extends the protocol to pharma/product-risk reporting. |
| EXT-04 | MSFT | Revenue | Hybrid | C136 | XBRL-only claim within hybrid condition | Current contract liability was $64.555 billion as of June 30, 2025. | F-MSFT-0028 | Demonstrates that a hybrid condition can produce XBRL-only claims. |
| EXT-05 | MSFT | Revenue | Hybrid | C138 | Text-only risk/assertion claim within hybrid condition | SSP estimates and performance-obligation timing create revenue accuracy and cut-off considerations. | T-MSFT-REVENUE-089 | Demonstrates that a hybrid condition can produce text-only audit reasoning. |

### Appendix Table H5. Bounded-Extension Preliminary Coding Summary

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

Note: These values are preliminary author-coded diagnostics. The table does not aggregate audit-valid scores because those judgments require independent audit-domain review before supporting audit-judgment claims.

What this validates: The protocol can be applied across varied reporting environments, and boundary cases are visible through retrieval diagnostics.

What this does not validate: The extension does not estimate population-level performance, failure-mode prevalence, or retrieval-method superiority.

## Appendix I. Sensitivity Guidance And Boundary Conditions

Appendix I separates the current Tier 1 methodological protocol-validation demonstration from the additional evidence required for stronger empirical, model-performance, or system-performance claims. The current paper validates the inspectability of the retrieval protocol; it does not estimate model-performance effects. Appendix Table I1A specifies the additional design features that would be required if future studies use this framework to test whether retrieval design improves LLM audit outputs.

### Appendix Table I1A. Tier 2 Model-Validation Extension Design

| Design Component | Minimum Model-Validation Design | Stronger Design | Why It Matters |
|---|---:|---:|---|
| Filers | 12 | 20-24 | Creates cross-filer variation without claiming full SEC representativeness |
| Constructs | 2: revenue and inventory | 2 or more, pre-specified | Separates construct-specific retrieval fit from general model behavior |
| Retrieval conditions | 4: LLM-only, text, XBRL, hybrid | Same across all sampled filers | Treats retrieval as an experimental research-design factor |
| Base outputs | 96 | 160-192 | Provides enough task-output observations across filer, construct, and condition cells |
| Prompt/retrieval sensitivity outputs | 48-96 | 88-160 or targeted subset | Tests stability without turning the study into an unrestricted benchmark |
| Expected coded claims | 384-576 | 700-1,200 | Provides claim-level variation while preserving nesting within outputs |
| Independent expert-coded claims | At least 120 | 200-300 or all risk/assertion claims | Supports audit-valid and integrated correctness claims |
| Expert coders | Two audit-domain coders | Two or more, with adjudication | Provides reliability evidence and reduces author-coding concern |
| Reliability evidence | Percent agreement and kappa or alpha where appropriate | Same plus disagreement taxonomy | Makes audit-valid coding reviewer-evaluable |
| Statistical structure | Claims nested within task outputs and filers | Mixed or clustered models plus sensitivity tables | Avoids treating multiple claims from one output as independent |
| Primary outcomes | Source-reference validity, unsupported/overreaching claims, evidence-use type, construct-relevant retrieval coverage | Same plus pre-registered secondary outcomes | Aligns evidence with retrieval-environment validity rather than broad model quality |

The minimum design is not a universal sample-size rule. It is a design threshold based on the number of factors a model-validation claim would need to cover: retrieval condition, audit construct, filer, industry or reporting environment, prompt variation, retrieval variation, and expert-coded audit-validity judgments. Smaller samples may be appropriate for qualitative or protocol-validation claims; broader samples are necessary when researchers claim model-performance effects or failure-mode prevalence.

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

Appendix Table I2 reports a deterministic source-environment perturbation diagnostic over the same 18 filer-construct cells used to build the retrieval conditions. The diagnostic varies text source budget and XBRL fact/path inclusion without re-running the LLM. This evidence strengthens retrieval-stage source-composition transparency because it shows exactly how much the retrieved source set changes before model inference. It is not an output-level robustness test. The fact-only XBRL variant is especially important for this paper's contribution: removing relation paths lowers the mean source-set Jaccard to 0.594, showing that XBRL relational retrieval is not equivalent to retrieving reported facts alone.

### Appendix Table I3. Sensitivity Checks Not Claimed As Completed

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
| Independent expert coding | Required for stronger audit-valid conclusions | Not yet completed |

For the current paper, these items are reported as sensitivity guidance and boundary conditions. For a Tier 2 model-validation study, the researcher should pre-specify a bounded sensitivity matrix. A minimum version would vary text top-k, XBRL traversal depth or relation filters, hybrid context budget, and prompt wording while holding the model and task constant. The study should then report whether the main qualitative inference changes under those variants.

### Appendix Table I4. Reporting Items Mapped To Validity Dimensions

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

### Appendix Table I5. Text Retrieval Data Structure For Future Studies

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

### Appendix Table I6. XBRL Relational Retrieval Data Structure For Future Studies

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

### Appendix Table I7. Reproducibility Package Checklist

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

The supplement supports the manuscript's Tier 1 methodological demonstration by documenting a source-to-context-to-output-to-claim evidence trail across a nine-filer package with 72 retrieval-conditioned outputs and 281 preliminary coded claims. It supports the claim that hybrid condition labels do not guarantee integrated evidence use: in hybrid conditions, 8 of 89 claims used both text and XBRL sources, 61 used text only, and 20 used XBRL only.

The supplement also specifies the additional Tier 2 design needed for model-validation claims. That design is guidance for future empirical LLM audit studies, not completed evidence in the current paper.

## What The Supplement Does Not Support

The supplement does not support claims that hybrid retrieval is superior, XBRL retrieval improves audit reasoning, `gemma4:31b` has general audit expertise, failure-mode frequencies generalize to SEC filers, preliminary audit-valid scores are final expert evidence, or the current prototype implements production vector RAG, RDF/OWL graph storage, or GraphRAG performance evaluation. It also does not support model-performance validation claims, which would require the Tier 2 design features summarized in Appendix Table I1A.

## Final Reviewer Assessment

This appendix is submission-ready for a bounded AJPT methodology paper if the main manuscript preserves the same claim boundaries. It gives reviewers a coherent route from source filings to retrieval contexts, LLM outputs, claim-level variables, selected examples, boundary-condition diagnostics, replication documentation, and checksum-based file-integrity checks. Remaining items are author-specific or optional repository decisions: finalize author/disclosure fields, decide whether to distribute raw SEC downloads separately, and capture a local model digest if the serving environment exposes one.
