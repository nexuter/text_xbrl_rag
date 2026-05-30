# Phase 6 Methodological Demonstration Design

## Purpose

This file designs the SEC/XBRL methodological demonstration for the paper.

The demonstration is not a benchmark and should not rank retrieval methods. Its purpose is to show that retrieval design changes what audit researchers can validly infer from LLM outputs.

Core demonstration claim:

> The same LLM audit task can produce outputs that appear similarly useful under a naive accuracy view, yet support different research inferences once retrieval-environment validity, claim-level correctness, and failure modes are applied.

## Reviewer Accept-Level Standard

For Phase 6 to support an accept-level AJPT methodology paper, the demonstration must satisfy five conditions:

1. Use actual SEC filings and Inline XBRL materials.
2. Make retrieval conditions inspectable through retrieval logs.
3. Compare text-based, XBRL-based, and hybrid retrieval without claiming that one is universally superior.
4. Apply the Phase 5 claim-level correctness protocol to concrete LLM outputs.
5. Show at least one inference shift that would be missed by a simple overall accuracy or usefulness evaluation.

## Accept-Level Demonstration Success Criteria

The demonstration should be judged successful only if it produces evidence for the methodological claim, not merely interesting LLM outputs.

Minimum success criteria:

1. At least one claim is text-supported but not graph-valid, or graph-valid but weakly text-supported.
2. At least one claim is graph-valid but only partially audit-valid or audit-invalid.
3. At least one hybrid-retrieval output improves apparent completeness while creating a separability concern.
4. At least one LLM-only output contains a plausible company-specific claim that lacks source traceability.
5. At least one core construct claim receives a different interpretation under the Phase 5 protocol than under a naive overall usefulness or accuracy view.

Failure-to-demonstrate rule:

> If the retrieval conditions do not produce any divergence across correctness layers, the demonstration should not claim that XBRL-augmented retrieval improves audit reasoning. Instead, it should report that, in these cases, the framework primarily served as a reporting and traceability diagnostic.

This rule protects the paper from appearing to force a favorable result.

## Demonstration Scope

The demonstration will use:

- three familiar public SEC filers
- three consumer-facing business settings
- two audit constructs
- three primary retrieval designs
- one required diagnostic LLM-only baseline

Primary retrieval designs:

1. Text-based contextual retrieval
2. XBRL-based relational retrieval
3. Hybrid retrieval

Required diagnostic condition:

4. LLM-only baseline

The LLM-only condition is not a fourth retrieval design. It is a diagnostic baseline used to assess traceability and pretraining-contamination concerns when familiar companies are used.

## Filer Selection Criteria

Candidate filers should satisfy all required criteria:

1. Annual Form 10-K available through SEC EDGAR.
2. Inline XBRL and extracted XBRL instance available.
3. Material revenue and inventory disclosures.
4. Sufficient narrative disclosure for text retrieval.
5. Sufficient XBRL facts, concepts, and linkbase files for relational retrieval.
6. Familiar business model that allows readers to interpret LLM outputs without extensive company background.
7. Filing-specific prompts and retrieval logs can discipline the use of general company knowledge.
8. Not selected based on expected LLM performance.

Preferred criteria:

- visible revenue recognition policy
- visible inventory accounting policy
- product sales, retail, wholesale, or consumer-products context
- manageable filing complexity for a methodological demonstration
- company extension concepts present but not so dominant that extraction becomes idiosyncratic
- business model familiar enough to make inference-shift examples intuitive

Selection rule:

> Filers are selected for construct coverage and public reproducibility, not because they are expected to favor text retrieval, XBRL retrieval, or hybrid retrieval.

## Case Selection Memo Requirement

Before running retrieval or LLM outputs, researchers should prepare a short case selection memo. This memo should be retained in the appendix or replication package.

The memo should include:

- candidate filer list
- inclusion and exclusion criteria
- final selected filers
- backup filer rule
- date of case selection
- confirmation that selection occurred before reviewing LLM outputs
- rationale for using familiar companies despite pretraining-contamination concerns
- statement that cases are used for methodological illustration, not population inference

Reviewer-safe sentence:

> Case selection is documented before output generation so that the demonstration does not appear to choose firms after observing which cases best support the proposed framework.

## Proposed Filers

| Filer | CIK | Filing | Industry Role | Why Useful |
|---|---:|---|---|---|
| Nike, Inc. | 0000320187 | 10-K for period ended 2025-05-31, accession 0000320187-25-000047 | Athletic footwear and apparel | Familiar brand; useful for wholesale/direct revenue, returns, inventory, discounts, and inventory obsolescence reserves |
| Starbucks Corporation | 0000829224 | 10-K for period ended 2025-09-28, accession 0000829224-25-000114 | Coffeehouse retail and licensed stores | Familiar business model; useful for store revenue, licensed revenue, stored value cards, loyalty points, deferred revenue, and inventory reserves |
| Target Corporation | 0000027419 | 10-K for period ended 2025-02-01, accession 0000027419-25-000018 | Mass-market retail | Highly familiar retail setting; useful for sales, returns, inventory, cost of sales, markdowns, and inventory valuation |

Backup filer:

| Filer | CIK | Filing | Industry Role | Use If |
|---|---:|---|---|---|
| The Coca-Cola Company | 0000021344 | 10-K for period ended 2024-12-31, accession 0000021344-25-000011 | Branded beverage products | Use if Nike, Starbucks, or Target creates excessive extraction complexity or if the manuscript needs an even more familiar consumer-products case |

## SEC Availability Check

The candidate filings have publicly available SEC filing detail pages, iXBRL 10-K documents, complete submission text files, extension taxonomy files, linkbase files, and extracted XBRL instance documents.

| Filer | SEC Filing Detail Page | iXBRL 10-K | Extracted XBRL Instance | Linkbase Availability |
|---|---|---|---|---|
| Nike | https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/0000320187-25-000047-index.htm | `nke-20250531.htm` | `nke-20250531_htm.xml` | XSD, CAL, DEF, LAB, PRE |
| Starbucks | https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/0000829224-25-000114-index.htm | `sbux-20250928.htm` | `sbux-20250928_htm.xml` | XSD, CAL, DEF, LAB, PRE |
| Target | https://www.sec.gov/Archives/edgar/data/27419/000002741925000018/0000027419-25-000018-index.htm | `tgt-20250201.htm` | `tgt-20250201_htm.xml` | XSD, CAL, DEF, LAB, PRE |
| Coca-Cola | https://www.sec.gov/Archives/edgar/data/21344/000002134425000011/0000021344-25-000011-index.htm | `ko-20241231.htm` | `ko-20241231_htm.xml` | XSD, CAL, DEF, LAB, PRE |

Reviewer-safe sentence:

> The demonstration uses familiar firms for interpretability, but it relies on filing-specific SEC materials rather than general company knowledge. All text chunks, XBRL paths, and LLM claims should be traceable to the filing detail page and extracted source files.

## Rationale for Primary and Backup Filers

The original candidate set used less-prominent filers to reduce pretraining-contamination concerns. That choice was methodologically defensible, but it introduced a different problem: readers may need company-specific background before they can interpret the retrieval outputs and correctness coding.

For the methodological demonstration, interpretability is especially important. The paper is not estimating population-level retrieval performance; it is showing how retrieval design changes research inference. Therefore, the demonstration should use companies whose business models are familiar enough that readers can focus on the methodological contrast rather than learning the company first.

The revised primary filers are selected to make the demonstration easier to interpret while retaining SEC/iXBRL reproducibility. They are not selected because they are expected to favor text retrieval, XBRL retrieval, or hybrid retrieval.

### Why These Three Filers Work Together

The primary sample is designed around five methodological needs:

1. **Construct coverage**: each filer has revenue and inventory contexts that can support the two planned audit constructs.
2. **Retrieval contrast**: each filer should contain both narrative disclosures and structured XBRL facts/relations, allowing text-based and XBRL-based retrieval to differ in a visible way.
3. **Reader interpretability**: the businesses are familiar enough that readers can understand why revenue recognition, returns, inventory, discounts, stored value cards, or markdowns matter.
4. **Industry variation without losing comparability**: athletic apparel, coffeehouse retail, and mass-market retail are different enough to avoid a single-company or single-industry illustration, but close enough to share revenue and inventory constructs.
5. **Reviewer defensibility**: the companies are public, reproducible SEC cases with Inline XBRL materials, and the demonstration explicitly mitigates pretraining concerns through filing-specific retrieval logs and source-traceable coding.

Selection logic:

> The cases are selected for interpretability, construct coverage, and public reproducibility. Their familiarity is a feature of the methodological demonstration, but it also requires explicit controls for pretraining contamination and source traceability.

## Construct-by-Case Role Matrix

The demonstration should not imply that every company is equally strong for every construct. Each case has a primary role and secondary diagnostic uses.

| Filer | Primary Demonstration Role | Revenue Construct Role | Inventory Construct Role | Most Important Validity Risk to Show |
|---|---|---|---|---|
| Nike | Channel and inventory-risk narrative plus reported relation preservation | Wholesale/direct revenue, receivables, revenue disaggregation | Inventory, cost of sales, gross margin, obsolescence or reserve context | Text-supported narrative may not preserve graph-valid relations |
| Starbucks | Revenue-recognition complexity in a familiar setting | Stored value cards, loyalty rewards, breakage, deferred revenue, licensed revenue | Retail inventory and reserve context as secondary case | Graph-valid liabilities may be overread as audit evidence |
| Target | Intuitive inventory valuation setting | Retail sales, returns, digital/store channel context | Inventory, markdowns, cost of sales, gross margin | Plausible valuation-risk language may exceed retrieved evidence |
| Coca-Cola | Backup consumer-products case | Product revenue and geographic/segment context | Inventory and cost of sales context | Familiar brand knowledge may substitute for retrieved evidence |

Recommended main-text emphasis:

- Use Starbucks as the clearest revenue-recognition example.
- Use Target as the clearest inventory-valuation example.
- Use Nike as the integration and cross-construct example.
- Use Coca-Cola only if one primary case creates extraction or exposition problems.

This role assignment reduces the risk that the demonstration looks like a broad firm-level sample. The cases are illustrative settings, not observations for statistical inference.

### Nike, Inc.

Nike is a strong primary filer because its business is widely understood: it designs and sells athletic footwear and apparel through wholesale and direct-to-consumer channels. This makes it easier for readers to interpret revenue-channel, returns, inventory, discounting, and obsolescence-related claims without learning an unfamiliar company.

