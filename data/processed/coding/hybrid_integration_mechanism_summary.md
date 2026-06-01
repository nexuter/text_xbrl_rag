# Hybrid Integration Mechanism Summary

This diagnostic decomposes hybrid-condition claims by the evidence type actually used in each claim.
It is a mechanism diagnostic for the paper's integration-failure argument, not a model-performance result.

Hybrid claims analyzed: 89

| Mechanism | Claims | Share | Interpretation |
|---|---:|---:|---|
| integrated_text_xbrl_bridge | 8 | 9.0% | Claim uses both text and XBRL evidence with an inferential bridge. |
| text_only_within_hybrid | 61 | 68.5% | Hybrid prompt was available, but the claim used narrative text only. |
| xbrl_only_within_hybrid | 20 | 22.5% | Hybrid prompt was available, but the claim used XBRL facts or paths only. |

The mechanism table shows that hybrid non-integration is not a single phenomenon.
In this sample, non-integrated hybrid claims primarily arise because the model uses either the narrative layer or the XBRL layer, rather than because it cites both layers but fails to connect them.