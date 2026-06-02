# Response-To-Reviewers Outline: Audit-Specific Fit

## Reviewer Concern

The paper could be read as a general AI/RAG or accounting-data methodology paper rather than a contribution to auditing methodology.

## Revision Summary

We revised the introduction, claim-level correctness section, discussion, conclusion, and online supplement to strengthen the audit-specific logic. The revised manuscript now makes explicit that retrieval-environment validity is needed because audit inferences depend on the nature, reliability, and evidentiary status of the materials supplied to the LLM.

## Specific Changes

1. We clarified the intended audit-research use cases:
   - LLMs as measurement tools in archival or textual audit research;
   - audit analytics and retrieval/system-design studies;
   - LLM-assisted audit judgment studies.
2. We added an audit-specific example showing that inventory policy text plus XBRL reserve facts may support a bounded factual claim and an assertion-relevant diagnostic, but not an audit conclusion about reserve sufficiency, fair valuation, or management bias.
3. We added Appendix Table F1B to distinguish supported and unsupported interpretations when the same retrieved evidence is used at different audit interpretation levels.
4. We strengthened the conclusion to state that the contribution is not generic retrieval documentation. It is reviewer-evaluable guidance for deciding whether dynamically retrieved materials support an audit construct, preserve evidence meaning, remain traceable, avoid source overreach, and stop short of audit evidence sufficiency when the evidence consists only of public filings and management-reported XBRL.

## Suggested Response-Letter Language

We agree that the paper must be clearly positioned as an auditing-methodology contribution. We revised the manuscript to make the audit-specific logic more explicit. The revised introduction now identifies the intended audit-research use cases: archival audit studies using LLMs as measurement tools, audit analytics and system-design studies, and judgment-and-decision-making studies of LLM-assisted audit judgments. We also added a compact example showing that the same retrieved evidence can be text-supported and graph-valid while remaining insufficient for an audit conclusion.

The online supplement now includes Appendix Table F1B, which distinguishes supported and unsupported interpretations across audit interpretation levels. This table makes clear that public filing text and management-reported XBRL may support source support, graph validity, assertion relevance, and preliminary audit-boundary diagnostics, but not audit evidence sufficiency, misstatement, fraud, reserve adequacy, or valuation correctness. These revisions sharpen the paper's audit-specific contribution and preserve the boundary between methodological protocol validation and substantive audit-judgment validation.

## Evidence Locations

- Main manuscript, Introduction.
- Main manuscript, Section V, claim-level correctness hierarchy.
- Main manuscript, Section VIII, discussion and boundary conditions.
- Main manuscript, Conclusion.
- Online Supplement, Appendix Table F1B.

## Boundary To Preserve

Do not state that the current public-filing/XBRL demonstration validates audit judgments. The revision strengthens audit-specific fit by clarifying where audit inference must stop unless additional audit evidence and expert validation are added.
