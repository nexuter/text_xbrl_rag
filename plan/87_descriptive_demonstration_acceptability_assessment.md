# Descriptive Demonstration Acceptability Assessment

## Purpose

This memo evaluates whether the current manuscript can plausibly receive a favorable AJPT review while relying on a descriptive methodological demonstration rather than a hypothesis-testing model-performance study. The analysis is based on precedents from AJPT methodological and research-needs papers, not on guesswork.

## Bottom-Line Judgment

The current descriptive demonstration can be acceptable for AJPT **only if the manuscript is framed and revised as a research-methodology paper whose evidence tests the usability of a method, not the performance of a model**.

However, the current Section VIII limitation language is too defensive. It risks inviting the reviewer to conclude that the paper is "a good idea not yet validated." The paper should instead state a positive evidentiary standard:

> The demonstration is not designed to test model performance because model performance is not the paper's construct. The demonstration tests whether retrieval-environment validity can be operationalized, logged, inspected, and used to change the interpretation of LLM audit-research outputs.

The paper should therefore be revised from "descriptive demonstration" language toward **methodological stress test / protocol validation demonstration** language.

## AJPT Precedent

### 1. Power and Gendron (2015)

**Paper:** "Qualitative Research in Auditing: A Methodological Roadmap," *Auditing: A Journal of Practice & Theory* 34(2): 147-165.

**What AJPT accepted:** A roadmap/commentary that legitimizes and clarifies qualitative auditing research. It is not a hypothesis-testing empirical paper.

**Relevant lesson:** AJPT can accept methodology papers that primarily provide a conceptual roadmap when the paper addresses a real reviewer/evaluator problem and provides criteria for judging quality.

**Implication for our paper:** We do not need to prove that XBRL-augmented retrieval improves LLM audit performance. We do need to prove that retrieval-environment validity helps reviewers evaluate LLM-based auditing studies.

### 2. Malsch and Salterio (2016)

**Paper:** "'Doing Good Field Research': Assessing the Quality of Audit Field Research," *Auditing: A Journal of Practice & Theory* 35(1): 1-22.

**What AJPT accepted:** The paper's stated goal is to provide editors and reviewers with suggestions/guidelines for assessing the quality of audit field research. It poses and answers ten quality questions and illustrates the responses with best practices from published or forthcoming papers.

**Relevant lesson:** AJPT accepts methodology papers that help reviewers evaluate research quality, even when the paper does not run a new empirical test. But the guidance must be operational enough to be used in review.

**Implication for our paper:** Retrieval-environment validity should be presented as reviewer-usable quality criteria. The demonstration should show that the criteria can be applied to real artifacts: retrieved contexts, source IDs, claims, and evidence-use labels.

### 3. Griffith, Kadous, and Young (2016)

**Paper:** "How Insights from the 'New' JDM Research Can Improve Auditor Judgment: Fundamental Research Questions and Methodological Advice," *Auditing: A Journal of Practice & Theory* 35(2): 1-22.

**What AJPT accepted:** The paper translates established JDM frameworks into audit research questions and methodological advice. It outlines ideas, develops high-level audit research questions, and provides guidance for designing and evaluating experiments.

**Relevant lesson:** A methodology contribution can be grounded in theory translation and design guidance rather than original performance evidence.

**Implication for our paper:** Our analogous move is to translate construct validity, audit documentation, source traceability, and separability concerns into retrieval-specific design criteria for LLM audit studies.

### 4. Hatfield and Saiewitz (2022)

**Paper:** "Theoretical and Practical Guidance for Incorporating Auditor-Client Communication in Experimental Research," *Auditing: A Journal of Practice & Theory* 41(4): 163-177.

**What AJPT accepted:** The paper provides theoretical and practical guidance for experimental design choices, compares design options from non-interactive highly controlled studies to participant interaction, and discusses best practices and pitfalls.

**Relevant lesson:** AJPT values papers that map design options to theoretical constructs and warn researchers about design-choice consequences. This paper later received AJPT Best Paper recognition, which is strong evidence that guidance-oriented methodology papers can be valued highly.

