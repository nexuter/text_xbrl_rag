# Final Reviewer-Facing Appendix Package

Revision note: This appendix package was superseded by the current supplement in `submission/Online_Supplement_Appendix.md` and by `plan/89_demonstration_scope_and_validation_revision_log.md`. The current submission package uses 72 outputs, 48 extension outputs, 281 preliminary coded claims, and 464 retrieval-log rows.

## Purpose

This package converts the prior project-log appendix materials into a reviewer-facing appendix structure for the AJPT Methodological Papers submission.

The appendix should help reviewers evaluate whether the manuscript's methodological demonstration is transparent, reproducible, and properly bounded. It should not read as a technical file dump or as evidence of retrieval-method performance.

## Appendix Design Principle

The appendix is organized around the paper's central methodological construct:

> Retrieval-environment validity: the extent to which the dynamically retrieved information environment supplied to an LLM aligns with the audit construct the researcher intends to study.

Each appendix item should answer one of four reviewer questions:

1. What information was available for retrieval?
2. What information was actually retrieved and shown to the LLM?
3. How were LLM outputs converted into claim-level research variables?
4. What claims are supported, and what claims remain outside the data?

## Reviewer-Facing Appendix Map

| Appendix | Title | Reviewer Question | Validity Function | Main-Text Link |
|---|---|---|---|---|
| A | Source Corpus and Filer Manifest | What filed documents created the source universe? | Selection, traceability | Demonstration data sources |
| B | Text Retrieval Store and Chunking | How was narrative filing evidence represented and retrieved? | Selection, representation, stability | Text retrieval condition |
| C | XBRL Fact and Relation Store | How were management-reported accounting facts and relations represented? | Representation, traceability | XBRL relational retrieval condition |
| D | Prompt and Retrieval Context Archive | What exactly did the LLM see? | Traceability, separability | Retrieval-condition implementation |
| E | LLM Run Configuration and Output Archive | Were outputs generated under controlled model settings? | Stability, separability | LLM execution design |
| F | Claim-Level Coding Package | How were outputs converted into correctness and evidence-use variables? | Traceability, representation | Correctness protocol |
| G | Source Spot Checks and Selected Examples | Can selected claims be traced back to filed evidence? | Traceability, representation | Main demonstration examples |
| H | Bounded Extension Evidence | Does the protocol remain applicable beyond the three deep cases? | Selection, separability | Bounded extension |
| I | Sensitivity Guidance and Boundary Conditions | What checks are needed for stronger empirical claims? | Stability, separability | Discussion and limitations |

## Appendix A. Source Corpus And Filer Manifest

### Purpose

Appendix A documents the source universe used to construct the retrieval environments. It should reassure reviewers that the demonstration is built from actual SEC filing and Inline XBRL artifacts rather than manually curated examples.

### Included Artifacts

| Artifact | Location |
|---|---|
| Filing download manifest | `data/processed/download_manifest.md` |
| Machine-readable download manifest | `data/processed/download_manifest.json` |
| Extraction summary | `data/processed/extraction_summary.md` |
| Machine-readable extraction summary | `data/processed/extraction_summary.json` |
| Raw SEC files | `data/raw_sec/` |
| Filer manifest | `config/filer_manifest.json` |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Filer identity | Company, ticker, CIK, sample role, and construct role |
| Filing identity | Form type, fiscal year, accession number, and source URL |
| Source status | Raw filing retained, processed text available, XBRL facts extracted |
| Sample role | Main deep case, bounded extension, or backup filer |
| Exclusions | Failed downloads, parsing exceptions, or unused backup filers |

### What This Validates

Appendix A validates the source selection trail for the main and bounded-extension demonstrations. It supports the claim that the paper uses real filed data across nine active filers.

### What This Does Not Validate

Appendix A does not establish population representativeness, audit evidence quality, or SEC-filer generalizability.

## Appendix B. Text Retrieval Store And Chunking

### Purpose

Appendix B makes text retrieval inspectable at the chunk level. It should prevent the phrase "text retrieval" from being treated as a black box.

### Included Artifacts

| Artifact | Location |
|---|---|
| Combined text chunk table | `data/processed/text_chunks/text_chunks.csv` |
| Filer-level text chunk JSON files | `data/processed/text_chunks/` |
| Text retrieval specification | `plan/31_phase7_text_retrieval_specification.md` |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Chunk identifier | Stable ID used in prompts, logs, and coding |
| Source metadata | Filer, filing, topic label, and source section where available |
| Chunking rule | Chunk unit, target size, overlap policy, and count rule |
| Retrieval operator | Keyword-ranked contextual retrieval in the current demonstration |
| Retrieval parameters | Construct query, source filter, top-k rule, and prompt inclusion rule |
| Implementation boundary | Vector database and embedding metadata are guidance for future Tier 2/Tier 3 studies, not implemented performance evidence here |

