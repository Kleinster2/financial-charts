---
aliases: []
---
#actor #energy #nuclear #usa #public

Oklo — Sam Altman-backed SMR company. [[Aurora]] microreactor. OpenAI connection.

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Technology | [[XLK]] | 0.56 |
| [[Semiconductors]] | [[SMH]] | 0.50 |
| Software | [[IGV]] | 0.50 |
| *[[S&P 500]]* | *[[SPY]]* | *0.49* |

OKLO shows moderate Technology correlation ([[XLK]] r = 0.56).

---

## Cluster validation

OKLO is the primary actor of the [[Nuclear renaissance#Cluster validation|Nuclear / SMR cohort]] ([[Oklo]], [[NuScale]], [[Nano Nuclear]], [[Centrus Energy]], [[Cameco]], [[BWXT]], [[Uranium Energy Corp]]; intra-corr 0.645, PC1 69.9%, validated June 2026). OKLO anchors the SMR-developer sub-bloc — OKLO+SMR are the tightest pair (join distance 0.169) — and is the highest-volatility name in the cohort (~104% annualized). The cohort rejects the random-basket and vol-matched nulls at the 0.0001 floor and the holdout is STABLE, but it has zero threshold width: the URA/NLR uranium ETFs sit inside the cluster at every cut, so the basket trades as the sector ETF rather than a distinct factor. Full diagnostic, topology, and PC1 weights in [[Nuclear renaissance#Cluster validation]].

![[nuclear-smr-cluster-dendrogram-1y.png]]
*Hierarchical clustering of the Nuclear / SMR cohort vs nuclear utilities and uranium/market ETFs — OKLO clusters with the pure-plays, distinct from the operating utilities (CEG/VST/TLN).*

---

## Why Oklo matters

[[Sam Altman]]'s nuclear bet — now scaling from concept to deployment with a 14 GW pipeline, $2.6B cash hoard, and binding deals with [[Meta]] (1.2 GW) and [[Equinix]] (500 MW). The story shifted from "pre-revenue startup" to "pre-revenue infrastructure company with hyperscaler demand locked."

| Metric | Value |
|--------|-------|
| Ticker | OKLO |
| Market cap | ~$10.2B |
| Chairman | [[Sam Altman]] |
| CEO | Jake DeWitte |
| Pipeline | 14 GW (predominantly data center/hyperscaler) |
| Cash (YE 2025) | ~$1.41B ($788M cash + $624M marketable securities) |
| Additional raise (early 2026) | $1.182B net (via $1.5B ATM program) |
| Total cash position | ~$2.6B |

---

## Charts

![[oklo-price-chart.png]]
*OKLO common-stock price history from the local market-data database. The equity is a milestone-duration instrument: reactor schedule, hyperscaler demand, and financing capacity dominate the read-through more than current revenue.*

![[oklo-fundamentals-chart.png]]
*Revenue remains zero through FY2025; the relevant financial signal is widening development-stage losses as licensing, engineering, fuel, and site work scale.*

![[oklo-sankey.png]]
*FY2025 income-statement flow. The Sankey is mainly a burn-rate map because Oklo is still pre-commercial.*

---

## Financials

### Annual history

| Fiscal year | Revenue | Gross profit | Operating income | Net income |
|-------------|---------|--------------|------------------|------------|
| 2021 | $0 | $0 | -$5.16M | -$5.16M |
| 2022 | $0 | $0 | -$10.0M | -$10.0M |
| 2023 | $0 | -$0.08M | -$18.6M | -$32.2M |
| 2024 | $0 | -$0.27M | -$52.8M | -$73.6M |
| 2025 | $0 | -$0.52M | -$139.3 million | -$105.7M |

*Source: local `market_data.db`; OKLO fundamentals fetched during the May 19, 2026 vault session via `fetch_fundamentals.py OKLO`.*

### Q4/FY2025 earnings (reported Mar 17, 2026)

| Metric | FY2025 | FY2024 |
|--------|--------|--------|
| Revenue | $0 (pre-revenue) | $0 |
| Net loss | $105.7M | $73.6M |
| Operating loss | $139.3 million | — |
| Non-cash stock comp | $41.8M | — |
| Operating cash used | $82.2M (adj: $69.2M, within $65-80M guide) | — |
| EPS | -$0.27 (vs -$0.17 est) | — |

### FY2026 guidance

| Metric | FY2026 Guide |
|--------|-------------|
| Operating cash outflows | $80-100M |
| Investing cash outflows | $350-450M (significant ramp — construction begins) |

Stock reaction: surged ~5-10% pre-earnings on DOE/NRC approval news, settled to ~$60-61 post-earnings (+1.4%). Investors shrugged off wider loss given regulatory wins and cash position.

---

## Pipeline and customers

| Customer | Deal | Scale | Timeline |
|----------|------|-------|----------|
| [[Meta]] | Binding prepayment — Aurora power campus, Pike County, Ohio | 1.2 GW | Pre-construction 2026; Phase 1 online ~2030; full 1.2 GW by 2034 |
| [[Equinix]] | Agreement + $25M prepayment | 500 MW | — |
| US military | Active discussions | — | — |
| Additional data center / industrial | Active discussions | — | — |

Total pipeline: 14 GW, predominantly data center and hyperscaler customers.

---

## Regulatory milestones (2025-2026)

| Milestone | Status |
|-----------|--------|
| DOE Other Transaction Authority (OTA) for Aurora-INL | Executed |
| Nuclear Safety Design Agreement (NSDA) | Approved |
| NRC materials license ([[Idaho]] Radiochemistry Lab) | Obtained — first NRC license (major milestone for isotope business) |
| NRC pre-application engagement | Completed |
| Rolling NRC readiness review | Initiated |
| DOE recycling R&D funding | Awarded |

---

## Key projects

| Project | Status |
|---------|--------|
| Groves Project ([[Idaho]]) | Criticality target July 4; structure, reactor tank, and major components in place; fuel procured |
| Atomic Alchemy (isotopes) | Expected first revenue mid-2026; Idaho lab now NRC-licensed |
| Tennessee Advanced Fuel Center | Initial geotechnical surveys and soil borings completed; site development initiated |
| Meta Aurora campus (Ohio) | Pre-construction and site characterization beginning 2026 |

European partnerships: BlueCala (joint technology development — balance of plant, regulatory, fuel strategy) and newcleo/Nucleo (strategic partnership with potential $2B manufacturing investment to expand US fuel fabrication capacity).

### Kalshi criticality pricing (May 19, 2026)

[[Kalshi]]'s KXCRITICALITY market prices [[Oklo]] achieving criticality before Aug. 1, 2026 at 18c last, 17c / 20c bid-ask. Volume was 10,853.86 and open interest was 4,650.65 at the API read.

That is the market's cleanest near-term read on the Groves Project criticality target embedded in this note: traders view a 2026 criticality event as possible but not base case. The pricing is consistent with the bull/bear split below: [[Oklo]] has cash, hyperscaler demand, and regulatory momentum, but the equity story still depends on proving that the first reactor milestone happens on a credible schedule.

*Source: [[Kalshi]] API series KXCRITICALITY, read May 19, 2026: https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXCRITICALITY*

---

## [[Aurora]] microreactor

| Spec | Value |
|------|-------|
| Power | 15-50 MW |
| Fuel | Recycled nuclear fuel |
| Type | Fast reactor |

---

## Business model

Power-as-a-service: build, own, operate reactors; sell power via PPA. Recurring revenue model. Plus isotope production via Atomic Alchemy subsidiary.

---

## Investment case

Bull:
- [[Sam Altman]] backing + [[OpenAI]] data center angle
- 14 GW pipeline with binding hyperscaler deals
- $2.6B cash (multi-year runway at $450-550M/yr burn)
- Regulatory momentum (first NRC license obtained)
- Fuel recycling = waste-to-energy differentiation
- AI power demand secular tailwind

Bear:
- Pre-revenue — years from commercial operations
- NRC rejection history (2022)
- Groves Project criticality not yet achieved
- [[NuScale]] ahead on commercial deployment
- ~$8B market cap for zero-revenue company
- Execution risk on 14 GW pipeline

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | OKLO |
| Market cap | ~$10.2B |
| Chairman | [[Sam Altman]] |
| CEO | Jake DeWitte |
| Pipeline | 14 GW |
| Cash | ~$2.6B |
| Status | Pre-commercial; first revenue (isotopes) expected mid-2026 |

*Updated 2026-05-19*

---

## Related

### Securities
- [[Oklo securities note]] — OKLO common equity, charts, and market-pricing companion

### Strategic / operating context
- [[OpenAI]] — connection (Sam Altman chairs both, AI power demand)
- [[Sam Altman]] — chairman (invested pre-OpenAI)
- [[Meta]] — 1.2 GW Aurora campus binding deal (Jan 2026)
- [[Equinix]] — 500 MW agreement + $25M prepayment
- [[NuScale]] — competitor (SMR peer, further along on NRC)
- [[Constellation Energy]] — peer (nuclear power)
- [[Nuclear renaissance]] — thesis context (AI power demand)

---

## Sources

- [BusinessWire: Oklo FY2025 Results (Mar 17)](https://www.businesswire.com/news/home/20260317948925/en/Oklo-Publishes-Full-Year-2025-Financial-Results-and-Business-Update)
- [BusinessWire: Oklo-Meta Agreement (Jan 2026)](https://www.businesswire.com/news/home/20260109127781/en/Oklo-Meta-Announce-Agreement-in-Support-of-1.2-GW-Nuclear-Energy-Development-in-Southern-Ohio)

