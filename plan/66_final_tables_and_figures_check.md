# Final Tables And Figures Check

## Purpose

This memo finalizes the table and figure strategy for the AJPT Methodological Papers submission. The review stance is that of an AJPT reviewer asking:

> Do the tables and figures clarify the methodology contribution, or do they make the paper look like a model-performance benchmark?

## Reviewer Verdict

The table and figure package is **near accept-level** after final placement discipline.

The conceptual tables and two figures strongly support the paper's methodology contribution. The remaining risk is not table content but table interpretation: aggregate coding summaries can be misread as performance evidence unless they are moved to the appendix and labeled as preliminary author-coded diagnostics.

## Final Placement Decision

### Main Text Items

These items should remain in the manuscript because they define the methodological contribution.

| Final Label | Item | Placement | Reviewer Function | Status |
|---|---|---|---|---|
| Figure 1 | Retrieval-Environment Validity Framework | Section III | Identifies the paper's core methodological object | Main text |
| Table 1 | Fixed Information Set Versus Dynamic Retrieval | Section III | Explains why retrieval creates a distinct research-design issue | Main text |
| Table 2 | Five Dimensions of Retrieval-Environment Validity | Section III | Defines the validity framework | Main text |
| Table 3 | Retrieval Typology for LLM-Based Audit Research | Section IV | Distinguishes LLM-only, text, XBRL, and hybrid retrieval | Main text |
| Table 4 | Construct-to-Retrieval Mapping | Section IV | Prevents overclaiming and links retrieval to audit constructs | Main text |
| Table 5 | Claim Correctness Layers | Section V | Operationalizes claim-level evaluation | Main text |
| Table 6 | Tiered Reporting Standard | Section VI | Provides practical methodological guidance | Main text |
| Figure 2 | Demonstration Pipeline | Section VII | Shows source-to-context-to-output-to-claim flow | Main text |
| Table 7 | Selected Claim-Level Demonstration Examples | Section VII | Shows how the framework changes inference | Main text |

### Appendix Items

These items should move to the appendix or online supplement because they are detailed, implementation-heavy, or potentially benchmark-looking.

| Appendix Label | Original Item | Final Placement | Reason |
|---|---|---|---|
| Appendix Table A1 | Retrieval Failure Mode Taxonomy | Appendix F or I | Useful but long; supports coding protocol rather than first-order contribution |
| Appendix Table A2 | Main Preliminary Coding Summary | Appendix F | Could be misread as model-performance results |
| Appendix Table A3 | Bounded Extension Preliminary Coding Summary | Appendix H | Extension evidence, not main empirical result |
| Appendix Table A4 | Reporting Items Mapped to Validity Dimensions | Appendix I | Implementation detail and reporting guidance |
| Appendix Table A5 | Text Retrieval Data Structure | Appendix B | Reproducibility detail |
| Appendix Table A6 | XBRL Relational Retrieval Data Structure | Appendix C | Reproducibility detail |
| Appendix Table A7 | Reproducibility Package Checklist | Appendix I | Supplementary guidance |
| Appendix Table A8 | Bounded Extension Filer Selection | Appendix H | Extension documentation |
| Appendix Table A9 | Bounded Extension Retrieval Diagnostics | Appendix H | Extension documentation |
| Appendix Table A10 | Bounded Extension Selected Examples | Appendix H or G | Extension documentation |

This renumbering keeps the main manuscript clean: seven tables and two figures. That is still table-rich, but defensible for a methodological paper because each main-text table performs a distinct design function.

## Main Text Table Rationales

### Figure 1. Retrieval-Environment Validity Framework

Keep as the first visual because it anchors the paper's novelty. The figure should be simple and conceptual rather than technical. It should not include vector databases, RDF/OWL stores, or implementation details.

Required caption boundary:

> Retrieval-environment validity concerns the correspondence between the audit construct a study intends to examine and the information environment actually supplied to the LLM through retrieval. The framework treats retrieval as part of research design, not as a technical preprocessing step.

### Table 1. Fixed Information Set Versus Dynamic Retrieval

Keep in the framework section. This table is important because it gives reviewers a reason to accept the new construct. It shows why retrieval is not just another prompt-design detail.

Potential reviewer risk:

The table could sound too general if it is not tied to audit constructs. The current "Audit research implication" row handles this sufficiently.

### Table 2. Five Dimensions Of Retrieval-Environment Validity

Keep. This is the core framework table.

Required final check:

Ensure each dimension has an observable artifact:

1. selection -> retrieved chunks/facts/paths;
2. representation -> chunk boundaries and XBRL metadata;
3. stability -> parameters and logs;
4. traceability -> claim-to-source links;
5. separability -> controlled model/prompt/baseline.

