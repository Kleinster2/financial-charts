#concept #demand #ai #datacenter

AI hyperscalers are the demand side of the semiconductor supply chain — they consume the chips that foundries, memory companies, and OSATs produce.

---

## Why they matter

Hyperscaler capex = demand signal for the whole stack:

```
Hyperscaler $ → NVIDIA/AMD → TSMC/Samsung → [[SK Hynix]] ([[HBM]]) → [[ASE]] (packaging) → [[Cohu]] (test)
```

**2026 capex forecast:** ~$602B (CreditSights), up 36% YoY. See [[Hyperscaler capex]] for detailed analysis, chart, and forecasts.

![[hyperscaler-capex.png]]
*[[Amazon]] · [[Google]] · [[Meta]] · [[Microsoft]] · [[Oracle]]*

| Category | Amount |
|----------|--------|
| Big 5 capex (2026E) | **~$602B** |
| Global AI VC (2025 YTD Oct) | **$193B** (record) |
| [[China]] AI capex (2025) | $98B (+48% YoY) |

---

## The players

| Tier | Player | Foundry exposure | Notes |
|------|--------|------------------|-------|
| 1 | [[Microsoft]] | [[TSMC]] | [[OpenAI]] partner, largest spender |
| 1 | [[Google]] | [[TSMC]] | TPUs, Broadcom disintermediation |
| 1 | [[Amazon]] | [[TSMC]] | Trainium/Inferentia custom silicon |
| 1 | [[Meta]] | [[TSMC]] | Heavy NVIDIA buyer, [[Llama]] |
| 2 | [[Anthropic]] | [[TSMC]] | TPU route, not NVIDIA |
| 2 | [[xAI]] | [[Samsung]]? | Musk ecosystem, potential anchor |
| 2 | [[Oracle]] | [[TSMC]] | GPU cloud, NVIDIA partner |
| 2 | [[Tesla]] | [[Samsung]] | Dojo, $16.5B deal |

See individual actor notes for details.

---

## Key dynamics

**TSMC concentration**: Most hyperscalers depend on TSMC. Limited alternatives if [[Taiwan]] risk materializes.

**Samsung opportunity**: Musk ecosystem ([[Tesla]] + [[xAI]]) is the beachhead. [[AMD]] 2nm deal could bring others.

**[[Power constraints]]**: 44GW US shortfall. May slow chip deployment even if supply exists. [[BYOP]] (Bring Your Own Power) emerging.

**Enabler vs hyperscaler**: [[Broadcom]] designs chips for hyperscalers but isn't one. Sits between hyperscalers and foundries.

---

## For theses

- [[Long TSMC]] — hyperscaler demand locks TSMC capacity
- [[Short TSMC long Korea]] — Musk ecosystem anchoring Samsung
- [[Long memory]] — every GPU needs [[HBM]]
- [[Long OSAT and test equipment]] — more chips = more test/packaging

---

## Cluster validation — failed cluster test (May 2026)

The AI hyperscalers cohort is a CONCEPT/THESIS hub (capex drives semi demand), NOT a tradable cluster. The math falsifies the cluster interpretation while the thesis remains intact. Validated 2026-05-03 via `scripts/cluster_analysis.py --config scripts/cluster_configs/hyperscalers.yaml`. Full procedure in `docs/cluster-validation.md`.

### Result: math says no

| Diagnostic | Result | Verdict |
|---|---|---|
| Avg intra-cluster correlation (1Y) | **0.29** (range 0.11-0.49) | Weak — fails the 0.50 floor |
| PC1 explained variance | **43.5%** | Multi-factor — fails the 50% floor |
| Hierarchical clustering at 0.4 | All 5 names are SINGLETONS — no cluster forms | Falsified |
| Cluster vs broad ETFs (XLK/QQQ/SMH/SPY) | 0.48 — *higher* than intra-cluster | Names trade with broad market more than each other |
| Cluster vs other Mag 7 (AAPL/NVDA/TSLA) | 0.30 — *higher* than intra-cluster | Names trade with non-hyperscaler tech as much as with each other |

### Pairwise correlations (1Y)

|     | MSFT | GOOGL | AMZN | META | ORCL |
|---|---|---|---|---|---|
| MSFT | — | 0.17 | 0.34 | 0.27 | 0.37 |
| GOOGL | 0.17 | — | 0.41 | 0.35 | 0.15 |
| AMZN | 0.34 | 0.41 | — | 0.49 | 0.11 |
| META | 0.27 | 0.35 | 0.49 | — | 0.20 |
| ORCL | 0.37 | 0.15 | 0.11 | 0.20 | — |

Tightest pair: AMZN-META at 0.49 — still below cluster-floor. ORCL is the most disconnected (avg 0.21 with the rest), reflecting its legacy database core + 2025-26 [[OpenAI]] / Stargate partnership idiosyncratic re-rating. MSFT-GOOGL at 0.17 is barely above noise — surprising given the surface narrative of "hyperscaler capex peers."

### Why the math falsifies the cluster

Hyperscalers share a common AI-capex driver but each has its own dominant idiosyncratic factor at the equity level:

| Name | Dominant idiosyncratic factor that overwhelms hyperscaler co-movement |
|---|---|
| MSFT | Cloud-wars share, [[OpenAI]] partnership terms, Copilot monetization |
| GOOGL | Search monetization vs AI-answer cannibalization, antitrust (Search remedy) |
| AMZN | E-commerce margins, AWS share losses to Azure, retail-vs-cloud weighting |
| META | Ad market exposure, Reels/TikTok competition, Reality Labs burn |
| ORCL | Database modernization, Stargate / [[OpenAI]] hosting deal, legacy ERP base |

Each name is more sensitive to its own product cycle than to the shared capex pattern. The capex itself is highly correlated (all 5 spending more on AI infrastructure each quarter), but the equity returns are not.

### What this means for the vault

- **The thesis ("hyperscaler capex drives the semi stack") is intact.** The chain MSFT/GOOGL/AMZN/META/ORCL → NVIDIA → TSMC → SK Hynix → ASE / Cohu is structurally valid as a demand-flow narrative.
- **The cohort is NOT a tradable cluster basket.** Equal-weighted basket would not isolate "hyperscaler factor" — it would dilute idiosyncratic noise across 5 unrelated stories.
- **Trade the chain, not the cohort.** Long [[NVIDIA]] / [[TSMC]] / [[SK Hynix]] / [[Broadcom]] is a cleaner expression of the hyperscaler-capex thesis than long the hyperscalers themselves. Those names share a common end-demand factor and likely cluster more tightly (worth validating separately).
- **Do not construct a "hyperscaler basket" trade.** Pair-trades within the cohort (long X / short Y) are noise — the names don't share enough common factor for the residual to mean anything.

This is a textbook cluster-validation outcome: the procedure is just as valuable when it falsifies a cluster as when it confirms one. The honest finding is the value-add.

### The actual tradable cluster — supplier chain (May 2026)

The constructive follow-up: the SUPPLIERS the hyperscalers buy from DO form a cluster, even though the buyers don't. Validated 2026-05-03 via `scripts/cluster_analysis.py --config scripts/cluster_configs/hyperscaler_suppliers.yaml`. The supplier-chain candidate cohort: NVDA, AMD, AVGO, TSM, ASML, AMAT, KLAC, LRCX.

**Result: partial validation with clean sub-structure.** Intra-cluster correlation 0.61, PC1 66.3%. The hierarchical cluster at 0.4 returns NVDA + TSM + ASML + AMAT + KLAC + LRCX + MU (memory) as a tight algorithmic cluster — but AMD and AVGO are SINGLETONS.

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (1Y) | **0.609** (range 0.43-0.86) | Moderate-to-strong cohesion |
| Tightest sub-cluster | ASML, AMAT, KLAC, LRCX (avg 0.81) | Wafer fabrication equipment is a tight 4-name basket |
| Hierarchical at 0.4 | NVDA, TSM, ASML, AMAT, KLAC, LRCX, MU cluster + SMH/SOXX/XLK/SPY | AMD and AVGO are SINGLETONS |
| Cluster vs hyperscalers | 0.305 (+0.30 advantage) | Cleanly distinct from the buyers |
| Cluster vs broad ETFs (SMH, SOXX) | 0.71 (-0.10 NEGATIVE) | Cluster IS the semi/tech complex right now |

**Key sub-structure findings:**

- **The wafer fabrication equipment quartet (ASML, AMAT, KLAC, LRCX) is the tightest sub-cluster in the AI complex** — pairwise correlations 0.74-0.86. Buy any one, get exposure to all four. The cleanest tradable cluster the math has identified in this validation pass.
- **NVDA, TSM, MU cluster with the equipment names** — confirming the chain (chips → foundry → memory → equipment) is a single factor.
- **AMD is a singleton** — it trades on its NVDA-competitor narrative (share-take story), not the AI capex factor. Different business cycle.
- **AVGO is a singleton** — diversified custom-silicon + VMware integration. AI accelerator exposure dilutes vs networking and software segments.

**What this fixes about the hyperscaler thesis:** the demand-flow narrative (hyperscaler capex → semi stack) is structurally valid, but the tradable expression is the supplier basket, not the buyers. The 0.30 separation between cluster and hyperscalers is consistent with this — the supplier complex captures AI-capex factor cleanly while the hyperscalers themselves are diluted by their respective product cycles.

**Trade implications:**
- Long the AI capex chain = long {NVDA, TSM, ASML, AMAT, KLAC, LRCX, MU} basket. PC1 66% means equal-weighted basket is largely the factor.
- Tightest sub-basket = ASML/AMAT/KLAC/LRCX (wafer fab equipment). 0.81 intra-corr.
- Pair NVDA short / AMD long is a within-fabless competitive trade, NOT an AI exposure trade.
- Long the cluster vs short SMH = isolating AI specifically (hard, since SMH IS heavily exposed to the same names). Better expression is overweight the equipment quartet within a semi allocation.

---

## Related

- [[Hyperscaler capex]] — detailed capex analysis, chart, forecasts
- [[Foundry Wars]] — context (hyperscalers drive foundry demand)
- [[TSMC]] — primary foundry (most hyperscalers)
- [[Samsung]] — alternative foundry (Musk ecosystem)
- [[NVIDIA]] — supplier (GPU dominant)
- [[Power constraints]] — constraint (44GW shortfall)
- [[Broadcom]] — enabler (custom silicon design)
- [[AI infrastructure financing]] — how capex is funded
