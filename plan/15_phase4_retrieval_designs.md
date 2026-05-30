# Phase 4 Retrieval Design Operationalization

## Purpose

This file operationalizes retrieval-environment validity by defining retrieval designs in audit-research terms.

The purpose is not to prescribe a best retrieval architecture. The purpose is to help audit researchers match retrieval design to the intended audit construct and understand the inferential limits introduced by each design.

## Central Claim

Text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval support different audit constructs because they use different retrieval operators and create different information environments.

The key distinction is:

> Text-based and XBRL-based retrieval differ by retrieval operator, not by whether the final prompt is natural language.

## Reviewer-Level Concern

At an accept-level standard, reviewers will ask whether these retrieval designs are sufficiently operational to be used as research manipulations.

The paper should therefore specify:

- what changes across retrieval conditions
- what is held constant across retrieval conditions
- how token budget and information volume are handled
- how retrieval logs make the manipulation inspectable
- how the design avoids treating hybrid retrieval as a performance winner

## Accept-Level Contribution of Phase 4

At an accept-level standard, Phase 4 should convince reviewers that retrieval designs are not informal implementation choices. They are research design conditions that can be specified, compared, and evaluated.

The contribution of Phase 4 is:

> It converts retrieval-environment validity from an abstract framework into manipulable research design conditions by specifying retrieval operators, construct fit, validity risks, required controls, and minimum reporting expectations.

The section should help reviewers answer:

- What exactly changes across retrieval conditions?
- Why is that change theoretically tied to the audit construct?
- What must be held constant or reported?
- What validity risk does the retrieval condition introduce?
- What inference is and is not permitted under that condition?

## Retrieval Designs

The paper distinguishes four retrieval designs:

1. LLM-only
2. Text-based contextual retrieval
3. XBRL-based relational retrieval
4. Hybrid retrieval

## Operational Definition of a Retrieval Condition

A retrieval condition should be defined by five elements:

1. **Source**: where information is retrieved from.
2. **Unit**: what counts as a retrievable item.
3. **Operator**: how retrievable items are selected.
4. **Representation**: how retrieved items are rendered to the LLM.
5. **Controls**: what is held constant or reported across conditions.

| Element | Text-Based Contextual Retrieval | XBRL-Based Relational Retrieval | Hybrid Retrieval |
|---|---|---|---|
| Source | Narrative filing sections | XBRL instance, taxonomy, linkbases | Text sections + XBRL data |
| Unit | Chunk, paragraph, note, section | Concept, fact, relation path, context, dimension | Text chunk + relation path |
| Operator | Semantic similarity or keyword ranking | Typed accounting-relation traversal | Semantic retrieval + relation traversal |
| Representation | Natural language text chunks | Facts and labeled relation paths, possibly rendered in text | Integrated text and relation context |
| Controls | top-k, chunk size, token budget | seed concept, relation type, traversal depth, taxonomy version | allocation, ordering, token budget, component conditions |

Reviewer-safe sentence:

> A retrieval condition is not defined by the final prompt alone; it is defined by the source, unit, operator, representation, and controls that create the LLM's information environment.

## Design 1: LLM-Only Baseline

### Definition

LLM-only baseline refers to an LLM condition in which the model receives the task prompt but no external retrieved information.

### Retrieval Operator

None.

### Information Environment

The information environment consists of:

- task prompt
- model pretraining
- model-internal representations
- any information supplied directly in the prompt

### Best-Suited Construct

Baseline model reasoning.

### Appropriate Use

Use LLM-only conditions when the researcher wants a baseline for comparing how retrieved information changes output claims.

### Validity Risks

- pretraining contamination
- lack of traceability
- hallucinated accounting relationships
- inability to distinguish general model knowledge from task-specific evidence use

### Minimum Reporting

- model name and version
- prompt template
- task materials included in the prompt
- whether the filing or company was public before model training cutoff
- rationale for using LLM-only baseline

## Design 2: Text-Based Contextual Retrieval

### Definition

Text-based contextual retrieval selects narrative text chunks based on semantic similarity or keyword matching between the query and textual reporting materials.

### Retrieval Operator

Semantic similarity, keyword search, or text ranking.

### Information Environment

Examples of retrieved information include:

- MD&A paragraphs
- accounting policy notes
- footnote disclosures
- risk factor excerpts
- audit report language
- management explanations

### Best-Suited Constructs

