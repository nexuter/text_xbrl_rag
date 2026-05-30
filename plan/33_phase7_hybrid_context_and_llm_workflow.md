# Phase 7 Hybrid Context Assembly and LLM Demonstration Workflow

## Purpose

This memo specifies how text retrieval and XBRL relational retrieval should be assembled into LLM prompts, and how the full demonstration pipeline should be reported for reproducibility.

Hybrid retrieval is not simply "more context." It creates a distinct information environment in which the LLM can, but may not, integrate narrative disclosures with reported accounting facts and relations. Therefore, hybrid context assembly must be disclosed separately from text and XBRL retrieval.

## Hybrid Retrieval Reporting Principle

Hybrid retrieval should be reported as a separate research condition with its own implementation choices:

- how much text context is included
- how much XBRL context is included
- how components are ordered
- whether source identifiers are preserved
- whether the prompt asks for integration
- whether the total token budget is equalized against single-source conditions

Without these disclosures, a reviewer cannot tell whether observed output differences arise from retrieval design, extra context volume, prompt wording, or model behavior.

## Hybrid Context Assembly Specification

| Field | Required Disclosure |
|---|---|
| `hybrid_condition_id` | Stable condition identifier. |
| `text_component_source` | Text retrieval log IDs included. |
| `xbrl_fact_component_source` | XBRL fact retrieval log IDs included. |
| `xbrl_relation_component_source` | XBRL relation retrieval log IDs included. |
| `text_component_budget` | Word or token budget allocated to text. |
| `xbrl_component_budget` | Word or token budget allocated to XBRL facts and paths. |
| `component_order` | Text first, XBRL first, interleaved, or grouped by construct. |
| `source_id_policy` | Whether chunk IDs, fact IDs, and path IDs are preserved. |
| `truncation_policy` | How long text or relation lists are shortened. |
| `deduplication_policy` | How overlapping text or facts are handled. |
| `integration_instruction` | Whether prompt asks the model to connect narrative and XBRL evidence. |
| `token_equalization_policy` | Whether context length is equalized across retrieval conditions. |

## Current Demonstration Hybrid Rule

The current Phase 6 demonstration uses:

| Component | Current Rule |
|---|---|
| Text component | Top three text chunks per filer-construct pair |
| XBRL fact component | Top eight XBRL facts per filer-construct pair |
| XBRL relation component | Top six relation paths per filer-construct pair |
| Order | Text context first, XBRL context second |
| Source IDs | Preserved in rendered context |
| Context labels | Text and XBRL sections separately labeled |
| Equalization | Context lengths disclosed but not exactly equalized |

Reviewer-safe wording:

> The hybrid condition combines separately logged text and XBRL components. We preserve source IDs and component labels so that hybrid outputs can be evaluated for integrated correctness rather than assumed to be integrated merely because both sources were present.

## Prompt Rendering Requirements

Prompt files should disclose:

| Prompt Element | Purpose |
|---|---|
| Company and filing identity | Prevents ambiguous task context. |
| Fiscal year and period | Anchors temporal scope. |
| Retrieval condition label | Identifies text, XBRL, hybrid, or baseline. |
| Retrieved context with source IDs | Enables traceability. |
| Instruction to use only provided context | Limits outside knowledge. |
| XBRL boundary instruction | Prevents treating reported relationships as audit evidence. |
| Claim format | Enables claim-level segmentation. |
| Limitation requirement | Reduces overconfident audit conclusions. |

## LLM Demonstration Workflow

The demonstration should be reported as a reproducible pipeline.

### Step 1: Source Acquisition

Inputs:

- SEC filing metadata
- 10-K HTML filing
- Inline XBRL instance and related artifacts

Outputs:

- raw filing directory
- source manifest
- accession-level metadata

Reporting requirements:

- CIK
- accession number
- filing type
- filing date
- fiscal period
- SEC source URL
- download date
- download script

### Step 2: Text Extraction

Inputs:

- raw 10-K HTML

Outputs:

- normalized filing text
- text chunk table

Reporting requirements:

- extraction script
- sections included
- sections excluded
- chunking rule
- chunk size and overlap
- source traceability rule

### Step 3: XBRL Extraction

Inputs:

- Inline XBRL/XML
- taxonomy/linkbase artifacts

Outputs:

- fact table
- concept table when available
- relation edge/path table

Reporting requirements:

- parser or extraction script
- fact fields extracted
- relation types extracted
- taxonomy year/version
- extension-concept treatment
- period/unit/dimension handling

### Step 4: Retrieval Store Construction

Text store:

- chunk table
- optional embeddings
- optional vector index

XBRL relation store:

- fact table
- relation edge table
- optional RDF/OWL export
- optional graph database index

Reporting requirements:

- retrieval unit
- retrieval operator
- ranking rule
- filters
- top-k or traversal depth
- context budget

### Step 5: Retrieval Execution

Conditions:

1. LLM-only baseline.
2. Text-based contextual retrieval.
3. XBRL-based relational retrieval.
4. Hybrid retrieval.

Outputs:

- retrieval log
- selected context files
- prompt files

Reporting requirements:

- query or seed concepts
- retrieved item IDs
- ranks and scores
- prompt inclusion decision
- context word/token counts

### Step 6: LLM Execution

Inputs:

- prompt files
- model configuration

Outputs:

- raw model outputs
- run summary

Reporting requirements:

- model name
- model version
- provider
- local or API execution
- temperature
- context window
- date of execution
- failed or retried prompts

### Step 7: Output Segmentation and Coding

Inputs:

- raw model outputs
- retrieval contexts
- source files

Outputs:

- claim-level coding table
- failure mode table
- inference shift table

Reporting requirements:

- claim segmentation rule
- text-supported coding rule
- graph-valid coding rule
- audit-valid coding rule
- integrated correctness rule
- coder qualifications
- inter-rater reliability plan

### Step 8: Source and Graph Spot-Checks

Inputs:

- selected claims
- cited chunks, facts, and relation paths

Outputs:

- source spot-check memo
- graph spot-check memo

Reporting requirements:

- sampled examples
- raw source locations
- whether source IDs resolved correctly
- whether relation paths were faithfully rendered
- unresolved source limitations

## Reproducibility Package Checklist

Minimum package:

- source filing manifest
- raw filing paths or SEC URLs
- download script
- extraction script
- text chunk table
- XBRL fact table
- XBRL relation edge/path table
- retrieval log
- context manifest
- rendered context files
- prompt files
- model run script
- raw LLM outputs
- claim-level coding table
- selected source spot-check file

Recommended package:

- source file hashes
- embedding metadata
- vector index metadata
- RDF/OWL mapping or export
- taxonomy/linkbase manifest
- reranking logs if applicable
- coder instructions
- inter-rater reliability file
- sensitivity check outputs

## Reviewer-Facing Demonstration Position

Suggested language:

> The demonstration is designed to show how retrieval design changes the information environment from which LLM audit outputs are generated. We therefore report the implementation pipeline from SEC filing download through retrieval logs, prompt rendering, model execution, claim coding, and source spot-checking. The objective is not to rank retrieval systems, but to make retrieval choices visible enough that readers can evaluate their implications for inference validity.

## Reviewer Risk and Response

Potential reviewer concern:

> Hybrid retrieval receives more information than text-only or XBRL-only retrieval, so output differences may reflect context volume.

Response:

> We disclose context lengths and treat this as a separability risk rather than a performance result. The correctness protocol evaluates whether hybrid claims actually integrate narrative and relational evidence. Future sensitivity checks should include token-budget equalization.

