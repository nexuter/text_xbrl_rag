# Phase 9 Revision Action List

## Purpose

This action list converts the reviewer stress test in `plan/44_phase9_reviewer_stress_test_v1.md` into concrete manuscript revisions.

## Priority 1: Must Complete Before Submission

| Action | Target File | Manuscript Location | Rationale |
|---|---|---|---|
| Add "Why Existing Validity Language Is Not Enough" subsection | `plan/42_phase8_manuscript_draft_v1_with_table_callouts.md` or v2 draft | Section 3, after definition | Defends novelty against "renamed construct validity" criticism |
| Add "Implications for LLM-Based Audit Research Design" subsection or box | v2 draft | End of Introduction or Section 6 | Directly answers what audit researchers do differently |
| Move aggregate preliminary coding results out of main-text emphasis | v2 draft and `plan/41_phase8_tables_and_figures_package.md` | Section 7 / Appendix | Prevents Table 9 from being read as model performance evidence |
| Add expert-coding requirement paragraph | v2 draft | Section 5 or Section 7 | Protects audit-valid and integrated correctness claims |
| Add explicit prototype boundary statement | v2 draft | Abstract and Introduction | Avoids vector-RAG/RDF performance expectations |
| Add literature-positioning table | v2 draft or appendix | Section 2 | Sharpens novelty relative to top accounting/auditing literature |
| Strengthen demonstration headline | v2 draft | Section 7 opening | Makes inference-shift contribution clearer |

## Priority 2: Should Complete Before Reviewer Circulation

| Action | Target File | Manuscript Location | Rationale |
|---|---|---|---|
| Add one-sentence inference purpose before each main table | v2 draft | Throughout | Prevents table-driven/checklist-paper impression |
| Add one-sentence research-design implication after each main table | v2 draft | Throughout | Shows tables operationalize the framework |
| Shorten technical implementation prose in main text | v2 draft | Sections 4, 6, 7 | Keeps paper methodology-focused |
| Add "reviewer use" framing for reporting guidance | v2 draft | Section 6 | Aligns with AJPT methodological call |
| Clarify that XBRL relation retrieval supports reported relation preservation, not audit evidence | v2 draft | Sections 4, 5, 8 | Reinforces audit boundary |
| Create appendix index with final artifact paths | New appendix index file | Appendix package | Improves reviewer navigation |

## Priority 3: Valuable If Time Allows

| Action | Target File | Manuscript Location | Rationale |
|---|---|---|---|
| Obtain audit-domain expert review for selected claims | Coding files and appendix | Section 7 / Appendix F | Moves demonstration closer to accept-level evidence |
| Add independent coder reliability plan or pilot | Appendix F | Section 5 / Appendix | Strengthens audit-valid coding credibility |
| Run a small prompt-variation sensitivity check | Data and appendix | Appendix H | Demonstrates stability guidance in practice |
| Run a small top-k or retrieval-scope sensitivity check | Data and appendix | Appendix H | Demonstrates selection-validity sensitivity |
| Generate one RDF/OWL export example | Data and appendix | Appendix C | Supports ontology portability discussion without overclaiming |
| Add one vector retrieval prototype run | Data and appendix | Appendix B/H | Only needed if manuscript leans heavily on vector RAG language |

## Proposed v2 Draft Changes

### Abstract

Add a boundary sentence:

> Our demonstration uses an inspectable keyword/text and table-based XBRL relational prototype; vector indexes, RDF/OWL stores, and graph databases are discussed as implementation extensions that require additional reporting rather than as performance claims in this study.

### Introduction

Add reviewer-facing fit:

> For reviewers, the framework provides criteria for evaluating whether an LLM audit study's retrieval environment supports the claimed audit construct.

Add a short implications paragraph:

> After reading this paper, an audit researcher should define the audit construct before retrieval, choose retrieval operators that fit that construct, log the evidence actually supplied to the model, evaluate output claims by correctness layer, and avoid treating reported XBRL relations as audit evidence.

### Section 2

Add a literature positioning table:

| Literature Stream | What It Studies | Limitation for LLM Retrieval Studies | This Paper's Increment |
|---|---|---|---|
| XBRL research | Structured reporting data and XBRL-based measures | Does not study retrieval-created LLM information environments | Uses XBRL as a relational retrieval environment |
| Textual analysis | Text as data and text-based measures | Often treats retrieved/processed text as the observed data object | Treats retrieval as a dynamic design choice |
| LLM accounting research | Model performance, prompting, and accounting tasks | May evaluate outputs without validating retrieved evidence | Adds retrieval-environment validity and claim-level correctness |
| Audit analytics/AI | Technology-enabled audit data and tools | Focuses on practice systems and evidence use rather than LLM retrieval design | Provides research-design guidance for LLM audit studies |
| AJPT methodology | Guidance for audit research methods | Does not yet address dynamic retrieval in LLM studies | Extends methodology guidance to retrieval-augmented LLM designs |

### Section 3

Add subsection:

> Why Existing Validity Language Is Not Enough

Core point:

> Retrieval creates a dynamic materials boundary. The evidence package observed by the model is not fully specified by the corpus, prompt, or model. It is created by a retrieval pipeline at runtime. Therefore, researchers must validate the retrieval-created information environment itself.

### Section 5

Add expert-coding paragraph:

> Audit-valid and integrated correctness require audit-domain judgment. In empirical applications, coders should have audit expertise, coding should be independent of prompt construction where feasible, disagreement should be reconciled or reported, and reliability should be disclosed. The present demonstration uses preliminary author coding only to illustrate the protocol.

### Section 7

Replace demonstration headline with:

> The demonstration shows that retrieval condition labels do not reveal claim-level evidence use.

Revise Table 9 handling:

> We report aggregate preliminary coding in the appendix as a transparency artifact. We do not interpret these means as model performance because audit-valid and integrated scores require expert validation.

## Reviewer-Facing Response Strategy

If a reviewer says the paper is "just construct validity":

> The paper agrees that the issue is grounded in construct validity, but identifies a retrieval-specific mechanism: the information environment is dynamically constructed at runtime. Retrieval-environment validity operationalizes how researchers should document and evaluate that mechanism.

If a reviewer says the demonstration is weak:

> The demonstration is intentionally descriptive and Tier 1. Its purpose is not to test model performance but to show how the framework changes interpretation of the same output claims. The full claim table and source trail are provided for transparency.

If a reviewer says XBRL is not audit evidence:

> The paper agrees and makes that boundary central. XBRL supports graph-valid reported relation claims, not audit-valid conclusions unless combined with additional audit evidence and professional judgment.

If a reviewer says this is too technical:

> The technical appendices operationalize the validity framework. They are included so reviewers can inspect selection, representation, stability, traceability, and separability.

## Completion Criteria for v2

The v2 draft should be considered complete when:

1. The abstract and introduction state the prototype boundary.
2. Section 3 defends the novelty of retrieval-environment validity.
3. Section 2 includes a sharper literature-positioning table.
4. Section 5 includes expert-coding safeguards.
5. Section 7 presents the demonstration as evidence-use divergence, not performance.
6. Table 9 is moved to appendix or explicitly labeled as a transparency artifact.
7. The manuscript explicitly answers: "What would an audit researcher do differently after reading this paper?"
