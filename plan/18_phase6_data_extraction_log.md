# Phase 6 Data Download and Extraction Log

## Purpose

This file records the first execution step for the Phase 6 methodological demonstration: downloading SEC filing materials and extracting candidate text chunks, XBRL facts, and XBRL relation paths.

This is an execution log, not a final retrieval experiment. The extracted data are intended to support later text retrieval, XBRL relational retrieval, hybrid context construction, and claim-level correctness coding.

## Downloaded Filings

| Filer | CIK | Accession | Local Folder | Main 10-K HTML | Extracted XBRL Instance |
|---|---:|---|---|---|---|
| Nike, Inc. | 0000320187 | 0000320187-25-000047 | `data/raw_sec/nke_2025_10k/` | `nke-20250531.htm` | `nke-20250531_htm.xml` |
| Starbucks Corporation | 0000829224 | 0000829224-25-000114 | `data/raw_sec/sbux_2025_10k/` | `sbux-20250928.htm` | `sbux-20250928_htm.xml` |
| Target Corporation | 0000027419 | 0000027419-25-000018 | `data/raw_sec/tgt_2025_10k/` | `tgt-20250201.htm` | `tgt-20250201_htm.xml` |

Downloaded materials include:

- SEC filing detail page
- complete submission text file
- primary 10-K iXBRL HTML
- extracted XBRL instance XML
- extension taxonomy schema
- calculation linkbase
- definition linkbase
- label linkbase
- presentation linkbase
- SEC-rendered report files and exhibits available in the filing directory

The full download manifest is stored at:

- `data/processed/download_manifest.md`
- `data/processed/download_manifest.json`

## Extraction Scripts

Two local scripts were created:

| Script | Purpose |
|---|---|
| `scripts/sec_download.py` | Downloads SEC filing materials from EDGAR filing directories |
| `scripts/extract_demo_data.py` | Extracts text chunks, XBRL facts, labels, and relation paths from downloaded files |

The download script uses SEC filing directory `index.json` files to identify downloadable materials and preserves a manifest for each filer.

The extraction script currently performs:

- keyword-based text block extraction from the main 10-K HTML
- removal of iXBRL hidden/header metadata from text chunks
- seed-pattern extraction of revenue and inventory-related XBRL facts
- context, period, unit, and dimension extraction for XBRL facts
- label extraction from label linkbases
- relation arc extraction from presentation, calculation, and definition linkbases

## Extracted Data Outputs

| Output | File |
|---|---|
| Text chunks | `data/processed/text_chunks/text_chunks.csv` |
| Per-filer text chunks | `data/processed/text_chunks/{ticker}_text_chunks.json` |
| XBRL facts | `data/processed/xbrl_facts/xbrl_facts.csv` |
| Per-filer XBRL facts | `data/processed/xbrl_facts/{ticker}_xbrl_facts.json` |
| XBRL relation paths | `data/processed/xbrl_paths/xbrl_paths.csv` |
| Per-filer XBRL paths | `data/processed/xbrl_paths/{ticker}_xbrl_paths.json` |
| Extraction summary | `data/processed/extraction_summary.md` |

## Extraction Counts

| Filer | Text Chunks | XBRL Facts | XBRL Relation Paths |
|---|---:|---:|---:|
| Nike | 184 | 365 | 99 |
| Starbucks | 122 | 135 | 210 |
| Target | 103 | 102 | 79 |

Text chunk counts by construct:

| Filer | Revenue | Inventory | Revenue and Inventory |
|---|---:|---:|---:|
| Nike | 121 | 27 | 36 |
| Starbucks | 94 | 19 | 9 |
| Target | 57 | 24 | 22 |

XBRL relation paths by relation type:

| Filer | Presentation | Calculation | Definition |
|---|---:|---:|---:|
| Nike | 51 | 12 | 36 |
| Starbucks | 114 | 16 | 80 |
| Target | 47 | 13 | 19 |

