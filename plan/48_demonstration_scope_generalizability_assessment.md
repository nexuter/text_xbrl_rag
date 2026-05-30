# Demonstration Scope and Generalizability Assessment

## Purpose

This memo evaluates whether the current three-filer demonstration is sufficient for the paper's methodological claims, or whether the paper needs a broader and more comprehensive data collection strategy across firm size, industry, and reporting complexity.

Reviewer question:

> Is the demonstration broad enough to support the paper's methodological contribution, or does it look like a narrow set of hand-picked examples?

## Bottom-Line Assessment

The current three-filer demonstration is sufficient for a **Tier 1 methodological illustration** but not sufficient for claims of empirical generalizability across firms, industries, filing complexity, or audit settings.

The paper should not claim:

- that XBRL relational retrieval behaves similarly across industries;
- that hybrid retrieval generally improves audit reasoning;
- that the observed failure modes occur at representative rates;
- that the framework is empirically validated across the population of SEC filers.

The paper can defensibly claim:

- retrieval condition labels can obscure claim-level evidence use;
- text retrieval, XBRL relational retrieval, and hybrid retrieval create different information environments;
- claim-level correctness layers reveal inference differences that response-level evaluation would miss;
- the framework can be applied to actual SEC filing and Inline XBRL data.

To strengthen the paper before submission, I recommend adding a **bounded robustness extension** rather than converting the paper into a large empirical study.

## Why More Cases May Matter

Although the contribution is methodological, the demonstration carries rhetorical and evidentiary weight. Reviewers may evaluate whether the demonstration shows a general methodological problem or merely a few convenient examples.

The current cases have strengths:

1. Nike, Starbucks, and Target are familiar firms.
2. Their business models are understandable to readers.
3. Revenue and inventory are intuitive audit-relevant constructs.
4. The source trail is transparent.
5. The demonstration is manageable enough for claim-level coding and spot checking.

But the current cases also have limitations:

1. They are all large, prominent public companies.
2. They are all consumer-facing firms.
3. They all have relatively mature reporting processes.
4. They may not capture variation in XBRL extension use, reporting complexity, industry-specific taxonomies, or disclosure style.
5. They do not show whether retrieval-environment validity problems appear in less familiar or more complex reporting environments.

An AJPT reviewer may therefore ask whether the demonstration is illustrative but too narrow.

## Methodological Versus Empirical Generalization

The paper should distinguish two types of generalization.

### Methodological Generalization

Methodological generalization asks whether the framework is applicable beyond the specific cases. For this purpose, the paper does not need a large archival sample. It needs cases that demonstrate the mechanism:

1. retrieval dynamically creates the LLM's information environment;
2. different retrieval designs expose different evidence;
3. claim-level correctness layers can diverge;
4. response-level evaluation can produce misleading inference.

The current demonstration mostly satisfies this standard.

### Empirical Generalization

Empirical generalization asks whether observed patterns hold across firms, industries, size groups, filing complexity, and audit constructs. For this purpose, the current three cases are not enough.

If the paper wants to claim that retrieval failure modes are common, that hybrid retrieval often fails to integrate evidence, or that XBRL relational retrieval improves traceability across reporting settings, then the paper would need a broader sampling design and more systematic coding.

## Recommended Framing

The safest framing is:

> The demonstration is not designed to estimate population-level performance or failure-mode prevalence. It is designed to show, using actual SEC filing and Inline XBRL data, how retrieval-environment validity can be operationalized and how claim-level evidence use can change research inference.

This framing keeps the paper within AJPT methodology territory.

## Recommended Demonstration Expansion

I recommend a two-layer demonstration design.

### Layer 1: Deep Case Demonstration

Keep the current three filers as the main manuscript demonstration:

| Filer | Why Keep |
|---|---|
| Nike | Familiar global consumer products company with revenue and inventory relevance |
| Starbucks | Familiar consumer-facing company with supply chain, inventory, and revenue relevance |
| Target | Familiar retailer with strong inventory relevance and intuitive operating model |

Purpose:

Use these cases for detailed claim-level examples, source spot checks, and manuscript tables.

This layer supports interpretability and traceability.

### Layer 2: Bounded Robustness Extension

Add a supplemental set of additional filers to show that the framework applies across a wider range of reporting environments. This extension should remain bounded and methodological, not become a full empirical study.

Recommended size:

6 to 12 additional filers.

