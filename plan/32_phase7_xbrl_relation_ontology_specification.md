# Phase 7 XBRL Relational Retrieval and Ontology Specification

## Purpose

This specification defines how XBRL facts and reporting relationships should be represented, retrieved, logged, and reported when used as relational context for LLM audit research.

The purpose is to make XBRL-based retrieval inspectable and reproducible. XBRL relation retrieval should be framed as retrieval over management-coded reported accounting relationships, not as retrieval over independent audit evidence.

## Reviewer-Facing Claim

XBRL-based relational retrieval differs from text retrieval because the retrieval operator is not semantic similarity over narrative chunks. It is typed relation selection or traversal over reported facts, concepts, contexts, dimensions, and taxonomy/linkbase relations. Therefore, it requires a different data structure and different reporting standards.

## Current Demonstration Status

The current Phase 6 demonstration uses:

| Component | Current Implementation |
|---|---|
| Source | Inline XBRL extracted from actual SEC filings |
| Fact store | CSV fact table |
| Relation store | CSV path table from extracted linkbase relations |
| Retrieval | Seed-pattern selection over concepts, labels, and relation paths |
| Relation depth | Direct arcs |
| RDF/OWL store | Not implemented in the current prototype |
| Graph DB | Not implemented in the current prototype |

Reviewer-safe wording:

> The demonstration uses table-based XBRL relational retrieval to preserve inspectability. The appendix provides an RDF/OWL-compatible mapping that shows how the same facts and relations can be represented in an ontology or graph database for future implementations.

## XBRL Fact Node Schema

## Minimum Versus Extended Implementation

To avoid overclaiming ontology construction, the paper should distinguish minimum relational retrieval from an ontology-backed implementation.

| Level | Appropriate Use | Required Components | Manuscript Language |
|---|---|---|---|
| Minimum relational prototype | Methodological demonstration focused on inspectable reported relationships | Fact table, relation edge/path table, source IDs, retrieval seeds, traversal or selection rule, prompt rendering | "Table-based XBRL relational retrieval over disclosed facts and direct relation paths." |
| Ontology-compatible implementation | Replication package or future study needing portability across graph tools | Minimum prototype components plus RDF/OWL mapping, stable namespaces, class/property definitions, taxonomy manifest | "RDF/OWL-compatible representation of XBRL facts and relations." |
| Graph database implementation | Study evaluating graph traversal, graph retrieval, or large-scale relation search | Ontology-compatible components plus graph database/triple store, query language, index details, traversal execution logs | Not required for the current demonstration unless graph-system performance is claimed. |

The current demonstration belongs to the minimum relational prototype level. The RDF/OWL mapping is included as a portability and reporting schema, not as evidence that a full ontology database was implemented.

### Researcher-Coded Versus XBRL-Coded Relations

The paper should separate relations encoded by XBRL from relations introduced by the researcher.

| Relation Type | Source | Interpretation |
|---|---|---|
| XBRL presentation, calculation, and definition relations | Filing taxonomy/linkbase or standard taxonomy | Management-coded or taxonomy-coded reported accounting structure. |
| Concept-to-construct mapping | Researcher coding | Methodological mapping from reported concept to study construct. |
| Concept-to-audit-assertion relevance | Researcher coding | Non-evidentiary relevance judgment for audit research. |

This distinction is important because the ontology layer can otherwise appear to convert reported accounting structure into audit evidence. It does not. It only makes explicit which links are sourced from XBRL and which links are researcher-coded.

Each reported fact should be represented as a node or table row.

| Field | Required | Description |
|---|---:|---|
| `fact_id` | Yes | Stable fact identifier. |
| `ticker` | Yes | Company ticker. |
| `cik` | Yes | SEC CIK. |
| `accession` | Yes | SEC accession number. |
| `concept_qname` | Yes | Namespace-qualified XBRL concept. |
| `concept_name` | Yes | Local concept name. |
| `namespace` | Yes | US GAAP, SEC, DEI, or filer extension namespace. |
| `concept_label` | Recommended | Human-readable label. |
| `value` | Yes | Reported value. |
| `unit_ref` | Recommended | Unit reference ID. |
| `unit` | Yes if numeric | Unit value or measure. |
| `decimals` | Recommended | Reported decimals attribute. |
| `precision` | Optional | Precision if applicable. |
| `context_ref` | Yes | XBRL context ID. |
| `period_type` | Recommended | Instant or duration. |
| `period_start` | If duration | Start date. |
| `period_end` | Yes | End date or instant date. |
| `dimensions` | Yes | Axis-member pairs or none. |
| `source_file` | Yes | Source Inline XBRL/XML file. |
| `source_line_or_xpath` | Recommended | Raw source traceability. |

