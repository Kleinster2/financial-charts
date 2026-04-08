---
aliases:
  - Nous
  - NousResearch
tags:
  - actor
  - company
  - ai
  - open-source
  - crypto
type: company
status: private
founded: 2023
hq: unclear (sources conflict — NY or distributed)
---

# Nous Research

Open-source AI lab building foundation models and [[Agent harnesses|agent infrastructure]], with a crypto-native capitalization strategy anchored on [[Solana]]-based distributed training. The closest analogue is a hybrid of [[Hugging Face]] (open models, community) and [[Together AI]] (compute marketplace) — but with a token-incentive layer instead of a SaaS revenue model.

---

Three dynamics define the Nous Research story right now:

1. Model traction without revenue clarity. The Hermes model family has 55M+ downloads across [[Hugging Face]], powering 120+ mobile apps and products. Hermes 4 (8B/70B/405B on [[Meta|Llama 3.1]]) and DeepHermes 3 ([[Mistral]] 24B) are competitive open-source alternatives. But the business model remains pre-revenue — no evidence of meaningful API income from Nous Portal, and the planned Psyche compute marketplace token hasn't launched. [[Paradigm]] bet $50M at a $1B token valuation (Apr 2025) on network effects that don't exist yet.

2. The [[Hermes Agent]] harness. Launched Mar 2026, already at 36K GitHub stars. A persistent, self-improving autonomous agent — not a framework like [[LangChain]] or [[CrewAI]] but a deployable agent that learns from its own task history. Runs on a $5/month VPS, connects to 14+ messaging platforms, supports 200+ models via [[OpenRouter]]. The learning loop (auto-generated skills from completed tasks, persistent memory) is the differentiator. Competes in a different category from [[Anthropic|Claude Code]] or [[Anysphere|Cursor]] (which are harnesses for developers), closer to [[OpenClaw]] (general-purpose persistent agents).

3. Psyche — decentralized training on [[Solana]]. The crypto angle isn't grafted on; it's foundational. Psyche coordinates distributed GPU contributors to train models, using token incentives instead of centralized compute contracts. Testing partners include [[Oracle]], Northern Data Group, [[Crusoe Energy|Crusoe Cloud]], [[Lambda Labs]], and Andromeda Cluster. If it works, it's a structural cost advantage for training. If it doesn't, the $1B valuation is a crypto premium on an open-source lab with no revenue.

Open questions: Does the token launch create real utility or just speculative trading? Can Psyche's distributed training match centralized cluster quality? Will Hermes Agent's learning loop prove durable as [[OpenClaw]] (349K stars, 247K devs) dominates the open-source agent category? And can a ~20-person team sustain model + agent + compute network development simultaneously?

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2022 (informal collective); 2023 (incorporated) |
| HQ | Unclear — The AI Insider says New York; other sources suggest distributed |
| Team | ~20 people |
| Total raised | $65M |
| Last round | $50M Series A (Apr 2025), led by [[Paradigm]], $1B token valuation |
| Key models | Hermes 4, DeepHermes 3, OpenHermes 2.5 |
| Model downloads | 55M+ (Hugging Face) |
| Key products | [[Hermes Agent]], Psyche network, Nous Portal |
| GitHub (Hermes Agent) | 36.4K stars, 4.6K forks |

---

## Founders

| Name | Role | Background |
|------|------|------------|
| Jeffrey Quesnelle | Co-Founder, CEO & CTO | M.S. Computer Science, U of Michigan; ex-MEV engineer at Eden Network |
| Karan Malhotra | Co-Founder, Head of Behavior | B.A. Philosophy & Religion, Emory |
| Teknium | Co-Founder, Head of Post Training | Pseudonymous; extensive open-source LLM contributions |
| Shivani Mitra | Co-Founder | Role not publicly disclosed |

Notable collaborator: Diederik P. Kingma (co-inventor of Adam optimizer, ex-[[OpenAI]] founding team).

---

## Funding

