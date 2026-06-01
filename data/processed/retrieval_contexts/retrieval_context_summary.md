# Phase 6 Retrieval Context Build Summary

Generated prompt-ready contexts from the shared filer manifest.

| Filer | Role | Construct | Text Words | XBRL Words | Hybrid Words | Baseline Words |
|---|---|---|---:|---:|---:|---:|
| NKE | main_deep_case | revenue | 537 | 624 | 748 | 10 |
| NKE | main_deep_case | inventory | 422 | 628 | 715 | 10 |
| SBUX | main_deep_case | revenue | 478 | 708 | 764 | 10 |
| SBUX | main_deep_case | inventory | 521 | 514 | 560 | 10 |
| TGT | main_deep_case | revenue | 566 | 577 | 761 | 10 |
| TGT | main_deep_case | inventory | 786 | 556 | 742 | 10 |
| WMT | bounded_extension | revenue | 720 | 653 | 925 | 10 |
| WMT | bounded_extension | inventory | 629 | 568 | 676 | 10 |
| HD | bounded_extension | revenue | 742 | 631 | 857 | 10 |
| HD | bounded_extension | inventory | 732 | 569 | 807 | 10 |
| CAT | bounded_extension | revenue | 800 | 664 | 870 | 10 |
| CAT | bounded_extension | inventory | 511 | 535 | 579 | 10 |
| PFE | bounded_extension | revenue | 962 | 672 | 901 | 10 |
| PFE | bounded_extension | inventory | 624 | 585 | 772 | 10 |
| MSFT | bounded_extension | revenue | 601 | 224 | 555 | 10 |
| MSFT | bounded_extension | inventory | 269 | 203 | 298 | 10 |
| CROX | bounded_extension | revenue | 698 | 639 | 881 | 10 |
| CROX | bounded_extension | inventory | 733 | 589 | 761 | 10 |

## Output Files

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/retrieval_logs/retrieval_log.csv`
- `data/processed/retrieval_contexts/*_context.txt`
- `data/processed/prompts/*_prompt.txt`