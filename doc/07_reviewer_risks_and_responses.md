# Reviewer Risks and Responses

## Risk 1: The Framework Looks Like a Checklist

Reviewer concern:

> The paper offers a broad checklist rather than a theoretically grounded methodological contribution.

Response:

Make retrieval-environment validity the primary contribution. Present the typology, correctness protocol, failure taxonomy, checklist, and demonstration as supporting tools that operationalize this single concept.

## Risk 2: The Concept Is Just Construct Validity

Reviewer concern:

> Information environments have always mattered in audit research.

Response:

Emphasize the dynamic retrieval layer. In LLM-RAG studies, the information environment is selected, ranked, transformed, and presented by a retrieval system at runtime. Retrieval-environment validity is a diagnostic lens for construct validity in this setting, not a replacement for construct validity.

## Risk 3: XBRL Is Not Audit Evidence

Reviewer concern:

> XBRL is management-prepared reporting data, not independent audit evidence.

Response:

Agree and make this a boundary condition. XBRL encodes management-coded reported accounting relationships that are relevant to, but not equivalent to, audit assertions. The paper does not claim that XBRL constitutes sufficient appropriate audit evidence.

## Risk 4: Hybrid Retrieval Looks Like the Winner

Reviewer concern:

> The paper may imply that hybrid retrieval is best.

Response:

State that hybrid retrieval supports a different construct: narrative-numeric integration. It may improve integrated correctness but reduce separability and increase construct contamination.

## Risk 5: Audit-Valid Correctness Is Subjective

Reviewer concern:

> Audit-valid correctness depends on expert judgment.

Response:

Treat audit-valid correctness as expert-coded judgment, not an objective benchmark. Require independent coders, coder expertise disclosure, coding guide, inter-rater agreement, and disagreement resolution.

## Risk 6: Demonstration Is Too Weak

Reviewer concern:

> The demonstration does not show that the framework changes research inference.

Response:

Use actual SEC filing and Inline XBRL data. Provide retrieved text chunks, XBRL relation paths, claim-level coding, failure modes, and an inference shift table.

## Risk 7: The Paper Sounds Like Computer Science

Reviewer concern:

> The paper reads like a technical RAG or GraphRAG paper rather than an audit methodology paper.

Response:

Minimize technical architecture discussion. Focus on audit constructs, construct validity, relevance, reliability, documentation, internal validity, and professional judgment. Keep GraphRAG and MCP discussion out of the main contribution.

## Modest Contribution Paragraph

Our framework is intentionally modest. It does not claim that XBRL-based retrieval improves audit judgment, that XBRL data constitute audit evidence, or that hybrid retrieval is universally superior. Instead, it provides a way for audit researchers to specify, validate, and report the retrieval-created information environment so that claims about LLM performance or audit judgment are appropriately bounded.
