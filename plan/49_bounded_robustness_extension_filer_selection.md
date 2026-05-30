# Bounded Robustness Extension Filer Selection

## Purpose

This memo implements the recommendation in `plan/48_demonstration_scope_generalizability_assessment.md`: add a six-filer bounded robustness extension to the current three-filer deep demonstration.

The goal is not statistical representativeness. The goal is maximum-variation methodological sampling: show that retrieval-environment validity can be evaluated across different reporting environments while keeping the paper clearly positioned as an AJPT methodology paper.

## Decision

Proceed with a six-filer bounded robustness extension.

The current three filers remain the main-text deep demonstration:

| Current Main Demonstration Filer | Role |
|---|---|
| Nike | Familiar consumer products/apparel case with revenue and inventory relevance |
| Starbucks | Familiar consumer-facing food/beverage case with revenue, stored value, and inventory relevance |
| Target | Familiar retailer with strong inventory and sales relevance |

The six additional filers should be used primarily for appendix-level robustness diagnostics, not for full model-performance claims.

## Selected Six Additional Filers

The selected additional filers are:

| Ticker | Company | Industry / Setting | Size / Complexity Role | Construct Fit | SEC CIK | Latest 10-K Accession Verified | Report Date | Primary Document |
|---|---|---|---|---|---|---|---|---|
| WMT | Walmart Inc. | Mega-scale retail | Very large retailer; inventory-heavy; broad store and ecommerce operations | Strong revenue and inventory fit | 0000104169 | 0000104169-26-000055 | 2026-01-31 | wmt-20260131.htm |
| HD | Home Depot, Inc. | Specialty retail / home improvement | Large specialty retailer; inventory-heavy but operationally distinct from Target/Walmart | Strong revenue and inventory fit | 0000354950 | 0001628280-26-019436 | 2026-02-01 | hd-20260201.htm |
| CAT | Caterpillar Inc. | Industrial manufacturing | Manufacturing and equipment setting; inventory and cost structure more complex than retail | Strong inventory; moderate-to-strong revenue fit | 0000018230 | 0000018230-26-000008 | 2025-12-31 | cat-20251231.htm |
| PFE | Pfizer Inc. | Pharma / healthcare products | Product lifecycle, reserves, regulatory context, and healthcare-sector reporting | Moderate-to-strong inventory; strong revenue fit | 0000078003 | 0000078003-26-000026 | 2025-12-31 | pfe-20251231.htm |
| MSFT | Microsoft Corp. | Technology / software / cloud | Strong revenue-recognition and deferred-revenue setting; weak inventory boundary case | Strong revenue; weak inventory boundary | 0000789019 | 0000950170-25-100235 | 2025-06-30 | msft-20250630.htm |
| CROX | Crocs, Inc. | Mid-size consumer products / footwear | Smaller and less complex than mega-cap filers; familiar product business | Strong inventory; moderate-to-strong revenue fit | 0001334036 | 0001334036-26-000006 | 2025-12-31 | crox-20251231.htm |

Metadata was verified from SEC submissions metadata on May 29, 2026.

## Selection Logic

### Why Walmart

Walmart adds a mega-scale retailer that is familiar to readers and has strong inventory and revenue relevance. It provides a scale contrast with Target and can test whether the framework remains useful when disclosures and XBRL facts are large and operationally broad.

Expected contribution:

- selection validity under high-volume retail reporting;
- traceability of sales and inventory facts;
- comparison against Target without claiming retail representativeness.

### Why Home Depot

Home Depot adds a specialty retail setting that is intuitive but distinct from general merchandise retail. Inventory is central, and sales/revenue recognition remains straightforward enough for readers to interpret.

Expected contribution:

- inventory-heavy retrieval in a different retail business model;
- stronger public understandability than many industrial or niche firms;
- useful comparison for text versus XBRL retrieval in merchandise-heavy reporting.

### Why Caterpillar

Caterpillar adds industrial manufacturing complexity. This is important because the current three filers are consumer-facing and do not fully stress inventory, cost, and manufacturing-related reporting structures.

Expected contribution:

- representation validity for inventory and cost-related XBRL concepts;
- relation retrieval challenges in a manufacturing context;
- boundary against overly consumer-retail-centered conclusions.

### Why Pfizer

Pfizer adds a healthcare/pharma product setting. Pharma can introduce inventory reserves, product lifecycle issues, regulatory risk, and revenue complexity, while still being understandable to readers.

Expected contribution:

- industry variation outside retail/apparel;
- inventory valuation and product reserve context;
- revenue and product-risk narratives that may require text-XBRL integration.

### Why Microsoft

Microsoft adds a technology/software/cloud setting where revenue recognition and deferred revenue are highly relevant, but inventory is not a natural focal construct. This is valuable as a boundary case.

Expected contribution:

- strong test of revenue retrieval and contract-liability facts;
- weak-fit inventory case that demonstrates construct-to-retrieval matching;
- prevents the paper from implying that the same constructs fit all industries.

### Why Crocs

Crocs adds a mid-size consumer products/apparel case that remains easy for readers to understand. It helps address the concern that all cases are mega-cap filers with mature reporting infrastructures.

Expected contribution:

- firm-size contrast relative to Nike, Walmart, Microsoft, Pfizer, and Caterpillar;
- familiar product/inventory setting;
- additional apparel/consumer-product comparison without relying only on Nike.

## Backup Filers

The following backup filers were considered and can be used if download, parsing, or construct-fit issues arise.