### Current Demonstration Diagnostic Counts

| Ticker | Text Chunks |
|---|---:|
| NKE | 184 |
| SBUX | 122 |
| TGT | 103 |
| WMT | 120 |
| HD | 125 |
| CAT | 213 |
| PFE | 196 |
| MSFT | 150 |
| CROX | 164 |

### What This Validates

Appendix B validates that narrative retrieval units were constructed and logged consistently enough for source traceability and claim-level coding.

### What This Does Not Validate

Appendix B does not claim that the current prototype is production vector RAG, nor does it compare chunk-size, overlap, embedding-model, or vector-index performance.

## Appendix C. XBRL Fact And Relation Store

### Purpose

Appendix C documents how XBRL facts and relation paths were extracted and represented as relational retrieval inputs. It should make clear that XBRL is management-reported structured data, not audit evidence or ground truth.

### Included Artifacts

| Artifact | Location |
|---|---|
| Combined XBRL fact table | `data/processed/xbrl_facts/xbrl_facts.csv` |
| Filer-level XBRL fact JSON files | `data/processed/xbrl_facts/` |
| Combined XBRL relation-path table | `data/processed/xbrl_paths/xbrl_paths.csv` |
| Filer-level XBRL path JSON files | `data/processed/xbrl_paths/` |
| XBRL relation and ontology specification | `plan/32_phase7_xbrl_relation_ontology_specification.md` |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Fact schema | Fact ID, concept QName, label, value, unit, decimals, period, and dimensions |
| Relation schema | Path ID, source concept, target concept, relation type, arcrole, role, and depth |
| Taxonomy handling | Taxonomy/linkbase source, year or version, and extension-concept policy |
| Retrieval rule | Seed concepts, relation filters, path-depth rule, and construct-specific filters |
| Ontology boundary | RDF/OWL mapping is a portability specification unless an export is explicitly produced |

### Current Demonstration Diagnostic Counts

| Ticker | XBRL Facts | XBRL Relation Paths | Diagnostic Meaning |
|---|---:|---:|---|
| NKE | 365 | 99 | Main deep case with usable relation paths |
| SBUX | 135 | 210 | Main deep case with rich relation-path evidence |
| TGT | 102 | 79 | Main deep case with moderate relation-path evidence |
| WMT | 141 | 109 | Retail extension case |
| HD | 173 | 174 | Specialty-retail extension case |
| CAT | 1,047 | 574 | High-complexity industrial stress case |
| PFE | 336 | 272 | Pharma/product-risk extension case |
| MSFT | 144 | 0 | Revenue boundary case showing relation-path scarcity |
| CROX | 123 | 102 | Mid-size consumer-product extension case |

### What This Validates

Appendix C validates that XBRL relational retrieval creates a distinct information environment from narrative text retrieval.

### What This Does Not Validate

Appendix C does not validate audit assertions, audit evidence sufficiency, or superiority of XBRL retrieval. It also does not claim a full production RDF/OWL triple store or GraphRAG implementation.

## Appendix D. Prompt And Retrieval Context Archive

### Purpose

Appendix D is the core traceability appendix. It answers the reviewer question:

> What exactly did the LLM see?

### Included Artifacts

| Artifact | Location |
|---|---|
| Retrieval context manifest | `data/processed/retrieval_contexts/context_manifest.csv` |
| Machine-readable context manifest | `data/processed/retrieval_contexts/retrieval_context_manifest.json` |
| Retrieval context summary | `data/processed/retrieval_contexts/retrieval_context_summary.md` |
| Retrieval context files | `data/processed/retrieval_contexts/` |
| Prompt files | `data/processed/prompts/` |
| Retrieval log | `data/processed/retrieval_logs/retrieval_log.csv` |
| Hybrid context workflow | `plan/33_phase7_hybrid_context_and_llm_workflow.md` |

### Current Scope

| Item | Count |
|---|---:|
| Main deep-case prompt/context conditions | 24 |
| Bounded-extension prompt/context conditions | 18 |
| Total prompt/context conditions | 42 |
| Retrieval log rows | 313 |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Run identifier | Filer, construct, retrieval condition, and run ID |
| Final prompt | Full rendered prompt supplied to the model |
| Retrieved context | Full text/XBRL/hybrid context supplied to the model |
| Source IDs | Text chunk IDs, XBRL fact IDs, and XBRL path IDs preserved |
| Assembly rule | Context ordering, formatting, truncation, and budget policy |
| LLM-only baseline | Diagnostic baseline used for separability and pretraining-contamination concerns |

