# Gate A Decision Memo: Audit-Boundary Validation

## Decision

For this revision cycle, the paper adopts the **claim-narrowing path** rather than adding independent audit-domain expert coding.

Audit-boundary coding remains a qualitative, preliminary author diagnostic used to flag whether a claim appears to stay within the evidentiary limits of public filing text and management-reported XBRL. It is not treated as final audit-judgment evidence, model-performance evidence, or audit evidence sufficiency.

## Rationale

The paper is positioned as an AJPT methodological paper about retrieval-environment validity, data/variable construction, and reviewer-evaluable protocol design for LLM-based audit research. The current independent coding evidence strongly supports the reliability of core retrieval-validity variables:

- claim segmentation;
- claim kind;
- evidence-use type;
- text-supported correctness;
- graph-valid correctness;
- integrated correctness;
- confidence coding.

However, the current coder exercise does not establish audit-domain expert validation for audit-boundary judgments. Adding that expert layer would move the paper toward a stronger audit-judgment validation study and would require additional design features: expert recruitment, expertise documentation, training, blinded expert coding, reconciliation, reliability analysis, and stronger controls over output-level model performance.

## Reviewer-Facing Position

The revision should state clearly:

1. The current paper validates a measurement protocol, not audit judgments.
2. Independent coders validate source-use and correctness-variable reliability, not audit evidence sufficiency.
3. Audit-boundary notes are retained because they are useful for showing where public filing and XBRL support ends.
4. Audit-boundary notes should not be aggregated as validated audit-performance outcomes.
5. Future Tier 2 studies making audit-judgment or model-performance claims should add audit-domain expert coding and reliability evidence.

## Implementation Consequences

| Area | Revision Rule |
|---|---|
| Main manuscript | State the Gate A decision explicitly: audit-boundary remains a qualitative diagnostic, not an expert-validated outcome |
| Online supplement | Add a gate-decision table distinguishing variables independently reliability-tested from audit-boundary notes |
| Replication README | Clarify that legacy `audit_valid_prelim` columns are retained for compatibility but should be read as preliminary audit-boundary diagnostics |
| Data files | Do not report aggregate audit-boundary means as model-performance evidence |
| Response letter | Present this as a deliberate scope choice, not an omission |

## Column-Name Boundary

Some processed claim-level files retain legacy column names such as `audit_valid_prelim` and `audit_valid_rationale`. These names should be interpreted as preliminary audit-boundary diagnostics. They are not final audit-judgment labels and should not be used as dependent variables for model-performance claims without expert validation.

## Status

Gate A is resolved for the current revision: **claim narrowing, not new audit-domain expert coding**.
