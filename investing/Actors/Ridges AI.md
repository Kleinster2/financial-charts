---
aliases:
  - Ridges
  - SN62
  - Subnet 62
  - ridges_ai
tags:
  - actor
  - ai
  - coding
  - private
  - crypto
  - decentralized
---

#actor #ai #coding #crypto #usa #private

**Ridges AI** — Decentralized AI software engineer running as Subnet 62 on [[Bittensor]]. Aims to replace human coders end-to-end. Founded by [[Shakeel Hussein]] ("Shak"). V1 product shipped Oct 30, 2025 as an IDE extension priced around $12/month — roughly 1/50 to 1/250 the cost of centralized competitors like [[Claude Code]] and [[Cursor]]. Direct analog to [[Cognition]]'s Devin, but built as a decentralized incentive game rather than a centralized company.

Ridges is the first Bittensor subnet to put the "competitive markets for AI" thesis under a visible benchmark (SWE-Bench) with a visible price tag. Subnet miners submit autonomous coding agents; validators score them on real GitHub issues; winners are paid in TAO and SN62 alpha. The incentive structure collapses the cost curve — miners have no salary line and their winning agents are open-sourced, so the frontier compounds across a rolling set of anonymous contributors rather than inside a single lab.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Product | AI software engineer (IDE extension + CLI) |
| Bittensor subnet | 62 (SN62) |
| Subnet registered | Early 2025 |
| V1 product shipped | Oct 30, 2025 |
| CEO | [[Shakeel Hussein]] ("Shak") |
| Alpha token market cap | ~$45M (April 2026) |
| Rank among ~128 subnets | Top 15; 3rd by value at peak |
| Miner cap | 256 per subnet |
| Consumer price | ~$12/mo base, ~$8/mo with opt-in data sharing |
| GitHub | [github.com/ridgesai/ridges](https://github.com/ridgesai/ridges) |
| Website | [ridges.ai](https://www.ridges.ai/) |

---

## Leadership

| Name | Role | Notes |
|------|------|-------|
| [[Shakeel Hussein]] | CEO / founder | Public face of the subnet; frequent podcast / AMA presence |

Ridges runs lean — most of the "headcount" is the 256 competitive miners, who are not employees. The core team focuses on validator infrastructure, the Cerebro reward model, and the IDE extension.

---

## How it works

Ridges is not a single model — it is a competitive market where up to 256 miners submit autonomous coding agents and validators score them on real-world benchmark tasks.

| Component | Function |
|-----------|----------|
| Validators | Generate coding challenges from top PyPI packages and real [[GitHub]] issues; score miner submissions |
| Miners | Submit complete agent solutions (code + reasoning pipelines); winners paid in TAO and SN62 alpha |
| Cerebro | Ridges' task-difficulty classifier and reward-model supervisor |
| Problem Routing Protocol | Routes incoming user tasks to the best-performing agent for each task type |
| Open-source winners | Top solutions are open-sourced, so each generation inherits the prior frontier |

Economically, the subnet functions as a bounty program: TAO emissions and SN62 alpha emissions fund the prize pool, and the best agent in any given period wins most of it. Cost compression comes from miners having no salary line — they are paid only if they win.

Model-agnostic: Ridges agents can be built on any LLM ([[GPT]], [[Claude]], [[DeepSeek]], [[Qwen]]). Competitive pressure pushes miners toward cheaper models wrapped in thicker agent scaffolding — the opposite of the frontier-model-centric approach of [[Cursor]] or [[Claude Code]].

---

## SWE-Bench performance

| Period | Benchmark | Score |
|--------|-----------|-------|
| ~45 days after launch | [[SWE-Bench]] Verified | 80% |
| Peak (pre-Polyglot) | SWE-Bench Verified | 88% |
| Post-Polyglot mixed set | SWE-Bench + Polyglot | 17-18% (initial drop) |
| October 6, 2025 | SWE-Bench + Polyglot | ~41% |

Reached competitive SWE-Bench Verified scores with under $1M total paid to miners — an efficiency claim that, if durable, is the core economic argument for Bittensor-style competitive markets over single-lab R&D.

Polyglot addition (non-Python languages) exposed how narrowly miners had optimized for the Python benchmark. Score recovery from 17% → 41% over weeks demonstrates iteration speed of the competitive market — losing solutions are open-sourced, winning solutions build on them.

---

## Funding history

Ridges has raised capital both via traditional equity rounds and via SN62 alpha-token emissions — an unusual hybrid pattern now common among revenue-generating Bittensor subnets. Known equity investors:

| Round | Investor | Amount | Notes |
|-------|----------|--------|-------|
| Seed / angel | [[DSV Fund]] | $300K | Crypto-AI focus |
| Seed / angel | [[Stillcore Capital]] | Undisclosed | Crypto-native fund |

The bulk of operating capital effectively comes from SN62 alpha-token appreciation — at roughly $45M market cap, the subnet itself is the fundraising vehicle. This is a material structural difference vs [[Cursor]] (multi-billion equity rounds) and [[Cognition]] (Series C/D ladder).

---

## Competitive landscape

| Competitor | Approach | Price | SWE-Bench |
|------------|----------|-------|-----------|
| [[Cursor]] ([[Anysphere]]) | Centralized IDE | $20/mo, $200/mo enterprise | ~70% via [[Anthropic]]/[[OpenAI]] models |
| [[Claude Code]] | [[Anthropic]] agent | $20/mo (Pro), $200/mo (Max) | 70-77% |
| [[Cognition]] (Devin) | Centralized autonomous agent | $500/mo enterprise | ~15% at launch; higher now |
| [[GitHub Copilot]] | Embedded assistant | $10-39/mo | — |
| Ridges AI | Decentralized competitive market | ~$12/mo | 41% Polyglot, 88% SWE-Bench-only |

Ridges' positioning is not "best agent" — it is "cheapest viable autonomous agent." A Bittensor subnet can undercut centralized peers because miners subsidize compute with TAO rewards, there is no single-company margin layer, and model-agnosticism lets the market route tasks to whichever model is cheapest per solved task.

If the pricing holds, Ridges is a direct cost-disruption threat to [[Cursor]]'s $29.3B valuation and to [[Cognition]]'s $10.2B enterprise story. Constraint: enterprise buyers need latency, reproducibility, and security review for production coding — decentralized inference touching proprietary source trees and CI pipelines is a harder sell than consumer developer tools.

---

## Evolution

| Date | Milestone |
|------|-----------|
| Early 2025 | SN62 registered on [[Bittensor]] |
| ~March 2025 | Miners reach 80% SWE-Bench Verified within 45 days of launch |
| Mid-2025 | Peak 88% SWE-Bench Verified (pre-Polyglot) |
| Q3 2025 | Polyglot benchmark added; mixed-set scores drop to 17-18% |
| Oct 6, 2025 | Mixed-set score rebounds to ~41% |
| Oct 30, 2025 | V1 consumer product ships as IDE extension, ~$12/mo |
| April 2026 | SN62 alpha token ~$45M market cap, top 15 Bittensor subnet |

---

## Strategic framing

Ridges is the most concrete test of whether [[Bittensor]]'s "intelligence markets" thesis produces commercially competitive output. Holding ~40-50% SWE-Bench Verified at 1/250 the cost of frontier labs would shift the argument for decentralized AI from crypto-speculative to infrastructure-real. Two load-bearing assumptions:

1. Miner open-sourcing genuinely compounds — each generation inherits the prior frontier rather than cannibalizing prize pools.
2. Enterprise buyers accept decentralized inference for coding workloads.

Counter-example: [[Cursor]] scaled to $1B ARR on the opposite bet — that developers would pay a premium for a polished, centrally-controlled product running the best frontier models. Enterprise has mostly validated that bet. Ridges has to prove the cost gap is large enough to pull workloads from the incumbent, not just win on price for hobbyists.

One-line: a live public experiment in whether [[Crypto-to-AI pivot]] produces real software or just cheaper benchmarks.

---

## Related

- [[Bittensor]] — parent protocol
- [[SWE-Bench]] — primary benchmark
- [[Shakeel Hussein]] — founder / CEO
- [[Cognition]] — direct competitor (centralized)
- [[Cursor]] — IDE-competitor
- [[Claude Code]] — incumbent agent
- [[GitHub Copilot]] — embedded-assistant competitor
- [[AI agents]] — parent concept
- [[Agentic AI]] — capability layer
- [[Vibe coding]] — adjacent workflow concept
- [[Crypto-to-AI pivot]] — broader thematic context
- [[Crypto]] — category
