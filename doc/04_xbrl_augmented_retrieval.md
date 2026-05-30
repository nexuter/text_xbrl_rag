# XBRL-Augmented Retrieval

## Safe Framing

XBRL encodes management-coded reported accounting relationships that are relevant to, but not equivalent to, audit assertions.

XBRL is not independent audit evidence or ground truth.

## Why XBRL Matters for Audit Research

XBRL provides a machine-readable representation of reported accounting relationships embedded in financial statements and disclosures. These relationships can help researchers study whether LLMs preserve, distort, hallucinate, or over-rely on reported accounting relationships when generating audit-related claims.

## What XBRL Can Represent

XBRL-based relational retrieval can expose:

- reported facts
- accounting concepts
- reporting periods
- units
- dimensions
- calculation relationships
- presentation relationships
- extension concepts
- company-specific tagging choices
- relationships between line items and disclosures

## What XBRL Does Not Represent

XBRL does not directly represent:

- independent audit evidence
- the full evidential basis auditors use
- management intent
- fraud concealment
- internal control operating effectiveness
- auditor-client negotiation
- professional skepticism under social pressure
- third-party evidence reliability

## Retrieval Typology

| Retrieval Design | Retrieval Operator | Best-Suited Construct | Key Risk |
|---|---|---|---|
| LLM-only | None | Baseline reasoning | Pretraining contamination |
| Text-based contextual retrieval | Semantic similarity | Narrative comprehension | Relation hallucination |
| XBRL-based relational retrieval | Typed relation traversal | Reported relation preservation | Source overreach |
| Hybrid retrieval | Semantic + relation traversal | Narrative-numeric integration | Reduced separability / construct contamination |

## Important Distinction

Text-based and XBRL-based retrieval differ by retrieval operator, not by whether the final prompt is natural language.

Text-based retrieval selects information by semantic similarity. XBRL-based relational retrieval selects information by typed accounting-relation traversal.

## Hybrid Retrieval Caution

Hybrid retrieval may increase integrated correctness but reduce separability because narrative and relational inputs are jointly introduced.

Hybrid retrieval should not be presented as universally superior. It supports a different construct: narrative-numeric integration.
