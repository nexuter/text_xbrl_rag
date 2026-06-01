# Pre-Reviewer-Feedback Sanity Check

## Purpose

This memo records the final sanity check performed before circulating the manuscript for reviewer-style feedback.

## Data And Count Checks

| Item | Verified Count |
|---|---:|
| Retrieval contexts | 72 |
| Main LLM outputs | 24 |
| Extension LLM outputs | 48 |
| Main coded claims | 94 |
| Extension coded claims | 187 |
| Total coded claims | 281 |
| Retrieval log rows | 464 |
| Checksum manifest rows | 387 |

`scripts/validate_llm_results.py` completed successfully and rewrote `plan/52_llm_results_validation_log.md`.

## Risk-Phrase Search

The submission-facing files were searched for stale or overclaim-prone language:

- `Primary Construct Role`
- `Audit Mean`
- `Audit Diagnostic`
- `protocol scales`
- `increases confidence`
- `18 outputs`
- `42 retrieval`
- `182 preliminary`
- `583 retrieval`
- `Checksum manifest rows | 383`

No problematic hits remained in the submission-facing manuscript, supplement, README, or core plan files. Boundary statements that say the paper does *not* claim hybrid superiority, XBRL audit-reasoning improvement, or model-performance validation were retained.

## DOCX Internal Text Check

The generated DOCX files were searched internally for risky remnants:

| File | Result |
|---|---|
| `submission/AJPT_Main_Manuscript.docx` | No risky terms; no `Insert Table/Figure` callouts |
| `submission/AJPT_Online_Supplement.docx` | No risky terms; no `Insert Table/Figure` callouts |
| `submission/AJPT_Cover_Letter.docx` | No risky terms |
| `submission/AJPT_Title_Page.docx` | No risky terms |

## Word COM Structural QA

| File | Pages | Words | Tables | Key Language Check |
|---|---:|---:|---:|---|
| `AJPT_Cover_Letter.docx` | 3 | 614 | 0 | Protocol, Tier 2, nine-filer, 48/72 outputs, and 281 claims present |
| `AJPT_Main_Manuscript.docx` | 33 | 7,946 | 7 | Protocol, Tier 2, nine-filer, 48/72 outputs, and 281 claims present |
| `AJPT_Online_Supplement.docx` | 15 | 3,805 | 22 | Protocol, Tier 2, nine-filer, 48/72 outputs, and 281 claims present |
| `AJPT_Title_Page.docx` | 2 | 205 | 0 | Author-facing title page; no protocol-language requirement |

## Replication Package Check

The processed-only ZIP exists and contains the expected core files:

- `PACKAGE_CONTENTS.md`
- `data/processed/checksums/checksum_manifest.csv`
- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`

ZIP entry count: 394.

## Remaining Non-Substantive Items

The following are author/submission-system items rather than methodology issues:

1. Fill author names, affiliations, correspondence details, and date.
2. Confirm conflict-of-interest, funding, acknowledgments, and final data availability wording.
3. Decide whether raw SEC files should be uploaded separately; the current package is processed-only with reconstruction instructions.
4. PNG-based DOCX render QA remains unavailable because the local renderer lacks `pdf2image`; Word COM structural QA was used instead.

## Sanity Verdict

The package is internally consistent for reviewer feedback. The main substantive boundary to preserve is that the paper demonstrates protocol validation and claim-level evidence-use diagnostics, not model-performance validation, retrieval superiority, audit-judgment quality, or failure-mode prevalence.
