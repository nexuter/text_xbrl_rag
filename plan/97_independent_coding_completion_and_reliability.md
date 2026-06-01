# Independent Coding Completion And Reliability Evidence

Note: The initial reliability values in this log were superseded by the recoded independent-coding application documented in `plan/99_recoded_independent_coding_application_log.md`.

## Purpose

This step records completion of the independent claim-coding validation exercise. It converts the prior coder-ready validation package into completed reliability evidence for the claim-level measurement protocol.

## Inputs

- `coder/coder1_coding_form.csv`
- `coder/coder2_coding_form.csv`

Each coder completed 120 claims. The validation sample includes all 89 hybrid-condition claims and 31 non-hybrid comparison claims.

## Outputs

- `data/processed/coding/independent_coding_results.csv`
- `data/processed/coding/intercoder_reliability_summary.md`
- `data/processed/coding/independent_coding_disagreements.csv`
- `scripts/analyze_independent_coding.py`

The completed files were copied into the submission replication package and the replication zip was rebuilt.

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

## Interpretation

The results provide strong reliability evidence for the paper's claim-level measurement protocol. This materially reduces the reviewer concern that the demonstration relies only on author coding.

The results support use of claim-level evidence-use and correctness variables as methodological diagnostics. They do not establish model-performance effects, retrieval-method superiority, or final audit-valid conclusions.

## Manuscript Revisions

- The main manuscript now reports the independent coding sample and reliability statistics in Section VII.
- The online supplement now includes independent coding validation evidence and a reliability-results table.
- The replication README now describes the completed independent coding evidence rather than a template-only package.

## QA

- Combined independent coding rows: 240.
- Disagreement records across coded variables: 19.
- Revised DOCX files regenerated.
- Word COM QA passed:
  - Main manuscript: 36 pages, 8,828 words, 8 tables.
  - Online supplement: 16 pages, 4,067 words, 24 tables.
- Main manuscript rendered to 36 PNG pages through Word PDF export plus PyMuPDF.
- Replication zip rebuilt with 403 entries.
