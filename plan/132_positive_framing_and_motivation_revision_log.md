# Positive Framing And Motivation Revision Log

## Purpose

This revision implements SR-12 from the second-revision workflow. The objective is to make the manuscript read as assertive and bounded rather than cautious and repetitive.

## Implemented Revisions

1. Rewrote the abstract to foreground:
   - the under-specified retrieved information environment problem;
   - retrieval-environment validity as the methodological contribution;
   - reviewer-facing decision rules;
   - the nine-filer evidence package;
   - the design-specific hybrid source-use divergence result.
2. Revised the opening introduction to state the methodological problem more directly.
3. Added a reader-facing retrieval mechanics example:
   - top-k text retrieval can omit construct-relevant evidence;
   - increasing top-k changes context volume;
   - relation-path depth and filtering change the effective XBRL information set.
4. Moved the claim-level evidence divergence motivation earlier in the introduction.
5. Added an early compact example distinguishing:
   - text-supported claims;
   - graph-valid claims;
   - audit-boundary relevance;
   - integrated text-XBRL evidence use.
6. Revised the discussion section to reduce repeated caveat language and translate boundaries into design implications.

## Reviewer-Facing Position

The revised opening now leads with the paper's problem, contribution, reviewer decision rule, and evidence package. The design boundaries remain, but they are framed as methodological design requirements rather than repeated disclaimers.

## Files Revised

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## Key Text Added

- Abstract now reports that, within this design, 8 of 89 hybrid claims used both text and XBRL sources, while 61 used text only and 20 used XBRL only.
- Introduction now explains how top-k, context volume, relation paths, relation depth, and filtering affect the effective information set observed by the model.
- Introduction now provides a compact inventory-reserve example that distinguishes source support from audit conclusion.

## QA Focus

- Ensure the 8/89 result remains described as design-specific.
- Ensure the abstract does not imply model-performance validation.
- Ensure the discussion still preserves the audit evidence sufficiency boundary while reducing defensive repetition.

## Remaining Boundary

This step does not add new analyses or output reruns. It improves framing and placement of existing evidence.
