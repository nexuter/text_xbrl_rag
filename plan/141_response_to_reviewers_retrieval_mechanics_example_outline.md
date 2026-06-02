# Response To Reviewers Outline: Retrieval Mechanics Example

## Reviewer Concern

The manuscript needed a more concrete explanation of how retrieval choices create the model's effective information set. Without this, readers could understand the framework conceptually but still be uncertain how to implement or evaluate text retrieval, XBRL relational retrieval, and hybrid retrieval.

## Revision Response

We added a reader-facing mechanics example in Section IV and short companion notes in Appendices B and C. The example shows how an inventory valuation task changes when the researcher varies text top-k, XBRL fact/path inclusion, relation-path rendering, and hybrid context assembly.

## Key Clarification

The revision clarifies that changing retrieval settings changes the evidence environment before the LLM generates an output. Top-k affects which narrative chunks enter the prompt. XBRL fact/path settings affect whether the model sees isolated facts or reported accounting relationships. Hybrid retrieval also creates source-order and token-budget issues that must be documented before researchers interpret output differences.

## Planned Response-Letter Language

Suggested response:

> We agree that the framework should be concrete enough for auditing researchers to implement and evaluate. We added a mechanics example in Section IV that walks through a single inventory valuation prompt under text retrieval, XBRL relational retrieval, and hybrid retrieval. The example explains how chunking, top-k, relation-path rendering, source order, and token budget create the effective information set observed by the model. We also added companion notes in Appendices B and C linking the example to the actual top-5 text design, top-3/top-8 perturbations, table-based XBRL fact/path retrieval, and fact-only XBRL perturbation reported in Appendix I.

## Residual Boundary

The revision does not convert the paper into a retrieval-system benchmark. Chunk-size, overlap, traversal-depth, and GraphRAG sensitivity are identified as Tier 2 or Tier 3 requirements when researchers make stronger model-performance or system-performance claims.

