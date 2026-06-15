---
aliases: [Cluster validation capstone 2026-06-15, FDR OOS capstone]
tags: [report, cluster-validation, methodology, capstone]
---

# Cluster validation capstone — FDR + OOS (2026-06-15)

> [!summary] The campaign survives correction. Of 83 logged cohorts with a permutation p-value, 71 survive Benjamini-Hochberg FDR control and 43 survive the strict Bonferroni; with `uncorrected == BH == 71`, essentially none of the "validated" verdicts are multiple-testing artifacts. Out of sample, 29 of the 33 cohorts old enough to grade hold or strengthen post-definition; the overfit catches are three — [[Mag 7]] and [[Boutique advisory consolidation|Boutique advisory]] (OOS-weakened) and the Edge control-plane risk basket (OOS-failed). The one caveat that reframes everything below: this tests CO-MOVEMENT (the random-basket null), not DISTINCTNESS — many of the 71 survivors are ETF-replicable, which the threshold scan, not the FDR, adjudicates.

This is the cross-cohort close to the multi-week cluster-validation campaign — the multiple-testing correction and out-of-sample re-validation flagged quarterly in `CLAUDE.md`. It runs over `scripts/cluster_registry.csv` (136 rows, 100 unique cohorts; 83 carry a random-basket p-value) via `scripts/cluster_registry.py correction` and the accumulated `scripts/cluster_oos_validation.py` verdicts. Method and prior context: `docs/cluster-validation.md`, `docs/cluster-validation-audit-2026-06-09.md`, [[Vault cluster taxonomy]].

## 1. False Discovery Rate correction

Across 83 unique cohorts (deduplicated to the latest test per cohort, dropping rows without a random-basket p-value), at alpha 0.05:

| Threshold | Cutoff | Pass | Read |
|---|---|---|---|
| Uncorrected | p < 0.05 | 71 / 83 | Co-move more than a random basket |
| Benjamini-Hochberg (FDR) | p ≤ 0.0195 | 71 / 83 | FDR-controlled — same 71 |
| Bonferroni (strict) | p ≤ 0.000602 | 43 / 83 | Survive correction for all 83 tests |

The key number is that `uncorrected == BH == 71`: with the BH line landing at 0.0195 (the Exchange-operators row), every cohort that clears the naive 0.05 also clears FDR control, so roughly zero of the uncorrected passes are false discoveries. The campaign's "validated" stamps are not an artifact of running ~80 tests. The conservative Bonferroni (43 survivors) is dominated by the 33 cohorts pinned at the 0.0001 permutation floor plus 10 between 0.0002 and 0.0006 — these are the unambiguously cohesive cohorts ([[P&C insurance carriers basket|P&C insurers]], [[Mega banks basket|mega banks]], [[Space pure-plays]], [[Defense primes]], the commodity family [[Gold equity beta|gold]]/[[Uranium equity beta|uranium]]/[[Copper equity beta|copper]]/[[Oil and gas equity beta|oil]], [[Quantum computing]], [[Homebuilders]], [[Regulated utilities]], and more).

### The 12 that fail even uncorrected (false-discovery candidates)

| Cohort | p (random-basket) | Campaign verdict |
|---|---|---|
| [[Cybersecurity consolidation]] | 0.051 | borderline |
| [[Ad-tech]] | 0.051 | falsified (AppLovin decoupled) |
| Animal health | 0.065 | borderline |
| [[GLP-1 receptor agonists\|GLP-1 obesity]] | 0.076 | falsified (narrative, not factor) |
| [[Theatrical exhibition]] | 0.100 | falsified (3 idiosyncratic names) |
| [[DTC Telehealth]] | 0.107 | falsified (most fragmented in the campaign) |
| AI hyperscalers | 0.135 | label, not a tight factor |
| Premium subscription content | 0.157 | diffuse |
| Live sports and entertainment rights | 0.170 | falsified (TKO sector-orphan) |
| Studios & premium content | 0.274 | diffuse |
| [[IoT cellular modules]] | 0.277 | falsified (only the Quectel+Fibocom pair holds) |
| Foundry monopoly | 0.328 | TSMC-dominated (one name, not a cohort) |

These are exactly the cohorts the campaign falsified or flagged qualitatively — the FDR independently confirms they are not distinguishable from random baskets. No surprises; the statistics and the hand-built verdicts agree.

## 2. Out-of-sample (post-definition) re-validation

Of the 100 unique cohorts, 33 were defined early enough to have accumulated post-definition return history (≥15 obs). Their OOS verdicts:

| OOS verdict | Count | Read |
|---|---|---|
| OOS-STRENGTHENING | 18 | Tighter post-definition than in-sample |
| OOS-CONFIRMED | 11 | Holds post-definition |
| OOS-WEAKENED | 2 | [[Mag 7]], [[Boutique advisory consolidation\|Boutique advisory]] |
| OOS-FAILED | 1 | Edge control-plane risk basket (ECPR) |
| INSUFFICIENT_HISTORY | 1 | [[Global luxury candidate basket]] (7 obs) |

