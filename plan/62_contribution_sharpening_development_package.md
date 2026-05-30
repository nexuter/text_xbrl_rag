# Contribution Sharpening Development Package

## Purpose

This package implements the improvements from `plan/61_reviewer_contribution_sufficiency_assessment.md`. It strengthens the manuscript's contribution relative to existing literature by making four points explicit:

1. This is not an audit-system or audit-practice paper.
2. The data/variable-construction contribution is central, not incidental.
3. The demonstration claim is evidence-use divergence, not retrieval performance.
4. Audit-valid coding requires expert review for stronger audit-judgment claims.

## Implemented Improvements

| Improvement From Reviewer Assessment | Implementation |
|---|---|
| Add direct "not a systems paper" contrast. | Added to `plan/56_ajpt_style_alignment_and_v3_revision_package.md` and `plan/60_final_reference_package.md`. |
| Strengthen data/variable-construction contribution. | Added study-level variables to the v3 first-page contribution paragraph: text-supported correctness, graph-valid correctness, audit-valid correctness, integrated correctness, evidence-use type, and failure-mode labels. |
| Tighten demonstration claim. | Replaced performance-oriented wording with evidence-use divergence wording in `plan/56`. |
| Add expert-coding boundary. | Added expert-coding boundary wording to the v3 demonstration section package in `plan/56`. |
| Keep technical and audit-system references subordinate. | Added emerging LLM/RAG audit-system papers to `plan/60` as selective contrast literature, not core references. |

## Sharpened Contribution Hierarchy

The manuscript should now use the following hierarchy consistently:

1. **Conceptual contribution:** retrieval-environment validity.
2. **Research-design contribution:** guidance for aligning retrieval design with audit constructs.
3. **Data/variable-construction contribution:** converting retrieval artifacts and LLM outputs into claim-level evidence-use variables.
4. **Evaluation contribution:** correctness layers and failure modes for diagnosing LLM audit-study outputs.
5. **Demonstration contribution:** SEC/XBRL examples showing that retrieval-condition labels mask heterogeneous claim-level evidence use.

This hierarchy should govern the abstract, introduction, related literature, demonstration, and conclusion.

## Finalized Novelty Statement

Use this statement in the introduction, related literature synthesis, or conclusion:

> Prior accounting and auditing research studies data, tools, models, auditors, or outcomes. This paper studies the retrieval-created information environment that connects source data to LLM output in auditing research designs.

## Finalized Contrast With Emerging Audit-System Papers

Use this statement in the related literature or discussion:

> Emerging LLM/RAG audit studies increasingly evaluate systems, agents, or task performance. Our focus is different: we provide criteria for auditing researchers to evaluate whether the retrieval-created information environment supports the inference they draw from LLM outputs.

## Finalized Data/Variable-Construction Contribution

Use this wording in the contribution paragraph or methodological guidance section:

> The paper contributes to data and variable construction for LLM-based auditing research by converting retrieval artifacts and model responses into study-level variables: text-supported correctness, graph-valid correctness, audit-valid correctness, integrated correctness, evidence-use type, and failure-mode labels.

## Finalized Demonstration Claim

Use this wording in the demonstration section:

> The demonstration's evidentiary contribution is not that one retrieval design performs better. It is that response-level retrieval labels are insufficient: claims within the same condition can rely on different evidence bases, and those differences change the research inference.

## Finalized Expert-Coding Boundary

Use this wording in the demonstration or limitations section:

> Audit-valid and integrated-correctness scores are preliminary author-coded diagnostics unless independently reviewed by audit-domain experts. The main demonstration supports claims about source traceability and claim-level evidence-use divergence. Studies that make stronger claims about audit judgment quality should use expert coding, coder independence, and reliability procedures appropriate to those claims.

## Revised Reviewer Verdict After Improvements

After these improvements, the contribution is stronger and more defensible. A reviewer should now see the paper as:

> A methodological framework for constructing, documenting, and evaluating retrieval-created information environments in LLM-based auditing research.

The paper is still not acceptance-ready until a full v3 manuscript, clean appendix, and final table/figure package are produced. But the contribution itself is now sharper:

1. It is not competing with audit automation papers.
2. It is not competing with RAG architecture papers.
3. It is not claiming XBRL superiority.
4. It is not relying on performance results.
5. It is making a research-design and data/variable-construction contribution.

## Remaining Development Tasks

| Task | Reason |
|---|---|
| Produce full v3 manuscript | The sharpened paragraphs need to be integrated into a coherent full draft. |
| Finalize appendix | Reviewer confidence depends on a clean evidence trail. |
| Check all tables and figures | Tables must support the hierarchy rather than create a toolkit impression. |
| Check reproducibility materials | The data/variable-construction contribution depends on inspectable artifacts. |
| Decide expert-review path | Limited expert review would strengthen acceptance odds, but explicit boundary language may be sufficient for submission. |

## Bottom Line

The reviewer improvement package has been implemented at the planning and manuscript-control level. The contribution now has a clearer route to publication: retrieval-environment validity plus claim-level evidence-use variable construction for LLM-based auditing research.
