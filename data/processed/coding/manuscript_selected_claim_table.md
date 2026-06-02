# Selected Claim-Level Demonstration Examples

| Example | Claim ID | Filer | Construct | Condition | Claim Summary | Text Source | XBRL Source | Text | Graph | Audit | Integrated | Inference Consequence |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| E01 | C058 | Starbucks | Inventory | Hybrid | Inventory reserves were $56.6 million as of September 28, 2025. | T-SBUX-INVENTORY-015 | F-SBUX-0034 | 1 | 1 | 1 | 1 | Hybrid retrieval supports direct narrative-XBRL corroboration for a bounded factual claim. |
| E02 | C013 | Nike | Revenue | Hybrid | Refund liability increased from $799 million to $1.277 billion and may be a revenue valuation risk cue. | None | F-NKE-0253; F-NKE-0252 | 0 | 0.5 | 1 prelim. | 0 | The claim is graph-grounded but effectively XBRL-only despite the hybrid condition. |
| E03 | C014 | Nike | Revenue | Hybrid | Digital commerce platform failure risk may map to revenue completeness and occurrence. | T-NKE-REVENUE-021 | None | 0.5 | NA | 1 prelim. | 0 | The claim is text-supported but does not use XBRL despite the hybrid condition. |
| E04 | C016 | Nike | Revenue | LLM-only | Context is insufficient to identify filing-specific revenue risk cues. | None | None | NA | NA | 1 | NA | The no-context baseline supports traceability diagnosis rather than performance comparison. |
| E05 | C090 | Target | Inventory | Hybrid | Net inventory was $12.740 billion as of February 1, 2025. | None | F-TGT-0007 | 0 | 1 | 1 prelim. | 0 | The claim is graph-grounded but does not integrate the available Target inventory narrative context. |

Note: Audit-boundary diagnostics marked preliminary require expert review before final audit-judgment claims. Evidence-use type and integrated correctness are separately evaluated for protocol reliability in the independent coding sample.
