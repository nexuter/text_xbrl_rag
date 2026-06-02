# Second-Revision Reviewer Response Evidence Crosswalk

Date: 2026-06-01

## Purpose

This crosswalk consolidates the second-revision work into a reviewer-facing evidence map. It is intended to support the response letter and final pre-submission QA by linking each major reviewer concern to:

- revisions made;
- evidence added;
- claims narrowed;
- manuscript or supplement location;
- residual boundary preserved.

## Summary Assessment

The second revision now addresses the central reviewer concern: the paper no longer rests on a descriptive three-case idea or an under-validated XBRL/LLM claim. It is framed as a nine-filer, 72-output, 281-claim protocol-validation package with independent coding evidence, XBRL construct-coverage diagnostics, retrieval-stage perturbation diagnostics, claim-evidence calibration, and explicitly bounded audit-inference language.

The follow-up audit of Major Comments 1-5 and the Minor Comments confirms that the manuscript now makes a disciplined Tier 1 methodology claim. The response letter must preserve this discipline: the paper validates a retrieval-environment protocol and central source-use/integration measures, not model performance, retrieval superiority, audit evidence sufficiency, or general hybrid-retrieval behavior.

The remaining unresolved issue is not a substantive reviewer concern. It is submission metadata: author-specific title-page and cover-letter fields must be completed before DOCX regeneration and upload.

## Evidence Crosswalk