- narrative disclosure comprehension
- accounting policy interpretation
- management explanation summarization
- qualitative risk cue identification
- disclosure tone or emphasis analysis

### Appropriate Use

Use text-based contextual retrieval when the intended construct depends on narrative meaning, policy language, or management explanations.

### Validity Risks

- relation hallucination
- omission of structured accounting relations
- weak numeric or dimensional grounding
- retrieval of semantically similar but construct-irrelevant text
- overinterpretation of narrative richness as audit reasoning quality

### Example

For a revenue recognition task, text retrieval may retrieve policy language about performance obligations and timing of revenue recognition. This may support narrative comprehension but may omit reported relations involving contract assets, contract liabilities, deferred revenue, and disaggregated revenue dimensions.

### Minimum Reporting

- text corpus used
- chunking rule
- embedding or search method
- top-k setting
- ranking rule
- retrieved text examples
- token budget
- rationale linking text retrieval to the intended construct

## Design 3: XBRL-Based Relational Retrieval

### Definition

XBRL-based relational retrieval selects information through typed accounting-relation traversal over XBRL facts, concepts, taxonomy elements, dimensions, periods, units, and linkbases.

### Retrieval Operator

Typed accounting-relation traversal.

Examples include:

- concept-to-fact lookup
- calculation link traversal
- presentation hierarchy traversal
- dimensional axis/member traversal
- period/context matching
- unit matching
- extension concept mapping
- related disclosure linkage, when available

### Operator Rule Template

Researchers should specify XBRL-based relational retrieval as a rule or query template rather than as a vague graph search.

Example template:

```text
Given seed concept C and filing F:
1. Retrieve facts for C in F for the target periods.
2. Retrieve standard taxonomy label and definition for C.
3. Retrieve calculation parents and children up to depth d.
4. Retrieve presentation parents and children up to depth d.
5. Retrieve dimensions, members, units, and contexts for retrieved facts.
6. Retrieve company extension concepts linked to or near C.
7. Preserve relation type labels in the representation shown to the LLM.
```

This template should be adapted to the intended construct. For example, calculation consistency tasks may emphasize calculation links, while extension interpretation tasks may emphasize presentation hierarchy, labels, and extension anchoring.

### Information Environment

Examples of retrieved information include:

- XBRL facts
- standard taxonomy concepts
- company extension concepts
- labels and definitions
- calculation paths
- presentation paths
- contexts and periods
- units
- dimensions and members
- reported line item relationships

### XBRL Framing

XBRL encodes management-coded reported accounting relationships that are relevant to, but not equivalent to, audit assertions.

XBRL is not independent audit evidence or ground truth.

### Best-Suited Constructs

- reported relation preservation
- calculation consistency reasoning
- taxonomy extension interpretation
- period/context comparison
- dimensional or segment disaggregation
- relation hallucination detection
- graph-valid correctness assessment

### Appropriate Use

Use XBRL-based relational retrieval when the intended construct depends on reported accounting relationships rather than narrative similarity alone.

### Validity Risks

- source overreach
- treating reported relationships as audit evidence
- treating calculation or presentation links as economic causality
- omitting narrative context
- overfitting to management-coded structures
- taxonomy version or tagging quality sensitivity

### Example

For inventory valuation, XBRL-based relational retrieval may retrieve inventory facts, inventory reserve concepts, cost of revenue relationships, periods, and dimensions. This may support graph-valid relation preservation but may not capture qualitative disclosures about obsolescence, management estimates, or internal control conditions.

### Minimum Reporting

- taxonomy version
- filing accession number
- XBRL parser or extraction method
- concept selection rule
- relation types traversed
- traversal depth
- handling of company extension concepts
- validation or spot-check procedures
- examples of relation paths
- representation format shown to the LLM
- seed concept selection rule
- whether labels, definitions, facts, and relation paths are all shown or selectively shown

## Design 4: Hybrid Retrieval

### Definition

Hybrid retrieval combines text-based contextual retrieval and XBRL-based relational retrieval in the same LLM condition.

### Retrieval Operator

Semantic retrieval plus typed accounting-relation traversal.

### Information Environment

Examples of retrieved information include:

- narrative disclosure text
- XBRL facts and concepts
- relation paths
- period changes
- dimensional information
- text-to-line-item links where available

### Best-Suited Constructs

- narrative-numeric integration
- narrative and reported relation consistency
- integrated correctness
- comparing management explanation to reported accounting relationships
- evaluating whether LLMs reconcile text and structured reporting information

