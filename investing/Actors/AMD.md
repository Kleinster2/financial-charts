---
aliases: [AMD]
---
#actor #fabless #cpu #gpu #ai

**AMD** — fabless chip designer competing in CPUs (vs Intel) and GPUs/AI (vs NVIDIA).

## Core thesis

AMD has closed the hardware gap with NVIDIA but the [[CUDA moat]] kept them locked out of AI. The NodAI acquisition (late 2023) is their attempt to build software competence. Now has "non-zero chance" of challenging CUDA — up from zero.

---

## Leadership

| Role | Name | Since |
|------|------|-------|
| CEO | **[[Lisa Su]]** | Oct 2014 |
| CFO | Jean Hu | Jan 2023 |
| CTO | Mark Papermaster | 2011 |
| EVP, Computing & Graphics | Rick Bergman | 2020 |
| EVP, Data Center Solutions | Forrest Norrod | 2023 |

Lisa Su is AMD's transformational CEO — took company from near-bankruptcy to $300B+ market cap.

---

## Key strengths

- **CPU leadership**: EPYC server CPUs taking share from Intel
- **Chiplet architecture**: Cost-effective multi-die designs
- **NodAI acquisition**: Reshaping org around software-hardware co-design
- **Underdog positioning**: Lower expectations, cheaper valuation

---

## Manufacturing relationships

| Foundry | Relationship | Status |
|---------|--------------|--------|
| [[TSMC]] | Primary | Capacity constrained, locked out of some 2nm |
| [[Samsung]] | Potential | In talks for 2nm EPYC Venice (Jan 2026 decision) |

AMD is one of the customers forced to [[Samsung]] because [[TSMC]] 2nm locked by [[Apple]]/NVIDIA.

---

## Competitive position

| Market | vs Competitor | Status |
|--------|---------------|--------|
| Server CPU | Intel | Winning — taking share |
| AI/GPU | [[NVIDIA]] | Behind, but software improving |
| Desktop | Intel | Competitive |

---

## Key catalysts

- [ ] NodAI-driven software improvements gain traction
- [ ] ROCm reaches CUDA parity for key workloads
- [ ] Samsung 2nm deal closes (Jan 2026)
- [ ] Hyperscalers adopt AMD AI chips at scale

---

## Key risks

- CUDA moat holds — software gap doesn't close
- **NVIDIA infrastructure expansion** — SLURM acquisition (Dec 2025) adds another layer AMD users depend on
- Samsung yields disappoint — supply/cost disadvantage
- NVIDIA extends hardware lead (Blackwell, etc.)
- Intel recovers in server CPUs

---

## Financials

### Annual (10 years)

| Year | Revenue | Net Income | EPS | Stock Price |
|------|---------|------------|-----|-------------|
| 2016 | $4.3B | -$0.5B | -$0.55 | $11 |
| 2017 | $5.3B | -$0.03B | -$0.04 | $10 |
| 2018 | $6.5B | $0.3B | $0.32 | $18 |
| 2019 | $6.7B | $0.3B | $0.30 | $46 |
| 2020 | $9.8B | $2.5B | $2.06 | $92 |
| 2021 | $16.4B | $3.2B | $2.57 | $144 |
| 2022 | $23.6B | $1.3B | $0.84 | $65 |
| 2023 | $22.7B | $0.9B | $0.53 | $148 |
| 2024 | $25.8B | $1.6B | $1.01 | $119 |
| 2025E | $32.0B | $3.3B | $2.03 | $125 |

*Source: Company filings. Stock price = year-end close. Lisa Su turnaround era began 2014. 2022-23 dip from PC market normalization.*

---

## CES 2026 — Helios AI Rack

**Lisa Su: "World's best AI rack"** — direct shot at NVIDIA.

| Spec | Value |
|------|-------|
| **FP4 performance** | 2.9 exaFLOPS |
| **FP8 training** | 1.4 exaFLOPS |
| **GPUs per rack** | 72x Instinct MI455X |
| **CPUs per rack** | 18x EPYC Venice (Zen 6, 2nm) |
| **HBM4 memory** | 31TB total |
| **Bandwidth** | 1.4 PB/s aggregate |
| **Weight** | 7,000 lbs (double-wide rack) |
| **Launch** | H2 2026 |

