# Response To Reviewers Outline: RAG And Evidence-Traceability Positioning

## Reviewer Concern

The manuscript needed clearer positioning against non-accounting RAG evaluation, attribution, and citation-support literature. Without that comparison, reviewers could interpret retrieval-environment validity as a relabeling of context relevance, answer faithfulness, or citation quality.

## Revision Response

We expanded Section II to engage directly with evidence-attribution and citation-generation research. The revision now cites Rashkin et al. (2023) and Gao et al. (2023), in addition to Lewis et al. (2020), Es et al. (2024), and Saad-Falcon et al. (2024).

## Key Distinction Added

General RAG and attribution research asks whether model output is supported by retrieved or cited sources. The revised manuscript explains that auditing research requires a further question: whether those sources instantiate the intended audit construct and whether the generated claim stays within the inference that public filing text and management-reported XBRL can support.

## Planned Response-Letter Language

Suggested response:

> We agree that the manuscript should be more explicit about its relationship to the broader RAG and attribution literature. We revised Section II to discuss RAG evaluation, source attribution, and citation-supported generation research, including RAGAS, ARES, AIS, and ALCE. We then clarify the incremental audit-methodological contribution: source attribution and answer faithfulness are necessary but not sufficient for LLM-based auditing research. A claim may be faithful to retrieved public-filing text or management-reported XBRL while still failing to support the intended audit construct or overstating audit evidence sufficiency. Retrieval-environment validity therefore asks whether the retrieved environment supports the audit-research inference, not only whether the generated answer is cited or faithful.

## Residual Boundary

The paper still does not claim to benchmark RAG systems, improve citation generation, or validate audit-performance outcomes. The contribution remains a research-design framework for specifying, preserving, and evaluating retrieval-created information environments in LLM-based auditing studies.

