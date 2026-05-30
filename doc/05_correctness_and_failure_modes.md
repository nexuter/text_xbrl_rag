# Claim-Level Correctness and Failure Modes

## Why Claim-Level Coding Is Needed

LLM audit outputs should not be evaluated only as right or wrong. A response may be supported by disclosure text, consistent with XBRL relation paths, and still not be professionally reasonable as audit reasoning.

## Multi-Layered Correctness Protocol

Unit of analysis: individual LLM output claim.

| Correctness Layer | Coding Question |
|---|---|
| Text-supported | Is the claim supported by retrieved disclosure text? |
| Graph-valid | Does the claim match XBRL relation paths? |
| Audit-valid | Is the claim professionally reasonable? |
| Integrated | Are text, graph, and audit logic mutually consistent? |

## Key Sentence

A claim can be text-supported and graph-valid but still audit-invalid if it overstates risk or treats management-coded reported relationships as independent audit evidence.

## Audit-Valid Correctness

Audit-valid correctness should be treated as expert-coded judgment rather than an objective benchmark.

Suggested rubric:

- `1`: professionally reasonable, linked to relevant assertion or risk, and appropriately qualified
- `0.5`: plausible but incomplete, overgeneralized, or missing important caveats
- `0`: unsupported, misleading, or treats management-coded information as independent audit evidence

## Reliability Requirements

Minimum reporting for audit-valid coding:

- at least two independent coders
- coder expertise disclosed
- coding guide included
- disagreement resolution protocol
- inter-rater agreement reported
- coding uncertainty disclosed
- graph-valid coding spot-checked

## Retrieval Failure Mode Taxonomy

| Failure Mode | Linked Validity Issue | Example |
|---|---|---|
| Omission | Selection validity | Revenue policy retrieved but contract liability relation omitted |
| Distortion | Representation validity | XBRL calculation path rendered as causal relation |
| Retrieval instability | Stability | Equivalent query returns materially different relation paths |
| Attribution failure | Traceability | Claim cannot be traced to retrieved text or graph path |
| Model-retrieval confounding | Separability | Performance attributed to model but caused by retrieval condition |
| Relation hallucination | Graph-valid correctness | Non-existing account relation invented |
| Source overreach | Audit-valid correctness | Management-coded XBRL relation treated as independent audit evidence |
| Integration failure | Integrated correctness | Narrative and XBRL trend not reconciled |

## Full and Light Protocols

| Protocol | Use Case | Components |
|---|---|---|
| Full protocol | Hypothesis-testing studies | Expert coding, graph validation, text support coding, inter-rater reliability |
| Light protocol | Exploratory benchmark or large-scale screening | Sampled claim audit, automated graph validation, retrieval log inspection |
