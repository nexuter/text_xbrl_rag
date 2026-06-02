# Major Comment 3 Coding Independence Audit

Date: 2026-06-01

## Reviewer Comment Reviewed

Major Comment 3 argues that the paper's core coding-based evidence is not yet sufficiently independent. The reviewer is concerned that most coding remains author-generated, the 120-claim independent coding sample is partial and hybrid-weighted, and the most judgment-laden audit-valid / audit-boundary dimension has not been independently validated by audit-domain experts.

## Bottom-Line Assessment

The issue is partially addressed, but not by completing the literal expert-audit-coding path requested by the reviewer. The revision instead takes a claim-narrowing path:

- independently validate the central protocol variables that support the paper's methodological claim: claim segmentation, claim kind, evidence-use type, text-supported correctness, graph-valid correctness, and integrated correctness;
- avoid treating audit-boundary diagnostics as final audit-valid or audit-judgment outcomes;
- disclose that audit-domain expert coding is required for stronger audit-judgment, model-performance, or retrieval-superiority claims.

This is defensible only if the response letter and manuscript clearly state that the paper is a Tier 1 retrieval-methodology / protocol-validation paper, not a completed audit-valid model-performance validation study.

## Actionable Fix Status

| Reviewer Request | Current Revision Response | Status |
|---|---|---|
| Add independent audit-domain coding for audit-valid dimension | Not completed. The revision narrows audit-boundary notes to qualitative preliminary diagnostics and states that expert audit-domain coding is a Tier 2 requirement | Not literally addressed; defensible through narrowed claims |
| Expand independent coding sample or apply independent coding to full set for core variables | Independent sample covers 120 of 281 claims, including all 89 hybrid claims and 31 non-hybrid anchors | Partially addressed |
| Coders blinded to condition | Not completed. Condition labels remained visible because source availability is needed for source-use and integrated-correctness coding | Disclosed limitation |
| Report disagreement patterns, not only agreement statistics | Added main-text disagreement-pattern sentence and supplement detail: 22 variable-level disagreements, including 3 claim-kind, 3 text-support, 1 graph-valid, and 15 confidence-code disagreements | Addressed |
| Reduce concern that author interpretation drives main result | Independent coding shows 100.0 percent agreement for evidence-use type and integrated correctness, the variables supporting the hybrid-label-versus-claim-use argument | Substantially addressed for source-use/integration; not for audit-valid judgments |

## Evidence In The Revised Package

| Evidence Item | Location | Interpretation |
|---|---|---|
| 120-claim independent coding sample | Manuscript Section VII; Appendix F4-F5 | Validates measurement consistency for central protocol variables |
| All 89 hybrid claims included | Appendix F4A | Directly tests the paper's central question: whether hybrid condition labels correspond to integrated text-XBRL claim use |
| 31 non-hybrid anchors | Appendix F4A | Provides LLM-only, text-only, and XBRL-only anchors for coding source-use and correctness outside hybrid claims |
| Source-use type agreement = 100.0 percent | Manuscript Section VII; Appendix F5 | Supports the claim-level source-use diagnostic |
| Integrated correctness agreement = 100.0 percent | Manuscript Section VII; Appendix F5 | Supports the claim that integration must be measured at claim level |
| Disagreement pattern added | Manuscript Section VII; Appendix F5 | Shows disagreements are boundary cases, not a systematic source-use/integration problem |
| Gate decision for audit-boundary validation | Appendix F4B; plan/125 and plan/126 | Prevents preliminary audit-boundary notes from being overclaimed as expert audit-valid evidence |

## Remaining Reviewer Risk

The likely follow-up concern is that the authors did not adopt the reviewer's strongest recommendation: independent audit-domain expert coding for audit-valid judgments. The response should be candid:

- We agree with the reviewer that audit-valid correctness requires audit-domain expert validation.
- We therefore removed or narrowed audit-valid performance language rather than claiming that the current coders validate audit judgment quality.
- The paper's empirical claim rests on independently validated source-use and integration variables, not on audit-valid performance scores.
- Appendix F4B explicitly defines audit-domain expert coding as a Tier 2 requirement for future studies or stronger claims.

## Response-Letter Position

The response should not say "we fully validated audit-valid correctness." A safer response is:

> We agreed with the reviewer that the original framing could overstate the audit-valid dimension. In the revision, we narrowed the claim: audit-boundary notes are retained only as qualitative diagnostics, while the independent coding evidence is used to support the central retrieval-methodology variables, especially evidence-use type and integrated correctness. We also added disagreement-pattern reporting and explicitly identify audit-domain expert coding as required for Tier 2 model-performance or audit-judgment studies.

## Reviewer-Facing Follow-Up Questions To Preempt

1. Why were coders not blinded to condition?
   - Because source availability and retrieval condition are needed to code whether a claim used available text/XBRL evidence and whether it integrated source layers. The exercise validates measurement consistency, not treatment effects.

2. Why is the sample hybrid-weighted?
   - Because the central methodological claim concerns whether hybrid condition labels produce integrated claim-level evidence use. Including all 89 hybrid claims directly covers that claim, while 31 non-hybrid anchors calibrate the coding scale outside hybrid contexts.

3. Why not independently code all 281 claims?
   - The 120-claim validation sample is adequate for Tier 1 protocol validation of the core variables, but the manuscript should not use it for prevalence, model-performance, or audit-judgment claims. Full-set or broader expert coding is required for Tier 2 studies.

4. Does the coding establish audit-valid correctness?
   - No. It establishes source-use and integration measurement reliability. Audit-boundary notes are qualitative diagnostics and require audit-domain expert validation before being treated as audit-valid outcomes.

## Implementation Log

- Added a main-text disagreement-pattern sentence in Section VII.
- Revised Appendix F4A to separate core independently coded variables from qualitative audit-boundary notes.
- Expanded Appendix F5 reconciliation note to report variable-level disagreement counts and the substantive location of disagreements.
