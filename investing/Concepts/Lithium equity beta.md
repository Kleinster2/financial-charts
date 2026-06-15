---
aliases: [Lithium equity beta, Lithium miner cohort, Lithium mining cluster, Lithium miners factor]
tags: [concept, commodities, metals, mining, lithium, battery, cluster-validation]
---

# Lithium equity beta

Whether the listed lithium miners trade as one factor — and, since lithium has no investable spot instrument, what you actually own when you own the lithium trade. The cohort is four liquid US-listed names: [[Albemarle]] (ALB, high-leverage producer), [[SQM]] (diversified producer), [[Lithium Americas]] (LAC, the pre-revenue Thacker Pass developer), [[Sigma Lithium]] (SGML, Brazil producer). The validation answers yes, they cohere — and the cohesion is a real lithium-equity factor (it clears the vol-matched null) — but it is the loosest and noisiest of the three commodity cohorts, it is replicated by the LIT ETF, and it splits producers from the developer. This is the third commodity-beta cohort after [[Copper equity beta]] and [[Gold equity beta]], and it carries a structural difference that sharpens the family: lithium is not exchange-traded, so the equity complex and LIT ARE the only investable lithium exposure.

> [!warning] Cluster status: real but loose lithium factor — ETF-replicable by LIT, with a producer/developer split (June 2026)
> The four lithium names cohere as a genuine factor: weekly intra-corr 0.624 (daily 0.521 — depressed by cross-region async, so weekly is the better read), PC1 65-72%, and they reject the random-basket (p 0.0010) and vol-matched (p 0.0003) nulls — the cohesion is not just shared high vol. But it is the loosest commodity cohort yet (gold 0.86, copper 0.71, lithium 0.62) and ETF-replicable: cluster vs LIT is -0.126 (negative advantage — the cohort correlates more with its ETF than with itself), and LIT contaminates the cluster from threshold 0.30. It is internally split: [[Albemarle]]+[[SQM]] form a tight producer pair (0.80), but [[Lithium Americas]] (118% annualized vol, pre-revenue) splits off — it trades on Thacker Pass execution (GM JV, DOE loan, permits), not the lithium price. Holdout WEAKENED (ratio 0.77). The structural twist: with no GLD/CPER-equivalent spot instrument, you cannot decompose miners-vs-metal here — the equity IS the lithium price expression. See below.

A commodity cohort coheres because its members share one exogenous price, and lithium is no exception — but lithium pays a heavy idiosyncratic-noise tax that gold and copper do not. Three sources of noise hold the cohesion to 0.62 where gold reaches 0.86: the members span development stages (a pre-revenue developer trades on project catalysts, not spot), they are extreme-vol (52-126% annualized), and they are cross-region ADRs whose closes are asynchronous. What survives all that noise is still a real factor — the vol-matched null rejects at p 0.0003 — but the investable read is the same as copper and gold: the lithium-equity factor is the LIT ETF (or the [[Albemarle]]/[[SQM]] producer core), and single-name selection is a bet on a specific project or cost curve, not a separable factor. The one thing lithium adds to the family is that here the equity is not a levered proxy for an investable metal — it is the only lithium exposure that exists.

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/lithium_equity_beta.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, and `cluster_holdout_test.py --window 2y`. Standard in `docs/cluster-validation.md`. Coverage note: PLL ([[Piedmont Lithium]]) is excluded — it was delisted when Piedmont merged with Sayona to form Elevra Lithium in 2025; LAAC (Lithium Americas Argentina) was unavailable from the data source. The cohort is the four liquid US-listed names with clean history.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.521 daily / 0.624 weekly | Moderate — async-depressed daily, weekly is the better read |
| PC1 explained variance | 64.9% daily / 72.0% weekly | Moderate single-factor |
| Tightest pair | ALB-SQM = 0.80 | The two established producers |
| Loosest member | LAC (0.31-0.48 to peers) | The pre-revenue developer, splits off |
| Cluster vs lithium ETF (LIT) | 0.647 (-0.126) | Negative advantage — the cohort IS LIT |
| Cluster vs materials (XLB) | 0.339 (+0.183) | Distinct from broad materials |
| Cluster vs market (SPY) | 0.283 (+0.239) | Distinct from the market |
| Random-basket null | p 0.0010 | More cohesive than a random four-pick |
| Vol-matched null | p 0.0003 | Cohesion exceeds same-vol baskets — a real lithium factor |
| Threshold scan | boundary-dependent | LIT contaminates from 0.30 |
| 2y holdout | WEAKENED (ratio 0.77) | Factor present but eroding / regime-dependent |

![[lithium-equity-beta-cluster-correlation-1y.png]]
*1Y correlation matrix: the ALB/SQM/SGML producer block is visible; LAC is the weak column/row.*

### Hierarchical clustering and join distances

The cohort builds from a tight producer pair outward, with the developer attaching last and the ETF contaminating before the four ever form an island.

