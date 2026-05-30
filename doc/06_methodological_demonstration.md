# Methodological Demonstration

## Purpose

The demonstration should show how retrieval design changes what researchers can validly infer from LLM outputs.

It should not rank retrieval methods or prove that XBRL-based or hybrid retrieval is better.

## Required Framing

The demonstration is descriptive rather than inferential. Its goal is to demonstrate framework utility, not to test performance hypotheses.

## Suggested Design

- Use actual SEC filing and Inline XBRL data.
- Select 3 less-prominent SEC filers.
- Use 2 industries.
- Use 2 audit constructs:
  - revenue recognition risk
  - inventory valuation assertion
- Compare 3 retrieval designs:
  - text-based contextual retrieval
  - XBRL-based relational retrieval
  - hybrid retrieval

## Required Outputs

The demonstration should include:

- retrieved text chunks
- XBRL relation paths
- LLM claims
- claim-level coding
- failure mode examples
- retrieval logs, at least in an appendix
- inference shift table

## Inference Shift Table

| Observed Pattern | Naive Inference | Framework-Based Inference |
|---|---|---|
| Hybrid retrieval has highest score | Hybrid is best | Hybrid may improve integrated correctness but reduce separability |
| XBRL retrieval reduces relation hallucination | XBRL retrieval is superior | XBRL improves graph-validity but may create source overreach |
| Text retrieval gives richer answer | Text retrieval reasons better | Text retrieval improves narrative support but may not preserve reported relations |
| LLM identifies revenue risk | LLM understands audit risk | Claim may be text-supported or graph-valid but only partially audit-valid |

## Example Claim

Claim:

> Contract liabilities increased, indicating revenue recognition risk.

Possible coding:

| Layer | Score | Rationale |
|---|---:|---|
| Text-supported | 0.5 | Disclosure mentions contract liabilities but does not directly establish cutoff risk |
| Graph-valid | 1 | XBRL facts show reported contract liability change |
| Audit-valid | 0.5 | Plausible risk cue, but not sufficient as an audit conclusion |
| Integrated | 0.5 | Text and graph support a risk cue, not a definitive conclusion |

## Sensitivity Checks

The demonstration or guidance should include sensitivity checks for:

- model variation
- prompt variation
- retrieval top-k or traversal depth
- token budget equalization
- taxonomy version
- graph extraction spot-checks
- repeated retrieval stability

## What Success Looks Like

The demonstration succeeds if it shows that a simple accuracy comparison leads to different inferences than a retrieval-environment validity analysis.
