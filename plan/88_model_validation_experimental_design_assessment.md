# Model Validation Experimental Design Assessment

## Purpose

This memo evaluates whether the current SEC/XBRL demonstration is sufficient for **model validation** and, if not, what additional experimental design would be needed. The assessment is grounded in AJPT methodological and empirical precedents rather than an unsupported judgment about sample size.

## Bottom-Line Judgment

The current evidence package is sufficient for a **Tier 1 methodological protocol validation** if the manuscript keeps its claims bounded. It is **not sufficient for model-performance validation** if the manuscript claims that XBRL-augmented retrieval improves LLM audit reasoning, audit judgment quality, or output correctness.

The manuscript should therefore separate two evidentiary standards:

1. **Protocol validation standard:** Can retrieval environments be specified, logged, reconstructed, traced to claims, and used to diagnose evidence-use differences?
2. **Model validation standard:** Does a retrieval design improve model output quality under controlled, generalizable, and independently coded conditions?

The current manuscript can satisfy the first standard. It does not yet satisfy the second.

## AJPT Precedents and Design Lessons

### 1. AJPT editorial policy

AJPT states that its central focus includes original research that improves auditing theory or auditing methodology, and it also publishes discussion and analysis of current issues relevant to auditing research and practice.

**Design lesson:** A methods paper can be accepted without a full model-performance experiment, but its empirical material must match the claim. If the paper claims methodology, the evidence can validate usability, transparency, and reviewer evaluability. If it claims performance, stronger empirical design is required.

Source: https://doi.org/10.2308/1558-7991-39.4.bmi

### 2. Malsch and Salterio (2016), AJPT

Malsch and Salterio provide reviewer-facing criteria for assessing audit field research quality. Their contribution is not a new hypothesis test; it is an evaluative framework for research quality.

**Design lesson:** Our manuscript can be framed similarly if retrieval-environment validity is presented as a reviewer-facing quality framework for LLM audit studies. The evidence should show that the framework can be applied to real artifacts, not that a model is better.

Source: https://doi.org/10.2308/ajpt-51170

### 3. Griffith, Kadous, and Young (2016), AJPT

This paper provides methodological advice for designing and evaluating audit JDM experiments using newer JDM frameworks.

**Design lesson:** If we move toward model validation, the design must specify the construct, independent variables, dependent variables, manipulation checks, and threats to internal validity. Retrieval condition should be treated as a manipulated research-design factor, not as an implementation label.

Source: https://doi.org/10.2308/ajpt-51347

### 4. Hatfield and Saiewitz (2022), AJPT

Hatfield and Saiewitz provide practical guidance for incorporating auditor-client communication in experimental audit research and compare design choices that vary in control and realism.

**Design lesson:** A strong LLM validation design should explicitly trade off control and ecological validity. A small controlled design can validate mechanisms; a broader filer sample can test whether the protocol travels across reporting environments.

Source: https://doi.org/10.2308/AJPT-2019-520

### 5. Leiby, Rennekamp, and Trotman (2021), AJPT

Leiby et al. survey challenges in audit JDM research, emphasizing access to experienced participants, data quality, and publication pressures for multiple experiments.

**Design lesson:** If we use audit-domain experts for validation, the manuscript must report expert qualifications, screening, coding instructions, data-quality checks, and reliability evidence. A vague "expert review" would likely create more reviewer concern than it resolves.

Source: https://doi.org/10.2308/AJPT-19-105

### 6. Aghazadeh and Peytcheva (2018), AJPT

This AS4 post-implementation study combines experiments, comment-letter analysis, and surveys to address a standard-setting question from multiple stakeholder perspectives.

**Design lesson:** AJPT values triangulation when a single method cannot fully support the inference. For our paper, triangulation can mean retrieval sensitivity checks, source-trace validation, and expert calibration rather than simply increasing the number of LLM outputs.

Source: https://doi.org/10.2308/ajpt-51742

