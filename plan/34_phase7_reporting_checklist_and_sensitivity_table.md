# Phase 7 Reporting Checklist and Sensitivity Table

## Purpose

This checklist provides manuscript and appendix reporting standards for LLM-based audit research that uses text retrieval, XBRL relational retrieval, or hybrid retrieval.

The checklist is designed for AJPT-style methodological transparency. It helps readers evaluate retrieval-environment validity by making the retrieval-created information environment observable.

## Main-Text Reporting Checklist

The main text should report the following at a concise level.

| Item | Required Main-Text Disclosure |
|---|---|
| Research construct | Audit construct the retrieval condition is intended to support. |
| Retrieval design | LLM-only, text, XBRL, hybrid, or other. |
| Retrieval operator | Semantic similarity, keyword ranking, relation traversal, seed-pattern selection, etc. |
| Retrieval unit | Text chunk, fact, concept, relation edge, relation path, or combined context. |
| Source data | Filing type, period, accession, and source data type. |
| Context budget | Word/token count by condition. |
| Source traceability | Whether chunk IDs, fact IDs, path IDs, and prompt files are preserved. |
| XBRL boundary | Statement that XBRL is reported accounting information, not audit evidence. |
| Evaluation unit | Claim-level coding rather than answer-level accuracy. |
| Correctness layers | Text-supported, graph-valid, audit-valid, integrated. |
| Failure modes | Retrieval-related failure modes considered. |
| Demonstration purpose | Descriptive methodological demonstration, not retrieval ranking. |

## Tiered Reporting Standard

The checklist should not read as a burdensome compliance regime. It should be presented as a tiered reporting standard that scales with the study's claims.

| Tier | Intended Study Type | Minimum Required Reporting | What Not to Claim |
|---|---|---|---|
| Tier 1: Descriptive methodological demonstration | Shows how retrieval design changes valid inference | Retrieval units, operators, source IDs, context budgets, prompts, logs, claim coding, selected spot-checks | Do not claim retrieval performance superiority. |
| Tier 2: Empirical LLM audit study using RAG | Tests LLM outputs under retrieval-augmented conditions | Tier 1 plus embedding/index metadata, fuller sensitivity checks, expert coding, reliability evidence | Do not attribute effects to the model without separating retrieval effects. |
| Tier 3: Retrieval-system or GraphRAG evaluation | Evaluates retrieval architecture or system performance | Tier 2 plus benchmark design, retrieval metrics, system parameters, scalability/latency evidence | Do not generalize to audit validity without audit-specific correctness coding. |

The current paper should position its demonstration primarily as Tier 1, while offering Tier 2 and Tier 3 reporting guidance for future researchers.

## Mapping to Retrieval-Environment Validity

Each reporting item should connect to the paper's central validity framework.

| Validity Dimension | Reporting Items That Operationalize It | Reviewer Question Addressed |
|---|---|---|
| Selection validity | Retrieval unit, query/seed, filters, top-k, traversal depth | Did the retriever select construct-relevant information? |
| Representation validity | Chunking rule, XBRL fact schema, relation edge schema, taxonomy version, dimensions | Was the selected information faithfully represented? |
| Stability | Retrieval logs, repeated retrieval checks, index metadata, taxonomy version | Would equivalent retrieval runs create the same information environment? |
| Traceability | Source IDs, prompt files, raw outputs, spot-checks | Can claims be traced back to retrieved evidence? |
| Separability | Context budgets, hybrid assembly rule, LLM-only baseline, token equalization | Can retrieval effects be distinguished from model or prompt effects? |

This mapping should appear in either the main methodological guidance section or an appendix table. It prevents the checklist from looking like a generic reproducibility appendix.

## Appendix Reporting Checklist

The appendix or reproducibility package should report the following in detail.

### Source and Extraction

| Item | Required Appendix Disclosure |
|---|---|
| Source filing manifest | CIK, accession, filing date, period end, source URL. |
| Download script | Script and execution date. |
| Raw file manifest | Raw file names and hashes where feasible. |
| Text extraction rule | Parser, included sections, excluded sections. |
| XBRL extraction rule | Parser, fact fields, linkbase relation fields. |
| Taxonomy source | Taxonomy year/version and extension taxonomy treatment. |

### Text Retrieval

| Item | Required Appendix Disclosure |
|---|---|
| Chunk table | Chunk IDs, source files, section labels, text, counts. |
| Chunking rule | Unit, target size, overlap, tokenizer/word-count rule. |
| Embedding metadata | Model, version, dimensions, preprocessing. |
| Vector index metadata | Store, index type, similarity metric. |
| Retrieval parameters | Query, top-k, filters, reranking, prompt inclusion. |
| Text retrieval log | Retrieved chunk IDs, ranks, scores, prompt position. |

