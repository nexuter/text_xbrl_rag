# Claim-Evidence Calibration Register

## Purpose

This register implements `SR-00` from `plan/112_second_revision_comprehensive_revise_plan.md`.

It classifies the major claims in the current manuscript by the evidence level that can support them. The goal is to prevent the second revision from asking bounded protocol-validation evidence to carry broader claims about model performance, audit evidence sufficiency, retrieval-method superiority, or population-level prevalence.

## Evidence-Level Definitions

| Evidence Level | Definition | Appropriate Claim Type |
|---|---|---|
| Conceptual | Supported by theory, literature positioning, and methodological logic | Definitions, frameworks, reviewer decision rules, design guidance |
| Protocol-validation | Supported by implemented artifacts, logs, preserved prompts, source IDs, outputs, and reproducibility materials | The protocol can be implemented, inspected, reconstructed, and linked from source to claim |
| Measurement-validation | Supported by independent coding, reliability evidence, or other measurement checks | Claim-level variables can be applied consistently by coders |
| Sensitivity-supported | Supported by perturbation diagnostics, reruns, matched-budget tests, prompt/order tests, or model variation | Claims about stability, separability, retrieval variation, or robustness |
| Future guidance | Proposed as a design requirement for future studies, not completed evidence in the current paper | Tier 2 model validation, production GraphRAG/vector RAG, expert audit-validity validation |

## Action Codes

| Action | Meaning |
|---|---|
| Keep | Claim is supported at the stated evidence level |
| Narrow | Claim should be softened or bounded more explicitly |
| Move | Claim should be moved to supplement, limitations, or future guidance |
| Remove | Claim should be deleted unless new evidence is added |
| Add Evidence | Claim may stay if the planned revision adds the specified evidence |

## Claim Calibration Table

