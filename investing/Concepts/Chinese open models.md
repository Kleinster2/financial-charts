---
aliases: [China open source AI, Chinese open-weight models]
---

China's open-weight AI models now dominate the open ecosystem — 5 of top 15 open models are Chinese.

## Key players

| Company | Model | Notes |
|---------|-------|-------|
| [[DeepSeek]] | R1, V3 | Kicked off movement, hedge fund backed |
| [[Qwen]] | 2.5 | [[Alibaba]], largest training data (50T tokens) |
| [[Kimi]] | k2 | [[Moonshot AI]], strong creative writing |
| [[MiniMax]] | Various | Filed IPO |
| [[Zhipu]] | GLM-4 | Filed IPO, strong reasoning |

## Why they release open weights

US enterprises won't pay for API subscriptions to Chinese companies (security concerns). Open weights let them influence the growing AI market indirectly — developers use models without sending data to China.

Government sees open models building international influence. Incentives to keep it going.

## License advantage

Chinese open models use unrestricted licenses — no strings attached. [[Llama]] and [[Gemma]] have user limits and reporting requirements. This matters for production use.

## DeepSeek losing its crown

DeepSeek kicked off the movement but others catching up:
- Using DeepSeek's published architectures (same MoE design)
- More recent models often slightly better (leapfrogging)
- Kimi, Zhipu, MiniMax all showing strong results

DeepSeek secretive in communication but open in technical reports. Others like MiniMax and Moonshot actively seeking Western mindshare (IPO paperwork).

## US response

Gap motivated [[ATOM Project]] and renewed US focus on open models. July 2025: China released 4-5 DeepSeek-caliber models, US released zero.

## Business model uncertainty — and the proprietary pivot

Through 2025, no Chinese open model had a clear path to revenue — same as US open models. That changed in early 2026:

[[Alibaba]] began shifting its leading [[Qwen]] models to proprietary (closed-source) in April 2026, keeping them exclusive for cloud customers. Zhou Jingren (former [[Alibaba Cloud]] CTO) replaced Lin Junyang as AI division head after internal disagreements over commercialization. The trigger: Alibaba was spending heavily on open-source training while rivals ([[MiniMax]], [[Zhipu]], [[Moonshot AI]]) outperformed Qwen in coding — a fast-growing revenue area. MaaS (model-as-a-service) is now positioned as a key cloud revenue driver. Open-source continues for select models and areas (e.g. [[Happy Horse]] video generation).

[[Meta]] made a parallel shift in the US, with [[Muse Spark]] (proprietary, from [[Meta Superintelligence Labs]]) replacing [[Llama]] as the flagship line.

The broader industry consensus: with value shifting to AI applications (coding, agents), building powerful open models alone is not enough. The question is whether the developer ecosystem built on open weights will tolerate the bait-and-switch — or migrate to alternatives that remain open.

*Source: FT (Apr 10, 2026)*

## Related

- [[ATOM Project]] — US response
- [[DeepSeek]] — started the movement
- [[Export controls]] — constraints on Chinese compute
- [[Llama]] — US open model, Meta now pivoting to proprietary [[Muse Spark]]
- [[Alibaba]] — Qwen pivot to proprietary (Apr 2026)
- [[Open source commoditization]] — broader commoditization dynamics
