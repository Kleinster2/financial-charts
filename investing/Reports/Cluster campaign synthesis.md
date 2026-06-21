---
aliases: [Cluster campaign synthesis, Cluster validation capstone synthesis, The law of distinctness]
tags: [report, cluster-validation, synthesis, capstone]
---

# Cluster validation campaign — capstone synthesis

> [!note] Living capstone — last updated 2026-06-20. This is the standing synthesis of the cluster-validation campaign; it is revised in place as new cohorts are validated, not re-created per date. Per-pass FDR/OOS snapshots live in dated reports (e.g. the 2026-06-15 quarterly pass).

A synthesis of the whole cluster-validation campaign: 137 cohorts logged in `scripts/cluster_registry.csv` (121 primary + 16 sub-cohorts; 118 with computed random-basket nulls), tested with the Gate-11 pipeline (intra-correlation, PCA, hierarchical clustering, random-basket and vol-matched permutation nulls, threshold-stability scan, out-of-sample holdout, and intra-advantage versus the relevant sector ETF). The living data hub is [[Vault cluster taxonomy]]; this report draws the campaign's structural conclusion. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.

## The central finding

Co-movement is common; distinctness is rare. Of the 118 cohorts with computed nulls, 104 pass the random-basket null under Benjamini-Hochberg FDR control — i.e. the great majority of "sectors" really do cohere more than a random pick of comparable names. But passing that null is necessary, not sufficient, for an ownable factor. The decisive question is the next one: does the cohort cohere more with itself than with the liquid sector ETF that already exists? On that test the campaign sorts into three tiers:

| Tier | Definition | Count (approx) | Investable read |
|---|---|---|---|
| 1. Distinct non-ETF factor | Positive intra-advantage vs the sector ETF AND a separable threshold band — no liquid ETF replicates it | 9 (+ 2 sub-group) | Own the basket |
| 2. Real but ETF-replicable | Coheres and beats the nulls, but = its sector ETF (small/negative ETF intra-advantage; ETF contaminates the cluster) | the majority (~90) | Own the ETF |
| 3. Falsified | Fails the random-basket null (pure dispersion) OR shatters by driver | 14 fail the null outright; more shatter | Own the names singly, or nothing |

The campaign's one-line law: distinctness is earned by a shared driver no liquid ETF already prices — and that happens only at concentrated oligopolies, homogeneous single-asset cohorts, and specialized supply chains. Everything diffuse — broad cyclical complexes, brand-momentum labels, pipeline/event-driven names — either resolves to a sector ETF or shatters.

## Tier 1 — the nine distinct non-ETF factors

These are the only cohorts where the basket out-coheres every liquid ETF: a positive intra-advantage over the sector ETF and (for most) a separable threshold band. Ranked by robustness:

| Cohort | Intra | vs sector ETF | Threshold band | Holdout | Why it escapes the ETF |
|---|---|---|---|---|---|
| [[Drug distributors]] | 0.644 | +0.502 (vs XLV/IHI) | 0.30 [0.40–0.70] | STABLE 0.93 | low-margin fee-based logistics; orthogonal to the drug-development cycle XLV prices |
| [[Tankers]] | 0.795 | +0.483 (vs BOAT/SEA) | 0.15 [0.30–0.45] | STABLE 0.95 | rate-cycle owners; only ETFs are broad-shipping (diluted); the driver trades via [[BWET]] but the levered equity factor has no ETF |
| [[Solid waste]] | 0.583 | +0.424 (vs EVX) | 0.15 [0.55–0.70] | WEAKENED 0.74 | EVX is diluted by smaller environmental names; clusters with XLI, not the waste majors |
| [[Residential REITs]] | 0.849 | +0.360 (vs VNQ) | 0.15 [0.20–0.35] | STABLE 0.96 | one asset (US multifamily), one driver (rates + rent); VNQ dilutes with every property type |
| [[Railroads]] | 0.646 | +0.203 (vs IYT) | 0.10 [0.45–0.55] | WEAKENED 0.81 | the Class I rail oligopoly; IYT is truck/parcel-heavy, sits with freight not rails |
| [[Trucking and LTL]] | 0.742 | +0.203 (vs IYT) | 0.15 [0.30–0.45] | STRENGTHENING 1.11 | tight freight-cycle factor; IYT is the nearest proxy but the pure-trucker basket separates |
| [[Life science tools]] | 0.620 | +0.172 (vs XLV/IHI) | 0.00 (0.50 point) | STABLE 0.89 | bioprocessing/pharma-R&D-capex; no liquid pure-tools ETF exists |
| [[Analog and auto-industrial semiconductors]] | 0.729 | +0.079 (vs SMH/SOXX) | 0.15 [0.35–0.50] | WEAKENED 0.81 | the auto/industrial-inventory cycle; SMH is cap-weighted and AI-dominated, so it holds these names but tracks the AI pole |
| [[Tobacco majors basket]] | 0.512 | distinct vs XLP | 0.00 (boundary) | WEAKENED 0.76 | the only distinct defensive (vs staples/utilities = XLP/XLU); boundary-dependent + weakening |

