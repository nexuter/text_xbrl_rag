# V3 Appendix And Online Supplement

## Purpose

This appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration in:

**Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL-Augmented Retrieval**

The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-valid and integrated-correctness coding is preliminary unless independently reviewed by audit-domain experts.

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

| Ticker | Company | Role | Primary Construct Role | Methodological Purpose |
|---|---|---|---|---|
| NKE | Nike | Main deep case | Revenue and inventory | Familiar consumer-facing filer for source tracing and evidence-use illustration |
| SBUX | Starbucks | Main deep case | Revenue and inventory | Familiar consumer-facing filer with interpretable inventory and revenue disclosures |
| TGT | Target | Main deep case | Revenue and inventory | Familiar retail filer with inventory and revenue reporting relevance |
| WMT | Walmart | Bounded extension | Inventory | Mega-scale retail extension case |
| HD | Home Depot | Bounded extension | Inventory | Specialty-retail extension case |
| CAT | Caterpillar | Bounded extension | Inventory | High-complexity industrial stress case |
| PFE | Pfizer | Bounded extension | Inventory | Pharma/product-risk reporting extension case |
| MSFT | Microsoft | Bounded extension | Revenue | Revenue boundary case with relation-path scarcity |
| CROX | Crocs | Bounded extension | Inventory | Mid-size consumer-product extension case |

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
| Bounded-extension prompt/context conditions | 18 |
| Total prompt/context conditions | 42 |
| Retrieval log rows | 313 |

Each run is identified by filer, construct, retrieval condition, and run identifier. The archive preserves rendered prompts, text chunks, XBRL fact identifiers, XBRL path identifiers, source IDs, and context assembly rules. The LLM-only condition is retained as a diagnostic baseline for traceability and possible pretraining-contamination concerns.

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
| Extension outputs | 18 |
| Total outputs | 42 |
| Output errors | 0 |

Exact third-party output replication may depend on local model builds, hardware, and serving environment. The final replication package should capture local model metadata or digest where available.

What this validates: Outputs were generated under a consistent local model configuration.

What this does not validate: The appendix does not establish cross-model robustness or general audit expertise of the selected model.

## Appendix F. Claim-Level Coding Package

Appendix F shows how LLM outputs were converted into claim-level research variables. This is central to the paper's data and variable-construction contribution.

### Appendix Table F1. Claim-Level Coding Scope

| Item | Count |
|---|---:|
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total coded claims | 182 |
| Factual claims | 76 |
| Risk/assertion-mapping claims | 99 |
| Insufficient-context claims | 7 |
| Claims requiring manual or expert review for audit-valid use | 182 |

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

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 15 | 6 | 9 | 0 | 0.63 | 0.88 | 1.00 | 0.60 |
| hybrid | revenue | 15 | 6 | 9 | 0 | 0.47 | 0.88 | 1.00 | 0.50 |
| llm_only | inventory | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| llm_only | revenue | 3 | 0 | 0 | 3 | NA | NA | 1.00 | NA |
| text | inventory | 13 | 5 | 8 | 0 | 0.69 | NA | 1.00 | NA |
| text | revenue | 15 | 6 | 9 | 0 | 0.70 | NA | 1.00 | NA |
| xbrl | inventory | 15 | 7 | 7 | 1 | NA | 0.70 | 1.00 | NA |
| xbrl | revenue | 15 | 7 | 8 | 0 | NA | 0.73 | 1.00 | NA |

Note: These values are preliminary author-coded diagnostics. They are included to make the coding protocol inspectable. They should not be interpreted as model-performance measures or final audit-validity evidence.

What this validates: The demonstration is claim-level rather than anecdotal and operationalizes output-to-variable construction.

What this does not validate: Audit-valid and integrated scores require independent audit-domain expert review before supporting stronger audit-judgment claims.

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

The source spot-check archive identified no invalid source references in the current output set. This supports source traceability, but it does not independently validate all audit-valid inferences.

What this validates: Selected examples in the manuscript can be traced through source IDs and coding records.

What this does not validate: Selected examples do not provide independent expert validation of all 182 coded claims.

