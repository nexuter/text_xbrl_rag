# Ex Ante Construct Protocol Revision Log

## Purpose

This log records implementation of `SR-03` and `SR-04` from `plan/112_second_revision_comprehensive_revise_plan.md`.

The reviewers argued that the demonstration's audit constructs were too broadly specified. This revision adds ex ante protocols for:

1. revenue recognition risk,
2. inventory valuation assertion.

The goal is to make construct-to-retrieval alignment reviewer-evaluable before LLM outputs are interpreted.

## Files Updated

| File | Change |
|---|---|
| `submission/Manuscript_Retrieval_as_Research_Design.md` | Added ex ante revenue and inventory construct protocol summary; added PCAOB standards references; updated appendix listing |
| `submission/Online_Supplement_Appendix.md` | Added Appendix Tables A2 and A3 with detailed construct protocols; updated Appendix A map/title |
| `submission/Tables_and_Figures.md` | Expanded Table 6 with revenue recognition risk and inventory valuation assertion rows |
| `plan/112_second_revision_comprehensive_revise_plan.md` | Workflow tracker updated |

## Audit-Standard Anchors

The construct protocols are anchored to:

1. PCAOB AS 1105, Audit Evidence.
2. PCAOB AS 2110, Identifying and Assessing Risks of Material Misstatement.
3. PCAOB AS 2301, The Auditor's Responses to the Risks of Material Misstatement.

These standards support the distinction between:

1. assertion-level risk assessment,
2. response design,
3. sufficient appropriate audit evidence,
4. audit conclusions.

## Main Manuscript Revision

The manuscript now states that the demonstration uses two ex ante construct protocols.

### Revenue Recognition Risk

The protocol asks whether retrieved public filing text and XBRL materials support source-traceable analysis of:

1. revenue policies,
2. contract liabilities,
3. variable consideration,
4. refund or return obligations,
5. disaggregation,
6. performance-obligation timing.

Assertion relevance is bounded to occurrence, completeness, accuracy, cut-off, and classification. The manuscript now explicitly states that the demonstration does not test whether revenue is materially misstated.

### Inventory Valuation Assertion

The protocol asks whether retrieved public filing text and XBRL materials support source-traceable analysis of:

1. inventory balances,
2. reserves,
3. write-downs,
4. costing methods,
5. obsolescence cues,
6. related reported amounts.

Assertion relevance is bounded to valuation, existence, completeness, and presentation. The manuscript now explicitly states that the demonstration does not test physical inventory existence, realizable value, or management bias.

## Supplement Revision

Added:

1. **Appendix Table A2. Ex Ante Construct Protocol: Revenue Recognition Risk**
2. **Appendix Table A3. Ex Ante Construct Protocol: Inventory Valuation Assertion**

Each table specifies:

1. construct label,
2. audit-standard anchor,
3. primary account/disclosure area,
4. assertion relevance,
5. expected text retrieval,
6. expected XBRL retrieval,
7. claims supported by current evidence,
8. claims not supported by current evidence,
9. valid claim example,
10. invalid or overreaching claim example,
11. coding boundary.

## Tables Packet Revision

Table 6 now includes demonstration-specific rows for:

1. revenue recognition risk,
2. inventory valuation assertion.

The "what not to claim" column explicitly states that retrieved public filing/XBRL materials do not prove:

1. revenue misstatement,
2. GAAP noncompliance,
3. fraud,
4. physical inventory existence,
5. reserve adequacy,
6. net realizable value,
7. management bias,
8. audit evidence sufficiency.

## QA

QA searches confirmed:

1. `PCAOB 2024a`, `PCAOB 2024b`, and `PCAOB 2024c` are cited in the manuscript and listed in references.
2. Appendix Tables A2 and A3 are present in the supplement.
3. The manuscript appendix listing now identifies Appendix A as including ex ante construct protocols.
4. Table 6 includes both demonstration constructs.
5. Audit evidence sufficiency language appears as boundary framing, not as a completed claim.

## Sources Checked

Official PCAOB sources were checked before adding the audit-standard anchors:

1. PCAOB AS 1105, Audit Evidence: https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105
2. PCAOB AS 2110, Identifying and Assessing Risks of Material Misstatement: https://pcaobus.org/Standards/Auditing/Pages/AS2110.aspx
3. PCAOB AS 2301, The Auditor's Responses to the Risks of Material Misstatement: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2301

## Reviewer Risk Reduced

This revision directly addresses:

1. Reviewer 1 Major Comment 3: audit constructs were too broadly specified.
2. Reviewer 2 Major Comment 5: audit positioning exceeded what public filing data can support.
3. Reviewer concern that source traceability was being validated without construct relevance being specified first.

## Remaining Boundary

This revision defines construct protocols and boundaries. It does not add audit-domain expert coding or audit evidence sufficiency testing. Those remain separate requirements if the paper later makes stronger audit-judgment or model-performance claims.

## SR-03 / SR-04 Status

`SR-03` and `SR-04` are complete. The next closely related workstream is `SR-05`: build the XBRL concept/relation coverage diagnostic for the two constructs.
