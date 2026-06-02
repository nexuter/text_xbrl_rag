# Response-To-Reviewers Outline: Positive Framing And Early Motivation

## Reviewer Concern

The manuscript was careful but risked sounding too defensive. Reviewers could miss the positive methodological contribution because boundary statements appeared before the reader fully saw the problem, decision rule, and evidence package.

## Revision Summary

We revised the abstract, introduction, and discussion to lead with the methodological problem and positive contribution. The revised manuscript now explains early that retrieval creates the effective information set observed by the LLM and that this information set must be evaluated before output-based audit inferences are interpreted.

## Specific Changes

1. The abstract now states the problem, framework, reviewer decision rule, evidence package, and key design-specific source-use divergence result.
2. The introduction now includes a concrete retrieval mechanics example showing how top-k, context volume, relation paths, depth, and filtering affect the model's effective information set.
3. The introduction now moves claim-level evidence divergence earlier, before the literature review.
4. The introduction now includes a compact example separating text-supported, graph-valid, audit-boundary, and integrated evidence-use layers.
5. The discussion now translates boundary conditions into design implications rather than repeating caveats.

## Suggested Response-Letter Language

We revised the opening sections to make the contribution easier to see earlier. The abstract now states the methodological problem, the retrieval-environment validity framework, the reviewer-facing decision rule, and the nine-filer evidence package. We also moved the claim-level source-use divergence result into the introduction, while preserving the design-specific boundary around those counts.

In addition, the revised introduction now includes a reader-facing retrieval mechanics example. It explains how top-k text selection, context-volume changes, XBRL relation paths, relation depth, and filtering choices alter the effective information set observed by the LLM. We also added a compact inventory-reserve example that distinguishes text-supported, graph-valid, audit-boundary, and integrated evidence use. These changes make the paper's methodological contribution more concrete without expanding the paper into a performance benchmark.

## Evidence Locations

- Abstract.
- Main manuscript, Introduction.
- Main manuscript, Discussion and Boundary Conditions.

## Boundary To Preserve

The early source-use divergence result should remain described as design-specific. It should not be characterized as a population estimate, model-performance result, or evidence that hybrid retrieval is superior.
