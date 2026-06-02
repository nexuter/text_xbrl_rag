# Response To Reviewers Outline: Literature, Terminology, And Title Cleanup

## Reviewer Concern

The prior draft risked overclaiming the implemented XBRL component and contained small citation-status vulnerabilities that could distract reviewers from the methodological contribution.

## Revision Response

We revised the title and terminology to better match the implemented design. The title now refers to `XBRL Relational Retrieval` rather than `XBRL-Augmented Retrieval`, because the paper implements source-traceable XBRL fact/path retrieval and does not claim to implement a full ontology database, RDF/OWL graph store, or GraphRAG benchmark.

## Citation Cleanup

We rechecked RAG/RAG-evaluation citations and updated the manuscript to cite the proceedings versions of RAGAS and ARES rather than treating them as arXiv-only working papers.

## Audit-Validity Boundary

We also softened submission-facing audit-validity terminology. The revision consistently treats audit-boundary measures as preliminary diagnostics unless independently reviewed by audit-domain experts. This protects the paper's main contribution: retrieval-environment validity and claim-level evidence-use traceability, not audit-performance validation.

## Planned Response-Letter Language

Suggested response:

> We appreciate the reviewers' concern that the manuscript should not overstate either the XBRL implementation or the audit-validity implications of the demonstration. We revised the title to use "XBRL Relational Retrieval," updated terminology throughout the submission-facing package, and clarified that the implemented XBRL component is a source-traceable fact/path retrieval environment rather than a full ontology or graph-database architecture. We also updated RAG evaluation references to their proceedings records and retained the paper's boundary that preliminary audit-boundary diagnostics are not model-performance or audit-validity evidence absent expert review.

## Remaining Author Actions

The only unresolved fields are author-specific submission metadata, including author identities, affiliations, corresponding-author information, funding, conflicts, acknowledgments, submission date, and final journal-specific disclosure wording.

