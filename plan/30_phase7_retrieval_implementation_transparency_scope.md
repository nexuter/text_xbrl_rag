# Phase 7 Retrieval Implementation Transparency Scope

## Purpose

This memo verifies whether the project plan already covers the implementation details needed for text retrieval, XBRL relational retrieval, and the LLM demonstration. It then defines the additional Phase 7 scope needed to make the paper transparent and reproducible for AJPT reviewers and future audit researchers.

The objective is not to turn the paper into a systems paper or a retrieval-performance benchmark. The objective is to make the retrieval-created information environment sufficiently inspectable that readers can understand, reproduce, and critique the conditions under which LLM audit outputs were generated.

## Gap Assessment

| Area | Current Plan Coverage | Reviewer-Relevant Gap | Phase 7 Adjustment |
|---|---|---|---|
| Text retrieval concept | Phase 4 distinguishes text-based contextual retrieval from XBRL-based relational retrieval. Phase 6 builds a minimal text retrieval prototype. | The plan did not explicitly require disclosure of chunk schema, chunk size, overlap, embedding model, vector index, similarity metric, top-k, reranking, or metadata filters. | Add a text retrieval implementation specification and appendix reporting template. |
| XBRL relation retrieval concept | Phase 4 defines XBRL-based relational retrieval. Phase 6 extracts facts and relation paths. | The plan did not explicitly specify the relational data model, ontology mapping, RDF/OWL serialization, taxonomy versioning, extension-concept treatment, or graph traversal parameters. | Add an XBRL relation retrieval implementation specification and RDF/OWL mapping template. |
| Hybrid retrieval | Phase 4 and Phase 6 distinguish hybrid retrieval as a separate retrieval design. | The plan did not explicitly require disclosure of how text and XBRL context are assembled, budgeted, ordered, and source-traced in the final prompt. | Add a hybrid context assembly specification. |
| LLM demonstration pipeline | Phase 6 records downloads, extraction, context construction, prompts, LLM runs, coding, and spot-checks. | The plan did not yet consolidate these steps into a reproducible end-to-end workflow that readers could follow. | Add an implementation workflow for the demonstration. |
| Sensitivity checks | Phase 7 includes top-k, traversal depth, token budget, taxonomy version, and stability. | The list was too broad to show how retrieval performance and efficiency parameters differ between vector text retrieval and relation retrieval. | Expand sensitivity guidance to include chunk size, overlap, embedding model, similarity metric, reranking, relation filters, extension concepts, periods, and dimensions. |

## Scope Boundary

The manuscript should describe implementation choices enough for transparency, but it should not claim that a particular vector database, graph database, ontology tool, embedding model, or LLM is optimal.

The paper should make three bounded claims:

1. Retrieval implementation choices are research-design choices because they determine the information environment shown to the LLM.
2. Text retrieval and XBRL relation retrieval require different data structures, operators, and reporting standards.
3. Transparent reporting of retrieval stores, parameters, prompts, and logs helps researchers evaluate retrieval-environment validity.

The paper should not claim:

1. XBRL relation retrieval is generally more accurate than text retrieval.
2. RDF/OWL storage is required for every audit LLM study.
3. The demonstration prototype is a production-grade RAG or GraphRAG system.
4. Retrieval parameter sensitivity checks are equivalent to audit evidence validation.

## Text Retrieval Data Structure

A text retrieval implementation should disclose at least four layers: source documents, chunks, embeddings, and retrieval logs.

### Source Document Layer

Minimum fields:

| Field | Purpose |
|---|---|
| `document_id` | Stable source identifier. |
| `ticker` / `cik` / `accession` | SEC filing identity. |
| `filing_type` / `filing_date` / `period_end` | Filing context. |
| `source_file` | Raw or processed file path. |
| `source_hash` | Reproducibility check. |
| `section_label` | Filing section or disclosure source. |
| `extraction_method` | Parser or rule used to extract text. |

### Chunk Layer

Minimum fields:

| Field | Purpose |
|---|---|
| `chunk_id` | Stable retrieval unit. |
| `document_id` | Link to source document. |
| `section_label` | Disclosure location. |
| `construct_tag` | Revenue, inventory, going concern, etc. |
| `chunk_text` | Retrieved text unit. |
| `char_start` / `char_end` | Source traceability when available. |
| `token_count` / `word_count` | Context-budget accounting. |
| `chunk_size_rule` | Fixed tokens, paragraphs, disclosure blocks, or hybrid rule. |
| `overlap_rule` | Number or percentage of overlapping tokens. |
| `preceding_chunk_id` / `following_chunk_id` | Local context reconstruction. |

### Embedding / Vector Index Layer

Minimum fields:

