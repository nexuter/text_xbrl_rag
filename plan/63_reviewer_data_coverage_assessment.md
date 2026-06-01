# Reviewer Assessment: Does The Data Sufficiently Support The Claimed Contributions?

Revision note: This assessment was superseded by the full-scale extension revision in `plan/89_demonstration_scope_and_validation_revision_log.md`. The current submission package uses 72 outputs, 48 extension outputs, 281 preliminary coded claims, and 464 retrieval-log rows.

## Purpose

This memo evaluates whether the paper's claimed contributions are sufficiently covered by the actual data, outputs, coding, and reproducibility artifacts. The stance is that of a critical AJPT reviewer asking:

> Are the data strong enough to support what the manuscript claims?

## Reviewer Verdict

**Yes for the bounded methodological contribution; no for broader empirical or performance claims.**

The current data are sufficient to support a **methodological demonstration** of retrieval-environment validity and claim-level evidence-use divergence. The data are not sufficient to support claims about model performance, retrieval-method superiority, population-level failure rates, or final audit-judgment validity.

The manuscript is data-supported if it claims:

> Retrieval design creates different information environments, and response-level retrieval labels are insufficient because individual LLM claims can rely on different evidence bases.

The manuscript is not data-supported if it claims:

1. XBRL retrieval improves audit reasoning;
2. hybrid retrieval performs better than text or XBRL retrieval;
3. `gemma4:31b` has strong audit expertise;
4. audit-valid scores are final expert evidence;
5. the observed failure modes generalize to SEC filers generally;
6. the prototype implements production vector RAG, RDF/OWL, or GraphRAG.

## Data Coverage Summary

| Evidence Component | Current Data |
|---|---:|
| Active filers | 9 |
| Main deep-case filers | 3 |
| Bounded-extension filers | 6 |
| Retrieval context conditions | 42 |
| Text contexts | 12 |
| XBRL contexts | 12 |
| Hybrid contexts | 12 |
| LLM-only diagnostic contexts | 6 |
| LLM outputs | 42 |
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total coded claims | 182 |
| Factual claims | 76 |
| Risk/assertion-mapping claims | 99 |
| Insufficient-context claims | 7 |
| Invalid source references detected | 0 |
| Claims requiring manual/expert review | 182 |

## Hybrid Evidence-Use Test

The strongest data support concerns the paper's demonstration claim:

> Response-level retrieval labels are insufficient because claims within the same condition can rely on different evidence bases.

Hybrid-condition claim evidence use:

| Run | Both Text And XBRL | Text Only | XBRL Only | Total Hybrid Claims |
|---|---:|---:|---:|---:|
| Main deep cases | 3 | 22 | 5 | 30 |
| Bounded extension | 4 | 19 | 7 | 30 |
| Total | 7 | 41 | 12 | 60 |

Reviewer interpretation:

This is strong support for the paper's central demonstration claim. Hybrid retrieval did not produce uniformly integrated evidence use. Most hybrid-condition claims used only one evidence type. This directly supports the argument that condition-level labels are inadequate and that claim-level coding changes research inference.

## Contribution-By-Contribution Data Coverage

| Claimed Contribution | Data Needed | Current Coverage | Reviewer Assessment |
|---|---|---|---|
| Retrieval-environment validity as a conceptual framework | Conceptual logic and literature support | Not primarily data-dependent | Sufficient if framed as framework. |
| Retrieval as research design | Controlled retrieval conditions, logs, prompts, source contexts | 42 prompt/context conditions with text, XBRL, hybrid, and LLM-only diagnostic conditions | Sufficient for methodological illustration. |
| Data/variable construction for LLM auditing research | Inspectable retrieval artifacts and claim-level variables | Text chunks, XBRL facts, relation paths, retrieval logs, prompt contexts, outputs, and 182 coded claims | Strong coverage. |
| Claim-level correctness protocol | Claims segmented and coded across correctness layers | 182 preliminary author-coded claims across factual, risk/assertion, and insufficient-context types | Adequate, but expert review needed for audit-valid claims. |
| XBRL relational retrieval as a distinct information environment | XBRL facts, relation paths, relation diagnostics | XBRL facts and paths for eight of nine active filers; MSFT path scarcity documented as boundary case | Sufficient, with boundary language. |
| Hybrid retrieval evidence-use divergence | Hybrid claims with text/XBRL source-use differences | 60 hybrid claims; only 7 use both text and XBRL | Strong coverage. |
| Bounded applicability beyond three main filers | Additional varied filers and extension outputs | Six-filer extension with 18 outputs and 88 claims | Adequate for bounded robustness, not population inference. |
| Source traceability | Source IDs and validation checks | No invalid global source IDs or local text-rank references detected | Strong coverage for traceability. |
| Audit-valid correctness | Expert audit judgment or reliable coding | Preliminary author coding only; all 182 require manual/expert review | Not sufficient for final audit-valid claims. |
| Performance comparison | Representative sample, stable metrics, model comparison, statistical inference | Not designed or executed | Not supported. |

## What The Data Support Well

### 1. Retrieval Environments Are Distinguishable

The data include separate text, XBRL, hybrid, and LLM-only conditions. The retrieval contexts and logs show that different evidence environments were supplied to the same model under controlled prompts.

Reviewer assessment:

This supports the research-design contribution.

### 2. The Data/Variable-Construction Contribution Is Real

The project converted raw SEC filings and Inline XBRL into:

1. text chunks;
2. XBRL facts;
3. XBRL relation paths;
4. retrieval logs;
5. prompt/context files;
6. LLM outputs;
7. claim-level coding variables.

Reviewer assessment:

This is one of the strongest data-supported contributions. The paper is not merely proposing a conceptual framework; it demonstrates how retrieval artifacts become research data and claim-level variables.

### 3. Hybrid Labels Mask Claim-Level Evidence Use

The hybrid-condition results show that hybrid prompts often produced claims using only text or only XBRL evidence. This directly supports the claim that response-level condition labels are not enough.

Reviewer assessment:

This is the clearest empirical illustration and should be emphasized in the main text.

### 4. Boundary Conditions Are Observable

MSFT produced no selected revenue relation paths under the current retrieval design. CAT produced a much larger XBRL fact and relation environment than other filers.

Reviewer assessment:

These cases are valuable because they show why retrieval diagnostics must precede inference. They also prevent the paper from sounding like XBRL relational retrieval is always rich or superior.

### 5. Source Traceability Is Credible

Validation found no invalid source references in coded outputs.

Reviewer assessment:

This supports traceability validity and strengthens the appendix/reproducibility claim.

## What The Data Do Not Support

### 1. Final Audit-Valid Correctness

All 182 claims require manual/expert review. Current coding is preliminary author coding.

Reviewer implication:

The paper can discuss audit-valid coding as a protocol and illustrate it with examples, but it cannot treat audit-valid means as final expert evidence.

### 2. Retrieval-Method Performance Ranking

The design is not a benchmark. It does not use representative sampling, formal statistical inference, multiple models, or retrieval sensitivity tests.

Reviewer implication:

Do not rank text, XBRL, or hybrid retrieval.

### 3. Population Generalizability

The nine active filers support a maximum-variation methodological demonstration, not a representative sample.

Reviewer implication:

Do not estimate prevalence of failure modes or claim broad SEC-filer generalization.

### 4. Full Vector RAG Or Ontology Implementation

The current prototype uses keyword-ranked text retrieval and table-based XBRL relational retrieval. It does not implement production vector DB, RDF/OWL triple store, or GraphRAG.

Reviewer implication:

Keep vector/RDF/GraphRAG language as implementation guidance or future extension.

### 5. Model-General Claims

The demonstration uses one model, `gemma4:31b`, with local Ollama and temperature 0.

Reviewer implication:

The method is model-agnostic, but the data do not show cross-model robustness.

## Reviewer Concern: Is The Demonstration Large Enough?

For a methodology paper, yes, if framed correctly.

The three main cases support deep traceability. The six-filer extension adds breadth across industry and reporting complexity. Together, they are enough to demonstrate that the protocol can be applied and that evidence-use divergence is observable beyond one hand-picked case.

But the sample is not enough for:

1. prevalence estimation;
2. performance benchmarking;
3. statistical comparison across conditions;
4. generalized conclusions about SEC filers.

## Required Manuscript Guardrails

The manuscript should use the following guardrails:

1. Call the evidence a **methodological demonstration**, not an empirical test.
2. Interpret Table 9A/9B as **transparency artifacts**, not performance results.
3. State that audit-valid and integrated scores are **preliminary author-coded diagnostics**.
4. Emphasize **claim-level evidence-use divergence** as the main data-supported finding.
5. Use MSFT and CAT as **boundary-condition examples**, not anomalies to hide.
6. Keep vector DB, RDF/OWL, and GraphRAG claims at the **implementation-guidance** level.

## Data-Supported Main-Text Claim

The following claim is fully supported:

> Across 42 retrieval-conditioned outputs and 182 preliminary coded claims, the demonstration shows that retrieval-condition labels do not determine claim-level evidence use. In hybrid conditions, only 7 of 60 claims used both text and XBRL sources, while 41 used text only and 12 used XBRL only. This pattern supports the methodological need for claim-level evidence-use coding rather than response-level retrieval-condition evaluation.

## Data-Supported Appendix Claim

The following appendix claim is fully supported:

> The retrieval and output archive preserves source-to-context-to-claim traceability across the main and bounded-extension runs. The validation check found 42 expected outputs, 182 coded claims, and no invalid source references, although all audit-valid and integrated-correctness scores remain preliminary until audit-domain expert review.

## Claims To Remove Or Avoid

Avoid these statements:

1. "Hybrid retrieval improves audit reasoning."
2. "XBRL relational retrieval is more accurate than text retrieval."
3. "The model successfully performed audit risk assessment."
4. "The extension validates the framework across SEC filers."
5. "The audit-validity scores indicate high quality."
6. "The ontology/RDF implementation improves LLM reasoning."

## Recommended Strengthening If The Authors Want A Stronger Reviewer Reaction

These are not strictly required for a methodology submission, but they would increase reviewer confidence:

| Optional Strengthening | Benefit |
|---|---|
| Audit-domain expert review of 10-20 selected claims | Strengthens audit-valid and integrated-correctness credibility. |
| Independent recoding of a small claim subset | Shows the coding protocol is usable beyond the authors. |
| Source spot-check table for selected extension examples | Reinforces traceability in the appendix. |
| Small retrieval sensitivity check for top-k or chunk window | Strengthens stability/selection validity. |
| Explicit data availability statement | Makes reproducibility contribution more concrete. |

## Final Reviewer Judgment

The current data are sufficient for the paper's sharpened methodological contribution. They show that:

1. retrieval environments can be constructed and logged from real SEC/XBRL filings;
2. retrieval artifacts can be converted into claim-level research variables;
3. hybrid retrieval labels do not guarantee integrated evidence use;
4. source traceability can be validated across outputs and coded claims;
5. bounded extension cases reveal meaningful retrieval-environment boundary conditions.

The data are not sufficient for broader claims about audit performance, retrieval superiority, population prevalence, or final expert audit judgment. If the manuscript stays within the methodological frame, the data coverage is adequate and reviewer-defensible.
