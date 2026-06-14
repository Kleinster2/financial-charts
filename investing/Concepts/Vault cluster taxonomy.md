---
aliases: [Cluster taxonomy, Cluster comparison, Vault clusters, Cluster validation taxonomy]
tags: [concept, framework, cluster-validation, meta-analysis]
---

# Vault cluster taxonomy

Synthesis of cluster-validation findings across the vault's validated and falsified cohorts as of May 2026. Documents what was learned by applying the [[Space pure-plays]] framework to 8 cohorts with matched methodology (1Y window through 2026-05-07, threshold 0.5, identical PCA + factor-decomposition + subset-optimization scripts). The cross-cohort tests revealed structural patterns that recur — useful as a reference when validating new cohorts. Statistically re-validated June 9–10 2026 against a cleaned stock-only null with multiple-testing correction, and extended with a post-definition out-of-sample layer — see the June 2026 re-validation section. For the vocabulary used throughout — cohort (candidate), cluster (verdict), basket (tradeable expression) — see [[Cohort, cluster, basket]].

---

## Cross-cohort comparison (matched methodology)

| Cluster | N | Intra-corr (1Y) | Pairwise range | PC1 | Specific factor | Verdict |
|---|---|---|---|---|---|---|
| [[Sectors/WFE\|WFE quartet]] | 4 | 0.804 | 0.740-0.857 | 85.33% | — | Validated (tightest — oligopoly limit) |
| [[Sectors/Korea Memory\|Korea Memory]] | 2 | 0.756 | (pair only) | 87.82% | — | Validated (pair) |
| [[Sectors/US Memory\|US Memory]] | 3 | 0.696 | 0.655-0.754 | 79.72% | — | Validated |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 7 | 0.691 | 0.482-0.840 | 73.79% | 37.0% | Validated (tightest N=7) |
| [[Space pure-plays]] | 7 | 0.624 | 0.494-0.749 | 67.96% | 59.6% | Validated |
| [[Sectors/AI Compute\|AI Compute]] | 3 | 0.600 | 0.544-0.663 | 73.37% | — | Validated |
| [[Concepts/Defense primes basket\|Defense primes 6-core]] | 6 | 0.556 | 0.448-0.707 | 64.31% | 36.0% | Validated (after LDOS exclusion) |
| [[Concepts/Defense primes basket\|Defense primes 7-name]] | 7 | 0.512 | 0.210-0.707 | 58.59% | — | Partial (LDOS drag) |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 7 | 0.316 | 0.078-0.461 | 41.82% | 14.6% | Falsified |
| [[Concepts/Boutique advisory consolidation\|Boutique advisory consolidation]] | 6 | 0.731 (matched re-run 2026-06-10) | — | 77.70% | — | Validated (matched; holdout STABLE 0.90) |
| [[Sectors/UAS defense micro-cluster\|UAS pair]] | 2 | 0.678 | (pair only) | — | — | Validated micro-cluster (KTOS-AVAV; current through Jun. 3) |

All cohorts now run with matched methodology — Boutique advisory's pending re-run completed 2026-06-10 (intra 0.731, PC1 77.70%, random-basket p at the 0.0001 floor), slotting it into the validated band exactly where the May 2025 figures suggested. [[Space pure-plays]] is the canonical worked example with all 19 analytical sections; [[Concepts/Mag 7 cluster|Mag 7]] is the canonical falsified counterpoint at same N=7. The table's intra-corr/PC1 figures are the May 2026 matched-window snapshot; every cohort's permutation p-value was re-measured 2026-06-09/10 against a cleaned stock-only null — see the June 2026 re-validation section below.

![[vault-cluster-taxonomy-intra-corr-chart.png]]
*Cross-cohort intra-correlation comparison using the taxonomy table above. The chart shows the 0.50 validation floor, the updated UAS pair at 0.678 through Jun. 3 2026, and the falsified Mag 7 reference at 0.316; Boutique advisory remains marked as older-methodology until re-run.*

---

## June 2026 statistical re-validation campaign

The 2026-06-09 robustness audit of the validation framework (`docs/cluster-validation-audit-2026-06-09.md`, plain-language companion in `investing/Reports/2026-06-10-cluster-framework-explainer.md`) found the random-basket null pool polluted with non-equity series (ETFs, FX pairs, crypto, macro, synthetic indices) and the permutation math capable of impossible p = 0.0 readings. Remediation landed 2026-06-10 — stock-only null pool (~920 US-listed names), Phipson-Smyth p-values at 10,000 permutations — and all 34 registry cohorts were re-graded. Three campaign results matter for this taxonomy:

### 1. Honest p-values, and the distortion was size-dependent

20 of 34 cohorts pass Bonferroni, 30 of 34 pass Benjamini-Hochberg FDR at alpha 0.05; the only outright failures (Foundry monopoly p = 0.328, [[AI hyperscalers]] 0.135, Animal health 0.065, [[Cybersecurity consolidation]] 0.051) were already falsified or never promoted — no validated cohort lost certification. The old pollution had distorted in both directions by cohort size: small-N cohorts were penalized by occasional all-crypto/all-FX null draws ([[Sectors/AI Compute\|AI Compute]] p 0.023 → 0.0026, [[Sectors/Korea Memory\|Korea Memory]] 0.006 → 0.0031, [[Concepts/Mag 7 cluster\|Mag 7]] 0.010 → 0.0050), while weak mid-size cohorts were flattered by FX/macro deflators ([[AI hyperscalers]] 0.028 → 0.135). Mag 7's falsification never rested on the permutation test anyway — the holdout (ratio 0.44, REGIME-DEPENDENT) and zero-width threshold scan carry it. A vol-matched null variant now exists for high-beta cohorts; [[Space pure-plays]] rejects all three nulls — independence, random-basket, and same-volatility baskets — at the 0.0001 floor, retiring the "it's just shared beta" critique by measurement.

### 2. The registry is now a forward ledger (post-definition OOS pass)

Every cohort carries a git-frozen definition date (first commit of its YAML config) and is re-validated quarterly on returns strictly after it — data discovery bias cannot have touched (`scripts/cluster_oos_validation.py`, §5 of the falsification framework in `docs/cluster-validation.md`). First pass 2026-06-10, all verdicts PRELIMINARY at 19–25 of the 40 required observations: 18 OOS-STRENGTHENING, 11 OOS-CONFIRMED, 3 OOS-WEAKENED ([[Concepts/Boutique advisory consolidation\|Boutique advisory]], Fabless semis, [[Concepts/Mag 7 cluster\|Mag 7]]), 1 OOS-FAILED (ECPR — see exploration log), 1 insufficient (luxury, defined May 28). Broad ratio inflation across defense/insurance STRENGTHENING rows (1.3–1.7) reflects ambient correlation rising in May–June 2026 (Hormuz, CPI anticipation); the OOS random-basket p is the control — those cohorts also beat random baskets on the same days at the floor. First non-preliminary verdicts land ~July 2026; status callouts only cite OOS verdicts once PRELIMINARY drops.

