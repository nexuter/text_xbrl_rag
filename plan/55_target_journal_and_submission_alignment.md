# Target Journal and Submission Alignment

## Decision

Target journal:

**Auditing: A Journal of Practice & Theory (AJPT)**

Submission category:

**AJPT Methodological Papers Call**

Submission positioning:

**A research-methodology paper for LLM-based auditing research, not an audit-practice procedure paper and not a retrieval-system performance benchmark.**

## Source Basis

This decision is based on the official AJPT journal page and the AJPT Methodological Papers call.

The AJPT journal page states that AJPT's purpose is to improve the practice and theory of auditing, broadly including internal auditing, external auditing, and other attestation activities. It also states that papers embodying improvements in auditing theory or auditing methodology are central to the journal.

The AJPT Methodological Papers call states that the call is intended for studies that introduce new methods or provide recommendations regarding existing methods applicable to auditing research. It explicitly distinguishes this from papers that investigate new methods or recommendations related to audit procedures or audit methodologies in practice. The call lists research design, modeling, variable selection, data collection, and variable construction as relevant methodological topics.

Official sources:

- AJPT journal page: https://aaahq.org/Research/Journals/Auditing-A-Journal-of-Practice-and-Theory
- AJPT Methodological Papers call: https://aaahq.org/portals/0/documents/calls/2025/AJPT%20Methodological%20Papers.pdf

## Fit Assessment

| AJPT Methodological Call Criterion | Fit of Current Paper | Required Framing |
|---|---|---|
| Introduces or recommends methods applicable to auditing research | Strong fit | Present retrieval-environment validity as a research-design framework. |
| Evaluation of research design, modeling, or variable selection | Strong fit | Emphasize how retrieval design affects construct validity and inference in LLM audit studies. |
| New or improved data collection or variable construction techniques | Strong fit | Position XBRL relational retrieval as structured research-data construction, not audit evidence. |
| Guidance for future research best practices | Strong fit | Keep reporting checklist, correctness protocol, and failure-mode taxonomy central. |
| Audit-practice procedure recommendations | Risk if overstated | Avoid language suggesting the framework tells auditors how to perform audit procedures. |
| Technical system or benchmark contribution | Risk if overstated | Avoid ranking RAG, GraphRAG, vector retrieval, or `gemma4:31b` performance. |

## Specific Call-Topic Alignment

The manuscript should claim alignment with the call topics selectively rather than trying to fit every example in the call.

Primary alignment:

1. **Evaluation of research design, modeling, or variable selection and recommendations for best practices.**
2. **New or improved techniques related to data collection or variable construction.**

Secondary alignment:

3. **New or improved analytical techniques applied to archival, experimental, qualitative, or other data.**

Do not claim alignment with statistical-technique evaluation, participant recruitment, or human-subject experimental design topics. The detailed stress test is documented in `plan/57_ajpt_call_topic_alignment_stress_test.md`.

## Recommended Submission Identity

The manuscript should identify itself as follows:

> This paper develops a methodology for designing and evaluating retrieval-augmented LLM studies in auditing research. It introduces retrieval-environment validity, a framework for assessing whether the information retrieved for an LLM is aligned with the intended audit construct. The paper provides a retrieval typology, correctness protocol, failure-mode taxonomy, reporting checklist, and SEC/XBRL-based methodological demonstration. The objective is to improve research design and inference in LLM-based audit research, not to recommend audit procedures or benchmark model performance.

## Why AJPT Is The Primary Target

AJPT is the strongest target because the paper is explicitly about auditing research methods. The manuscript's intended audience is audit researchers who may use LLMs, RAG, XBRL, or other structured data in research designs. The paper improves how these researchers specify constructs, build retrieval environments, evaluate LLM outputs, and report reproducibility evidence.

Alternative outlets are weaker fits:

| Outlet | Why It Is Less Preferred |
|---|---|
| Accounting Horizons | More practice-facing. Could fit if rewritten as guidance for practitioners, but that would weaken the methodological contribution. |
| Journal of Information Systems | Better fit for systems architecture, ontology implementation, or database design, but that would pull the paper away from audit methodology. |
| Journal of Emerging Technologies in Accounting | Better fit for emerging technology demonstration, but less ideal for a research-methodology contribution. |
| Contemporary Accounting Research / The Accounting Review | Possible only if the paper includes a stronger empirical theory contribution or broad accounting research design contribution beyond auditing. |

## Critical Reviewer Boundary

The largest AJPT risk is that reviewers may read the manuscript as a proposal for using LLMs, RAG, or XBRL in audit practice. That would place it partly outside the methodological call.

To avoid this, the manuscript must consistently use the following boundaries:

1. The object is **audit research design**, not audit engagement execution.
2. XBRL is **management-reported structured data**, not audit evidence or ground truth.
3. Retrieval is a **research-design choice** because it constructs the LLM's information environment.
4. The demonstration is **descriptive and methodological**, not a model-performance evaluation.
5. The two-layer case design supports **traceability and bounded generalizability**, not population inference.

## Required Manuscript Changes Before Submission

| Manuscript Area | Required Change |
|---|---|
| Title and abstract | Keep "research design" and "retrieval-environment validity" prominent. Avoid wording that implies audit automation. |
| Introduction | State within the first page that the paper is submitted to the AJPT methodological call as a research-methodology paper. |
| Contribution paragraph | Make the first contribution the validity framework, not XBRL or LLM implementation. |
| Literature review | Position against audit research methodology, textual-analysis research design, XBRL data construction, and LLM accounting research. |
| Demonstration | Keep main deep cases and bounded extension separated. Avoid performance language. |
| Tables and figures | Move aggregate coding summaries to appendix unless expert-coded reliability is added. |
| Appendix | Include full reproducibility trail, but label prototype choices clearly. |
| Cover letter | Explicitly say the manuscript is for the AJPT Methodological Papers call. |

## Cover-Letter Positioning Paragraph

> We submit this manuscript for consideration under AJPT's Methodological Papers call. The manuscript introduces retrieval-environment validity as a research-design framework for auditing studies that use retrieval-augmented large language models. Rather than proposing an audit procedure or benchmarking a particular model, the paper provides methodological guidance for aligning retrieval design with audit constructs, evaluating LLM outputs at the claim level, and reporting retrieval-created information environments transparently. The SEC/XBRL demonstration illustrates how the framework changes research inference and provides reproducible artifacts for reviewer inspection.

## Reviewer-Positive Framing

An AJPT reviewer should be able to describe the paper's contribution this way:

> This paper gives audit researchers a vocabulary and protocol for designing LLM/RAG studies so that observed model outputs are not mistaken for model capability when they may be caused by the retrieved information environment. The XBRL component is valuable because it shows how structured reporting relations can be used as research data in retrieval designs while preserving important audit boundaries.

## Reviewer-Negative Framing To Avoid

The manuscript should not sound like:

> This paper proposes a new LLM-based audit tool that uses XBRL ontology data to improve audit reasoning.

That framing is weaker for AJPT's methodological call because it sounds like an audit-technology or audit-procedure contribution. The stronger framing is:

> This paper proposes a research-design methodology for studying LLM outputs in auditing when the model's information environment is constructed through text retrieval, XBRL relational retrieval, or hybrid retrieval.

## Submission Timing

The AJPT Methodological Papers call is open through **September 30, 2026**. As of the current project date, **May 29, 2026**, the paper has approximately four months for manuscript completion, expert coding, appendix finalization, and cover-letter preparation.

## Bottom Line

AJPT Methodological Papers is the correct primary target. The manuscript is well aligned if it is framed as a methodology paper for LLM-based auditing research design. The next work package should be a submission-aligned manuscript revision that integrates the bounded extension into a v3 draft while tightening every section against the AJPT call boundary.
