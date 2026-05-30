# Phase 7 Reviewer Stress Test

## Purpose

This memo evaluates the Phase 7 reproducibility and reporting materials from the perspective of an AJPT reviewer.

Reviewer question:

> Do the implementation specifications and reporting checklist strengthen the paper's methodology contribution, or do they make the paper look like a technical systems appendix?

## Overall Verdict

Conditional favorable.

The Phase 7 materials substantially improve the paper's credibility because they make retrieval-created information environments observable and reproducible. They answer a predictable reviewer concern: if retrieval design matters, future researchers need to know exactly what to disclose about chunks, embeddings, XBRL facts, relation paths, prompts, model settings, and coding.

However, the materials must be framed carefully. If the manuscript presents these specifications as a technical contribution in their own right, reviewers may see the paper as drifting away from AJPT methodology. If the manuscript presents them as operational tools for retrieval-environment validity, they strengthen the paper.

## Strengths

1. The materials distinguish text retrieval and XBRL relation retrieval by data structure and retrieval operator, not merely by prompt wording.
2. The current demonstration is described accurately as keyword-ranked contextual retrieval and table-based XBRL relational retrieval.
3. The RDF/OWL material is framed as a compatibility and portability layer, not as a claim that a full ontology database has already been implemented.
4. The reporting checklist makes retrieval design inspectable at the level of source data, retrieval units, parameters, prompt rendering, outputs, and claim coding.
5. The sensitivity table separates text retrieval parameters from XBRL relation retrieval parameters.
6. The hybrid retrieval workflow directly addresses the separability risk that hybrid contexts may improve outputs simply by providing more information.

## Major Reviewer Concerns

### Concern 1: The checklist may look like generic reproducibility guidance.

Risk:

An AJPT reviewer may ask why this belongs in an audit methodology paper rather than a technical appendix.

Required improvement:

Tie each checklist item to a retrieval-environment validity dimension. The reporting materials should be positioned as the operationalization of selection, representation, stability, traceability, and separability.

Action taken:

Added a "Mapping to Retrieval-Environment Validity" section to `plan/34_phase7_reporting_checklist_and_sensitivity_table.md`.

### Concern 2: The paper may appear to claim vector RAG while the demonstration uses keyword-ranked retrieval.

Risk:

If the manuscript says "RAG" too broadly, reviewers may expect embedding-based retrieval and object that the demonstration does not implement a vector database.

Required improvement:

Distinguish a minimum inspectable prototype from an embedding-based RAG implementation.

Action taken:

Added a "Minimum Versus Extended Implementation" section to `plan/31_phase7_text_retrieval_specification.md`.

### Concern 3: The ontology language may imply a stronger technical implementation than exists.

Risk:

RDF/OWL discussion can sound like a full ontology database contribution. That would create a mismatch with the actual Phase 6 prototype and distract from the methodology contribution.

Required improvement:

Separate table-based relational retrieval, RDF/OWL-compatible mapping, and graph database implementation.

Action taken:

Added a "Minimum Versus Extended Implementation" section to `plan/32_phase7_xbrl_relation_ontology_specification.md`.

### Concern 4: XBRL-to-audit assertion links may appear to be objective rather than researcher-coded.

Risk:

An audit reviewer may object if ontology links appear to convert XBRL relations into audit assertions.

Required improvement:

Clearly distinguish XBRL-coded relations from researcher-coded construct/assertion mappings.

Action taken:

Added a "Researcher-Coded Versus XBRL-Coded Relations" section to `plan/32_phase7_xbrl_relation_ontology_specification.md`.

### Concern 5: The checklist may ask too much of future researchers.

Risk:

A very long checklist can feel impractical and reduce the paper's usefulness.

Required improvement:

Present reporting expectations as tiered rather than universal.

Action taken:

Added a "Tiered Reporting Standard" section to `plan/34_phase7_reporting_checklist_and_sensitivity_table.md`.

## Reviewer-Ready Positioning

Recommended manuscript framing:

> The reporting checklist is not a generic replication appendix. It operationalizes retrieval-environment validity. Each item corresponds to a threat created by dynamic retrieval: selection, representation, stability, traceability, or separability. The level of required disclosure should scale with the study's claims. Our demonstration is a Tier 1 methodological demonstration; studies claiming embedding-based RAG effects or GraphRAG performance require additional disclosures.

## Remaining Weaknesses

1. The current demonstration still lacks actual embedding-based vector retrieval. This is acceptable only if the paper avoids claiming vector-RAG performance.
2. The current XBRL relation store is table-based. This is acceptable only if RDF/OWL is described as a mapping/specification rather than an implemented database.
3. The sensitivity checks are proposed guidance rather than fully executed checks. The demonstration should not imply that all sensitivity checks were performed.
4. Expert review and inter-rater reliability remain needed before audit-valid and integrated correctness can be treated as final evidence.

## Accept-Level Assessment

At this point, the Phase 7 materials are strong enough to support an AJPT methodology submission if the manuscript uses them correctly.

The strongest version of the contribution is:

> This paper does not propose another RAG system. It provides a validity framework and reporting protocol for studies in which retrieval systems create the information environment observed by LLMs. The text and XBRL specifications show how to disclose the retrieval environment well enough for reviewers to evaluate whether conclusions about LLM audit outputs are warranted.

This is publication-relevant because it tells audit researchers what they must report and validate before drawing conclusions from LLM-RAG audit studies.

## Next Development Step

The next manuscript-development step should be Phase 8: begin drafting the manuscript sections. The Phase 7 materials should be used as source material for:

1. the methodological guidance section;
2. the demonstration section;
3. the appendix reporting checklist;
4. the limitations and boundary conditions section.

