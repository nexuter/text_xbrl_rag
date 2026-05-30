# Phase 6 Methodological Demonstration Subsection Draft

## Purpose

This file drafts the manuscript-ready demonstration subsection using the validated `gemma4:31b` examples.

The subsection is written to support the paper's central methodological claim:

> Retrieval design changes what researchers can validly infer from LLM audit outputs.

## Draft Subsection

### Methodological Demonstration

To illustrate how retrieval-environment validity changes the interpretation of LLM-based audit outputs, we conduct a descriptive demonstration using actual SEC filing text and Inline XBRL data. The purpose of the demonstration is not to rank retrieval methods or to estimate model performance. Instead, the demonstration shows how the same audit task supports different research inferences depending on the retrieved information environment.

We use three familiar SEC filers: Nike, Starbucks, and Target. Familiar firms make the output claims easier for readers to interpret, but they also increase the risk that the model may rely on general pretraining knowledge. We therefore evaluate claims only against retrieved filing text, retrieved XBRL facts and relation paths, and a no-context diagnostic baseline. Each LLM output is segmented into discrete claims and coded using four correctness layers: text-supported, graph-valid, audit-valid, and integrated correctness.

The main run uses `gemma4:31b` through local Ollama with temperature set to zero. The run covers three filers, two audit constructs, and four retrieval conditions: text-only retrieval, XBRL relational retrieval, hybrid retrieval, and an LLM-only diagnostic baseline. The full run produced 24 outputs and 94 segmented claims. We report selected examples in the main text and retain the full prompt, retrieval, output, and claim-coding trail in the appendix.

Table X reports five examples that illustrate how claim-level coding changes the inference a researcher can draw from the output.

### Table X

Selected claim-level demonstration examples

| Example | Claim ID | Filer | Construct | Condition | Claim Summary | Text Source | XBRL Source | Text | Graph | Audit | Integrated | Inference Consequence |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| E01 | C058 | Starbucks | Inventory | Hybrid | Inventory reserves were $56.6 million as of September 28, 2025. | T-SBUX-INVENTORY-015 | F-SBUX-0034 | 1 | 1 | 1 | 1 | Hybrid retrieval supports direct narrative-XBRL corroboration for a bounded factual claim. |
| E02 | C013 | Nike | Revenue | Hybrid | Refund liability increased from $799 million to $1.277 billion and may be a revenue valuation risk cue. | None | F-NKE-0253; F-NKE-0252 | 0 | 0.5 | 1 prelim. | 0.5 | The claim is graph-grounded but effectively XBRL-only despite the hybrid condition. |
| E03 | C014 | Nike | Revenue | Hybrid | Digital commerce platform failure risk may map to revenue completeness and occurrence. | T-NKE-REVENUE-021 | None | 0.5 | NA | 1 prelim. | 0.5 | The claim is text-supported but does not use XBRL despite the hybrid condition. |
| E04 | C016 | Nike | Revenue | LLM-only | Context is insufficient to identify filing-specific revenue risk cues. | None | None | NA | NA | 1 | NA | The no-context baseline supports traceability diagnosis rather than performance comparison. |
| E05 | C090 | Target | Inventory | Hybrid | Net inventory was $12.740 billion as of February 1, 2025. | None | F-TGT-0007 | 0 | 1 | 1 prelim. | 0.5 | The claim is graph-grounded but does not integrate the available Target inventory narrative context. |

Note: Audit-valid and integrated scores marked preliminary require expert review before final manuscript claims.

The first example shows the constructive role of hybrid retrieval. In the Starbucks inventory case, the model identifies a reported inventory reserve amount and cites both a narrative disclosure and a matching XBRL fact. This claim is text-supported, graph-valid, audit-valid as a bounded factual statement, and integrated because the text and XBRL evidence refer to the same accounting item and period. The valid inference is narrow but useful: hybrid retrieval can support direct narrative-XBRL corroboration for a bounded reported amount.

The second, third, and fifth examples show why hybrid retrieval should not be interpreted as automatically superior. In the Nike revenue case, the model receives both narrative and XBRL context, but one claim relies only on XBRL facts about refund liabilities, while another relies only on narrative disclosure about digital commerce platform risk. In the Target inventory case, the model reports a graph-valid inventory balance from XBRL but does not connect that balance to the available inventory-policy narrative. These claims may be useful. However, they do not demonstrate full integration of narrative and XBRL evidence. A naive evaluation might label them as successful hybrid retrieval outputs. The correctness protocol leads to a different inference: the hybrid condition created an opportunity for integrated reasoning, but the model's claim-level evidence use remained separated.

The fourth example illustrates the role of the LLM-only baseline. When no retrieved filing context is provided, the model states that the context is insufficient to identify filing-specific revenue risk cues. This output should not be interpreted as model failure. Instead, it functions as a traceability diagnostic. The no-context condition helps distinguish retrieval-supported reasoning from unsupported reliance on general company knowledge.

Overall, the demonstration shows why retrieval design should be treated as part of research design. Text retrieval supports narrative traceability, XBRL retrieval supports reported-relation traceability, and hybrid retrieval can support integrated correctness only when the model actually uses both evidence layers in the same claim. The relevant methodological question is therefore not which retrieval condition is "best," but what type of claim each retrieval-created information environment can validly support.

## Inference Shift

The demonstration changes the research inference in three ways.

First, an output produced under a hybrid condition should not be assumed to contain integrated reasoning. Claim-level source mapping can reveal that the model used only text or only XBRL for a given claim.

Second, XBRL-supported claims can be graph-valid without being sufficient audit evidence. XBRL facts and relation paths are management-reported structured information, not independent audit evidence.

Third, a no-context baseline is not merely a control condition for accuracy. It is a traceability diagnostic that helps researchers detect whether a model generates filing-specific claims without retrieved filing evidence.

## Reviewer-Safe Interpretation

The demonstration supports the following bounded claims:

- Retrieval design changes the evidence basis of LLM audit claims.
- Hybrid retrieval creates the possibility of integrated correctness but does not guarantee it.
- XBRL relational retrieval can preserve reported accounting facts and relations, but audit-valid inference requires professional qualification.
- Claim-level source mapping is necessary because retrieval condition labels do not reveal what evidence the model actually used.

The demonstration should not claim:

- Hybrid retrieval is generally more accurate.
- XBRL retrieval improves audit reasoning by itself.
- The LLM has audit expertise because preliminary audit-valid scores are high.
- Familiar-company outputs are free of pretraining-contamination risk.

## Appendix Links

Full supporting materials:

- `data/processed/llm_outputs/gemma4_31b_full/`
- `data/processed/coding/claim_level_coding_gemma4_31b.csv`
- `data/processed/coding/selected_manuscript_examples_prelim.csv`
- `data/processed/coding/manuscript_selected_claim_table.md`
- `plan/26_phase6_reviewer_validation_of_coded_examples.md`

## Remaining Work Before Manuscript Use

Before this subsection is treated as final manuscript evidence:

- expert-review the audit-valid and integrated coding for selected claims;
- verify cited text chunks and XBRL facts against original filing source files;
- decide whether to move preliminary scores into appendix-only language;
- add a short graph spot-check memo for the XBRL facts used in Table X.