| Reviewer Concern | Revision Made | New Evidence / Artifact | Claim Narrowed? | Location | Residual Boundary |
|---|---|---|---|---|---|
| Incremental contribution unclear relative to construct validity, documentation, RAG evaluation, and XBRL data-quality research | Repositioned retrieval-environment validity as a retrieval-specific diagnostic for construct drift in dynamic information environments | Adjacent-validity comparison; reviewer decision-rule table; added RAGAS, ARES, attribution, and citation-generation positioning | Yes. The paper does not claim to replace construct validity, RAG evaluation, or XBRL data-quality research | Manuscript Sections II-III; Tables 2-3; plan/120; plan/138-139 | Retrieval-environment validity is an audit-methodological lens, not a universal validity theory |
| Demonstration too bounded or descriptive | Reframed demonstration as full-scale nine-filer protocol validation with distinct evidence layers | 72 retrieval-conditioned outputs; 281 preliminary coded claims; 120-claim independent coding sample; main cases plus six-filer extension | Yes. Counts are design-specific diagnostics, not population frequencies | Manuscript Section VII; Appendix H; plan/128-129 | No model-performance, prevalence, or retrieval-superiority inference |
| Audit constructs underspecified | Added ex ante construct protocols for revenue recognition risk and inventory valuation assertion | Appendix Tables A2/A3; Table 6 construct-to-retrieval mapping; PCAOB audit evidence/risk anchors | Yes. Public filing/XBRL support is separated from audit evidence sufficiency | Manuscript Sections IV-V; Appendix A; Tables 6-7; plan/121 | No claim that retrieved public filings prove misstatement, fraud, reserve adequacy, or audit truth |
| XBRL relational retrieval under-validated | Added XBRL construct-family coverage diagnostic and worked examples | XBRL coverage script/output; Appendix C2/C3; NKE inventory source-to-claim trace; period/dimension representation-risk example | Yes. XBRL is management-reported structured data, not audit evidence | Manuscript Sections IV and VII; Appendix C; plan/122-123 | No implemented RDF/OWL graph database or GraphRAG benchmark claim |
| Coding independence incomplete | Expanded independent coder process documentation and clarified coding scope | 120-claim validation sample; coder process documentation; reliability results; integrated-code rule cleanup | Yes. Independent coding supports source-use and integration reliability, not audit-domain expert validation | Manuscript Section VII; Appendix F4-F5; coder docs; plan/124 | Audit-boundary diagnostics remain qualitative unless expert reviewed |
| Audit-boundary validation may be overstated | Adopted Gate A claim-narrowing path rather than claiming audit-domain validation | Gate A decision memo; Appendix F4B; legacy-column interpretation note | Yes. Removed audit-valid performance framing; retained preliminary audit-boundary diagnostics | Manuscript Sections V, VII, VIII; Appendix F; README notes; plan/125-126 | Strong audit-judgment claims require audit-domain expert review |
| Separability and stability concerns | Added retrieval-stage context-volume and source-environment perturbation diagnostics | Context-volume diagnostics; top-3/top-8 text perturbations; XBRL fact-only and reduced-budget variants; bounded sensitivity decision matrix | Yes. Diagnostics are retrieval-stage transparency, not output-level robustness | Manuscript Section VII; Appendix I1-I3; data/processed/sensitivity; plan/127 | No matched-budget output rerun, prompt sensitivity, cross-model robustness, or model-performance validation |
| Overgeneralization risk | Rewrote counts and demonstration language as design-specific protocol diagnostics | Appendix H evidence-layer map; design-specific hybrid source-use counts; extension framed as maximum-variation methodological check | Yes. No prevalence or population inference | Manuscript Section VII; Appendix H; plan/128-129 | Purposive sample, not representative SEC-filer sample |
| Audit-specific fit needs strengthening | Added intended audit-research use cases and same-evidence audit-boundary example | Audit use-case paragraph; Appendix F1B same-evidence table; audit evidence hierarchy | Yes. Framework supports LLM-based audit research methodology, not audit-practice automation | Manuscript Introduction, Sections V and VIII; Appendix F; plan/130-131 | No audit procedure, engagement workflow, or decision aid proposed |
| Manuscript reads too caveat-heavy | Rewrote abstract/intro to foreground practical decision rule and positive methodological result | Early retrieval mechanics and claim-layer examples; discussion reframed around design implications | Yes. Boundaries preserved but moved into claim-calibration logic | Abstract, Introduction, Discussion; plan/132-133 | Boundaries remain explicit where inferentially necessary |
| Replication package and metadata need synchronization | Refreshed replication README, authoritative file map, reviewer file map, checksums, and pipeline documentation | Updated processed-only replication package docs; package checksum manifest; REVIEWER_FILE_MAP | No substantive claim expansion | README_REPLICATION; replication_package docs; plan/134-135 | Raw SEC archive remains excluded by default and reconstructable from public SEC sources |
| Citation status and terminology cleanup | Updated title/terminology and citation status | Title revised to `XBRL Relational Retrieval`; RAGAS and ARES proceedings records; added Rashkin/Gao attribution literature | Yes. Removed wording that could imply broader XBRL-augmented architecture or audit-valid performance | Manuscript title, Section II, references, submission docs; plan/136-139 | XBRL relational retrieval is table-based fact/path retrieval in this implementation |
| Retrieval mechanics insufficiently concrete | Added reader-facing mechanics example and supplement mechanics notes | Section IV mechanics example; Appendix B/C notes; links to Appendix I perturbations | No claim expansion | Manuscript Section IV; Appendix B/C/I; plan/140-141 | Chunk-size, overlap, traversal-depth, and GraphRAG sensitivity remain future Tier 2/3 requirements |
| Table package feels like a checklist | Reframed reporting section around evidence tiers and shortened appendix table listings | Table 8 renamed; Section VI organized around source inventory, retrieval recipe, output linkage; appendix summary shortened | No claim expansion | Manuscript Section VI and Appendix summary; Tables file; plan/142-143 | Detailed field-level schemas remain in the supplement for reproducibility |
| Submission package still has author placeholders | Audited and classified remaining placeholders | Author checklist updated; placeholder audit log created | Not applicable | Title page, cover letter, Author_Information_Checklist; plan/144-145 | Author metadata must be completed before DOCX regeneration |
| Major Comment 1 follow-up: contribution may still sound like relabeled construct validity | Added direct positioning as an audit-specific organizing framework for retrieval-related construct drift | Major-comment audit memo; Table 2/3 positioning; Section III language | Yes. Avoids claiming a new universal validity category | Manuscript Introduction and Section III; Tables 2-3; plan/147 | Treat as reviewer decision rule / diagnostic lens grounded in construct validity |
| Major Comment 2 follow-up: demonstration may still be too weak for validation language | Chose the conceptual/methodological Tier 1 path and toned down model-validation claims | Tier 1 transparency language; non-claim list; Appendix I Tier 2 requirements | Yes. Demonstration validates protocol inspectability, not output robustness | Manuscript Sections VII-VIII; Appendix I; plan/148 | No matched-budget reruns, prompt-order sensitivity, output-level perturbation reruns, or multi-model test |
| Major Comment 3 follow-up: coding evidence may remain author-dependent | Added disagreement-pattern reporting and separated audit-boundary notes from expert audit-valid labels | 120-claim independent coding; 22 variable-level disagreement summary; no source-use/integration disagreements | Yes. Independent coding supports source-use/integration reliability, not audit-valid correctness | Manuscript Section VII; Appendix F4-F5; plan/149 | No independent audit-domain expert validation of audit-boundary judgments |
| Major Comment 4 follow-up: 8/89 hybrid count may look generalizable | Added explicit design-specific and non-generalization language | Wording: "within this design," "in this implementation," "not ... hybrid retrieval generally behaves this way" | Yes. Count is mechanism diagnostic, not rate estimate | Manuscript Abstract, Introduction, Section VII; Appendix H; plan/150 | No population frequency, model-performance, or general hybrid behavior inference |
| Major Comment 5 follow-up: audit positioning may exceed public filing data | Added task-success criteria and public-reporting audit-research boundary | Revenue/inventory task-success criteria; engagement-like extension guidance | Yes. Demonstration is assertion-relevant public-reporting reasoning, not audit-valid engagement reasoning | Manuscript Section IV and VIII; Appendix A; Table 6; plan/151 | No audit-practice evidence environment or audit-judgment validation |
| Minor Comments follow-up | Added compact early correctness-layer example and documented coverage | Figure 1A; minor-comment coverage audit | No claim expansion | Manuscript Introduction; Tables/Figures; plan/152 | Boundary repetition remains partly deliberate to prevent overclaiming |

