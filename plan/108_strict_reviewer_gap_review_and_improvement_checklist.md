# Strict Reviewer Gap Review And Improvement Checklist

## Purpose

This memo evaluates the current submission package from the standpoint of a strict AJPT methodology reviewer. The review assumes the paper is framed as a research-methodology paper for LLM-based auditing research, not as a model-performance or audit-practice validation study.

## Overall Reviewer Verdict

The paper is now substantially stronger than the earlier descriptive-demonstration version. The most important improvements are the nine-filer full-scale protocol package, the 120-claim independent coding validation sample, the corrected integrated-correctness rule, the hybrid one-layer-use mechanism diagnostic, and the explicit Tier 1 versus Tier 2 boundary.

However, an accept-oriented reviewer would still ask whether the paper's title, abstract, and methodological claims are fully matched to the actual implementation. The current package is close to submission-ready, but several issues should be corrected or tightened before treating it as final.

## P0 Issue: Mechanical Count Inconsistency

### Finding

The checksum manifest has 408 rows in the current generated checksum summary and authoritative package files, but several replication README files still report 387 checksum manifest rows.

Observed evidence:

- `data/processed/checksums/checksum_summary.md` reports `Total files hashed: 408`.
- `submission/replication_package/AUTHORITATIVE_FILES.md` reports checksum manifest rows = 408.
- `submission/Replication_Package_Manifest.md` reports 408 file checksums.
- `submission/README_REPLICATION.md`, `submission/replication_package/README_REPLICATION.md`, and root `README_REPLICATION.md` still report checksum manifest rows = 387.

### Why A Reviewer Would Care

This is not conceptually important, but it is credibility-sensitive. A reviewer who checks replication counts may treat count drift as evidence that the package was assembled after the manuscript and not fully synchronized.

### Required Fix

Update all replication README expected-count tables to report checksum manifest rows = 408. Then regenerate the processed-only replication zip if any package copy changes.

## P1 Issue: Title And Abstract May Slightly Over-Promise XBRL-Augmented Implementation

### Finding

The title and abstract emphasize "XBRL-Augmented Retrieval" and "XBRL relational retrieval." The manuscript correctly states that the implementation is keyword-ranked text retrieval and table-based XBRL fact/path retrieval, while RDF/OWL, vector stores, graph databases, and GraphRAG are guidance or extensions rather than implemented systems.

### Reviewer Risk

A reviewer sympathetic to the paper may still ask: Is this really an XBRL-augmented retrieval methodology, or a table-based source-tracing demonstration using XBRL-derived facts and paths? The answer is acceptable, but it should be stated early so the title does not appear to promise a full ontology or graph database implementation.

### Recommended Fix

Add one sentence to the abstract or introduction clarifying that the demonstration implements an inspectable table-based XBRL fact/path retrieval prototype, while RDF/OWL and graph database implementations are treated as portability extensions. Keep the title, but reduce possible overclaiming in the first page.

## P1 Issue: Stability Dimension Is Conceptually Central But Empirically Thin

### Finding

The framework includes stability as one of five retrieval-environment validity dimensions. The current demonstration preserves deterministic retrieval logs and includes source-environment perturbation diagnostics, but it does not perform repeated retrieval runs across time, indexing variants, embedding variants, or reranking variants.

### Reviewer Risk

The stability dimension may look under-demonstrated relative to selection, traceability, and separability. The paper already says the current diagnostic is not output robustness evidence, but the main framework could still read as if all five dimensions are equally validated.

### Recommended Fix

In Section VII or VIII, add a short sentence: the demonstration provides stronger evidence for traceability, representation, separability documentation, and evidence-use coding than for temporal or stochastic retrieval stability; stability is operationalized here through preserved deterministic retrieval artifacts and specified as a Tier 2/Tier 3 requirement for repeated or embedding-based retrieval systems.

## P1 Issue: Independent Coders Validate Protocol Variables, Not Audit Expertise

### Finding

The manuscript reports excellent independent-coding reliability for evidence-use type and integrated correctness. It also states that audit-valid correctness remains preliminary unless independently reviewed by audit-domain experts. This distinction is mostly clear, but the coder qualification boundary could be made more explicit.

### Reviewer Risk

A reviewer could ask whether the independent coders were audit-domain experts. If not, high reliability supports the coding protocol but should not be read as audit-judgment validation. The manuscript already says this in several places, but one concise statement in the independent-coding paragraph would close the loop.

### Recommended Fix

Add a sentence near the independent-coding reliability paragraph: the independent coding exercise was designed to evaluate the consistency of source-use and integration coding, not to substitute for expert audit-domain validation of audit-valid correctness.

## P1 Issue: Main Manuscript Could Better Explain Why 120 Claims Is Enough For Protocol Reliability

### Finding