### Appropriate Use

Use hybrid retrieval when the intended construct explicitly requires integration of narrative and structured reporting relationships.

### Validity Risks

- reduced separability
- construct contamination
- larger token budget or context volume
- unclear whether output changes arise from text, relations, or both
- information overload or conflicting evidence

### Example

For revenue recognition, hybrid retrieval may provide both performance obligation disclosures and XBRL relations involving revenue, contract liabilities, and deferred revenue. This may support narrative-numeric integration, but researchers must avoid concluding that hybrid retrieval is universally better because text and relation effects are jointly introduced.

### Minimum Reporting

- text retrieval procedure
- XBRL retrieval procedure
- integration rule
- ordering of retrieved materials
- token budget allocated to text vs relations
- whether token budgets are equalized across conditions
- rationale for studying an integrated construct
- sensitivity checks separating text-only and XBRL-only effects

### Required Controls

Hybrid retrieval should be interpreted cautiously unless the design includes:

- a text-only condition
- an XBRL-only condition
- a hybrid condition
- token budget reporting
- sensitivity analysis with equalized or disclosed context lengths
- explicit statement that hybrid retrieval tests narrative-numeric integration, not general superiority

## Retrieval Typology Table

| Retrieval Design | Retrieval Operator | Information Environment | Best-Suited Construct | Key Risk |
|---|---|---|---|---|
| LLM-only | None | Prompt and model-internal information | Baseline model reasoning | Pretraining contamination |
| Text-based contextual retrieval | Semantic similarity or keyword search | Narrative disclosures | Narrative comprehension | Relation hallucination |
| XBRL-based relational retrieval | Typed accounting-relation traversal | Reported accounting relationships | Reported relation preservation | Source overreach |
| Hybrid retrieval | Semantic retrieval + relation traversal | Narrative text + reported relationships | Narrative-numeric integration | Reduced separability |

## Retrieval Manipulation Table

This table clarifies what is manipulated and what should be held constant.

| Design | Manipulated Retrieval Component | Should Be Held Constant or Reported |
|---|---|---|
| LLM-only | External retrieval absent | Model, prompt, task, temperature, task materials |
| Text-based contextual retrieval | Text retrieval source/operator/results | Model, prompt shell, task, token budget, top-k or context length |
| XBRL-based relational retrieval | Typed relation traversal and relation paths | Model, prompt shell, task, token budget or disclosed context length |
| Hybrid retrieval | Joint provision of text and relation outputs | Model, prompt shell, task, ordering rule, token budget, text/XBRL allocation |

Reviewer-safe sentence:

> Retrieval conditions should be treated as research manipulations only when the researcher specifies both the retrieval component that changes and the design features held constant or disclosed across conditions.

## Inferential Permissions and Limits

This table clarifies what each design allows the researcher to infer.

| Design | Permitted Inference | Inference Not Permitted Without Additional Evidence |
|---|---|---|
| LLM-only | How the model responds without external retrieval under the specified prompt | That the model used reliable audit-relevant information |
| Text-based contextual retrieval | How narrative context supports LLM output claims | That the model preserved structured accounting relations |
| XBRL-based relational retrieval | How reported accounting relationships support or constrain LLM claims | That the model made audit-valid judgments or obtained independent audit evidence |
| Hybrid retrieval | How the model integrates narrative and reported relational information | That hybrid retrieval is generally superior or that text and relation effects are separable |

Reviewer-safe sentence:

> Retrieval designs do not simply change performance; they change what kind of inference the researcher can make.

## Construct-to-Retrieval Mapping

