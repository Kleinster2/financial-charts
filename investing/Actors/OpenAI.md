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
| Valuation | $730B pre-money, ~$840B post-money (Feb 2026 round) |
| Revenue (2025) | ~$13.1B recognized; $20B exit-rate ARR |
| Revenue (2024) | ~$3.7B recognized; $5.5B exit-rate ARR |
| H1 2025 net loss | $13.5B (incl. R&D $6.7B, S&M $2B) |
| Gross margin | 33% (2025), down from 40% (2024) |
| Inference costs (2025) | $8.4B; projected $14.1B (2026) |
| ChatGPT WAU | 800M-900M (Mar 2026) |
| Paid subscribers | ~35M (Plus/Pro/Team/Enterprise) |
| Enterprise/Team/Edu users | ~9M business users |
| Business clients | ~1.5M |
| Consumer market share | 64.5% of generative AI platforms |
| Total funding raised | ~$168B across 11 rounds |
| Employees | ~3,500 (est.) |
| CEO | [[Sam Altman]] |
| COO | Brad Lightcap |
| CTO | Vacant (since [[Mira Murati]] departure Sep 2024) |
| Board chair | [[Bret Taylor]] |
| Founded | December 2015, San Francisco |
| HQ | San Francisco |

---

## Synopsis

OpenAI is the most heavily funded private company in history and the dominant consumer AI platform, but its financial profile looks more like a hyperscaler buildout than a software company. The $20B ARR headline masks a cost structure growing faster than revenue: inference costs alone hit $8.4B in 2025 and are projected at $14.1B for 2026, compressing gross margins to 33%. The company projects massive losses through 2028 and doesn't expect cash-flow positivity until 2029-2030. The $110B mega-round (Feb 2026) — [[Amazon]] $50B, [[SoftBank]] $30B, [[NVIDIA]] $30B — buys time but creates obligations: $100B in AWS spend over 8 years, 2 GW of Amazon Trainium compute, and an implicit IPO path (Amazon's $35B tranche terminates if no IPO/listing by Dec 2028).

The competitive picture is more nuanced than the user numbers suggest. [[Anthropic]]'s Claude is gaining enterprise share rapidly — overtaking OpenAI in enterprise preference surveys (Jul 2025) while growing from $900M to $14B ARR in the same period OpenAI went from $6B to $20B. Google Gemini replaced ChatGPT as Apple's default AI provider (Jan 2026). The talent exodus — [[Ilya Sutskever]] (SSI, $32B), [[Mira Murati]] (Thinking Machines Lab, $12B), [[John Schulman]] (Anthropic), 7+ researchers to [[Meta]]'s Superintelligence Lab — has stripped the safety and research bench. The Mission Alignment team was disbanded in Feb 2026. Elon Musk's $134B lawsuit goes to jury trial in April 2026.

The strategic bet is infrastructure + distribution: $600B in compute spend by 2030 via [[Project Stargate]] (7 GW planned capacity, $500B commitment), a Cerebras deal ($10B+ for inference diversification), and the personal agent platform play (Codex relaunch, [[Peter Steinberger]] acqui-hire). If OpenAI can convert its 900M user base into a durable platform — where agents, not just models, are the product — the current losses are a land grab. If the models commoditize faster than the platform locks in, the $840B valuation becomes the most expensive AI bet in history.

---

## Evolution

The story of OpenAI is the story of a nonprofit research lab that accidentally created a consumer product so powerful it had to become a $840B for-profit company to fund its own ambitions — and whether the resulting entity can outrun the costs of staying at the frontier.

- 2015-2018 (the nonprofit era): Founded in December 2015 with $1B in pledges from [[Sam Altman]], [[Elon Musk]], [[Peter Thiel]], [[Reid Hoffman]], [[Jessica Livingston]], and others. The stated mission: ensure AGI benefits all of humanity. Musk was co-chair alongside Altman. [[Ilya Sutskever]] — recruited from [[Google Brain]] — became chief scientist. [[Greg Brockman]] (ex-CTO of [[Stripe]]) became CTO and later president. The early team published foundational work but had trouble retaining talent against Google and Facebook's compensation. Musk left the board in February 2018, later claiming he departed over disagreements about the organization's direction (and his simultaneous involvement with [[Tesla]] AI). With Musk gone, Altman's influence consolidated.

- 2019 (the turn): In March 2019, OpenAI created a "capped-profit" subsidiary — OpenAI LP — where investors could earn up to 100x returns, with excess flowing to the nonprofit parent. The rationale was straightforward: competing at the frontier required billions, and the nonprofit couldn't raise them. [[Microsoft]] invested $1B and became the exclusive cloud partner. GPT-2 was published in February 2019 with a staged release, OpenAI withholding the full model over misuse concerns — the last time the organization's safety instincts would lead its commercial instincts. The capped-profit structure was a compromise: enough capitalism to fund the mission, enough mission to justify the structure. It satisfied nobody fully, and it wouldn't survive contact with real money.

