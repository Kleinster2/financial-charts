---
aliases: [Open AI]
tags: [actor, ai, modellab, usa, private]
---

# OpenAI

**OpenAI** — the company that made AI a consumer product, then became a $840B private enterprise trying to outspend every competitor to stay on top. Founded in 2015 as a nonprofit research lab by [[Sam Altman]], [[Ilya Sutskever]], [[Greg Brockman]], and others (including [[Elon Musk]], who left the board in 2018), it reorganized into a capped-profit entity in 2019, then completed conversion to a public benefit corporation in October 2025. Revenue tripled from ~$6B to $20B ARR in 2025, driven by [[ChatGPT]]'s 800M+ weekly active users and 35M+ paid subscribers. But the numbers underneath are brutal: $13.5B net loss in H1 2025, gross margins compressing from 40% to 33% as inference costs quadruple, and no path to profitability before 2029. The bull case is distribution dominance — 64% market share in consumer generative AI, 900M+ users, deepening enterprise penetration. The bear case is that [[Anthropic]] is closing the quality gap while burning 14x less cash, [[Google]] is displacing ChatGPT in the Apple ecosystem, and OpenAI's entire safety brain trust has walked out the door. The $110B mega-round (Feb 2026) buys runway but at a valuation ($840B post-money) that demands flawless execution on the $600B infrastructure buildout, the [[Project Stargate]] partnership, and the bet that the personal agent platform — not just the model — becomes the moat.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Structure | Public benefit corporation (converted Oct 28, 2025) |
| Valuation | $852B post-money ($122B round closed Apr 1, 2026); secondary bids at ~$765B (10% discount) |
| Revenue (2025) | ~$13.1B recognized; $20B exit-rate ARR |
| Revenue (2024) | ~$3.7B recognized; $5.5B exit-rate ARR |
| H1 2025 net loss | $13.5B (incl. R&D $6.7B, S&M $2B) |
| Gross margin | 33% (2025), down from 40% (2024) |
| Inference costs (2025) | $8.4B; projected $14.1B (2026) |
| ChatGPT WAU | 800M-900M (Mar 2026) |
| Paid subscribers | ~35M (Plus/Pro/Team/Enterprise) |
| Enterprise/Team/Edu users | ~9M business users |
| Business clients | ~1.5M |
| [[Consumer]] market share | ~75% (2025), down from 85% (2024) and 100% (2023). 64.5% by gen-AI platform count |
| Total funding raised | ~$168B across 11 rounds |
| Employees | ~4,500 (Mar 2026); targeting ~8,000 by end 2026 |
| CEO | [[Sam Altman]] |
| Board chair | [[Bret Taylor]] |
| Founded | December 2015, San Francisco |
| HQ | San Francisco |

---

## Leadership (current, Apr 2026)

| Function | Leader | Since | Prior | Notes |
|----------|--------|-------|-------|-------|
| CEO | [[Sam Altman]] | 2019 (reinstated Nov 2023) | [[Y Combinator]] | — |
| President | [[Greg Brockman]] | 2015 | [[Stripe]] CTO | Returned from sabbatical Mar 2026 |
| COO | Brad Lightcap | 2023 | Internal | — |
| CEO of Applications | [[Fidji Simo]] | Aug 2024 | [[Meta]] (led Facebook app) | Rebranded role to "CEO of AGI Deployment" |
| Chief Scientist | [[Jakub Pachocki]] | May 2024 | Internal (VP Research) | Replaced [[Ilya Sutskever]] |
| CTO | Vacant | Sep 2024 | [[Mira Murati]] departed → [[Thinking Machines Lab]] | Unfilled for 19+ months |
| [[Infrastructure]] | [[Sachin Katti]] | Nov 2025 | [[Intel]] CTO/AI Officer | Reorganized into 3 groups after own-DC pivot |
| Safety/Alignment | Disbanded | Feb 2026 | Joshua Achiam → "chief futurist" | Mission Alignment team eliminated |
| Research (models) | [[Mark Chen]] | 2024 | Internal | SVP Research |
| Board | [[Bret Taylor]] (chair), [[Larry Summers]] (resigned Nov 2025), [[Nicole Seligman]], Fidji Simo, others | — | — | Taylor installed after Nov 2023 board crisis |

The org chart is the strategy made visible. The CTO vacancy (19 months), the disbanded safety team, and the infrastructure leadership turnover all signal where OpenAI is investing attention and where it isn't. The Simo consolidation (ChatGPT + Codex + Atlas into a "superapp") and the Katti infrastructure reorg are the two structural bets: win the consumer/enterprise platform race against [[Anthropic]], and secure compute without owning the physical assets.

---

## Synopsis

OpenAI is the most heavily funded private company in history and the dominant consumer AI platform, but its financial profile looks more like a hyperscaler buildout than a software company. The $20B ARR headline masks a cost structure growing faster than revenue: inference costs alone hit $8.4B in 2025 and are projected at $14.1B for 2026, compressing gross margins to 33%. The company projects massive losses through 2028 and doesn't expect cash-flow positivity until 2029-2030. The $110B mega-round (Feb 2026) — [[Amazon]] $50B, [[SoftBank]] $30B, [[NVIDIA]] $30B — buys time but creates obligations: $100B in [[AWS]] spend over 8 years, 2 GW of Amazon [[Trainium]] compute, and an implicit IPO path (Amazon's $35B tranche terminates if no IPO/listing by Dec 2028).

The competitive picture is more nuanced than the user numbers suggest. [[Anthropic]]'s [[Claude]] is gaining enterprise share rapidly — overtaking OpenAI in enterprise preference surveys (Jul 2025) while growing from $900M to $14B ARR in the same period OpenAI went from $6B to $20B. Google Gemini replaced ChatGPT as Apple's default AI provider (Jan 2026). The talent exodus — [[Ilya Sutskever]] (SSI, $32B), [[Mira Murati]] (Thinking Machines Lab, $12B), [[John Schulman]] (Anthropic), 7+ researchers to [[Meta]]'s [[Superintelligence]] Lab — has stripped the safety and research bench. The Mission Alignment team was disbanded in Feb 2026. Elon Musk's $134B lawsuit reached an adverse advisory jury verdict for Musk on May 18, 2026, reducing but not fully ending the litigation overhang because the judge retains formal authority.

The strategic bet is infrastructure + distribution: $600B in compute spend by 2030 via [[Project Stargate]] (7 GW planned capacity, $500B commitment), a Cerebras relationship that now appears headed above $20B for inference diversification, and the personal agent platform play (Codex relaunch, [[Peter Steinberger]] acqui-hire). If OpenAI can convert its 900M user base into a durable platform — where agents, not just models, are the product — the current losses are a land grab. If the models commoditize faster than the platform locks in, the $840B valuation becomes the most expensive AI bet in history.

---

## Evolution

The story of OpenAI is the story of a nonprofit research lab that accidentally created a consumer product so powerful it had to become a $840B for-profit company to fund its own ambitions — and whether the resulting entity can outrun the costs of staying at the frontier.

- 2015-2018 (the nonprofit era): Founded in December 2015 with $1B in pledges from [[Sam Altman]], [[Elon Musk]], [[Peter Thiel]], [[Reid Hoffman]], [[Jessica Livingston]], and others. The stated mission: ensure AGI benefits all of humanity. Musk was co-chair alongside Altman. [[Ilya Sutskever]] — recruited from [[Google Brain]] — became chief scientist. [[Greg Brockman]] (ex-CTO of [[Stripe]]) became CTO and later president. The early team published foundational work but had trouble retaining talent against Google and Facebook's compensation. Musk left the board in February 2018, later claiming he departed over disagreements about the organization's direction (and his simultaneous involvement with [[Tesla]] AI). With Musk gone, Altman's influence consolidated.

- 2019 (the turn): In March 2019, OpenAI created a "capped-profit" subsidiary — OpenAI LP — where investors could earn up to 100x returns, with excess flowing to the nonprofit parent. The rationale was straightforward: competing at the frontier required billions, and the nonprofit couldn't raise them. [[Microsoft]] invested $1B and became the exclusive cloud partner. GPT-2 was published in February 2019 with a staged release, OpenAI withholding the full model over misuse concerns — the last time the organization's safety instincts would lead its commercial instincts. The capped-profit structure was a compromise: enough capitalism to fund the mission, enough mission to justify the structure. It satisfied nobody fully, and it wouldn't survive contact with real money.

