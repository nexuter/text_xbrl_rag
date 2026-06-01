# Post-Revision Strict Reviewer Assessment

## Purpose

This memo re-audits the manuscript package after the strict-reviewer revisions logged in `plan/109_strict_reviewer_gap_revision_log.md`. The goal is to identify any remaining issues a demanding AJPT methodology reviewer could use to request major revisions.

## Verification Performed

Machine checks confirmed the following authoritative counts and markers:

| Item | Status |
|---|---|
| Main LLM run manifest | 24 rows, as reported |
| Extension LLM run manifest | 48 rows, as reported |
| Main coded claims | 94 rows, as reported |
| Extension coded claims | 187 rows, as reported |
| Checksum manifest | 408 rows, as reported |
| Main DOCX includes table-based XBRL fact/path boundary | Confirmed |
| Main DOCX includes hybrid-heavy validation-sample rationale | Confirmed |
| Main DOCX uses "no unresolved source identifiers" language | Confirmed |
| Main DOCX includes temporal/stochastic stability boundary | Confirmed |
| Supplement DOCX has updated checksum-based closing note | Confirmed |
| Replication zip README reports checksum rows = 408 | Confirmed |
| Replication zip model metadata note reports 48 extension outputs | Confirmed |

The prior P0 count inconsistency is closed.

## Overall Reviewer Verdict

The current package is defensible as an AJPT methodology-paper submission. It now makes a coherent Tier 1 methodological claim: retrieval should be treated as research design, retrieval environments can be preserved and inspected, and claim-level evidence-use variables can reveal inference-relevant differences hidden by retrieval-condition labels.

The remaining issues are not fatal, but several could still become major-revision comments if the reviewer reads the paper as promising more than a Tier 1 protocol-validation study.

## Remaining P1 Issue: Abstract Understates The Validation Evidence And Overstates The Generic Demonstration

### Finding

The abstract describes the framework and says the demonstration uses text, XBRL, hybrid, and LLM-only retrieval. It does not mention the nine-filer design, 72 outputs, 281 preliminary coded claims, or the 120-claim independent coding validation sample.

### Reviewer Risk

The abstract may undersell the strongest evidence added during revision. A reviewer could initially read the paper as still being a conceptual/descriptive illustration rather than a protocol-validation package with independent coding reliability.

### Recommended Improvement

Revise the abstract to include one compact evidence sentence:

> We illustrate the framework in a nine-filer protocol-validation package comprising 72 retrieval-conditioned outputs and 281 preliminary coded claims, with a 120-claim independent coding sample used to evaluate source-use and integration coding reliability.

This would sharpen the paper's AJPT-methodology fit without claiming model performance.

## Remaining P1 Issue: Non-Hybrid Comparison Sample Selection Needs One More Sentence

### Finding

The manuscript and supplement explain that the independent coding sample includes all 89 hybrid-condition claims and 31 non-hybrid comparison claims. They clearly justify why all hybrid claims are included, but they do not fully explain how the 31 non-hybrid comparison claims were selected.

### Reviewer Risk

A strict reviewer may ask whether the non-hybrid comparison claims were cherry-picked. This does not threaten the central hybrid-integration claim because all hybrid claims are included, but it affects perceived coding-validation discipline.

### Recommended Improvement

Add a short note in the supplement and, if space permits, the main text:

> The non-hybrid comparison claims were included to cover LLM-only, text-only, and XBRL-only evidence-use categories and to give coders non-hybrid anchors for applying the source-use and correctness scales.

If the actual selection was stratified by condition, construct, or claim type, state that explicitly.

## Remaining P1 Issue: "Audit-Valid Correctness" In The Contribution Paragraph Could Still Be Overread

### Finding

The contribution paragraph lists variables created by the protocol, including "audit-valid correctness." Later sections repeatedly state that audit-valid correctness remains preliminary unless reviewed by audit-domain experts.

### Reviewer Risk

Because the contribution paragraph appears early, a reviewer may read the paper as claiming validated audit-valid measurement before reaching the limitations.

### Recommended Improvement

Revise the early contribution wording from:

> audit-valid correctness

to:

> audit-valid boundary diagnostics, when supported by appropriate expert judgment

or:

> preliminary audit-valid boundary diagnostics