- 2020-2022 (GPT-3 and the platform): GPT-3 launched in June 2020 with 175B parameters — 100x GPT-2 — and proved that scaling laws worked. The API opened to developers, creating the foundation for every AI startup that followed. DALL-E (Jan 2021) and DALL-E 2 (Apr 2022) demonstrated multimodal capabilities. Revenue was still negligible. Microsoft deepened its investment, eventually committing ~$13B cumulative. Meanwhile, tensions over safety and commercialization drove Dario Amodei, Daniela Amodei, and five other senior researchers to leave in early 2021, founding [[Anthropic]] — taking OpenAI's scaling playbook and safety expertise with them. This was the most consequential departure in AI history: it created OpenAI's only credible frontier competitor.

- 2022-2023 (ChatGPT changes everything): ChatGPT launched November 30, 2022, built on GPT-3.5. It reached 100M users in two months — the fastest consumer product adoption in history. What had been a research lab became a consumer platform overnight. GPT-4 followed in March 2023, demonstrating multimodal reasoning that approached human-level on standardized tests. Revenue jumped from near-zero to ~$2B annualized. The January 2023 Microsoft mega-round (~$10B, $29B valuation) gave OpenAI the war chest, and Microsoft embedded GPT into [[Copilot]] across Office, Azure, and Bing. The symbiosis looked perfect: Microsoft got the frontier model, OpenAI got the distribution and compute. But the relationship was already asymmetric — Microsoft was building its own AI capabilities while paying for OpenAI's.

- November 2023 (the board crisis): On November 17, the OpenAI board fired Sam Altman, stating he was "not consistently candid in his communications." The board — including [[Ilya Sutskever]], who had voted for removal — offered no public explanation. Microsoft CEO [[Satya Nadella]] immediately offered Altman a role. Within 72 hours, 700+ of ~770 employees signed a letter threatening to resign and join Microsoft unless Altman was reinstated. Altman returned on November 22. The board was reconstituted with [[Bret Taylor]] as chair, adding [[Larry Summers]] and corporate governance veterans. Sutskever — who had reversed his position during the crisis — remained briefly, then departed in May 2024 to found [[SSI]] (Safe Superintelligence Inc., raised $2B at $32B valuation by March 2025). The lesson: Altman is OpenAI. The nonprofit governance structure that was supposed to prioritize safety over commerce had been stress-tested and failed — the employees chose Altman over the board, and the board folded.

- 2024 (scaling the platform): Revenue surged from ~$2B to $5.5B exit-rate ARR. GPT-4o launched (May), then o1 reasoning models (September). ChatGPT hit 300M WAU by December. The October 2024 round ($6.6B at $157B valuation) brought in [[Thrive Capital]], NVIDIA, and Microsoft. Enterprise adoption accelerated: DevDay 2024 delivered GPT-4 Turbo (128K context, 3x cheaper), custom GPTs, the GPT Store, and the Assistants API. But the talent bleeding continued: [[Mira Murati]] (CTO) departed in September, founding Thinking Machines Lab ($12B valuation by Feb 2025). [[John Schulman]] (co-founder) left for [[Anthropic]]. [[Andrej Karpathy]] departed. The pattern was unmistakable: OpenAI's safety and research leaders were leaving, and the replacements were commercial operators.

- 2025 (for-profit conversion and the infrastructure bet): The year of structural transformation. Revenue hockey-sticked to $20B ARR — the first $1B revenue month came in July 2025. GPT-5 launched August 7, incorporating the o-series reasoning models as "thinking mode." The March 2025 SoftBank-led round ($40B at $300B) included a clawback: SoftBank could reduce its commitment to $20B if the for-profit restructuring wasn't completed by year-end. On October 28, OpenAI converted from capped-profit to a public benefit corporation. The nonprofit became the OpenAI Foundation, retaining ~26% ownership and the right to appoint all board directors. Microsoft's stake was restructured from 49% capped-profit share to ~27% equity, with exclusivity extending through 2032. The conversion unlocked the mega-round but also exposed the mission tension: [[Larry Summers]] resigned from the board in November 2025 after House panel emails linked him to Jeffrey Epstein. The io acquisition ($6.4B, May 2025) — buying [[Jony Ive]]'s hardware startup — signaled ambitions beyond software. And OpenAI announced $600B in own compute spend by 2030, with the [[Project Stargate]] JV ($500B commitment) as the centerpiece.