| ID | Current Claim Or Claim Family | Current Location | Current Evidence | Evidence Level | Action | Reviewer Risk If Unchanged | Revision Instruction |
|---|---|---|---|---|---|---|---|
| C01 | Retrieval should be treated as part of research design, not a technical implementation detail. | Abstract, Introduction, Conclusion | Methodological logic; audit research design analogy; reviewer reports accept premise | Conceptual | Keep | Low | Preserve as the paper's core thesis. |
| C02 | Retrieval constructs the information environment from which the model generates responses. | Introduction, Section III | Description of retrieval operations; preserved prompt/context archive | Conceptual + Protocol-validation | Keep | Low | Keep, but use "information environment" consistently rather than implying evidence sufficiency. |
| C03 | Retrieval-environment validity is the extent to which dynamically retrieved information aligns with the intended audit construct. | Abstract, Section III | Definition and five-dimension framework | Conceptual | Keep | Medium | Keep but clarify it is a retrieval-specific diagnostic lens for construct drift, not a replacement for construct validity. |
| C04 | Existing construct validity, measurement validity, reproducibility, and RAG documentation are insufficient by themselves. | Introduction, Section III | Conceptual argument; adjacent-validity table currently planned/partially present | Conceptual | Add Evidence | High | Add stronger adjacent-literature comparison table and explicit reviewer decision rules. |
| C05 | The framework identifies five dimensions: selection, representation, stability, traceability, and separability. | Abstract, Section III | Framework logic; reporting checklist | Conceptual | Keep | Low | Keep, but ensure each dimension has an applied demonstration or clear future-guidance boundary. |
| C06 | The paper operationalizes the framework through retrieval typology, construct mapping, correctness protocol, failure taxonomy, reporting guidance, and reproducibility guidance. | Abstract, Introduction | Manuscript sections and supplement artifacts | Conceptual + Protocol-validation | Keep | Medium | Keep; tie each operational component to a reviewer-useful output. |
| C07 | The demonstration is a nine-filer protocol-validation package with 72 outputs and 281 coded claims. | Abstract, Section VII, Supplement | Run manifests, output archive, coding archive | Protocol-validation | Keep | Low | Keep with exact count QA before resubmission. |
| C08 | The 120-claim independent coding sample evaluates source-use and integration coding reliability. | Abstract, Section VII, Appendix F | Independent coding results, kappa statistics | Measurement-validation | Keep | Medium | Keep, but state it validates protocol variables, not audit-domain expert conclusions. |
| C09 | Retrieval-condition labels can mask different claim-level evidence bases. | Abstract, Introduction, Section VII | 281 coded claims; hybrid evidence-use decomposition; independent coding for source-use/integration | Protocol-validation + Measurement-validation | Keep | Low-Medium | Keep as the central empirical methodological result; frame as design-specific but important. |
| C10 | Hybrid retrieval often does not produce actual integrated text-XBRL reasoning. | Abstract implied, Section VII, Appendix F | 8 of 89 hybrid claims integrated; coding archive | Protocol-validation + Measurement-validation | Narrow | Medium | Phrase as "in this design, hybrid-condition labels did not guarantee integrated claim-level evidence use." Avoid broad frequency implication. |
| C11 | Retrieval design changes the evidence basis of LLM-generated audit claims. | Introduction | Claim-level coding by condition | Protocol-validation | Narrow | Medium-High | Revise to "retrieval design changes the observed claim-level source-use profile in this demonstration." Avoid causal-sounding "changes" unless sensitivity tests support it. |
| C12 | Retrieval design changes valid inference in LLM-based audit research. | Introduction / implied by research question | Conceptual argument plus demonstration | Conceptual + Protocol-validation | Narrow | High | Rephrase as "retrieval design can change which inferences are justified." Add decision-rule table before making this claim. |
| C13 | The demonstration supports the methodological need for claim-level evidence-use coding rather than response-level retrieval-condition evaluation. | Section VII | Hybrid evidence-use results; independent coding reliability for evidence-use and integration | Protocol-validation + Measurement-validation | Keep | Low | Keep and move earlier as empirical motivation. |
| C14 | XBRL relational retrieval creates a distinct information environment from narrative text retrieval. | Section VII, Appendix C | XBRL facts/paths, text chunks, separate contexts | Protocol-validation | Keep | Medium | Keep, but add XBRL concept/relation coverage diagnostic to show construct relevance. |
| C15 | Text retrieval supports narrative traceability; XBRL retrieval supports graph-valid reported-fact traceability. | Section VII, Appendix B/C/G | Text chunks, XBRL fact/path archive, source IDs | Protocol-validation | Keep | Medium | Keep, but avoid implying either source establishes audit evidence sufficiency. |
| C16 | Hybrid retrieval supports integrated correctness only when claims actually use both evidence layers. | Section VII, Discussion | Integrated correctness coding; 8 bridge claims | Measurement-validation | Keep | Low | Keep; this is one of the strongest and cleanest claims. |
| C17 | The source-to-context-to-output-to-claim chain is observable. | Section VII, Appendix D/F/G | Retrieval logs, prompts, raw outputs, claim coding, source IDs | Protocol-validation | Keep | Low | Keep as a positive methodological result. |
| C18 | The coded output validation identified no unresolved source identifiers in the analyzed set. | Section VII, Appendix G | Automated source-ID resolvability checks | Protocol-validation | Keep | Low-Medium | Keep as source-ID resolvability only; do not imply source substantiates every audit inference. |
| C19 | The protocol can diagnose whether hybrid retrieval produces actual narrative-XBRL integration or one-layer use. | Section VII | Hybrid mechanism diagnostic and coding reliability | Measurement-validation + Protocol-validation | Keep | Low | Keep. |
| C20 | The bounded six-filer extension shows protocol applicability across varied reporting environments. | Section VII, Appendix H | 48 extension outputs, 187 claims across six filers | Protocol-validation | Keep | Medium | Keep as bounded applicability/transferability, not representativeness. |
| C21 | The extension preserves the main inference that retrieval-condition labels do not reveal claim-level evidence use. | Section VII | Extension coding summaries | Protocol-validation | Narrow | Medium | Use "is consistent with" rather than "preserves" unless formal comparison is added. |
| C22 | The extension reveals boundary conditions such as Caterpillar complexity and Microsoft relation-path scarcity. | Section VII, Appendix H | Retrieval diagnostics by filer | Protocol-validation | Keep | Low | Keep as qualitative boundary-condition evidence. |
| C23 | Context-volume diagnostics improve separability and source-composition transparency. | Discussion, Appendix I | Context word counts and source-environment perturbation diagnostics | Sensitivity-supported at retrieval-stage only | Narrow | High | State these improve separability documentation, not output-level separability. |
| C24 | Source-environment perturbation diagnostics strengthen stability/separability evidence. | Discussion, Appendix I | Top-k and XBRL fact/path perturbations without LLM reruns | Sensitivity-supported at source-stage only | Narrow | High | Label as retrieval-stage diagnostics. Do not call them output robustness tests. |
| C25 | The demonstration provides stronger evidence for traceability, representation, separability documentation, and claim-level evidence-use coding than for temporal or stochastic stability. | Discussion | Evidence trail plus limited diagnostics | Protocol-validation + Measurement-validation | Keep | Low | Keep; this is properly calibrated. |
| C26 | Stronger empirical studies should add matched-budget, order, prompt, model, and expert-coding checks. | Discussion, Appendix I | Methodological logic and reviewer concerns | Future guidance | Keep | Low | Keep as Tier 2 guidance. |
| C27 | The current demonstration does not show hybrid retrieval superiority, XBRL improvement in audit reasoning, model audit expertise, or failure prevalence. | Section VII, Discussion, Supplement | Boundary logic | Conceptual boundary | Keep | Low | Keep but reduce repetition by consolidating. |
| C28 | XBRL facts and relations are management-reported information, not audit evidence or ground truth. | Introduction, Literature, Discussion, Supplement | XBRL/audit evidence logic | Conceptual | Keep | Low | Keep prominently. |
| C29 | Preliminary audit-valid boundary diagnostics are useful as a claim-level layer. | Introduction, Section V/VII | Author coding and examples | Conceptual + preliminary protocol evidence | Narrow | High | Replace any aggregate implication with "audit-boundary diagnostic"; require expert coding for stronger claims. |
| C30 | Audit-valid correctness requires professional judgment. | Discussion | Audit-evidence logic | Conceptual | Keep | Low | Keep. |
| C31 | The current prototype is intentionally inspectable: keyword-ranked text chunks and table-based XBRL fact/path retrieval. | Introduction, Discussion, Appendix B/C | Scripts and processed data | Protocol-validation | Keep | Low | Keep; this boundary protects against overclaiming. |
| C32 | Vector indexes, RDF/OWL stores, graph databases, and GraphRAG are reporting guidance and portability extensions rather than implemented systems. | Introduction, Discussion, Appendix | Boundary statement | Future guidance | Keep | Low | Keep, and ensure title/abstract do not imply implementation. |
| C33 | The paper provides guidance for designing, evaluating, and reporting LLM-based auditing research. | Abstract, Conclusion | Framework + reporting checklist + demonstration | Conceptual + Protocol-validation | Keep | Medium | Keep but tie to specific deliverables and decision rules. |
| C34 | The paper provides criteria for evaluating whether retrieval-created information environments support inference from LLM outputs. | Introduction, Conclusion | Conceptual framework + claim protocol | Conceptual + Protocol-validation | Keep | Low-Medium | Keep; add reviewer decision-rule table for support. |
| C35 | The demonstration should be interpreted as a methodological reproducibility package rather than a benchmark archive. | Data Availability, Supplement | Package contents and boundaries | Protocol-validation | Keep | Low | Keep. |
| C36 | Exact third-party LLM output replication may require local model digest and environment configuration. | Data Availability, Appendix E | Ollama metadata note; model ID boundary | Protocol-validation boundary | Keep | Low-Medium | Keep; verify model metadata note remains synchronized. |