The structural signature is unmistakable: every one is a concentrated oligopoly ([[Drug distributors|drug big-3]], [[Tankers|tankers]], [[Solid waste|waste big-4]], [[Railroads|Class I rails]], [[Tobacco majors basket|tobacco]]), a homogeneous single-asset cohort ([[Residential REITs|apartment REITs]]), or a specialized supply chain / cycle pure-play ([[Life science tools|picks-and-shovels]], [[Trucking and LTL|freight]], [[Analog and auto-industrial semiconductors|auto/industrial analog chips]]) — where a liquid ETF either does not exist or is too diluted to capture the names. Drug distributors is the purest case (the campaign's largest ETF intra-advantage, +0.502, and widest separable band, 0.30); tankers is the runner-up (+0.483, STABLE) and the cleanest "the driver itself trades but the equity factor doesn't" case ([[BWET]] prices the rate). Tobacco and life-science tools are the most marginal (no separable band); analog semis has the thinnest ETF margin (+0.079), distinct only because its ETF SMH is structurally AI-dominated.

A sub-group addendum: distinctness can live in a tight core even when the full label is ETF-replicable. The [[Auto parts retail|ORLY+AZO]] premium auto-parts duopoly is distinct (+0.599 vs the retail ETFs, the widest sub-cohort band, 0.45) while the five-name auto-parts cohort is only PARTIAL; and the [[Self-storage REITs|PSA/EXR/CUBE]] self-storage big-three is distinct (+0.173 vs VNQ, separable band [0.20–0.30], STABLE 0.96 holdout) while the four-name self-storage cohort is ETF-replicable — the looser fourth name (NSA) drags the label into VNQ. Distinctness can be a sub-group, not a whole sector.

## Tier 2 — real but ETF-replicable (the majority)

Most validated cohorts are real (they cohere and beat the nulls) yet not distinct — the sector ETF sits inside the cluster, so the basket adds nothing over owning the ETF. Representative cases:

| Cohort | = ETF | Note |
|---|---|---|
| WFE quartet (ASML/AMAT/KLAC/LRCX) | SMH/SOXX | the tightness ceiling (intra 0.82) yet ETF-embedded |
| [[Mega banks basket]] | XLF | money-center banks |
| [[Regional banks]] | KRE | the campaign's tightest cohort (0.871) — but KRE holds the exact names |
| [[Tower REITs]] | VNQ | distinct from data-center REITs, but VNQ-embedded |
| [[Packaged food and beverages]] | XLP | real defensive cohesion, splits by scale |
| [[Regulated utilities]] | XLU | a real factor, not duration, but = XLU |
| [[Building products]] | XLI + XHB | splits into two ETFs (HVAC vs housing-products) |
| [[Industrial distributors]] | XLI | MRO core holds, WSO defects |
| [[Reinsurers and specialty P&C]] | KIE | reinsurers don't even separate from primary carriers |
| [[Self-storage REITs]] | VNQ | distinct from apartments (+0.275) but = broad REITs; only the PSA/EXR/CUBE core separates |
| [[Precious metals royalties]] | GDX | the capital-light royalty model = gold, exactly like the miners (model-agnostic) |
| [[Rare earth equity beta]] | REMX | real but SHOCK-BORN — no factor at all before the 2025-26 China export-control shock |
| [[Traditional asset managers]] | XLF | levered market/financials beta; the lowest distinctness margin in the campaign (+0.011) |
| [[Aerospace aftermarket]] | ITA | distinct from the defense primes but ITA holds both; TransDigm an idiosyncratic singleton |

The energy value chain is the cleanest worked example of the law: [[Oilfield services]] = OIH, [[Refiners]] = CRAK, [[Midstream and pipelines]] = AMLP, the majors = XLE — four legs, each its own ETF, with services (capex cycle) decoupling from crude while refiners (crack spread) stay attached. The commodity-beta law is the other: copper/gold/lithium/uranium/steel miners ARE their commodity ETF (the equity is the metal) — and it is model-agnostic, because even the capital-light [[Precious metals royalties|gold royalties]] (no mines, no opex, optionality) collapse to GDX just like the miners. The one near-exception is shock-dependence: [[Rare earth equity beta|rare-earth equities]] only became a factor on the 2025-26 China shock, and even then = REMX. Banking and insurance each resolve into ETF-replicable poles (banks: KRE vs XLF; insurance: brokers/primary/life/title/reinsurers all = KIE/sector).

## Tier 3 — the falsifications

Two failure modes:

Pure dispersion (grade-1) — fails the random-basket null; no factor at all, just single-name stories. The clearest cases: [[Grocers]] (p 0.106 — only the blocked Kroger-Albertsons merger pair coheres) and [[Theatrical exhibition]] (p 0.099 — AMC/CNK/IMAX share an end-market, not a factor). Fourteen cohorts fail the null outright.

Driver-divergence (grade-2) — beats the null on shared sector beta but shatters because the label spans divergent drivers:
- [[Automakers]] — TSLA trades as tech, GM/F as legacy cyclicals, RIVN/LCID as EV-startups; negative ETF intra-advantage.
- [[Athletic footwear and apparel]] — brand-momentum names (NKE China reset, DECK/ONON hypergrowth, CROX value) on idiosyncratic product cycles; negative −0.053 vs the retail ETFs, regime-dependent.
- [[Chemicals]] — splits into cyclical commodity chems (DOW/LYB/CE) vs defensive industrial gases (LIN/APD).
- [[Biotech]] — durably loose (~0.42); each name its own pipeline/patent-cliff story; the healthcare set ([[Pharma majors|pharma]], [[GLP-1 receptor agonists|GLP-1]], [[Medtech]], [[DTC Telehealth]], biotech) is a clean sweep of non-distinctness.

## The cross-cutting laws

The campaign produced a set of repeatable laws, now well-supported:

1. Distinctness law — a cohort is a distinct factor only if it out-coheres every liquid ETF; that requires concentration (oligopoly), homogeneity (one asset), or a specialized supply chain. (Tier 1.)
2. ETF-embedding — real cohesion is usually just sector beta a liquid ETF already prices. Passing the random-basket null is necessary, not sufficient. (Tier 2, the majority.)
3. Commodity-beta law — miners = the commodity ETF; the equity is the underlying. It is model-agnostic: even capital-light gold royalties ([[Precious metals royalties|FNV/WPM/RGLD]] — no mines, no opex, optionality) collapse to GDX, the same verdict as the miners.
4. Value-chain-split law — multi-stage industries split by stage, asymmetrically (energy: services decouple, refiners stay attached).
5. Driver-divergence law — a label spanning divergent return drivers shatters (autos, apparel, chemicals, building products, the healthcare set).
6. Shock/regime dependence — some cohorts cohere only under a common shock; when the shock is generic risk beta already in the ETF, that is not distinctness (apparel), whereas a specific shared exogenous driver can be (the travel cyclicals). A factor can even be born from a shock with no prior existence: [[Rare earth equity beta|rare-earth equities]] were uncorrelated until the 2025-26 China export-control shock manufactured the cohort (regime-dependent in existence, not just in strength — a factor with a birthday) — and even then it = REMX.
7. Sub-group distinctness — distinctness can be concentrated in a tight core inside an otherwise-ETF-replicable label, with a looser member dragging the full label into the ETF (ORLY+AZO within [[Auto parts retail|auto parts]]; PSA/EXR/CUBE within [[Self-storage REITs|self-storage]]; GS+MS within banks).
8. Index-rule law — a name sitting inside a broad ETF is distinct iff the ETF is ruled by a different factor, and ETF-replicable iff ruled by the same one. [[Analog and auto-industrial semiconductors|Analog semis]] sit inside SMH yet separate, because SMH is cap-weighted and ruled by the AI mega-caps; [[Precious metals royalties|gold royalties]] sit inside GDX and collapse, because GDX is ruled by gold. Being in the index does not settle distinctness — what rules the index does.
9. Single-asset-REIT decoupling — a homogeneous single-asset REIT is distinct only if its demand driver decouples from the broad rate/REIT factor. Apartments (rate + rent + supply) do, so [[Residential REITs]] is distinct; storage (the "4 Ds") and cell towers do not, so [[Self-storage REITs]] and [[Tower REITs]] = VNQ.

## Formal statistics

Multiple-testing correction over the 118 cohorts with computed nulls (random-basket intra p-value, alpha 0.05):
- Pass uncorrected (p < 0.05): 104 / 118
- Pass Benjamini-Hochberg (FDR): 104 / 118 (BH threshold 0.0318)
- Pass Bonferroni: 63 / 118 (threshold 0.00042)

The 63 Bonferroni survivors are the unambiguously-cohesive cohorts; the 14 that fail even uncorrected are the pure-dispersion falsifications. But note the key limitation: this correction tests cohesion (the random-basket null), not distinctness — most of the 104 BH-passers are Tier 2 (= their ETF). The Tier-1 distinction rests on the intra-advantage-vs-sector-ETF and threshold-band diagnostics tracked per-cohort in [[Vault cluster taxonomy]], not on this single p-value.

## Investable read-through

- Own the basket for the nine Tier-1 factors — there is no liquid ETF substitute (drug distributors, tankers, waste, residential REITs, railroads, trucking, life-science tools, analog semis, tobacco), plus the two sub-group factors (the ORLY+AZO auto-parts duopoly and the PSA/EXR/CUBE self-storage big-three).
- Own the ETF for everything in Tier 2 — the bespoke basket adds nothing over SMH, XLF, KRE, VNQ, XLP, XLU, XLE/OIH/CRAK/AMLP, KIE, etc.
- Own the names singly (or avoid) in Tier 3 — grocers, theatrical exhibition, automakers, apparel, chemicals, biotech trade on stock-specific stories, not a factor.

## Methodology, caveats, provenance

- Pipeline and thresholds: `docs/cluster-validation.md`. Per-cohort configs: `scripts/cluster_configs/`. Registry: `scripts/cluster_registry.csv`.
- Out-of-sample (OOS) re-validation is deferred for the June campaign's ~20 new cohorts (incl. tankers, rare earths, analog semis, precious-metals royalties, self-storage) — they have no post-definition window yet (OOS needs ~15 post-definition observations; due ~July 2026). The last formal OOS pass was the 2026-06-15 capstone; three OOS downgrades (Mag 7, ECPR, Boutique advisory) remain to formalize then.
- Data-integrity guard: the split scanner `check_split_discontinuities.py --verify-yf` (added 2026-06-20) cross-checks every flag against yfinance's recorded splits, so an un-back-adjusted split cannot silently invert a cohort verdict (the KLA/FUBO/OPAD failure mode). It is wired into `/daily-scan`.
- Distinctness numbers (intra-advantage vs sector ETF, threshold bands) are computed at analysis time and recorded in [[Vault cluster taxonomy]]; the registry CSV stores the cohesion diagnostics and nulls.

## Related

- [[Vault cluster taxonomy]] — the living data hub (exploration log, sub-cohort sweep, summary cards)
- [[Cohort, cluster, basket]] — terminology
- Tier-1 cohorts: [[Drug distributors]], [[Tankers]], [[Solid waste]], [[Residential REITs]], [[Railroads]], [[Trucking and LTL]], [[Life science tools]], [[Analog and auto-industrial semiconductors]], [[Tobacco majors basket]]
- Sub-group distinct factors: [[Auto parts retail|ORLY+AZO]], [[Self-storage REITs|PSA/EXR/CUBE]]
- ETF-replicable cases of note this session: [[Precious metals royalties]] (= GDX), [[Rare earth equity beta]] (= REMX, shock-born), [[Self-storage REITs]] (= VNQ), [[Traditional asset managers]] (= XLF), [[Aerospace aftermarket]] (= ITA)
- The 2026-06-15 quarterly capstone (FDR + OOS) — the prior formal pass

---

*Living capstone — created 2026-06-20, last updated 2026-06-20 to the full 9 distinct factors + 2 sub-group factors (added tankers and analog semis; folded in the model-agnostic commodity-beta, index-rule, and single-asset-REIT-decoupling laws). Synthesis of the cluster-validation campaign through 2026-06-20 (137 cohorts). Data: `scripts/cluster_registry.csv`, [[Vault cluster taxonomy]].*