- 2020-2022 (GPT-3 and the platform): GPT-3 launched in June 2020 with 175B parameters — 100x GPT-2 — and proved that scaling laws worked. The API opened to developers, creating the foundation for every AI startup that followed. [[DALL-E]] (Jan 2021) and [[DALL-E]] 2 (Apr 2022) demonstrated multimodal capabilities. Revenue was still negligible. Microsoft deepened its investment, eventually committing ~$13B cumulative. Meanwhile, tensions over safety and commercialization drove [[Dario Amodei]], Daniela Amodei, and five other senior researchers to leave in early 2021, founding [[Anthropic]] — taking OpenAI's scaling playbook and safety expertise with them. This was the most consequential departure in AI history: it created OpenAI's only credible frontier competitor.

- 2022-2023 (ChatGPT changes everything): ChatGPT launched November 30, 2022, built on GPT-3.5. It reached 100M users in two months — the fastest consumer product adoption in history. What had been a research lab became a consumer platform overnight. GPT-4 followed in March 2023, demonstrating multimodal reasoning that approached human-level on standardized tests. Revenue jumped from near-zero to ~$2B annualized. The January 2023 Microsoft mega-round (~$10B, $29B valuation) gave OpenAI the war chest, and Microsoft embedded GPT into [[Copilot]] across Office, Azure, and Bing. The symbiosis looked perfect: Microsoft got the frontier model, OpenAI got the distribution and compute. But the relationship was already asymmetric — Microsoft was building its own AI capabilities while paying for OpenAI's.

- November 2023 (the board crisis): On November 17, the OpenAI board fired Sam Altman, stating he was "not consistently candid in his communications." The board — including [[Ilya Sutskever]], who had voted for removal — offered no public explanation. Microsoft CEO [[Satya Nadella]] immediately offered Altman a role. Within 72 hours, 700+ of ~770 employees signed a letter threatening to resign and join Microsoft unless Altman was reinstated. Altman returned on November 22. The board was reconstituted with [[Bret Taylor]] as chair, adding [[Larry Summers]] and corporate governance veterans. Sutskever — who had reversed his position during the crisis — remained briefly, then departed in May 2024 to found [[SSI]] (Safe [[Superintelligence]] Inc., raised $2B at $32B valuation by March 2025). The lesson: Altman is OpenAI. The nonprofit governance structure that was supposed to prioritize safety over commerce had been stress-tested and failed — the employees chose Altman over the board, and the board folded.

- 2024 (scaling the platform): Revenue surged from ~$2B to $5.5B exit-rate ARR. GPT-4o launched (May), then o1 reasoning models (September). ChatGPT hit 300M WAU by December. The October 2024 round ($6.6B at $157B valuation) brought in [[Thrive Capital]], NVIDIA, and Microsoft. Enterprise adoption accelerated: DevDay 2024 delivered GPT-4 Turbo (128K context, 3x cheaper), custom GPTs, the GPT Store, and the Assistants API. But the talent bleeding continued: [[Mira Murati]] (CTO) departed in September, founding Thinking Machines Lab ($12B valuation by Feb 2025). [[John Schulman]] (co-founder) left for [[Anthropic]]. [[Andrej Karpathy]] departed. The pattern was unmistakable: OpenAI's safety and research leaders were leaving, and the replacements were commercial operators.

- 2025 (for-profit conversion and the infrastructure bet): The year of structural transformation. Revenue hockey-sticked to $20B ARR — the first $1B revenue month came in July 2025. GPT-5 launched August 7, incorporating the o-series reasoning models as "thinking mode." The March 2025 SoftBank-led round ($40B at $300B) included a clawback: SoftBank could reduce its commitment to $20B if the for-profit restructuring wasn't completed by year-end. On October 28, OpenAI converted from capped-profit to a public benefit corporation. The nonprofit became the OpenAI Foundation, retaining ~26% ownership and the right to appoint all board directors. Microsoft's stake was restructured from 49% capped-profit share to ~27% equity, with exclusivity extending through 2032. The conversion unlocked the mega-round but also exposed the mission tension: [[Larry Summers]] resigned from the board in November 2025 after House panel emails linked him to [[Jeffrey Epstein]]. The io acquisition ($6.4B, May 2025) — buying [[Jony Ive]]'s hardware startup — signaled ambitions beyond software. And OpenAI announced $600B in own compute spend by 2030, with the [[Project Stargate]] JV ($500B commitment) as the centerpiece.

- Jan-Feb 2026 (the mega-round and its obligations): The $110B round closed February 27, 2026 — the largest private financing in history. [[Amazon]] committed $50B ($15B immediate in Series C preferred, $35B conditional on milestones including IPO/listing, terminates Dec 2028 if uninvested). [[SoftBank]] and [[NVIDIA]] each committed $30B. In exchange, OpenAI committed to $100B in [[AWS]] spending over 8 years and 2 GW of Amazon [[Trainium]] compute. NVIDIA's participation came with friction: [[Reuters]] reported (Feb 2) that OpenAI was dissatisfied with NVIDIA chips for inference workloads, targeting ~10% of inference from alternatives. The initial $10B+ Cerebras deal (2026-2028, 750 MW, inference-focused) formalized the diversification, and [[Reuters]] reported on Apr 17 that the commitment had since expanded to more than $20B over three years, with potential total spend near $30B, roughly $1B of OpenAI funding for new data centers, and warrants that could rise toward a 10% stake in Cerebras. GPT-5.4 launched March 5 with agentic capabilities. The Stargate Abilene expansion (1.2 GW to 2 GW) was cancelled March 6, though the core 4.5 GW Oracle contract remained intact. The Mission Alignment team was disbanded in February; its leader Joshua Achiam was moved to a "chief futurist" role. In a parallel retreat, OpenAI abandoned plans to build and own data centers (The Deep Dive, Mar 17) — lenders refused to underwrite construction costs for a company not yet profitable. The pivot to renting from Azure, [[AWS]], and [[Google Cloud]] triggered an infrastructure leadership overhaul: Sachin Katti (ex-[[Intel]] CTO/AI Officer, joined Nov 2025) took charge of all infrastructure teams, reorganized into three groups (technical design, commercial partnerships, facility operations). Keith Heyde (Director of Physical [[Infrastructure]]) departed; Peter Hoeschele, Shamez Hemani, and Anuj Saharan — the core [[Project Stargate|Stargate]] infrastructure team — all left for the same unnamed startup (Apr 10). The [[UK]] Stargate project was paused April 9, citing energy costs and regulatory hurdles. See [[OpenAI Infrastructure Spend]] and [[OpenAI talent exodus]] for details.

- March-April 2026 (the focus pivot): [[NVIDIA]] CEO [[Jensen Huang]] said he expects his recent $40B investment across OpenAI and [[Anthropic]] to be his "last money in" — both companies will go public this year. The paradox is sharp. OpenAI has the most users (900M+), the most capital ($168B raised), and the highest valuation ($840B) of any private company ever. But it also has no CTO, no chief scientist, a disbanded safety team, co-founders scattered across competitors (Sutskever at SSI, Schulman at Anthropic), gross margins compressing, losses deepening, and a $134B Musk lawsuit heading to jury trial in April. The acquisition of [[Promptfoo]] (announced Mar 9) — an AI security testing platform used by 25%+ of the Fortune 500 — signals the enterprise agent push is serious. And now, under pressure from [[Anthropic]]'s [[Claude Code]] and [[Claude Cowork]] dominance, OpenAI is making its most significant strategic pivot since the for-profit conversion. [[Fidji Simo]] (CEO of applications, hired Aug 2024) told staff they "cannot miss this moment because we are distracted by side quests" and announced plans to merge [[ChatGPT]], [[Codex]], and Atlas browser into a desktop "superapp." [[Greg Brockman]] returned from sabbatical to help oversee the product revamp. Simo called Anthropic's success a "wake-up call." The organizational diagnosis is damning: compute resources shifting between teams at the last minute, [[Sora]] housed under research despite being a consumer product, no clear strategic direction. [[Sam Altman]]'s earlier framing of "betting on a series of startups" inside OpenAI — which launched Sora (standalone app that flatlined), Atlas browser, hardware, and e-commerce features in 2025 — is now acknowledged as the problem. [[Codex]] recovered some ground (2M+ WAU, up 4x since January) after GPT-5.4 launched, but Anthropic remains the "dominant AI provider for businesses" (WSJ). The hiring push makes the shift concrete: OpenAI plans to nearly double headcount from ~4,500 to ~8,000 by end 2026, adding ~12 employees/day, with a new SF lease bringing its footprint past 1M sq ft (FT, Mar 21). New hires are concentrated in product development, engineering, research, and sales, plus "technical ambassadorship" specialists — forward-deployed engineers embedded in business customers to help them customize AI models, an approach pioneered by [[Palantir]]. Revenue mix is shifting accordingly: OpenAI anticipates 50% of revenue from business customers by year-end, up from ~40% today. The company is also in talks with private equity firms to launch a joint venture deploying OpenAI products in PE portfolio companies — offering a guaranteed minimum 17.5% return to PE investors to ease the high upfront cost of AI deployment (All-In pod, Mar 27). Beyond enterprise, OpenAI is exploring advertising to monetize its 900M+ free users (90%+ don't pay). Both OpenAI and Anthropic are gearing up for public listings as early as this year. One OpenAI investor told FT the risk is being left "in no man's land" — with [[Google]] competing fiercely for chatbot users and Anthropic ensconced with businesses. In a separate messaging play, [[Fidji Simo]] — who rebranded her role to "CEO of AGI deployment" — acquired [[TBPN]], the daily tech talk show with ~59K [[YouTube]] subscribers and outsized influence among Silicon Valley's terminally online tech crowd (WSJ, Apr 2 2026). OpenAI claimed TBPN would maintain editorial independence but executives hope to absorb the company's messaging into the show's content. The acquisition underscores how seriously OpenAI is taking narrative control alongside the product pivot.