Why Nike is useful:

- Its wholesale and direct-to-consumer channels create a natural revenue recognition and disaggregation setting.
- Its inventory context is intuitive because footwear and apparel products are exposed to seasonality, fashion risk, discounting, and obsolescence.
- Its disclosures can support text retrieval around revenue, channel mix, gross margin, inventory, and reserves.
- Its XBRL filing can support relation-based retrieval around revenue, receivables, inventories, cost of sales, gross profit, and segment/geographic dimensions.
- Its public familiarity makes LLM claims easier for readers to interpret, while filing-specific retrieval logs can still discipline the inference.

Expected methodological role:

> Nike is the primary apparel/footwear case for showing how text retrieval can support channel and inventory-risk narratives, while XBRL relational retrieval can preserve reported relationships among revenue, inventory, cost of sales, gross margin, and segment information.

Likely inference-shift example:

| Naive View | Framework-Based View |
|---|---|
| The LLM gives a persuasive explanation of revenue decline or margin pressure using channel-mix language. | Text support may be strong, but graph-validity must be separately assessed using reported revenue, inventory, cost of sales, and margin relationships. |

### Starbucks Corporation

Starbucks is a strong primary filer because its business model is familiar, but its accounting setting is rich. Readers understand coffeehouse sales, gift cards, loyalty rewards, and licensed stores, making it a strong case for showing how simple business intuition can diverge from accounting-specific retrieval evidence.

Why Starbucks is useful:

- Its company-operated store revenue is intuitive for readers.
- Its licensed store revenue, stored value cards, loyalty rewards, breakage, and deferred revenue create a richer revenue recognition setting.
- Its inventory balances and reserves provide an inventory valuation context without requiring an unfamiliar manufacturing process.
- Its disclosures can show why text retrieval may retrieve useful narrative explanations that still need XBRL relation checks.
- It is useful for demonstrating source overreach because gift card liabilities and deferred revenue are reported relationships, not audit evidence.

Expected methodological role:

> Starbucks is the primary revenue-recognition case because it makes deferred revenue, stored value cards, loyalty-related obligations, and breakage understandable to a broad readership while still requiring careful accounting interpretation.

Likely inference-shift example:

| Naive View | Framework-Based View |
|---|---|
| The LLM correctly states that gift card balances are relevant to revenue recognition. | The claim may be text-supported and graph-valid, but audit-validity depends on whether the model treats the balance as a risk cue rather than evidence of misstatement. |

### Target Corporation

Target is a strong primary filer because its business model is exceptionally familiar: it sells consumer goods through stores and digital channels and holds large retail inventories. This makes it a clear case for inventory valuation, markdowns, sales returns, and cost of sales.

Why Target is useful:

- It provides the most intuitive inventory valuation setting among the proposed cases.
- It has familiar retail economics: sales, returns, markdowns, cost of sales, gross margin, and inventory turnover.
- Its disclosures are likely to support text retrieval around inventory accounting and business conditions.
- Its XBRL data can support relation retrieval around sales, inventory, cost of sales, gross margin, and current assets.
- It gives the demonstration a general retail case that readers can interpret without specialized industry knowledge.

Expected methodological role:

> Target is the primary inventory valuation case because it allows readers to understand why reported inventory relationships are relevant while still requiring the protocol to prevent unsupported audit conclusions.

Likely inference-shift example:

| Naive View | Framework-Based View |
|---|---|
| The LLM correctly links inventory and markdown pressure to valuation risk. | The link may be professionally plausible, but the claim must be checked against retrieved disclosures, XBRL relation paths, and the distinction between risk cue and audit conclusion. |

### The Coca-Cola Company as Backup Filer

Coca-Cola is a useful backup because it is one of the most familiar consumer-products companies and has public SEC filings with Inline XBRL materials. It can replace one primary case if extraction complexity or disclosure structure becomes problematic.

Why Coca-Cola is a good backup:

- It is a public SEC filer with available 10-K and Inline XBRL materials.
- Its products and revenue model are highly familiar to readers.
- It has product revenue, concentrate/syrup, finished products, cost of sales, inventory, and geographic/operating segment context.
- It is useful if the paper needs a globally recognizable consumer-products case.
- It can strengthen exposition if Starbucks or Target disclosures create too much retail-specific complexity.
- It may be especially useful for showing that familiar brands still require source-traceable retrieval rather than general model knowledge.

Expected backup role:

> Coca-Cola should be used if the demonstration needs an even more familiar consumer-products case. It would improve reader accessibility, but its global scale and brand familiarity increase the need to address pretraining contamination.

Tradeoff:

| Choice | Strength | Weakness |
|---|---|---|
| Nike / Starbucks / Target | Highly interpretable business models; easier for readers to understand output claims | Greater pretraining-contamination concern because the companies are well known |
| Coca-Cola backup | Extremely familiar consumer-products case | Very high brand familiarity may increase reliance on model priors unless retrieval controls are strict |
| Original Caleres / Duluth / Helen of Troy set | Lower pretraining-contamination concern; less obvious company priors | Lower reader familiarity may make output interpretation harder |

## Pretraining-Contamination Mitigation for Familiar Filers

Using familiar companies is acceptable for a methodological demonstration only if the manuscript makes clear that the inference depends on retrieved filing evidence, not general model knowledge.

Required safeguards:

- Use the instruction: "Use only the information provided in the context."
- Require claim-level source mapping to retrieved text chunk IDs or XBRL path IDs.
- Code unsupported claims as attribution failures even if they are generally plausible.
- Include a required LLM-only diagnostic baseline to show how much the model says without retrieved filing context.
- Prefer filing-specific prompts that reference the exact fiscal year and filing period.
- Avoid asking broad company-knowledge questions.
- Report retrieval logs and context shown to the model.
- Report the model name, model version, access date, and stated knowledge cutoff if available.
- If the filing date is before the model's stated or likely training cutoff, treat pretraining contamination risk as high and emphasize LLM-only diagnostics.
- If the filing date is after the model's stated knowledge cutoff, still treat general company knowledge as a risk because company background may be known even if the exact filing is not.

Minimum contamination diagnostic:

| Diagnostic | Purpose | Required Output |
|---|---|---|
| LLM-only baseline | Shows what the model produces without retrieved filing context | Unsupported but plausible claims coded as attribution failures |
| Filing-period specificity | Reduces reliance on generic company knowledge | Prompt includes fiscal year, period of report, and accession number |
| Source mapping | Separates retrieved support from model priors | Each claim maps to text chunk ID, XBRL path ID, or unsupported status |
| No-context comparison memo | Documents pretraining risk | Short note comparing LLM-only output to retrieval-supported output |
| Model cutoff disclosure | Helps readers assess whether the filing may have appeared in training data | Model name, version, access date, and stated knowledge cutoff if available |

Reviewer-safe sentence:

> We intentionally use familiar companies to make the methodological contrast interpretable, but we do not rely on general company familiarity as evidence. Claims are evaluated only against retrieved filing text, XBRL relation paths, and expert-coded audit reasonableness.

## Model Reporting Requirement

The demonstration should report the model environment with enough detail for readers to evaluate contamination, reproducibility, and comparability.

Required fields:

| Field | Required Reporting |
|---|---|
| Model provider and model name | Exact model identifier used at the time of execution |
| Model version or snapshot | Version string, dated snapshot, or API model ID when available |
| Access date | Date outputs were generated |
| Stated knowledge cutoff | Report if disclosed by the provider; otherwise state that it is not disclosed |
| Temperature and decoding settings | Temperature, top-p, seed if available |
| System prompt or task shell | Full prompt shell in appendix |
| Retrieval context | Exact context shown to the model for each run |
| Repeated runs | Whether outputs were generated once or repeated |

Reviewer-safe sentence:

> Because familiar firms may already be represented in model pretraining, the demonstration reports the model environment and uses no-context baselines to separate retrieved support from plausible but unsupported model priors.

## Reviewer-Safe Case Selection Language

Suggested manuscript language:

> We select three public SEC filers to illustrate, rather than statistically test, how retrieval design affects research inference in LLM-based audit studies. The cases are chosen before evaluating model outputs and are selected because they provide public 10-K filings with Inline XBRL, narrative revenue and inventory disclosures, and sufficient structured reporting relationships to support text-based, XBRL-based, and hybrid retrieval conditions. Nike, Starbucks, and Target are intentionally familiar companies: their business models allow readers to understand the audit-relevant setting without extensive company background. This familiarity improves interpretability, but it also increases the importance of source-traceable retrieval. We therefore evaluate LLM claims only against retrieved filing text, XBRL relation paths, and expert-coded audit reasonableness. Coca-Cola is retained as a backup case if one primary case proves too complex or if the manuscript needs an alternative familiar consumer-products example. The case selection is intended to support methodological illustration and reproducibility, not population-level inference about LLM or retrieval performance.

## SEC Source Materials

For each filer, collect:

- 10-K iXBRL HTML filing
- extracted XBRL instance XML
- taxonomy extension schema
- calculation linkbase
- definition linkbase
- label linkbase
- presentation linkbase
- complete submission text file

Minimum source fields to report:

| Field | Required |
|---|---|
| Company name | Yes |
| CIK | Yes |
| Accession number | Yes |
| Filing date | Yes |
| Period of report | Yes |
| 10-K iXBRL filename | Yes |
| Extracted XBRL instance filename | Yes |
| Linkbase filenames | Yes |
| Taxonomy version / extraction date | Yes |
| Retrieval date | Yes |

## Audit Constructs

### Construct 1: Revenue Recognition Risk Cue Identification

The construct is not whether revenue is misstated. The construct is whether the LLM identifies and qualifies revenue recognition risk cues using the retrieved information environment.

Examples of construct-relevant information:

- revenue recognition policy
- product sales, wholesale, retail, and e-commerce channels
- returns and refund liabilities
- contract liabilities or deferred revenue, if applicable
- customer allowances, incentives, rebates, or promotional programs
- accounts receivable and revenue trends
- disaggregated revenue or segment information

Possible XBRL seed concepts:

- `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax`
- `us-gaap:SalesRevenueNet`
- `us-gaap:AccountsReceivableNetCurrent`
- `us-gaap:ContractWithCustomerLiability`
- `us-gaap:DeferredRevenueCurrent`
- `us-gaap:RefundLiabilityCurrent`
- company-specific revenue or return-related extension concepts

Reviewer-safe boundary:

> The demonstration evaluates risk-cue reasoning, not an audit conclusion about revenue misstatement.

