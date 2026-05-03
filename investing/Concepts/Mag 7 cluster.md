---
aliases: [Magnificent 7, Mag 7, M7]
tags: [concept/cluster, ai, mega-cap, equity]
---

# Mag 7 cluster

> [!failure] Cluster status: falsified as tradable basket (May 2026)
> Intra-cluster correlation only 0.33 across AAPL/MSFT/GOOGL/AMZN/META/NVDA/TSLA. PC1 only 43.3%. Hierarchical clustering at 0.4 returns ALL 7 names as effective singletons (NVDA migrates to the [[AI capex chain basket]]; the other 6 are each their own factor). The "Mag 7" framing is a media construct, not a tradable cluster. Each name has its own dominant idiosyncratic factor that overwhelms shared mega-cap-tech beta.

The seven largest US tech / mega-cap names — Apple, Microsoft, Alphabet, Amazon, Meta, NVIDIA, Tesla — are constantly discussed as a single entity in market commentary. The math says they are not. This note documents the falsification + the actual factor structure each name belongs to.

---

## What the math says

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (1Y) | 0.33 (range 0.16-0.49) | Far below the 0.50 cluster floor |
| PC1 explained variance | 43.3% | Multi-factor cohort — no single dominant factor |
| Hierarchical clustering at 0.4 | ALL 7 names effectively singletons; NVDA migrates to AICX cluster | Cluster does not form |
| Cluster vs broad ETFs (QQQ/XLK/SMH/SPY) | 0.54 (NEGATIVE -0.21 advantage) | Mag 7 names trade with broad market MORE than each other |
| Cluster vs AI capex chain | 0.33 (+0.001 — basically zero) | No separation from the AICX cluster either |

PC1 loadings are wide (0.30-0.42) but the dispersion in pairwise correlations (0.16-0.49) means PC1 is capturing a generic mega-cap-tech beta that is shared with the broader market — not a Mag-7-specific factor.

### Pairwise correlations (1Y)

|  | AAPL | MSFT | GOOGL | AMZN | META | NVDA | TSLA |
|---|---|---|---|---|---|---|---|
| AAPL | — | — | — | — | 0.26 | 0.23 | 0.27 |
| MSFT | — | — | 0.17 | 0.34 | 0.27 | 0.37 | 0.32 |
| GOOGL | — | 0.17 | — | 0.41 | 0.35 | 0.31 | 0.39 |
| AMZN | — | 0.34 | 0.41 | — | 0.49 | 0.35 | 0.39 |
| META | 0.26 | 0.27 | 0.35 | 0.49 | — | 0.41 | 0.38 |
| NVDA | 0.23 | 0.37 | 0.31 | 0.35 | 0.41 | — | 0.47 |
| TSLA | 0.27 | 0.32 | 0.39 | 0.39 | 0.38 | 0.47 | — |

Tightest pair: AMZN-META = 0.49. Loosest: MSFT-GOOGL = 0.17 (the two most-frequently-paired names in cloud-wars commentary correlate barely above noise).

---

## What each name actually trades with

When the algorithm is given the Mag 7 cohort plus a wider universe (AI capex chain, broad ETFs, semi peers), the hierarchical clustering at 0.4 places each name in a different cluster:

| Name | Algorithmic placement | Dominant idiosyncratic factor |
|---|---|---|
| AAPL | Singleton | iPhone cycle + China exposure + AI Apple-Intelligence rollout |
| MSFT | Singleton | Cloud share, OpenAI partnership terms, Copilot monetization |
| GOOGL | Singleton | Search vs AI-answer cannibalization, antitrust (Search remedy) |
| AMZN | Singleton | E-commerce margins, AWS share losses to Azure, retail-vs-cloud weighting |
| META | Singleton | Ad market exposure, Reels/TikTok competition, Reality Labs burn |
| NVDA | **Joins [[AI capex chain basket]]** with TSM/ASML/AMAT/KLAC/LRCX/MU + broad semi ETFs | AI accelerator demand cycle |
| TSLA | Singleton | EV cycle, China demand, FSD / robotaxi narrative, Musk political volatility |

Six singletons + one defection to AICX. The "cluster" does not exist at the equity-return level.

---

## Why the framing persists despite the math

- Index-construction effects: the 7 names dominate market-cap-weighted indices (SPY, QQQ), so their COMBINED contribution to index returns is high — but that's a weighting effect, not a cluster signal. The names move with the index because they ARE the index.
- Narrative bundling: AI infrastructure capex story is real and concentrated in these names + their suppliers. But each name's exposure to the AI thesis differs substantially.
- Performance correlation in DRAWDOWNS: in broad risk-off events, the names sell off together — but that's broad-market beta, not Mag-7-specific factor.
- Earnings sequencing: all 7 report in roughly the same 2-week window each quarter, creating apparent co-movement around earnings season.

None of these is a structural factor. The math is unambiguous: there is no Mag 7 cluster at the equity-return level.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long Mag 7 basket (equal-weighted) | Inferior to long QQQ — Mag 7 is the dominant constituent of QQQ; basket adds no factor isolation |
| Long Mag 7 / short SPY | Captures only mega-cap factor (already priced in QQQ-SPY spread) |
| Long Mag 7 / short XLK | Same — Mag 7 dominates XLK weighting |
| Long [[AI capex chain basket]] for AI exposure | Cleaner expression — NVDA + AI capex chain captures the AI factor without the 6 idiosyncratic mega-cap stories |
| Pair trades within Mag 7 (e.g., long MSFT short GOOGL on AI cloud) | Captures idiosyncratic story differentials, not factor differentials |

The math says: you cannot construct a "Mag 7 long-short" trade that isolates a meaningful factor. The factor doesn't exist.

---

## Why this finding matters

This is the most important falsification in the validation pass — Mag 7 is the most-discussed cluster in markets. The math says it is a media construct, not a tradable cluster. Three implications:

- Stop interpreting "Mag 7 led the market today" as a unified signal — it's just the largest names by weight contributing to index moves.
- Stop comparing companies against Mag 7 averages as if there's a factor to compare against. The names are too disparate.
- Use [[AI capex chain basket]] for AI exposure; use [[AI hyperscalers]] thesis as the framework for the demand-side story (not a tradable cluster).

---

## Related

- [[AI hyperscalers]] — the 5-name subset (MSFT, GOOGL, AMZN, META, ORCL) that also failed cluster validation
- [[AI capex chain basket]] — where NVDA actually clusters; the validated AI tradable basket
- [[Apple]] — Mag 7 member
- [[Microsoft]] — Mag 7 member
- [[Google]] — Mag 7 member
- [[Amazon]] — Mag 7 member
- [[Meta]] — Mag 7 member
- [[NVIDIA]] — Mag 7 member; clusters with [[AI capex chain basket]]
- [[Tesla]] — Mag 7 member
- `docs/cluster-validation.md` — methodology
- `scripts/cluster_configs/mag7.yaml` — config for this test

*Created 2026-05-03 — falsified-cluster note documenting the most widely-discussed market construct that fails statistical validation*