### What This Validates

Appendix D validates traceability and separability by preserving the actual information environment supplied to the LLM.

### What This Does Not Validate

Appendix D does not show that retrieved information was sufficient for an audit conclusion. It only documents what information was visible to the model.

## Appendix E. LLM Run Configuration And Output Archive

### Purpose

Appendix E documents model execution settings and output preservation. It should make the LLM run reproducible enough for methodological review without turning the paper into a model benchmark.

### Included Artifacts

| Artifact | Location |
|---|---|
| Main run summary and manifest | `data/processed/llm_outputs/gemma4_31b_full/` |
| Main raw JSON and text outputs | `data/processed/llm_outputs/gemma4_31b_full/raw_json/`; `data/processed/llm_outputs/gemma4_31b_full/text/` |
| Extension run summary and manifest | `data/processed/llm_outputs/gemma4_31b_extension/` |
| Extension raw JSON and text outputs | `data/processed/llm_outputs/gemma4_31b_extension/raw_json/`; `data/processed/llm_outputs/gemma4_31b_extension/text/` |
| LLM output harness memo | `plan/20_phase6_llm_output_harness.md` |
| Model-selection memo | `plan/21_phase6_model_selection_memo.md` |
| `gemma4:31b` validation memo | `plan/23_phase6_gemma4_31b_model_fit_validation.md` |
| LLM results validation log | `plan/52_llm_results_validation_log.md` |

### Current Run Configuration

| Field | Value |
|---|---|
| Provider | Ollama |
| Model | `gemma4:31b` |
| Temperature | 0.0 |
| Main outputs | 24 |
| Extension outputs | 18 |
| Total outputs | 42 |
| Output errors | 0 |

### What This Validates

Appendix E supports stability and separability by showing that outputs were generated under a consistent local model configuration.

### What This Does Not Validate

Appendix E does not establish that `gemma4:31b` is generally superior for audit research, nor does it provide cross-model robustness.

## Appendix F. Claim-Level Coding Package

### Purpose

Appendix F shows how LLM outputs were converted into claim-level research variables. This is central to the paper's data/variable-construction contribution.

### Included Artifacts

| Artifact | Location |
|---|---|
| Main claim-level coding table | `data/processed/coding/claim_level_coding_gemma4_31b.csv` |
| Main coding summary | `data/processed/coding/claim_coding_summary.md` |
| Main inference-shift table | `data/processed/coding/inference_shift_table_prelim.csv` |
| Main failure-mode examples | `data/processed/coding/failure_mode_examples_prelim.csv` |
| Extension claim-level coding table | `data/processed/coding/claim_level_coding_gemma4_31b_extension.csv` |
| Extension coding summary | `data/processed/coding/claim_coding_summary_gemma4_31b_extension.md` |
| Extension inference-shift table | `data/processed/coding/inference_shift_table_prelim_gemma4_31b_extension.csv` |
| Extension failure-mode examples | `data/processed/coding/failure_mode_examples_prelim_gemma4_31b_extension.csv` |
| Correctness protocol | `plan/16_phase5_correctness_protocol.md` |

### Current Coding Scope

| Item | Count |
|---|---:|
| Main coded claims | 94 |
| Extension coded claims | 88 |
| Total coded claims | 182 |
| Factual claims | 76 |
| Risk/assertion-mapping claims | 99 |
| Insufficient-context claims | 7 |
| Claims requiring manual/expert review | 182 |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Claim ID | Stable claim identifier |
| Output link | Source output and retrieval condition |
| Claim type | Factual, risk/assertion, or insufficient context |
| Evidence-use type | Text, XBRL, both, none, or unclear |
| Correctness layers | Text-supported, graph-valid, audit-valid, and integrated |
| Failure mode | Omission, distortion, attribution failure, integration failure, relation hallucination, source overreach, etc. |
| Coding boundary | Audit-valid and integrated scores are preliminary author-coded diagnostics unless reviewed by audit-domain experts |

### What This Validates

Appendix F validates that the paper's demonstration is claim-level rather than anecdotal. It also operationalizes retrieval artifacts and LLM outputs as research variables.

### What This Does Not Validate

Appendix F does not provide final expert audit-judgment evidence. It should not be interpreted as model performance evidence or as a ranking of retrieval methods.