### XBRL Retrieval

| Item | Required Appendix Disclosure |
|---|---|
| Fact table | Fact IDs, concepts, values, units, periods, dimensions. |
| Concept table | Labels, namespaces, standard/extension status. |
| Relation table | Source concept, target concept, relation type, arcrole, role, weight. |
| RDF/OWL mapping | Classes, properties, namespaces, export or mapping rules. |
| Retrieval parameters | Seed concepts, relation filters, traversal depth, period/unit filters. |
| XBRL retrieval log | Fact/path IDs, ranks, scores, prompt position. |

### Hybrid and Prompting

| Item | Required Appendix Disclosure |
|---|---|
| Hybrid assembly rule | Component budgets, ordering, truncation, labels. |
| Prompt files | Final rendered prompts for every condition. |
| Prompt shell | Task instruction, context restriction, output format. |
| Token counts | Context length and total prompt length by condition. |
| LLM configuration | Model, version, provider, temperature, context window, execution date. |

### Coding and Validation

| Item | Required Appendix Disclosure |
|---|---|
| Raw outputs | Unedited model responses. |
| Claim segmentation | Rule for splitting outputs into claims. |
| Coding rubric | Text, graph, audit, and integrated correctness rules. |
| Failure mode taxonomy | Coding definitions and examples. |
| Expert review | Coder qualifications and reliability plan. |
| Spot-checks | Selected text and XBRL source checks. |

## Sensitivity Check Table

| Retrieval Component | Sensitivity Check | Validity Threat Addressed | Minimum Reporting |
|---|---|---|---|
| Text chunking | Smaller vs larger chunks | Selection and representation validity | Chunk size, overlap, output changes. |
| Text chunking | No overlap vs overlap | Omission at chunk boundaries | Overlap rule and affected claims. |
| Text retrieval | Top-k variation | Relevance/noise tradeoff | Top-k values and context counts. |
| Text retrieval | Query wording variation | Construct-query dependence | Query variants and retrieval changes. |
| Text retrieval | Embedding model variation | Model-specific semantic retrieval | Embedding models and rank shifts. |
| Text retrieval | Reranking vs no reranking | Added selection layer | Reranker and affected included chunks. |
| XBRL retrieval | Direct arcs vs depth-2 paths | Relation coverage vs noise | Traversal depth and path counts. |
| XBRL retrieval | Relation type filters | Construct alignment | Relation types included/excluded. |
| XBRL retrieval | Standard concepts only vs extension concepts | Representation of filer-specific reporting | Extension policy and affected claims. |
| XBRL retrieval | Current period vs comparative periods | Temporal alignment | Period filters and fact counts. |
| XBRL retrieval | Dimension filters | Aggregation and disaggregation risk | Dimension policy and affected facts. |
| Hybrid retrieval | Equalized vs non-equalized token budget | Model-retrieval confounding | Word/token budget by component. |
| Hybrid retrieval | Text-first vs XBRL-first ordering | Prompt-order sensitivity | Ordering rule and output shifts. |
| LLM execution | Model variation | Model-specific behavior | Model names, versions, and coding differences. |
| LLM execution | Prompt wording variation | Prompt sensitivity | Prompt variants and claim shifts. |
| Full pipeline | Repeated retrieval run | Retrieval stability | Same query repeated, rank stability. |

## Reproducibility Package File Map

Suggested file groups:

| Folder | Contents |
|---|---|
| `raw/` | Raw filings or source URLs and hashes. |
| `metadata/` | Filing manifest and source document table. |
| `text/` | Text extraction output and chunk table. |
| `xbrl/` | Fact table, concept table, relation edge table, taxonomy manifest. |
| `ontology/` | RDF/OWL mapping or export. |
| `retrieval/` | Retrieval logs, context manifests, selected context files. |
| `prompts/` | Final prompt files. |
| `outputs/` | Raw LLM outputs and run summaries. |
| `coding/` | Claim-level coding, failure modes, inference shift tables. |
| `validation/` | Source and graph spot-check memos. |

## Reviewer-Facing Minimum Standard

A reviewer should be able to answer these questions from the manuscript and appendix:

1. What information was available to be retrieved?
2. What retrieval unit was selected?
3. What operator selected it?
4. What parameters governed selection?
5. What entered the final prompt?
6. What source IDs support each model claim?
7. Which output differences can be attributed to retrieval design, and which remain confounded?
8. Which claims are text-supported, graph-valid, audit-valid, or integrated?
9. What limitations prevent treating XBRL relations as audit evidence?

## Manuscript Use

This checklist should support three manuscript elements:

1. A concise main-text reporting table.
2. An appendix reporting template.
3. A reproducibility package checklist.

The checklist should be positioned as an operational tool for retrieval-environment validity, not as a universal compliance standard.