### 3. Tensions queued for the July pass

Two cohorts falsified in-sample are cohering out-of-sample: [[Cybersecurity consolidation]] (ratio 1.44, p = 0.0091) and Animal health (1.37, 0.0143). Boutique advisory's cooling is real but not a falsification — full six names, intra 0.724 → 0.530 post-definition, still beating random at p = 0.0009: a validated cluster descending from its May 1 print-event cohesion peak. Indian metals loosened on fresh data (intra 0.581 → 0.418 across windows) — watchlist.

---

## Ongoing exploration log

This section records boundary tests, candidate screens, and falsified cluster hypotheses that are too important to leave only in daily notes but are not yet part of the matched cross-cohort comparison table. Durable diagnostics still live in the cohort-owning note; this log tracks what was tested, what changed, and where the evidence lives.

| Date | Exploration | Status | Finding | Canonical evidence |
|---|---|---|---|---|
| 2026-06-14 | AI optics/networking (COHR/CIEN/CRDO/ALAB) — do the listed AI-datacenter-interconnect names trade as one factor? (added COHR/CIEN/CRDO/ALAB + FN to DB) | NOT ONE COHORT — two sub-cohorts (optical + interconnect) | Intra 0.495 (weekly 0.284), PC1 62.2% with a large PC2 (21.2%). Passes all three nulls — independence 0.0001, random-basket 0.0023, vol-matched 0.0002 — so real shared AI-capex beta, but the random-basket pass is ~20× weaker than the floor-passing cohorts. Every structural test says two factors: zero threshold width (optical peers LITE/FN contaminate from 0.25), splits into an optical pair (COHR+CIEN 0.71) and an interconnect-silicon pair (CRDO+ALAB 0.61) that join only at 0.589 — above the 0.5 cut. Negative intra-advantage −0.054 vs the optical peers (the optical sleeve is not distinct from broad optics), +0.085 vs NVDA (not just AI-compute beta). Holdout WEAKENED 0.73 with the factor structure flipping (loadings corr 0.12); tightened in the 2025 optical rerating (0.631) then decoupled through 2026 (0.505). The optical sleeve belongs to [[AI fiber supercycle]]; the [[Credo Technology Group]]+[[Astera Labs]] interconnect-silicon pair is the new micro-cohort under [[Connectivity]]. A thematic label spanning two factors, not a tradeable cohort — passes the cohesion nulls (unlike [[Medtech]]) but is two pairs averaged, like [[Exchange operators]] with tighter sub-pairs. | `scripts/cluster_configs/ai_optics.yaml`; [[AI interconnect#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-14 | Neoclouds (CRWV/NBIS/IREN/CIFR/APLD) — GPU-cloud + miner-convert cohort; the audit's last DB-ready candidate | Real cohort, not distinct from Crypto-to-AI | Intra 0.624 (weekly 0.585), PC1 69.9%; rejects independence/random-basket/vol-matched nulls at the 0.0001–0.0002 floor (real cohesion despite extreme 92–110% annualized vol — the highest-beta cohort in the set). But not a distinct factor: merges with the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners (+IBIT) from threshold 0.35, intra-advantage +0.000 vs that cohort. Two sleeves — pure GPU clouds (CRWV+NBIS, 0.73) and miner-converts (IREN+CIFR, 0.79, APLD bridging). Distinct from AI-compute (NVDA/MSFT, +0.316) — not NVDA beta. Tightening 0.56 (2025) → 0.70 (2026); holdout INDETERMINATE (cohort too young, CRWV/NBIS listed 2024–25). The converters ARE Crypto-to-AI; CRWV/NBIS the only non-miner sleeve. | `scripts/cluster_configs/neoclouds.yaml`; [[Neoclouds#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-14 | Theatrical exhibition (AMC/CNK/IMAX) — do the listed movie-theater names trade as one box-office factor? | FALSIFIED — a shared end-market, not a factor | Intra 0.328 (0.299 weekly — all US-listed, not async), PC1 55.5% (large PC2 27.6%). The decisive test: independence null rejected (p 0.0001) but random-basket null NOT rejected (p 0.099, vol-matched 0.108) — cohesion equals a random 3-pick of comparable names. Three singletons at every threshold (CNK+IMAX pair only at 0.588, AMC joins at 0.715); zero threshold width; holdout WEAKENED (0.81). Three different return drivers under one label: [[AMC Entertainment]] a levered meme stock (71% vol, just 0.17 corr with IMAX), [[IMAX]] an asset-light premium-format licensor, [[Cinemark]] the only pure operating exhibitor. Barely distinct from the studios it depends on (+0.100 vs DIS/LION). Cohesion faded 0.459 (2021 meme/COVID era) → 0.328 (2026). A shared end-market is not a shared factor — the theatrical mirror of [[Exchange operators]] (shared moat), but with no constructive sub-cluster underneath. | `scripts/cluster_configs/amc.yaml`; [[Theatrical exhibition#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-14 | Brazil fintech (STNE/PAGS/NU/MELI/XP) — the disruptor companion to the validated Brazilian-banks cohort | Real cohort, not a separable factor | Intra 0.570 (weekly 0.607), PC1 66.1%; rejects the random-basket null at the 0.0001 floor and holdout STABLE (1.03, loadings corr 0.75) — a real, durable cohort. But not distinct: at 0.5 the four financial fintechs merge with the incumbent banks (ITUB/BBD/BSBR) and EWZ/EEM into one cluster; intra-advantage −0.044 vs the banks (they correlate MORE with the incumbents than with each other) and +0.063 vs the ETFs. The disruption is real in the business but invisible in the tape — fintechs and banks are one Brazil-financials / EM-beta factor on BRL/Selic. MELI is the e-commerce outlier (joins at 0.546). Same shape as [[Nuclear renaissance|Nuclear/SMR]]: a real cohort inseparable from its sector benchmark. The validated Brazilian-banks cohort (0.847) is far tighter — the incumbents are the cleaner factor. | `scripts/cluster_configs/brazil_fintech.yaml`; [[Brazil fintech#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-14 | Fabless semis boundary refinement — added MRVL (the audit's missing fifth member) to NVDA/AMD/AVGO/QCOM, fresh window | MRVL belongs; the cohort is REGIME-DEPENDENT | MRVL fits as well as any member (PC1 loading 0.444, AVGO–MRVL 0.47 — the custom-ASIC pair the [[Short standalone ASICs]] thesis trades), so the audit's "natural fifth member" is confirmed. But the 5-name cohort on the fresh 1Y window (through 2026-06-12) is not a durable cluster: intra 0.412 (0.328 weekly), PC1 53.3%, negative intra-advantage vs SMH/SOXX (−0.214 — it is semis-ETF beta), threshold zero-width, holdout REGIME-DEPENDENT (ratio 0.58, loadings corr 0.04). Tight in the 2021–24 AI-compute boom (0.755 in 2022), decoupled to 0.392 by 2026. QCOM is the structural outlier (mobile/handset, joins last at 0.673); the durable micro-structure is the NVDA/AVGO/AMD AI-compute core + the AVGO/MRVL ASIC pair. | `scripts/cluster_configs/fabless_semis.yaml`; registry row 2026-06-14; [[Short standalone ASICs]] |
| 2026-06-14 | Medtech (MDT/BSX/ISRG/RMD/SYK/EW/ABT) — defensive secular-growth medical-device cohort | FALSIFIED — a sector, not a factor | Intra 0.348 (0.266 weekly — lower, all US-listed), PC1 44.8% (variance spread across PC2–PC4). Names shatter into singletons at 0.5 (EW/RMD/ABT/BSX alone; only MDT/ISRG/SYK loosely group, pulling in IHI). Negative intra-advantage vs the sector ETFs (−0.078): the names correlate more with IHI/XLV than with each other — the Mag-7-is-QQQ signature, no medtech-specific factor beyond healthcare/market beta. Random-basket p 0.0096, vol-matched 0.0143 (marginal, beats random only via shared beta); threshold zero-width; holdout WEAKENED 0.85 with unstable factor structure (loadings corr 0.29). Fragmented 0.672 (2022) → 0.292 (2026); only real pair MDT+SYK (0.56). Each name trades its own franchise (ISRG robotics, EW TAVR, RMD sleep apnea). Pure dispersion — unlike [[Exchange operators]], no constructive sub-cluster underneath. | `scripts/cluster_configs/medtech.yaml`; [[Medtech#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-14 | Financial data providers (SPGI/MCO/MSCI/FDS/TRI/RELX/MORN) — the "data toll roads"; closes the [[Exchange operators]] loop | VALIDATED — distinct data factor that absorbs the data-pivoted exchanges | Intra 0.607 (0.701 weekly, async-corrected), PC1 66.5%; rejects independence/random-basket/vol-matched nulls at the 0.0001 floor. Overwhelmingly distinct from the transaction exchanges CME/CBOE (+0.554, the widest business-model gap in the batch) and from broad financials (+0.337). The cohort's natural membership extends to NDAQ (joins from threshold 0.40) and ICE (from 0.55) — the constructive counterpart to the exchanges falsification: "exchanges" failed because ICE/NDAQ defected to this factor. Tight core SPGI+MCO (0.115); analytics FDS/MORN and diversified TRI/RELX attach as satellites. Holdout WEAKENED (0.82) but loadings corr 0.91 — durable structure, off the 2024-25 peak. | `scripts/cluster_configs/financial_data.yaml`; [[Financial data providers#Cluster validation]]; registry row 2026-06-14 |
| 2026-06-13 | Exchange operators (CME/ICE/NDAQ/CBOE) — WFE-type ceiling candidate (oligopoly + moat) | FALSIFIED — two decoupled sub-factors | Intra 0.360 (below the 0.50 floor), PC1 52.2% (PC2 27.9%), random-basket p 0.0195 (marginal), threshold zero-width (BOUNDARY-DEPENDENT). Hierarchical clustering splits the cohort: ICE+NDAQ merge with the data providers (SPGI/MCO/MSCI) — they trade as recurring-data "toll roads" — while CME+CBOE form a separate derivatives/volatility pair, the two connecting only at distance 0.756. Intra-advantage +0.030 vs data providers, −0.006 vs e-trading (not distinct). Fragmented from a 0.744 peak in the 2020 COVID-vol spike to ~0.40 now as ICE/NDAQ re-rated on data. An oligopoly plus a moat is not a cluster (contrast WFE at 0.804: same customers, one capex cycle). | `scripts/cluster_configs/exchanges.yaml`; [[Exchange operators]]; registry row 2026-06-13 |
| 2026-06-13 | European rearmament (RHM.DE/BA.L/LDO.MI/SAAB-B.ST/HO.PA/HAG.DE/KOG.OL) — the European leg of [[Long global rearmament]], tested vs the US primes | Validated — distinct European factor (6-name core; Kongsberg outlier) | Intra 0.651 (0.717 weekly, async-corrected), PC1 71.5%; rejects independence/random-basket/vol-matched nulls at the 0.0001 floor. Distinct on every axis: +0.340 vs the US [[Defense primes basket]], +0.424 vs European equity (VGK), +0.385 vs market. Six-name core (RHM/BA/LDO/SAAB/HO/HAG) joins ≤0.273; [[Kongsberg]] is the outlier (joins 0.592, lowest PC1 loading, maritime/offshore leg) — the European mirror of the LDOS exclusion. Holdout STABLE (1.03, loadings corr 0.79); threshold band [0.60, 0.65] fragile only because KOG.OL forces a loose cut. Confirms European rearmament is its own factor, not US-defense or European-equity beta. | `scripts/cluster_configs/euro_rearmament.yaml`; [[European rearmament#Cluster validation]]; registry row 2026-06-13 |
| 2026-06-13 | Defense IT services (LDOS/BAH/CACI/SAIC) — pattern-7 boundary-refinement test for the [[Defense primes basket]] LDOS exclusion | Validated — moderate, distinct, regime-sensitive | Intra 0.604, PC1 70.4%; rejects independence/random-basket/vol-matched nulls (p 0.0001/0.0004/0.0001). Hierarchical clustering separates the IT-services cohort from the hardware primes (+0.310 intra-advantage) and commercial IT ACN/CTSH (+0.296); LDOS clusters with IT-services, not the primes — the constructive answer to its exclusion from the 6-name primes core. Holdout WEAKENED (0.85): tight in budget-up years (0.745 in 2022, 0.696 in 2025), loose in the 2024 DOGE-scrutiny dispersion (0.526). Threshold clean four-name band [0.44, 0.48] (width 0.04); KBR joins just above as the natural fifth member, PSN stays out. Two service-pairs: BAH+SAIC (consulting) and LDOS+CACI (C5ISR/cyber). | `scripts/cluster_configs/defense_it.yaml`; [[Defense IT Services#Cluster validation]]; registry row 2026-06-13 |
| 2026-06-13 | Nuclear / SMR pure-play basket (OKLO, SMR, NNE, LEU, CCJ, BWXT, UEC) — highest-priority thesis-backed item from the Jun-12 coverage audit | Validated factor, ETF-replicable (not a distinct basket) | Intra-corr 0.645, PC1 69.9%; rejects independence + random-basket + vol-matched nulls all at the 0.0001 floor (vol-matched matters — developers run >100% annualized vol). Holdout STABLE (ratio 1.00). Threshold width 0.00 — but the contaminator is the sector's own ETF: URA/NLR hold these names and sit inside the cohort's cluster at every cut, so the basket is the ETF (−0.145 intra-advantage vs URA/NLR, +0.103 vs SPY/IWM). Distinct from operating utilities (+0.247): nuclear equity is two factors. Topology: SMR-developer sub-bloc (OKLO/SMR/NNE + LEU) vs uranium miners (CCJ/UEC), merging at join distance 0.379, BWXT the satellite. Tightening 0.602 → 0.695 across 2025→2026. A new verdict shape for the taxonomy: real + regime-durable + vol-matched-robust, yet not a distinct basket because the liquid sector ETF replicates it. | `scripts/cluster_configs/nuclear_smr.yaml`; [[Nuclear renaissance#Cluster validation]]; registry row 2026-06-13 |
| 2026-06-12 | [[AI SaaS Disruption]] seat-software basket (CRM, WDAY, NOW, HUBS, MNDY, TEAM) — first validation, closing the framework's own named example | Validated core, non-separable boundary | Intra 0.703, PC1 75.4%, random-basket p = 0.0001 on both diagnostics (null mean 0.137, 99th pct 0.301), holdout ratio 0.90 STABLE. Threshold width 0.00 — not because the cohort splits (intact from 0.40 up) but because ADBE+IGV attach from 0.30 and MSFT/SAP by 0.45 while ORCL stays a singleton at every cut: the basket is the dense core of the seat-software factor, hedgeable via IGV. Adobe confirmed as an Aurelion "Trapped Incumbent" in correlation space; Oracle has left the application-software complex. Rolling history re-tightened 0.470 (2024) → 0.735 (latest 90d) as the disruption thesis became one trade | `scripts/cluster_configs/ai_saas.yaml`; [[AI SaaS Disruption#Cluster validation]]; registry rows 2026-06-12 |
| 2026-06-12 | Registry backfill — statistical suite on the four config-only cohorts (SEI speed-to-power, PAX alt-managers, LION studios, STRZ premium-subscription) | LION/STRZ formally falsified; SEI real-but-boundaryless; PAX cohort real, PAX itself singleton | LION p = 0.274/0.352 and STRZ p = 0.157/0.175 vs the random-basket null — both post-separation media cohorts are indistinguishable from random 5-picks, formalizing the Jun-11 "media is a directory, not a factor" finding at the permutation level. SEI trio p = 0.0071/0.0088 but width 0.00 (fuses only by absorbing the equipment complex GEV/CAT/CMI/ETN/PWR at 0.55). PAX cohort p at the floor with width 0.00 — BAM joins the US-alt cluster from 0.30, before PAX (~0.55): BAM/BLK are statistically closer to the US alts than the "mini-Blackstone" is. All four now carry registry rows + definition dates for the July OOS pass | `scripts/cluster_registry.csv`; cluster sections in [[Lionsgate]], [[Starz]], [[Solaris Energy Infrastructure]], [[Pátria Investimentos]] |
| 2026-06-10 | ECPR (edge control-plane risk basket: [[Cloudflare]], [[Akamai]], [[Fastly]]) post-definition OOS test | Falsified out-of-sample — first OOS falsification in the framework | The cohort passed every in-sample diagnostic (clean-null random-basket p = 0.0123, BH-pass), then its intra-correlation went 0.444 → −0.001 over the 24 sessions after its May 3 definition date; random baskets beat it 69% of the time on the same window. The boundary did not survive contact with unseen data — the exact failure mode in-sample validation cannot catch. Re-grade at the July pass when PRELIMINARY drops. | `scripts/cluster_registry.csv` (oos columns); `investing/attachments/cluster-oos-validation-2026-06-10.txt`; `docs/cluster-validation-audit-2026-06-09.md` item 5 |
| 2026-06-09/10 | Full-registry statistical re-validation (clean null) + first OOS pass | 34 cohorts re-graded; no validated cohort lost certification | Stock-only null pool, Phipson-Smyth p at 10k draws: 20/34 Bonferroni, 30/34 BH-FDR. OOS first pass: 18 STRENGTHENING / 11 CONFIRMED / 3 WEAKENED / 1 FAILED / 1 insufficient, all PRELIMINARY. Distortion of old p-values was size-dependent (small-N penalized by crypto/FX null clumps, weak cohorts flattered by deflators). See the June 2026 re-validation section above. | `scripts/cluster_registry.csv`; `docs/cluster-validation-audit-2026-06-09.md` Status |
| 2026-06-05 | [[Sectors/UAS defense micro-cluster\|UAS defense micro-cluster]] current-data validation | Existing micro-cluster held and tightened | KTOS-AVAV remains a real 2-name micro-cluster through 2026-06-03 with 0.678 trailing-1Y pair correlation, up from the prior 0.638 read. It is distinct from defense primes (pair avg 0.368), broad ETFs (0.443), and the [[Space pure-plays]] cohort (0.464), but still too small to treat as a full cohort. | [[Sectors/UAS defense micro-cluster\|UAS defense micro-cluster]]; `prices_long` current through 2026-06-03 |
| 2026-06-05 | [[Space pure-plays]] current-data validation | Existing cluster held and tightened | Current local DB through 2026-06-03 still validates the seven-name cohort at the 0.5 threshold: 1Y intra-correlation 0.634, PC1 68.8%, pairwise range 0.538-0.748. The defense-prime separation widened to +0.357, confirming the public-space selloff is a space-beta sleeve rather than merely defense beta. | [[Space pure-plays]]; `scripts/cluster_configs/rklb.yaml`; `space-pureplays-cluster-jun03-*` diagnostics |
| 2026-05-27 | [[Space pure-plays]] post-SpaceX-IPO-hype refresh | Existing cluster held | Refreshed `prices_long` through 2026-05-27 and fixed date filtering in `scripts/cluster_analysis.py`; the seven-name cohort still clustered together at the 0.5 threshold with 1Y intra-correlation 0.625 and PC1 68.0%. `VOYG` is the best watch-list addition candidate, `KTOS` remains a defense-tech boundary case, and `DXYZ` is an event co-mover rather than structural member. | [[Space pure-plays]]; `scripts/cluster_configs/rklb.yaml`; `space-pureplays-cluster-may27-*` diagnostics |
| 2026-05-28 | [[Luxury]] / global luxury basket retest | Validated narrower core; broad basket falsified | Broad "global luxury" is a useful industry basket, not one clean correlation cluster. Strict European core = `MC.PA`, `RMS.PA`, `KER.PA`, `CFR.SW`, `MONC.MI` with 1Y avg correlation 0.664 and PC1 73.3%; loose core adds `BRBY.L` and `BC.MI`. `1913.HK` and `ZGN` remain outside the validated core. | [[Luxury]]; `scripts/cluster_configs/luxury_global.yaml`; `global-luxury-cluster-*` diagnostics |
| 2026-05-28 | [[Prada]]/[[Zegna]] fashion-cluster hypothesis | Falsified | `1913.HK` / `ZGN` pair correlation was only 0.175 over 1Y and 0.151 over 2Y; the wider fashion/premium set had only 0.288 1Y avg correlation and 39.1% PC1. [[Burberry]] and [[Brunello Cucinelli]] attach more to the loose luxury core than to a fashion sleeve. | [[Luxury]]; `scripts/cluster_configs/luxury_global.yaml`; follow-up Python screen logged in `investing/Daily/2026-05-28.md` |
| 2026-05-28 | Luxury-adjacent cluster screen | Watch list | Strongest neighbor was affluent-consumer beta, not fashion: `RACE`, `RL`, `ZGN`, `SPY`, `XLY`, `VGK`, `EWQ` showed 0.591 2Y avg correlation and 67.2% PC1. U.S. accessible premium/apparel was moderate; athletic premium was weaker; beauty/eyewear did not validate as one adjacent cluster. | [[Luxury]]; `investing/Daily/2026-05-28.md` |

---

## Structural patterns observed across cohorts

### 1. Cohort size does not determine cluster structure

Three N=7 cohorts span the verdict spectrum:

| Cohort | Intra-corr | Verdict |
|---|---|---|
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 0.691 | Validated (tightest N=7) |
| [[Space pure-plays]] | 0.624 | Validated |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 0.316 | Falsified |

Same N=7, materially different cluster structures. The binding constraint is business-model coherence, not cohort size. When validating a new N=7 cohort, the comparison question becomes "which of these three is it closest to in business-model variance?"

### 2. Three distinct stability trajectories

Cohort cohesion can move in three directions over time:

| Pattern | Example | Mechanism |
|---|---|---|
| Tightening | [[Space pure-plays]] (0.48 → 0.64 over 3Y → YTD) | Institutional basket construction (Nov 2025 regime shift) |
| Stable | [[Sectors/Crypto-to-AI\|Crypto-to-AI]] (0.69-0.74 throughout 3Y) | Cluster identity formed early (2023-2024 AI capex flood) and stayed |
| Stable | [[Concepts/Defense primes basket\|Defense primes 6-core]] (0.55-0.59 throughout) | DoD-customer factor is structurally durable, no narrative shift |
| Loosening | [[Concepts/Mag 7 cluster\|Mag 7]] (0.47 → 0.32 over 3Y → YTD) | Cohort decoupling into individual catalyst paths post-2024 |
| Event-peak decay | [[Concepts/Boutique advisory consolidation\|Boutique advisory]] (0.724 in-sample → 0.530 post-definition, Jun 2026 OOS pass) | Sector-print cohesion peak (May 1 2026) decaying toward baseline; still beats random (p = 0.0009) — cooling, not fragmenting |

Cleanest signature of an institutional-basket-construction event: PC2 collapses while PC1 rises (Space pure-plays Nov 2025: PC2 21.2% → 7.9%, PC1 51.9% → 71.2%). Cleanest signature of fragmentation: intra-correlation falls monotonically across windows (Mag 7).

### 3. Three distinct PC2 sub-structure types

PC2 captures cohort sub-structure when it exists. Three observed patterns:

| Pattern | Example | Description |
|---|---|---|
| Balanced 2-sleeve | [[Sectors/Crypto-to-AI\|Crypto-to-AI]] (pure miners vs AI-pivot) | PC2 loadings split roughly evenly with multiple names in each sleeve |
| Balanced 2-sleeve | [[Space pure-plays]] (data businesses vs hardware) | Same |
| Single-name outlier | [[Concepts/Defense primes basket\|Defense primes]] (HII +0.77 alone) | One name isolated on PC2; rest cluster near zero |
| Multi-axis fragmentation | [[Concepts/Mag 7 cluster\|Mag 7]] (PC2 + PC3 both meaningful) | No clean PC2 split; cohort spreads across multiple factors |

When checking a new cohort: look at PC2 loadings ranked by magnitude. If the loadings fall into two roughly-equal groups of opposite sign, you have a balanced split. If one name dominates PC2 magnitude (>0.6) with others near zero, you have an outlier. If PC2 + PC3 are both meaningful and loadings don't fall into clean groups, the cohort is multi-factor and may not be a single tradeable cluster.

### 4. Factor specificity ranges widely

After regressing the equal-weighted basket against relevant benchmarks, the residual variance reveals how cohort-specific the factor is:

| Cohort | Residual factor share | Reads |
|---|---|---|
| [[Space pure-plays]] | 59.6% | Genuine pure-play factor; basket is the only tradable expression |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 37.0% | Real factor but ~60% explained by SPY + IBIT + AI infra |
| [[Concepts/Defense primes basket\|Defense primes 6-core]] | 36.0% | Real factor; SPY beta near zero |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 14.6% | Essentially leveraged QQQ; cohort is the benchmark |

The right threshold for "genuine pure-play factor" is roughly 30-40%+ residual variance after relevant benchmarks. Below 20% the cohort doesn't add factor isolation beyond what's available via broad ETFs. Space pure-plays' 59.6% is the highest residual factor share among tested cohorts — the cleanest case for "you can only express this thesis via the basket."

### 5. The Swiss-Army-knife pattern

Every validated cohort has one diversifying name that appears in 3-4 of the top-5 Sharpe pairs. The name has lower PC1 loading (more idiosyncratic) but high cumulative return, so combining it with high-PC1-loading peers improves Sharpe via uncorrelated residual returns:

| Cohort | Swiss-Army-knife name | PC1 loading | 1Y return | Why it diversifies |
|---|---|---|---|---|
| [[Space pure-plays]] | [[Planet Labs\|PL]] | 0.30 (lowest) | +242% (#2 in cohort) | Pure-data EO; trades on NGA contract cycle |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | [[Iris Energy\|IREN]] | 0.41 | +163.5% (#1) | Heaviest AI-pivot among miners; HPC scale |
| [[Concepts/Defense primes basket\|Defense primes]] | [[RTX]] | 0.34 | +22.7% (#1) | Most diversified commercial+defense |

The Swiss-Army-knife name is the cohort member with the most-divergent business model relative to the rest. It's the cohort's least-factor-tracking name AND its highest-Sharpe-pair partner. Future cohort analyses should explicitly identify this name — it's the natural complement to the factor-clean tracking subset.

### 6. Factor-tracking ≠ return-maximizing (three independent confirmations)

Optimizing for "best 2-name tracking correlation to the full basket" produces a different optimal pair than optimizing for "best Sharpe" or "best cumulative return":

| Cohort | Best factor-tracking pair | Best Sharpe pair | Best return pair |
|---|---|---|---|
| [[Space pure-plays]] | LUNR+BKSY (0.94 corr) | RKLB+PL (Sharpe 2.03) | LUNR+PL (+254%) |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | HUT+CLSK (0.97 corr) | RIOT+IREN (1.78) | RIOT+IREN (+136%) |
| [[Concepts/Defense primes basket\|Defense primes]] | NOC+HII (0.94 corr) | RTX+GD (1.27) | RTX+HII (+22.6%) |

Crypto-to-AI and Defense primes both produced the SURPRISE pattern where the factor-tracking pair UNDERPERFORMS the full basket on Sharpe (HUT+CLSK 1.12 < full 7 1.39 < complement 5 1.49; NOC+HII 0.35 < full 6 0.82 < complement 4 1.09). The factor-clean tracking optimization passes over the high-return idiosyncratic names because they're factor-misaligned by construction. Three independent cohort tests confirmed: the right answer depends on the objective.

For traders: pick factor-tracking pair for hedging / pair-trading the basket; pick Sharpe-optimal pair for portfolio-construction position sizing; pick return-maximizing pair for single-name conviction.

### 7. Boundary refinement matters

Sometimes a cohort is mis-defined by one name. The framework can refine the boundary:

| Cohort | Original verdict | After name refinement |
|---|---|---|
| Defense primes | Partial (with LDOS, intra-corr 0.512) | Validated (without LDOS, intra-corr 0.556) |

LDOS had PC1 loading 0.295 (lowest in cohort, vs 0.37-0.42 for the others) AND 1Y return of -30% (vs +18-23% for top performers). Both signals pointed to misalignment. Removing it lifted the cohort's verdict from partial to validated. The rule: when a cohort partially validates, check the lowest-PC1-loading name first — it may be the boundary refinement.

### 8. Validated cohorts have low SPY beta

After benchmark decomposition, the validated cohorts trade on factors uncorrelated with broad market:

| Cohort | SPY beta (multivariate) |
|---|---|
| [[Concepts/Defense primes basket\|Defense primes]] | -0.52 |
| [[Space pure-plays]] | -0.12 |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | +0.71 (with IBIT controls) |
| [[Concepts/Mag 7 cluster\|Mag 7]] | -0.13 (with QQQ control — but QQQ beta +1.84) |

The pattern: validated cohorts have low or negative SPY beta because their factor is *independent* of broad market. The cohort identity is precisely what makes the basket distinct. Mag 7's failure mode is the inverse — high QQQ beta because Mag 7 IS QQQ, no separate factor.

---

## Per-cohort summary cards

### [[Sectors/WFE|WFE quartet]] (N=4, intra-corr 0.804)

The structural ceiling. Four oligopolists (ASML, AMAT, KLAC, LRCX) serving the same 3-4 leading-edge foundry customers on the same capex cycle. Constraints aren't replicable elsewhere in the vault. Use as the upper-bound reference — no thematic-basket cluster should be expected to reach 0.80+ intra-correlation because the constraint structure isn't replicable.

### [[Sectors/Korea Memory|Korea Memory]] (N=2, intra-corr 0.756)

Samsung + SK Hynix. Pair-only cohort — N=2 diagnostics are necessarily limited (no PC2/PC3 sub-structure, hierarchical clustering trivially groups the pair). The 0.756 reading is meaningful directionally but should be weighted appropriately given the small N.

### [[Sectors/US Memory|US Memory]] (N=3, intra-corr 0.696)

MU, SNDK, WDC. Tight cyclical memory cluster. Strong basic validation but no advanced patterns documented yet.

### [[Sectors/Crypto-to-AI|Crypto-to-AI]] (N=7, intra-corr 0.691)

The TIGHTEST N=7 cohort. Bitcoin miners pivoting to AI/HPC hosting. PC2 cleanly separates pure miners (MARA, CLSK, RIOT) from AI-pivot names (CORZ, HUT, WULF, IREN). IREN is the Swiss-Army-knife name. Cohort stable across 3Y/2Y/1Y/YTD (no regime shift). Identity formed in late 2023 with the AI capex flood and has been durable since.

### [[Space pure-plays]] (N=7, intra-corr 0.624)

THE CANONICAL REFERENCE for the framework. 19 analytical sections documenting basic validation + stability + the four follow-on patterns + cross-cohort comparison. Highest cohort-specific factor share (59.6%). Underwent a regime shift in Nov 2025 (PC2 collapsed from 21% to 8%, intra-corr jumped from 0.466 to 0.656). PL is the Swiss-Army-knife name.

### [[Sectors/AI Compute|AI Compute]] (N=3, intra-corr 0.600)

TSM + NVDA + AMD. Canonical AI trade but only N=3. Moderate cluster cohesion. Less coherent than Space pure-plays despite the "AI trade" framing — same trade-name doesn't mean same factor structure.

### [[Concepts/Defense primes basket|Defense primes 6-core]] (N=6, intra-corr 0.556)

LMT + RTX + NOC + GD + HII + LHX. 7-name variant (with LDOS) only partially validates; 6-name core is the clean cluster. PC2 isolates HII (single naval shipbuilder, no aerospace exposure) — single-outlier pattern, unlike the balanced 2-sleeve splits of other validated cohorts. RTX is the Swiss-Army-knife name. SPY beta -0.52 (controlling for ITA) — most insulated from broad market of any tested cohort.

### [[Concepts/Mag 7 cluster|Mag 7]] (N=7, intra-corr 0.316) — FALSIFIED

AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA. Below all three falsification thresholds: intra-corr below 0.50, PC1 below 50%, negative intra-advantage vs ETFs (-0.215). Essentially leveraged QQQ (R² 85.4% to broad benchmarks, only 14.6% specific factor). Cohort is loosening over time (0.47 → 0.32 over 3Y → YTD). Canonical reference for "what falsification looks like." Jun 2026 clean-null re-run: random-basket p = 0.0050/0.0106 (the old 0.010/0.027 was measured against a polluted pool) — the falsification rests on the holdout (0.44, REGIME-DEPENDENT) and zero-width threshold scan, not the permutation test; the OOS pass agrees (ratio 0.73, p = 0.051, PRELIMINARY OOS-WEAKENED).

### [[Sectors/UAS defense micro-cluster|UAS pair]] (N=2, intra-corr 0.678)

KTOS + AVAV. Real micro-cluster too small to be a full cohort. Current Jun. 3 validation tightened the pair to 0.678 trailing-1Y correlation; adding any of 6 tested defense-tech expansion candidates (MRCY, BWXT, HEI, etc.) still loosens the cluster rather than tightening. Standalone 2-name pair pending future expansion candidates (Karman Holdings KRMN, Anduril when public).

### [[Concepts/Boutique advisory consolidation|Boutique advisory consolidation]] (N=6, intra-corr 0.731)

PWP, LAZ, EVR, MC, HLI, PJT. Matched-methodology re-run completed 2026-06-10: intra-corr 0.731, PC1 77.70%, random-basket p at the 0.0001 floor, holdout STABLE (0.90) — the May 2025 published 0.73 figure held up almost exactly. The June OOS pass adds nuance: post-definition cohesion cooled to 0.530 (ratio 0.73, PRELIMINARY OOS-WEAKENED) while still beating random baskets at p = 0.0009 — the cohort is descending from its May 1 2026 sector-print cohesion peak, not fragmenting. Worth re-reading at the July pass. (The re-run also required repairing frozen PWP/LAZ/PJT price series — see the 2026-06-10 freshness audit.)

---

## Methodology notes

### Matched parameters

All cohorts re-run May 11 2026 with identical parameters for cross-cohort comparability:

- Window: 1-year daily returns through 2026-05-07
- Threshold: 0.5 for hierarchical clustering distance cut
- PCA: scikit-learn implementation, all components
- Factor decomposition: linear regression against relevant broad-market + thematic benchmarks
- Subset optimization: enumerate all C(N,2) pairs, rank by three objectives separately

Configs in `scripts/cluster_configs/`: `wfe_quartet.yaml`, `korea_memory.yaml`, `us_memory.yaml`, `crypto_to_ai.yaml`, `rklb.yaml`, `ai_compute.yaml`, `defense_primes.yaml`, `defense_primes_core.yaml`, `mag7.yaml`.

Cohort-specific full-analysis scripts: `mag7_full_analysis.py`, `crypto_to_ai_full_analysis.py`, `defense_primes_full_analysis.py`. Each runs stability + PC2/PC3 + factor decomposition + subset optimization + complement test in one pass.

### Verdict thresholds (per `docs/cluster-validation.md`)

| Diagnostic | Validated | Partial / Weak | Falsified |
|---|---|---|---|
| Intra-cluster correlation (avg) | ≥ 0.70 strong, 0.50-0.70 moderate | <0.50 (above 0.40) | <0.40 OR negative intra-advantage vs ETF |
| PC1 explained variance | ≥ 70% strong | 50-70% | <50% |
| Hierarchical clustering at 0.5 | Returns ≥ candidate cohort | Mixed: partial groupings | Singletons / mass-cluster with benchmarks |
| Cluster vs ETF intra-advantage | Positive (>+0.10 typical) | +0.00 to +0.10 | Negative |

Multi-dimensional verdict: a cohort passes all four for "validated," fails one or two for "partial," fails three or four for "falsified."

---

## Open questions / future cohort work

1. ~~Boutique advisory consolidation re-run~~ — DONE 2026-06-10: intra 0.731, PC1 77.70%, p floor; validated, see summary card.
2. ~~Hyperscalers re-run~~ — DONE 2026-06-09/10: falsification confirmed and now decisive at the permutation level on the clean null (p = 0.135 — cohesion indistinguishable from a random 5-pick); see [[AI hyperscalers]].
3. ~~Card networks~~ — DONE (registry 2026-05-13, re-graded 2026-06-10): V/MA pair intra 0.827, p = 0.0012, threshold-stable width 0.40 (widest tested); validated pair.
4. ~~Insurance brokers~~ — DONE: validated at full N=6 with intra 0.655 and p at the floor after the MRSH alias fix (the config had referenced Marsh McLennan's dead MMC ticker); OOS-STRENGTHENING (1.35).
5. ~~Mega banks~~ — DONE: intra 0.729, p at the floor; validated; OOS-CONFIRMED (0.95).
6. ~~Payments~~ — DONE: intra 0.395 — weak cohesion but p = 0.0006 (real, loose factor); OOS-STRENGTHENING (1.15). Not promoted to a validated callout.
7. ~~Foundry~~ — DONE: falsified (p = 0.328 clean-null; 0.207 intra). TSM has subordinates, not peers.
8. AI distillation wars — not yet tested as a cohort.
9. Brazilian banks (ITUB, BBD, NU) — could be useful for cross-vault analysis. DB-ready per the 2026-06-12 audit (ITUB, BBD, BSBR, NU, BPAC11.SA all ≥200 obs).
10. Chinese internet (BABA, JD, PDD, BIDU) — high-vol cohort like crypto miners; would test the framework outside US markets. DB-ready except 0700.HK and TME.
11. 2026-06-12 coverage audit — full sweep of securities notes × sector notes × theses against the configs' `cluster:` groups found 106 of 127 securities-note actors in no tested cohort, clustering into the following untested cohort-shaped structures (DB-ready = ≥200 obs in the 1Y window at audit date):
    - Thesis-backed (highest priority — conviction already on the books, boundary never tested): ~~nuclear/SMR (OKLO, SMR, NNE, LEU, CCJ, BWXT, UEC — [[Long nuclear]])~~ DONE 2026-06-13 — validated factor but ETF-replicable (see exploration log + [[Nuclear renaissance#Cluster validation]]); ~~European rearmament (RHM.DE, BA.L, LDO.MI, SAAB-B.ST, HO.PA, HAG.DE, KOG.OL)~~ DONE 2026-06-13 — validated distinct European factor (6-name core, +0.340 vs US primes; Kongsberg outlier); see exploration log + [[European rearmament#Cluster validation]]; hydrogen electrolyzers (PLUG, NEL.OL, ITM.L, BE, BLDP — three securities notes); China EV (NIO, XPEV, LI vs TSLA — [[Chinese EVs enter US]]; BYD/Geely HK lines need add_ticker or ADR aliases).
    - Sector-note-backed, DB-ready: ~~defense IT services (BAH, CACI, SAIC, LDOS)~~ DONE 2026-06-13 — validated as a distinct cluster (intra 0.604, +0.310 intra-advantage vs the primes), LDOS's confirmed home (see exploration log + [[Defense IT Services#Cluster validation]]); ~~exchanges (CME, ICE, NDAQ, CBOE — WFE-type ceiling candidate)~~ DONE 2026-06-13 — FALSIFIED (intra 0.360, zero threshold width): not one cluster — ICE/NDAQ trade with the data providers, CME/CBOE are a derivatives pair (see exploration log + [[Exchange operators]]); ~~medtech (MDT, BSX, ISRG, RMD, SYK, EW, ABT)~~ DONE 2026-06-14 — FALSIFIED (intra 0.348, PC1 44.8%, negative intra-advantage vs the sector ETFs): a sector label, not a factor — the names shatter into singletons (see [[Medtech#Cluster validation]]); ~~financial data/index providers (SPGI, MCO, MSCI, FDS, TRI, RELX, MORN)~~ DONE 2026-06-14 — VALIDATED (intra 0.607, +0.554 vs the CME/CBOE derivatives pair) and absorbs NDAQ + ICE, closing the [[Exchange operators]] loop (see [[Financial data providers#Cluster validation]]); IoT-module pair (Quectel 603236.SS / Fibocom 300638.SZ + SIVE.ST — micro-pair à la [[Sectors/UAS defense micro-cluster|UAS pair]]); ~~Brazil fintech (STNE, PAGS, NU, MELI, XP)~~ DONE 2026-06-14 — real cohort but NOT a separable factor (intra 0.570, holdout STABLE, yet negative intra-advantage vs the Brazilian banks): fintechs and incumbents trade as one Brazil-financials / EWZ factor; MELI the e-commerce outlier (see [[Brazil fintech#Cluster validation]]); ~~neoclouds (CRWV, NBIS, IREN, CIFR, APLD)~~ DONE 2026-06-14 — real cohort (intra 0.624, PC1 70%, passes all nulls incl. vol-matched) but NOT distinct from [[Sectors/Crypto-to-AI|Crypto-to-AI]] (+0.000 intra-advantage; miners contaminate from 0.35): the same AI-datacenter-buildout factor, with a CRWV/NBIS pure-cloud sleeve (see [[Neoclouds#Cluster validation]]).
    - Second tier, DB-ready: airlines (UAL, DAL, AAL, LUV, ALK); homebuilders (DHI, LEN, PHM, NVR); oil majors incl. PBR; cable/telecom distribution (CHTR, CMCSA, SATS, T, VZ, TMUS); sports betting (DKNG, FLUT, MGM, CZR); rare earths (MP, USAR, LYC.AX, TMC); GS+MS investment-bank pair (in no cluster group — mega banks is JPM/BAC/C/WFC/USB); stablecoin/crypto-fin extension (CRCL, GLXY onto the existing COIN/HOOD config).
    - Blocked on add_ticker: ~~AI optics/networking (LITE/ANET in DB; COHR, CIEN, CRDO, ALAB missing — notable given AI-infra coverage elsewhere)~~ DONE 2026-06-14 — NOT ONE COHORT: two sub-cohorts (optical COHR/CIEN → [[AI fiber supercycle]], interconnect-silicon CRDO/ALAB → [[Connectivity]]); passes cohesion nulls but zero threshold width + holdout WEAKENED; see [[AI interconnect#Cluster validation]]. Remaining: Japan semi materials ([[Long Japan photoresists]] / [[Long Japan wafers]] name cohorts at 1/4 DB coverage); DTC telehealth; title insurance; copper mining.
    - ~~Single-name boundary gap: MRVL absent from the fabless_semis `cluster:` group~~ DONE 2026-06-14 — MRVL added (it belongs as well as any member: PC1 loading 0.444, AVGO–MRVL 0.47 the custom-ASIC pair), but the 5-name re-run on a fresh window confirms the fabless cohort is REGIME-DEPENDENT (holdout 0.58, negative intra-advantage vs SMH/SOXX) — an AI-boom-era trade that has decoupled; QCOM is the real outlier. See exploration log + [[Short standalone ASICs]].

Items 1–7 were resolved by the May 13 registry batch and the June 9–10 clean-null re-grade; full per-cohort numbers in `scripts/cluster_registry.csv`. The framework is now tested on 34 logged cohorts and reproduces interpretable structural patterns reliably; items 8–11 remain genuinely open. The 2026-06-12 audit also closed four registry gaps (SEI, PAX, LION, STRZ had configs and embedded diagnostics but no statistical-suite rows) and added the [[AI SaaS Disruption]] basket — see the exploration log.

---

## Implications for trade construction

Based on the structural patterns above, the right expression of a cluster thesis depends on what the user wants:

| Goal | Expression | Example (Space pure-plays) |
|---|---|---|
| Maximum factor exposure with minimum names | Factor-tracking pair from subset optimization | LUNR + BKSY (0.94 tracking corr) |
| Maximum Sharpe ratio on the thesis | Sharpe-optimal pair (usually includes Swiss-Army-knife name) | RKLB + PL (Sharpe 2.03) |
| Maximum cumulative return | Return-maximizing pair (high-return names) | LUNR + PL (+254%) |
| Cleanest factor isolation (full basket) | Equal-weighted basket of all validated members | All 7 names |
| Hedge against the basket | Long benchmarks / Short basket pair | Long QQQ / Short Mag 7 (won't work because Mag 7 IS QQQ) |
| Pair-trade within cohort | Long PC2-positive sleeve / Short PC2-negative sleeve | Long data sleeve / Short hardware sleeve (Space pure-plays) |

The objective decomposition is the most consistently-useful pattern from this session. Future cohort analyses should explicitly enumerate all four (factor-tracking, Sharpe, return-max, complement) before recommending a position.

---

## Related

### Canonical references
- [[Cohort, cluster, basket]] — terminology glossary (the candidate vs the verdict vs the tradeable expression)
- [[Space pure-plays]] — 19-section worked example, all advanced patterns documented
- [[Concepts/Mag 7 cluster|Mag 7 cluster]] — canonical falsified-cluster example
- `docs/cluster-validation.md` — framework standard procedure

### Cohort notes referenced in this taxonomy
- [[Sectors/WFE|WFE]]
- [[Sectors/Korea Memory|Korea Memory]]
- [[Sectors/US Memory|US Memory]]
- [[Sectors/Crypto-to-AI|Crypto-to-AI]]
- [[Sectors/AI Compute|AI Compute]]
- [[Concepts/Defense primes basket|Defense primes basket]]
- [[Sectors/UAS defense micro-cluster|UAS defense micro-cluster]]
- [[Concepts/Boutique advisory consolidation|Boutique advisory consolidation]]

### Scripts
- `scripts/cluster_analysis.py` — basic validation (incl. weekly async-close cross-check as of Jun 2026)
- `scripts/cluster_permutation_test.py` — independence + random-basket + vol-matched nulls (clean stock-only pool, Phipson-Smyth)
- `scripts/cluster_holdout_test.py` — temporal train/test split (sign-aligned loadings)
- `scripts/cluster_threshold_scan.py` — threshold-stable range
- `scripts/cluster_registry.py` — cross-cohort log + Bonferroni/BH correction (`scripts/cluster_registry.csv`)
- `scripts/cluster_oos_validation.py` — post-definition out-of-sample pass (quarterly)
- `tests/cluster_statistics_tests.py` — 21 synthetic-data regression tests on the statistical layer
- `scripts/cluster_stability_check.py` — multi-window stability
- `scripts/cluster_deep_dive.py` — factor decomposition + PC2 + missing-name screen
- `scripts/cluster_subset_optimization.py` — optimal 2- and 3-name subsets
- `scripts/cohort_extras.py` — vol regime + drawdown
- `scripts/cohort_regime_and_events.py` — pre/post regime + event study
- `scripts/cohort_subset_robustness.py` — rolling robustness + complement
- `scripts/cohort_pc3_and_rates.py` — PC3 + rate sensitivity
- `scripts/may8_factor_decomposition.py` — single-day event study
- `scripts/chart_pc1_component.py` — PC1 factor index charts
- Cohort-specific full-analysis scripts: `mag7_full_analysis.py`, `crypto_to_ai_full_analysis.py`, `defense_primes_full_analysis.py`

*Created 2026-05-11 — synthesizing findings from 8-cohort framework application during May 10-11 sessions.*