| Field | Purpose |
|---|---|
| `embedding_model` | Model used to encode chunks and queries. |
| `embedding_model_version` | Version or release identifier. |
| `embedding_dimension` | Vector dimensionality. |
| `normalization_rule` | Lowercasing, stopword handling, or none. |
| `vector_db_or_index` | FAISS, Chroma, pgvector, Elasticsearch, or equivalent. |
| `distance_metric` | Cosine, dot product, Euclidean, or BM25/hybrid score. |
| `index_build_date` | Reproducibility and versioning. |
| `metadata_filters` | Filing, construct, period, section, or company filters. |

### Retrieval Log Layer

Minimum fields:

| Field | Purpose |
|---|---|
| `retrieval_id` | Stable retrieval event ID. |
| `query` | User query, prompt seed, or construct query. |
| `query_embedding_model` | If different from chunk embedding. |
| `top_k` | Number of candidates retrieved. |
| `reranking_policy` | None, cross-encoder, rule-based, or LLM rerank. |
| `retrieved_chunk_id` | Source chunk. |
| `rank` | Retrieval rank. |
| `score` | Similarity or ranking score. |
| `included_in_prompt` | Whether retrieved item entered final LLM context. |
| `prompt_context_position` | Ordering in final context. |
| `truncation_rule` | Whether chunk was shortened before prompt rendering. |

### Text Retrieval Parameters for Sensitivity Checks

Reviewers will expect the paper to identify parameters that can affect both performance and efficiency:

- chunk size
- chunk overlap
- chunking unit: sentence, paragraph, disclosure block, fixed token window
- embedding model
- vector index type
- similarity metric
- metadata filters
- top-k
- reranking policy
- maximum prompt tokens allocated to text context
- query formulation
- retrieval stability across equivalent runs

## XBRL Relation Retrieval Data Structure

XBRL relational retrieval should be represented as a graph-like store, even if the demonstration prototype uses tables. A reviewer should be able to reconstruct which facts and relations were available, how they were selected, and how they entered the prompt.

### Fact Node Schema

Minimum fields:

| Field | Purpose |
|---|---|
| `fact_id` | Stable fact identifier. |
| `ticker` / `cik` / `accession` | Filing identity. |
| `concept_qname` | XBRL concept with namespace. |
| `concept_label` | Human-readable label. |
| `namespace` | US GAAP, SEC, filer extension, etc. |
| `value` | Reported value. |
| `unit` | Unit reference. |
| `decimals` / `precision` | Measurement disclosure. |
| `period_start` / `period_end` / `instant` | Reporting period. |
| `dimensions` | Axis-member information. |
| `context_ref` | XBRL context identifier. |
| `source_file` | Inline XBRL or extracted XML file. |
| `source_line_or_xpath` | Traceability when available. |

### Concept Node Schema

Minimum fields:

| Field | Purpose |
|---|---|
| `concept_qname` | Stable concept identifier. |
| `namespace` | Standard or extension taxonomy. |
| `standard_or_extension` | Concept origin. |
| `label` | Preferred label. |
| `balance` | Debit, credit, or none if available. |
| `period_type` | Duration or instant. |
| `data_type` | Monetary, shares, string, etc. |
| `taxonomy_year` | Taxonomy version. |

### Relation Edge Schema

Minimum fields:

| Field | Purpose |
|---|---|
| `edge_id` | Stable relation identifier. |
| `source_concept` | Parent, summation, domain, or source concept. |
| `target_concept` | Child, item, member, or target concept. |
| `relation_type` | Presentation, calculation, definition, label, reference, or custom. |
| `arcrole` | XBRL arcrole. |
| `role` | Extended link role. |
| `order` | Presentation or definition order. |
| `weight` | Calculation weight, when applicable. |
| `preferred_label` | Label role when applicable. |
| `taxonomy_year` | Taxonomy version. |
| `source_linkbase` | Filing or taxonomy source. |
| `extension_flag` | Whether relation uses filer extension concepts. |

## RDF / OWL Mapping

The paper can present RDF/OWL as a portability and compatibility layer rather than as a required implementation. The mapping should show how a tabular XBRL extraction can be converted into an ontology-compatible graph.

### Core Classes

| Class | Meaning |
|---|---|
| `xbrl:Fact` | Reported XBRL fact instance. |
| `xbrl:Concept` | XBRL taxonomy concept. |
| `xbrl:Unit` | Measurement unit. |
| `xbrl:Period` | Reporting period. |
| `xbrl:Context` | XBRL context including period and dimensions. |
| `xbrl:DimensionMember` | Axis-member pair. |
| `xbrl:RelationEdge` | Typed taxonomy or filing relation. |
| `audit:AuditConstruct` | Research construct such as revenue risk or inventory valuation. |
| `audit:Assertion` | Audit assertion category such as valuation, completeness, occurrence, or cutoff. |

### Core Properties

| Property | Meaning |
|---|---|
| `xbrl:hasConcept` | Links a fact to a concept. |
| `xbrl:hasValue` | Links a fact to its reported value. |
| `xbrl:hasUnit` | Links a fact to a unit. |
| `xbrl:hasPeriod` | Links a fact or context to a reporting period. |
| `xbrl:hasDimensionMember` | Links a context to axis-member information. |
| `xbrl:presentationParentChild` | Presentation relation. |
| `xbrl:calculationSummationItem` | Calculation relation. |
| `xbrl:definitionDomainMember` | Definition relation. |
| `audit:mapsToConstruct` | Researcher-coded mapping from concept or relation to audit construct. |
| `audit:mayInformAssertion` | Researcher-coded, non-evidentiary link to an audit assertion. |