## XBRL Concept Node Schema

Each concept should be represented separately from individual facts.

| Field | Required | Description |
|---|---:|---|
| `concept_qname` | Yes | Namespace-qualified concept. |
| `concept_name` | Yes | Local name. |
| `namespace` | Yes | Standard or extension taxonomy namespace. |
| `standard_or_extension` | Yes | Whether concept is standard or filer-specific. |
| `label` | Recommended | Preferred label. |
| `documentation_label` | Optional | Documentation label if available. |
| `data_type` | Recommended | Monetary, string, shares, percent, etc. |
| `period_type` | Recommended | Instant or duration. |
| `balance` | Optional | Debit, credit, or none. |
| `taxonomy_year` | Yes | Taxonomy version or filing taxonomy source. |

## XBRL Relation Edge Schema

Each relation should be represented as a typed edge.

| Field | Required | Description |
|---|---:|---|
| `edge_id` | Yes | Stable relation edge ID. |
| `source_concept` | Yes | Source concept. |
| `target_concept` | Yes | Target concept. |
| `relation_type` | Yes | Presentation, calculation, definition, label, reference, or custom. |
| `arcrole` | Yes | XBRL arcrole. |
| `role` | Yes | Extended link role. |
| `order` | Recommended | Presentation or definition order. |
| `weight` | If calculation | Calculation weight. |
| `preferred_label` | Optional | Preferred label role. |
| `taxonomy_year` | Yes | Taxonomy version. |
| `source_linkbase` | Yes | Linkbase or filing source. |
| `extension_flag` | Yes | Whether an extension concept is involved. |

## RDF / OWL-Compatible Mapping

The project does not need a full ontology database to make the methodological point. However, an RDF/OWL-compatible mapping improves portability and helps readers understand how tabular XBRL extraction can support relation retrieval.

### Core Classes

| Class | Description |
|---|---|
| `xbrl:Fact` | Reported XBRL fact instance. |
| `xbrl:Concept` | Taxonomy concept. |
| `xbrl:Unit` | Measurement unit. |
| `xbrl:Context` | Reporting context. |
| `xbrl:Period` | Reporting period. |
| `xbrl:Dimension` | XBRL dimension axis. |
| `xbrl:Member` | XBRL dimension member. |
| `xbrl:RelationEdge` | Typed relation between concepts. |
| `audit:AuditConstruct` | Research construct selected by the researcher. |
| `audit:Assertion` | Audit assertion category. |

### Core Object Properties

| Property | Domain | Range | Meaning |
|---|---|---|---|
| `xbrl:hasConcept` | `xbrl:Fact` | `xbrl:Concept` | Fact reports a concept. |
| `xbrl:hasUnit` | `xbrl:Fact` | `xbrl:Unit` | Fact uses a unit. |
| `xbrl:hasContext` | `xbrl:Fact` | `xbrl:Context` | Fact belongs to a context. |
| `xbrl:hasPeriod` | `xbrl:Context` | `xbrl:Period` | Context has a reporting period. |
| `xbrl:hasDimension` | `xbrl:Context` | `xbrl:Dimension` | Context includes a dimension. |
| `xbrl:hasMember` | `xbrl:Dimension` | `xbrl:Member` | Dimension has a member. |
| `xbrl:hasSourceConcept` | `xbrl:RelationEdge` | `xbrl:Concept` | Relation source concept. |
| `xbrl:hasTargetConcept` | `xbrl:RelationEdge` | `xbrl:Concept` | Relation target concept. |
| `audit:mapsToConstruct` | `xbrl:Concept` or `xbrl:RelationEdge` | `audit:AuditConstruct` | Researcher-coded construct mapping. |
| `audit:mayInformAssertion` | `xbrl:Concept` or `xbrl:RelationEdge` | `audit:Assertion` | Non-evidentiary assertion relevance. |

### Core Data Properties

