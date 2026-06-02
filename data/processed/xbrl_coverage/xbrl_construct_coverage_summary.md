# XBRL Construct Coverage Diagnostics

## Purpose

This diagnostic links the ex ante revenue and inventory construct protocols to the XBRL facts and relation paths actually supplied in the retrieval environment. It is a retrieval-environment validity diagnostic, not a model-performance or final audit-judgment test.

## Output Files

- Filer-level coverage: `data/processed/xbrl_coverage/construct_coverage_by_filer.csv`
- Concept-family coverage: `data/processed/xbrl_coverage/construct_coverage_by_family.csv`

## Filer-Level Summary

- Construct-filer cells reviewed: `18`
- Complete expected-family coverage cells: `3`
- Partial expected-family coverage cells: `15`

| Ticker | Construct | Covered Families | Missing Families | Status |
|---|---|---:|---|---|
| CAT | inventory | 4/5 | inventory_movements | partial_family_coverage |
| CAT | revenue | 4/5 | refunds_returns_or_variable_consideration | partial_family_coverage |
| CROX | inventory | 4/5 | inventory_components | partial_family_coverage |
| CROX | revenue | 5/5 | None | complete_family_coverage |
| HD | inventory | 2/5 | inventory_components; inventory_movements; valuation_reserve_or_obsolescence | partial_family_coverage |
| HD | revenue | 4/5 | refunds_returns_or_variable_consideration | partial_family_coverage |
| MSFT | inventory | 3/5 | inventory_components; valuation_reserve_or_obsolescence | partial_family_coverage |
| MSFT | revenue | 3/5 | receivables_or_collectibility; refunds_returns_or_variable_consideration | partial_family_coverage |
| NKE | inventory | 5/5 | None | complete_family_coverage |
| NKE | revenue | 4/5 | contract_liability_or_deferred_revenue | partial_family_coverage |
| PFE | inventory | 4/5 | inventory_movements | partial_family_coverage |
| PFE | revenue | 2/5 | contract_liability_or_deferred_revenue; receivables_or_collectibility; refunds_returns_or_variable_consideration | partial_family_coverage |
| SBUX | inventory | 3/5 | cost_flow_or_cogs; inventory_movements | partial_family_coverage |
| SBUX | revenue | 3/5 | receivables_or_collectibility; refunds_returns_or_variable_consideration | partial_family_coverage |
| TGT | inventory | 4/5 | inventory_components | partial_family_coverage |
| TGT | revenue | 5/5 | None | complete_family_coverage |
| WMT | inventory | 2/5 | inventory_components; inventory_movements; valuation_reserve_or_obsolescence | partial_family_coverage |
| WMT | revenue | 4/5 | refunds_returns_or_variable_consideration | partial_family_coverage |

## Family-Level Summary

| Construct | Concept Family | Filers With Any Hit | Fact-Hit Filers | Path-Hit Filers |
|---|---|---:|---|---|
| revenue | revenue_or_sales_amount | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| revenue | contract_liability_or_deferred_revenue | 7/9 | CAT; CROX; HD; MSFT; SBUX; TGT; WMT | CAT; CROX; SBUX; TGT |
| revenue | refunds_returns_or_variable_consideration | 3/9 | CROX; NKE | NKE; TGT |
| revenue | receivables_or_collectibility | 6/9 | CROX; HD; NKE; WMT | CAT; TGT |
| revenue | disaggregation_or_customer_dimension | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| inventory | inventory_balance | 9/9 | CAT; CROX; HD; MSFT; NKE; PFE; SBUX; TGT; WMT | CAT; CROX; HD; NKE; PFE; SBUX; TGT; WMT |
| inventory | inventory_components | 4/9 | CAT; NKE; PFE; SBUX | CAT; NKE; PFE; SBUX |
| inventory | valuation_reserve_or_obsolescence | 6/9 | CAT; CROX; NKE; PFE; SBUX; TGT | CAT; CROX; NKE; PFE; SBUX; TGT |
| inventory | cost_flow_or_cogs | 8/9 | CAT; CROX; HD; MSFT; NKE; TGT; WMT | CROX; HD; NKE; PFE; TGT; WMT |
| inventory | inventory_movements | 4/9 | CROX; MSFT; NKE; TGT | CROX; NKE; TGT |

## Interpretation Boundary

These counts show whether the retrieval protocol surfaced expected XBRL concept families before LLM outputs are interpreted. They do not show that the LLM made correct audit judgments, that a reported balance has sufficient appropriate audit evidence, or that unobserved concept families are absent from the filing. Future Tier 2 model-validation studies should combine this diagnostic with expert coding, retrieval sensitivity tests, and model-output performance analysis.
