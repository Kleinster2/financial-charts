---
aliases: [AIWD, SaaSpocalypse basket, SaaS Apocalypse basket]
tags: [concept, index, custom, ai, disruption]
---

# AI workflow disruption basket

Stocks that correlate on AI capability announcements threatening white-collar workflows. Emerged as a distinct factor during the [[Claude Cowork disruption February 2026|February 2026 SaaSpocalypse]].

Wall Street now calls this phenomenon the **"SaaSpocalypse"** — the thesis that AI agents fundamentally break seat-based SaaS pricing. If one agent does the work of ten humans, why pay for ten seats? ~$285B in market cap erased Feb 3-4, 2026. We had the basket before it had a name.

---

## Constituents

*Rebalanced Feb 7, 2026: Move-weighted methodology. Weights derived from Feb 3-4 "SaaSpocalypse" selloff — bigger drop = higher weight. Market-revealed disruption exposure.*

### SaaS Platforms — hardest hit (43%)

| Ticker | Company | Weight | Feb Move |
|--------|---------|--------|----------|
| INTU | [[Intuit]] | 16% | -34% |
| NOW | [[ServiceNow]] | 14% | -28% |
| CRM | [[Salesforce]] | 13% | -26% |

### Legal & Data Analytics (51%)

| Ticker | Company | Weight | Feb Move |
|--------|---------|--------|----------|
| LZ | [[LegalZoom]] | 10% | -20% |
| TRI | [[Thomson Reuters]] | 9% | -18% |
| RELX | [[RELX]] | 6% | -14% |
| WKL.AS | [[Wolters Kluwer]] | 6% | -13% |
| LSEG.L | [[LSEG]] | 6% | -13% |
| TEAM | [[Atlassian]] | 5% | -12% |
| FDS | [[FactSet]] | 5% | -10.5% |
| MORN | [[Morningstar]] | 4% | -9% |

### Advertising (6%)

| Ticker | Company | Weight | Feb Move |
|--------|---------|--------|----------|
| OMC | [[Omnicom]] | 6% | -11% |

**Total: 100%** — 12 constituents, move-weighted

### Removed: Indian IT Services

| Ticker | Company | Feb Move | Why removed |
|--------|---------|----------|-------------|
| INFY | [[Infosys]] | -7.4% | Different thesis |
| TCS.NS | [[TCS]] | -7% | Different thesis |

**Rationale:** Indian IT is exposed to AI margin compression (billable hours → AI workflows), not product replacement (seats → agents). The -7% move vs -34% for SaaS shows the market sees them as less directly exposed. They may recover faster if Cowork fears fade. See [[Indian IT services]] for the separate thesis.

### Database tickers

```
INTU, NOW, CRM, LZ, TRI, RELX, WKL.AS, LSEG.L, TEAM, FDS, MORN, OMC
```

---

## Index methodology

- **Ticker:** AIWD
- **Weighting:** Move-weighted (Feb 3-4 selloff magnitude = weight)
- **Rebalance:** Event-driven (re-weight on next major AI disruption catalyst)
- **Base date:** Feb 3, 2026 = 100
- **History:** July 2021 – present (limited by LZ IPO)
- **Calculation:** Price return, USD-adjusted for non-US tickers
- **Script:** `scripts/create_aiwd_index.py --store`

**Rationale:** Let the market tell us disruption exposure. Intuit fell 34% vs TCS 7% — the market is pricing Intuit as 5x more exposed to AI workflow disruption. We follow the signal.

![[aiwd-index.png]]
*AIWD basket since July 2021 (LZ IPO). Peaked late 2021, ground down through 2022-24, then SaaSpocalypse collapse Feb 2026.*

### Components breakdown

![[aiwd-components.png]]
*12 constituents, move-weighted. Range: LZ +20% to INTU -60%. SaaS platforms (INTU, NOW, CRM) drive 43% of the basket.*

### vs S&P 500

![[aiwd-vs-spy.png]]
*AIWD +7% vs SPY +65% since July 2021. Tracked together through 2023, then AI narrative divergence accelerated. ~58pp underperformance.*

### vs IGV (Software ETF)

![[aiwd-vs-igv.png]]
*AIWD (blue) vs IGV (red) since July 2021. Same sector, opposite AI exposure. IGV includes AI winners; AIWD is pure disruption.*

**Why the gap?** IGV includes software that *benefits* from AI (platforms, infrastructure, dev tools). AIWD is pure disruption exposure — SaaS seats, legal research, IT services.

### SaaS vs Advertising breakdown

![[aiwd-saas-vs-services.png]]
*Top 3 SaaS (INTU, NOW, CRM) vs advertising (OMC) since Oct 2025.*

| Type | Weight | Pre-Feb trend | Feb move | Now |
|------|--------|---------------|----------|-----|
| **SaaS** (INTU, NOW, CRM) | 43% | Mixed | Crushed | -30% to -55% |
| **Advertising** (OMC) | 6% | Flat | Hit | -10% to -15% |

**Key insight:** SaaS with seat-based pricing got destroyed. Advertising less exposed — client relationships, creative judgment, media buying still need humans. But both are "product replacement" plays, unlike Indian IT services which is margin compression.

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Avg correlation** | **0.25** | Weak (event-driven) |
| Range | 0.03 - 0.54 | LZ-FDS to TRI-RELX |
| Strongest pair | TRI-RELX | 0.54 (legal duopoly) |
| vs SPY | ~0.30 | Low market beta |
| Period | 2024-01 to present | |