| Property | Domain | Description |
|---|---|---|
| `xbrl:factValue` | `xbrl:Fact` | Reported value. |
| `xbrl:decimals` | `xbrl:Fact` | Decimals attribute. |
| `xbrl:relationType` | `xbrl:RelationEdge` | Relation type. |
| `xbrl:arcrole` | `xbrl:RelationEdge` | Arcrole URI. |
| `xbrl:role` | `xbrl:RelationEdge` | Extended link role. |
| `xbrl:calculationWeight` | `xbrl:RelationEdge` | Calculation weight. |
| `xbrl:taxonomyYear` | `xbrl:Concept` or `xbrl:RelationEdge` | Taxonomy year/version. |

## Example RDF/Turtle Pattern

```turtle
@prefix xbrl: <https://example.org/xbrl/> .
@prefix audit: <https://example.org/audit/> .
@prefix us-gaap: <https://fasb.org/us-gaap/> .

<fact/F-SBUX-0034>
    a xbrl:Fact ;
    xbrl:hasConcept us-gaap:InventoryValuationReserves ;
    xbrl:factValue "56600000" ;
    xbrl:hasUnit <unit/USD> ;
    xbrl:hasContext <context/c-33> .

<edge/X-SBUX-INVENTORY-001>
    a xbrl:RelationEdge ;
    xbrl:hasSourceConcept us-gaap:InventoryNet ;
    xbrl:hasTargetConcept us-gaap:InventoryValuationReserves ;
    xbrl:relationType "presentation" ;
    audit:mapsToConstruct audit:InventoryValuation ;
    audit:mayInformAssertion audit:Valuation .
```

This example is schematic. Final RDF exports should use stable namespaces, source filing identifiers, and the exact extracted relations.

## Relation Retrieval Operators

An XBRL relation retriever should disclose:

| Operator Component | Required Disclosure |
|---|---|
| Seed selection | Concept names, labels, taxonomy roles, construct mappings, or manual seeds. |
| Relation types | Presentation, calculation, definition, or other relations included. |
| Traversal direction | Parent-to-child, child-to-parent, both, or fact-to-concept-to-relation. |
| Traversal depth | Direct arc, depth 2, depth 3, or bounded path length. |
| Period filter | Current year, comparative years, all periods, or selected contexts. |
| Unit filter | Monetary only, shares, percentages, or all units. |
| Dimension handling | Consolidated only, all dimensions, or selected axis-member pairs. |
| Extension treatment | Include, exclude, separately tag, or map to standard concepts. |
| Ranking | Seed score, path length, relation type priority, fact materiality, or manual order. |
| Prompt rendering | Facts first, paths first, grouped by concept, or grouped by assertion. |

## Relation Retrieval Sensitivity Checks

Minimum checks:

1. Direct arcs versus depth-2 traversal.
2. Presentation-only versus presentation plus calculation plus definition relations.
3. Standard concepts only versus standard plus extension concepts.
4. Current period only versus comparative periods.
5. Consolidated contexts only versus all dimensions.
6. Equalized prompt budget versus unconstrained relation context.

Optional checks:

1. Alternative seed concept lists.
2. Alternative taxonomy years.
3. Calculation-weight-aware ranking.
4. Relation path deduplication rules.
5. Graph database versus tabular retrieval implementation.

## Boundary Conditions

XBRL relation retrieval can support claims about:

- reported fact traceability
- reported relation preservation
- consistency between narrative disclosures and reported tagged facts
- whether the LLM overstates what a reported relation implies

XBRL relation retrieval cannot by itself support claims that:

- an audit assertion is satisfied
- management estimates are reasonable
- controls are effective
- misstatement exists or does not exist
- XBRL is independent audit evidence

## Manuscript Reporting Language

Suggested concise main-text language:

> XBRL-based relational retrieval constructs a structured information environment by selecting reported facts and typed taxonomy or filing relations. Unlike text retrieval, which selects narrative chunks by semantic or keyword similarity, XBRL retrieval selects concepts, facts, contexts, dimensions, and relation paths using disclosed traversal and filtering rules. Because these relations are management-coded representations of reported accounting information, we treat them as relevant to audit constructs but not as independent audit evidence.

## Reviewer Risk and Response

Potential reviewer concern:

> The paper overstates ontology construction or implies that XBRL is audit ground truth.

Response:

> The ontology-compatible schema is a data-management and reporting layer. It improves portability and traceability, but it does not convert XBRL into audit evidence. The correctness protocol separately evaluates graph-validity and audit-validity to prevent this overreach.
