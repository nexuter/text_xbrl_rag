# Abstract and Paper Structure

## Refined Abstract

Retrieval-augmented large language models (LLMs) are increasingly relevant to audit research, yet retrieval is often treated as a background implementation choice. We argue that, in retrieval-augmented LLM audit studies, retrieval design is part of the research design because retrieval systems dynamically select, rank, transform, and present the information environment observed by the model. This dynamic retrieval layer creates retrieval-specific threats to construct validity. We introduce retrieval-environment validity as a diagnostic lens for evaluating whether the dynamically retrieved information environment aligns with the audit construct the researcher intends to study. We ground its five dimensions--selection validity, representation validity, stability, traceability, and separability--in audit and research design concerns of relevance, reliability, documentation, reproducibility, and internal validity. Using XBRL as a management-coded representation of reported accounting relationships relevant to, but not equivalent to, audit assertions, we operationalize the framework through a retrieval typology, claim-level correctness protocol, failure taxonomy, reporting checklist, sensitivity check guidance, and a descriptive methodological demonstration using SEC filing and Inline XBRL data. The framework helps audit researchers bound what can validly be inferred from LLM outputs about narrative comprehension, reported relation preservation, and narrative-numeric integration.

## Final Contribution Paragraph

This paper contributes to auditing methodology in three ways. First, it introduces retrieval-environment validity as a retrieval-specific diagnostic lens for construct validity in LLM-based audit research. Second, it operationalizes this concept through tools for mapping retrieval designs to audit constructs, coding LLM outputs at the claim level, diagnosing retrieval-related failure modes, reporting retrieval conditions, and conducting sensitivity checks. Third, it provides a descriptive methodological demonstration using actual SEC filing and Inline XBRL data to show how retrieval design changes the inferences researchers can draw from LLM audit outputs.

## Recommended Paper Structure

1. Introduction
   - Motivate LLM-RAG audit research.
   - Argue that retrieval is part of research design.
   - State central research question.

2. Related Literature
   - AJPT methodology guidance papers.
   - XBRL as structured reporting data.
   - Textual analysis and LLM accounting research.
   - Audit analytics, Big Data, and AI in auditing.

3. Retrieval-Environment Validity
   - Define the concept.
   - Explain why dynamic retrieval differs from fixed information sets.
   - Present five dimensions.

4. XBRL-Augmented Retrieval
   - Frame XBRL as management-coded reported accounting relationships.
   - Distinguish text-based contextual retrieval, XBRL-based relational retrieval, and hybrid retrieval.
   - Discuss boundary conditions.

5. Correctness Protocol and Failure Modes
   - Present claim-level correctness layers.
   - Present audit-valid coding guidance.
   - Present failure mode taxonomy.

6. Methodological Guidance
   - Construct-to-retrieval decision tree.
   - Reporting checklist.
   - Sensitivity checks.

7. Methodological Demonstration
   - Use actual SEC filing and Inline XBRL data.
   - Compare retrieval designs descriptively.
   - Present inference shift table.

8. Discussion
   - Explain implications for LLM-based audit research.
   - Reiterate limits: XBRL is not audit evidence, hybrid is not universally superior.

9. Conclusion
   - Emphasize retrieval as research design.
   - Encourage bounded inference from LLM outputs.

## Conclusion Sentence

Our objective is not to prescribe a universally preferred retrieval architecture, but to help audit researchers align retrieval design with research constructs and limit inferential overreach when interpreting LLM outputs.
