# Red-Team Wording Pass Log

## Purpose

This log records implementation of `SR-00A` from `plan/112_second_revision_comprehensive_revise_plan.md`.

The goal was to apply the claim-evidence calibration register in `plan/116_claim_evidence_calibration_register.md` to the current manuscript and supplement by reducing wording that could imply unsupported model-performance validation, audit-evidence sufficiency, causal retrieval effects, broad generalizability, or expert audit validation.

## Files Updated

| File | Role |
|---|---|
| `submission/Manuscript_Retrieval_as_Research_Design.md` | Main manuscript wording pass |
| `submission/Online_Supplement_Appendix.md` | Supplement wording pass |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Workflow tracker update |
| `plan/116_claim_evidence_calibration_register.md` | Status update |

## Main Manuscript Changes

### 1. Hybrid Condition Versus Hybrid Retrieval

Changed wording so that "hybrid retrieval" does not automatically imply integrated reasoning.

Examples:

- "hybrid retrieval" -> "a hybrid condition" where the claim concerns the condition label.
- "hybrid retrieval supports integrated correctness" -> "a hybrid condition supports integrated correctness only when claims actually use both source layers."

### 2. Evidence Basis Versus Source-Use Profile

Reduced causal or general language around retrieval effects.

Examples:

- "show how retrieval design changes the evidence basis" -> "document how different retrieval designs produce different observed claim-level source-use profiles."
- "differences change the research inference" -> "differences affect which inferences are justified."
- "retrieval effects" -> "retrieval-conditioned information differences."

### 3. Audit-Valid Correctness

Replaced stronger "audit-valid correctness" language with "audit-boundary diagnostics" where expert audit validation is not present.

Examples:

- "preliminary audit-valid boundary diagnostics" -> "preliminary audit-boundary diagnostics."
- "Audit-valid correctness asks..." -> "Audit-boundary diagnostics ask..."
- "audit-valid conclusions" -> "audit-boundary or audit-judgment conclusions."

### 4. Evidence Versus Retrieved Materials

Reduced uses of "evidence" where the referent is public filing text or management-reported XBRL.

Examples:

- "evidence units" -> "source units."
- "formats evidence" -> "formats retrieved materials."
- "individual claims may use only one evidence layer" -> "individual claims may use only one source layer."

### 5. Protocol Validation Versus Model Performance

Changed wording to emphasize protocol-validation evidence rather than validation of model performance.

Examples:

- "The demonstration validates the proposed protocol" -> "The demonstration provides protocol-validation evidence."
- "validate central coding categories" -> "evaluate the reliability of central coding categories."

### 6. Extension Inference

Narrowed the six-filer extension claim.

Example:

- "the extension preserves the main inference" -> "the extension is consistent with the claim-level source-use concern."

### 7. Separability And Stability Boundaries

Narrowed sensitivity-diagnostic language.

Example:

- "improve separability" -> "improve separability documentation."
- Retained explicit boundary that source-environment perturbation is not output-level robustness.

## Supplement Changes

### 1. Replaced "What This Validates"

Changed appendix subhead-style language:

- "What this validates" -> "What this supports."
- "What this does not validate" -> "What this does not support."

This makes the supplement less likely to imply full empirical validation where the current evidence is protocol-level or diagnostic.

### 2. Audit-Boundary Terminology

Replaced supplement references to audit-valid coding or audit-valid scores with audit-boundary coding or audit-boundary diagnostics.

### 3. Source-Stage Perturbation Boundary

Changed "This evidence strengthens retrieval-stage source-composition transparency" to "This diagnostic supports retrieval-stage source-composition transparency" to avoid overreading source-stage perturbations as model-output robustness.

## QA Search Results

Searches were run for the main risky phrase families:

- `audit-valid`
- `audit-validity`
- `changes the evidence basis`
- `changes valid inference`
- `retrieval effects`
- `validates the proposed`
- `validates the inspectability`
- `What this validates`
- `does not validate`
- `improve separability`
- `strengthen.*stability`

Results:

1. No remaining `audit-valid` or `audit-validity` wording in the checked manuscript/supplement files.
2. No remaining `changes the evidence basis` or `changes valid inference` wording.
3. No remaining `retrieval effects` wording.
4. No remaining `What this validates` / `does not validate` appendix language.
5. One acceptable remaining phrase appears in the main manuscript: "improve separability documentation," which is intentionally bounded and does not claim completed matched-budget or output-level separability testing.

## Remaining Boundary

This pass did not add new empirical evidence. It calibrated language to the current evidence level. The next substantive evidence-building workstreams remain:

1. adjacent-validity comparison and reviewer decision-rule table,
2. ex ante construct protocols,
3. XBRL concept/relation coverage diagnostic,
4. coding-process strengthening and audit-boundary decision,
5. bounded separability/stability sensitivity work.

## SR-00A Status

`SR-00A` is complete for the current manuscript and online supplement markdown sources. Future edits should preserve the same claim-evidence discipline.
