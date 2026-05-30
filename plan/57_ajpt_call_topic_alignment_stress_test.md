# AJPT Call Topic Alignment Stress Test

## Purpose

This memo evaluates whether the manuscript's target position aligns with the specific topic examples listed in the AJPT Methodological Papers call. The goal is to avoid a vague "methodology paper" claim and instead identify the exact call topics the manuscript should claim.

## Bottom-Line Position

The manuscript should position itself primarily under two AJPT call topics:

1. **Evaluation of research design, modeling, or variable selection and recommendations for best practices.**
2. **New or improved techniques related to data collection or variable construction.**

It should position itself secondarily under:

3. **New or improved analytical techniques applied to archival, experimental, qualitative, or other data.**

It should not try to claim direct alignment with topics focused on existing statistical techniques, experimental manipulation, participant recruitment, or qualitative participant selection.

## Topic-By-Topic Alignment

| AJPT Call Topic | Fit | Why It Fits Or Does Not Fit | Recommended Position |
|---|---|---|---|
| New or improved analytical or statistical techniques applied to archival, experimental, qualitative, or other data | Moderate fit | The paper introduces a claim-level analytical protocol for evaluating LLM outputs using retrieval logs, text chunks, XBRL facts, and relation paths. It is analytical, but not statistical. | Use as secondary fit. Emphasize "analytical technique" and "other data," not statistical technique. |
| Evaluation of existing statistical techniques and recommendations for best practices | Weak fit | The manuscript does not evaluate statistical estimators, inference methods, standard errors, models, or statistical best practices. | Do not claim this topic. |
| Evaluation of research design, modeling, or variable selection and recommendations for best practices | Strongest fit | The central contribution is that retrieval is part of research design in LLM-based auditing research. The framework evaluates whether retrieval-created information environments align with audit constructs. | Make this the primary call-topic alignment. |
| New or improved techniques related to data collection or variable construction | Strong fit | The paper proposes techniques for collecting and organizing retrieval evidence: text chunks, XBRL facts, relation paths, retrieval logs, prompt contexts, LLM outputs, and claim-level coding variables. | Make this the second primary alignment. |
| Established but underutilized experimental or qualitative research designs relevant for auditing research | Weak to moderate fit | The paper uses controlled retrieval conditions, but it is not primarily an experimental-design paper and does not study human participants or qualitative field methods. | Mention only if describing controlled retrieval-condition logic; do not lead with it. |
| Guidance on effective manipulation of independent variables and measurement of dependent variables in experimental studies | Moderate but risky fit | Retrieval condition can be treated as a manipulated design factor, and claim-level correctness layers can be treated as measurement outcomes. However, calling the demonstration an experiment may make reviewers expect stronger experimental controls and statistical inference. | Use carefully in response to reviewers, not as the main submission identity. |
| Guidance on participant selection and recruitment for experimental and qualitative papers | No fit | The manuscript does not involve human participants, recruitment, or qualitative participant sampling. | Do not claim this topic. |

## Why The Strongest Fit Is Research Design

The manuscript's central move is not technical. It is methodological:

> Retrieval design determines the information environment observed by the LLM. Therefore, retrieval choices affect construct validity, evidence traceability, and the validity of research inferences drawn from LLM outputs.

This maps directly to the call topic on **research design, modeling, or variable selection** because the manuscript tells audit researchers how to:

1. define the intended audit construct before retrieval;
2. select retrieval operators appropriate to that construct;
3. distinguish text retrieval, XBRL relational retrieval, hybrid retrieval, and LLM-only baselines;
4. evaluate whether retrieved evidence supports the inference being drawn;
5. avoid attributing retrieval-created differences to model capability;
6. report retrieval environments transparently enough for replication and review.

## Why The Second Strongest Fit Is Data Collection And Variable Construction

The manuscript also fits the call topic on **data collection or variable construction** because it converts LLM audit studies from opaque prompt-response exercises into inspectable research datasets.

The proposed research data objects include:

| Research Data Object | Role In The Methodology |
|---|---|
| Text chunks | Narrative retrieval units for disclosure and risk-language evidence. |
| XBRL facts | Structured reported accounting fact units. |
| XBRL relation paths | Structured relation units for graph-valid checks. |
| Retrieval logs | Evidence-selection records for selection, stability, and traceability validity. |
| Prompt-context files | Records of the information environment actually supplied to the LLM. |
| LLM outputs | Raw model responses under controlled retrieval conditions. |
| Claim-level coding table | Constructed variables for text support, graph validity, audit validity, integrated correctness, and failure modes. |

The paper's variable-construction contribution is not firm-level XBRL variable construction. It is **research-design variable construction for LLM audit studies**: transforming retrieval artifacts and LLM outputs into auditable claim-level evidence-use variables.

## Where The Paper Should Not Overclaim

The paper should not claim that it contributes to:

1. statistical estimation;
2. causal inference methods;
3. survey or experimental participant recruitment;
4. auditor decision aids;
5. audit procedure design;
6. model-performance benchmarking;
7. proof that XBRL improves LLM audit reasoning.

Those claims would weaken alignment with the call by making the manuscript sound like a statistical methods paper, human-subjects design paper, audit-practice paper, or technology benchmark.

## Recommended Call-Alignment Sentence For The Introduction

Use this sentence in the first two pages:

> The paper aligns with AJPT's Methodological Papers call by evaluating a research-design problem in LLM-based auditing research: how retrieval choices construct the information environment from which LLM outputs are generated, and how researchers should collect, represent, and code retrieval artifacts so that audit-related inferences are valid and reproducible.

## Recommended Cover-Letter Sentence

Use this sentence in the cover letter:

> The manuscript fits the call's topics on research design and data/variable construction: it evaluates retrieval as a research-design choice in LLM-based auditing studies and provides best-practice guidance for collecting retrieval evidence, constructing claim-level evidence-use variables, and reporting retrieval-created information environments.

## Revised Submission Positioning

The most precise submission positioning is:

> This is a methodological paper on research design and data/variable construction for LLM-based auditing research. It introduces retrieval-environment validity to evaluate whether dynamically retrieved text and XBRL relation data support the audit construct under study, and it provides best-practice guidance for retrieval design, evidence logging, claim-level coding, and reproducibility reporting.

## Reviewer Stress Test

### Potential Reviewer Concern 1

> The paper does not introduce a statistical method, so why does it fit a methodological call?

Response:

> The call includes research design, modeling, variable selection, data collection, and variable construction, not only statistical techniques. The manuscript addresses retrieval as a research-design and variable-construction problem in LLM-based auditing research.

### Potential Reviewer Concern 2

> Is this really about audit methodology, or is it about a tool for auditors?

Response:

> The manuscript does not recommend audit procedures or evaluate audit engagement workflows. It provides methodological guidance for researchers who use LLMs, text retrieval, and XBRL data to study audit-related constructs.

### Potential Reviewer Concern 3

> Does the XBRL component make the paper too systems-oriented?

Response:

> XBRL is used as a structured research data source to illustrate retrieval-environment validity. The manuscript does not claim to build a production ontology system or benchmark graph retrieval. It shows how reported accounting relations can be represented, logged, and evaluated when used in LLM-based audit research.

## Required Updates To Manuscript Package

| Location | Update |
|---|---|
| Abstract | Keep current AJPT-aligned abstract, but consider adding "data/variable construction" if space permits. |
| Introduction | Add the recommended call-alignment sentence. |
| Contribution paragraph | Name the two primary call topics: research design and data/variable construction. |
| Cover letter | Use the recommended cover-letter sentence. |
| Reviewer response memo | Include the three stress-test responses above. |

## Final Assessment

The target position is well aligned with the AJPT Methodological Papers call if the manuscript explicitly claims the right topics. The paper should not try to fit every bullet. Its strongest and most defensible position is:

1. **Primary:** research design and best-practice guidance for LLM-based auditing research.
2. **Primary:** data collection and claim-level variable construction from retrieval artifacts and LLM outputs.
3. **Secondary:** analytical protocol for evaluating claim-level evidence use.

This is sharper than the broader statement that the paper is simply an "LLM audit methodology" paper.