This keeps the contribution but avoids making audit-validity sound validated in the current paper.

## Remaining P1 Issue: Model Digest Boundary Is Still Open

### Finding

The model metadata note includes model name, architecture, parameter count, context length, quantization, and temperature. It does not include an Ollama model digest or local file hash.

### Reviewer Risk

For an LLM methodology paper, a reviewer may ask whether `gemma4:31b` is sufficiently reproducible without a digest. The paper already acknowledges this limitation, but a digest would be cleaner.

### Recommended Improvement

Attempt to capture an Ollama digest or model file hash before final submission. If unavailable, add one explicit line to the model metadata note:

> A model digest was not available from the local `ollama show gemma4:31b` output captured for this package.

That converts an omission into a documented boundary.

## Remaining P2 Issue: Replication README Folder Map Could Confuse Processed-Only Package Users

### Finding

The replication README folder map lists `data/raw_sec/` as downloaded SEC filing and Inline XBRL source files. The submission package is explicitly processed-only by default and excludes the full raw SEC archive, while the manifest and submission README explain that raw SEC files are reconstructable or can be uploaded separately.

### Reviewer Risk

A reviewer opening only the processed-only zip could see `data/raw_sec/` in the README and wonder why the folder is absent.

### Recommended Improvement

Add a short note immediately before or after the folder map:

> The processed-only submission archive excludes `data/raw_sec/` by default; raw SEC files are publicly reconstructable using the download script and accession metadata. A separate raw-source archive can be deposited if repository size policy permits.

## Remaining P2 Issue: The Source-Traceability Claim Is Stronger Than The Spot-Check Scope

### Finding

The manuscript now uses the narrower phrase "no unresolved source identifiers," which is good. The supplement also states source spot checks support traceability. However, the distinction between automated source-ID resolution and selected spot-check review could be even clearer.

### Reviewer Risk

Small risk only. A reviewer could ask whether all source IDs were checked or only selected examples.

### Recommended Improvement

Clarify in the supplement that automated validation checks source-ID resolvability across the output set, while selected spot checks illustrate substantive source-to-claim traceability.

## Remaining P2 Issue: Submission Markdown Still Contains Internal Draft Label

### Finding

`submission/Manuscript_Retrieval_as_Research_Design.md` begins with `# Submission-Ready Manuscript Draft v3`. The generated DOCX appears to omit internal draft labels, and the DOCX is the submission file.

### Reviewer Risk

This is not an issue if only DOCX files are submitted. It could look unpolished if the Markdown source is shared as part of a repository.

### Recommended Improvement

Either remove the internal draft label from the submission-facing Markdown copy or ensure only DOCX/PDF files are included for journal review.

## Accept-Level Assessment

### Current Status

No remaining P0 issue identified. The package is now near submission-ready for an AJPT methodology-paper review.

### Likely Reviewer Reaction

A favorable reviewer can now support the paper as a methodological contribution because:

- the claim is clearly Tier 1 protocol validation rather than model-performance validation;
- the evidence package covers nine filers, two constructs, four retrieval conditions, 72 outputs, and 281 preliminary coded claims;
- all hybrid-condition claims are included in the independent coding sample;
- evidence-use type and integrated correctness have strong independent-coding reliability;
- XBRL and audit-evidence boundaries are repeatedly stated;
- replication materials are count-consistent and checksum-backed.

### Most Likely Remaining Major-Revision Request

The most likely major-revision request is not "more data" in general. It is narrower:

> Clarify the validation-sample design and model-provenance boundary, and ensure the abstract and contribution paragraph precisely match the Tier 1 evidence.

## Recommended Next Revision Order

1. Revise the abstract to mention the nine-filer, 72-output, 281-claim, 120-claim independent-coding evidence package.
2. Add one sentence explaining the selection purpose for the 31 non-hybrid comparison claims.
3. Soften the early contribution wording around "audit-valid correctness."
4. Attempt to capture model digest; if unavailable, document that explicitly.
5. Add a processed-only package note to the replication README folder map.
6. Clarify automated source-ID validation versus selected source spot checks.
7. Remove or hide the internal Markdown draft label if Markdown files will be shared with reviewers.
8. Regenerate DOCX, checksums, and the processed-only zip after any textual edits.