## Response Letter Structure Recommended

The response letter should be organized around the following themes rather than only reviewer-by-reviewer line items:

1. Calibrating manuscript claims to their evidence level.
2. Sharpening retrieval-environment validity as the distinct contribution.
3. Specifying audit constructs and preserving audit evidence boundaries.
4. Validating XBRL relational retrieval as a source environment.
5. Strengthening coding independence and measurement credibility.
6. Adding bounded separability and source-environment sensitivity diagnostics.
7. Reframing the demonstration as nine-filer protocol validation.
8. Strengthening audit-specific relevance and AJPT fit.
9. Improving replication transparency and submission-package consistency.
10. Cleaning literature, terminology, title, and presentation.

## Claims To Preserve In The Response Letter

- The paper is a methodology paper, not a model-performance benchmark.
- The contribution is retrieval-environment validity as a research-design and variable-construction framework.
- The evidence package validates a protocol, not an LLM model or retrieval method.
- XBRL is management-reported structured data, not audit evidence or ground truth.
- Independent coding supports reliability of source-use and integration variables, not expert audit-boundary validity.
- Bounded sensitivity diagnostics support retrieval-stage transparency, not output-level robustness.
- The six-filer extension supports protocol applicability across varied reporting environments, not population inference.

## Remaining Pre-Submission Tasks

1. Insert final author information and disclosures.
2. Regenerate DOCX files after author metadata is final.
3. Run final DOCX structural QA.
4. Rebuild submission zips if any package contents change.
5. Conduct final placeholder search excluding manuscript table/figure callouts.
6. Draft final response letter using `plan/153_second_revision_response_letter_master_outline.md`.
