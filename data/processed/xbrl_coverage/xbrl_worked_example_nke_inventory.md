# XBRL Worked Example: NKE Inventory Valuation

## Purpose

This worked example documents a source-to-claim trace for the NKE inventory valuation task. It shows how XBRL facts and relation paths were rendered into the LLM retrieval context and how selected claims were coded. The example supports retrieval-environment validity and representation transparency; it does not establish audit evidence sufficiency.

## Source Artifacts

| Artifact | Identifier | Details |
|---|---|---|
| Filing | NKE 10-K / Inline XBRL | `nke-20250531_htm.xml`, `nke-20250531_pre.xml`, `nke-20250531_cal.xml`, `nke-20250531_def.xml` |
| Retrieval context | XBRL-only | `data/processed/retrieval_contexts/nke_inventory_xbrl_context.txt` |
| Retrieval context | Hybrid | `data/processed/retrieval_contexts/nke_inventory_hybrid_context.txt` |
| Output | XBRL-only | `data/processed/llm_outputs/gemma4_31b_full/text/nke_inventory_xbrl_output.txt` |
| Output | Hybrid | `data/processed/llm_outputs/gemma4_31b_full/text/nke_inventory_hybrid_output.txt` |

## Fact Trace

| Fact ID | Concept | Value | Unit | Period | Dimensions | Construct Family |
|---|---|---:|---|---|---|---|
| F-NKE-0026 | InventoryValuationReserves | 233000000 | iso4217:USD | instant:2025-05-31 | none | valuation reserve or obsolescence |
| F-NKE-0027 | InventoryValuationReserves | 155000000 | iso4217:USD | instant:2024-05-31 | none | valuation reserve or obsolescence |
| F-NKE-0353 | InventoryFinishedGoodsNetOfReserves | 3806000000 | iso4217:USD | instant:2023-05-31 | North America segment | inventory balance / components |
| F-NKE-0354 | InventoryFinishedGoodsNetOfReserves | 2167000000 | iso4217:USD | instant:2023-05-31 | EMEA segment | inventory balance / components |
| F-NKE-0355 | InventoryFinishedGoodsNetOfReserves | 973000000 | iso4217:USD | instant:2023-05-31 | Greater China segment | inventory balance / components |

## Relation-Path Trace

| Path ID | Relation Type | Source Concept | Target Concept | Role | Representation Use |
|---|---|---|---|---|---|
| X-NKE-0056 | calculation | us-gaap:AssetsCurrent | us-gaap:InventoryFinishedGoodsNetOfReserves | Consolidated balance sheets | Locates finished-goods inventory within current assets |
| X-NKE-0067 | definition | nke:SignificantAccountingPoliciesLineItems | us-gaap:InventoryValuationReserves | Significant accounting policies details | Locates inventory valuation reserves in policy/detail structure |
| X-NKE-0015 | presentation | nke:SignificantAccountingPoliciesLineItems | us-gaap:InventoryValuationReserves | Significant accounting policies details | Shows presentation linkage for the reserve concept |

## Rendered Context

The rendered XBRL-only context included fact IDs, concept names, values, units, periods, dimensions, path IDs, relation types, source concepts, target concepts, arcroles, and role URIs. The hybrid context added filing text discussing the reserve policy and the reported reserve increase from 2024 to 2025.

## Claim Trace

| Claim ID | Condition | Claim Summary | Sources Used | Coding Interpretation |
|---|---|---|---|---|
| C021 | XBRL-only | 2025 inventory valuation reserves were 233 million USD | F-NKE-0026 | Graph-valid factual claim bounded to one reported instant |
| C023 | XBRL-only | Reserve increase from 155 million USD to 233 million USD is a risk cue for inventory valuation | F-NKE-0026; F-NKE-0027 | Partly graph-valid because the numeric change is supported, but the risk inference exceeds XBRL facts alone |
| C027 | Hybrid | 2025 reserve was 233 million USD, up from 155 million USD in 2024 | Text Chunk 2; F-NKE-0026; F-NKE-0027 | Integrated factual claim supported by both retrieved text and XBRL facts |
| C029 | Hybrid | Reserve increase is a risk cue for adequacy of the valuation reserve | Text Chunk 2; F-NKE-0026; F-NKE-0027 | Integrated risk-cue claim, but reserve adequacy remains an audit-boundary diagnostic rather than an audit conclusion |

## Representation-Risk Example

Fact IDs F-NKE-0353, F-NKE-0354, and F-NKE-0355 provide segment-level finished-goods inventory balances only for instant:2023-05-31. They should not be used as current 2025 segment-level inventory evidence. A claim that maps 2025 reserve adequacy to specific geographic segments using only these facts would require a period-mismatch warning. This example illustrates why period and dimension metadata must be preserved in the rendered context and in claim-level coding.

## Boundary

This example demonstrates source traceability and representation checks. It does not show that the inventory reserve is sufficient, that inventory is fairly valued, or that audit evidence has been obtained.