| Intended Audit Construct | Primary Retrieval Design | Useful Diagnostic Comparison | Rationale | Main Validity Risk |
|---|---|---|---|---|
| Baseline model reasoning | LLM-only | Text and XBRL conditions | Provides comparison condition without external retrieval | Pretraining contamination |
| Narrative disclosure comprehension | Text-based contextual retrieval | XBRL condition to test relation omission | Construct depends on management explanations and policy language | Omission of structured relations |
| Reported accounting relation preservation | XBRL-based relational retrieval | Text condition to test relation hallucination | Construct depends on typed reported relationships | Source overreach |
| Calculation consistency reasoning | XBRL-based relational retrieval | Text condition to test unsupported calculation claims | Construct depends on calculation paths and reported facts | Rendering calculation as causality |
| Taxonomy extension interpretation | XBRL-based relational retrieval plus targeted text | Text-only and XBRL-only conditions | Construct depends on extension concept placement and related disclosures | Misinterpreting custom tags |
| Narrative-numeric integration | Hybrid retrieval | Text-only and XBRL-only conditions | Construct requires reconciliation of text and reported relationships | Reduced separability |
| Assertion mapping | Hybrid retrieval plus expert-coded assertion layer | XBRL-only condition to identify source overreach | Construct requires reported relationships and professional judgment | Treating reported relationships as audit assertions |
| Fraud intent or management integrity | XBRL retrieval alone inappropriate | Non-XBRL data sources required | Construct depends on evidence outside reported relationships | Construct underrepresentation |
| Internal control operating effectiveness | XBRL retrieval alone inappropriate | Process/control evidence required | Construct requires process/control evidence | Construct underrepresentation |

Reviewer-safe sentence:

> "Primary retrieval design" identifies the design most aligned with the construct; it does not imply that other designs are irrelevant. Comparison conditions are often necessary for diagnostic interpretation and separability.

## Construct-to-Retrieval Decision Tree

Use this decision tree to choose retrieval design:

1. Is the intended construct baseline model reasoning without external information?
   - Yes: use LLM-only.
   - No: continue.

2. Does the construct depend primarily on narrative disclosure, accounting policy language, or management explanation?
   - Yes: use text-based contextual retrieval.
   - No: continue.

3. Does the construct depend primarily on reported accounting relationships, calculation paths, taxonomy placement, dimensions, periods, or extension concepts?
   - Yes: use XBRL-based relational retrieval.
   - No: continue.

4. Does the construct require integration of narrative explanations with reported accounting relationships?
   - Yes: use hybrid retrieval.
   - No: continue.

5. Does the construct require audit assertions, risks, or procedures?
   - Use hybrid retrieval only with expert-coded assertion or risk logic.
   - Do not treat XBRL relations as audit assertions.

6. Does the construct require fraud intent, management integrity, social pressure, internal control operation, or third-party evidence reliability?
   - XBRL-based relational retrieval alone is inappropriate.
   - The study needs additional data sources or a different design.

## Decision Tree Limitations

The decision tree is a design aid, not a rule for selecting the best retrieval method. It should be used to justify construct-retrieval alignment and to identify when a retrieval design underrepresents the intended construct.

Limitations:

- Some constructs require multiple information types.
- Some tasks require expert-coded assertion or risk logic.
- Some retrieval designs may be useful for diagnostic comparisons even if they are not theoretically ideal.
- Hybrid retrieval may support integration but weaken mechanism isolation.

## Token and Context Budget Strategies

Token budget is a major confound in retrieval comparisons. The manuscript should not require one universal solution, but it should require researchers to disclose and justify their strategy.

| Strategy | Description | Strength | Weakness |
|---|---|---|---|
| Equalized token budget | Each retrieval condition receives approximately the same context length | Supports comparability | May truncate naturally richer conditions |
| Disclosed unequal budget | Conditions receive different context lengths, but length and rationale are reported | Preserves natural retrieval output | Weakens performance comparisons |
| Component-balanced hybrid | Hybrid condition reserves explicit portions for text and XBRL outputs | Improves transparency | Requires arbitrary allocation choices |
| Sensitivity analysis | Results are checked under alternative top-k, traversal depth, or token limits | Shows robustness | Adds complexity |

Recommended stance:

> For methodological demonstrations, disclosed context length plus sensitivity analysis may be sufficient. For hypothesis-testing studies comparing retrieval conditions, token budget should be equalized or explicitly modeled.

## Boundary Conditions for XBRL-Based Relational Retrieval

### Appropriate Uses

XBRL-based relational retrieval is appropriate for studying:

- reported relation preservation
- calculation consistency
- taxonomy extension interpretation
- period/context comparison
- dimensional disaggregation
- graph-valid correctness
- relation hallucination

### Inappropriate Standalone Uses

XBRL-based relational retrieval alone is not appropriate for studying:

- fraud intent
- management integrity
- auditor-client negotiation
- professional skepticism under social pressure
- internal control operating effectiveness
- private audit evidence evaluation
- third-party evidence reliability
- sufficiency of audit evidence

### Reviewer-Safe Statement

