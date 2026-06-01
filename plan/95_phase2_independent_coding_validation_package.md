# Phase 2 Independent Coding Validation Package

Note: The reliability values in this phase log were superseded by the recoded independent-coding application documented in `plan/99_recoded_independent_coding_application_log.md`.

## Purpose

This phase addresses reviewer concerns that the claim-level coding protocol is central to the paper but initially author-coded. Two independent coders have now completed the 120-claim validation sample, allowing the revision to report reliability evidence for the core claim-level measurement variables.

## Files Created

- `data/processed/coding/independent_coding_protocol.md`
- `data/processed/coding/independent_coding_sample.csv`
- `data/processed/coding/independent_coding_results.csv`
- `data/processed/coding/intercoder_reliability_summary.md`
- `data/processed/coding/independent_coding_disagreements.csv`

The same files were copied into `submission/replication_package/data/processed/coding/`.

## Validation Sample

The sample contains 120 claims from the 281-claim archive.

| Condition | Sampled Claims |
|---|---:|
| Hybrid | 89 |
| LLM-only | 12 |
| XBRL | 10 |
| Text | 9 |
| Total | 120 |

The sample intentionally includes all 89 hybrid-condition claims because the key measurement-validity concern is whether hybrid-condition outputs actually integrate text and XBRL evidence.

## Reliability Results

| Variable | N | Agreement | Percent Agreement | Reliability Statistic |
|---|---:|---:|---:|---:|
| Claim segmentation agreement | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Claim kind | 120 | 117 | 97.5% | Cohen's kappa = 0.957 |
| Evidence-use type | 120 | 120 | 100.0% | Cohen's kappa = 1.000 |
| Text-supported correctness | 120 | 117 | 97.5% | Weighted kappa = 0.919 |
| Graph-valid correctness | 120 | 119 | 99.2% | Weighted kappa = 0.934 |
| Integrated correctness | 120 | 120 | 100.0% | Weighted kappa = 1.000 |
| Confidence code | 120 | 105 | 87.5% | Cohen's kappa = 0.754 |

## Protocol Content

The protocol defines:

- claim segmentation rules;
- claim-kind coding;
- evidence-use type coding;
- text-supported correctness;
- graph-valid correctness;
- integrated correctness;
- qualitative audit-boundary notes;
- reliability and reconciliation reporting requirements.

Audit-valid correctness remains qualitatively bounded unless audit-domain expert coding and reliability evidence are completed.

## Manuscript And Supplement Changes

- Added a paragraph in Section VII explaining that the replication package now includes the independent coding protocol, 120-claim validation sample, results template, and reliability summary template.
- Added Appendix Table F4 in the online supplement to identify the independent coding validation instrument.
- Updated the replication README to list the completed independent coding files and reliability evidence.
- Updated the replication manifest and authoritative file index.

## Reviewer-Response Position

The revision should use the following position:

> We agree that claim-level coding is central to the paper and should be externally reviewable. We therefore added a formal independent coding protocol and a fixed 120-claim validation sample that includes all hybrid-condition claims. Two independent coders completed the sample. After recoding under the clarified `integrated_code` instruction, agreement is 100.0 percent for evidence-use type, 97.5 percent for text-supported correctness, 99.2 percent for graph-valid correctness, and 100.0 percent for integrated correctness, with kappa or weighted kappa values between 0.919 and 1.000 for these core variables. These results support the reliability of the claim-level measurement protocol while preserving the paper's boundary that the demonstration is not a model-performance test or final audit-validity study.

## Remaining Requirement For Stronger Claims

Remaining disagreement records should be used to refine qualitative audit-boundary guidance and, if stronger audit-judgment claims are made later, to support reconciliation by audit-domain experts.