### 7. Elder et al. (2013), AJPT audit sampling synthesis

The audit sampling synthesis emphasizes that sample size depends on the objective, the type of evidence, and the evaluation of errors.

**Design lesson:** There is no universal AJPT sample-size rule. The correct question is whether the sample supports the paper's stated inference. For model validation, the sample must support variation across filers, constructs, retrieval conditions, and repeated retrieval/model perturbations.

Source: https://doi.org/10.2308/ajpt-50394

### 8. Derks et al. (2025), AJPT Bayesian audit evidence paper

Derks et al. argue that statistical evidence should align with the hypothesis and evidentiary interpretation.

**Design lesson:** If we test model performance, the paper should define the hypothesis and evidence threshold ex ante. If the paper remains methodological, it should not imply inferential performance evidence from descriptive counts.

Source: https://doi.org/10.2308/AJPT-2021-086

### 9. Brivot, Roussy, and Mayer (2018), AJPT qualitative audit study

This study uses 34 interviews with audit partners to analyze conventions of audit quality.

**Design lesson:** Smaller samples can be acceptable when the design is qualitative and theory-building. However, once the paper reports comparative performance or prevalence, reviewers will expect a different evidentiary standard.

Source: https://doi.org/10.2308/ajpt-51772

## Current Package Against a Model-Validation Standard

| Item | Current package | Adequate for protocol validation? | Adequate for model validation? |
|---|---:|---|---|
| Filers | 9 total, 3 main and 6 extension | Yes, as maximum-variation demonstration | No, not representative and not powered |
| Retrieval-conditioned outputs | 42 | Yes, enough to show traceable workflow | Limited, too small for robust condition effects |
| Coded claims | 182 | Yes, enough to show claim-level variable construction | Limited, claim dependence must be modeled |
| Retrieval conditions | LLM-only, text, XBRL, hybrid in main; text/XBRL/hybrid in extension | Yes | Partially; extension lacks LLM-only baseline |
| Constructs | Revenue and inventory | Yes | Limited; two constructs are a narrow audit task universe |
| Model | Single local `gemma4:31b`, temperature 0 | Yes, controlled demonstration | No, cannot generalize across models |
| Expert coding | Not completed | Acceptable only with boundary language | No |
| Reliability evidence | Not completed | Acceptable only with boundary language | No |
| Sensitivity checks | Guidance, not executed | Acceptable if described as Tier 1 | No |
| Token-budget control | Reported conceptually | Useful | Needs stronger condition-level equalization |

## Reviewer-Facing Implication

If the manuscript continues to say "descriptive demonstration," reviewers may ask why the paper does not validate model performance. The better response is not to pretend that the current sample is enough. The better response is to state:

> The current paper validates a research-design protocol. It does not validate model performance. To support model-performance claims, the paper specifies a Tier 2 validation design and reports which additional controls, sample size, expert coding, and sensitivity checks would be required.

This framing is consistent with AJPT methods precedents: the paper contributes a method and gives researchers the validation standard needed for future empirical LLM audit studies.

## Recommended Tier 2 Model-Validation Design

### Research Question

Does retrieval design affect the quality, traceability, and audit-validity of LLM-generated audit-research claims under controlled retrieval environments?

### Unit of Analysis

Use two nested units:

1. **Task-output level:** filer x construct x retrieval condition x prompt/run variant.
2. **Claim level:** individual claims nested within task outputs.

Claims should not be treated as independent observations without clustering because multiple claims come from the same model response and retrieval environment.

### Minimum Factorial Structure