## Claims Requiring Immediate Narrowing

These are the highest-risk claims to revise before resubmission.

| ID | Risk | Required Revision |
|---|---|---|
| C11 | "Retrieval design changes the evidence basis" can sound causal or general. | Revise to "In this demonstration, different retrieval designs produced different observed claim-level source-use profiles." |
| C12 | "Retrieval design changes valid inference" may overstate empirical support. | Revise to "Retrieval design can affect which inferences are justified, and the framework identifies when those effects are inference-threatening." |
| C21 | "Extension preserves the main inference" sounds stronger than bounded applicability. | Revise to "Extension results are consistent with the claim-level evidence-use concern across additional purposive filers." |
| C23 | "Improve separability" can imply completed matched-budget tests. | Revise to "improve separability documentation and identify confounds for Tier 2 testing." |
| C24 | "Strengthen stability/separability evidence" may overstate source-stage perturbations. | Revise to "provide retrieval-stage source-composition perturbation evidence, not output-level robustness." |
| C29 | Audit-valid diagnostics remain preliminary. | Use "audit-boundary diagnostic" unless expert audit-domain coding is added. |

## Claims That Need New Evidence Before They Can Be Strengthened

| Claim Area | Needed Evidence | Related Workstream |
|---|---|---|
| Distinctiveness from adjacent validity/RAG concepts | Adjacent-concept comparison table and non-accounting retrieval-evaluation literature | Workstream 1 |
| Construct-to-retrieval alignment | Ex ante revenue and inventory construct protocols | Workstream 2 |
| XBRL relational retrieval construct relevance | XBRL concept/relation coverage diagnostic and worked examples | Workstream 3 |
| Audit-boundary validity | Audit-domain expert coding or stronger narrowing | Workstream 4 / Gate A |
| Separability/stability | Matched-budget, order, prompt, top-k/relation-depth, and optional second-model diagnostics | Workstream 5 / Gate B |

