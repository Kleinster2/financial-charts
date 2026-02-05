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

### SaaS vs Services breakdown

![[aiwd-saas-vs-services.png]]
*TRI, FDS (SaaS) vs INFY, OMC (services) since Oct 2025. Different dynamics, same Feb convergence.*

| Type | Weight | Pre-Feb trend | Feb move | Now |
|------|--------|---------------|----------|-----|
| **SaaS** (TRI, FDS) | 60% | Already weak | Crushed | -20% to -27% |
| **Services** (INFY, OMC) | 40% | Flat to +20% | Crushed | -5% to -12% |

**Key insight:** SaaS (legal/data) was under pressure all year — market already worried about AI disruption. Services (Indian IT, ad agencies) were fine until Cowork plugins launched — then got hit hard. INFY moved from +20% to -5% in weeks.

**Implication:** Services names may have more recovery potential if Cowork fears fade. SaaS names have structural concerns beyond the catalyst.

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

**AIWD differentiation:** Cross-sector (legal + IT services + advertising), globally scoped, weighted by directness of AI revenue displacement. Only disruption-specific basket with a trackable ticker in our database.

---

## Related

- [[Claude Cowork disruption February 2026]] — catalyst event
- [[Software bear market]] — broader thesis
- [[AI disruption]] — macro theme
- [[Indian IT services]] — sub-theme
- [[GS AI Productivity Beneficiaries]] — inverse basket (companies that benefit from same disruption)
- [[UBS European AI Disruption Basket]] — closest Wall Street analog
- [[GS US Software Basket]] — GS sector basket
- [[IGV]] — iShares software ETF proxy
- [[BVP Nasdaq Cloud Index]] — SaaS benchmark
- [[JPMorgan JPAMAIDE]] — AI infrastructure bull basket

*Created 2026-02-04 · Updated 2026-02-05 (TRI earnings)*
