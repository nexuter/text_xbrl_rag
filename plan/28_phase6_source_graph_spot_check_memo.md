# Phase 6 Source and Graph Spot-Check Memo

## Purpose

This memo documents source verification for the selected manuscript examples in Table X.

The purpose is to support reviewer confidence that the demonstration examples are traceable to retrieved filing text and extracted Inline XBRL data rather than polished post-hoc interpretation.

## Materials Checked

Selected examples:

- `E01`: Starbucks inventory hybrid, claim `C058`
- `E02`: Nike revenue hybrid, claim `C013`
- `E03`: Nike revenue hybrid, claim `C014`
- `E04`: Nike revenue LLM-only baseline, claim `C016`
- `E05`: Target inventory hybrid, claim `C090`

Files checked:

- `data/processed/coding/selected_manuscript_examples_prelim.csv`
- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/retrieval_contexts/sbux_inventory_hybrid_context.txt`
- `data/processed/retrieval_contexts/nke_revenue_hybrid_context.txt`
- `data/processed/text_chunks/text_chunks.csv`
- `data/processed/xbrl_facts/xbrl_facts.csv`
- `data/raw_sec/sbux_2025_10k/sbux-20250928_htm.xml`
- `data/raw_sec/nke_2025_10k/nke-20250531_htm.xml`
- `data/raw_sec/tgt_2025_10k/tgt-20250201_htm.xml`

Detailed check table:

- `data/processed/coding/selected_source_spot_check.csv`

## Spot-Check Results

### E01: Starbucks Inventory Reserve

Claim:

> As of September 28, 2025, inventory reserves were $56.6 million.

Text source check:

- Source ID: `T-SBUX-INVENTORY-015`
- Processed file: `data/processed/text_chunks/text_chunks.csv`
- Source file: `sbux-20250928.htm`
- Result: verified

The extracted text chunk states that inventories are measured at the lower of cost or net realizable value and that inventory reserves were $56.6 million and $58.0 million as of September 28, 2025 and September 29, 2024, respectively.

XBRL source check:

- Source ID: `F-SBUX-0034`
- Processed file: `data/processed/xbrl_facts/xbrl_facts.csv`
- Raw file: `data/raw_sec/sbux_2025_10k/sbux-20250928_htm.xml`
- Raw location: line 8520
- Concept: `InventoryValuationReserves`
- Value: `56600000`
- Context: `c-33`
- Period: `instant:2025-09-28`
- Unit: `iso4217:USD`
- Result: verified

Reviewer interpretation:

This is a defensible integrated factual example because the narrative disclosure and XBRL fact refer to the same reported amount and period.

### E02: Nike Refund Liability Increase

Claim:

> The increase in the current refund liability from $799 million (as of 2024-05-31) to $1.277 billion (as of 2025-05-31) presents a risk cue for the valuation assertion of revenue.

XBRL source check:

- Source IDs: `F-NKE-0253`, `F-NKE-0252`
- Processed file: `data/processed/xbrl_facts/xbrl_facts.csv`
- Raw file: `data/raw_sec/nke_2025_10k/nke-20250531_htm.xml`
- Raw locations: lines 7798 and 7799
- Concept: `ContractWithCustomerRefundLiabilityCurrent`
- Values: `1277000000` and `799000000`
- Contexts: `c-9` and `c-10`
- Periods: `instant:2025-05-31` and `instant:2024-05-31`
- Unit: `iso4217:USD`
- Result: verified

Reviewer interpretation:

The numerical comparison is graph-valid as a reported XBRL fact comparison. The audit implication remains inferential and should be presented as a risk cue, not as evidence of misstatement or audit evidence sufficiency.

### E03: Nike Digital Commerce Platform Risk

Claim:

> The stated risk that failures in providing reliable, secure, and user-friendly digital commerce platforms could result in the loss of digital commerce sales indicates a risk cue for the completeness and occurrence assertions of revenue.

Text source check:

- Source ID: `T-NKE-REVENUE-021`
- Processed file: `data/processed/text_chunks/text_chunks.csv`
- Source file: `nke-20250531.htm`
- Result: verified

The extracted text chunk states that failure to provide effective, reliable, secure, and user-friendly digital commerce platforms could result in loss of digital commerce and other sales, harm reputation, and materially affect business and results of operations.

Reviewer interpretation:

The business-risk language is text-supported. The mapping to completeness and occurrence is a professional audit inference and should be coded as partially text-supported, not directly stated by the filing.

### E04: Nike LLM-Only Baseline

Claim:

> The provided context is insufficient to identify any audit-relevant risk cues or assertion-mapping considerations for revenue recognition for Nike, Inc. for the specified period.

Baseline source check:

- Context file: `data/processed/retrieval_contexts/nke_revenue_llm_only_context.txt`
- Result: verified

The baseline context provides no retrieved filing evidence. The model's refusal to provide filing-specific risk cues is consistent with the prompt and supports the traceability diagnostic.

### E05: Target Net Inventory

Claim:

> As of February 1, 2025, Target Corporation's net inventory was $12,740,000,000.

XBRL source check:

- Source ID: `F-TGT-0007`
- Processed file: `data/processed/xbrl_facts/xbrl_facts.csv`
- Raw file: `data/raw_sec/tgt_2025_10k/tgt-20250201_htm.xml`
- Raw location: line 2720
- Concept: `InventoryNet`
- Value: `12740000000`
- Context: `c-6`
- Period: `instant:2025-02-01`
- Unit: `iso4217:USD`
- Result: verified

Reviewer interpretation:

The claim is graph-valid as a reported XBRL fact. However, it does not integrate the available Target inventory narrative context, so it is useful as an additional cautionary example that hybrid retrieval can produce effectively XBRL-only claims.

## Reviewer-Level Assessment

The selected examples pass source and graph spot-checks.

Strengths:

- Table X examples are tied to actual LLM output claims.
- Text source IDs trace to extracted filing text chunks.
- XBRL fact IDs trace to processed fact rows and raw Inline XBRL tags.
- The selected examples now include all three demonstration filers.
- The LLM-only example traces to an explicitly empty retrieval context.
- The spot-check supports the paper's claim that retrieval-environment validity requires claim-level source mapping.

Important limitations:

- The text source files are HTML filings with minified or long-line structure, so line-number citation in raw HTML is less useful than chunk-ID citation.
- The spot-check verifies selected examples only; it does not validate all 94 segmented claims.
- Audit-valid coding still requires expert review.
- XBRL fact verification does not turn XBRL into independent audit evidence.

## Manuscript-Ready Statement

The following sentence can be used in the demonstration section or appendix:

> We spot-checked the selected examples against the extracted text chunks, processed XBRL fact table, and raw Inline XBRL files. The selected XBRL facts for Starbucks inventory reserves and Nike refund liabilities trace to the original Inline XBRL tags, and the selected narrative risk cues trace to extracted filing text chunks. These checks support traceability of the examples but do not replace expert coding of audit-valid inference.

## Next Step

The next step is to conduct a final reviewer-style assessment of the demonstration package:

- Does the demonstration now satisfy the Phase 6 acceptance criteria?
- Are the selected examples too narrow or too favorable?
- Is the source verification enough for a methodology paper?
- What must be moved to the appendix versus main text?
