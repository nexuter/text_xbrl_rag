# Adjacent-Validity Positioning Revision Log

## Purpose

This log records implementation of `SR-01` from `plan/112_second_revision_comprehensive_revise_plan.md`.

The reviewer reports raised a central contribution concern: retrieval-environment validity could be read as a relabeling of construct validity, measurement validity, reproducibility, RAG evaluation, audit documentation, or XBRL data-quality research. This task strengthens the manuscript's incremental positioning against those adjacent concepts.

## Files Updated

| File | Change |
|---|---|
| `submission/Manuscript_Retrieval_as_Research_Design.md` | Added RAG evaluation and evidence-traceability positioning; sharpened synthesis and Section III relation to adjacent concepts; added references |
| `submission/Tables_and_Figures.md` | Expanded Table 2 with XBRL data-quality research, RAG system evaluation, and evidence traceability / answer faithfulness rows |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Workflow tracker updated |

## Literature Added

Added non-accounting RAG / RAG-evaluation references:

1. Lewis et al. (2020), the original RAG architecture paper.
2. Es et al. (2025), Ragas evaluation framework.
3. Saad-Falcon et al. (2024), ARES automated RAG evaluation framework.

These references are used to show that the manuscript recognizes existing RAG evaluation concepts such as context relevance, answer faithfulness, and answer relevance.

## Manuscript Positioning Added

Added a new subsection:

**RAG Evaluation And Evidence Traceability**

The new subsection makes the distinction:

1. generic RAG evaluation asks whether retrieved passages are relevant and generated answers are faithful to retrieved context;
2. retrieval-environment validity asks whether the retrieved environment instantiates the audit construct required for the research inference.

The manuscript now states that a RAG system can retrieve relevant passages and produce faithful answers while still failing an audit research design if the retrieved materials:

1. omit construct-critical assertion evidence,
2. overread management-reported XBRL as audit evidence,
3. confound source type with context volume, ordering, or prompt salience.

## Table 2 Strengthening

Table 2 now includes explicit adjacent-concept rows for:

1. XBRL data-quality research,
2. RAG system evaluation,
3. evidence traceability / answer faithfulness.

These additions directly respond to the reviewers' request to distinguish retrieval-environment validity from adjacent validity and RAG-evaluation ideas.

## Incremental Contribution Sharpened

The revised language positions retrieval-environment validity as:

> an audit-specific validity question about whether the dynamically retrieved environment supports the audit construct and inference being studied.

This is narrower and stronger than claiming that retrieval-environment validity replaces existing validity categories. It complements them by identifying a runtime retrieval mechanism through which they can fail.

## QA

Search QA confirmed:

1. the new RAG references are cited in the manuscript text,
2. each new reference appears in the reference list,
3. Table 2 includes the new XBRL data-quality, RAG system evaluation, and evidence traceability rows,
4. the added language preserves the audit-methodology framing rather than turning the paper into a generic RAG-evaluation paper.

## Sources Checked

Primary sources checked while preparing this revision:

1. Lewis et al. (2020), arXiv record for *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
2. Es et al. (2025), arXiv record for *Ragas: Automated Evaluation of Retrieval Augmented Generation*.
3. Saad-Falcon et al. (2024), arXiv record for *ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems*.

## Remaining Boundary

This task strengthens conceptual contribution and literature positioning. It does not add empirical sensitivity evidence, XBRL concept coverage diagnostics, or expert audit-domain coding. Those remain separate P0 workstreams.

## SR-01 Status

`SR-01` is complete. The next substantive workstream is ex ante audit construct protocol development for revenue and inventory (`SR-03` and `SR-04`), with XBRL concept/relation coverage diagnostics (`SR-05`) following closely.