### Construct 2: Inventory Valuation Assertion Mapping

The construct is whether the LLM maps inventory-related disclosures and XBRL relations to valuation-relevant audit reasoning while avoiding unsupported conclusions.

Examples of construct-relevant information:

- inventory accounting policy
- lower of cost and net realizable value language
- obsolescence, markdown, reserve, or write-down disclosures
- inventory balances and period changes
- cost of sales / gross margin relation context
- segment or product category inventory exposure

Possible XBRL seed concepts:

- `us-gaap:InventoryNet`
- `us-gaap:InventoryFinishedGoodsNetOfReserves`
- `us-gaap:InventoryRawMaterialsAndSupplies`
- `us-gaap:InventoryWorkInProcess`
- `us-gaap:CostOfRevenue`
- `us-gaap:CostOfGoodsAndServicesSold`
- `us-gaap:GrossProfit`
- company-specific inventory reserve or inventory classification extension concepts

Reviewer-safe boundary:

> The demonstration evaluates whether the LLM reasons about the valuation assertion using public reporting data. It does not evaluate whether inventory is fairly stated.

## Retrieval Conditions

### Condition A: Text-Based Contextual Retrieval

Source:

- MD&A
- notes to financial statements
- significant accounting policies
- revenue recognition disclosures
- inventory disclosures
- business description only if needed for channel context

Retrieval unit:

- paragraph or note-level chunk

Operator:

- semantic similarity or keyword retrieval using construct-specific queries

Representation:

- verbatim text chunks with section labels and chunk IDs

Controls:

- top-k fixed or disclosed
- chunk size fixed or disclosed
- token budget reported
- source section reported

Expected strength:

- supports narrative disclosure comprehension

Expected risk:

- may omit structured accounting relationships and period/context distinctions

### Condition B: XBRL-Based Relational Retrieval

Source:

- extracted XBRL instance
- taxonomy extension schema
- labels
- calculation linkbase
- presentation linkbase
- definition linkbase

Retrieval unit:

- concept
- fact
- context
- unit
- dimension
- relation path

Operator:

- typed relation traversal from seed concepts

Representation:

- structured relation table rendered into text, preserving concept IDs, labels, values, periods, dimensions, and relation types

Controls:

- seed concept list reported
- traversal depth fixed or disclosed
- relation types preserved
- extension handling rule reported
- taxonomy/linkbase files reported

Expected strength:

- supports reported accounting relation preservation and graph-valid correctness

Expected risk:

- may omit narrative explanation and may invite source overreach

### Condition C: Hybrid Retrieval

Source:

- text retrieval output
- XBRL relational retrieval output

Retrieval unit:

- text chunks plus XBRL facts/relation paths

Operator:

- semantic text retrieval plus typed relation traversal

Representation:

- two-part context:
  1. narrative disclosure excerpts
  2. XBRL facts and relation paths

Controls:

- text and XBRL components separately logged
- ordering rule reported
- token allocation reported
- text-only and XBRL-only conditions retained for separability

Expected strength:

- supports narrative-numeric integration

Expected risk:

- reduces separability and may look superior merely because it receives more information

## Token and Context Control

Recommended design:

| Condition | Context Budget Rule |
|---|---|
| Text retrieval | Maximum 1,200-1,500 words or equivalent token budget |
| XBRL retrieval | Maximum 1,200-1,500 words after rendering relation tables |
| Hybrid retrieval | Component-balanced budget: approximately 50 percent text and 50 percent XBRL |
| LLM-only diagnostic baseline | No retrieved filing context |

The manuscript should disclose actual context length for every run. If exact equality is impractical, the demonstration should report context volume and avoid performance ranking.

## Retrieval Query Templates

### Revenue Recognition Text Query

```text
Retrieve passages relevant to revenue recognition, sales returns, refunds, customer incentives, contract liabilities, deferred revenue, accounts receivable, and explanations of revenue changes.
```

### Inventory Valuation Text Query

```text
Retrieve passages relevant to inventory accounting policy, lower of cost and net realizable value, obsolescence, markdowns, reserves, write-downs, cost of sales, and explanations of inventory changes.
```

### Revenue Recognition XBRL Retrieval Rule

```text
For each revenue seed concept:
1. Retrieve current-year and prior-year facts.
2. Retrieve labels and definitions.
3. Retrieve presentation parents and children up to depth 2.
4. Retrieve calculation parents and children up to depth 2.
5. Retrieve dimensions, members, units, and contexts.
6. Retrieve nearby company extension concepts in the same presentation group.
7. Preserve relation type labels.
```

### Inventory Valuation XBRL Retrieval Rule

```text
For each inventory seed concept:
1. Retrieve current-year and prior-year facts.
2. Retrieve labels and definitions.
3. Retrieve presentation parents and children up to depth 2.
4. Retrieve calculation parents and children up to depth 2.
5. Retrieve cost-of-sales and gross-profit relation paths where available.
6. Retrieve dimensions, members, units, and contexts.
7. Retrieve nearby company extension concepts related to reserves, markdowns, or inventory categories.
8. Preserve relation type labels.
```

## LLM Task Prompt Template

Use the same prompt shell across retrieval conditions.

