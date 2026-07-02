---
aliases: [Cluster validation capstone 2026-07-01, July 2026 capstone, FDR OOS boundary capstone]
tags: [report, cluster-validation, methodology, capstone]
---

# Cluster validation capstone — clean pool, FDR, OOS, boundary sweeps (2026-07-01/02)

> [!summary] The July capstone ran early on a repaired foundation and rewrote the evidence, not the verdicts. The null pool was purged of 234 mislabeled funds/ETFs/FX series (authorized metadata fix; the DB-default pool now equals the two-pass Yahoo-verified 1,061-name universe exactly), and on the honest placebo 110 of 114 cohorts pass FDR with `uncorrected == BH` — co-movement is nearly universal, so distinctness is the only discriminating question left. Eight of the twelve June "pure dispersion" falsifications flipped to null-passes without a single verdict overturning (they re-grade to shared-beta co-movement). Out of sample at 40 observations: [[Edge control-plane risk basket|ECPR]] is formally falsified (intra 0.468 → 0.042, the framework's first OOS kill), [[Boutique advisory consolidation|Boutique advisory]] is formally OOS-WEAKENED but real, and [[Mag 7 cluster|Mag 7]]'s planned demotion reversed — OOS-CONFIRMED as a weak stable beta, still falsified as a factor. The new full-universe boundary sweep graded all 41 separable cohorts: 21 CLEAN, 16 PERMEABLE, 4 CONTAMINATED — with [[TPG]] discovered sitting inside the [[Alternative asset managers basket|alt-managers]] envelope, a literal missing member found by machine.

This closes the quarterly FDR + OOS pass flagged in `CLAUDE.md`, brought forward from ~July 7 by the 2026-07-01 hardening session ("do all"). Method and prior context: `docs/cluster-validation.md`, `docs/cluster-validation-audit-2026-06-09.md` (2026-07-01 closure entry), [[2026-06-15-cluster-validation-capstone|June capstone]], [[Vault cluster taxonomy]]. Registry: `scripts/cluster_registry.csv` (198 rows after this pass; 114 unique cohorts carry a random-basket p-value).

## 0. The foundation repair that reframes everything below

The random-basket null pool — advertised since the June audit as "US-listed common stocks only" — was still carrying 152 non-stocks: 84 ETFs (including [[SPY]] itself and ARKX, the ARK Space ETF), 66 mutual funds, and 2 FX pairs, all typed `stock` in `ticker_metadata` because `add_ticker.py` defaults inserts to that label and the June 10 backfill was NULL-only by design. The leak was found by the new boundary sweep's first live run, which returned the space cohort's nearest "peer" as an ETF that literally holds the cohort.

The authorized fix (2026-07-01): a two-pass-confirmed `--verify` mode on `backfill_ticker_types.py` corrected 234 rows across the full metadata table (the pool-visible 152 plus mislabeled rows outside the current window), plus five internal synthetic series labeled by hand. Post-fix the DB-default pool and the two-pass Yahoo-verified snapshot (`scripts/universes/us_common_stocks.txt`, 1,061 names) are identical sets. Pattern guards in `is_us_common_stock_ticker` now reject Yahoo FX pairs (`=X`) and five-letter-ending-X mutual-fund tickers permanently.

Direction of the old bias: funds are internally diversified, so fund-bearing random baskets are more cohesive than honest ones — the polluted null was conservative for validations and anti-conservative for falsifications. Every verdict below is measured against the clean pool.

## 1. FDR over the clean pool

Across 114 unique cohorts (deduplicated to each cohort's latest p-carrying row — the `latest_p_rows` fix; see caveats), at alpha 0.05:

| Threshold | Pass | Read |
|---|---|---|
| Uncorrected (p < 0.05) | 110 / 114 | Co-move more than a random basket |
| Benjamini-Hochberg (FDR) | 110 / 114 | Same 110 — zero expected false discoveries |
| Bonferroni (strict) | 58 / 114 | Survive family-wise correction |

`uncorrected == BH` again: none of the passes are multiple-testing artifacts. The new n_perm adequacy audit (Phipson-Smyth floor vs the current Bonferroni cutoff) reports every row's resolution adequate; the 8 under-resolved rows found on 2026-07-01 (one at 1k permutations, seven at 4k/5k) were re-run at the 10k standard before this correction.

### The clean-pool re-grade of the 12 June failers

The June capstone's "12 that fail even uncorrected" were measured against the fund-inflated null. Re-run at 10k permutations on the clean pool:

| Cohort | June p | Clean-pool p | Re-grade |
|---|---|---|---|
| [[Cybersecurity consolidation]] | 0.051 | 0.0081 | flips — grade-2 (shared software beta) |
| [[Ad-tech]] | 0.0515 | 0.019 | flips — grade-2 (digital-ad/growth beta) |
| Animal health | 0.065 | 0.0125 | flips — grade-2 |
| [[GLP-1 receptor agonists\|GLP-1 obesity]] | 0.076 | 0.039 | flips marginally — [[Medtech]]-shape |
| [[Theatrical exhibition]] | 0.100 | 0.036 | flips thinly — shared consumer beta |
| [[Grocers]] | 0.106 | 0.036 | flips thinly — grade-2 |
| [[DTC Telehealth]] | 0.107 | 0.033 | flips thinly — high-beta-growth trade |
| [[AI hyperscalers]] | 0.135 | 0.031 | flips — grade-2, OOS-strengthening |
| Premium subscription content | 0.157 | 0.130 | still fails — pure dispersion |
| [[Wireless module chokepoints\|IoT cellular modules]] | 0.277 | 0.157 | still fails — Sivers dilution |
| [[Foundry monopoly consolidation\|Foundry monopoly]] | 0.328 | 0.159 | still fails — TSMC has no peers |
| Studios & premium content | 0.274 | 0.239 | still fails — pure dispersion |

Not one falsification-as-basket was overturned: the verdicts rest on singleton dendrograms, negative intra-advantages versus the owning ETFs, and zero threshold widths, none of which a pool fix touches. What changed is the honest grade — two-thirds of the falsified set co-moves via shared sector/risk beta rather than not at all. All eight flipped owner notes had their evidentiary basis corrected in place.

## 2. Out of sample — the formal verdicts

The quarterly OOS pass graded 161 cohorts (129 INSUFFICIENT_HISTORY — the June-defined wave is 1-2 weeks short of the 15-obs bar). Among graded cohorts: 18 PRELIMINARY OOS-STRENGTHENING, 11 PRELIMINARY OOS-CONFIRMED, 1 non-preliminary OOS-STRENGTHENING, 1 OOS-WEAKENED, 2 OOS-FAILED. After the July-1 close pushed the May-3 batch to exactly 40 observations, four cohorts were re-graded formally (non-preliminary):

| Cohort | In-sample intra | OOS intra | Ratio | p_oos | Formal verdict |
|---|---|---|---|---|---|
| [[Mag 7 cluster\|Mag 7]] | 0.310 | 0.331 | 1.06 | 0.0021 | OOS-CONFIRMED |
| [[Edge control-plane risk basket\|ECPR]] | 0.468 | 0.042 | 0.085 | 0.588 | OOS-FAILED |
| [[Boutique advisory consolidation\|Boutique advisory]] | 0.724 | 0.581 | 0.79 | 0.0001 | OOS-WEAKENED |
| [[AI hyperscalers]] | 0.262 | 0.385 | 1.44 | 0.0031 | OOS-STRENGTHENING |

- ECPR is the framework's first formal out-of-sample falsification, and it is total: post-definition cohesion is statistically zero and random baskets beat the cohort on 59% of draws. Callout downgraded to [!failure]. The cohort passed every in-sample test before dying on unseen data — the discovery-bias failure mode, caught by the one test built for it.
- Mag 7 is the honest reversal: June's preliminary OOS-WEAKENED ("the seven continue to decohere") did not survive sixteen more sessions. The formal verdict is weak, stable co-movement — exactly what "essentially leveraged QQQ" predicts. Falsified as a factor, confirmed as a beta; the note now says so.
- Boutique advisory cools from its May-1 print-event peak toward a structural resting level while rejecting the clean null at the floor — a validated cluster descending, not dissolving.
- AI hyperscalers resolves the June FDR-fail/OOS-hold ambiguity as grade-2: a real, strengthening, shared-AI-beta co-movement that is still not a five-name factor.

Also settled or newly flagged: Indian metals — the June watchlist worry (loosening on fresh data) — reversed to a full non-preliminary OOS-STRENGTHENING (ratio 1.40, intra 0.431 → 0.601); [[Global luxury candidate basket]] is the new deterioration watch, PRELIMINARY OOS-FAILED at 21 obs (ratio 0.55). Foundry (35 obs), Cybersecurity consolidation (39), and Animal health (37) cross the 40-obs bar ~July 8 and finalize then; all three currently read PRELIMINARY OOS-STRENGTHENING, consistent with their grade-2 re-grades.

## 3. Full-universe boundary sweeps — the separability claims, market-tested

The new market-relative boundary test (`cluster_boundary_sweep.py`, closing 2026-06-09 audit finding 3) swept all 41 cohorts with a separability claim against the verified 1,061-name pool: for every stock in the market, the average-linkage join distance to the cohort, graded against the config threshold and the cohort's own internal envelope.

| Verdict | Count | Meaning |
|---|---|---|
| BOUNDARY-CLEAN | 21 | No stock in the pool joins below the cut — the boundary is market-relative fact |
| BOUNDARY-PERMEABLE | 16 | Outsiders join at the cut but none breach the envelope — separability holds at tighter cuts |
| BOUNDARY-CONTAMINATED | 4 | Outsider(s) closer than the cohort's own loosest member — the config is wrong as drawn |

The four CONTAMINATED are the sweep's first discoveries, each a specific, checkable claim:

- [[Alternative asset managers basket]]: [[TPG]] sits inside the envelope at distance 0.243, with [[Carlyle|CG]] (0.291) below the cut — two literal alternative asset managers the config never included. Missing members found by machine; the cohort should be re-validated with them added.
- P&C insurance carriers: [[Arch Capital|ACGL]] (0.334), Loews, and [[Axis Capital|AXS]] breach the envelope — the specialty/reinsurance boundary blurs into the carrier cohort.
- Defense primes (7-name): [[Kratos|KTOS]] sits inside the 7-name envelope while the core-6 variant scans CLEAN — the seventh name loosens the envelope enough to admit defense-tech.
- IT services: 35 names "inside the envelope" is a known-outlier artifact — [[Wipro]] joins the candidate tree so late that the envelope covers half the market; the ex-Wipro sub-core reads PERMEABLE with 6. Rule: an envelope inflated by a known outlier is not a boundary.

The CLEAN column is the campaign's treasure list, now market-verified: [[Tankers]] (nearest outsider in the entire pool at distance 0.778 — the most isolated cohort in the vault), [[Korea Memory]] (0.759), [[Coal miners]] (0.705), [[Cable broadband]] (0.635), [[Title Insurance|title trio]] (0.601), [[Card networks duopoly|card networks]] (0.453), the [[Defense primes basket|core-6 defense primes]], [[Data center REITs|DC REITs]], [[Grain processors]], [[Insurance brokers basket|insurance brokers]], [[European rearmament]], [[Alcohol and spirits]], [[AI-power IPPs]], and the China cohorts (async-approximate). No stock in the market comes near these groups: their boundaries are facts, not config choices.

PERMEABLE nuances worth keeping: [[Quantum computing]] (38 below the cut, led by Arqit at 0.260 — itself a quantum name and missing-member candidate, then the nuclear/speculative complex) maps the retail-momentum super-cluster; [[Construction aggregates]] (19 below its loose 0.40 cut, zero inside the 0.12 envelope) stays an isolated pair — permeability at a loose cut is not contamination when the envelope is tight; [[WFE]] (45 below, MKSI/MPWR/ENTG nearest) is confirmed embedded in the semi complex, with its owners named.

## 4. Caveats that scope the counts

- Counts are not comparable to the June capstone's 83/71/43. Three things moved: the registry grew (83 → 114 p-carrying cohorts), the `latest_p_rows` fix repaired an eclipse bug that had been silently dropping cohorts whose newest row was a partial diagnostic (the June 83 was itself mildly understated), and the pool was cleaned.
- Permutation p-values are pool-vintage-relative. The eligible pool grew 1,121 → 1,213 names between June 23 and July 1 (before the fund purge cut it to 1,061); borderline p-values moved 2.7-6x on pool composition alone. The registry stores each p as measured; cross-vintage comparisons need this footnote.
- Pool size is window-vintage-dependent: ~370 eligible names for windows ending April 2026 versus ~1,062 for June windows, because ~700 campaign-era tickers carry only about a year of backfilled history. Old-window configs face thinner (valid, lower-powered) nulls.
- The June-defined cohort wave (commodity-beta family, defensives, steel/aluminum, coal, cannabis, and the rest) is 1-2 weeks short of its first OOS grades; they land mid-July. Vol-matched nulls were not re-run this pass; cited vol-matched figures remain June-vintage.
- Non-US cohorts' sweeps are approximate (US-synchronous pool; join distances async-overstated) — their CLEAN verdicts are directionally safe for exactly that reason.

## 5. Bottom line

The framework survived its own audit twice over. The placebo was rebuilt honestly, and on the honest placebo the discriminating question is no longer "is the co-movement real" (it almost always is — 110 of 114) but "who owns the factor" — an ETF, a parent complex, or the cohort itself. The distinctness layer now has a market-relative instrument, and its first full pass confirmed 21 boundaries as facts, demoted 4 configs as drawn, and found two missing members by name. Out of sample, the one cohort that ever fully failed unseen data is now formally falsified, the Mag 7 demotion reversed into something more precise than either verdict ("a beta, not a factor"), and the campaign's validated core — the ~dozen distinct cohorts no ETF replicates, with [[Tankers]], [[Coal miners]], [[Cable broadband]], [[Construction aggregates]], and the [[Card networks duopoly]] at the head — is unchanged and now stands on the strictest evidence the framework has ever produced.

### Follow-ups
- ~Jul 8: finalize Foundry / Cybersecurity consolidation / Animal health OOS verdicts at 40 obs.
- ~Mid-Jul: first OOS grades for the June-defined wave; grade [[Global luxury candidate basket]] (OOS-FAILED watch).
- Re-validate [[Alternative asset managers basket]] with [[TPG]] (+ [[Carlyle|CG]]) added; revisit the P&C carriers boundary vs specialty/reinsurance.
- Next full quarterly capstone: ~October 2026.

## Related
- [[2026-06-15-cluster-validation-capstone]] — the June capstone this pass supersedes
- [[Vault cluster taxonomy]] — cross-cohort map; exploration-log rows 2026-07-01/02
- `docs/cluster-validation.md` — the framework, including the boundary sweep (§6)
- `docs/cluster-validation-audit-2026-06-09.md` — audit + the 2026-07-01 closure entry
- `investing/attachments/cluster-oos-validation-2026-07-02.txt` — full OOS table