**Why so low?** This is an *event basket*, not a sector. Constituents span legal (TRI, RELX), IT services (INFY), advertising (OMC) — different industries that don't normally move together. Correlation spikes on AI capability announcements (Claude Cowork, GPT releases) then reverts.

**Pairwise clusters:**

| Cluster | Tickers | Internal corr |
|---------|---------|---------------|
| Legal | TRI-RELX | 0.54 |
| Data | FDS-MORN | 0.40 |
| Cross-sector | LZ-FDS | 0.03 |

---

## Feb 3-4, 2026 performance

| Constituent | Move | Weight |
|-------------|------|--------|
| Intuit | -34% | 16% |
| ServiceNow | -28% | 14% |
| Salesforce | -26% | 13% |
| LegalZoom | -20% | 10% |
| Thomson Reuters | -18% | 9% |
| RELX | -14% | 6% |
| Wolters Kluwer | -13% | 6% |
| LSEG | -13% | 6% |
| Atlassian | -12% | 5% |
| Omnicom | -11% | 6% |
| FactSet | -10.5% | 5% |
| Morningstar | -9% | 4% |

**Basket (move-weighted):** -19.8%

---

## Constituent earnings: fundamentals vs sentiment

### Thomson Reuters Q4 2025 (Feb 5, 2026)

First AIWD constituent to report after the selloff. Key test of whether fundamentals justify the -18% move.

| Metric | Q4 2025 | YoY |
|--------|---------|-----|
| Revenue | $2,009M | +5% |
| Organic revenue | **+7%** | |
| Adj EBITDA | $777M | +8% |
| FY EBITDA margin | 39.2% | +100bp |
| "Big 3" organic growth | **+9%** | Legal, Corporates, Tax |
| 2026 organic guide | **7.5-8.0%** | |
| 2026 margin guide | +100bp | |
| Dividend | +10% to $2.62 | 33rd consecutive raise |

**The verdict:** Fundamentals are fine. 7% organic growth, margin expanding, dividend growing. Nothing in the numbers says "business is being disrupted." But the stock was already down ~20% from the Feb 3 selloff before reporting — market is pricing in future disruption, not current weakness.

**The tension:** TRI's CoCounsel AI tool generates $32B in efficiency savings for legal clients. This is both the bull case (TRI *is* the AI tool) and the bear case (if AI commoditizes legal research, why pay Westlaw premium pricing?).

**Watch:** Stock reaction on Feb 5 will signal whether the market sees TRI as AI-resilient (moat holds, numbers prove it) or AI-vulnerable (good quarter doesn't matter if the product gets disrupted). This sets the template for how other AIWD names trade through earnings.

---

## Tracking thesis

This basket should:
1. **Spike down** on major AI capability announcements (new models, agent products)
2. **Correlate internally** more than with broad market
3. **Diverge on company-specific news** (earnings, moats proving durable)

Watch for:
- Next Anthropic/OpenAI product launch
- RELX earnings — second major AIWD constituent to report
- Signs of pricing power erosion in legal/data contracts
- TRI stock reaction post-earnings as template for basket

---

## Competitive landscape

No Wall Street firm has built an equivalent curated disruption basket. Closest analogs:

| Index | Firm | Type | vs AIWD |
|-------|------|------|---------|
| [[UBS European AI Disruption Basket]] | UBS | Europe-only disruption | Closest analog; broader (SAP, Sage) but Europe-only |
| [[GS US Software Basket]] | Goldman Sachs | Sector | Broad software, mixes winners and victims |
| [[IGV]] | iShares/BlackRock | ETF | 110 names, includes MSFT/PLTR (AI winners dilute signal) |
| [[BVP Nasdaq Cloud Index]] | BVP/Nasdaq | SaaS index | Medium-high disruption purity, not curated |
| [[JPMorgan JPAMAIDE]] | JPMorgan | AI infrastructure bull | Opposite side — AI beneficiaries, no bear basket |
| [[GS AI Productivity Beneficiaries]] | Goldman Sachs | AI adoption bull | Inverse of AIWD — same force, opposite trade |

**AIWD differentiation:** Pure SaaS/data disruption exposure (legal, analytics, SaaS platforms, advertising). Move-weighted from Feb 3-4 selloff. Only disruption-specific basket with a trackable ticker in our database.

---

## Related

- [[Claude Cowork disruption February 2026]] — catalyst event
- [[Software bear market]] — broader thesis
- [[AI disruption]] — macro theme
- [[Indian IT services]] — removed from basket (margin compression thesis, not product replacement)
- [[GS AI Productivity Beneficiaries]] — inverse basket (companies that benefit from same disruption)
- [[UBS European AI Disruption Basket]] — closest Wall Street analog
- [[GS US Software Basket]] — GS sector basket
- [[IGV]] — iShares software ETF proxy
- [[BVP Nasdaq Cloud Index]] — SaaS benchmark
- [[JPMorgan JPAMAIDE]] — AI infrastructure bull basket

*Created 2026-02-04 · Updated 2026-02-07 (move-weighted rebalance, 14 constituents)*