Important boundary: `audit:mayInformAssertion` should not be interpreted as audit evidence. It indicates that a reported accounting relationship may be relevant to an assertion-oriented analysis.

## XBRL Relation Retrieval Operators

An XBRL relation retriever should report:

- seed concepts or construct queries
- whether seeds are selected by concept name, label, taxonomy role, prior construct mapping, or manual coding
- relation types included
- traversal depth
- direction of traversal
- treatment of extension concepts
- period filters
- unit filters
- dimension handling
- whether calculation weights are used
- whether relation paths are deduplicated
- how relation paths are ranked or selected
- how facts and relation paths are rendered into prompt text

## Hybrid Context Assembly

Hybrid retrieval requires separate reporting because the same final prompt can obscure different information environments.

Minimum disclosures:

| Area | Required Disclosure |
|---|---|
| Context budget | Number of tokens or words allocated to text and XBRL components. |
| Ordering | Whether text or XBRL appears first. |
| Source IDs | Whether chunk IDs, fact IDs, and path IDs are preserved. |
| Truncation | Which components are shortened and by what rule. |
| Equalization | Whether hybrid receives more total context than single-source conditions. |
| Integration instruction | Whether the prompt asks the model to connect narrative and reported relation evidence. |

## Demonstration Implementation Workflow

The demonstration should be reported as an end-to-end pipeline:

1. Download SEC filings and Inline XBRL artifacts.
2. Extract filing text and create source document records.
3. Chunk text using a disclosed chunking rule.
4. Build a text retrieval store.
5. Extract XBRL facts, concepts, contexts, units, dimensions, and linkbase relations.
6. Build XBRL fact and relation tables.
7. Map fact and relation tables to an RDF/OWL-compatible schema.
8. Execute text retrieval for each filer-construct condition.
9. Execute XBRL relation retrieval for each filer-construct condition.
10. Assemble text, XBRL, hybrid, and LLM-only prompt contexts.
11. Run the disclosed LLM with fixed model configuration.
12. Parse LLM outputs into claim-level units.
13. Code text-supported, graph-valid, audit-valid, and integrated correctness.
14. Spot-check selected claims against source text and raw XBRL.
15. Report retrieval parameters, logs, prompts, outputs, coding, and limitations.

## Status of the Current Demonstration

The current Phase 6 demonstration already implements an inspectable prototype:

- text chunks are stored in `data/processed/text_chunks/text_chunks.csv`
- XBRL facts are stored in `data/processed/xbrl_facts/xbrl_facts.csv`
- XBRL relation paths are stored in `data/processed/xbrl_paths/xbrl_paths.csv`
- prompt-ready contexts are stored in `data/processed/retrieval_contexts/`
- retrieval logs are stored in `data/processed/retrieval_logs/retrieval_log.csv`
- prompts are stored in `data/processed/prompts/`
- LLM outputs and coding outputs are stored in `data/processed/llm_outputs/` and `data/processed/coding/`

However, the current prototype should be described precisely:

- Text retrieval is keyword-ranked contextual retrieval over extracted 10-K chunks, not yet embedding-based vector retrieval.
- XBRL retrieval uses extracted facts and direct relation paths, not yet a full RDF/OWL triple store or graph database.
- The prototype is sufficient for demonstrating retrieval-environment validity, but a replication-oriented appendix should disclose how it could be extended to vector DB and RDF/OWL storage.

If the manuscript claims embedding-based RAG or ontology database implementation, the project should add an implementation extension before submission. If the manuscript presents the current demonstration as a transparent methodological prototype, the appendix can report the vector DB and RDF/OWL structures as implementation guidance for future researchers.

## Reviewer-Facing Position

A reviewer-friendly framing would be:

> We do not argue that one retrieval technology is superior. Instead, we show that text and XBRL retrieval create different information environments and therefore require different reporting standards. To make the demonstration reproducible, we disclose the retrieval units, parameters, source IDs, prompt assembly rules, and coding outputs. We also provide a portable schema showing how text chunks can be managed in vector stores and how XBRL facts and relations can be represented in RDF/OWL-compatible form.

## Required Phase 7 Outputs

Phase 7 should now produce:

1. Text retrieval data structure specification.
2. XBRL relational retrieval data structure specification.
3. RDF/OWL mapping template for XBRL facts and relations.
4. Hybrid context assembly specification.
5. LLM demonstration implementation workflow.
6. Reproducibility package checklist.
7. Sensitivity check table separating text retrieval parameters from relation retrieval parameters.
8. Appendix reporting templates for retrieval stores, prompts, logs, and coded outputs.