Minimum useful expansion:

6 additional filers.

Stronger expansion:

12 additional filers.

The goal is not statistical representativeness. The goal is **maximum-variation theoretical sampling**.

## Recommended Sampling Dimensions

### Dimension 1: Firm Size

Include variation in market capitalization or filer scale.

| Size Group | Purpose |
|---|---|
| Large accelerated filers | Comparable to current cases; mature reporting systems |
| Mid-sized accelerated filers | More variation in disclosure depth and XBRL tagging |
| Smaller public filers, if data quality permits | Greater risk of sparse disclosures and extension concepts |

Rationale:

Retrieval-environment validity may be affected by disclosure richness, XBRL tagging quality, and reporting complexity. A sample limited to very large firms may understate selection and representation problems.

### Dimension 2: Industry

Select industries where the chosen audit constructs are meaningful.

| Industry Type | Revenue Construct Fit | Inventory Construct Fit | Expected Retrieval Value |
|---|---|---|---|
| Retail | High | High | Strong inventory and sales disclosures |
| Consumer products / apparel | High | High | Inventory valuation, returns, revenue channels |
| Manufacturing / industrial | High | High | More complex inventory and production cost disclosures |
| Technology / software | High | Lower or mixed | Deferred revenue, contract liabilities, limited inventory |
| Healthcare / pharma / medtech | High | Moderate to high | Product inventory, reserves, regulatory risk |
| Transportation / logistics | Moderate | Low | Useful boundary case for inventory construct limits |

Avoid relying heavily on financial institutions in this paper because inventory is generally not a natural construct and financial statement structure differs substantially. If included, financial institutions should be treated as a boundary case rather than part of the main revenue/inventory demonstration.

### Dimension 3: Reporting Complexity

Capture variation in:

1. number of XBRL facts;
2. extension concept use;
3. length of revenue and inventory footnotes;
4. segment or geographic complexity;
5. presence of contract liabilities, returns, allowances, reserves, or inventory valuation accounts.

Rationale:

The framework's value should be visible when retrieval complexity varies. Reporting complexity is likely to affect selection, representation, traceability, and separability.

### Dimension 4: Construct Fit

The additional cases should include both strong-fit and weak-fit examples.

| Construct Fit Type | Example | Why Useful |
|---|---|---|
| Strong fit | Retail inventory valuation | Shows framework under intuitive construct-data alignment |
| Mixed fit | Software revenue recognition | Shows XBRL/text retrieval when narrative and contract liabilities matter more than inventory |
| Weak fit | Service firm inventory | Shows boundary conditions and prevents overgeneralization |

Rationale:

A methodology paper is stronger when it shows where the method should and should not be used.

## Candidate Expansion Design

### Minimum Expansion: 6 Additional Filers

| Category | Number of Filers | Purpose |
|---|---:|---|
| Additional large consumer/retail firms | 2 | Check whether current examples are not idiosyncratic |
| Manufacturing / industrial firms | 2 | Add inventory complexity and different cost structures |
| Technology / software firms | 1 | Add deferred revenue / contract liability setting |
| Healthcare / pharma / medtech firm | 1 | Add product/regulatory/inventory reserve setting |

Total:

9 filers including the current 3.

This is the minimum expansion I would recommend if the paper wants stronger reviewer confidence without becoming a large empirical project.

### Stronger Expansion: 12 Additional Filers

| Category | Number of Filers | Purpose |
|---|---:|---|
| Consumer retail | 3 | Inventory-heavy comparison group |
| Consumer products / apparel | 2 | Similar to Nike but varied reporting |
| Manufacturing / industrial | 3 | Inventory and cost complexity |
| Technology / software | 2 | Revenue recognition and contract liability complexity |
| Healthcare / pharma / medtech | 2 | Inventory reserves and product risk |

Total:

15 filers including the current 3.

This would be more robust, but it may require much more claim coding and source validation. It is probably unnecessary unless the paper intends to make stronger claims about general applicability.

## Recommended Additional Tasks

If expanding the demonstration, the paper should not run full LLM/coding for every possible combination. A scoped extension is better.

### Task 1: Filing-Level Retrieval Diagnostics

For each additional filer, collect:

1. filing metadata;
2. text chunk count;
3. revenue-related chunk count;
4. inventory-related chunk count;
5. XBRL fact count;
6. revenue-related fact count;
7. inventory-related fact count;
8. relation path count;
9. extension concept count, if available;
10. retrieval context availability for each construct.

