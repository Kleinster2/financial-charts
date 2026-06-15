---
aliases: [Uranium equity beta, Uranium miner cohort, Uranium mining cluster, Uranium miners factor]
tags: [concept, commodities, metals, mining, uranium, nuclear, cluster-validation]
---

# Uranium equity beta

Whether the listed uranium miners trade as one factor, what that factor is, and how far it sits from the metal. The cohort is six liquid North American uranium names: [[Cameco]] (CCJ, the producer bellwether), [[Uranium Energy Corp]] (UEC), [[Denison Mines]] (DNN), [[NexGen Energy]] (NXE), [[Energy Fuels]] (UUUU), and Ur-Energy (URG). The validation answers yes, they cohere — tightly, durably, and as a real factor that clears the vol-matched null — and like the rest of the commodity family the cohort is replicated by its miner ETF (URNM/URA). This is the fourth commodity-beta cohort after [[Copper equity beta]], [[Gold equity beta]], and [[Lithium equity beta]], and it completes the family. It also carries the family's cleanest test, because uranium — unlike lithium — has a financialized physical proxy (SRUUF, the Sprott Physical Uranium Trust), and the miners sit further from that metal than any other miner cohort: a forward buildout-thesis trade, not a spot hold. It is distinct from [[Nuclear renaissance]], which is the reactor/SMR/utility cohort; these are the fuel producers.

> [!warning] Cluster status: validated and tight, ETF-replicable by URNM — but the biggest miners-vs-metal wedge in the family (June 2026)
> The six uranium names are a tight, durable, single-factor cohort: intra-corr 0.765 (weekly 0.767 — synchronous North American listings, no async), PC1 80.6%, and they reject the independence, random-basket and vol-matched nulls all at the 0.0001 floor. The cohesion is ETF-replicable — cluster vs the miner ETFs URNM/URA is -0.088 (it correlates more with its own ETF than with itself), and URNM/URA contaminate the cluster from threshold 0.20. Holdout STABLE (ratio 1.01 — durable across the 2024 bull, the 2025 consolidation, and the 2026 re-tightening). What sets uranium apart is its distance from the metal: cluster vs physical uranium (SRUUF) is +0.180 — far above gold's +0.070 and copper's +0.033 — and SRUUF only joins the cluster at threshold 0.40, after the equity ETFs. The uranium equities are a leveraged bet on the supply-deficit/demand buildout (AI-datacenter power, SMRs, reactor restarts), not a proxy for spot, and this year they returned +45-156% while physical uranium was nearly flat (+8.5%). See below.

A commodity cohort coheres because its members share one exogenous price; uranium coheres tightly, but its equities are the least metal-like in the family. The reason is composition: half the cohort is pre-production developers ([[NexGen Energy]]'s Rook I, [[Denison Mines]]'s Wheeler River) that have no spot exposure at all yet — they are options on the next decade of uranium supply, priced off contract signings, financing, permitting, and reactor demand rather than today's pound. So the cohort clears the nulls (there is a real, distinct uranium-equity factor), it is replicated by URNM (own the ETF), and yet it is genuinely separable from the physical metal in a way gold and copper miners are not. The investable read is two-instrument: URNM for the levered uranium-equity thesis, SRUUF for the unlevered metal — and this year the choice mattered enormously, because the equity returned roughly 5-18x the metal.

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/uranium_equity_beta.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, and `cluster_holdout_test.py --window 2y`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.765 (weekly 0.767) | Tight, synchronous — second-tightest commodity cohort |
| PC1 explained variance | 80.6% | Dominant single factor |
| Tightest pair | DNN-NXE = 0.890 | The two Athabasca developers |
| Loosest pair | CCJ-URG / UEC-URG = 0.634 | The bellwether vs the smallest producer |
| Cluster vs miner ETFs (URNM/URA) | 0.853 (-0.088) | Negative advantage — the cohort IS URNM |
| Cluster vs physical uranium (SRUUF) | 0.585 (+0.180) | The biggest miners-vs-metal wedge in the family |
| Cluster vs market (SPY) | 0.445 (+0.319) | Distinct from the broad market |
| Independence / random-basket / vol-matched nulls | all p 0.0001 | Reject at the floor — a real uranium factor |
| Threshold scan | boundary-dependent | URNM/URA contaminate from 0.20, SRUUF at 0.40 |
| 2y holdout | STABLE (ratio 1.01) | Durable across regimes |

![[uranium-equity-beta-cluster-correlation-1y.png]]
*1Y correlation matrix: uniformly high (0.63-0.89), no block structure — one uranium factor, with the DNN/NXE developer pair the tightest cell.*

### Hierarchical clustering and join distances

The six names build into one tight cluster from the developer pair outward, with the miner ETFs sitting on top of them and the physical metal joining only later.