**Architecture:**
- Built on Meta's 2025 OCP (Open Compute Project) design
- 18 compute trays, each with 4 MI455X + 1 Venice CPU
- Liquid cooled throughout
- AMD Pensando "Vulcano" NICs for networking
- ROCm software ecosystem

**Venice CPU (Zen 6):**
- 2nm process
- Up to 256 cores
- 2x memory/GPU bandwidth vs prior gen

**Competition:** Goes head-to-head with NVIDIA NVL72 (72 Rubin GPUs).

See [[CES 2026]] for event context.

---

## Q4 2025 earnings (Feb 3, 2026)

**Record quarter — beat expectations but guidance disappointed:**

| Metric | Actual | Expected |
|--------|--------|----------|
| Q4 Revenue | **$10.3B** (record) | $9.7B |
| Q4 EPS (GAAP) | $0.92 | — |
| Q4 EPS (Non-GAAP) | **$1.53** (record) | $1.24 |
| Data Center | $5.4B (+39% YoY) | — |
| FY 2025 Revenue | **$34.6B** (record) | — |
| FY 2025 EPS | $2.65 | — |
| Q1 2026 Guidance | $9.8B ± $300M | ~$10.0B |

**Beat and sell-off:** Stock fell 17% — worst day since 2017 despite beating. Q1 guidance disappointed bulls expecting stronger AI acceleration.

**Data center strength:** +39% YoY driven by EPYC CPUs and Instinct AI GPUs. But $390M from non-recurring China GPU sales inflated the Q4 beat.

**Lisa Su:** "2025 was a defining year for AMD, with record revenue and earnings driven by strong execution and broad-based demand for our high-performance and AI platforms."

**China exposure:** Q1 guidance includes ~$100M from Instinct MI308 sales to China — unclear regulatory runway.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | AMD (NASDAQ) |
| Market cap | ~$290B |
| Revenue (FY 2025) | **$34.6B** |
| Revenue (2026E) | ~$45B |
| EPS (FY 2025) | $2.65 |
| EPS (2026E) | ~$6.50 |
| Data Center (Q4) | $5.4B (+39% YoY) |
| Primary foundry | [[TSMC]] |
| Potential foundry | [[Samsung]] (2nm EPYC) |
| Key acquisition | NodAI (late 2023) |
| CES 2026 | Helios rack (2.9 exaFLOPS) |

*Updated 2026-02-06 — Q4 2025 earnings*

![[amd-price-chart.png]]
*AMD price history*

![[amd-fundamentals.png]]
*AMD revenue and net income. Chart starts 2018 ([[Lisa Su]] turnaround era). Q1 2023 net income excluded (small loss distorts scale).*

---

## Market expectations

**Priced in:**
- CPU gains vs Intel continue
- AI remains NVIDIA-dominated
- TSMC remains primary foundry

**Not priced in (potential surprises):**
- Software closes gap → AI share gains
- Samsung deal + good yields → cost advantage
- Hyperscaler adoption accelerates

---

## For theses

- [[Short TSMC long Korea]] — potential Samsung 2nm customer, validates Korea demand
- [[Long TSMC]] — if AMD stays TSMC, reinforces moat; if leaves, tests it

---

## February 2026: TCS Helios partnership (India)

At the [[India AI Impact Summit 2026]] (Feb 16–20), [[AMD]] announced a partnership with [[TCS]] to develop rack-scale AI infrastructure on AMD's "Helios" platform — extending the [[CES 2026]] Helios unveil into [[India]]'s enterprise market.

| Detail | Value |
|--------|-------|
| Partner | [[TCS]] |
| Platform | Helios (rack-scale AI) |
| Market | [[India]] enterprise |

---

## Related

- [[Lisa Su]] — CEO
- [[NVIDIA]] — competitor (GPU/AI, NVL72 vs Helios)
- [[Intel]] — competitor (CPU)
- [[CUDA moat]] — competitive barrier in AI
- [[Samsung]] — potential 2nm foundry
- [[TSMC]] — primary foundry
- [[Foundry Wars]] — manufacturing context
- [[Leading edge race]] — node competition
- [[CES 2026]] — Helios unveil, Lisa Su keynote
- [[Lenovo]] — partner (Tech World @ CES)
- [[Meta]] — Helios built on Meta OCP design
- [[TCS]] — Helios rack-scale AI partnership (India)
- [[India AI Impact Summit 2026]] — TCS partnership announcement
