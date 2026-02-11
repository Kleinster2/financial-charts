---
aliases: [AIFD, Insurance broker basket, Wealth management disruption basket]
tags: [basket/internal, ai, disruption, insurance, wealth-management]
---

# AI financial disintermediation basket

Financial services stocks that correlate on AI capability announcements threatening advisory and intermediation business models. Emerged as a distinct factor during the [[Insurify insurance broker selloff February 2026]] (Feb 9) and [[Altruist wealth management selloff February 2026]] (Feb 10) — the second and third [[AI disintermediation]] shocks after the [[Claude Cowork disruption February 2026|SaaSpocalypse]].

Companion to [[AI workflow disruption basket|AIWD]] (software/data victims). Together, AIWD + AIFD cover the full AI disintermediation spectrum: AIWD = product replacement (SaaS seats → agents), AIFD = advisory replacement (human middlemen → AI comparison/planning tools).

---

## Constituents

Move-weighted from Feb 9-10 selloff. Bigger drop = higher weight.

### Insurance brokers — Feb 9 Insurify catalyst (58%)

| Ticker | Company | Weight | Feb 9 move |
|--------|---------|--------|------------|
| WTW | [[Willis Towers Watson]] | 15% | -12% |
| AJG | [[Arthur J. Gallagher]] | 12% | -9.9% |
| AON | [[Aon]] | 11% | -9.3% |
| RYAN | [[Ryan Specialty]] | 10% | -8.5% |
| BRO | [[Brown & Brown]] | 7% | -7.8% |
| MMC | [[Marsh McLennan]] | 3% | -6.1% |

### Wealth managers — Feb 10 Altruist catalyst (42%)

| Ticker | Company | Weight | Feb 10 move |
|--------|---------|--------|-------------|
| SCHW | [[Charles Schwab]] | 13% | -8.1% |
| RJF | [[Raymond James]] | 10% | -8.5% |
| LPLA | [[LPL Financial]] | 10% | -8.4% |
| SF | [[Stifel Financial]] | 9% | -7.2% |

Total: 100% — 10 constituents, move-weighted

### Excluded

| Ticker | Company | Why excluded |
|--------|---------|-------------|
| PGR | [[Progressive]] | Insurance carrier, not broker — production layer, not distribution |
| CB | [[Chubb]] | Insurance carrier |
| TRV | [[Travelers]] | Insurance carrier |
| IBKR | [[Interactive Brokers]] | Execution platform, no advisory — immune (+15% YTD) |
| HOOD | [[Robinhood]] | Retail/crypto platform — fell on broader AI fear, not advisory-specific |

Rationale: The basket captures advisory/intermediation exposure specifically. Carriers manufacture the product; execution platforms provide infrastructure. Neither is a middleman. The market confirmed this distinction — carriers fell 1-2% vs. brokers falling 6-12%.

### Database tickers

```
WTW, AJG, AON, RYAN, BRO, MMC, RJF, LPLA, SCHW, SF
```

---

## Index methodology

- Ticker: AIFD
- Weighting: Move-weighted (Feb 9-10 selloff magnitude = weight, with SCHW upweighted for market cap significance)
- Rebalance: Event-driven (re-weight on next major AI disruption catalyst)
- Base date: Feb 7, 2026 = 100 (last trading day before Insurify catalyst)
- History: July 2021 – present (limited by RYAN IPO)
- Calculation: Price return
- Script: `scripts/create_aifd_index.py --store`

---

## Charts

![[aifd-index.png]]
*AIFD basket since Jan 2024. Peaked early 2025 around 112, ground down through H2 2025, then Feb 9-10 catalysts accelerated the decline. Now at ~98 — below the base date.*

### vs AIWD and S&P 500

![[aifd-vs-aiwd-vs-spy-price-chart.png]]
*AIFD (blue) vs AIWD (red) vs SPY (green) since Jan 2024. SPY +48%, AIFD roughly flat, AIWD -18%. AIWD already in freefall from the SaaSpocalypse — AIFD is where AIWD was a week ago. If the AI disintermediation thesis keeps expanding across sectors, AIFD may follow AIWD's trajectory.*

Key insight: AIFD tracked with SPY through mid-2025, then started diverging. The Feb 9-10 drop is modest compared to AIWD's cliff — financial services intermediation is earlier in the repricing cycle than software. This could mean either (a) AIFD has more downside ahead, or (b) financial services middlemen have stronger moats than SaaS companies.

---

## AIFD vs AIWD: structural differences

| Dimension | AIWD (software) | AIFD (financial services) |
|-----------|-----------------|--------------------------|
| Revenue model | Per-seat subscription | Commission/AUM fees |
| Switching costs | Low-medium | High (relationships, contracts) |
| Regulatory moat | Low | High (licensing, fiduciary duties) |
| AI replacement type | Product replacement (agent does the work) | Advisory replacement (AI does comparison/planning) |
| Speed of disruption | Fast (software can switch tools quickly) | Slow (enterprise relationships, compliance) |
| Feb 2026 drawdown | -18% from peak | ~-12% from peak |

AIFD constituents may be structurally more defensible than AIWD — insurance brokers have 90%+ retention rates, licensed regulatory requirements, and complex commercial relationships that resist commoditization. But the personal lines / simple advisory wedge is real, and margin compression doesn't require full replacement.

---

## Tracking thesis

This basket should:
1. Spike down on AI advisory/comparison tool launches (new ChatGPT apps, Hazel features, competitor products)
2. Correlate internally more than with broad market on AI catalysts
3. Show insurance broker vs. wealth management divergence on sector-specific catalysts

Watch for:
- Additional insurance AI apps entering ChatGPT/Claude/Gemini directories (dozen+ in pipeline)
- Altruist Hazel expansion into portfolio construction, estate planning
- Broker earnings — any mention of AI fee pressure, client behavior change
- Regulatory response — licensing bodies restricting AI advisory tools

---

## Related

- [[AI workflow disruption basket]] — companion basket (software/data victims)
- [[Alternative asset managers basket]] — control group (sold off in Wave 1 as collateral damage, then recovered)
- [[AI disintermediation]] — thesis driving both baskets
- [[Insurify insurance broker selloff February 2026]] — insurance catalyst (Feb 9)
- [[Altruist wealth management selloff February 2026]] — wealth management catalyst (Feb 10)
- [[Claude Cowork disruption February 2026]] — original SaaSpocalypse (AIWD catalyst)
- [[Insurify]] — insurance AI trigger
- [[Altruist]] — wealth management AI trigger
- [[Insurance]] — sector note
- [[Willis Towers Watson]] — highest-weight constituent
- [[Charles Schwab]] — largest market cap constituent

*Created 2026-02-10*