## Red-Team Terms Flagged For Manuscript Pass

The following terms require review in the next pass:

| Term / Phrase | Risk | Preferred Treatment |
|---|---|---|
| validates the framework | May imply full empirical validation | Use "illustrates," "operationalizes," or "provides protocol-validation evidence" unless stronger evidence is added |
| retrieval effects | May imply causal identification | Use "retrieval-conditioned differences" or "observed source-use profiles" unless matched sensitivity supports causal language |
| audit-valid correctness | May imply expert audit validation | Use "audit-boundary diagnostic" unless expert coding is completed |
| hybrid retrieval | Can imply integrated reasoning | Clarify "hybrid condition" versus "integrated claim" |
| XBRL-augmented reasoning | Can imply XBRL improves reasoning | Use "XBRL relational retrieval environment" or "XBRL-supported graph-valid claim" |
| robust | Implies sensitivity or statistical robustness | Use only if tied to completed diagnostics |
| generalizes | Implies external validity | Use "travels across purposive cases" or "bounded applicability" |
| evidence | Can imply audit evidence | Use "retrieved materials," "public filing support," or "management-reported XBRL information" where appropriate |

## Reviewer Decision-Rule Draft

This draft should become a manuscript table after refinement.

| Retrieval Problem Type | When It Matters | Reviewer Decision |
|---|---|---|
| Inference-invalidating | Retrieved environment omits or misrepresents construct-critical material needed for the stated audit construct | Reject or require redesign for claims depending on that construct |
| Design-confounding | Retrieval condition differs in context volume, order, salience, prompt, or model in a way that prevents attribution | Require sensitivity analysis or narrow causal interpretation |
| Measurement-threatening | Claim-level coding cannot be applied reliably or independently | Require coder validation, clearer protocol, or narrower measurement claims |
| Disclosure-limiting | Retrieval details are incomplete but the paper makes only descriptive or illustrative claims | Require disclosure, package clarification, or appendix support |
| Acceptable boundary | Limitation is disclosed and does not affect the specific claim being made | Accept with boundary statement |

## Audit-Evidence Hierarchy Draft

This draft should be integrated into the manuscript and supplement.

| Level | Meaning | Current Demonstration Status |
|---|---|---|
| Public-filing support | Claim is supported by retrieved public SEC filing text | Demonstrated through text chunks and source IDs |
| XBRL graph/reporting support | Claim is consistent with retrieved management-reported XBRL facts or relation paths | Demonstrated through fact/path IDs and graph-valid coding |
| Assertion relevance | Claim relates to a plausible audit assertion or risk area | Illustrated through construct protocols and coding, but needs tighter ex ante definition |
| Audit-boundary diagnostic | Claim is assessed for whether it overreaches beyond public filing/XBRL support | Preliminary diagnostic unless expert-coded |
| Audit evidence sufficiency | Claim is supported by evidence sufficient and appropriate for an audit conclusion | Not demonstrated in current public-filing/XBRL package |

## Implementation Implications For The Manuscript

1. The introduction can keep a strong thesis, but should avoid saying the demonstration proves retrieval effects.
2. Section III should add the reviewer decision-rule table to make the framework practical.
3. Section V should replace or reframe "audit-valid correctness" with the audit-evidence hierarchy.
4. Section VII should describe the 8-of-89 hybrid result as design-specific evidence-use heterogeneity.
5. Section VIII should consolidate boundaries rather than repeating them after nearly every result.
6. The response letter should explicitly state where claims were narrowed and where new evidence was added.

## SR-00 Status

`SR-00` is complete at the planning/register level. `SR-00A` is also complete for the current manuscript and online supplement markdown sources; see `plan/117_red_team_wording_pass_log.md`. `SR-00B` is complete; see `plan/118_reviewer_decision_rule_table_log.md`. `SR-00C` is complete; see `plan/119_audit_evidence_hierarchy_implementation_log.md`. The next execution item is `SR-01`: draft the adjacent-validity comparison section and table.
