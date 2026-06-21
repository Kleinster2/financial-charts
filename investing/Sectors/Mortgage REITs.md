---
aliases: [mREITs, mortgage REIT]
---
#sector #finance #reits #mortgage

# Mortgage REITs

Mortgage REITs (mREITs) invest in mortgage-backed securities and mortgage loans. High dividend yields (10-15%) but rate-sensitive and leveraged. Two giants: Annaly (NLY) and AGNC.

---

## Key players

| Company | Ticker | Portfolio | Yield | Strategy |
|---------|--------|-----------|-------|----------|
| Annaly | NLY | $97.8B | ~12% | Diversified (Agency + Credit + MSR) |
| AGNC | AGNC | — | ~14% | Pure Agency MBS |
| Two Harbors | TWO | — | — | Agency + MSR |
| Starwood Property | STWD | — | — | Commercial mortgages |
| New York Mortgage | NYMT | — | — | Residential credit |

---

## Annaly vs AGNC

| Metric | Annaly (NLY) | AGNC |
|--------|--------------|------|
| Portfolio | $97.8B | Smaller |
| Strategy | Diversified | Pure Agency |
| Dividend | Quarterly | Monthly |
| Yield | ~12.3% | ~13.7% |
| Leverage | 5.7–6.0x | 7.2–7.5x |
| Credit risk | Some (non-agency, MSR) | None (agency only) |
| Rate sensitivity | Moderate | Higher |

Annaly: Diversified with Agency MBS ($87.3B), residential credit, and MSRs.

AGNC: Pure-play Agency MBS, higher leverage, monthly dividends.

---

## 2025 performance

| Metric | Value |
|--------|-------|
| NLY YTD return | +14.8% |
| AGNC 6-month return | +14.2% |
| Sector vs industry | Outperforming |

Annaly Q3 2025:
- Economic return: 8.1% (Q3), 11.5% (YTD)
- 8 consecutive quarters positive economic return
- Liquidity: $8.8B (incl. $5.9B cash + unencumbered MBS)

---

## How mREITs work

Business model:

1. Borrow short-term (repo market)
2. Buy long-term MBS
3. Earn spread (MBS yield - funding cost)
4. Leverage amplifies returns

Key risks:

| Risk | Description |
|------|-------------|
| Interest rate | Rising rates hurt MBS prices |
| Spread | MBS spreads can widen |
| Prepayment | Falling rates = faster prepays |
| Leverage | Amplifies gains AND losses |
| Funding | Repo market disruptions |

---

## Rate environment impact

| Scenario | Impact on mREITs |
|----------|------------------|
| Rates falling | MBS prices rise, book value up |
| Rates rising | MBS prices fall, book value down |
| Stable rates | Carry trade works, steady dividends |
| Inverted curve | Funding costs exceed yields |

Current: Rates declining from 2023 peak — supportive for mREITs.

---

## MBS spread dynamics

| Metric | Value (Q3 2025) |
|--------|-----------------|
| Agency MBS OAS | +29 bps |
| vs 10-year average | ~20 bps wider |
| vs IG corporates | More attractive |

Opportunity: Agency MBS still cheap vs history and vs corporates.

---

## Dividend sustainability

Warning signs:
- Book value declining faster than dividends
- Leverage increasing
- Spread compression

Healthy signs (current):
- NLY raised dividend 7.7% in Mar 2025
- Positive economic returns
- Adequate liquidity buffers

---

## Investment implications

Bull case:
- High yields (12-14%)
- Rates declining
- Spreads attractive vs history
- Agency MBS = no credit risk

Bear case:
- Rate volatility hurts
- Leverage amplifies losses
- Prepayment risk if rates fall fast
- Complex, hard to analyze

Best environment: Stable or gradually declining rates with steep yield curve.

---

## Cluster validation

> [!warning] Cluster status: validated cohesion but ETF-replicable (= REM); an agency-vs-commercial sub-structure, and NOT the bond trade (Jun 2026)
> The five mortgage REITs ([[Annaly Capital|NLY]]/[[AGNC]]/[[Starwood Property Trust|STWD]]/[[Blackstone Mortgage|BXMT]]/[[Rithm Capital|RITM]]) are a real but ETF-replicable cohort: intra-corr 0.652, PC1 72.3%, rejecting the independence, random-basket and vol-matched nulls (0.0001/0.0001/0.0003), holdout WEAKENED (0.85). The decisive number is a NEGATIVE −0.169 intra-advantage versus the mortgage-REIT ETF [[REM]], which contaminates the cluster from threshold 0.20 (the tightest cut) — the mREITs correlate with REM more than with each other. Two structural findings beyond the ETF verdict: (1) NOT the bond trade — even the agency names (leveraged agency MBS) cluster with REITs/credit, not Treasuries (+0.342 versus [[TLT]], which forms its own separate cluster; "rate-sensitive" is a valuation statement, not daily co-movement); and (2) an agency-vs-commercial sub-structure — agency [[Annaly Capital|NLY]]+[[AGNC]] (0.88) and commercial [[Starwood Property Trust|STWD]]+[[Blackstone Mortgage|BXMT]] (0.72) are tight within type, looser across (~0.57-0.64), fusing only at 0.404 — two wings of one mREIT factor, not a clean split. Own [[REM]] for the exposure. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.652 [0.570–0.882] | Moderate; weekly 0.618; the agency pair (NLY/AGNC 0.88) the tightest |
| PC1 explained variance | 72.3% | One factor (weekly 69.7%), with an agency/commercial sub-structure |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Beats a random 5-pick |
| Vol-matched null p (10k) | 0.0003 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.85 | train 0.772 → test 0.653 (eroding in 2026) |
| Threshold clean width | 0.00 | REM contaminates from 0.20; VNQ from 0.50 — never isolates |
| Intra-adv vs mREIT ETF (REM) | −0.169 | Negative — correlates with its ETF more than itself (= REM) |
| Intra-adv vs rates (TLT) | +0.342 | NOT the bond trade — clusters with REITs, not Treasuries |
| Intra-adv vs equity REITs (VNQ) | +0.138 | Modestly tighter than equity REITs (one broad REIT complex) |