| Ticker | Company | Reason to Keep as Backup | SEC CIK | Latest 10-K Accession Verified | Report Date | Primary Document |
|---|---|---|---|---|---|---|
| DE | Deere & Co. | Industrial/manufacturing alternative to CAT | 0000315189 | 0001104659-25-122321 | 2025-11-02 | de-20251102x10k.htm |
| COST | Costco Wholesale Corp. | Retail alternative to WMT or HD | 0000909832 | 0000909832-25-000101 | 2025-08-31 | cost-20250831.htm |
| TSCO | Tractor Supply Co. | Specialty retail, somewhat smaller than mega retailers | 0000916365 | 0000916365-26-000014 | 2025-12-27 | tsco-20251227.htm |
| DECK | Deckers Outdoor Corp. | Consumer products/apparel alternative to CROX | 0000910521 | 0001628280-26-037664 | 2026-03-31 | deck-20260331.htm |
| YETI | YETI Holdings, Inc. | Mid-size consumer products alternative | 0001670592 | 0001670592-26-000013 | 2026-01-03 | yeti-20260103.htm |
| WDAY | Workday, Inc. | Software/SaaS alternative to MSFT | 0001327811 | 0001327811-26-000014 | 2026-01-31 | wday-20260131.htm |
| TSLA | Tesla, Inc. | Familiar manufacturing/technology boundary case | 0001318605 | 0001628280-26-003952 | 2025-12-31 | tsla-20251231.htm |
| AZO | AutoZone Inc. | Specialty retail / automotive inventory alternative | 0000866787 | 0001104659-25-102611 | 2025-08-30 | azo-20250830x10k.htm |

## Why Not a Larger Sample

A larger accounting empirical sample would create expectations that are not aligned with the paper's methodology contribution:

1. formal sampling theory;
2. statistical inference;
3. population-level failure-mode prevalence;
4. coder reliability across a large claim set;
5. performance comparisons across industries and models.

Those expectations would shift the paper away from AJPT methodology and toward an empirical benchmark. The six-filer extension is a better fit because it increases external plausibility while preserving deep traceability.

## Recommended Work Scope for the Extension

### Step 1: Retrieval Diagnostics for All Six Additional Filers

For each additional filer, collect:

1. filing metadata;
2. text chunk count;
3. revenue-related text chunk count;
4. inventory-related text chunk count;
5. XBRL fact count;
6. revenue-related XBRL fact count;
7. inventory-related XBRL fact count;
8. XBRL relation path count;
9. extension concept count, if feasible;
10. whether each construct has enough evidence for text, XBRL, and hybrid retrieval.

This step is required.

### Step 2: Limited LLM Runs

Do not run the full four-condition design for every additional filer unless time permits.

Recommended minimum:

- one construct per additional filer;
- three retrieval conditions: text, XBRL, and hybrid;
- no LLM-only baseline unless pretraining contamination or public familiarity becomes central.

Recommended construct assignment:

| Filer | Primary Construct for Extension Run | Reason |
|---|---|---|
| WMT | inventory | Inventory-heavy retail benchmark |
| HD | inventory | Specialty retail inventory comparison |
| CAT | inventory | Industrial manufacturing inventory complexity |
| PFE | inventory | Product/reserve/regulatory setting |
| MSFT | revenue | Strong deferred revenue / contract-liability setting |
| CROX | inventory | Mid-size consumer product inventory setting |

This produces 18 additional LLM outputs if text, XBRL, and hybrid conditions are run for six filer-construct pairs.

### Step 3: Limited Claim Coding

Code only the top 3 to 5 claims per output for:

1. text support;
2. graph validity;
3. integrated correctness;
4. failure mode;
5. audit-validity only as illustrative unless expert-reviewed.

Expected additional claim count:

Approximately 54 to 90 claims.

This is enough to show that the protocol can be applied beyond the three main cases without turning the paper into a large benchmark.

## How the Extension Should Appear in the Manuscript

### Main Text

Keep Nike, Starbucks, and Target as the main demonstration.

Add one paragraph:

> To assess whether the framework applies beyond the three deep cases, we conduct a bounded robustness extension using six additional filers selected for variation in industry, scale, reporting complexity, and construct fit. This extension is not designed to estimate population-level performance. It tests whether the retrieval-environment validity protocol remains applicable across different reporting environments.

### Appendix

Report the extension in appendix tables:

1. filer selection table;
2. retrieval diagnostics table;
3. limited LLM/coding summary;
4. boundary-case notes.

## Reviewer-Facing Claim

With the six-filer extension, the paper can claim:

> The framework was illustrated in three deep cases and stress-tested through a bounded six-filer extension spanning retail, specialty retail, industrial manufacturing, pharma, software/cloud, and mid-size consumer products.

The paper still should not claim:

- population-level prevalence;
- retrieval-method superiority;
- model performance;
- audit-valid conclusion quality without expert coding.

## Implementation Implications

The current scripts use hard-coded filer lists in:

- `scripts/sec_download.py`
- `scripts/extract_demo_data.py`
- `scripts/build_retrieval_contexts.py`

Before downloading the additional filers, refactor or carefully extend the filer configuration so the main three-case demonstration and the robustness extension can be distinguished in outputs.

Recommended approach:

1. Create a shared JSON filer manifest.
2. Add a `sample_role` field:
   - `main_deep_case`
   - `bounded_extension`
   - `backup`
3. Add fields for:
   - ticker;
   - company;
   - CIK;
   - accession;
   - report date;
   - primary document;
   - folder;
   - primary construct for extension.
4. Update scripts to read from the manifest and optionally filter by sample role.

## Final Decision

Add the six-filer bounded robustness extension with WMT, HD, CAT, PFE, MSFT, and CROX.

This is the best balance between reviewer credibility and methodological focus.