## Appendix H. Bounded Extension Evidence

Appendix H addresses the concern that the framework might depend on three familiar deep-case filers. The extension is a maximum-variation methodological check, not a representative empirical sample.

### Appendix Table H1. Bounded-Extension Filer Selection

| Ticker | Company | Industry / Setting | Primary Construct | Methodological Purpose |
|---|---|---|---|---|
| WMT | Walmart | Mega-scale retail | Inventory | High-volume retail inventory setting |
| HD | Home Depot | Specialty retail / home improvement | Inventory | Specialty retail inventory setting |
| CAT | Caterpillar | Industrial manufacturing | Inventory | High-complexity inventory and LIFO reporting stress case |
| PFE | Pfizer | Pharma / healthcare products | Inventory | Product, reserve, and regulatory reporting setting |
| MSFT | Microsoft | Software/cloud | Revenue | Revenue-recognition and contract-liability boundary case |
| CROX | Crocs | Mid-size consumer products / footwear | Inventory | Size variation and consumer-product inventory setting |

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

| Ticker | Primary Construct | Conditions | Output Count | Coded Claims |
|---|---|---|---:|---:|
| WMT | Inventory | Text, XBRL, hybrid | 3 | 15 |
| HD | Inventory | Text, XBRL, hybrid | 3 | 15 |
| CAT | Inventory | Text, XBRL, hybrid | 3 | 14 |
| PFE | Inventory | Text, XBRL, hybrid | 3 | 15 |
| MSFT | Revenue | Text, XBRL, hybrid | 3 | 14 |
| CROX | Inventory | Text, XBRL, hybrid | 3 | 15 |
| Total | Mixed | Text, XBRL, hybrid | 18 | 88 |

### Appendix Table H4. Selected Bounded-Extension Examples

| Example | Filer | Construct | Condition | Claim ID | Claim Role | Claim Summary | Sources | Preliminary Interpretation |
|---|---|---|---|---|---|---|---|---|
| EXT-01 | HD | Inventory | Hybrid | C026 | Integrated factual claim | Merchandise inventories were $25.8 billion as of February 1, 2026. | T-HD-INVENTORY-020; F-HD-0004 | Demonstrates clean text-XBRL corroboration in a specialty retail setting. |
| EXT-02 | CAT | Inventory | Hybrid | C042 | Integrated risk/assertion claim | LIFO use and the LIFO reserve create an inventory valuation consideration. | T-CAT-INVENTORY-016; F-CAT-0048 | Shows possible integration in a high-complexity manufacturing setting; audit-validity remains preliminary. |
| EXT-03 | PFE | Inventory | Hybrid | C057 | Integrated risk/assertion claim | Historical inventory write-offs and product return adjustments indicate inventory valuation considerations. | T-PFE-REVENUE_INVENTORY-035; F-PFE-0134 | Extends the protocol to pharma/product-risk reporting. |
| EXT-04 | MSFT | Revenue | Hybrid | C069 | XBRL-only claim within hybrid condition | Current contract liability was $64.555 billion as of June 30, 2025. | F-MSFT-0028 | Demonstrates that a hybrid condition can produce XBRL-only claims. |
| EXT-05 | MSFT | Revenue | Hybrid | C071 | Text-only risk/assertion claim within hybrid condition | SSP estimates and performance-obligation timing create revenue accuracy and cut-off considerations. | T-MSFT-REVENUE-089 | Demonstrates that a hybrid condition can produce text-only audit reasoning. |

### Appendix Table H5. Bounded-Extension Preliminary Coding Summary

| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hybrid | inventory | 25 | 12 | 13 | 0 | 0.50 | 0.85 | 1.00 | 0.58 |
| hybrid | revenue | 5 | 2 | 3 | 0 | 0.50 | 1.00 | 1.00 | 0.50 |
| text | inventory | 24 | 10 | 14 | 0 | 0.71 | NA | 1.00 | NA |
| text | revenue | 5 | 2 | 3 | 0 | 0.70 | NA | 1.00 | NA |
| xbrl | inventory | 25 | 11 | 14 | 0 | NA | 0.72 | 1.00 | NA |
| xbrl | revenue | 4 | 2 | 2 | 0 | NA | 0.75 | 1.00 | NA |