| Factor | Recommended levels | Reason |
|---|---:|---|
| Retrieval condition | 4: LLM-only, text, XBRL, hybrid | Separates model-only, narrative, relational, and combined evidence environments |
| Construct | 2: revenue recognition risk, inventory valuation assertion | Retains current construct focus |
| Filers | Minimum 12; stronger 20-24 | Creates cross-filer variation without claiming full SEC representativeness |
| Industry groups | Minimum 4 | Prevents consumer-retail overfitting |
| Size/reporting complexity strata | Minimum 2 x 2: large/smaller and simple/complex | Tests whether the protocol travels across reporting environments |
| Prompt variants | Minimum 2 | Tests prompt sensitivity without exploding cost |
| Retrieval variants | Minimum 2 targeted variants | Tests top-k/traversal-depth sensitivity |
| Models | Minimum 1 controlled model; stronger 2 models | One model is acceptable for retrieval-design inference; two models needed for cross-model robustness |

### Recommended Sample Size

For a **minimum publishable model-validation addendum**:

- 12 filers x 2 constructs x 4 retrieval conditions = 96 base outputs.
- Add one prompt variant for 50 percent of tasks or all main tasks = 48 to 96 sensitivity outputs.
- Expected claims: 4-6 per output, approximately 384-576 base claims before sensitivity outputs.
- Expert-code at least 120 stratified claims:
  - 15 claims per retrieval-condition x construct cell across 4 x 2 cells.
  - Oversample rare integrated and XBRL-only claims.
  - Include all manuscript table examples.

For a **stronger model-validation design**:

- 20-24 filers x 2 constructs x 4 retrieval conditions = 160-192 base outputs.
- Add retrieval sensitivity for top-k or traversal depth on 25-50 percent of tasks = 40-96 additional outputs.
- Add two-model replication on a focused subset = 48-64 additional outputs.
- Expected claims: approximately 700-1,200.
- Expert-code 200-300 stratified claims, or all risk/assertion-mapping claims if feasible.

These numbers are not arbitrary power claims. They are design thresholds derived from the need to observe variation across the major manipulated and blocking factors: retrieval condition, construct, filer, industry, reporting complexity, and sensitivity variant.

### Filer Sampling Design

Use purposive stratified sampling, not random SEC sampling, because the paper's method needs construct-relevant filings and inspectable XBRL relation structures.

Recommended strata:

| Stratum | Minimum representation | Examples of rationale |
|---|---:|---|
| Consumer retail / apparel | 3-4 filers | Familiar revenue and inventory settings |
| Technology / software / cloud | 3-4 filers | Multi-element revenue, contract liabilities, lower inventory |
| Manufacturing / industrial | 3-4 filers | Inventory costing, reserves, segment complexity |
| Pharma / life sciences / consumer products | 3-4 filers | Returns, allowances, reserves, product lifecycle risks |
| Large accelerated filers | At least 6 | Rich disclosure and XBRL coverage |
| Mid-size or reporting-complex filers | At least 6 | Tests extension concepts and sparse relation paths |

The sample should be described as maximum-variation validation, not population-representative inference.

### Retrieval Sensitivity Design

The minimum sensitivity layer should vary retrieval while holding model, prompt template, and task constant:

| Retrieval component | Base setting | Sensitivity setting | Validity dimension |
|---|---|---|---|
| Text top-k | Current top-k | top-k +/- one level | Selection validity |
| Text chunking | Current chunk rule | smaller/larger chunks or overlap | Representation and stability |
| XBRL traversal depth | Current relation path rule | depth +/- one level | Selection and representation |
| XBRL relation filters | Current relation types | calculation only / presentation plus calculation | Representation |
| Hybrid budget | Current assembly | equalized text/XBRL budget | Separability |
| Prompt order | Current context order | text-first vs XBRL-first | Separability and prompt-order sensitivity |

The manuscript does not need to show every sensitivity variant for every task. It should pre-specify a bounded sensitivity matrix and report whether the main qualitative inference changes.

### Expert Coding Design

A model-validation design needs independent audit-domain coding. Minimum acceptable design:

1. Two independent coders with audit-domain training or professional audit experience.
2. Blind coders to retrieval condition where feasible.
3. Provide each coder the claim, source excerpts/facts, and coding rubric.
4. Code four outcomes:
   - source-supported correctness;
   - graph-valid correctness;
   - audit-validity / overreach;
   - integrated evidence use.
5. Report percent agreement and Cohen's kappa or Krippendorff's alpha where the scale permits.
6. Resolve disagreements through adjudication and report common disagreement types.

Suggested expert-coded sample:

| Validation claim | Minimum coded claims |
|---|---:|
| Protocol usability only | 36-60 claims |
| Bounded model-validation addendum | 120 claims |
| Strong model-validation study | 200-300 claims or full risk/assertion claim population |

The current 15-20 claim calibration idea is useful for manuscript examples but too small for model validation.

### Statistical Analysis

For a Tier 2 validation study, use models that reflect nesting and small-cell structure:

1. Descriptive cell tables for retrieval condition x construct.
2. Mixed-effects logistic or multinomial models for claim-level outcomes, with claims nested within task outputs and filers.
3. Filer-level clustered standard errors or random filer effects.
4. Sensitivity reports showing whether conclusions change under retrieval/prompt variants.
5. Pre-specified primary outcomes to avoid overinterpreting many claim-level labels.

Recommended primary outcomes:

| Outcome | Level | Why it matters |
|---|---|---|
| Invalid source reference rate | Claim | Traceability and documentation |
| Unsupported or overreaching claim rate | Claim | Audit-validity risk |
| Evidence-use type | Claim | Whether hybrid labels imply integrated use |
| Construct-relevant retrieval coverage | Task-output | Selection validity |
| Claim-level inference shift | Task-output or claim | Whether retrieval changes research inference |

## How This Should Change the Current Manuscript

### Do not reposition the current paper as a model-validation study

That would create a large reviewer vulnerability. The current data are not designed for formal model validation.

### Add a "Model-Validation Extension Design" subsection

The manuscript should explicitly state what a stronger Tier 2 model-validation study would require. This converts a limitation into methodological guidance and aligns with the AJPT call topic on evaluating research design, modeling, variable selection, and best practices.

### Strengthen the current validation evidence

The current manuscript should revise Section VII and VIII to state:

- the demonstration validates the protocol, not model performance;
- the current sample is a maximum-variation methodological sample;
- stronger model-performance claims require the Tier 2 design above;
- current counts should be interpreted as evidence-use diagnostics, not prevalence estimates.

### Add one bounded validation layer if feasible before submission

The highest-value addition is not a full model benchmark. It is:

1. a bounded retrieval sensitivity audit on selected filer-construct tasks; and
2. limited expert calibration of at least 36-60 claims.

This would not make the paper a full model-validation study, but it would materially reduce the "good idea, insufficiently validated" concern.

## Recommended Manuscript Language

Add the following to Section VIII or the online supplement:

> Model-performance validation requires a different evidentiary design from the protocol validation reported in this paper. A performance study should define retrieval condition as an experimental factor, sample filers across industry and reporting-complexity strata, preserve task-output and claim-level nesting, conduct retrieval and prompt sensitivity checks, and obtain independent audit-domain coding with reliability evidence. The current demonstration provides the first layer of that design: it shows how retrieval environments, prompts, outputs, source references, and claim-level variables can be constructed and inspected. It does not estimate model-performance effects or failure-mode prevalence.

## Final Assessment

AJPT precedent supports the current paper as a methodology paper only if model-performance claims remain outside the contribution. If the authors want to claim that the model or XBRL-augmented retrieval is validated, the current design is insufficient.

The recommended strategy is therefore:

1. Preserve the current paper as a research-methodology paper.
2. Reframe the current demonstration as protocol validation.
3. Add a Tier 2 model-validation design as guidance.
4. If feasible, add bounded sensitivity and 36-60 claim expert calibration before submission.
5. Reserve full model-performance validation for a follow-on empirical paper or a major extension.

