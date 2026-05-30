# Phase 6 Retrieval Context Construction Log

## Purpose

This file records the construction of prompt-ready retrieval contexts for the Phase 6 methodological demonstration.

This step converts the extracted SEC filing text, XBRL facts, and XBRL relation paths into controlled information environments for:

1. text-based contextual retrieval
2. XBRL-based relational retrieval
3. hybrid retrieval
4. LLM-only diagnostic baseline

No LLM outputs are generated in this step.

## Script

The retrieval contexts were generated with:

- `scripts/build_retrieval_contexts.py`

Inputs:

- `data/processed/text_chunks/text_chunks.csv`
- `data/processed/xbrl_facts/xbrl_facts.csv`
- `data/processed/xbrl_paths/xbrl_paths.csv`

Outputs:

- `data/processed/retrieval_contexts/context_manifest.csv`
- `data/processed/retrieval_contexts/retrieval_context_summary.md`
- `data/processed/retrieval_contexts/*_context.txt`
- `data/processed/prompts/*_prompt.txt`
- `data/processed/retrieval_logs/retrieval_log.csv`

## Retrieval Conditions Generated

The script generated prompt-ready inputs for:

| Filers | Constructs | Conditions | Prompt Files |
|---:|---:|---:|---:|
| 3 | 2 | 4 | 24 |

Conditions:

| Condition | Role |
|---|---|
| Text | Text-based contextual retrieval |
| XBRL | XBRL-based relational retrieval |
| Hybrid | Combined text and XBRL retrieval |
| LLM-only | Diagnostic baseline for traceability and pretraining-contamination risk |

## Context Lengths

| Filer | Construct | Text Words | XBRL Words | Hybrid Words | Baseline Words |
|---|---|---:|---:|---:|---:|
| NKE | revenue | 537 | 624 | 748 | 10 |
| NKE | inventory | 422 | 574 | 691 | 10 |
| SBUX | revenue | 478 | 708 | 764 | 10 |
| SBUX | inventory | 521 | 520 | 563 | 10 |
| TGT | revenue | 566 | 577 | 761 | 10 |
| TGT | inventory | 786 | 535 | 724 | 10 |

The context lengths are not exactly equalized, but they are close enough for a descriptive methodological demonstration. The final manuscript should avoid performance ranking and should disclose context length by condition.

## Retrieval Operator Rules

### Text Retrieval

Current implementation:

- keyword-ranked retrieval over extracted 10-K text chunks
- five text chunks selected per filer-construct pair
- prompt rendering truncates long chunks where needed
- retrieved chunk IDs are preserved

This is an inspectable retrieval prototype, not a production vector database.

Reviewer-safe interpretation:

> The text condition provides a transparent contextual retrieval baseline. It should be described as keyword-ranked contextual retrieval unless a later version adds embedding-based vector retrieval.

### XBRL Relational Retrieval

Current implementation:

- seed-pattern selection over extracted XBRL facts
- seed-pattern relation selection over presentation, calculation, and definition linkbases
- twelve facts selected per filer-construct pair
- ten relation paths selected per filer-construct pair
- concept IDs, labels, values, units, periods, dimensions, relation types, arcroles, and role URIs are preserved

This is sufficient for the first methodological demonstration because the objective is not to optimize graph retrieval, but to show how typed XBRL facts and relation paths create a different information environment from text chunks.

### Hybrid Retrieval

Current implementation:

- top three text chunks
- top eight XBRL facts
- top six XBRL relation paths
- text and XBRL components are separately labeled inside the context

This supports narrative-numeric integration while preserving enough logging to evaluate separability.

### LLM-Only Diagnostic Baseline

Current implementation:

- no retrieved filing context
- same prompt shell
- context states that no retrieved filing context is provided

The baseline is used only for traceability and pretraining-contamination diagnostics.

## Retrieval Log

The retrieval log is stored at:

- `data/processed/retrieval_logs/retrieval_log.csv`

Each row includes:

- retrieval ID
- filer
- construct
- condition component
- source ID
- source file
- retrieval operator
- query or seed concept family
- rank or relation depth
- score
- included conditions
- context word count
- notes

For each filer-construct pair, the log contains:

| Component | Rows |
|---|---:|
| Text chunks | 5 |
| XBRL facts | 12 |
| XBRL relation paths | 10 |

## Prompt Files

Prompt files are stored in:

- `data/processed/prompts/`

Examples:

| Prompt | Purpose |
|---|---|
| `sbux_revenue_hybrid_prompt.txt` | Starbucks revenue recognition hybrid context |
| `tgt_inventory_xbrl_prompt.txt` | Target inventory valuation XBRL relational context |
| `nke_inventory_llm_only_prompt.txt` | Nike inventory no-context diagnostic baseline |

Each prompt includes:

- company name
- fiscal year
- period ended
- accession number
- construct
- retrieval context
- instruction not to use outside company knowledge
- instruction not to treat XBRL as independent audit evidence

## Quality Checks Performed

### Check 1: Context Completeness

All 24 prompt files were generated.

### Check 2: Retrieval Log Completeness

For each filer and construct, retrieval logs include:

- 5 text chunks
- 12 XBRL facts
- 10 XBRL relation paths

### Check 3: Construct Fit

Manual spot checks showed:

- Starbucks revenue hybrid context includes stored value card, deferred revenue, loyalty program, and breakage-related text and XBRL facts.
- Target inventory XBRL context includes inventory net, inventory LIFO reserve period charge, cost of goods and services sold, and inventory-related relation paths.
- Nike revenue and inventory contexts include channel, revenue, inventory, cost of sales, and segment/geographic relation information.

### Check 4: Noise Reduction

Target inventory XBRL fact selection initially included deferred tax and self-insurance reserve concepts due to a broad `Reserve` keyword. The script was revised to narrow inventory seed selection and exclude noisy inventory-adjacent concepts.

## Current Limitations

- Text retrieval is keyword-ranked rather than embedding-based vector retrieval.
- XBRL relation selection is direct-arc selection rather than full depth-2 graph traversal.
- Context lengths are disclosed but not exactly token-equalized.
- Some extension concept labels remain unavailable when not resolved through the current label extraction.
- The contexts are ready for LLM prompting, but no model outputs have been generated yet.
- Retrieval ranking rules are transparent but simple; later sensitivity checks can compare semantic/vector retrieval or alternative traversal depth.

## Reviewer-Level Assessment

This step strengthens Phase 6 because it turns the demonstration design into inspectable retrieval-created information environments.

Reviewer-relevant strengths:

- Each condition is operationalized before observing LLM outputs.
- Retrieval logs make the context construction auditable.
- Text and XBRL components are separately traceable.
- Hybrid contexts preserve separability information through component labels.
- LLM-only prompts are available for pretraining-contamination diagnostics.

Remaining risk:

> The next step must run LLM outputs without altering retrieval contexts after seeing results. If contexts are changed after output generation, the case-selection and retrieval-design credibility would weaken.

## Next Step

Run the 24 prompt files:

1. 18 primary retrieval-condition prompts
2. 6 LLM-only diagnostic baseline prompts

Then preserve raw outputs and begin Phase 5 claim-level coding.