The bet is that scale — user scale, compute scale, capital scale — creates a moat before the models commoditize. The risk is that OpenAI's year of distraction gave Anthropic an enterprise lead that a superapp consolidation can't close.

---

## Products

### Models (current, March 2026)

| Model | Released | Role |
|-------|----------|------|
| [[OpenAI GPT-5.4]] | Mar 5, 2026 | Flagship: agentic, computer use, Thinking/Pro variants |
| GPT-5.3 Instant | Early Mar 2026 | Fast tier |
| GPT-5.2 | Dec 2025 | Previous flagship, Codex backbone |
| GPT-5 | Aug 7, 2025 | First unified model with "thinking mode" (o-series merged) |
| o3 / o4-mini | Apr 2025 | Reasoning-focused (chain-of-thought), retiring |
| [[GPT-4.5]] | Feb 2025 | Research preview, deprecated Jul 2025 |
| [[GPT\|GPT-4o]] | May 2024 | Omni — native voice/vision. Retired Feb 2026 |

### [[Consumer]] and enterprise

- [[ChatGPT]] — consumer/enterprise interface (Free/$8 Go/$20 Plus/$200 Pro/Team/Enterprise/Edu)
- [[Codex]] — coding agent (GPT-5.2-Codex), MacOS app launched Feb 2026, repo-scale reasoning. 2M+ WAU (Mar 2026, up 4x since Jan). Centerpiece of "superapp" strategy
- [[Sora]] — video generation (Sora 2/Sora 2 Pro); standalone app launched Sep 2025, usage flatlined. Shut down entirely Mar 2026. [[Disney]] $1B investment + licensing deal to integrate Sora into Disney+ cancelled (All-In pod, Mar 27)
- Atlas — web browser (being merged into "superapp")
- Deep Research — o3-powered comprehensive web research agent (launched Feb 2, 2025)
- Whisper — speech-to-text
- [[AgentKit]] — SDK for building/deploying [[AI agents]] (announced Oct 2025 Dev Day)
- Realtime API — low-latency bidirectional audio streaming (GA)

### Hardware

- [[Acquired]] [[Jony Ive]]'s startup "io" for $6.4B (May 2025). First hardware prototypes completed Nov 2025: pocket-sized, screenless, audio-based device with cameras/microphones. [[Target]] launch late 2026 or early 2027.
- [[Ming-Chi Kuo]] reported (Apr 27, 2026) a separate AI agent smartphone in development — [[Qualcomm]] + [[MediaTek]] joint chip co-design, [[Luxshare Precision]] exclusive assembly. Mass production targeted 2028; 300-400M annual shipments target; specs and suppliers to be finalized end-2026 / early-2027. Two product tracks (io companion + agent smartphone), not the same device. See [[OpenAI hardware program]].

---

## Financials

### Revenue trajectory

| Period | Revenue / ARR | Note |
|--------|--------------|------|
| 2023 | ~$2B | First meaningful revenue year |
| 2024 | ~$3.7B recognized; $5.5B exit ARR | ChatGPT Plus drove bulk |
| H1 2025 | $4.3B recognized | Already exceeded full 2024 |
| Jul 2025 | First $1B revenue month | Up from ~$500M/mo at start of year |
| FY 2025 | ~$13.1B recognized; $20B exit ARR | 233% YoY growth on exit ARR |
| 2026 proj. | $20B+ entering year | |
| 2030 proj. | $85B-280B (varies by source) | OpenAI internal projections |

### ChatGPT revenue (2024)

[[ChatGPT]] generated $2.7B in 2024, ~75% of OpenAI's total revenue. ChatGPT H1 2025 downloads: 350M.

### Revenue recognition vs [[Anthropic]]

[[Chamath Palihapitiya]] (8090 Capital, Mar 27 2026) on why headline revenue comparisons are misleading: OpenAI is ~75% consumer subscriptions, ~25% API; [[Anthropic]] is nearly the inverse. OpenAI uses conservative consumer-subscription rev rec; Anthropic recognizes "gross tonnage" as revenue. When OpenAI's $20B ARR is compared to Anthropic's reported run rate, they are *"two totally different conversations"* — normalizing would show OpenAI still the larger revenue generator, with Anthropic catching up. Both will need clean, [[GAAP]]-normalized disclosures for their IPOs.

### Cost structure

| Item | 2025 | 2026 proj. |
|------|------|-----------|
| Inference costs | $8.4B | $14.1B |
| R&D | $6.7B (H1 alone) | — |
| S&M | $2B (H1 alone) | — |
| H1 net loss | $13.5B | — |
| Gross margin | 33% (down from 40% in 2024) | — |

Profitability timeline: massive losses projected through 2028, cash-flow positive target 2029-2030.

---

## Funding rounds

| Date | Round | Amount | Valuation | Key Investors |
|------|-------|--------|-----------|---------------|
| 2019 | Strategic | $1B | — | [[Microsoft]] |
| Jan 2023 | Strategic | ~$10B | ~$29B | [[Microsoft]] (cumulative ~$13B) |
| Late 2023 | Secondary | — | ~$80B | Employee stock |
| Oct 2024 | Series | $6.6B | $157B | [[Microsoft]], [[NVIDIA]], [[Thrive Capital]] |
| Mar 2025 | SoftBank-led | $40B | $300B post | [[SoftBank]] ($30B), Microsoft, [[Coatue]], [[Altimeter]], Thrive, [[Founders Fund]], Magnetar |
| Oct 2025 | Employee secondary | ~$6.6B | $500B | SoftBank, Thrive, [[Dragoneer]], [[MGX]], [[T. Rowe Price]] |
| Feb 27, 2026 | Mega-round | $122B | ~$852B post | [[Amazon]] ($50B), [[SoftBank]] ($30B), [[NVIDIA]] ($30B), plus tech giants, VCs, retail |

Total raised: ~$180B+ across 11 rounds.

![[openai-private-valuation-arc-mar2026-ft.png]]
*Top-valued private companies by post-money valuation ($bn), Jan 2024–Mar 2026. OpenAI rises from $29B (Jan 2024) → $80B (Feb 2024) → $157B (Oct 2024) → $300B (Mar 2025) → $500B (Oct 2025) → $812B (Jan 2026) → $852B (Mar 2026). [[SpaceX]] reaches $1,250B by Mar 2026; [[ByteDance]] flat at $480B; [[Anthropic]] from $18B to $380B. OpenAI's climb from the bottom of the top-10 to second place in 26 months tracks the model release cadence (GPT-4o May 2024, o1 Sep 2024, GPT-5 Aug 2025, GPT-5.4 Mar 2026) and the SoftBank/Amazon/NVIDIA mega-rounds. Source: FT / Crunchbase, FT research (animated chart, Apr 29 2026).*

### Top-10 private company valuations, monthly ($bn)

Extracted from 27 FT animated-chart frames (Mar 2024 frame added separately on May 13). Blank = company outside top 10 that month.

