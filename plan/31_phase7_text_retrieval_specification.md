# Phase 7 Text Retrieval Implementation Specification

## Purpose

This specification defines the minimum information needed to report and reproduce text-based contextual retrieval in an LLM audit research study.

The purpose is methodological transparency, not retrieval optimization. Text retrieval choices determine which narrative disclosure environment the LLM observes. Therefore, chunking, embedding, indexing, ranking, truncation, and prompt assembly should be treated as research-design choices.

## Reviewer-Facing Claim

Text retrieval should not be described merely as "we used RAG." The paper should disclose the retrieval unit, retrieval operator, ranking rule, context budget, and source traceability so that reviewers can assess whether the retrieved text environment aligns with the audit construct being studied.

## Current Demonstration Status

The current Phase 6 demonstration uses:

| Component | Current Implementation |
|---|---|
| Source | SEC 10-K filing text extracted from actual filings |
| Retrieval unit | Construct-tagged text chunks |
| Ranking | Keyword-ranked contextual retrieval |
| Retrieved items | Five chunks per filer-construct pair |
| Prompt rendering | Top chunks rendered with chunk IDs and source files |
| Vector DB | Not implemented in the current prototype |
| Embeddings | Not implemented in the current prototype |

Reviewer-safe wording:

> The demonstration uses keyword-ranked contextual retrieval over extracted filing chunks to keep the retrieval-created information environment inspectable. The appendix reports how the same retrieval design can be implemented in an embedding-based vector store and which parameters future studies should disclose.

If the manuscript later claims embedding-based RAG performance, the project should add an actual vector-store implementation before submission.

## Text Retrieval Data Model

## Minimum Versus Extended Implementation

To avoid overstating the current demonstration, the paper should distinguish minimum implementation from extended implementation.

| Level | Appropriate Use | Required Components | Manuscript Language |
|---|---|---|---|
| Minimum inspectable prototype | Methodological demonstration focused on retrieval-environment validity | Source documents, text chunks, ranking rule, context files, retrieval logs, prompt files | "Keyword-ranked contextual retrieval over disclosed filing chunks." |
| Embedding-based RAG implementation | Study claiming semantic retrieval behavior or comparing RAG systems | Minimum prototype components plus embedding model, vector index, similarity metric, top-k, reranking, and index metadata | "Embedding-based vector retrieval using disclosed model and index parameters." |
| Production retrieval system | Deployment or system-performance study | Embedding/vector components plus monitoring, latency, drift, access control, and operational evaluation | Not the target of this methodology paper. |

The current demonstration belongs to the minimum inspectable prototype level. This is appropriate because the paper's claim is not that vector retrieval improves audit performance, but that retrieval-created information environments must be specified and evaluated.

### 1. Source Document Table

Each filing or document source should have one record.

| Field | Required | Description |
|---|---:|---|
| `document_id` | Yes | Stable source document ID. |
| `ticker` | Yes | Company ticker when applicable. |
| `cik` | Yes | SEC CIK. |
| `company_name` | Yes | Registrant name. |
| `accession` | Yes | SEC accession number. |
| `filing_type` | Yes | 10-K, 10-Q, 8-K, etc. |
| `filing_date` | Yes | Filing date. |
| `period_end` | Yes | Fiscal period end. |
| `source_file` | Yes | Raw or processed file path. |
| `source_url` | Recommended | SEC source URL. |
| `source_hash` | Recommended | File hash for reproducibility. |
| `extraction_method` | Yes | Parser, script, or extraction rule. |
| `extraction_timestamp` | Recommended | When the source was extracted. |

### 2. Text Chunk Table

Each row is one candidate retrieval unit.

| Field | Required | Description |
|---|---:|---|
| `chunk_id` | Yes | Stable chunk ID used in prompts and logs. |
| `document_id` | Yes | Foreign key to source document. |
| `ticker` | Yes | Company ticker. |
| `accession` | Yes | SEC accession number. |
| `section_label` | Recommended | MD&A, footnote, risk factor, policy, etc. |
| `construct_tag` | Yes | Audit construct tag, e.g., revenue or inventory. |
| `chunk_text` | Yes | Text available for retrieval. |
| `preceding_context` | Recommended | Local context before chunk. |
| `following_context` | Optional | Local context after chunk. |
| `char_start` | Recommended | Source character offset when available. |
| `char_end` | Recommended | Source character offset when available. |
| `word_count` | Yes | Word count by disclosed rule. |
| `token_count` | Recommended | Token count by disclosed tokenizer. |
| `chunking_rule` | Yes | Paragraph, disclosure block, fixed window, or hybrid. |
| `chunk_size_target` | Yes | Target size in tokens or words. |
| `overlap_size` | Yes | Overlap in tokens, words, or percentage. |
| `previous_chunk_id` | Recommended | Prior chunk in source order. |
| `next_chunk_id` | Recommended | Next chunk in source order. |