```text
You are assisting with an auditing research task. Use only the information provided in the context.

Task:
Identify audit-relevant risk cues or assertion-mapping considerations for [AUDIT CONSTRUCT] for [COMPANY], fiscal year [FISCAL YEAR], period ended [PERIOD OF REPORT], accession [ACCESSION NUMBER], based on the provided context.

Instructions:
1. Provide no more than five audit-relevant claims.
2. Distinguish factual claims from risk-cue or assertion-mapping claims.
3. Do not conclude that a misstatement exists.
4. State when the provided context is insufficient.
5. Avoid treating reported XBRL relationships as independent audit evidence.
6. Do not use general company knowledge outside the provided context.

Context:
[RETRIEVED CONTEXT]

Output format:
- Claim:
  - Claim type:
  - Support used:
  - Limitation:
```

This prompt is intentionally conservative. It gives the model an opportunity to qualify claims, which makes audit-valid correctness meaningful rather than trivially punitive.

## Output and Coding Plan

For each filer, construct, and retrieval condition:

1. Run the LLM task prompt.
2. Preserve the raw output.
3. Segment the output into claims.
4. Tag each claim as core construct, supporting factual, context, or procedure-like.
5. Code text-supported correctness.
6. Code graph-valid correctness.
7. Code audit-valid correctness.
8. Code integrated correctness.
9. Identify failure modes.
10. Produce an inference statement.

Minimum expected cells:

| Filers | Constructs | Conditions | Runs | Approximate Claim Rows |
|---:|---:|---:|---:|---:|
| 3 | 2 | 3 primary retrieval conditions + 1 diagnostic baseline | 24 | 80-120 |

The 18 primary retrieval-condition runs support the main methodological comparison. The 6 LLM-only runs are used only to diagnose traceability and pretraining contamination.

Optional robustness:

- one repeated run per condition
- one alternative model
- one alternative retrieval depth for XBRL retrieval
- one alternative top-k for text retrieval

## Minimum Evidence Package for the Manuscript

The main manuscript should not attempt to show all 80-120 coded claim rows. It should show enough evidence for readers to see how the framework changes inference.

Minimum main-text evidence:

1. One revenue-recognition example, preferably Starbucks.
2. One inventory-valuation example, preferably Target.
3. One integration example, preferably Nike or hybrid retrieval.
4. One LLM-only contamination diagnostic example.
5. One table showing selected claim-level correctness divergence.
6. One inference-shift table linking observed output patterns to revised research inference.

Appendix evidence:

- full retrieval logs
- full prompts
- all retrieved text chunks used in prompts
- all rendered XBRL relation paths used in prompts
- raw LLM outputs
- complete claim-level coding table
- no-context comparison memo
- graph spot-check memo

Reviewer-safe sentence:

> The main text demonstrates the inferential consequences of retrieval design through selected cases, while the appendix preserves the full retrieval and coding trail needed to evaluate reproducibility.

## Claim-Level Coding Table Template

| Filer | Construct | Condition | Claim ID | Claim Text | Claim Importance | Text Source ID | XBRL Path ID | Text-Supported | Graph-Valid | Audit-Valid | Integrated | Failure Mode | Inference Note |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---|
| NKE | Revenue | Text | NKE-REV-T-01 | TBD | Core construct | T-NKE-REV-02 | N/A | TBD | TBD | TBD | TBD | TBD | TBD |
| SBUX | Revenue | Hybrid | SBUX-REV-H-01 | TBD | Core construct | T-SBUX-REV-03 | X-SBUX-REV-02 | TBD | TBD | TBD | TBD | TBD | TBD |
| TGT | Inventory | XBRL | TGT-INV-X-01 | TBD | Supporting factual | N/A | X-TGT-INV-03 | TBD | TBD | TBD | TBD | TBD | TBD |
| NKE | Inventory | LLM-only | NKE-INV-B-01 | TBD | Core construct | N/A | N/A | TBD | TBD | TBD | TBD | Attribution failure / unsupported | Used only for contamination diagnostic |

## Retrieval Log Template

| Retrieval ID | Filer | Construct | Condition | Source File | Source Section or XBRL File | Retrieval Operator | Query or Seed Concept | Rank / Path Depth | Context Length | Included in Prompt |
|---|---|---|---|---|---|---|---|---:|---:|---|
| T-NKE-REV-01 | NKE | Revenue | Text | nke-20250531.htm | Revenue recognition note | Semantic / keyword | revenue recognition | 1 | TBD | Yes |
| X-NKE-REV-01 | NKE | Revenue | XBRL | nke-20250531_htm.xml | Extracted instance + linkbases | Relation traversal | us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax | 2 | TBD | Yes |
| B-NKE-REV-01 | NKE | Revenue | LLM-only | N/A | N/A | None | No retrieved context | 0 | 0 | No |

## Planned Inference Shift Patterns

The demonstration should look for, but not force, the following patterns:

| Pattern | Why It Matters |
|---|---|
| Text retrieval produces richer narrative explanations but weak graph-validity | Shows why narrative support is not the same as reported relation preservation |
| XBRL retrieval produces accurate fact/relation claims but weak audit-validity | Shows why reported relationships are not audit evidence |
| Hybrid retrieval improves integrated correctness but weakens separability | Shows why hybrid retrieval is not automatically superior |
| Background factual claims score well while core construct claims are partial | Shows why claim importance tags matter |
| A claim is not assessable because retrieval logs are incomplete | Shows why traceability is part of validity |