| Month | OpenAI | SpaceX | ByteDance | Anthropic | xAI | Ant Group | Stripe | Databricks | Reliance Retail | Waymo | Revolut |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jan 2024 | 29 | 137 | 220 | 18.4 | — | 150 | 50 | 43 | 101.4 | 30 | 0 |
| Feb 2024 | 80 | 137 | 220 | 18.4 | — | 150 | 50 | 43 | 101.4 | 30 | — |
| Mar 2024 | 80 | 137 | 220 | 18.4 | — | 150 | 52.7 | 43 | 101.4 | 30 | 0 |
| Apr 2024 | 80 | 137 | 220 | 18.4 | 1 | 150 | 65 | 43 | 101.4 | 30 | — |
| May 2024 | 80 | 137 | 220 | 18.4 | 24 | 150 | 65 | 43 | 101.4 | 30 | — |
| Jun 2024 | 80 | 137 | 220 | 18.4 | 24 | 150 | 65 | 43 | 101.4 | 31.3 | — |
| Jul 2024 | 80 | 137 | 220 | 18.4 | 24 | 150 | 65 | 43 | 101.4 | 45 | — |
| Aug 2024 | 80 | 137 | 220 | — | 24 | 150 | 65 | 43 | 101.4 | 45 | 45 |
| Sep 2024 | 130.3 | 137 | 220 | — | 24 | 150 | 65 | 43 | 101.4 | 45 | 45 |
| Oct 2024 | 157 | 137 | 220 | — | 45.8 | 150 | 65 | 43 | 101.4 | 45 | 45 |
| Nov 2024 | 157 | 137 | 220 | — | 50 | 150 | 65 | 49.9 | 101.4 | 45 | 45 |
| Dec 2024 | 157 | 137 | 220 | — | 50 | 150 | 65 | 62 | 101.4 | 45 | 45 |
| Jan 2025 | 157 | 137 | 220 | — | 50 | 150 | 89.8 | 62 | 101.4 | 45 | 45 |
| Feb 2025 | 241.8 | 137 | 220 | — | 50 | 150 | 91.5 | 62 | 101.4 | 45 | 45 |
| Mar 2025 | 300 | 137 | 220 | 61.5 | 50 | 150 | 91.5 | 62 | 101.4 | — | 45 |
| Apr 2025 | 300 | 137 | 220 | 61.5 | 50 | 150 | 91.5 | 62 | 101.4 | — | 45 |
| May 2025 | 300 | 137 | 220 | 61.5 | 50 | 150 | 91.5 | 62 | 101.4 | — | 45 |
| Jun 2025 | 300 | 137 | 220 | 61.5 | 50 | 150 | 91.5 | 62 | 101.4 | — | 45 |
| Jul 2025 | 300 | 345.7 | 220 | 61.5 | 50 | 150 | 91.5 | 62 | 101.4 | — | 45 |
| Aug 2025 | 300 | 400 | 220 | 173.3 | 50 | 150 | 105.5 | 97 | 101.4 | — | 45 |
| Sep 2025 | 428.5 | 400 | 220 | 183 | 50 | 150 | 106.7 | 100 | 101.4 | — | 45 |
| Oct 2025 | 500 | 400 | 397.4 | 183 | 50 | 150 | 106.7 | 100 | 101.4 | — | 65.5 |
| Nov 2025 | 500 | 688.9 | 480 | 183 | 50 | 150 | 106.7 | 124.6 | 101.4 | — | 75 |
| Dec 2025 | 500 | 800 | 480 | 183 | 202.8 | 150 | 106.7 | 134 | 101.4 | — | 75 |
| Jan 2026 | 812.2 | 1,213.2 | 480 | 363.9 | — | 150 | 154.7 | 134 | 101.4 | 119.4 | 75 |
| Feb 2026 | 850.8 | 1,250 | 480 | 380 | — | 150 | 159 | 134 | 101.4 | 126 | 75 |
| Mar 2026 | 852 | 1,250 | 480 | 380 | — | 150 | 159 | 134 | 101.4 | 126 | 75 |

The OpenAI trajectory has four distinct step-functions visible in the data: Jan→Feb 2024 (Microsoft $10B/$29B), Aug→Sep→Oct 2024 ($80B→$130B→$157B on the [[Series E]] round), Jan→Mar 2025 ($157B→$300B on the SoftBank-led $40B), and Aug→Oct→Jan 2026 ($300B→$500B→$812B on the Oct 2025 secondary and the $122B Feb 2026 mega-round closing). The plateau periods between rounds are where the company waits for the next financing event — the steps are not organic growth but funding marks. SpaceX shows the cleanest contrast: similar mega-step in Jul-Dec 2025 ($137B→$800B) but on a different revenue and FCF base. *Note: Mar 2026 SpaceX includes [[xAI]] in the consolidated entity from Feb 2026 — the $1,250B figure is post-merger.* Source: FT / Crunchbase + FT research, animated chart Apr 29 2026.

### Amazon $50B structure

$15B in Series C preferred stock (due Mar 31, 2026). Remaining $35B conditional on milestones including IPO or direct listing — terminates if not invested by Dec 31, 2028. OpenAI committed to $100B [[AWS]] spend over 8 years and 2 GW of [[Amazon]] [[Trainium]] compute. [[AWS]] becomes exclusive cloud distributor for Frontier enterprise platform (alongside Azure for APIs).

### SoftBank clawback

The March 2025 $30B commitment had a clawback clause — could be reduced to $20B if the for-profit restructuring wasn't completed by Dec 31, 2025. Restructuring completed Oct 28, 2025.

---

## Ownership estimates (Feb 2026)

| Entity | Est. Stake | Notes |
|--------|-----------|-------|
| [[OpenAI Foundation]] (nonprofit) | ~26% | Appoints all board directors; warrant for additional shares |
| [[Microsoft]] | ~27% | Down from 49% capped-profit share; restructured Oct 2025 |
| Employees/founders | ~20-25% | Including former employees |
| [[SoftBank]] | ~5-8% | Multiple rounds |
| [[Amazon]] | ~5-7% | Feb 2026 round; conditional tranche pending |
| [[NVIDIA]] | ~3-5% | Feb 2026 round |
| Other investors | ~10-15% | Thrive, Coatue, Altimeter, Founders Fund, etc. |

Microsoft receives 20% of OpenAI revenue through 2032. Sam Altman reportedly not taking equity in the for-profit structure — governance question about incentive alignment.

---

## Leadership

### Current

| Role | Person |
|------|--------|
| CEO | [[Sam Altman]] (co-founder) |
| CEO of Applications | [[Fidji Simo]] (joined Aug 2024; oversees product, finance, strategy) |
| President | [[Greg Brockman]] (co-founder; returned from sabbatical, now leads computing + product revamp) |
| COO | Brad Lightcap |
| Chief Research Officer | Mark Chen |
| CTO of Applications | Vijaye Raji (joined via Statsig acquisition) |
| Board chair | [[Bret Taylor]] |
| CTO | Vacant since Sep 2024 |

### Research organization (Apr 2026)

[[Jakub Pachocki]] (Unsupervised Learning, Apr 9 2026) on OpenAI's research structure: the company explicitly budgets a "large chunk" of compute to the most scalable methods — the approaches believed most responsible for driving general model intelligence. Three criteria for experiment prioritization: (1) empirical evidence, (2) do we understand why it works, (3) do we expect it to scale. This discipline resists the temptation to parcel compute across many smaller experiments even when individual allocations could be more efficient. The research org is shifting from pure capability hill-climbing to deployment urgency: "We believe the models are now capable enough — not as smart as people in all ways — but capable enough to actually materially change the economy."

Research milestones being targeted: research-level intern capabilities by September 2026, fully automated AI researcher by March 2028. As of April 2026, both targets remain active. The majority of coding at OpenAI is now done via [[Codex]]. [[GPT|GPT-5.2 Pro]] has generated "minor but quite impactful" research ideas that OpenAI is using internally.

Alignment research is viewed as "a core part of research" rather than a separate function. Pachocki champions [[Chain-of-thought monitoring]] — using reasoning models' hidden CoT as an interpretability tool — and participated in a cross-lab scheming collaboration with [[Anthropic]] and [[DeepMind]]. He described his belief in "a research path that actually gets us to an extremely happy world" as having "increased quite a lot," while acknowledging the industry must "be prepared to take trade-offs and possibly slow down development depending on what we see."
| Chief Scientist | [[Jakub Pachocki]] (confirmed Apr 2026; joined OpenAI early 2017) |

### Board (post-restructuring)

