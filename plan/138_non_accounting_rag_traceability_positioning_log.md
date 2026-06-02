# Non-Accounting RAG And Evidence-Traceability Positioning Log

Date: 2026-06-01

## Purpose

This log documents SR-15 of the second-revision workflow. The reviewer-facing goal was to strengthen the manuscript's engagement with non-accounting RAG evaluation, evidence attribution, and citation-support research while preserving the paper's audit-methodological contribution.

## Reviewer Risk Addressed

The prior draft cited RAGAS and ARES and distinguished generic RAG evaluation from retrieval-environment validity. However, a reviewer could still ask whether the paper is simply rebranding existing RAG faithfulness, attribution, or citation-quality ideas for accounting. The revision makes the distinction explicit.

## Literature Added

1. Rashkin et al. (2023), *Computational Linguistics*: attribution in natural language generation and the Attributable to Identified Sources framework.
2. Gao et al. (2023), EMNLP: citation-supported LLM generation and automatic citation evaluation.

These sources complement Lewis et al. (2020), Es et al. (2024), and Saad-Falcon et al. (2024) by focusing on source attribution and citation support rather than only retrieval relevance and answer faithfulness.

## Manuscript Revision

Section II, `RAG Evaluation And Evidence Traceability`, now states that:

- general RAG evaluation asks whether retrieved passages are relevant and answers are faithful;
- attribution and citation-generation research asks whether generated statements are linked to identified sources;
- audit research requires an additional validity question: whether the retrieved source environment corresponds to the intended audit construct and stays within public-filing/XBRL evidence boundaries.

## Contribution Sharpening

The new language clarifies that retrieval-environment validity is not equivalent to:

- context relevance;
- answer faithfulness;
- citation quality;
- generic source attribution.

Instead, retrieval-environment validity asks whether a source-supported answer can support the audit-research inference being drawn. This distinction is central because a generated claim can be faithful to management-reported text or XBRL and still overstate audit evidence sufficiency.

## Files Updated

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## Verification

QA checks should confirm:

- `Rashkin et al. 2023` and `Gao et al. 2023` are cited in the RAG/evidence-traceability section.
- Both references appear in the reference list.
- The revision does not imply that citation support or attribution is sufficient for audit-validity claims.

## Source Status Notes

- Rashkin et al. (2023): https://aclanthology.org/2023.cl-4.2/
- Gao et al. (2023): https://aclanthology.org/2023.emnlp-main.398/