### Table 3. Retrieval Typology

Keep. This table distinguishes retrieval designs by source, unit, operator, use, and risk. That distinction is essential because the paper's contribution is not "RAG helps auditing"; it is that retrieval designs construct different research environments.

Required final check:

Preserve the XBRL risk wording:

> Overreading reported structure as audit evidence.

### Table 4. Construct-To-Retrieval Mapping

Keep. This is one of the most AJPT-aligned tables because it gives researchers practical research-design guidance.

Required final check:

The table should continue using "What Not To Claim" as an explicit overclaim-control column.

### Table 5. Claim Correctness Layers

Keep. This is central to the data/variable-construction contribution because it converts LLM outputs into claim-level research variables.

Required final check:

Do not imply that audit-valid correctness is objective ground truth. It is expert-coded judgment when used for stronger claims.

### Table 6. Tiered Reporting Standard

Keep, but renumber from original Table 7 to final Table 6 after moving the failure-mode taxonomy to the appendix.

Reviewer value:

This table maps directly to the AJPT call's interest in research design, variable construction, and best-practice recommendations.

### Figure 2. Demonstration Pipeline

Keep. It supports transparency and reproducibility without requiring readers to parse the appendix first.

Required final check:

The caption must state that the demonstration is methodological and descriptive, not a benchmark.

### Table 7. Selected Claim-Level Demonstration Examples

Keep as the only main-text result table. This table should show the mechanics of the framework, not report means by condition.

Required final edits:

1. Label scores as preliminary author-coded diagnostics in the table note.
2. Use examples to demonstrate evidence-use divergence, source traceability, and boundary conditions.
3. Include at least one integrated hybrid claim, one text-only claim within hybrid, one XBRL-only claim within hybrid, and one LLM-only insufficient-context claim.
4. Avoid interpreting the scores as accuracy rates or evidence of audit performance.

## Tables To Move Out Of Main Text

### Retrieval Failure Mode Taxonomy

Move to appendix. The taxonomy is useful, but putting it in the main manuscript creates table overload. The main text can summarize the failure modes in prose and refer to Appendix F or I.

Main-text replacement sentence:

> Appendix F provides a failure-mode taxonomy linking retrieval omissions, representation errors, attribution failures, relation hallucinations, source overreach, and integration failures to the correctness layers used in the demonstration.

### Preliminary Coding Summary Tables

Move Table 9A and Table 9B to the appendix.

Reason:

The means look like performance metrics even when the notes say otherwise. This is the highest table-related rejection risk.

Required appendix label:

> Preliminary author-coded transparency summaries. These values are not model-performance measures, retrieval-method rankings, or final audit-validity evidence.

Main-text replacement sentence:

> The full preliminary coding summaries are reported in the appendix for transparency. In the main text, we emphasize the claim-level evidence-use pattern rather than comparing average correctness scores across retrieval conditions.

### Reporting Items Mapped To Validity Dimensions

Move to appendix. It is useful for reproducibility, but too detailed for the main manuscript.

Main-text replacement sentence:

> Appendix I maps each reporting item to selection, representation, stability, traceability, and separability validity.

## Final Table Numbering

Use this numbering in the v3 manuscript:

| Final Number | Title |
|---|---|
| Figure 1 | Retrieval-Environment Validity Framework |
| Table 1 | Fixed Information Set Versus Dynamic Retrieval |
| Table 2 | Five Dimensions of Retrieval-Environment Validity |
| Table 3 | Retrieval Typology for LLM-Based Audit Research |
| Table 4 | Construct-to-Retrieval Mapping |
| Table 5 | Claim Correctness Layers |
| Table 6 | Tiered Reporting Standard |
| Figure 2 | Methodological Demonstration Pipeline |
| Table 7 | Selected Claim-Level Demonstration Examples |

Use this appendix numbering:

| Appendix Number | Title |
|---|---|
| Appendix Table A1 | Retrieval Failure Mode Taxonomy |
| Appendix Table A2 | Main Deep-Case Preliminary Coding Summary |
| Appendix Table A3 | Bounded-Extension Preliminary Coding Summary |
| Appendix Table A4 | Reporting Items Mapped to Validity Dimensions |
| Appendix Table A5 | Text Retrieval Data Structure |
| Appendix Table A6 | XBRL Relational Retrieval Data Structure |
| Appendix Table A7 | Reproducibility Package Checklist |
| Appendix Table A8 | Bounded-Extension Filer Selection |
| Appendix Table A9 | Bounded-Extension Retrieval Diagnostics |
| Appendix Table A10 | Bounded-Extension Selected Examples |