## Demonstration Tables for Manuscript

### Table 1: Case Selection

Report filer, industry, CIK, accession, filing date, period of report, and rationale for inclusion.

### Table 2: Retrieval Conditions

Report source, unit, operator, representation, controls, and expected validity risk for each condition.

### Table 3: Example Retrieved Context

For one revenue case and one inventory case, show:

- one text chunk
- one XBRL relation path
- one hybrid context excerpt

### Table 4: Claim-Level Correctness

Show selected coded claims that illustrate divergence across correctness layers.

### Table 5: Inference Shift

Compare naive inference with retrieval-environment-validity inference.

## Draft Inference Shift Table

| Demonstration Finding | Naive Interpretation | Retrieval-Environment Validity Interpretation |
|---|---|---|
| Text retrieval identifies revenue risk cues using revenue policy language | Text retrieval supports audit risk reasoning | Text retrieval supports narrative comprehension, but graph-validity and relation preservation remain untested |
| XBRL retrieval correctly reports inventory balance changes | XBRL retrieval supports inventory valuation reasoning | XBRL retrieval supports reported relation preservation, not audit evidence sufficiency |
| Hybrid retrieval generates the most complete answer | Hybrid retrieval is best | Hybrid retrieval may support narrative-numeric integration, but text and relation effects are not separable |
| LLM output contains many correct background facts but an unsupported core risk conclusion | The output is mostly accurate | The retrieval condition fails to support the core audit construct |
| XBRL relation path is rendered as economic causality | The model used structured data well | The output shows representation validity failure and possible source overreach |

## Data Acquisition Plan

Recommended local structure for execution:

```text
data/
  raw_sec/
    nke_2025_10k/
    sbux_2025_10k/
    tgt_2025_10k/
    ko_2024_10k_backup/
  processed/
    text_chunks/
    xbrl_paths/
    retrieval_logs/
    llm_outputs/
    coding_tables/
```

Minimum files to save per filer:

- 10-K HTML
- extracted XBRL instance XML
- XSD schema
- calculation linkbase
- DEF linkbase
- LAB linkbase
- PRE linkbase
- complete submission text file

## Extraction Plan

### Text Extraction

Extract and label:

- Item 1 business context
- Item 7 MD&A
- revenue recognition note
- inventory accounting policy
- inventory note
- segment note, if relevant

Text chunks should preserve:

- company
- filing
- item/note section
- paragraph order
- source URL or local path
- chunk ID

### XBRL Extraction

Extract and label:

- facts for seed concepts
- fact values
- periods
- units
- contexts
- dimensions
- standard labels
- company extension labels
- calculation parent/child paths
- presentation parent/child paths
- definition/dimension paths where relevant

XBRL paths should preserve:

- relation type
- source concept
- target concept
- depth
- role URI or role label
- standard vs extension concept indicator

## Reviewer Stress Test

### Concern 1: The cases are cherry-picked.

Response:

The filer selection criteria are stated before coding and do not depend on LLM output quality. The cases are selected for construct coverage, public reproducibility, and availability of Inline XBRL data.

### Concern 2: The demonstration is too small.

Response:

The demonstration is descriptive and methodological, not inferential. Its purpose is to show how the framework changes interpretation, not to estimate population-level retrieval performance.

### Concern 3: The paper still looks like a benchmark.

Response:

The design reports correctness by layer and claim type, avoids a headline accuracy score, and focuses on inference shifts rather than rankings.

### Concern 4: XBRL extraction errors may drive the findings.

Response:

The demonstration requires graph spot-checks against original SEC files, including concept IDs, relation types, periods, units, dimensions, and extension handling.

### Concern 5: Hybrid retrieval receives more information.

Response:

The design uses component-balanced context reporting and retains text-only and XBRL-only conditions to preserve diagnostic separability.

### Concern 6: Audit-valid correctness lacks ground truth.

Response:

Audit-valid correctness is expert-coded professional reasonableness, not objective truth. The demonstration uses bounded risk-cue and assertion-mapping constructs rather than audit conclusions.

### Concern 7: The prompt is too conservative.

Response:

The prompt is conservative by design because the paper studies validity of research inference, not maximum model performance. A less constrained prompt can be used as a sensitivity check.

### Concern 8: The demonstration depends on one LLM.

Response:

The main demonstration can use one documented model because it is methodological. Model variation should be included as a sensitivity check if feasible.

### Concern 9: Familiar companies create pretraining-contamination risk.

Response:

This is the main tradeoff introduced by the revised case selection. The demonstration uses familiar companies to improve reader interpretability, but every LLM claim is evaluated only against retrieved filing text, XBRL relation paths, and expert-coded audit reasonableness. The LLM-only diagnostic baseline is required and unsupported plausible claims are coded as attribution failures.

### Concern 10: The cases are no longer less-prominent, so the original selection logic is inconsistent.

Response:

The revised design explicitly changes the selection logic from low-prominence to interpretability plus source traceability. The paper should state that familiar companies are used because the demonstration is methodological and descriptive, not because the authors seek representative firm-level inference.

### Concern 11: Public familiarity may make the results look less generalizable.

Response:

The demonstration is not intended to generalize to all firms. Its purpose is to show how retrieval-environment validity changes inference in inspectable cases. Generalizability should be discussed as a boundary condition, with less-prominent filers identified as a natural extension or robustness setting.

