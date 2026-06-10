---
aliases: [Cluster framework explainer, Cluster audit explainer]
tags: [report, explainer, methodology]
---
#report #explainer

# Cluster framework audit, remediation, and OOS pass — plain-language explainer

Companion to `docs/cluster-validation-audit-2026-06-09.md` (the technical audit) and `docs/cluster-validation.md` §Statistical falsification (the methodology). This is the narrative version, preserved from the June 9–10 2026 working sessions: what the cluster routine does, what was broken, what was fixed, and what the new out-of-sample pass adds. Written to be readable without prior vault context.

## Part 1 — The audit and the fix

### What the tool does

The vault has a routine that answers one question: do these stocks actually move together as a pack, or did we just imagine a pattern? Seven space companies jump on the same day — are they a real pack, like [[Space pure-plays]], where the group behaves as one animal? Or seven unrelated companies that happened to have a good day?

You can't eyeball it, because on a good day everything goes up. So the tool plays a luck game: it deals thousands of random hands of stocks from the database, measures how in-sync each random hand is, and asks whether the proposed group is more cohesive than 99.9% of random hands. If random hands look just as coordinated, the pattern was luck. Everything depends on that deck of random stocks being fair.

### What was broken

The deck was contaminated. The database had 1,250 tickers with no label saying what they were, and the tool dealt all of them. The random-stock deck secretly contained 105 currency exchange rates, 48 cryptocurrencies, two dozen market indices (including the vault's own synthetic ones), ETFs, and foreign listings whose exchanges close at different hours. It was like testing whether seven friends are a real soccer team by comparing them against random groups drawn from a crowd that includes toddlers — who barely coordinate, making the team look like champions — and Olympic synchronized swimmers (the cryptos, which move in lockstep), who set a bar almost nobody can beat.

Smaller defects on top: the tool could report a 0% chance of luck, which is mathematically impossible from a 1,000-shuffle test (the honest minimum is 1-in-1,001); a missing stock was silently dropped so a six-name team could be graded while the report claimed seven; one helper script read from a stale copy of the prices; and a calendar bug gave the team one extra trading day the random hands never saw.

### What was fixed (June 9–10 2026)

A new script asked the market-data source what each of the 1,250 unlabeled tickers actually is and saved the answers (830 stocks, 230 ETFs, 105 currencies, 48 cryptos, 17 indices). The tool now deals only from real, US-listed common stocks — a clean deck of about 920. The probability math was corrected so 0% is impossible (Phipson-Smyth: floor 1-in-10,001 at 10,000 shuffles), shuffles went from 1,000 to 10,000, missing stocks now trigger loud warnings, and the calendar and stale-data defects were repaired.

### What the re-grade showed

All 34 stock-packs ever certified were re-graded against the fair deck. The headline: 20 of 34 pass the strictest statistical bar (Bonferroni), 30 of 34 pass the standard false-discovery control (Benjamini-Hochberg), and the only four failing outright — Foundry monopoly, [[AI hyperscalers]], [[Cybersecurity consolidation]], and an animal-health screen — had already been called falsified or were never promoted to notes. No previously certified pack lost its certification, which says the framework's redundancy worked: when one diagnostic was silently broken, the other three carried the verdicts.

The interesting twist: the rigged deck had distorted scores in both directions, split by group size. Small packs had faced an unfairly high bar, because random hands occasionally came up all-crypto — an unbeatable synchronized-swimmer squad ([[AI Compute]] improved from p 0.023 to 0.0026 on the fair deck, [[Korea Memory]] from 0.006 to 0.0031). Weak mid-size packs had slid under an unfairly low bar, because currencies and macro series dragged the random hands' coordination down ([[AI hyperscalers]] went from a passing 0.028 to a decisive failing 0.135).

## Part 2 — The out-of-sample pass (what it does and why)

### The hole it closes

Every pack in the registry exists because it had already moved together — the space cohort's own config file says it was proposed because of the May 8 2026 basket rally. All four older diagnostics then run on windows containing that very move: the holdout splits inside it, the permutation test resamples across it, the threshold scan re-cuts it. That is selection on the dependent variable — testing a pattern on the data that made you see the pattern. Every result is flattered by construction, and no amount of in-sample rigor fixes it. It is the cluster-validation version of the backtest sin.

### The mechanism

`scripts/cluster_oos_validation.py` exploits something the repo provides for free: git records exactly when each cohort's membership was frozen — the day its config file was first committed. That is a tamper-proof definition date (May 3 2026 for the big screening batch, May 10 for space, May 28 for luxury). Everything the market printed after that date is data nobody had seen when the boundary was drawn. Per cohort the script:

1. Recomputes the in-sample baseline — intra-correlation on the trailing year ending at the definition date.
2. Computes the same statistics on returns strictly after it (even the discovery day itself is excluded).
3. Grades the ratio of out-of-sample to in-sample cohesion: at or above 1.10 is OOS-STRENGTHENING, 0.85–1.10 OOS-CONFIRMED, 0.60–0.85 OOS-WEAKENED, below 0.60 OOS-FAILED.
4. Runs the random-basket null on the same out-of-sample window against the cleaned stock pool.

The fourth step matters because the ratio alone has a blind spot: in a market-wide correlation spike, every group's cohesion rises, including dead ones. The ratio asks whether the cohort kept its own cohesion; the out-of-sample p-value asks whether it is still more cohesive than random stocks over those exact same days. The permutation comparison stays valid even on a 19-day window — the null baskets suffer the identical short, noisy window — it just has less power, which is why anything under 40 observations carries a PRELIMINARY prefix and under 15 reports INSUFFICIENT_HISTORY.

### What it changes structurally

Results merge into `scripts/cluster_registry.csv` (new `definition_date` and `oos_*` columns), so the registry stops being a one-shot validation log and becomes a forward ledger: every cohort carries a frozen birth date and accumulates a track record against data that postdates it. The pass runs quarterly alongside the FDR correction; verdicts harden as history accrues, and vault status callouts only cite an OOS verdict once it sheds PRELIMINARY (about 40 observations — early July 2026 for the May 3 batch).

The first reading showed the shape of the output: [[Space pure-plays]], defined May 10, had 19 unseen trading days — out-of-sample intra-correlation 0.671 against 0.563 in-sample (ratio 1.19, strengthening), beating random baskets at p = 0.0005. Preliminary, but it is the first number in the vault that discovery bias literally cannot have manufactured: you cannot cherry-pick data that did not exist yet.

## Related

- `docs/cluster-validation-audit-2026-06-09.md` — the technical audit with file:line findings and the remediation log
- `docs/cluster-validation.md` — the methodology standard, including §5 Post-definition out-of-sample re-validation
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Space pure-plays]] — canonical validated cluster; [[Mag 7 cluster]] — canonical falsified cluster
- [[Korea Memory]], [[US Memory]], [[AI hyperscalers]], [[Cybersecurity consolidation]] — callouts re-validated June 10 2026
