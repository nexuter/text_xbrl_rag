# Minor Comments Coverage Audit

Date: 2026-06-01

## Bottom-Line Assessment

The seven minor comments are mostly addressed. The strongest remaining gap was Minor Comment 4: the paper had correctness-layer tables, but no compact visual example early in the manuscript. I added Figure 1A and an early manuscript placeholder to help readers understand text-supported, graph-valid, audit-boundary, integrated, and audit-evidence-sufficiency distinctions before reaching the detailed coding section.

## Coverage By Comment

| Minor Comment | Current Status | Evidence / Action |
|---|---|---|
| 1. Boundary statements are repetitive | Partially addressed | The manuscript is now disciplined about boundaries, but repetition remains intentional in abstract, demonstration, discussion, and supplement to prevent overclaiming. Further tightening can occur during final style editing. |
| 2. Engage non-accounting retrieval evaluation and evidence traceability | Addressed | Section II includes a RAG Evaluation and Evidence Traceability subsection covering RAG architecture, context relevance, answer faithfulness, answer relevance, attribution, and citation grounding. |
| 3. Acknowledge retrieval-environment validity as subtype/lens of construct validity | Addressed | Introduction and Section III state that the concept does not replace construct validity and is best understood as a retrieval-specific diagnostic lens for construct drift. |
| 4. Add compact visual example of correctness layers early | Addressed now | Added Figure 1A and an early placeholder after the introductory correctness-layer paragraph. |
| 5. Cleaner statement of what nine-filer extension teaches beyond applicability | Addressed | Section VII states the extension supports protocol maintenance across varied reporting environments, claim-level source-use concern, and boundary-condition visibility such as large XBRL environments and relation-path scarcity. |
| 6. Avoid model-performance benchmarking language | Addressed | The manuscript repeatedly states that the demonstration is protocol validation, not model-performance, retrieval-superiority, or benchmark evidence. |
| 7. Add retrieval mechanics example for AJPT readers | Addressed | Section IV Mechanics Example explains top-k, chunking, relation-path omission, traversal/filtering, source order, token budget, and relation to validity dimensions. |

## Remaining Reviewer Risk

The only meaningful residual risk is Minor Comment 1. Boundary statements are still frequent. This is partly necessary because prior major comments focused on overclaiming, audit-validity, model-performance inference, and design-specific counts. The response should frame remaining repetition as deliberate boundary discipline while noting that the revision consolidated some boundary logic into tables and supplement sections.

## Response-Letter Position

> We revised the manuscript to address the minor comments by strengthening the non-accounting RAG/evidence-traceability discussion, clarifying that retrieval-environment validity is a retrieval-specific diagnostic lens grounded in construct validity, adding an early compact correctness-layer example, sharpening the nine-filer extension's methodological lessons, and tightening model-performance boundary language. We retained some boundary repetition intentionally because several major comments concerned overclaiming from public filing/XBRL data and design-specific counts.

## Implementation Log

- Added Figure 1A to the tables and figures packet.
- Added an early `[Insert Figure 1A about here]` placeholder in the Introduction.
- Documented comment-by-comment coverage for revision tracking.