- Jan-Feb 2026 (the mega-round and its obligations): The $110B round closed February 27, 2026 — the largest private financing in history. [[Amazon]] committed $50B ($15B immediate in Series C preferred, $35B conditional on milestones including IPO/listing, terminates Dec 2028 if uninvested). [[SoftBank]] and [[NVIDIA]] each committed $30B. In exchange, OpenAI committed to $100B in AWS spending over 8 years and 2 GW of Amazon Trainium compute. NVIDIA's participation came with friction: Reuters reported (Feb 2) that OpenAI was dissatisfied with NVIDIA chips for inference workloads, targeting ~10% of inference from alternatives. The $10B+ Cerebras deal (2026-2028, 750 MW, inference-focused) formalized the diversification. GPT-5.4 launched March 5 with agentic capabilities. The Stargate Abilene expansion (1.2 GW to 2 GW) was cancelled March 6, though the core 4.5 GW Oracle contract remained intact. The Mission Alignment team was disbanded in February; its leader Joshua Achiam was moved to a "chief futurist" role.

- March 2026 (current state): The paradox is sharp. OpenAI has the most users (900M+), the most capital ($168B raised), and the highest valuation ($840B) of any private company ever. But it also has no CTO, no chief scientist, a disbanded safety team, co-founders scattered across competitors (Sutskever at SSI, Schulman at Anthropic, Brockman on indefinite sabbatical), gross margins compressing, losses deepening, and a $134B Musk lawsuit heading to jury trial in April. The bet is that scale — user scale, compute scale, capital scale — creates a moat before the models commoditize. The risk is that it doesn't, and OpenAI becomes the most expensive proof that distribution without differentiation is a losing position.

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

### Consumer and enterprise

- [[ChatGPT]] — consumer/enterprise interface (Free/$8 Go/$20 Plus/$200 Pro/Team/Enterprise/Edu)
- Codex — coding agent (GPT-5.2-Codex), MacOS app launched Feb 2026, repo-scale reasoning
- [[Sora]] — video generation (Sora 2/Sora 2 Pro with improved temporal coherence)
- Deep Research — o3-powered comprehensive web research agent (launched Feb 2, 2025)
- Whisper — speech-to-text
- AgentKit — SDK for building/deploying AI agents (announced Oct 2025 Dev Day)
- Realtime API — low-latency bidirectional audio streaming (GA)

### Hardware

- Acquired [[Jony Ive]]'s startup "io" for $6.4B (May 2025). First hardware prototypes completed Nov 2025: pocket-sized, screenless, audio-based device with cameras/microphones. Target launch late 2026 or early 2027.

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
| Oct 2025 | Employee secondary | ~$6.6B | $500B | SoftBank, Thrive, [[Dragoneer]], [[MGX]], T. Rowe Price |
| Feb 27, 2026 | Mega-round | $110B | $730B pre / ~$840B post | [[Amazon]] ($50B), [[SoftBank]] ($30B), [[NVIDIA]] ($30B) |

Total raised: ~$168B across 11 rounds from 67 investors.

### Amazon $50B structure

$15B in Series C preferred stock (due Mar 31, 2026). Remaining $35B conditional on milestones including IPO or direct listing — terminates if not invested by Dec 31, 2028. OpenAI committed to $100B AWS spend over 8 years and 2 GW of [[Amazon]] Trainium compute. AWS becomes exclusive cloud distributor for Frontier enterprise platform (alongside Azure for APIs).

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
| President | [[Greg Brockman]] (co-founder; extended sabbatical since late 2024) |
| COO | Brad Lightcap |
| CTO of Applications | Vijaye Raji (joined via Statsig acquisition) |
| Board chair | [[Bret Taylor]] |
| CTO | Vacant since Sep 2024 |
| Chief Scientist | Vacant since May 2024 |

### Board (post-restructuring)