## Initial Quality Checks

### Text Extraction

The first extraction pass captured iXBRL metadata in early text chunks. The extraction script was revised to remove iXBRL hidden/header/resources blocks and taxonomy URI-heavy metadata lines.

After revision, early Nike text chunks begin with readable business and revenue-channel disclosures rather than XBRL namespace metadata.

Example usable text chunk:

| Chunk ID | Filer | Construct | Content Summary |
|---|---|---|---|
| `T-NKE-REVENUE-001` | Nike | Revenue | Describes Nike's footwear/apparel business, Nike Direct, digital platforms, and wholesale accounts |
| `T-SBUX-REVENUE-008` | Starbucks | Revenue | Describes Starbucks Cards, stored value cards, loyalty program, and related customer behavior |

### XBRL Fact Extraction

Extracted facts include revenue, cost of sales, gross profit, accounts receivable, inventory, deferred revenue, and related concepts.

Examples:

| Fact ID | Filer | Concept | Value | Period |
|---|---|---|---:|---|
| `F-NKE-0001` | Nike | `RevenueFromContractWithCustomerExcludingAssessedTax` | 46,309,000,000 | 2024-06-01 / 2025-05-31 |
| `F-NKE-0012` | Nike | `InventoryFinishedGoodsNetOfReserves` | 7,489,000,000 | 2025-05-31 |
| `F-SBUX-0017` | Starbucks | `DeferredRevenueCurrent` | 1,840,600,000 | 2025-09-28 |
| `F-TGT-0007` | Target | `InventoryNet` | 12,740,000,000 | 2025-02-01 |

### XBRL Relation Extraction

Extracted relation paths include presentation, calculation, and definition arcs involving revenue, receivables, inventory, cost of sales, gross profit, deferred revenue, and related concepts.

Examples:

| Path ID | Filer | Relation Type | Source Concept | Target Concept |
|---|---|---|---|---|
| `X-NKE-0001` | Nike | Presentation | `us-gaap:IncomeStatementAbstract` | `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` |
| `X-NKE-0005` | Nike | Presentation | `us-gaap:AssetsCurrentAbstract` | `us-gaap:InventoryFinishedGoodsNetOfReserves` |
| `X-SBUX-0008` | Starbucks | Presentation | `us-gaap:LiabilitiesCurrentAbstract` | `us-gaap:DeferredRevenueCurrent` |

## Current Limitations

The extracted files are suitable for building retrieval contexts, but they are not yet final retrieval logs.

Known limitations:

- Text extraction is keyword-based and may include broad risk-factor passages that need ranking or filtering before prompt construction.
- XBRL relation extraction currently captures direct arcs involving seed-pattern concepts rather than full depth-2 traversal paths.
- Text chunks preserve readable filing language but do not yet include SEC item/note labels with perfect precision.
- XBRL text block facts may contain embedded HTML and should be excluded or separately cleaned before relation-based prompting.
- No LLM outputs have been generated yet.
- No claim-level coding has been performed yet.

## Next Execution Step

The next step is to build retrieval-condition inputs:

1. Select or rank text chunks for each filer and construct.
2. Select XBRL facts and relation paths for each filer and construct.
3. Render prompt-ready text, XBRL, and hybrid contexts.
4. Create retrieval logs for each condition.
5. Run LLM-only diagnostic baseline and retrieval-based prompts.

## Reviewer-Level Assessment

This extraction step supports the Phase 6 design because it shows that the candidate familiar firms have sufficient public SEC/iXBRL materials for the demonstration.

Reviewer-relevant strengths:

- Source materials are public and reproducible.
- Download and extraction are scripted.
- Extracted text and XBRL data are traceable to local SEC files.
- Counts show enough text chunks, facts, and relation paths for revenue and inventory constructs.
- Early extraction quality issue was identified and corrected.

Remaining reviewer risk:

- The next stage must turn these extracted materials into controlled retrieval environments rather than ad hoc examples.