1Y daily log returns through 2026-06-18, threshold 0.5. Config: `scripts/cluster_configs/mortgage_reits.yaml`; registry row 2026-06-21.

### Boundary — REM inside from 0.20; Treasuries stay out

![[mortgage-reits-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five mREITs cluster with [[REM]] (their ETF) and [[VNQ]] (equity REITs) — one REIT complex — while [[TLT]] (Treasuries) forms its OWN separate cluster and SPY is apart. The mREITs sit with REITs, not bonds.*

The threshold scan returns zero clean width — [[REM]] joins the cohort cluster at 0.20 (the tightest cut), [[VNQ]] at 0.50. There is no threshold at which the mREITs separate from their ETF.

### Topology — agency and commercial wings

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | NLY + AGNC | 0.118 | the agency pair — very tight (corr 0.88) |
| 2 | STWD + BXMT | 0.275 | the commercial/CRE-credit pair (corr 0.72) |
| 3 | RITM + (NLY+AGNC) | 0.329 | the hybrid joins the agency wing |
| 4 | (STWD+BXMT) + (RITM+NLY+AGNC) | 0.404 | the two wings fuse — one mREIT factor |

The agency wing ([[Annaly Capital|NLY]]/[[AGNC]], + hybrid [[Rithm Capital|RITM]]) and the commercial wing ([[Starwood Property Trust|STWD]]/[[Blackstone Mortgage|BXMT]]) are each tight internally but join only at 0.404 — a real sub-structure, yet they do fuse below the cut into one factor. PC1 explains 72.3%.

### PC1 index weights

![[mortgage-reits-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 72.3% (weekly 69.7%); loadings near-even (0.43–0.47). Moderate vols (17–23%).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NLY | 0.471 | 21.1% | 19.2% | 21.8% |
| AGNC | 0.464 | 20.8% | 19.6% | 21.0% |
| STWD | 0.438 | 19.6% | 16.9% | 23.0% |
| BXMT | 0.426 | 19.1% | 21.9% | 17.2% |
| RITM | 0.435 | 19.5% | 22.7% | 17.0% |

The PC1-mimic basket is a worse-tracking [[REM]] — the ETF already holds these names. The topology (agency vs commercial wings) is the real internal structure, distinct from this raw-return PC1-mimic.

### Distinctness — it is REM, and not the bond trade

![[mortgage-reits-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm agency block (NLY/AGNC) and a warm commercial block (STWD/BXMT), cooler across the two; REM warm against all; TLT cool against all.*

The intra-advantage numbers: −0.169 versus [[REM]] (the mREITs are their ETF), +0.342 versus Treasuries ([[TLT]]), +0.138 versus equity REITs ([[VNQ]]), +0.263 versus the market. The negative REM advantage with REM contaminating from 0.20 is the ETF-replicable verdict; the +0.342 over TLT is the clean negative — these are not the bond trade despite the agency MBS leverage. Own [[REM]].

### Historical tightness evolution

![[mortgage-reits-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Moderately durable — 0.65 to 0.81, tightening in rate-shock windows (2022) and easing to 0.655 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.755 | 80.5% |
| 2022 | 0.808 | 84.7% |
| 2024 | 0.740 | 79.3% |
| 2025 | 0.734 | 78.8% |
| 2026 | 0.655 | 72.6% |

*A real cohort every year (0.65–0.81), tightening when rates/spreads move all the names together (2022), eroding in 2026 (holdout WEAKENED 0.85). ETF-replicable throughout — REM captures it.*

Method: `docs/cluster-validation.md`, [[Vault cluster taxonomy]].

---

## Related

Key players:
- [[Annaly Capital]] — largest mREIT, diversified strategy
- [[AGNC]] — pure Agency MBS, monthly dividend

Market context:
- [[MBS market]] — underlying asset class
- [[Mortgage rates]] — key driver
- [[Housing]] — sector context
- [[Fannie Mae]] — Agency MBS issuer
- [[Freddie Mac]] — Agency MBS issuer
- [[REITs]] — broader REIT sector

*Created 2026-01-16*