## Required Notes And Boundary Language

### Note For Table 7

> Scores are preliminary author-coded diagnostics used to illustrate the claim-level correctness protocol. They are not final expert audit-validity evidence and should not be interpreted as model-performance measures.

### Note For Appendix Tables A2 And A3

> These summaries are preliminary author-coded transparency artifacts. They are included to show how the coding protocol was applied across claims, not to rank retrieval methods, estimate population performance, or validate audit judgment quality.

### Figure 2 Caption Boundary

> The demonstration is a methodological illustration of source-to-context-to-output-to-claim traceability. It is not designed to evaluate model performance, retrieval-method superiority, or population-level failure-mode prevalence.

## Reviewer Stress Test

### Concern 1. Too Many Tables

Reviewer concern:

> The manuscript may feel table-heavy.

Assessment:

Seven tables and two figures are acceptable for a methodology paper if long implementation tables are moved to the appendix. The main-text tables are not redundant: each supports one methodological component.

Mitigation:

Use concise prose before each table explaining what decision the table helps researchers make.

### Concern 2. Aggregate Coding Looks Like Performance Benchmarking

Reviewer concern:

> The coding summaries look like condition-level performance results.

Assessment:

This is the most serious table risk.

Mitigation:

Move coding-summary means to appendix only. In the main text, report the strongest non-performance evidence-use statistic:

> In hybrid conditions, only 7 of 60 claims used both text and XBRL sources, while 41 used text only and 12 used XBRL only.

### Concern 3. Audit Validity Scores Look Too High

Reviewer concern:

> Audit-valid means of 1.00 look implausibly strong and may imply unvalidated audit expertise.

Assessment:

This risk is real if the means appear in the main text.

Mitigation:

Keep audit-valid means in appendix only and explain that they reflect preliminary author coding under prompts that required inferential bridges and limitations. Do not use them as evidence of model audit performance.

### Concern 4. Table 7 Examples Could Be Cherry-Picked

Reviewer concern:

> Selected examples may be anecdotal.

Assessment:

Acceptable if Table 7 explicitly links each example to the full claim-level coding package in Appendix F and selected source checks in Appendix G.

Mitigation:

Add a note:

> Examples are selected from the full 182-claim coding archive and are included to illustrate correctness layers and evidence-use types.

### Concern 5. Figures Are Too Generic

Reviewer concern:

> The figures may look like generic process diagrams.

Assessment:

Figure 1 is conceptual by design. Figure 2 becomes specific because it names SEC filings, Inline XBRL, retrieval conditions, `gemma4:31b`, and claim-level coding.

Mitigation:

Keep Figure 2 tied to the actual two-layer demonstration.

## Table And Figure Accept-Level Checklist

| Requirement | Status | Final Action |
|---|---|---|
| Core conceptual framework visible | Ready | Keep Figure 1 and Table 2 in main text |
| Retrieval designs clearly distinguished | Ready | Keep Table 3 in main text |
| Construct-fit guidance visible | Ready | Keep Table 4 in main text |
| Claim-level coding protocol visible | Ready | Keep Table 5 in main text |
| Reporting guidance visible | Ready | Keep Table 6 in main text |
| Demonstration pipeline visible | Ready | Keep Figure 2 in main text |
| Main-text result table bounded | Ready with edits | Keep only selected examples and add preliminary-coding note |
| Aggregate coding moved out of main text | Required | Move Table 9A/9B to appendix |
| Failure taxonomy moved out of main text | Recommended | Move to appendix to reduce table load |
| Table numbering finalized | Ready | Use final numbering above in v3 |
| Figure captions bounded | Required | Add non-benchmark language |
| Accessibility/alt text | Needed | Add during final manuscript formatting |

## Final Reviewer Assessment

The table and figure strategy is accept-level if the final manuscript follows this placement discipline. The strongest main-text visual sequence is:

1. why dynamic retrieval differs from fixed information sets;
2. what retrieval-environment validity means;
3. how retrieval designs map to audit constructs;
4. how claims are coded;
5. how the demonstration creates source-to-context-to-output-to-claim traceability;
6. how selected claims illustrate evidence-use divergence.

The package will not be accept-level if aggregate coding means are presented as central results. The paper's data-supported empirical statement should remain claim-level evidence-use divergence, not average correctness by retrieval condition.

## Final Decision

**Tables and figures are ready for v3 manuscript integration after the placement changes above.**

The next submission-preparation task should be the reproducibility-materials check, followed by the full v3 manuscript integration.
