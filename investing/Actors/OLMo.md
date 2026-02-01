---
aliases: [Open Language Model]
---

[[Allen Institute for AI]]'s fully open language model — releases data, code, and weights.

## Why it matters

Most "open" models only release weights. OLMo releases everything needed to reproduce training:
- Training data (Dolma dataset)
- Training code
- Intermediate checkpoints
- Ablation studies

This enables real research on what makes models work.

## Technical choices

- Dense models (not MoE) for simpler training
- Sliding window attention
- Strong ablation studies showing effect of each design choice
- ~$2M cluster rental for training (including engineering issues, multiple seeds)

## OLMo 3

Trained on less data than some competitors but achieved better performance through data quality. Focus on reasoning data for math/code capability.

## Research contributions

- Demonstrated data quality > data quantity
- Published [[RLVR]] methodology (Tulu 3)
- Coined "RLVR" term before DeepSeek popularized it
- Open process for reproducing ablations

## Funding

$100M NSF grant over 4 years — largest CS grant NSF ever awarded. Part of [[ATOM Project]] ecosystem for US open models.

## Related

- [[Allen Institute for AI]] — parent organization
- [[Nathan Lambert]] — post-training lead
- [[ATOM Project]] — strategic context
- [[RLVR]] — training technique they named
