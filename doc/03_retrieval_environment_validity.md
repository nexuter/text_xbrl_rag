# Retrieval-Environment Validity

## Definition

**Retrieval-environment validity** is the extent to which the dynamically retrieved information environment provided to an LLM aligns with the audit construct the researcher intends to study.

## Clarification

Retrieval-environment validity is not a replacement for construct validity. It is a retrieval-specific diagnostic lens for evaluating whether the dynamically constructed information environment aligns with the construct the study claims to examine.

## Why It Is Needed

Traditional audit experiments typically define the information set ex ante. In retrieval-augmented LLM studies, the information environment is dynamically constructed by a retrieval system at runtime. The retriever may select, rank, transform, summarize, omit, or reformat information before the model produces an output.

This creates retrieval-specific threats to construct validity.

## Five Dimensions

| Dimension | Audit/Method Anchor | Question | Failure Mode |
|---|---|---|---|
| Selection validity | Relevance | Did retrieval select construct-relevant information? | Omission |
| Representation validity | Reliability / faithful representation | Was retrieved information accurately represented? | Distortion |
| Stability | Reproducibility | Is retrieval stable across equivalent runs? | Retrieval instability |
| Traceability | Documentation / support | Can output claims be traced to retrieved information? | Attribution failure |
| Separability | Internal validity | Can retrieval effects be separated from model effects? | Model-retrieval confounding |

## Core Claim

These dimensions identify how construct validity can be threatened when retrieval systems dynamically construct the LLM's information environment.

## Examples of Validity Threats

- A text retriever retrieves narrative revenue policy disclosures but omits XBRL relations involving contract liabilities.
- An XBRL relation path is rendered as a causal economic relation rather than a reporting relation.
- A hybrid retrieval condition performs better because it receives more total context, not because it supports better reasoning.
- An LLM output refers to a cutoff risk, but the claim cannot be traced to retrieved text or XBRL relation paths.
- A study attributes performance differences to model capability even though retrieval conditions created different information environments.

## Reviewer-Safe Boundary

This concept concerns research design validity. It does not imply that retrieved information constitutes sufficient appropriate audit evidence.
