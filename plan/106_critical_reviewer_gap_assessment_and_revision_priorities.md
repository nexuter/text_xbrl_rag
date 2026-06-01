# Critical Reviewer Gap Assessment And Revision Priorities

## Purpose

This note records a deliberately critical AJPT-reviewer-style assessment of the current submission package after the independent coding, context-volume diagnostic, source-environment perturbation diagnostic, and hybrid integration mechanism diagnostic were added.

The assessment focuses on whether a reviewer could still argue that the manuscript's evidence, coding, or framing is internally inconsistent or insufficient for publication as an AJPT methodology paper.

## Overall Reviewer Verdict

The paper is much closer to an acceptably bounded methodology contribution than the earlier version. The strongest elements are now:

- a clearly named methodological construct: retrieval-environment validity;
- an AJPT-relevant framing around research design and variable construction;
- a nine-filer protocol-validation package with 72 outputs and 281 coded claims;
- independent two-coder validation for the central claim-level protocol variables;
- context-volume and source-environment perturbation diagnostics;
- a hybrid integration mechanism diagnostic showing why condition labels are insufficient.

However, I would not yet call the package fully clean from a reviewer standpoint. The most important remaining issue is not the lack of more data. It is an internal measurement-scale inconsistency around integrated correctness.

## Highest-Risk Issue: Integrated-Correctness Scale Inconsistency

### Reviewer Concern

The independent coder instructions now correctly define ordinary non-integration as `0`, not `NA` or partial integration. The manuscript says:

> ordinary non-integration is coded as `0`, not `NA`

But several manuscript/supporting artifacts still carry the older preliminary author scale in which one-source hybrid claims are coded as `0.5` for integrated diagnostic:

- Table 8 in `submission/Tables_and_Figures.md` reports `Integrated Diagnostic = 0.5` for one-source hybrid claims:
  - E02: XBRL-only within hybrid;
  - E03: text-only within hybrid;
  - E05: XBRL-only within hybrid.
- Appendix F3 and H5 report `Integrated Mean` values around `0.50` to `0.60`, which imply partial integration is common.
- The new mechanism diagnostic says only 8 of 89 hybrid claims have an integrated text-XBRL bridge.

These statements can be reconciled conceptually, but a reviewer should not have to infer the reconciliation. As currently written, the package risks appearing to use two different definitions of integrated correctness.

### Why This Matters

This issue touches the paper's central contribution. The main claim is that hybrid condition labels do not guarantee integrated evidence use. If non-integrated one-source hybrid claims still receive `0.5` in selected tables, the measurement protocol appears unstable.

### Recommended Fix

This should be treated as a P0 revision before submission.

1. Harmonize all integrated-correctness reporting around the recoded rule:
   - `1`: text and XBRL jointly used in an inferential bridge;
   - `0.5`: both text and XBRL appear but are weakly connected or juxtaposed;
   - `0`: text-only, XBRL-only, no-source, or non-integrated claims.

2. Update Table 8:
   - E01 remains `1`;
   - E02 should be `0`;
   - E03 should be `0`;
   - E04 remains `NA` or `0` depending on whether the table treats LLM-only as not applicable or non-integrated;
   - E05 should be `0`.

3. Replace Appendix F3/H5 `Integrated Mean` with a less ambiguous measure:
   - preferred: `Integrated Bridge Claims`;
   - or `Integrated Bridge Share`;
   - optionally paired with `Text-only Hybrid Claims` and `XBRL-only Hybrid Claims`.

4. Recompute or regenerate any summary files that currently average old `integrated_prelim = 0.5` one-source claims.

5. If the older preliminary scale must be preserved for provenance, move it to deprecated/pilot artifacts and state that manuscript evidence uses the recoded integrated-correctness rule.

## Remaining Reviewer Risks After P0 Fix

| Risk | Severity | Reviewer Objection | Recommended Treatment |
|---|---|---|---|
| Output-level sensitivity absent | Medium | Context-volume and source perturbation stop before model inference | Keep as explicit Tier 2 boundary; do not claim output robustness |
| Source perturbation may look mechanical | Medium-Low | Top-3/top-8 Jaccard is partly determined by top-k nesting | Reframe as source-budget perturbation rather than strong stability evidence |
| Audit-valid coding remains preliminary | Medium-Low | Audit-valid scores lack expert validation | Keep audit-valid out of aggregate evidence; use expert coding only for future Tier 2 |
| Boundary statements may crowd out positive contribution | Low-Medium | Paper repeatedly says what it does not claim | Add a concise positive takeaway after each boundary-heavy section |
| Main text and supplement density | Low-Medium | Too many diagnostics may obscure core contribution | Use roadmap language to direct reviewers to the most important artifacts |
| DOCX visual QA incomplete | Low | Latest PNG render QA unavailable | Preserve structural QA and disclose renderer boundary in audit note |

## Recommended Next Revision Sequence

### Step 1: Fix Integrated-Correctness Consistency

Update the data summaries, main selected examples, appendix summaries, and DOCX files so integrated correctness uses one rule everywhere. This is the highest-value improvement because it removes a direct internal inconsistency.

### Step 2: Reframe Perturbation Diagnostic Language

Where the manuscript says the perturbation diagnostic supports "stability," use more careful wording:

> source-budget and source-composition transparency

or:

> retrieval-stage perturbation transparency

This avoids overstating the diagnostic as a full retrieval-stability test.

### Step 3: Add A Short Positive Contribution Paragraph

After the demonstration or in the discussion, add a short paragraph stating what the paper now positively establishes:

> The package demonstrates that audit researchers can preserve the retrieval-created information environment, convert LLM outputs into claim-level evidence-use variables, validate central coding categories with independent coders, and diagnose whether hybrid retrieval produces actual integration or one-layer use.

This will help counter the possible reviewer impression that the paper is mostly boundary conditions.

### Step 4: Preserve Tier 2 Boundary

Do not add model-output robustness language unless a new output-level sensitivity exercise is actually run. Keep matched-budget, evidence-order, prompt-variation, and model-variation checks as Tier 2 requirements.

## Acceptability Assessment

If the integrated-correctness inconsistency is fixed, I would view the paper as plausibly acceptable as an AJPT methodological paper, subject to editorial judgment and normal refinement. Without that fix, I would likely recommend another revision because the central measurement concept appears internally inconsistent across the manuscript, appendix, and coding materials.

The paper does not need to become a full model-validation study to be publishable. It does need to make the coding rule, tables, and diagnostic summaries internally consistent.

## Files Likely Requiring Update

- `submission/Tables_and_Figures.md`
- `submission/Manuscript_Retrieval_as_Research_Design.md`
- `submission/Online_Supplement_Appendix.md`
- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv`
- `data/processed/coding/coding_summary_by_condition*.csv`
- `data/processed/coding/claim_coding_summary*.md`
- `data/processed/coding/manuscript_selected_claim_table.md`
- corresponding files inside `submission/replication_package/`
- regenerated DOCX files and replication zip

## Bottom Line

The main remaining improvement is not to add more analysis. It is to make the integrated-correctness construct internally clean. Once one-source hybrid claims are consistently treated as non-integrated rather than partially integrated, the new hybrid mechanism diagnostic becomes a strong reviewer-facing asset rather than a potential contradiction.