[[Bret Taylor]] (chair), [[Adam D'Angelo]], Dr. Sue Desmond-Hellmann (fmr CEO Gates Foundation), Dr. Zico Kolter, Gen. Paul Nakasone (ret., fmr NSA/CYBERCOM), Adebayo Ogunlesi, Nicole Seligman (fmr EVP/GC [[Sony]]), [[Sam Altman]]. [[Larry Summers]] resigned Nov 2025 after House panel [[Jeffrey Epstein]] emails.

### Key departures

| Person | Departed | Went to | Valuation |
|--------|----------|---------|-----------|
| [[Ilya Sutskever]] | May 2024 | [[SSI]] (founder) | $32B |
| [[Mira Murati]] | Sep 2024 | Thinking Machines Lab (founder) | $12B |
| [[John Schulman]] | Aug 2024 | [[Anthropic]] | — |
| [[Jan Leike]] | May 2024 | [[Anthropic]] | — |
| [[Andrej Karpathy]] | 2024 | Independent (education) | — |
| [[Caitlin Kalinowski]] | Mar 2026 | — (resigned over [[Pentagon]] deal) | — |
| 7+ researchers | Summer 2025 | [[Meta]] [[Superintelligence]] Lab | — |

Jan Leike on departure: "Safety has taken a backseat to shiny products." Mission Alignment team disbanded Feb 2026; leader Joshua Achiam moved to "chief futurist" role.

---

## [[Infrastructure]]

### [[Project Stargate]]

$500B JV with [[SoftBank]] (40% ownership, financial lead), OpenAI (40%, operational lead), [[Oracle]] ($7B), [[MGX]] ($7B). Targeting 10 GW US AI infrastructure by 2029.

| Site | Capacity | Status |
|------|----------|--------|
| Abilene, TX | Core facility — 1.2 GW, 450,000+ GB200s under [[Oracle]] 15-yr lease | Operational; 2 GW expansion cancelled Mar 6, 2026 |
| Shackelford County, TX | Planned | Announced Sep 2025 |
| Dona Ana County, NM | Planned | Announced Sep 2025 |
| Lordstown, OH | Under construction | Expected operational 2026 |
| Milam County, TX | Planned | Announced Sep 2025 |
| Stargate [[UAE]] | 1 GW (200MW by YE2026) | Partnership with [[G42]], Oracle, SoftBank, NVIDIA |
| [[Norway]] | 230 MW | Hydropower |
| [[Argentina]] | 500 MW by 2027 | $25B, [[Patagonia]] |

Oracle partnership alone: $300B over 5 years for 4.5 GW capacity.

### Compute diversification

- [[Cerebras]] deal: initially $10B+, 2026-2028, 750 MW, inference-focused. [[Reuters]] reported Apr 17 that commitments have grown to >$20B over three years, could reach ~$30B total, and may include ~$1B of OpenAI funding for new data centers plus warrants toward a 10% stake. Altman was an early Cerebras investor.
- NVIDIA friction: [[Reuters]] (Feb 2, 2026) reported OpenAI dissatisfied with NVIDIA chips for inference. [[Target]]: ~10% of inference from alternatives. Affected products: Codex, agent-to-agent communication.
- OpenAI's own compute spend target: ~$600B by 2030 (revised from $1.4T total partner commitments).

---

## Competitive positioning

| Company | Est. ARR (early 2026) | Funding | Key differentiator |
|---------|----------------------|---------|-------------------|
| OpenAI | ~$25B (latest known) | ~$180B+ | [[Consumer]] scale, distribution, brand |
| [[Anthropic]] | ~$30B (Apr 2026) | ~$57B | Enterprise trust, safety-first, capital efficiency |
| [[Google]] DeepMind | Not reported separately | Google internal | Workspace/Cloud distribution, Gemini |
| [[xAI]] | Not reported | ~$12B | Speed, real-time search, X distribution |
| [[Meta]] AI | Not reported | Internal | Open-source [[Llama]], [[Superintelligence]] Lab |

[[NEA]]'s Mustapa Neimucha (The Information, Apr 7 2026) identified four areas where OpenAI retains advantages over [[Anthropic]]: (1) ads (~$100M ARR, intent-based, benefiting from [[Gemini]] not monetizing); (2) device strategy (Apple ecosystem opportunity); (3) custom chips (working with [[Broadcom]]); (4) consumer brand (ChatGPT as the generic term outside tech/finance). On brand, Neimucha acknowledged Anthropic may have the edge among the informed ("Anthropic is a bit of a better brand right now") but OpenAI dominates mass consumer awareness — citing [[Sam Altman]]'s Super Bowl claim that "more people in [[Texas]] use ChatGPT than people in the world use [[Claude]]."

Enterprise market share (Ramp data, Mar 2026): New corporate AI clients are choosing [[Anthropic]] at 3x the rate of OpenAI — a complete reversal from a year ago (FT, Mar 21 2026). Among companies paying for AI models, Anthropic holds ~30% share vs OpenAI ~25% and [[Google]] ~10% ([[Ramp]] AI Index, Feb 2026). OpenAI's spokesman called the [[Ramp]] methodology "insane" — "Large enterprise clients do not pay for multimillion dollar contracts with a credit card." Anthropic overtook OpenAI in enterprise preference surveys (Jul 2025, TechCrunch).

![[ramp-anthropic-vs-openai-new-customers-mar2026.png]]
*Share of new corporate AI clients picking each startup. Anthropic ~80% vs OpenAI ~20% by Feb 2026. Source: Ramp AI Index (FT, Mar 21 2026)*

![[ramp-anthropic-market-share-mar2026.png]]
*Market share among companies paying for AI models. Anthropic ~30%, OpenAI ~25%, Google ~10% by Jan 2026. Source: Ramp AI Index (FT, Mar 21 2026)*

### Apple relationship weakening

ChatGPT was integrated into [[Siri]]/iOS in 2024-2025 (no cash exchanged — Apple viewed distribution as compensation). In January 2026, [[Apple]] announced [[Google]] Gemini will power Apple Intelligence and new [[Siri]], displacing ChatGPT as the default.

### Legal threat over 2024 iPhone integration (FT/Bloomberg May 14, 2026)

OpenAI is exploring legal action against [[Apple]] over the 2024 iPhone deal, per FT reporting (Bloomberg first carried the threat). The grievance, attributed to people familiar with OpenAI's thinking: a "pattern of behaviour from Apple... showing no interest in investing required resources to deliver on the promise of the partnership... focused solely on extracting a tax for their market position."

Two structural shifts make this stage of the dispute more than a contract argument:

1. Apple's January 2026 announcement that [[Google]] [[Gemini]] would power Apple Intelligence positioned ChatGPT as a fallback rather than the default. The FT framed that as a "rebuke" of OpenAI.
2. OpenAI has poached talent from Apple's AI team and hired former Apple design chief [[Jony Ive]] to work on a new device — explicitly positioned by analysts as a potential iPhone competitor (see the device note in the OpenAI hardware push section). The 2024 partnership has now structurally shifted into a competitor relationship.

Apple's expected announcement with its new operating system later this year — allowing users to plug into multiple third-party AI models — would further dilute the original OpenAI-only integration. The legal threat is the lever OpenAI is reaching for to either restore Apple's promotional / engineering investment in the integration or extract damages.

Timing context: the legal threat lands the same week as the Musk-vs-OpenAI for-profit-conversion case verdict expected — OpenAI now defending one suit and threatening another in adjacent windows.

*Source: [OpenAI considering legal action against Apple over iPhone AI deal](https://www.ft.com/content/e6505cf8-9e86-4053-bd34-6ed376c74443), FT, May 14, 2026, by George Hammond + Michael Acton (SF). Original report: Bloomberg.*

---

## Key risks

### Financial
- Losses deepening: $13.5B net loss in H1 2025 alone
- Inference costs growing faster than revenue (quadrupled in 2025)
- Gross margin compression: 40% to 33%
- No profitability until 2029-2030 at earliest
- $100B [[AWS]] spend commitment over 8 years

### Competitive
- [[Anthropic]] gaining enterprise share with 14x less cash burn
- [[Google]] Gemini displacing ChatGPT in Apple ecosystem
- [[Meta]] poaching research talent aggressively
- Model capability convergence reducing differentiation
- [[Claude]] Code at $2.5B ARR vs OpenAI's Codex playing catch-up

### Legal
- [[Elon Musk]] lawsuit: advisory jury rejected Musk's damages claim on May 18, 2026; judge retains formal authority because the jury was advisory.
- 50+ copyright lawsuits consolidated in SDNY (before Judge Stein)
- GEMA v. OpenAI: German court ruled training on copyrighted data without license violates German copyright law (appeal expected 2026)

### Talent and governance
- No CTO since Sep 2024, no chief scientist since May 2024
- Co-founders scattered: Sutskever (SSI), Schulman (Anthropic), Brockman (sabbatical)
- Mission Alignment team disbanded Feb 2026
- Microsoft 20% revenue share through 2032 is a perpetual margin drag
- Altman reportedly not taking equity — incentive alignment question

---

## Apr 2026 — secondary market + IPO pressure

*Data from [[All-In Podcast]] Episode 222, April 3, 2026; [[Bloomberg]], April 6, 2026*

~6 institutional investors (hedge funds, VCs holding large stakes) approached [[Next Round Capital]] in recent weeks looking to sell ~$600M in OpenAI shares. [[Next Round Capital]] founder Ken Smythe ($2.5B in total transactions handled): *"We literally couldn't find anyone in our pool of hundreds of institutional investors to take these shares."* Bids coming in at ~$765B — 10% discount from $850B. Last year, these shares would have been "snatched up within days."

[[Morgan Stanley]] and [[Goldman Sachs]] offering OpenAI shares to wealth management clients with zero carry fees — through authorized channels OpenAI established to counter high-fee broker model. By contrast, Goldman charges usual carry (~15-20% of profits) for [[Anthropic]] shares. Zero-carry for OpenAI vs premium-carry for Anthropic signals where bank demand sits.

Finalized largest-ever private fundraising ($122B, Apr 1) — $122B from tech giants, VCs, and retail investors. But primary fundraising and secondary sales don't follow the same playbook: existing investors often buy into new rounds to maintain stakes (to avoid founder friction), then sell exposure on the secondary market.

![[openai-vs-anthropic-valuation-apr2026.png]]
*OpenAI vs Anthropic valuation history. OpenAI at $852B is currently more than double Anthropic's $380B. Source: [[PitchBook]], [[Bloomberg]]*

Simultaneously, secondary marketplaces (Augment, [[Hiive]], [[Next Round Capital]]) are seeing record demand for [[Anthropic]] shares. Buyers have $2B ready to deploy. [[Hiive]] registered >$1.6B in demand at a premium. Bids value Anthropic at ~$600B — 58% above its $380B Series G. Augment co-founder Adam Crawley: *"It's just better risk-reward right now. People are betting that Anthropic's valuation will catch up with OpenAI's."* [[Hiive]] co-founder Prab Rattan: *"The demand is one of the highest we've ever seen — it's essentially unlimited interest."* The gap between OpenAI's inability to find buyers and Anthropic's excess demand is the clearest secondary-market signal of competitive momentum shift.

Some investors grown cautious over OpenAI's soaring operating costs — committed to spend far more than Anthropic on infrastructure. While OpenAI touts its consumer base, it's moving slowly on capturing enterprise clients. Anthropic has dominated the higher-margin enterprise market, and its growth trajectory appears stronger ([[Bloomberg]], Apr 6).

Scale paradox: [[Chamath Palihapitiya|Chamath]]: "I've never seen a business like this... these are trillion dollar companies" in terms of revenue potential and market impact. However, capital absorption remains the primary constraint — the amount of money required to stay competitive is growing faster than the ability to deploy it efficiently.

Tech sector P/E convergence thesis: Chamath prediction: after mega-IPOs from [[SpaceX]], OpenAI, and [[Anthropic]], the entire tech sector's price-to-earnings multiples will converge DOWN toward non-tech sector P/E ratios. Reasoning: these AI companies' capabilities will erode existing tech companies' competitive moats. "It's going to be nasty" for incumbent tech valuations.

TBPN acquisition context: The [[TBPN]] deal (already covered above) represents OpenAI's recognition that narrative control is as important as product leadership in the competitive landscape.

---

## Apr 28, 2026 — WSJ revenue miss report

The day after the Microsoft exclusivity reset, the [[Wall Street Journal]] reported that OpenAI fell short of its own internal projections for both user growth and revenue. Two specific shortfalls were cited: a missed target of 1 billion weekly active users by year-end 2025 (current ~900M per company disclosure), and missed monthly revenue targets across early 2026 amid rising competition in coding (vs [[Claude Code]]) and enterprise services (vs [[Anthropic]] / [[Google]]). [[ChatGPT]]'s share of generative-AI web traffic dropped from 86.7% (Jan 2025) to 64.5% (Jan 2026); [[Gemini]] rose from 5.7% to 21.5% over the same window.

The most load-bearing detail in the WSJ report: CFO [[Sarah Friar]] was reported to have raised internal concerns about whether OpenAI can fund its committed compute contracts if revenue growth does not accelerate. CFO worries surfacing in internal documents reaching reporters is a different signal than public earnings guidance — it reflects internal risk discussions the company has not yet had publicly.

OpenAI's pushback was direct: *"This is ridiculous. We are totally aligned on buying as much compute as we can."* The line is technically consistent with the WSJ findings — wanting compute is not the same as being able to pay for committed compute over multi-year contracts.

The sell-off priced the entire AI capex stack: [[Oracle]] -4.05%, [[CoreWeave]] -5.83%, [[Broadcom]] -4.39%, [[AMD]] -3.41%, [[Marvell Technology|Marvell]] -3.15%, [[NVIDIA]] -1.59%, [[IREN]] -8.10%, [[Cipher Mining|Cipher]] -4.96%, [[SoftBank]] -10% in Tokyo. The graduated chip-stack pricing — NVDA absorbing better than AMD or AVGO — reflects diversification of customer base. [[Microsoft]] was roughly flat: the [[Microsoft-OpenAI exclusivity end|Apr 27 reset]] put MSFT structurally better-positioned to absorb OpenAI revenue weakness than to benefit from OpenAI revenue strength.

The structural read connects to the [[OpenAI#Apr 2026 — secondary market + IPO pressure|Apr 3-6 secondary-market signal]]: institutional investors trying to sell ~$600M of OpenAI shares at a 10% discount to the $852B post-money mark. The internal-revenue narrative now matches the secondary-market narrative — the market is repricing OpenAI risk faster than primary funding rounds can clear.

See [[2026 OpenAI revenue miss]] for the full event note covering compute-coverage gap mechanics, individual stock reactions, and watch-list of second-order effects.

*Source: WSJ via [CNBC](https://www.cnbc.com/2026/04/28/openai-reportedly-missed-revenue-targets-shares-of-oracle-and-these-chip-stocks-are-falling.html), [Sherwood News](https://sherwood.news/markets/openai-linked-stocks-suffer-after-wsj-reports-that-the-company-has-missed-key-revenue-and-user-targets/), [24/7 Wall St](https://247wallst.com/investing/2026/04/28/openais-revenue-miss-is-ripples-through-sp-500-while-earnings-pour-in/), Apr 28, 2026.*

---

## Apr 27, 2026 — Microsoft exclusivity ended

[[Microsoft]] and [[OpenAI]] announced a restructured partnership ending [[Microsoft]]'s exclusive license on OpenAI's models. [[OpenAI]] is now free to distribute through any cloud — [[Andy Jassy]] (Amazon CEO) confirmed [[AWS]] hosting "soon." Microsoft IP rights continue non-exclusively through 2032. Microsoft no longer pays OpenAI a revenue share; OpenAI continues to pay Microsoft 20% revenue share through 2030, capped, independent of OpenAI tech progress (the AGI off-ramp removed). Azure remains the primary launch cloud "unless Microsoft decides otherwise." MSFT was -4% pre-market on the headline, recovered to roughly flat (~-0.4% to -0.7%) by the close as the market parsed that Microsoft kept what mattered (IP, revenue share inbound, ~27% equity, $7.6B Q2 FY26 mark-to-market gain). See [[Microsoft-OpenAI exclusivity end]] for full details. The structural read: [[OpenAI]] is freeing distribution on the cloud side at the same time it is trying to escape platform-owner dependence on the device side via the [[OpenAI hardware program]].

*Source: [Microsoft official blog](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/), CNBC, Reuters, Bloomberg Tech 4/27/26.*

---

## Apr-May 2026 — Musk trial and advisory verdict

The [[Elon Musk]] $134B lawsuit against [[OpenAI]] entered jury selection in Oakland on April 27, 2026. The trial concerns two remaining claims (others dismissed): (1) [[Sam Altman]] and OpenAI violated a promise to Musk that OpenAI would maintain a permanent charitable mission, breached when the 2019 for-profit affiliate was created; (2) Altman/OpenAI received undeserved benefits (Musk's investment) from those broken promises. Witnesses include Altman, Musk, and [[Satya Nadella]].

Procedural detail material to outcome: the jury is advisory only — the judge is not bound by it. Per Professor Lund (Columbia Law School, Bloomberg Tech 4/27/26): the judge will retain discretion regardless of verdict, though a jury verdict provides "cover" for the judge's ruling. Musk has dropped multiple original claims; the case is narrower than initial filings.

The judge has called out Musk's potential motive — operating [[xAI]] as a competing for-profit AI company while suing to retroactively unwind OpenAI's for-profit conversion. SpaceX IPO disclosures explicitly note that [[Grok]] would benefit if the suit succeeds.

On May 18, 2026, the advisory jury rejected Musk's damages case, finding he was not entitled to compensation on the claim that OpenAI, Altman, and other co-founders cheated him out of his founding stake. Reuters and AP framed the result as a win for OpenAI and Altman. Because the jury was advisory, the formal equitable ruling still sits with Judge Yvonne Gonzalez Rogers, but the practical read is that Musk lost the cleanest damages route.

Litigation overhang moves from existential unwind risk toward residual judge-discretion risk. The verdict also weakens the [[xAI]] competitive-leverage angle: Musk still competes with OpenAI commercially, but the lawsuit no longer looks like a near-term path to re-open OpenAI's corporate structure.

*Sources: Bloomberg Tech 4/27/26 (Professor Eric Lund interview); [Reuters via Investing.com, May 18 2026](https://www.investing.com/news/stock-market-news/elon-musk-loses-lawsuit-against-openai-4696614); [AP, May 18 2026](https://apnews.com/article/0b9b0bfaffe96f2c930341f52dfe4f8c).*

---

## Apr 22, 2026 - GPT-5.4-Cyber moves OpenAI deeper into government cyber

OpenAI briefed U.S. federal agencies, state governments, and Five Eyes partners on GPT-5.4-Cyber, a defensive cybersecurity variant of its flagship model. The company is not just shipping a generic model checkpoint. It is building a gated distribution channel for vetted security vendors, researchers, organizations, and now government users.

The readthrough is strategic. OpenAI is moving downstream from general model capability into the security workflow itself, where trust, distribution, and policy controls matter as much as raw model performance. That makes the overlap with [[Anthropic]]'s recent cyber push more direct and pulls OpenAI closer to the control-point layer already pressuring incumbent cyber vendors.

*Source: Reuters, "OpenAI briefs US agencies, Five Eyes on new cybersecurity product, Axios reports" (Apr 22, 2026).*

---

## May 5-7, 2026 — GPT-5.5 Instant launch + $50B compute spend disclosure + AI agent phone fast-track

Three OpenAI updates landed in the same 48-hour window, all reinforcing the [[Project Stargate]] / compute-binding narrative.

### GPT-5.5 Instant launch (May 5-7)

[[ChatGPT]] launched [[GPT-5.5]] Instant as the new default model, replacing [[GPT-5.3]] Instant for all users. Improvements per the OpenAI release: better accuracy, clarity and conciseness across everyday answers, image understanding, STEM questions, and decisions on when to web-search. The model is described as more "factually reliable" with tighter answers, fewer unnecessary follow-up questions, and reduced overformatting / gratuitous emoji output.

Memory upgrade: [[ChatGPT]] Plus and Pro users now get more personalized continuous responses pulling from past chats, saved memories, files, and Gmail context (where connected). Memory sources are now visible across consumer plans for clearer control and edits.

The cleanest read on GPT-5.5 vs prior: [[OpenAI]]'s default-model cadence has accelerated. [[GPT-5.4]] in March, [[GPT-5.4-Cyber]] in April (cybersecurity variant), now [[GPT-5.5]] Instant in May — three default-model updates in three months. This is the clearest competitive response to [[Anthropic]]'s [[Claude Sonnet]] 4.6 (Feb 17) → [[Claude Opus]] 4.7 (April 23) → [[Claude Mythos]] (training, not yet shipped per [[Mythos]] leak section above) sequence. Both labs are now shipping default-model updates roughly monthly — a step-change vs the quarterly cadence of 2024-2025.

### Brockman: $50B compute spend in 2026 (May 5)

[[Greg Brockman]] disclosed that [[OpenAI]] expects to spend $50B on compute in 2026 — up from "roughly $30M in 2017" per his Bloomberg interview. The trajectory:

| Year | Compute spend |
|------|---------------|
| 2017 | ~$30M |
| 2026 | $50B (announced) |

That is a roughly 1,667× increase in nine years — a compounding rate of ~1.5× per year sustained for nine years. The number itself confirms the [[Dylan Patel]] Mar 13 framing of [[OpenAI]] as the compute-aggressive bidder vs [[Anthropic]]'s conservative posture, and it sets a benchmark for the [[Anthropic vs OpenAI compute race]] thread: $50B / year run rate is roughly 5-6 GW of inference capacity at $10-13B per GW per Patel's math, consistent with the H2 2026 OpenAI capacity target.

The disclosure also matters for [[Project Stargate]] tracking: $50B 2026 compute spend is roughly 10% of the announced $500B Stargate JV envelope, implying the Stargate spend is back-loaded to 2027-2028 as the [[Abilene]] / [[New Mexico]] / [[Wisconsin]] sites come online and the [[Lancium]] / [[Crusoe Energy]] partner arrangements scale.

Cross-name reads:
- [[NVIDIA]] — primary supplier of the H100/H200/Blackwell capacity backing the $50B run-rate
- [[Microsoft]] — primary cloud hyperscaler partner (post-exclusivity unwind, see Apr 27 entry)
- [[CoreWeave]] / [[Oracle]] / [[SoftBank]] / [[NScale]] — non-Microsoft compute counterparties from the OpenAI pre-Stargate diversification phase

### AI agent phone fast-tracked for 1H 2027 (May 5)

OpenAI is fast-tracking its first AI-agent phone for mass production in 1H 2027 per [[9to5Mac]] reporting. Stated drivers:
1. Supporting a year-end 2026 IPO narrative (a hardware product gives the IPO story structural depth beyond pure SaaS / API revenue)
2. Intensifying competition in AI-agent phones — [[Apple]]'s [[Siri]]-overhauled iPhone is the primary competitive target, but also [[Google]]'s [[Gemini]]-native Pixel and [[Samsung]]'s [[Galaxy AI]] integration

The phone is the [[Jony Ive]] / [[LoveFrom]] design partnership product. Hardware specifications and pricing are not disclosed; mass production timing is the leak's primary content.

Strategic read: [[OpenAI]] turning into a hardware company changes the competitive map for [[Apple]]. Apple's [[App Store]] / iPhone economics depend on iPhone being the dominant mobile-AI delivery mechanism. An [[OpenAI]] phone with [[Jony Ive]] credibility and direct distribution undermines that. [[Apple]] tipping toward the Apple-relationship-weakening framing already in the OpenAI note (post-Apple-Sora-rumors and post-iOS-26-AI-shortfall) — the [[OpenAI]] hardware push accelerates the divergence.

For the IPO narrative, the hardware timing is well-paced: Q4 2026 IPO + 1H 2027 hardware launch + late-2027 Stargate capacity ramp = three discrete catalysts compounding through the IPO-to-2028 window.

*Sources: [Bloomberg — OpenAI to Spend $50 Billion on Computing in 2026, Brockman Says](https://www.bloomberg.com/news/articles/2026-05-05/openai-to-spend-50-billion-on-computing-in-2026-brockman-says); [9to5Mac — OpenAI's new phone being fast-tracked to launch next year](https://9to5mac.com/2026/05/05/openais-new-phone-being-fast-tracked-to-launch-next-year-per-report/); [OpenAI release notes — May 2026](https://releasebot.io/updates/openai); [CNBC — Trump admin moves further into AI oversight, will test Google, Microsoft and xAI models](https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html).*

### Trump admin AI oversight expansion (May 5)

Same week, the [[Trump administration]] moved further into AI oversight, with [[CAISI]] (the [[Commerce Department]]-housed Center for AI Standards and Innovation) testing [[Google]], [[Microsoft]], and [[xAI]] models. [[OpenAI]] is reportedly already being tested. The framework is voluntary but commercially meaningful: government testing creates a procurement-relevant rating that affects which models can be approved for federal-agency deployment — a material consideration given OpenAI's [[GPT-5.4-Cyber]] / federal-cyber push (Apr 22 entry).

The competitive read: [[Anthropic]] — explicitly safety-coded — should benefit from any framework that rewards alignment / safety scoring on model evals. [[OpenAI]] / [[Google]] / [[Microsoft]] / [[xAI]] are now competing on a measured-safety axis they previously did not have to compete on. See [[CAISI]] for the regulatory framework detail.

---

## May 23, 2026 — accelerated IPO window and runway math

FT's May 23 2026 mega-IPO article says leaks about [[OpenAI]]'s accelerated IPO timetable are now being read by public investors as a signal that the AI labs could follow [[SpaceX]] in short order. The same piece puts the latest private mark at $852B and says OpenAI booked almost $6B of revenue last quarter, driven by [[ChatGPT]] and growing [[Codex]] usage.

The tension is the burn line. FT reports OpenAI has told investors it expects to burn roughly $600B before reaching profitability in 2030, despite already raising more private capital than any start-up in history and closing a $122B 2026 round. That makes the IPO less a celebratory exit than a funding mechanism: public investors are being asked to extend the runway for the [[Project Stargate]] / compute strategy while the company tries to prove that consumer distribution plus coding-agent growth can outrun infrastructure commitments.

Jun. 5 prediction-market refresh: the daily-scan cross-venue divergence was stale-state noise. [[Kalshi]]'s before-Jan. 1 2027 leg printed 75c, while [[Polymarket]]'s direct no-2026 leg printed 28.5c, so both venues still price 2026 as the base case but at a cooler roughly 72-75% range. See [[2026 IPO pipeline]] for the Jun. 5 cross-venue refresh.

*Source: [[Financial Times|FT]] article, May 23 2026: https://www.ft.com/content/ae9bb47d-bd1d-473c-b4c5-abae0420cc12.*

---

## May 26, 2026 — Aurelion valuation critique

[[Aurelion Research]]'s May 26 mega-IPO note is most skeptical on OpenAI because the $852B post-money private mark already capitalizes a very large 2029/2030 revenue outcome while the company still needs outside capital to finance the compute runway. Aurelion's critique is not that OpenAI lacks demand. It is that demand is being converted into an enormous public-market funding ask before investors can see durable margins on owned infrastructure.

![[aurelion-openai-revenue-path-2026.png]]
*Aurelion revenue-path chart for OpenAI. The key source-attributed point is that OpenAI already has massive revenue scale, but the valuation asks buyers to underwrite several more years of growth and infrastructure spend.*

![[aurelion-openai-internal-forecast-2026.png]]
*Aurelion reproduction of an OpenAI forecast path. Treat this as Aurelion's presentation of source/forecast data, not a new company filing.*

![[aurelion-openai-valuation-model-2026.png]]
*Aurelion downside model: if OpenAI ends 2026 around a $20B revenue run rate and trades at 20x revenue, Aurelion's toy valuation lands near $400B. This is an opinionated stress case, not a verified market price.*

The clean read-through is that OpenAI has the broadest distribution and the most visible consumer franchise, but the public-market ask is also the most explicitly financial. Aurelion frames the IPO as a mechanism for funding the [[Project Stargate]] / compute strategy rather than just a liquidity event. That fits the FT burn math: a company can have extraordinary revenue scale and still be structurally dependent on capital markets if the next model cycle requires infrastructure commitments ahead of cash payback.

*Sources: [[Aurelion Research]], "Special Article: SpaceX, OpenAI, and Anthropic IPOs," May 26 2026: https://read.aurelionresearch.com/p/special-article-spacex-openai-and; OpenAI official financing release, Mar. 31 2026: https://openai.com/index/accelerating-the-next-phase-ai/.*

---

## May 12, 2026 — Secondary-market void declaration (parallel to [[Anthropic]])

OpenAI issued a stock-transfer-policy update on May 12, declaring all transfers without written board consent void under Delaware bylaw transfer restrictions. The language was identical to [[Anthropic]]'s May 11 notice (same "void" terminology, same target categories — SPVs, tokenized interests, forward contracts). Source reporting did not enumerate OpenAI's specific named platforms but noted "both companies named the same list of targets" (Yahoo / Bloomberg).

OpenAI's notice statement: *"the sale will not be recognized and carry no economic value to you."* The choice of "void" (not voidable) is the most aggressive Delaware corporate-law stance — it eliminates good-faith-purchaser equitable defenses for downstream tokenized-contract buyers.

Market reaction: tokenized [[OpenAI]] contracts on perp DEXs crashed approximately $1,400 → $900 (-36%) in 24 hours after the announcement — a sharper drawdown than tokenized [[Anthropic]] contracts saw on its May 11 notice. The contrast with OpenAI's October 2025 board-authorized tender offer ($6.6B across 600+ employees) is the structural point: the company has not moved against authorized secondary liquidity, only the unauthorized SPV / tokenized / forward-contract layer that grew up alongside it.

Full structural treatment: [[Private market secondaries#Issuer pushback: the void-declaration mechanism (May 11-12, 2026)]] and [[Tokenized private shares#Issuer pushback: void declarations (May 11-12, 2026)]]. The dated-event hub is [[Anthropic SPV void May 11 2026]] (Events/) — carries the timeline, named-platform list, and the void-vs-voidable mechanics.

*Sources: [Yahoo Finance / Bloomberg — Anthropic and OpenAI warn buyers](https://finance.yahoo.com/markets/stocks/articles/anthropic-openai-warn-buyers-unauthorized-180743368.html); [Spendnode synthesis](https://www.spendnode.io/blog/anthropic-voids-unauthorized-stock-trades-1-6t-tokenized-may-2026/); [TechCrunch](https://techcrunch.com/2026/05/12/anthropic-warns-investors-against-secondary-platforms-offering-access-to-its-shares/) (May 12, 2026, includes OpenAI parallel context).*

---

## Related

- [[ChatGPT]] — consumer/enterprise interface, 75% of revenue
- [[GPT]] — model family
- [[OpenAI GPT-5.4]] — current flagship (standalone benchmark analysis)
- [[Sora]] — video generation
- [[Codex]] — coding agent
- [[Project Stargate]] — $500B infrastructure JV
- [[OpenAI Infrastructure Spend]] — compute strategy analysis
- [[OpenAI talent exodus]] — departure pattern and implications
- [[OpenAI personal agent moat]] — agent platform thesis
- [[Steinberger OpenAI acqui-hire]] — [[Peter Steinberger]]/[[OpenClaw]] acquisition
- [[OpenAI DevDay 2024]] — developer platform event
- [[Sam Altman]] — CEO
- [[Jakub Pachocki]] — Chief Scientist
- [[Chain-of-thought monitoring]] — alignment technique (cross-lab, Pachocki-driven)
- [[FrontierMath]] — research-level math benchmark
- [[Microsoft]] — 27% owner, cloud partner, 20% revenue share through 2032
- [[Amazon]] — $50B investor, [[AWS]] commitment
- [[SoftBank]] — $30B+ investor, Stargate co-owner
- [[NVIDIA]] — $30B investor, compute supplier (with tensions)
- [[HOF Capital]] — portfolio investor / HOF frontier-AI exposure
- [[Cerebras]] — alternative inference compute
- [[Promptfoo]] — AI security testing platform acquired Mar 2026, integrating into Frontier
- [[TBPN]] — tech talk show acquired Apr 2026 (narrative/messaging play)
- [[Anthropic]] — primary competitor, founded by OpenAI defectors
- [[OpenAI hardware program]] — io device + AI agent smartphone (Qualcomm/MediaTek/Luxshare, per Kuo Apr 2026)
- [[Qualcomm]] — chip co-designer (smartphone, joint with MediaTek)
- [[MediaTek]] — chip co-designer (smartphone, joint with Qualcomm)
- [[Luxshare Precision]] — exclusive smartphone assembly partner
- [[Microsoft-OpenAI exclusivity end]] — Apr 27, 2026 partnership reset; cloud distribution opened
- [[Private market secondaries]] — concept hub; May 12 2026 void declaration adds the issuer-pushback mechanism subsection
- [[Tokenized private shares]] — concept hub; tokenized OpenAI contracts crashed $1,400 → $900 on May 12 void notice
- [[Ventuals]] — perp DEX with OpenAI synthetic exposure
- [[PreStocks]] — asset-backed tokenization platform