![[uranium-equity-beta-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | DNN | NXE | 0.110 | DNN+NXE (developers) |
| 2 | CCJ | DNN+NXE | 0.153 | +Cameco |
| 3 | UEC | (cluster) | 0.198 | +UEC |
| 4 | UUUU | (cluster) | 0.230 | +Energy Fuels |
| 5 | URG | (cluster) | 0.320 | all six |

Final join distance 0.320 — the cohort unifies tightly and with no internal split, but the threshold scan returns no stable width: URNM and URA contaminate from threshold 0.20 and SRUUF from 0.40, so the six names are never a clean island. BOUNDARY-DEPENDENT. The contamination order is itself the finding: the equity ETF binds the miners before the physical metal does.

![[uranium-equity-beta-cluster-threshold-scan.png]]

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility.

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| CCJ | 0.406 | 16.60% | 57.53% | 20.10% |
| UEC | 0.407 | 16.62% | 83.78% | 13.82% |
| DNN | 0.431 | 17.62% | 63.09% | 19.45% |
| NXE | 0.432 | 17.66% | 57.90% | 21.24% |
| UUUU | 0.402 | 16.42% | 98.08% | 11.66% |
| URG | 0.369 | 15.08% | 76.48% | 13.73% |

![[uranium-equity-beta-cluster-pca-1y.png]]
*Balanced loadings (0.37-0.43), developers DNN/NXE highest — every name is the uranium factor. Inverse-vol weighting tilts the index toward the lower-vol CCJ/DNN/NXE and away from UUUU (98% vol, rare-earth book).*

### Permutation nulls

![[uranium-equity-beta-cluster-permutation.png]]

A tight commodity cohort is guaranteed to crush these nulls; the rejection confirms co-movement but not distinctness. Against 10,000 random six-name baskets (null mean intra 0.149) and 10,000 volatility-matched baskets (vol-matched null mean 0.191, pool 1,033 names), the cohort's 0.765 rejects at the 0.0001 floor on both. As with copper and gold, the informative diagnostics are the threshold scan and the intra-advantage versus the metal, not the nulls — and here those say the uranium-equity factor is real, replicated by URNM, and unusually far from the physical metal.

### Historical tightness evolution

![[uranium-equity-beta-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2021 | 0.601 | 66.9% | 0.465 |
| 2022 | 0.789 | 82.5% | 0.272 |
| 2023 | 0.804 | 83.8% | 0.270 |
| 2024 | 0.784 | 82.2% | 0.268 |
| 2025 | 0.727 | 77.4% | 0.342 |
| 2026 | 0.767 | 80.9% | 0.316 |

This is a durable cluster, and its tightness tracks the uranium price regime cleanly — the family's best confirmation of the regime rule. Cohesion ran 0.78-0.80 through the 2022-24 spot bull, eased to 0.727 in the 2025 consolidation when the metal chopped, and re-tightened to 0.77 (0.816 latest 90D) as uranium resumed in 2026. A commodity-equity cohort tightens when the underlying makes a sustained directional move and loosens when it ranges — uranium and [[Gold equity beta|gold]] (both sustained bulls, both STABLE holdouts) are the tight end of the family; [[Copper equity beta|copper]] and [[Lithium equity beta|lithium]] (choppy / noisy, both WEAKENED) the loose end.

---

## What the verdict means

Uranium completes the commodity-beta family and extends it on one axis the others could not reach — distance from the metal. Three reads:
- It IS a real uranium-equity factor, and URNM is it. The cohort clears the vol-matched null at p 0.0001 and has a -0.088 advantage versus its ETF — own URNM for the uranium-equity factor; single-name selection (CCJ's production vs NXE's Rook I optionality) is idiosyncrasy.
- But it is the least metal-like cohort in the family. The +0.180 wedge versus physical uranium (SRUUF), and SRUUF joining only at threshold 0.40, say the equities are a forward buildout trade, not a spot proxy — half the cohort is pre-production developers with no spot exposure yet. This year proved it: the miners returned +45-156% while the metal returned +8.5%. The two-instrument read is real — URNM for the thesis, SRUUF for the metal.
- The premium over the metal scales with optionality. Across the family the miners-vs-metal wedge runs copper +0.033 (mature integrated majors) < gold +0.070 (established producers) < uranium +0.180 (a cohort half-built of developers). The more of a cohort that is pricing future supply rather than current production, the further its equity sits from the metal.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long uranium-miner basket | Equivalent to long URNM — the levered uranium-equity thesis with name concentration |
| Long miners / short SRUUF | Captures the +0.180 buildout premium over spot — the largest and most real metal wedge in the family, but a thesis bet (developers), not carry |
| Long miners / short URNM | Near-zero net exposure — the cohort IS URNM (-0.088 advantage) |
| URNM vs SRUUF | The clean expression of the equity-vs-metal decision; this year +31.5% vs +8.5% |
| Long uranium / short SPY | Distinct from the market (+0.319), but very high vol and a commodity-thesis bet |
| Pair trades within the cohort | Idiosyncratic — CCJ production/contract book vs NXE/DNN development optionality vs UUUU's rare-earth book |

---

## Related

### Member actors
- [[Cameco]] — the producer bellwether, lowest-vol PC1 anchor
- [[Uranium Energy Corp]] — US ISR producer/developer
- [[NexGen Energy]] — Rook I / Arrow developer (Athabasca), tightest pair with Denison
- [[Denison Mines]] — Wheeler River / Phoenix ISR developer (Athabasca)
- [[Energy Fuels]] — US producer, diversified with rare earths (highest vol, +156% on the rare-earth rally)

### Adjacent concept notes
- [[Uranium]] — the commodity (spot, term contracts, supply deficit) the cohort prices the future of
- [[Nuclear renaissance]] — the demand cohort (reactors/SMRs/utilities); the buildout thesis driving the miners
- [[Copper equity beta]] / [[Gold equity beta]] / [[Lithium equity beta]] — the rest of the commodity-beta family
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