## Appendix G. Source Spot Checks And Selected Examples

### Purpose

Appendix G links selected manuscript examples back to raw and processed filing evidence.

### Included Artifacts

| Artifact | Location |
|---|---|
| Selected manuscript examples | `data/processed/coding/selected_manuscript_examples_prelim.csv` |
| Manuscript selected claim table | `data/processed/coding/manuscript_selected_claim_table.md` |
| Source spot-check table | `data/processed/coding/selected_source_spot_check.csv` |
| Reviewer validation memo | `plan/26_phase6_reviewer_validation_of_coded_examples.md` |
| Source graph spot-check memo | `plan/28_phase6_source_graph_spot_check_memo.md` |

### Required Reviewer Disclosures

| Field | Required Disclosure |
|---|---|
| Example ID | Stable selected-example identifier |
| Claim ID | Link to coded claim |
| Retrieved source IDs | Text chunk, XBRL fact, and XBRL path IDs |
| Source verification | Processed-source and raw-filing location where feasible |
| Validity lesson | What the example demonstrates about retrieval-environment validity |

### What This Validates

Appendix G validates that the selected manuscript examples are source-traceable and are not cherry-picked without a coding trail.

### What This Does Not Validate

Appendix G does not validate all 182 claims independently. It provides selected spot checks and reviewer-facing examples.

## Appendix H. Bounded Extension Evidence

### Purpose

Appendix H addresses the concern that the framework might depend on three hand-picked familiar filers.

### Included Artifacts

| Artifact | Location |
|---|---|
| Generalizability assessment | `plan/48_demonstration_scope_generalizability_assessment.md` |
| Extension filer selection memo | `plan/49_bounded_robustness_extension_filer_selection.md` |
| Extension data and diagnostics log | `plan/50_bounded_robustness_extension_data_and_diagnostics_log.md` |
| Extension LLM and coding log | `plan/51_bounded_robustness_extension_llm_and_coding_log.md` |
| Extension manuscript integration package | `plan/53_bounded_extension_manuscript_integration_package.md` |

### Extension Summary

| Ticker | Company | Industry / Setting | Construct | Role |
|---|---|---|---|---|
| WMT | Walmart | Mega-scale retail | Inventory | Scale and retail inventory extension |
| HD | Home Depot | Specialty retail | Inventory | Specialty retail extension |
| CAT | Caterpillar | Industrial manufacturing | Inventory | High-complexity XBRL stress case |
| PFE | Pfizer | Pharma / healthcare products | Inventory | Product-risk reporting extension |
| MSFT | Microsoft | Software/cloud | Revenue | Revenue boundary case with relation-path scarcity |
| CROX | Crocs | Mid-size consumer products | Inventory | Size variation and consumer-product setting |

### Current Extension Scope

| Item | Count |
|---|---:|
| Extension filers | 6 |
| Extension prompt/context conditions | 18 |
| Extension outputs | 18 |
| Extension coded claims | 88 |

### What This Validates

Appendix H validates that the protocol can be applied across varied reporting environments and that boundary cases are visible through retrieval diagnostics.

### What This Does Not Validate

Appendix H does not validate population-level prevalence, retrieval-method superiority, or general SEC-filer performance.

## Appendix I. Sensitivity Guidance And Boundary Conditions

### Purpose

Appendix I separates what the current Tier 1 methodological demonstration performs from what future Tier 2 or Tier 3 studies should report when making stronger empirical or system-performance claims.

### Included Artifacts

| Artifact | Location |
|---|---|
| Reporting checklist and sensitivity table | `plan/34_phase7_reporting_checklist_and_sensitivity_table.md` |
| Phase 7 reviewer stress test | `plan/35_phase7_reviewer_stress_test.md` |
| Tables and figures package | `plan/41_phase8_tables_and_figures_package.md` |

### Sensitivity Checks Not Claimed As Completed

| Check | Why It Matters | Current Treatment |
|---|---|---|
| Chunk-size variation | Selection and representation validity | Guidance, not completed benchmark |
| Chunk-overlap variation | Boundary omissions in text retrieval | Guidance, not completed benchmark |
| Embedding model variation | Vector-retrieval stability | Not applicable to current keyword prototype |
| Top-k variation | Retrieval selection sensitivity | Guidance, not completed benchmark |
| XBRL traversal-depth variation | Relation coverage versus noise | Guidance, not completed benchmark |
| Relation-type filters | Construct alignment of XBRL retrieval | Guidance, not completed benchmark |
| Token-budget equalization | Separability of text and XBRL effects | Conceptual control, not full sensitivity run |
| Model variation | Model-specific output behavior | Model selection justified; cross-model comparison not claimed |
| Prompt variation | Prompt stability | Guidance, not completed benchmark |
| Independent expert coding | Audit-valid correctness | Needed for stronger audit-judgment claims |