Note: These values are preliminary author-coded diagnostics. They should not be interpreted as model-performance measures, prevalence estimates, or final audit-validity evidence.

What this validates: The protocol can be applied across varied reporting environments, and boundary cases are visible through retrieval diagnostics.

What this does not validate: The extension does not estimate population-level performance, failure-mode prevalence, or retrieval-method superiority.

## Appendix I. Sensitivity Guidance And Boundary Conditions

Appendix I separates the current Tier 1 methodological demonstration from the additional evidence required for stronger empirical or system-performance claims.

### Appendix Table I1. Sensitivity Checks Not Claimed As Completed

| Check | Why It Matters | Current Treatment |
|---|---|---|
| Chunk-size variation | Affects text selection and boundary omissions | Guidance only |
| Chunk-overlap variation | Affects continuity of narrative retrieval | Guidance only |
| Embedding model variation | Affects vector-retrieval stability | Not applicable to current keyword prototype |
| Top-k variation | Affects evidence volume and selection | Guidance only |
| XBRL traversal-depth variation | Affects relation coverage and noise | Guidance only |
| Relation-type filters | Affects construct alignment of relation retrieval | Guidance only |
| Token-budget equalization | Affects separability across retrieval conditions | Conceptual control, not full sensitivity run |
| Model variation | Affects model-specific output behavior | Not claimed |
| Prompt variation | Affects stability and output framing | Guidance only |
| Independent expert coding | Required for stronger audit-valid conclusions | Not yet completed |

### Appendix Table I2. Reporting Items Mapped To Validity Dimensions

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

### Appendix Table I3. Text Retrieval Data Structure For Future Studies

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

### Appendix Table I4. XBRL Relational Retrieval Data Structure For Future Studies

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

### Appendix Table I5. Reproducibility Package Checklist

| Component | Current Status | Final Packaging Action |
|---|---|---|
| Source filer manifest | Present | Verify filing metadata and URLs |
| Raw SEC source folders | Present | Add checksum manifest if releasing public package |
| Download and extraction scripts | Present | Add execution-order README |
| Text chunks | Present | Preserve chunk IDs and retrieval parameters |
| XBRL facts and paths | Present | Preserve fact/path IDs and taxonomy boundary |
| Retrieval logs | Present | Confirm final examples cite source IDs |
| Rendered prompts and contexts | Present | Include in supplement archive |
| Raw LLM outputs | Present | Capture model digest or local metadata if available |
| Claim-level coding | Present with boundary | Add expert review or retain preliminary limitation |
| Source spot checks | Present | Use only source-verified examples in main text |
| Sensitivity results | Not claimed | Do not imply completed benchmark |
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

The supplement supports the manuscript's Tier 1 methodological demonstration by documenting a source-to-context-to-output-to-claim evidence trail across 42 retrieval-conditioned outputs and 182 preliminary coded claims. It supports the claim that hybrid condition labels do not guarantee integrated evidence use: in hybrid conditions, 7 of 60 claims used both text and XBRL sources, 41 used text only, and 12 used XBRL only.

## What The Supplement Does Not Support

The supplement does not support claims that hybrid retrieval is superior, XBRL retrieval improves audit reasoning, `gemma4:31b` has general audit expertise, failure-mode frequencies generalize to SEC filers, preliminary audit-valid scores are final expert evidence, or the current prototype implements production vector RAG, RDF/OWL graph storage, or GraphRAG performance evaluation.

## Final Reviewer Assessment

This appendix is submission-ready for a bounded AJPT methodology paper if the main manuscript preserves the same claim boundaries. It gives reviewers a coherent route from source filings to retrieval contexts, LLM outputs, claim-level variables, selected examples, and boundary-condition diagnostics. The remaining packaging improvements are archival rather than conceptual: add a concise replication README, capture local Ollama model metadata where available, and decide whether to add file checksums before public release.
