# Phase 9 Reviewer Stress Test of Manuscript Draft v1

## Purpose

This memo evaluates `plan/42_phase8_manuscript_draft_v1_with_table_callouts.md` and `plan/43_phase8_appendix_materials_package.md` from the perspective of an AJPT reviewer.

Reviewer question:

> Is the manuscript now strong enough to be viewed as a publishable audit methodology paper, rather than as a promising idea, a technical RAG/XBRL system paper, or an underpowered empirical demonstration?

## Overall Reviewer Verdict

Major revision, but not desk reject if submitted to an AJPT methodology call with careful framing.

The paper has a publishable methodological idea: retrieval is part of research design in LLM-based audit research, and retrieval-created information environments create validity threats that are not addressed by simply reporting the model and prompt. The phrase "retrieval-environment validity" is useful, memorable, and directly tied to audit research design.

However, the manuscript is not yet at an accept-level standard. It still needs sharper theoretical anchoring, stronger reviewer-facing evidence that the framework changes research practice, and tighter handling of the demonstration. The appendix is strong, but the main manuscript risks sounding like a checklist paper unless it more clearly explains what audit researchers would do differently after reading it.

## Recommendation

Conditional revise-and-resubmit.

I would not recommend rejection because the paper identifies a real methodological gap created by retrieval-augmented LLM studies. I would not recommend acceptance because the current draft still relies too heavily on assertion, tables, and preliminary author coding.

## Major Strengths

1. The first page now clearly frames retrieval as research design, not as a technical detail.
2. The paper repeatedly states that XBRL is management-reported structured data, not audit evidence or ground truth.
3. The framework has a clear five-part structure: selection, representation, stability, traceability, and separability.
4. The claim-level correctness protocol is a genuine contribution because it distinguishes text-supported, graph-valid, audit-valid, and integrated correctness.
5. The demonstration uses actual SEC filing and Inline XBRL data rather than synthetic examples.
6. The appendix package substantially improves transparency by preserving source-to-prompt-to-output-to-claim traceability.
7. The paper avoids the most dangerous overclaim: it does not claim that hybrid retrieval is generally superior.

## Major Reviewer Concerns

### Concern 1. The framework may be perceived as renamed construct validity unless its unique retrieval mechanism is sharper.

The draft defines retrieval-environment validity clearly, but reviewers may ask whether this is simply construct validity, measurement validity, and reproducibility under a new label. The paper needs to make the incremental mechanism unmistakable:

> In retrieval-augmented LLM studies, the information set is not only selected by the researcher ex ante; it is dynamically constructed by a retrieval system at runtime.

This mechanism should be repeated and operationalized more forcefully. The manuscript should explain why existing construct validity language is insufficient unless the retrieval-created information environment is separately documented and evaluated.

Required improvement:

Add a short subsection titled "Why Existing Validity Language Is Not Enough" after the definition of retrieval-environment validity. The subsection should explain that retrieval creates a moving treatment/materials boundary, which makes the information environment itself an object of validation.

### Concern 2. The contribution is strong but still reads as too table-driven.

The manuscript has many useful tables, but reviewers may see a sequence of typologies, checklists, and appendices rather than a tightly argued methodology paper. The paper needs a stronger through-line:

1. LLM audit studies require an information environment.
2. Retrieval dynamically creates that environment.
3. Different retrieval designs create different evidence bases.
4. Therefore, output validity depends on retrieval-environment validity.
5. The proposed protocol tells researchers how to diagnose and report that validity.

Required improvement:

Before each major table, add one sentence explaining the inference problem the table solves. After each table, add one sentence explaining how it changes research design or reviewer evaluation.

### Concern 3. The demonstration is useful but not yet strong enough to carry evidentiary weight.

The demonstration is correctly framed as descriptive, but it still risks being read as empirical evidence because it reports outputs, claims, and means. The preliminary coding summary is especially risky because audit-validity means of 1.00 look implausibly strong without expert coding.

Required improvement:

Move Table 9 to the appendix unless expert coding is completed. In the main text, use the five selected examples to demonstrate inference shifts and explicitly say that the aggregate coding table is a transparency artifact, not a performance result.

### Concern 4. Audit-valid correctness needs stronger safeguards.

The draft says audit-valid correctness requires professional judgment, but the current coding is preliminary author coding. This is acceptable for a methodology demonstration only if the manuscript states exactly what would be required before audit-valid scores could support empirical claims.

Required improvement:

Add an "Expert Coding Requirement" paragraph in Section 5 or Section 7:

- audit-valid and integrated scores require audit-domain coders;
- coders should be independent of prompt construction where feasible;
- disagreement should be reconciled or reported;
- reliability should be reported for empirical studies;
- author coding in this paper is illustrative.

### Concern 5. The paper must better explain what an audit researcher would do differently after reading it.

The acceptance criterion in the project plan is excellent, but the manuscript should answer it explicitly. Right now, the answer is spread across the introduction, reporting section, and appendix.

Required improvement:

Add a short section or boxed paragraph titled "Implications for LLM-Based Audit Research Design." It should state:

1. define the audit construct before retrieval;
2. choose retrieval operators that match the construct;
3. log what the model saw;
4. code claims by correctness layer;
5. distinguish reported XBRL relations from audit evidence;
6. report retrieval sensitivity proportional to the study's claims.

### Concern 6. Literature positioning is directionally right but too compressed.

The related literature section identifies the correct streams, but it still reads as a high-level map. Reviewers will expect sharper contrasts with XBRL research, textual analysis, LLM accounting, and audit analytics.

Required improvement:

Add a literature positioning table in the main text or appendix with columns:

| Literature Stream | What It Studies | Methodological Limitation for LLM Retrieval Studies | This Paper's Increment |

The key phrase should be:

> Prior research studies data and models; this paper studies the retrieval-created information environment that mediates between data and model output.

### Concern 7. The current demonstration does not implement vector retrieval or RDF/OWL retrieval.

The draft now handles this reasonably well, but the title and abstract still use "XBRL-Augmented Retrieval" and the larger project history includes ontology/RDF language. A reviewer may expect an ontology database or GraphRAG implementation.

Required improvement:

Add an explicit boundary sentence in the abstract or introduction:

> Our demonstration uses an inspectable keyword/text and table-based XBRL relational prototype; vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions that require additional reporting rather than as performance claims in this study.

### Concern 8. The paper needs a clearer target-journal fit statement.

AJPT methodology calls favor papers that guide future researchers and reviewers. The draft implies this, but it should say more directly how the paper helps reviewers evaluate future LLM audit studies.

Required improvement:

In the introduction, add one sentence:

> For reviewers, the framework provides criteria for evaluating whether an LLM audit study's retrieval environment supports the claimed audit construct.

## Desk-Reject Risk Assessment

| Risk | Current Level | Why | Mitigation |
|---|---|---|---|
| Sounds like a technical systems paper | Moderate | RAG, XBRL, RDF/OWL, prompts, and model details can distract from methodology | Keep technical details in appendix and tie every implementation item to validity |
| Sounds like a checklist paper | Moderate | Many tables/checklists may feel procedural rather than conceptual | Strengthen the central mechanism and use tables as operationalizations |
| Overclaims demonstration | Moderate | Claim means and audit-validity scores may look like performance evidence | Move aggregate coding to appendix and foreground selected inference-shift examples |
| Weak audit grounding | Low to moderate | Audit evidence boundaries are stated well, but expert coding remains missing | Add expert-coding safeguards and audit assertion boundary language |
| Insufficient novelty | Moderate | Reviewers may see construct validity plus RAG transparency | Explain dynamic retrieval as a distinct treatment/materials boundary problem |
| Insufficient literature integration | Moderate | Related literature is correct but compressed | Add sharper comparison table and cite each stream in the argument |

## Accept-Level Test

### Question 1. Is the contribution sufficiently novel?

Potentially yes.

The novelty is not "XBRL plus LLM" or "RAG for audit." The novelty is:

> Retrieval-created information environments are part of research design, and audit researchers need a validity framework for evaluating whether those environments support claimed inferences from LLM outputs.

This is a publishable methodological contribution if the paper makes the dynamic retrieval mechanism central and distinguishes itself from generic construct validity guidance.

### Question 2. Is the paper sufficiently audit-specific?

Almost.

The strongest audit-specific elements are:

1. audit construct alignment;
2. XBRL as reported accounting structure but not audit evidence;
3. audit-valid correctness as professional judgment;
4. traceability and documentation;
5. assertion/risk cue boundaries.

The remaining weakness is that audit-valid correctness is not yet supported by expert coding. This does not block a methodology paper, but the paper must not let preliminary author scores look like audit evidence.

### Question 3. Does the demonstration change inference?

Yes, but this needs to be stated more crisply.

The most important demonstration finding is not that hybrid retrieval performs better. It is that condition labels do not reveal claim-level evidence use. A hybrid response can contain integrated, text-only, XBRL-only, or insufficiently supported claims. Therefore, evaluating at the response or condition level can produce invalid inferences about LLM audit reasoning.

This should be the demonstration's headline.

### Question 4. Would an audit researcher do something differently after reading the paper?

Yes, if the manuscript states the answer explicitly.

The researcher would:

1. define the audit construct before choosing retrieval;
2. choose text, XBRL, or hybrid retrieval based on construct fit;
3. log retrieved evidence, not just prompts and model settings;
4. evaluate claims by correctness layer;
5. avoid treating XBRL as audit evidence;
6. report enough retrieval detail for reviewers to inspect selection, representation, stability, traceability, and separability.

## Reviewer Recommendation Letter, Condensed

This manuscript addresses an important and timely methodological issue for audit research. As LLM-based audit studies increasingly rely on retrieval, researchers and reviewers need criteria for evaluating whether the retrieved information environment supports the audit construct being studied. The manuscript's central concept of retrieval-environment validity is promising and audit-relevant. The claim-level correctness protocol is especially useful because it distinguishes text-supported, graph-valid, audit-valid, and integrated claims.

However, I would require major revisions before publication. The manuscript should more clearly distinguish retrieval-environment validity from existing construct validity language, reduce the risk that tables and checklists overwhelm the central argument, and better bound the preliminary demonstration. The current author-coded audit-validity results should be treated as illustrative only. The paper would be substantially stronger if it moved aggregate preliminary coding to the appendix, added explicit expert-coding requirements, and sharpened the claim that retrieval condition labels do not reveal claim-level evidence use.

## Required Revision Priorities

1. Add a subsection explaining why existing validity concepts are insufficient without retrieval-environment validation.
2. Add a concise "what audit researchers should do differently" box or subsection.
3. Move aggregate preliminary coding results to the appendix unless expert coding is completed.
4. Add expert-coding and reliability safeguards for audit-valid and integrated correctness.
5. Add a literature-positioning table that contrasts this paper with XBRL, textual analysis, LLM accounting, and audit analytics research.
6. Add an explicit boundary statement that the current prototype is keyword/table-based and not a vector-RAG or RDF/OWL performance study.
7. Tighten the demonstration headline around claim-level evidence-use divergence, especially within hybrid retrieval.

## Final Assessment

The manuscript is now strong enough to justify continued development toward AJPT submission. It is not yet accept-ready, but it has crossed the threshold from "interesting idea" to "credible methodology paper under revision." The next step should be to implement the required revisions in a v2 draft rather than adding more conceptual material.