**Implication for our paper:** The retrieval typology and construct-to-retrieval mapping are central. The demonstration should make design-choice consequences visible, not compete with empirical RAG benchmarks.

### 5. Appelbaum, Kogan, and Vasarhelyi (2017)

**Paper:** "Big Data and Analytics in the Modern Audit Engagement: Research Needs," *Auditing: A Journal of Practice & Theory* 36(4): 1-27.

**What AJPT accepted:** A research-needs paper that positions Big Data and analytics against audit evidence and analytical-procedure standards, then proposes key research questions and measurement/reporting needs.

**Relevant lesson:** AJPT accepts forward-looking methods papers when they synthesize an emerging technology, connect it to audit evidence/research design, and identify what future research must measure and report.

**Implication for our paper:** The manuscript should explicitly say that its contribution is not a completed technology evaluation but the measurement/reporting standard future LLM-RAG audit studies need.

### 6. Hoitash, Hoitash, and Morris (2021)

**Paper:** "eXtensible Business Reporting Language (XBRL): A Review and Implications for Future Research," *Auditing: A Journal of Practice & Theory* 40(2): 107-132.

**What AJPT accepted:** A review and future-research paper explaining the richness of XBRL data, reviewing XBRL literature, discussing tagging/data-quality issues, and identifying future research topics.

**Relevant lesson:** AJPT is receptive to structured-reporting methodology and future-research guidance when the paper clarifies data richness, limitations, and appropriate uses.

**Implication for our paper:** XBRL should remain framed as a retrieval environment and research-data structure, not as audit evidence. This is aligned with the current manuscript, but the demonstration should more clearly validate the method's ability to expose XBRL-specific relation evidence.

## Reviewer Risk Assessment

### Risk 1: "This is a good idea, but the data do not validate it."

This is the most serious risk. The current Section VIII wording reinforces the risk by saying the demonstration is descriptive and does not test a hypothesis.

**Response:** Replace the defensive limitation with a positive methodological validation claim. The paper validates the *protocol*, not the *model*.

Minimum revised claim:

> The demonstration validates three properties of the method: retrieval environments can be logged and reconstructed; LLM outputs can be decomposed into source-traceable claims; and response-level retrieval-condition labels can mask materially different claim-level evidence use.

### Risk 2: "AJPT methodology papers still need evidence."

The precedent papers often do not test new hypotheses, but they provide operational guidance, examples, quality criteria, or literature-based synthesis. Therefore, our paper cannot rely only on conceptual novelty.

**Response:** Strengthen the demonstration as an implementation proof, not a performance test:

1. Report the number of retrieved contexts, outputs, claims, source references, and invalid source references.
2. Emphasize no invalid source references in validation.
3. Report the hybrid evidence-use divergence: 7 of 60 hybrid claims used both text and XBRL, 41 used text only, and 12 used XBRL only.
4. Use the six-filer extension as maximum-variation protocol stress testing, not robustness of model performance.

### Risk 3: "Why not add expert coding?"

This is a fair reviewer concern. The current paper can survive without full expert coding only if audit-valid and integrated scores remain preliminary diagnostics. But a small expert calibration would materially improve credibility.

**Recommended direction:** Add a limited audit-domain expert calibration if feasible:

- Sample: 24 to 36 claims, stratified by retrieval condition and evidence-use type.
- Task: Ask one or two audit-domain experts to judge whether each claim overstates audit inference relative to the supplied evidence.
- Output: Do not use this as a performance benchmark. Use it as a calibration check that the coding protocol is interpretable to audit-domain reviewers.
- Report: Agreement rate and examples of disagreement, not broad accuracy statistics.

This would align with AJPT precedents because it strengthens reviewer evaluability without turning the paper into a model-performance study.

### Risk 4: "Why not test sensitivity?"

A full RAG benchmark would move the paper away from its methodological contribution. But a small retrieval-environment sensitivity audit would directly support the paper's own construct.

**Recommended direction:** Add a bounded sensitivity appendix:

- Vary text top-k for a small subset of filer-construct tasks.
- Vary XBRL relation traversal depth or relation filter for a small subset.
- Keep the model/prompt fixed.
- Report whether retrieved evidence units and evidence-use labels change.

This is not needed to rank retrieval methods. It supports stability and separability dimensions.

## Decision Framework

### Current package without further changes

Likely reviewer outcome: **Major revision**, not clean accept.

Reason: The idea is strong and aligned with the AJPT call, but Section VIII may make the paper look under-validated.

### Current package with reframing only

Likely reviewer outcome: **More credible major revision / possible revise-and-resubmit**.

Reason: Stronger framing can clarify that the correct evidentiary target is protocol validation rather than model performance.

### Current package with reframing plus bounded sensitivity audit

Likely reviewer outcome: **Credible R&R with accept-level potential**.

Reason: This directly addresses whether retrieval-environment validity can be observed and stress-tested across design choices.

### Current package with reframing plus bounded sensitivity audit plus limited expert calibration

Likely reviewer outcome: **Strongest submission posture**.

Reason: This best matches AJPT methodology precedents: theory-grounded guidance, operational criteria, concrete examples, reviewer-facing quality checks, and bounded evidence that the protocol is usable by domain experts.

## Recommended Direction

Revise the manuscript in three moves:

1. **Reframe Section VIII.**
   Replace "The current demonstration is descriptive" with "The demonstration is a methodological protocol validation, not a model-performance hypothesis test."

2. **Add a short "Methodological Validation Evidence" subsection to Section VII.**
   State exactly what the demonstration validates:
   - 42 retrieval-conditioned outputs were generated.
   - 182 claims were coded.
   - Source traceability was validated with no invalid source references.
   - Hybrid labels did not imply integrated evidence use: only 7 of 60 hybrid claims used both text and XBRL.
   - The six-filer extension showed the protocol can be applied across varied reporting environments and reveals boundary cases.

3. **Add one bounded additional validation layer before submission if feasible.**
   Preferred: bounded retrieval sensitivity audit.
   Stronger: bounded retrieval sensitivity audit plus limited expert calibration.

## Proposed Manuscript Language

Replace the current Section VIII limitation paragraph with:

> The demonstration is a methodological protocol validation rather than a model-performance hypothesis test. This distinction is central to the paper's contribution. The relevant question is not whether one retrieval design produces higher-quality audit judgments, but whether retrieval-created information environments can be specified, logged, inspected, and linked to claim-level evidence use. The demonstration validates those properties by preserving source-to-context-to-output-to-claim traces across text, XBRL, hybrid, and no-context conditions. Stronger empirical studies that estimate model performance, retrieval superiority, or audit-judgment quality should add fuller sensitivity checks, expert coding, reliability evidence, and stronger controls over token budget and retrieval variation.

Add after the Section VII claim-level results:

> The demonstration provides methodological validation evidence on the protocol itself. First, the source-to-context-to-output-to-claim chain is observable: the replication package preserves retrieved chunks, XBRL facts, relation paths, prompts, raw outputs, claim coding, and source identifiers. Second, the protocol detects inference-relevant differences that would be hidden by response-level labels. In hybrid conditions, only 7 of 60 claims used both text and XBRL sources, while 41 used text only and 12 used XBRL only. Third, source traceability can be inspected: validation identified no invalid source references in the coded output set. Fourth, the bounded six-filer extension shows that the protocol can be applied across varied reporting environments while also revealing boundary cases, such as relation-path scarcity for Microsoft revenue and high XBRL relation complexity for Caterpillar inventory.

## Final Assessment

AJPT precedents support the possibility of publishing a methodology paper without a full hypothesis-testing empirical design. But the manuscript should not sound like it is apologizing for being descriptive. It should argue that the demonstration is descriptive **because descriptive protocol validation is the right evidence for this contribution**.

The highest-return revision is not to turn the paper into a model-performance study. It is to make the demonstration look like a reviewer-usable validation of the proposed methodology.