### Concern 12: The design still permits result-driven example selection.

Response:

The case selection memo is prepared before retrieval and output generation. The manuscript should also pre-specify the minimum evidence package: one revenue example, one inventory example, one integration example, one LLM-only diagnostic example, selected claim-level divergence, and an inference-shift table.

### Concern 13: The demonstration may not produce the expected divergence patterns.

Response:

The design includes a failure-to-demonstrate rule. If correctness layers do not diverge, the paper should report that result and frame the framework as a traceability and reporting diagnostic in those cases rather than claiming that XBRL-augmented retrieval changes audit reasoning.

### Concern 14: Model knowledge cutoff is not addressed.

Response:

The revised design requires model name, version, access date, decoding settings, and stated knowledge cutoff where available. If the filing may have appeared in training data, the LLM-only baseline becomes central to interpreting traceability and pretraining risk.

## Reviewer-Level Critical Assessment

### Strengths

- The revised filer set improves interpretability for readers.
- The cases support intuitive revenue and inventory constructs.
- SEC/iXBRL availability is verified at the filing-detail level.
- The design now explicitly acknowledges and mitigates pretraining-contamination risk.
- The LLM-only condition is correctly framed as a diagnostic baseline rather than a fourth retrieval design.
- Claim-level templates, retrieval logs, and local data folders now match the revised filer set.
- Case selection memo requirement reduces result-driven case-selection concerns.
- Model reporting and cutoff disclosure strengthen the pretraining-contamination defense.
- The failure-to-demonstrate rule prevents overclaiming if the expected divergence patterns do not appear.
- The minimum evidence package clarifies what must appear in the manuscript versus appendix.

### Remaining Weaknesses

- Familiar-company use remains a review risk and must be justified in the introduction to the demonstration.
- The actual extraction stage may reveal that Starbucks or Coca-Cola has complex extension concepts that require narrower seed concept rules.
- The paper must avoid letting brand familiarity substitute for filing-specific evidence.
- The final demonstration should include at least one no-context LLM claim that sounds plausible but fails traceability coding.
- If reviewers strongly prefer lower pretraining risk, the original Caleres / Duluth / Helen of Troy set can be retained as a robustness or appendix alternative.
- The demonstration must avoid cherry-picking only the most dramatic claim divergences; selected examples should be tied to the pre-specified evidence package.
- Model provider knowledge-cutoff disclosure may be incomplete, so the paper should not overstate contamination control.

### Accept-Level Improvement

The revised Phase 6 design is stronger than the prior version if the manuscript emphasizes interpretability as a methodological demonstration choice and treats pretraining contamination as a validity threat to be diagnosed rather than ignored.

Reviewer-safe verdict:

> The case selection is acceptable for a descriptive methodology paper because the familiar firms make the retrieval contrasts interpretable, while the design uses filing-specific prompts, retrieval logs, LLM-only baselines, and claim-level source mapping to prevent general company knowledge from being mistaken for retrieval-supported reasoning.

### Final Accept-Level Assessment

From a reviewer perspective, Phase 6 can support a favorable assessment if the final paper executes the design as specified. The design now addresses the main reasons a reviewer would hesitate:

- why familiar firms are used
- how pretraining contamination is diagnosed
- how examples are selected before observing outputs
- what counts as successful evidence for the methodological claim
- what the authors will conclude if the expected divergence does not appear

The remaining risk is execution quality, not design logic. The design will not be accept-level if the paper only presents polished examples without full retrieval logs, no-context diagnostics, and claim-level coding.

## Accept-Level Reviewer Verdict

Phase 6 is accept-level as a design if it produces concrete examples showing that:

- text support, graph validity, audit validity, and integrated correctness can diverge
- retrieval logs change what can be inferred from LLM outputs
- XBRL-based relational retrieval adds methodological value without being treated as audit evidence
- hybrid retrieval supports integration while raising separability concerns
- simple output accuracy is less informative than retrieval-environment-validity analysis

The strongest manuscript version will include at least two detailed examples:

1. A revenue recognition case where text retrieval supports a plausible narrative risk cue but omits a structured relationship available through XBRL.
2. An inventory valuation case where XBRL retrieval preserves a reported inventory relation but the LLM overstates the audit implication, producing graph-valid but audit-invalid or partially audit-valid reasoning.

## Phase 6 Deliverables Status

- Demonstration purpose and accept-level standard: complete.
- Filer selection criteria: complete.
- Candidate SEC filers: complete.
- SEC filing availability check: complete.
- Case selection memo requirement: complete.
- Familiar-company interpretability rationale: complete.
- Pretraining-contamination mitigation design: complete.
- Model reporting and cutoff disclosure requirement: complete.
- Accept-level demonstration success criteria: complete.
- Minimum main-text and appendix evidence package: complete.
- Audit constructs: complete.
- Retrieval conditions: complete.
- Query and retrieval rule templates: complete.
- LLM prompt template: complete.
- Claim-level coding table template: complete.
- Retrieval log template: complete.
- Inference shift table: complete.
- Reviewer stress test: complete.
- Reviewer-level critical assessment: complete.
- Actual SEC file download: pending execution.
- Text and XBRL extraction: pending execution.
- LLM output generation: pending execution.
- Claim-level coding with real outputs: pending execution.