The supplement explains that the validation sample includes all 89 hybrid-condition claims and 31 non-hybrid comparison claims. The main manuscript reports the reliability results but does not fully explain why this sampling choice is appropriate for the paper's central claim.

### Reviewer Risk

Without the rationale, 120 claims may look arbitrary. The design is defensible because the key protocol-risk is hybrid evidence integration; therefore, all hybrid claims are coded, and non-hybrid claims serve as comparison cases.

### Recommended Fix

Add one sentence after the 120-claim sample description: this sampling design intentionally overweights hybrid claims because the central methodological question is whether a hybrid retrieval condition actually produces integrated text-XBRL evidence use.

## P1 Issue: "No Invalid Source References" Could Sound Broader Than It Is

### Finding

The manuscript states that coded output validation identified no invalid source references in the analyzed set. The supplement says selected source spot-checks identified no invalid source references.

### Reviewer Risk

If the validation script checks source IDs mechanically rather than semantically validating every source's substantive relevance, "no invalid source references" could be read too strongly.

### Recommended Fix

Clarify that this means source identifiers resolved to preserved retrieved materials, not that every cited source independently validates the audit inference. Suggested wording: "no unresolved source identifiers in the analyzed set."

## P2 Issue: Context-Volume Diagnostic Is Useful But Could Be Misread As Separability Control

### Finding

The manuscript carefully says the context-volume diagnostic does not eliminate separability concerns. Still, the phrase "strengthen separability" appears in a few places paired with "source-composition transparency."

### Reviewer Risk

A strict reviewer may argue that context-volume reporting documents separability threats but does not strengthen separability unless matched-budget or evidence-order sensitivity is conducted.

### Recommended Fix

Use "documents separability threats" or "improves separability transparency" rather than "strengthens separability" wherever possible.

## P2 Issue: Appendix Closing Note Appears Outdated

### Finding

The online supplement ends by saying remaining packaging improvements include adding a concise replication README, capturing model metadata, and deciding whether to add file checksums. But the package now has a replication README and checksums.

### Reviewer Risk

This looks like an old planning note that escaped into the submission-facing supplement.

### Recommended Fix

Revise the closing note to say remaining tasks are author-specific submission items and optional model-digest/raw-source archiving decisions, not missing replication README/checksum work.

## P2 Issue: Local Model Metadata Is Still A Reproducibility Boundary

### Finding

The manuscript says exact output replication may require recording local model digest and environment configuration. This is honest, but if the package lacks model digest metadata, a reviewer may ask for it.

### Reviewer Risk

For an LLM methodology paper, model provenance matters even if the study is not a benchmark.

### Recommended Fix

If available from Ollama, add a small model metadata note to the replication package: model name, local tag, digest if available, parameter size, quantization if known, temperature, run date, and hardware/serving caveat. If digest is unavailable, state that explicitly.

## P2 Issue: Literature Position Is Strong But Could Be Sharpened In One Sentence

### Finding

The manuscript positions against LLM/RAG performance studies, XBRL research, textual analysis, and audit methodology. The contribution is clear, but the novelty sentence can be even sharper.

### Recommended Fix

Add or sharpen one sentence in the contribution paragraph: prior studies typically evaluate data, models, auditors, or outputs; this paper treats the retrieval-created information environment as the unit of methodological validation.

## Accept-Level Assessment

### Current Status

Conditional near-ready for AJPT methodology review, but not final until the P0 count inconsistency and outdated appendix closing note are fixed.

### What The Paper Can Credibly Claim

- It introduces retrieval-environment validity as a methodological construct.
- It operationalizes retrieval-created information environments as auditable research-design artifacts.
- It demonstrates a source-to-context-to-output-to-claim protocol across 9 filers, 72 outputs, and 281 preliminary coded claims.
- It validates key protocol variables through a 120-claim independent coding exercise.
- It shows that hybrid retrieval labels do not guarantee integrated evidence use.

### What The Paper Still Cannot Claim

- Hybrid retrieval improves audit judgment.
- XBRL retrieval improves LLM audit reasoning.
- The model is validated for audit practice.
- Failure-mode frequencies generalize to SEC filers.
- Audit-valid correctness is independently expert-validated.
- The implementation is a production vector RAG, RDF/OWL, graph database, or GraphRAG system.

## Recommended Revision Order

1. Fix checksum count mismatch from 387 to 408 in all replication README files.
2. Remove or update the outdated appendix closing note about missing README/checksums.
3. Add first-page implementation boundary sentence for table-based XBRL fact/path retrieval.
4. Add one sentence explaining the 120-claim validation sampling logic.
5. Clarify source-reference validation as source-ID resolvability rather than substantive audit validation.
6. Replace any remaining "strengthen separability" wording with "documents separability threats" or "improves separability transparency."
7. Add or confirm local model metadata/digest note.
8. Regenerate DOCX files, checksum manifest, and processed-only replication zip after edits.
9. Rerun count and risky-phrase QA.