### What This Validates

Appendix I validates that the manuscript knows where the current demonstration ends and where stronger future designs begin.

### What This Does Not Validate

Appendix I does not provide completed sensitivity results. It is reporting guidance and boundary-setting material.

## Cross-Appendix Evidence Trail

The reviewer should be able to follow this chain:

| Step | Evidence Object | Appendix |
|---|---|---|
| 1 | SEC filing and Inline XBRL source | A |
| 2 | Extracted text chunk or XBRL fact/path | B or C |
| 3 | Retrieved evidence selected for a run | D |
| 4 | Final prompt shown to the LLM | D |
| 5 | Raw LLM output | E |
| 6 | Segmented claim | F |
| 7 | Claim-level evidence-use and correctness coding | F |
| 8 | Selected source spot check | G |
| 9 | Extension and boundary-condition evidence | H |
| 10 | Sensitivity limits and future reporting requirements | I |

## Data-Supported Claims For Main Text

The appendix supports the following manuscript claims:

1. The demonstration uses actual SEC filing text and Inline XBRL data.
2. The retrieval environments are inspectable through source IDs, retrieval logs, prompt contexts, and output archives.
3. The demonstration includes 42 retrieval-conditioned outputs and 182 preliminary coded claims.
4. Hybrid retrieval labels do not guarantee integrated evidence use: only 7 of 60 hybrid-condition claims used both text and XBRL, while 41 used text only and 12 used XBRL only.
5. Source traceability is strong in the current archive: validation identified no invalid source references.
6. The bounded extension shows that the protocol remains applicable across varied reporting environments, while also revealing boundary cases such as CAT complexity and MSFT relation-path scarcity.

## Claims The Appendix Does Not Support

The appendix should explicitly prevent the following inferences:

1. Hybrid retrieval is superior to text or XBRL retrieval.
2. XBRL relational retrieval improves audit reasoning.
3. `gemma4:31b` demonstrates general audit expertise.
4. The observed failure-mode frequencies generalize to SEC filers.
5. The preliminary audit-valid or integrated scores are final expert evidence.
6. The current prototype implements production vector RAG, RDF/OWL graph storage, or GraphRAG performance evaluation.

## Recommended Appendix Opening Paragraph

The following paragraph can open the final appendix:

> This appendix documents the source corpus, retrieval artifacts, prompts, LLM outputs, claim-level coding, and validation checks for the methodological demonstration. The purpose is to make the retrieval-created information environment inspectable. The appendix should be read as transparency and reproducibility support for a methodological demonstration, not as a performance benchmark. XBRL facts and relations are management-reported structured data and are not treated as audit evidence or ground truth. Audit-valid and integrated-correctness coding is preliminary unless independently reviewed by audit-domain experts.

## Accept-Level Appendix Readiness Checklist

| Requirement | Status | Remaining Action |
|---|---|---|
| Source corpus documented | Ready | Verify accession and URL formatting in final manuscript appendix |
| Text retrieval units documented | Ready | Include chunking rule and keyword-prototype boundary |
| XBRL facts and paths documented | Ready | Preserve management-reported-data boundary |
| Prompt/context archive documented | Ready | Ensure all final manuscript examples cite run IDs and source IDs |
| LLM settings documented | Ready | Add exact local model version string if available at final submission |
| Claim-level coding documented | Ready with boundary | Add expert review or keep audit-valid coding explicitly preliminary |
| Selected source spot checks documented | Ready | Use only source-verified examples in main text |
| Bounded extension documented | Ready | Frame as maximum-variation methodological extension |
| Sensitivity limits documented | Ready | Do not imply sensitivity tests were completed |
| Reviewer-facing structure | Ready after this package | Use this file rather than project-log ordering |

## Final Reviewer Assessment

After this restructuring, the appendix is close to accept-level for a methodology paper if the manuscript preserves the same boundaries. The appendix provides a coherent evidence trail from filed source data to retrieval contexts, LLM outputs, claim-level variables, and selected source checks.

The largest remaining appendix-related risk is audit-validity interpretation. If the main manuscript treats audit-valid or integrated scores as final evidence, the appendix will not save the paper. If the manuscript uses those scores as preliminary diagnostics and bases its main inference on source traceability and claim-level evidence-use divergence, the appendix should be reviewer-defensible.