## Embedding and Vector Store Specification

If the text retrieval condition uses embedding-based retrieval, the study should disclose the following.

| Field | Required | Description |
|---|---:|---|
| `embedding_model` | Yes | Embedding model name. |
| `embedding_model_version` | Yes | Release, checkpoint, or API version. |
| `embedding_dimension` | Yes | Vector dimensionality. |
| `embedding_date` | Recommended | When embeddings were generated. |
| `normalization_rule` | Yes | Text preprocessing rule. |
| `vector_store` | Yes | FAISS, Chroma, pgvector, Elasticsearch, etc. |
| `index_type` | Yes | Flat, HNSW, IVF, BM25, hybrid, etc. |
| `distance_metric` | Yes | Cosine, dot product, Euclidean, BM25, hybrid score. |
| `metadata_filters` | Yes | Filing, period, section, construct, or company filters. |
| `query_template` | Yes | Query used to retrieve chunks. |
| `top_k` | Yes | Number of candidates retrieved. |
| `reranking_policy` | Yes | None, cross-encoder, LLM rerank, or rule-based. |
| `prompt_inclusion_rule` | Yes | How retrieved candidates enter the prompt. |

## Retrieval Log Template

Each retrieval event should be logged at the retrieved-item level.

| Field | Description |
|---|---|
| `retrieval_id` | Stable retrieval event ID. |
| `condition` | Text, XBRL, hybrid, or baseline. |
| `query_id` | Query or construct seed ID. |
| `query_text` | Query used for retrieval. |
| `retrieval_operator` | Keyword, embedding similarity, hybrid BM25/vector, etc. |
| `chunk_id` | Retrieved chunk ID. |
| `rank` | Rank before prompt rendering. |
| `score` | Similarity or ranking score. |
| `rerank_score` | Optional reranking score. |
| `included_in_prompt` | Yes/no. |
| `prompt_position` | Order in final prompt. |
| `truncation_applied` | Yes/no. |
| `rendered_word_count` | Words after prompt rendering. |
| `notes` | Any exception or manual handling. |

## Parameters That Affect Performance and Efficiency

Text retrieval performance and efficiency should not be treated as fixed properties of "RAG." They depend on disclosed design choices.

| Parameter | Why It Matters for Audit Research |
|---|---|
| Chunk size | Affects whether accounting policies, risk factors, and footnotes remain interpretable. |
| Chunk overlap | Affects whether relevant context is split across chunk boundaries. |
| Chunking unit | Disclosure blocks may preserve meaning better than arbitrary token windows. |
| Embedding model | Affects semantic matching for accounting terminology. |
| Similarity metric | Affects ranking of retrieved narrative evidence. |
| Metadata filters | Can prevent irrelevant sections but may introduce researcher selection effects. |
| Top-k | Affects recall, prompt length, and noise. |
| Reranking | Can improve relevance but adds another opaque selection layer. |
| Prompt budget | Determines how much retrieved evidence the LLM can observe. |
| Query formulation | Determines whether retrieval captures the intended audit construct. |

## Recommended Sensitivity Checks

Minimum sensitivity checks for a text retrieval study:

1. Chunk size variation.
2. Chunk overlap variation.
3. Top-k variation.
4. Query formulation variation.
5. Metadata filter variation.
6. Token budget equalization across retrieval conditions.
7. Repeated retrieval stability when approximate nearest neighbor indexes or API retrieval tools are used.

Optional checks:

1. Alternative embedding model.
2. Reranking versus no reranking.
3. Disclosure-block chunking versus fixed-token chunking.
4. Hybrid BM25/vector retrieval versus pure vector retrieval.

## Manuscript Reporting Language

Suggested concise main-text language:

> Text-based contextual retrieval constructs a narrative information environment by selecting filing text chunks according to a disclosed retrieval operator. In our demonstration, we use keyword-ranked retrieval over construct-tagged 10-K chunks to keep the context selection inspectable. In embedding-based implementations, researchers should additionally report chunking rules, embedding model, vector index, similarity metric, top-k, reranking, context budget, and retrieval logs.

## Reviewer Risk and Response

Potential reviewer concern:

> The paper discusses RAG but does not implement a production vector database.

Response:

> The demonstration is not designed to benchmark RAG systems. It uses an inspectable retrieval prototype to show how retrieval environments affect valid inference. We separately provide the implementation fields required for vector-store replication so that future studies can apply the same reporting logic to embedding-based RAG.
