# Nine-Filer Demonstration Scope Reframing Log

## Purpose

This revision implements SR-10 from the second-revision workflow. The objective is to prevent reviewers from reading the nine-filer demonstration as a representative empirical sample or model-performance validation exercise.

## Implemented Revisions

1. Revised the main manuscript to state that the demonstration has four evidentiary layers:
   - three deep cases for source tracing and claim-level illustration;
   - six extension cases for bounded protocol applicability across varied reporting environments;
   - retrieval-stage sensitivity diagnostics for context-volume and source-composition transparency;
   - a 120-claim independent coding sample for source-use and integration coding reliability.
2. Revised the main manuscript's bounded-extension wording to specify that findings apply within the current retrieval implementation.
3. Revised the main manuscript's hybrid-claim count paragraph to state that the 8/89, 61/89, and 20/89 counts are design-specific diagnostics, not estimated population frequencies.
4. Added `Appendix Table H1. Demonstration Evidence Layers And Permitted Inferences` to the online supplement.
5. Updated the second-revision workflow tracker to mark SR-10 completed.

## Reviewer-Facing Position

The nine-filer package should be described as a layered protocol-validation package. The correct inference is:

> The protocol can be specified, preserved, reconstructed, independently coded for source-use variables, and applied across varied filer settings.

The incorrect inference is:

> The paper estimates the prevalence of hybrid non-integration, proves one retrieval method is superior, or validates model performance.

## Design-Specific Count Boundary

The 72 outputs, 281 preliminary coded claims, and 89 hybrid-condition claims are retained because they document the protocol and make source-use heterogeneity inspectable. They should not be used as population denominators for SEC filers, audit tasks, LLM systems, or retrieval methods.

## Files Revised

- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `plan/112_second_revision_comprehensive_revise_plan.md`

## QA Notes

- Search should confirm that the manuscript contains design-boundary phrases such as "in this design" and "in this model, prompt, and context architecture."
- The appendix now states explicitly what each evidence layer supports and what it does not support.
- No DOCX files were regenerated in this step.
