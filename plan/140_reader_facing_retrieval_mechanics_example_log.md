# Reader-Facing Retrieval Mechanics Example Log

Date: 2026-06-01

## Purpose

This log documents SR-16 of the second-revision workflow. The reviewer-facing goal was to make the retrieval mechanics understandable to accounting readers without turning the manuscript into a technical systems paper or implying that unimplemented architectures were completed.

## Reviewer Risk Addressed

Reviewers and readers may accept the conceptual argument but still ask how text retrieval and XBRL relational retrieval were operationalized. If the mechanics are opaque, the demonstration may appear difficult to reproduce and the framework may look too abstract.

## Revision Implemented

Added a new Section IV subsection, `Mechanics Example`, that walks through one inventory valuation prompt across:

1. text retrieval;
2. XBRL relational retrieval;
3. hybrid retrieval.

The example explains how:

- text chunking, filtering, ranking, and top-k selection create the narrative information set;
- changing top-k can add or remove construct-relevant chunks while also changing context volume;
- XBRL concept-family selection, fact metadata, and relation-path rendering create the structured information set;
- omitting relation paths leaves reported facts but removes part of the accounting relationship environment;
- hybrid retrieval requires documentation of source order, token budget, and actual claim-level integration.

## Supplement Revision

Appendix B now includes a reader-facing mechanics note explaining that the current baseline text environment is a keyword-ranked top-5 chunk design and that Appendix I reports top-3/top-8 source-environment perturbations.

Appendix C now includes a reader-facing mechanics note explaining that the current XBRL environment uses table-based fact/path bundles, not an implemented RDF/OWL graph database, and that the fact-only perturbation illustrates the role of relation paths.

## Boundary Preserved

The revision does not claim:

- production vector RAG performance;
- completed chunk-size or overlap sensitivity;
- an implemented RDF/OWL graph database;
- completed GraphRAG performance evaluation;
- model-output robustness from retrieval-stage perturbations.

## Files Updated

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## Verification

QA should confirm that the new language:

- includes top-k, chunking, relation-path, source-order, and token-budget mechanics;
- points readers to Appendices B, C, and I;
- preserves the distinction between completed Tier 1 diagnostics and future Tier 2/Tier 3 sensitivity or benchmark work.

