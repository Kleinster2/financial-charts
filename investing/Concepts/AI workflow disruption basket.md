#concept #index #ai #disruption #correlation

# AI workflow disruption basket

Stocks that correlate on AI capability announcements threatening white-collar workflows. Emerged as a distinct factor during the [[Claude Cowork disruption February 2026|February 2026 SaaSpocalypse]].

---

## Constituents

### Legal & Data Analytics (60%)

| Ticker | Company | Weight | Notes |
|--------|---------|--------|-------|
| TRI | [[Thomson Reuters]] | 15% | Westlaw, legal research |
| RELX | [[RELX]] | 15% | LexisNexis |
| WKL.AS | [[Wolters Kluwer]] | 10% | Legal, tax, compliance |
| LZ | [[LegalZoom]] | 5% | Consumer legal |
| FDS | [[FactSet]] | 10% | Financial data |
| MORN | [[Morningstar]] | 5% | Investment research |

### Indian IT Services (25%)

| Ticker | Company | Weight | Notes |
|--------|---------|--------|-------|
| INFY | [[Infosys]] | 10% | ADR (offshore services) |
| TCS.NS | [[TCS]] | 10% | Largest IT services |
| HCLTECH.NS | [[HCL Tech]] | 5% | |

### Advertising & Agencies (15%)

| Ticker | Company | Weight | Notes |
|--------|---------|--------|-------|
| OMC | [[Omnicom]] | 7.5% | Ad holding company |
| PUB.PA | [[Publicis]] | 7.5% | Ad holding company |

**Total: 100%** — tilted toward legal/data (most directly exposed)

### Database tickers

All 11 constituents now in `market_data.db`:
```
TRI, RELX, WKL.AS, LZ, FDS, MORN, INFY, TCS.NS, HCLTECH.NS, OMC, PUB.PA
```

---

## Index methodology

- **Ticker:** AIWD
- **Weighting:** Modified equal weight (larger weight to most directly exposed)
- **Rebalance:** Quarterly
- **Base date:** Feb 3, 2026 = 100
- **Calculation:** Price return, USD-adjusted for non-US tickers
- **Script:** `scripts/create_aiwd_index.py --store`

![[aiwd-index.png]]
*AIWD basket from Jan 2025. Sharp drop at right edge = Claude Cowork plugins selloff (Feb 3-4, 2026).*

### Components breakdown

![[aiwd-components.png]]
*AIWD (blue) vs key components since Oct 2025. Thomson Reuters (red) hardest hit at -28%. Note Feb convergence — the correlation event.*

### vs S&P 500

![[aiwd-vs-spy.png]]
*AIWD -18% vs SPY +20% since Jan 2025. ~38 percentage points of underperformance. AI disruption thesis playing out.*

### vs IGV (Software ETF)

![[aiwd-vs-igv.png]]
*AIWD (blue) -18% vs IGV (red) -10% since Jan 2025. AIWD underperforming by 8pp.*

**Why the gap?** IGV includes software that *benefits* from AI (platforms, infrastructure, dev tools). AIWD is pure disruption exposure — legal, data analytics, Indian IT. Same sector, different AI exposures.

---

## Feb 3-4, 2026 performance

| Constituent | Move |
|-------------|------|
| LegalZoom | -20% |
| Thomson Reuters | -18% |
| RELX | -14% |
| Wolters Kluwer | -13% |
| Omnicom | -11% |
| FactSet | -10.5% |
| Publicis | -9% |
| Morningstar | -9% |
| Infosys | -7.4% |
| TCS | -7% |
| HCL Tech | -4.6% |

**Basket (weighted):** ~-11.5%

---

## Tracking thesis

This basket should:
1. **Spike down** on major AI capability announcements (new models, agent products)
2. **Correlate internally** more than with broad market
3. **Diverge on company-specific news** (earnings, moats proving durable)

Watch for:
- Next Anthropic/OpenAI product launch
- Earnings from Thomson Reuters (Feb 5), RELX
- Signs of pricing power erosion in legal/data contracts

---

## Related

- [[Claude Cowork disruption February 2026]] — catalyst event
- [[Software bear market]] — broader thesis
- [[AI disruption]] — macro theme
- [[Indian IT services]] — sub-theme

*Created 2026-02-04*