So 29 of the 31 gradeable cohorts hold or strengthen on truly unseen data — strong evidence the cohorts were not backfit to their definition window. The newest cohorts (this session and the concurrent ones — the commodity family, the two defensives, steel/aluminum, oil, casinos, sports betting) have only 1-2 days of post-definition data and will grade at the next quarterly pass.

## 3. The FDR × OOS cross — where the two disagree

The interesting cohorts are where in-sample and out-of-sample part ways:

- Pass FDR, fail OOS (the overfit catches): [[Mag 7]] (p 0.005 in-sample, OOS-WEAKENED — the seven mega-caps co-moved historically but have decohered as AI winners and laggards separated), [[Boutique advisory consolidation\|Boutique advisory]] (p 0.0001, OOS-WEAKENED), and ECPR (p 0.012, OOS-FAILED — the one cohort that looked real in-sample and broke out-of-sample). These three are the capstone's real value: statistically clean in-sample, yet not durable.
- Fail FDR, hold OOS (the ambiguous four): AI hyperscalers (p 0.135, OOS-CONFIRMED), Foundry monopoly (p 0.328, OOS-STRENGTHENING), Animal health (p 0.065, OOS-STRENGTHENING), [[Cybersecurity consolidation]] (p 0.051, OOS-STRENGTHENING). These co-move post-definition but were not distinguishable from random in-sample — typically because they are small, market-beta-dominated groups whose "cohesion" is just shared large-cap or sector beta that the post-definition window happened to amplify. Treat as unresolved, not validated.
- Pass both (the robust core): the bulk of the 29 OOS-holders that also clear FDR — [[Mega banks basket|mega banks]], [[Korea Memory]], [[Card networks duopoly|card networks]], [[Security control points]], [[Hyperscaler supplier chain]], [[Alternative asset managers basket]], and the rest. These are the cohorts that are both cohesive beyond chance and durable out of sample.

## 4. Caveats that reframe the counts

- This is the random-basket null, not the distinctness test. A cohort passing FDR co-moves more than a random N-pick — necessary, not sufficient. The campaign's most important finding, that most validated cohorts are ETF-replicable (the commodity family = its sector ETF, [[Mega banks basket|mega banks]] = XLF, [[Regulated utilities]] = XLU), lives entirely in the threshold scan and the intra-advantage-vs-ETF, which the FDR does not touch. Read "71 survive FDR" as "71 are real co-moving cohorts," not "71 distinct tradeable factors."
- 33 cohorts are pinned at the 0.0001 permutation floor. With 10,000 permutations the smallest reportable p-value is the Phipson-Smyth floor (~0.0001), so a third of the registry is tied at the floor and the correction cannot rank within it. This is the corrected state after the 2026-06-09 audit, which found the older n_perm=1000, p=0.0 rows anti-conservative; the dedup-to-latest in the correction keeps the 10k-perm rows.
- 17 sub-cohorts and one alias (AI Compute) carry no random-basket p-value and are excluded from the FDR. The sub-cohort robustness sweeps (Macau pair, megabank IB pair, tobacco UK/US pairs, lithium/steel/aluminum sub-groups, etc.) were graded by threshold-stable width, not permutation, so they are not in the 83.
- Tooling note: `cluster_registry.py correction` crashes on cp1252 stdout because the registry contains CJK cohort names (中特估); run it with `PYTHONIOENCODING=utf-8`. Worth fixing at the source (same class of bug as the permutation-script CJK crash fixed 2026-06-13).

## 5. Bottom line

The campaign holds up. After correcting for ~80 shots on goal, the validated cohorts are not multiple-testing luck — 71 of 83 survive FDR with essentially no false-discovery inflation, and the falsifications the campaign called by hand (GLP-1, theatrical exhibition, DTC telehealth, ad-tech, IoT modules) are exactly the cohorts that fail the correction. Out of sample, the cohorts old enough to grade overwhelmingly hold, and the three that do not — [[Mag 7]], [[Boutique advisory consolidation\|Boutique advisory]], ECPR — are now flagged for downgrade. The standing reminder for every "validated" stamp: the FDR certifies co-movement; distinctness from the sector ETF is a separate test, and on that test most of these cohorts are the ETF.

### Follow-ups
- Re-grade [[Mag 7]], [[Boutique advisory consolidation|Boutique advisory]], and ECPR (OOS deterioration) — consider status downgrades in their notes.
- Resolve the four FDR-fail / OOS-hold ambiguous cohorts (AI hyperscalers, Foundry monopoly, Animal health, Cybersecurity consolidation) at the next pass with more post-definition data.
- Next quarterly capstone: re-run once the 2026-06-14/15 cohorts (commodity family, defensives, steel/aluminum, oil) have ≥15 post-definition obs.

## Related
- [[Vault cluster taxonomy]] — the cross-cohort map and exploration log
- `docs/cluster-validation.md` — the Gate-11 framework
- `docs/cluster-validation-audit-2026-06-09.md` — the prior p-value audit