[[Bret Taylor]] (chair), [[Adam D'Angelo]], Dr. Sue Desmond-Hellmann (fmr CEO Gates Foundation), Dr. Zico Kolter, Gen. Paul Nakasone (ret., fmr NSA/CYBERCOM), Adebayo Ogunlesi, Nicole Seligman (fmr EVP/GC Sony), [[Sam Altman]]. [[Larry Summers]] resigned Nov 2025 after House panel Jeffrey Epstein emails.

### Key departures

| Person | Departed | Went to | Valuation |
|--------|----------|---------|-----------|
| [[Ilya Sutskever]] | May 2024 | [[SSI]] (founder) | $32B |
| [[Mira Murati]] | Sep 2024 | Thinking Machines Lab (founder) | $12B |
| [[John Schulman]] | Aug 2024 | [[Anthropic]] | — |
| [[Jan Leike]] | May 2024 | [[Anthropic]] | — |
| [[Andrej Karpathy]] | 2024 | Independent (education) | — |
| [[Caitlin Kalinowski]] | Mar 2026 | — (resigned over Pentagon deal) | — |
| 7+ researchers | Summer 2025 | [[Meta]] Superintelligence Lab | — |

Jan Leike on departure: "Safety has taken a backseat to shiny products." Mission Alignment team disbanded Feb 2026; leader Joshua Achiam moved to "chief futurist" role.

---

## Infrastructure

### [[Project Stargate]]

$500B JV with [[SoftBank]] (40% ownership, financial lead), OpenAI (40%, operational lead), [[Oracle]] ($7B), [[MGX]] ($7B). Targeting 10 GW US AI infrastructure by 2029.

| Site | Capacity | Status |
|------|----------|--------|
| Abilene, TX | Core facility | Operational; 2 GW expansion cancelled Mar 6, 2026 |
| Shackelford County, TX | Planned | Announced Sep 2025 |
| Dona Ana County, NM | Planned | Announced Sep 2025 |
| Lordstown, OH | Under construction | Expected operational 2026 |
| Milam County, TX | Planned | Announced Sep 2025 |
| Stargate UAE | 1 GW (200MW by YE2026) | Partnership with [[G42]], Oracle, SoftBank, NVIDIA |
| Norway | 230 MW | Hydropower |
| Argentina | 500 MW by 2027 | $25B, Patagonia |

Oracle partnership alone: $300B over 5 years for 4.5 GW capacity.

### Compute diversification

- [[Cerebras]] deal: $10B+, 2026-2028, 750 MW, inference-focused. 15x faster responses than GPU-based for specific workloads. Altman was early Cerebras investor.
- NVIDIA friction: Reuters (Feb 2, 2026) reported OpenAI dissatisfied with NVIDIA chips for inference. Target: ~10% of inference from alternatives. Affected products: Codex, agent-to-agent communication.
- OpenAI's own compute spend target: ~$600B by 2030 (revised from $1.4T total partner commitments).

---

## Competitive positioning

| Company | Est. ARR (early 2026) | Funding | Key differentiator |
|---------|----------------------|---------|-------------------|
| OpenAI | $20B+ | ~$168B | Consumer scale, distribution, brand |
| [[Anthropic]] | $14B | ~$57B | Enterprise trust, safety-first, capital efficiency |
| [[Google]] DeepMind | Not reported separately | Google internal | Workspace/Cloud distribution, Gemini |
| [[xAI]] | Not reported | ~$12B | Speed, real-time search, X distribution |
| [[Meta]] AI | Not reported | Internal | Open-source Llama, Superintelligence Lab |

Enterprise market share (Ramp data): OpenAI 36-42%, [[Anthropic]] 12-22% and accelerating. Anthropic overtook OpenAI in enterprise preference surveys (Jul 2025, TechCrunch).

### Apple relationship weakening

ChatGPT was integrated into Siri/iOS in 2024-2025 (no cash exchanged — Apple viewed distribution as compensation). In January 2026, [[Apple]] announced [[Google]] Gemini will power Apple Intelligence and new Siri, displacing ChatGPT as the default.

---

## Key risks

### Financial
- Losses deepening: $13.5B net loss in H1 2025 alone
- Inference costs growing faster than revenue (quadrupled in 2025)
- Gross margin compression: 40% to 33%
- No profitability until 2029-2030 at earliest
- $100B AWS spend commitment over 8 years

### Competitive
- [[Anthropic]] gaining enterprise share with 14x less cash burn
- [[Google]] Gemini displacing ChatGPT in Apple ecosystem
- [[Meta]] poaching research talent aggressively
- Model capability convergence reducing differentiation
- Claude Code at $2.5B ARR vs OpenAI's Codex playing catch-up

### Legal
- [[Elon Musk]] lawsuit: $134B damages claim, jury trial April 2026 (Oakland). Judge denied preliminary injunction but case proceeds.
- 50+ copyright lawsuits consolidated in SDNY (before Judge Stein)
- GEMA v. OpenAI: German court ruled training on copyrighted data without license violates German copyright law (appeal expected 2026)

### Talent and governance
- No CTO since Sep 2024, no chief scientist since May 2024
- Co-founders scattered: Sutskever (SSI), Schulman (Anthropic), Brockman (sabbatical)
- Mission Alignment team disbanded Feb 2026
- Microsoft 20% revenue share through 2032 is a perpetual margin drag
- Altman reportedly not taking equity — incentive alignment question

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
- [[Microsoft]] — 27% owner, cloud partner, 20% revenue share through 2032
- [[Amazon]] — $50B investor, AWS commitment
- [[SoftBank]] — $30B+ investor, Stargate co-owner
- [[NVIDIA]] — $30B investor, compute supplier (with tensions)
- [[Cerebras]] — alternative inference compute
- [[Anthropic]] — primary competitor, founded by OpenAI defectors