![[lithium-equity-beta-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | ALB | SQM | 0.200 | ALB+SQM (producer pair) |
| 2 | SGML | ALB+SQM | 0.418 | +Sigma |
| 3 | LAC | (producers) | 0.612 | all four |

Final join distance 0.612 — LAC attaches only at a long distance (correlation ~0.39), and the threshold scan returns no stable width: LIT joins the producer cluster from threshold 0.30, so the four lithium names are never a clean island. BOUNDARY-DEPENDENT.

![[lithium-equity-beta-cluster-threshold-scan.png]]

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility — which heavily downweights the two extreme-vol names (LAC, SGML).

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ALB | 0.549 | 27.69% | 63.12% | 32.78% |
| SQM | 0.550 | 27.73% | 51.77% | 40.03% |
| LAC | 0.387 | 19.52% | 118.22% | 12.34% |
| SGML | 0.497 | 25.06% | 126.09% | 14.85% |

![[lithium-equity-beta-cluster-pca-1y.png]]
*The producers ALB/SQM carry PC1 (loadings ~0.55); LAC is the low-loading outlier. Inverse-vol weighting pushes the index almost entirely onto ALB/SQM (73%), because LAC and SGML run at >115% annualized vol.*

### Permutation nulls

![[lithium-equity-beta-cluster-permutation.png]]

The vol-matched null is the decisive test for a cohort this volatile — the question is whether four extreme-vol names cohere more than any four extreme-vol names would. Against 10,000 volatility-matched baskets (null mean intra 0.177, 99th pct 0.392), the cohort's 0.521 daily intra clears at p 0.0003; the random-basket null rejects at p 0.0010. So the cohesion is a genuine lithium factor, not an artifact of shared high vol — even though the absolute level is the lowest in the commodity family.

### Historical tightness evolution

![[lithium-equity-beta-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2024 | 0.528 | 65.5% | 0.597 |
| 2025 | 0.549 | 67.4% | 0.617 |
| 2026 | 0.600 | 70.3% | 0.462 |

This factor is neither durable nor newly formed — it is tightening off a low base as lithium rebounds, but it remains loose. Cohesion rose from 0.53 (2024) to 0.60 (2026) as the lithium price recovered from its 2023-24 crash (+58% YoY into 2026), consistent with the [[Gold equity beta|gold finding]] that a strong directional move tightens a commodity-equity cohort. But the 2y holdout still reads WEAKENED (0.77), because the rebound is recent and the 2024-25 bottom was choppy — so lithium only partly confirms the regime rule, and confirms more loudly that idiosyncratic noise (developers, small-caps, cross-region async, no spot instrument) caps how tight a commodity-equity cohort can get.

---

## What the verdict means

Lithium is the third confirmation of the commodity-beta law, and it stress-tests the law's edges. Three reads:
- It IS the lithium trade, and the lithium trade is only an equity. The cohort correlates -0.126 against LIT (it is the ETF) and there is no spot instrument to own instead — so unlike gold (GLD) or copper (CPER), there is no unlevered metal alternative. The lithium-equity factor is the only lithium factor, which makes LIT or the [[Albemarle]]/[[SQM]] producer core the cleanest expression and raises the stakes on the equity-specific noise.
- The producer/developer split is the new structural axis. [[Lithium Americas]] (118% vol, pre-revenue) trades on Thacker Pass execution, GM, and the DOE loan, not on spot lithium — it is a lithium option, not lithium beta, and the dendrogram separates it. This differs from the developer-tightens-the-cohort case of the revenue-less [[Quantum computing]] pure-plays: those share one narrative driver, whereas each lithium developer has idiosyncratic project news, so "no fundamentals" loosens rather than binds here.
- Cohesion scales with regime cleanliness and the absence of noise. Across the family the ordering is exact — gold 0.86 (clean bull, established producers), copper 0.71 (choppy, diversified majors), lithium 0.62 (noisy rebound, developers plus small-caps plus cross-region ADRs). The factor is real in all three; how tightly it binds is set by the price regime and the idiosyncratic-vol tax.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long lithium basket | Equivalent to long LIT (lithium + battery tech) — the only investable lithium exposure, no metal alternative exists |
| Long producers (ALB/SQM) | The clean, lower-vol core (0.80 pair); SQM's iodine/plant-nutrition book dampens its single-commodity leverage |
| Long LAC (developer) | A Thacker Pass option, not lithium beta — driven by GM/DOE financing and permitting, splits from the cohort |
| Long lithium / short XLB | Captures the +0.183 separation from broad materials — real |
| Long lithium / short SPY | Distinct from the market (+0.239) but very high vol and regime-dependent (holdout 0.77) |
| Pair trades within the cohort | Idiosyncratic project/cost-curve bets (ALB leverage vs SQM diversification vs LAC execution) — not factor exposures |

---

## Related

### Member actors
- [[Albemarle]] — largest Western producer, high lithium leverage, PC1 anchor
- [[SQM]] — diversified producer (iodine, plant nutrition), the looser producer
- [[Lithium Americas]] — Thacker Pass developer (LAC), the pre-revenue outlier
- [[Sigma Lithium]] — Brazil producer (SGML), extreme vol

### Adjacent concept notes
- [[Lithium]] — the commodity (crash, rebound, deficit, demand) the cohort cannot be distinguished from
- [[Copper equity beta]] — the first commodity-beta cohort
- [[Gold equity beta]] — the second; the regime-tightness contrast (gold strengthened, lithium weakened)
- [[Batteries]] / [[Battery supply chain]] — the demand thesis
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