Purpose:

Show that the framework can be applied across different reporting environments without fully coding all LLM outputs.

### Task 2: Limited LLM Runs

Run only selected conditions for the additional filers:

Option A:

Hybrid only for both constructs.

Option B:

Text, XBRL, and hybrid for one construct per filer.

Option C:

Full four-condition design for a smaller subset.

Recommended choice:

Option B.

Reason:

It is sufficient to test whether retrieval-created information environments differ across settings without exploding the workload.

### Task 3: Claim-Level Coding Subsample

Code a limited number of claims per additional filer:

1. top 3 to 5 claims per output;
2. focus on source use, graph validity, and integration;
3. keep audit-valid scores illustrative unless expert-reviewed.

Purpose:

Demonstrate generality of the coding protocol, not estimate performance.

### Task 4: Boundary Case Table

Create a table showing where the framework works differently:

| Filer Type | Retrieval Challenge | Validity Dimension Most Affected | Implication |
|---|---|---|---|
| Retail | Many inventory facts and disclosures | Selection | Need retrieval filters |
| Software | Revenue narrative more important than inventory | Construct fit | XBRL inventory retrieval may be inappropriate |
| Manufacturing | Complex cost/inventory relations | Representation | Need period/unit/context preservation |
| Smaller filer | Sparse disclosures | Omission | LLM output may reflect retrieval poverty |

## Reviewer Decision Logic

### If No Additional Cases Are Added

The paper remains viable only if it keeps claims narrow:

> We provide a methodological framework and demonstrate its application in three familiar SEC filers.

Reviewer risk:

Moderate. Some reviewers may see the demonstration as too hand-picked.

### If 6 Additional Filers Are Added

The paper becomes stronger:

> We provide a deep three-filer demonstration and a bounded robustness extension showing that the framework applies across varied reporting environments.

Reviewer risk:

Lower. This should be enough for a methodology paper.

### If 12 Additional Filers Are Added

The paper becomes much stronger but may drift toward empirical benchmarking:

> We provide broader evidence that retrieval-environment validity concerns appear across industries and reporting complexity.

Reviewer risk:

Mixed. Stronger evidence, but higher workload and greater risk that reviewers expect statistical analysis, coder reliability, and formal sampling justification.

## Recommended Decision

Add a bounded robustness extension of **6 additional filers**, for a total of 9 filers.

Do not attempt a broad archival-style empirical sample at this stage.

The paper is a methodology paper. A large sample could distract from the conceptual contribution and create expectations for hypothesis testing, statistical inference, and population-level claims. A 9-filer maximum-variation design is a better fit because it strengthens external plausibility while preserving the paper's methodological identity.

## Suggested Manuscript Language

Add to the demonstration section:

> Our primary demonstration uses three familiar filers to allow detailed source tracing and claim-level illustration. To reduce the risk that the demonstration reflects only idiosyncratic features of these firms, we recommend a bounded robustness extension using additional filers selected for variation in firm size, industry, reporting complexity, and construct fit. The purpose of this extension is not statistical generalization, but theoretical sampling: to show that retrieval-environment validity can be evaluated across different reporting environments and to identify boundary conditions for text, XBRL, and hybrid retrieval.

Add to limitations:

> Because the current demonstration is not a population-level empirical study, it does not estimate the prevalence of retrieval failure modes across SEC filers. Future studies can extend the framework using larger samples when their research questions concern prevalence, performance, or cross-sectional determinants of retrieval validity.

## Implication for Current Project Plan

The project plan should add a pre-submission decision point:

> Decide whether to keep the demonstration as a three-filer deep methodological illustration or add a six-filer bounded robustness extension before submission.

Recommended path:

1. Preserve the current three filers for main-text examples.
2. Add six additional filers for appendix-level robustness diagnostics.
3. Limit the additional work to retrieval diagnostics and selected LLM/coding checks.
4. Avoid broad performance claims.

## Final Reviewer Assessment

From a reviewer perspective, the current three-filer demonstration is acceptable only if the claims remain narrow. However, because the demonstration will likely carry substantial persuasive weight, a bounded expansion would materially strengthen the paper.

The best balance is not a large accounting-style empirical sample. It is a maximum-variation methodological extension that shows the framework works across different reporting environments while preserving deep traceability.