| Date | Round | Amount | Lead | Notable investors |
|------|-------|--------|------|-------------------|
| Jan 2024 | Seed 1 | $5.2M | Distributed Global, OSS Capital | Balaji Srinivasan, Alex Atallah ([[OpenRouter]]/[[OpenSea]] founder), Vipul Reddy ([[Together AI]] CEO), Gavin Uberti ([[Etched]] CEO) |
| Jun 2024 | Seed 2 | ~$15M | — | Delphi Digital, North Island Ventures, Raj Gokal ([[Solana]] co-founder), Robot Ventures |
| Apr 2025 | Series A | $50M | [[Paradigm]] | $1B token valuation; essentially entire round from Paradigm |

---

## Evolution

The story of Nous Research is the story of whether open-source AI can sustain itself without a SaaS business model — by using crypto incentive mechanisms instead.

- 2022: Started as an internet-native collective of AI researchers who found each other on Discord, GitHub, and Twitter. No incorporation, no office, no funding — just shared interest in fine-tuning open-weight models. The founding team included Jeffrey Quesnelle (a Michigan CS grad turned MEV engineer), Karan Malhotra (philosophy background, not CS), and Teknium (pseudonymous, prolific open-source contributor). This origin story matters: Nous never had a traditional startup formation. It grew out of the decentralized AI community, which explains the later crypto pivot.

- 2023: Formalized as a company. Released OpenHermes 2.5 on [[Mistral]] 7B — a fine-tune that punched well above its weight class. Downloads accumulated fast. The Hermes brand became synonymous with high-quality open-source fine-tunes. But the question was already visible: downloads don't pay salaries. [[Hugging Face]] solved this with a hosted platform business; Nous had no equivalent.

- Jan 2024: Raised $5.2M seed from Distributed Global and OSS Capital. Angel list was crypto-native ([[Solana]] co-founder Raj Gokal, Balaji Srinivasan) and AI-native ([[Together AI]] CEO, [[Etched]] CEO, [[OpenSea]]/[[OpenRouter]] founder Alex Atallah). This investor mix foreshadowed the strategy: crypto infrastructure for AI training.

- Jun 2024: Quiet ~$15M second seed from Delphi Digital, North Island Ventures, and others. Total seed: ~$20M. Started building Psyche — the decentralized training network on [[Solana]] that would become the core business thesis.

- Apr 2025: $50M Series A from [[Paradigm]] at a $1B token valuation. Paradigm — the crypto VC that backed [[Uniswap]], [[Optimism]], and other DeFi infrastructure — essentially wrote the entire round. The valuation was token-based (SAFT/warrant structure), not equity-based. This was the bet: Nous's open-source models + Psyche compute network could create a token-incentivized flywheel where contributors train models, earn tokens, and the network grows. No official token launched yet.

- Mar 2026: [[Hermes Agent]] released — a persistent, self-improving autonomous agent framework. First tagged release v0.2.0 on Mar 12; rapid iteration to v0.8.0 by Apr 8. Hit 36K GitHub stars in under a month. The agent space was already crowded ([[OpenClaw]] at 349K stars), but Hermes Agent's self-learning loop and cost structure ($5/month VPS) carved a niche.

---

## Products

- [[Hermes Agent]] — persistent autonomous agent framework (see product note)
- Hermes model family — open-source LLMs (Hermes 4, DeepHermes 3, Hermes 2 Pro, OpenHermes 2.5), fine-tuned on [[Meta|Llama]], [[Mistral]], Yi base models
- Psyche — decentralized training network on [[Solana]], token-incentivized distributed GPU compute
- Nous Portal — model hosting/API service (includes free tiers, unclear revenue)

---

## Related

- [[Agent harnesses]] — competitive landscape
- [[Long agent harnesses]] — investment thesis
- [[Hermes Agent]] — flagship product
- [[Paradigm]] — lead Series A investor
- [[Solana]] — infrastructure for Psyche network
- [[OpenRouter]] — model distribution partner
- [[OpenClaw]] — primary competitor in open-source agent space
- [[Hugging Face]] — model distribution, partial analogue
- [[Together AI]] — compute marketplace analogue

### Cross-vault
- [Technologies: Hermes Agent](obsidian://open?vault=technologies&file=Hermes%20Agent) — technical architecture deep-dive
- [Technologies: agentskills.io](obsidian://open?vault=technologies&file=agentskills.io) — skill standard Hermes uses
- [Technologies: OpenClaw](obsidian://open?vault=technologies&file=OpenClaw) — competitor architecture