> XBRL-based relational retrieval helps researchers evaluate how LLMs use reported accounting relationships. It does not provide the full evidential basis required for audit judgments.

## How Retrieval Designs Link to Retrieval-Environment Validity

| Retrieval Design | Selection Validity Issue | Representation Validity Issue | Stability Issue | Traceability Issue | Separability Issue |
|---|---|---|---|---|---|
| LLM-only | No external construct-specific selection | N/A unless prompt includes materials | Model output may vary | Claims often lack source trace | Cannot separate pretraining from reasoning |
| Text-based contextual retrieval | May omit structured relations | Text chunks may lose section context | Depends on embedding/index/query stability | Claims can be traced to chunks if logged | Text effect can be separated if comparison exists |
| XBRL-based relational retrieval | May omit narrative context | Relation paths may be misrendered | Depends on taxonomy/parser/traversal settings | Strong if concept/path IDs retained | Relational effect separable if text condition exists |
| Hybrid retrieval | May retrieve both relevant and excess context | Integration format may privilege one source | Depends on both retrieval systems | Traceability requires text and relation mapping | Weakest unless text-only and XBRL-only conditions included |

## Minimal Design Validity Checks

Before interpreting LLM outputs, researchers should perform minimal checks for each retrieval condition:

| Check | Purpose |
|---|---|
| Retrieval log inspection | Confirms what information was provided |
| Construct-retrieval rationale | Explains why the information environment matches the construct |
| Token/context reporting | Helps evaluate context-volume confounds |
| Source type labeling | Distinguishes management-coded, third-party, and researcher-supplied information |
| Relation label preservation | Prevents typed XBRL relations from being collapsed into vague prose |
| Comparison condition design | Supports separability of text, relation, and model effects |
| Sensitivity to top-k/traversal depth | Evaluates robustness of retrieval-created environment |
| Token budget strategy | Clarifies whether observed differences may reflect information volume |

## Accept-Level Design Criteria

For Phase 4 to support an accept-level review, the manuscript should satisfy the following:

1. Each retrieval design is defined by source, unit, operator, representation, and controls.
2. Text-based and XBRL-based retrieval are distinguished by operator, not final prompt format.
3. XBRL-based relational retrieval is specified through a reproducible rule template.
4. Hybrid retrieval is framed as appropriate for integration constructs, not as a superior method.
5. Token/context budget and information volume are reported or controlled.
6. The decision tree is framed as a construct-alignment aid, not a universal rule.
7. The section states what each retrieval design permits and does not permit researchers to infer.
8. The design section prepares the reader for Phase 5 correctness coding and Phase 6 demonstration.

## Draft Manuscript Section

Retrieval-environment validity requires researchers to specify how retrieval design creates the information environment observed by the LLM. We distinguish four retrieval designs: LLM-only, text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval. These designs are not ordered from weak to strong. Rather, they support different audit constructs and introduce different validity risks.

LLM-only conditions provide a baseline in which the model receives no external retrieved information. Such conditions help researchers examine baseline model behavior, but they also create risks of pretraining contamination and weak traceability. Text-based contextual retrieval selects narrative materials using semantic similarity or keyword search. It is well suited for constructs such as narrative disclosure comprehension and accounting policy interpretation, but it may omit structured accounting relationships. XBRL-based relational retrieval selects information through typed accounting-relation traversal over XBRL facts, concepts, taxonomy elements, periods, units, dimensions, and linkbases. It is well suited for constructs such as reported relation preservation and calculation consistency, but it risks source overreach if researchers treat management-coded reported relationships as audit evidence. Hybrid retrieval combines text-based and XBRL-based retrieval. It may support narrative-numeric integration, but it reduces separability because narrative and relational inputs are jointly introduced.

The distinction between text-based and XBRL-based retrieval lies in the retrieval operator, not in whether the final prompt is natural language. Text-based retrieval selects information by semantic similarity, while XBRL-based relational retrieval selects information by typed accounting-relation traversal. This distinction matters because retrieval operators shape the information environment and therefore the inferences researchers can validly draw from LLM outputs.

## Reviewer Stress Test

### Concern 1: This reads like a technical retrieval architecture.

Response:

The section should remain focused on audit constructs, retrieval operators, and validity risks. Technical implementation details should be minimized or moved to the methodological demonstration or appendix.

### Concern 2: XBRL retrieval is treated as better than text retrieval.

Response:

The manuscript should state that text-based and XBRL-based retrieval support different constructs. XBRL-based retrieval is not superior; it is more appropriate when the construct depends on reported accounting relationships.

### Concern 3: Hybrid retrieval is presented as the best design.

Response:

Hybrid retrieval supports narrative-numeric integration but reduces separability. It should be framed as construct-specific and methodologically risky if used without text-only and XBRL-only comparisons.

### Concern 4: XBRL is being treated as audit evidence.

Response:

The manuscript should repeatedly state that XBRL encodes management-coded reported accounting relationships relevant to, but not equivalent to, audit assertions.

### Concern 5: The decision tree is too simplistic.

Response:

The decision tree is not a universal rule. It is a design aid for aligning retrieval design with intended audit constructs and identifying when additional data or expert coding is needed.

### Concern 6: The retrieval designs are not sufficiently controlled as manipulations.

Response:

The manuscript should include a retrieval manipulation table that specifies what changes across conditions and what is held constant or reported. This is especially important for hybrid retrieval, where token budget and information volume may confound interpretation.

### Concern 7: XBRL-based relational retrieval is underspecified.

Response:

The manuscript should provide an operator rule template for XBRL-based relational retrieval, including seed concept selection, relation types traversed, traversal depth, context/unit/dimension handling, extension handling, and relation label preservation.

### Concern 8: Hybrid retrieval creates unavoidable confounds.

Response:

Hybrid retrieval does create separability concerns. That is why the paper frames hybrid retrieval as appropriate for narrative-numeric integration, not as a superior design. Studies using hybrid retrieval should include text-only and XBRL-only comparisons where possible.

### Concern 9: The paper does not say what can be inferred from each retrieval condition.

Response:

The manuscript should include an inferential permissions table. This table clarifies that text retrieval permits claims about narrative support, XBRL retrieval permits claims about reported relation preservation, and hybrid retrieval permits claims about integration only when separability limitations are acknowledged.

### Concern 10: The construct-to-retrieval mapping is too prescriptive.

Response:

The manuscript should use "primary retrieval design" rather than "preferred retrieval design" and separately identify diagnostic comparison conditions. This preserves construct alignment without implying that a single retrieval method is always correct.

### Concern 11: Token budget confounds may invalidate retrieval comparisons.

Response:

The manuscript should require token/context budget reporting and should describe acceptable strategies: equalized token budget, disclosed unequal budget, component-balanced hybrid context, and sensitivity analysis.

## Reviewer-Level Accept Statement

If written into the manuscript clearly, Phase 4 could support the following reviewer assessment:

> The retrieval typology is useful because it converts an otherwise technical design choice into explicit research conditions. The authors appropriately distinguish retrieval operators, identify construct fit, state inferential limits, and avoid claiming that XBRL-based or hybrid retrieval is generally superior. This makes the framework actionable for researchers designing LLM-based audit studies.

## Phase 4 Reviewer-Level Assessment

### Strengths

- Retrieval designs are distinguished by operator rather than final prompt format.
- XBRL is framed as reported accounting relationships, not audit evidence.
- Hybrid retrieval is treated as construct-specific rather than superior.
- The decision tree makes the framework actionable.
- Boundary conditions help prevent overclaiming.
- Retrieval conditions are now framed as research manipulations that require controls and reporting.
- XBRL-based relational retrieval now includes a rule template that makes the design more operational.
- Retrieval conditions are now defined by source, unit, operator, representation, and controls.
- The section now clarifies what each retrieval design permits and does not permit researchers to infer.

### Remaining Weaknesses

- The final manuscript must avoid excessive technical detail.
- XBRL examples must be concrete enough to show why typed relation traversal matters.
- The methodological demonstration must show text-only, XBRL-only, and hybrid conditions to support separability.
- Phase 5 must provide a strong correctness protocol so the retrieval designs can be evaluated meaningfully.
- The final manuscript must decide how much of the operator rule template belongs in the main text versus appendix.
- Demonstration design must handle token/context budget transparently.
- The construct-to-retrieval mapping should be written as alignment guidance, not a deterministic method-selection rule.

## Phase 4 Deliverables

- Retrieval design definitions: complete.
- Retrieval operator specifications: complete.
- Retrieval typology table: complete.
- Construct-to-retrieval mapping: complete.
- Construct-to-retrieval decision tree: complete.
- Boundary conditions for XBRL-based relational retrieval: complete.
- Draft XBRL-augmented retrieval section: complete.
