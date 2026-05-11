# Cluster validation — standard for public actor notes

For every public-company actor note, the "where does this name actually trade" question must be answered mathematically, not by analogy. The procedure produces a single-page validation that confirms (or refutes) the actor's peer cluster, identifies its nearest neighbors in correlation space, and quantifies how single-factor the cluster is.

This is the rigorous version of the existing `## Sector correlation` section, which only correlates the actor against 3-4 ETFs. Cluster validation extends that to a candidate peer cohort + adjacent-sector controls + broad-market benchmarks, and runs three diagnostics.

---

## When to run

Required:
- Every new public-company actor note created with a securities companion (`investing/Assets/{Name} securities.md`).
- Every existing public-company actor note when it is materially expanded (e.g., a quarterly earnings ingestion that adds >100 lines, or a strategic re-classification).
- Every concept note that names a peer cluster (e.g., [[Boutique advisory consolidation]], [[AI SaaS Disruption]], [[Hyperscaler capex]]).

Optional but useful:
- After a major sector shock (e.g., the May 1 2026 boutique-advisory print), to test whether cluster cohesion held or broke.
- When evaluating whether a new ticker belongs to an existing cluster (add it to the candidate list, re-run, check whether the dendrogram includes it below the threshold).

Skip:
- Private companies (no return data).
- ETF or index notes (the ETF *is* the cluster).
- Country / region / sector hub notes (different concept; use `add_sector_correlations.py`).

---

## How to run

Each cluster is defined by a YAML config in `scripts/cluster_configs/{name}.yaml`. The config specifies the candidate cohort (always group `cluster`) plus adjacent-sector control groups. See `scripts/cluster_configs/boutique_advisory.yaml` for the canonical example.

```bash
# Validate an existing cluster
python scripts/cluster_analysis.py --config scripts/cluster_configs/boutique_advisory.yaml

# Validate by primary actor (auto-loads scripts/cluster_configs/{ticker}.yaml)
python scripts/cluster_analysis.py --primary PWP

# Override threshold or output prefix
python scripts/cluster_analysis.py --primary PWP --threshold 0.35 --prefix pwp-tighter
```

Outputs land in `investing/attachments/`:

| File | Content |
|---|---|
| `{prefix}-correlation-1y.png` | Pairwise return-correlation heatmap, 1-year window |
| `{prefix}-correlation-2y.png` | Same, 2-year window (stability check) |
| `{prefix}-dendrogram-1y.png` | Hierarchical clustering tree with cut threshold |
| `{prefix}-pca-1y.png` | PCA scree + PC1 loadings on the candidate cohort |
| `{prefix}-results.txt` | Plain-text summary of all numerics |

---

## Designing the YAML config

The config is the entire model — get it right and the validation is meaningful, get it wrong and the math is precise but pointless.

```yaml
name: Boutique advisory               # human-readable label for the cluster
primary: PWP                          # primary actor whose note hosts the analysis (optional)
prefix: boutique-cluster              # output filename stem (defaults to {primary}-cluster)
threshold: 0.4                        # dendrogram cut on 1-|corr| distance
window_end: 2026-04-30                # optional; latest weekday if omitted

groups:
  cluster:                            # REQUIRED group name; the candidate cohort being tested
    color: "#2962FF"
    tickers: [PWP, LAZ, EVR, MC, HLI, PJT]
  bulge:                              # adjacent-sector controls (1-3 of these typical)
    color: "#000000"
    tickers: [GS, MS, JPM]
  ins_brk:                            # most-distant comparator (sanity check that the cluster is distinctive)
    color: "#26A69A"
    tickers: [AON, AJG, BRO]
  etf:                                # ALWAYS include 3-4 broad benchmarks
    color: "#9E9E9E"
    tickers: [XLF, KBE, IWM, SPY]
```

### Choosing groups

Three principles:

1. The `cluster` group must be the smallest plausible candidate cohort. Don't pre-include every name you suspect belongs — the whole point is to test the boundary. If in doubt, leave a candidate out and let the dendrogram tell you whether it belongs (it will appear in the same hierarchical cluster if it does).

2. Include 2-3 adjacent-sector control groups, not the whole financial system. Each adjacent group answers a specific question: "is the cluster really distinct from X?" For boutique advisory, the relevant questions were: distinct from bulge brackets? from mid-IBs? from asset managers? from insurance brokers? If you include 8 groups the heatmap becomes unreadable; if you include 0 there is nothing to test against.

3. Always include broad ETFs (XLF/SPY for US financials, IWM for small-cap, sector-specific ETFs as appropriate). The cluster's correlation to broad benchmarks tells you how much of the move is generic risk-on/risk-off vs cluster-specific.

### Choosing the threshold

The 1-|corr| distance threshold defaults to 0.4. Members with pairwise distance below the threshold are bundled into one cluster. Empirically:

- 0.3 = correlation > 0.7 required for cluster membership. Tight cluster definition. Use for highly cohesive cohorts (e.g., the same business in different jurisdictions: US/UK/EU regional banks).
- 0.4 = correlation > 0.6 required. Default. Picks up coherent industry sub-sectors that share a single dominant factor.
- 0.5 = correlation > 0.5 required. Loose cluster definition. Use only if the cohort is structurally noisy (e.g., specialty pharma, where idiosyncratic clinical-trial outcomes dominate).

Run with the default first, then tune if the dendrogram returns a single mega-cluster (threshold too loose) or all-singletons (threshold too tight).

---

## Interpreting the output

The `results.txt` file has five sections. Read in order:

### 1. Intra-cluster correlations

```
--- 1Y INTRA-CLUSTER PAIRWISE CORRELATIONS ---
Average intra-cluster correlation: 0.727
Range: [0.605, 0.887]
```

- >0.7 average = strong cluster cohesion. The names trade together.
- 0.5-0.7 = moderate cohesion. Real cluster, but with idiosyncratic dispersion. Common for cohorts with one or two outlier business models.
- <0.5 = weak cohesion. The candidate cohort is not actually a cluster; the names are loosely related by taxonomy but not by market behavior.

If the *range* is wide (e.g., 0.3-0.9), one or more candidates is an outlier — check the dendrogram to see which.

### 2. Group-pair correlations

```
--- AVG GROUP-PAIR CORRELATIONS (1Y) ---
Cluster vs others:
  cluster vs alt_mgr   : 0.591  (intra advantage: +0.135)
  cluster vs bulge     : 0.559  (intra advantage: +0.168)
  cluster vs ins_brk   : 0.128  (intra advantage: +0.598)
```

The "intra advantage" is the gap between the intra-cluster average and the cluster-vs-group average. It quantifies how distinctive the cluster is from each comparator:

- +0.30 or more = clearly distinct. The cluster has a real cohesion factor not shared with this group.
- +0.10 to +0.30 = moderately distinct. The cluster shares systematic factor exposure with this group but adds something specific.
- <+0.10 = not distinct. The cluster moves with this group; the candidate cohort does not deserve a separate identity.

If *every* comparator shows <0.10 intra advantage, the candidate cluster is probably just a slice of the comparator group. Re-think the boundary.

### 3. Hierarchical clustering

```
--- HIERARCHICAL CLUSTERS (1Y, distance threshold 0.4) ---
  Cluster 4: PWP, LAZ, EVR, MC, HLI, PJT
```

This is the boundary test. The algorithm has no prior label about which names you proposed — it groups purely on return distance. If the algorithm-discovered cluster matches your proposed cohort exactly, the boundary is mathematically validated. If it doesn't:

- Algorithm includes names you didn't propose → those names belong; add them.
- Algorithm splits your proposed cohort → the cohort is two sub-clusters; either tighten the definition or treat it as two clusters.
- Algorithm merges your cohort with a comparator group → your cohort is not distinct from that comparator at this threshold; either tighten threshold (0.3) or accept that it is a sub-cluster of the larger group.

### 4. PCA on the candidate cohort

```
--- PCA ON CANDIDATE COHORT (1Y) ---
Explained variance ratio:
  PC1: 77.47%
PC1 loadings: PWP 0.397, LAZ 0.398, EVR 0.429, MC 0.433, HLI 0.381, PJT 0.409
```

PC1 explained variance answers "how single-factor is this cluster?":

- >70% = single-factor cohort. Equal-weighted basket ≈ PC1. Useful for pair trades and event analysis.
- 50-70% = dominant-factor cohort with meaningful sub-structure. PC2/PC3 may identify a within-cluster business-model split worth flagging.
- <50% = multi-factor cohort. The candidate cluster has at least two distinct trading regimes; the cluster validation is weaker.

PC1 loadings should all be positive and roughly equal. If they aren't (one name negative, or one name dramatically larger than others), that name has a different return profile from the rest — flag it as a candidate outlier.

### 5. Conclusions to draft

For the actor note, condense the output into a 5-row summary table + one paragraph. See `investing/Concepts/Boutique advisory consolidation.md` for the canonical write-up format.

---

## Stability check across windows

The 1Y window is the primary diagnostic, but a cluster that is tight on 1Y may have been loose on 2Y or 3Y — or vice versa. The direction of travel matters:

- A cluster that has been tightening over time (intra-corr rising as window narrows) is consolidating as a tradeable factor — basket-level flows are increasingly dominating single-name fundamentals. May 8 2026 [[Space pure-plays]] is the canonical example: 0.48 (3Y) → 0.55 (2Y) → 0.61 (1Y) → 0.64 (YTD).
- A cluster that has been loosening over time is fragmenting. The historical cohort identity may no longer apply; consider whether the cohort taxonomy needs to be re-cut.
- A cluster that is stable across windows is a structurally durable factor. The cohort definition is correct and the trading regime hasn't shifted.

Run via `python scripts/cluster_stability_check.py` (defaults to the [[Space pure-plays]] cohort; edit `COHORT` constant for other clusters, or generalize the script as needed). Produces a single table:

```
Window         obs   intra          range     PC1     PC2   vs def     gap
--------------------------------------------------------------------------------
YTD 2026        65   0.636 [0.51,0.78]   69.3%    8.3%    0.270  +0.365
1Y             135   0.607 [0.50,0.75]   66.6%    8.8%    0.241  +0.365
2Y             180   0.551 [0.29,0.74]   60.4%   14.7%    0.242  +0.309
3Y             263   0.482 [0.26,0.60]   54.8%   14.1%    0.218  +0.263
```

The "vs def" column is the cross-correlation between the cohort and a single representative control group (typically the most-relevant adjacent sector — defense primes for space, mid-IBs for boutique advisory, etc.). The "gap" column is the intra-cluster advantage over that control. A stable or widening gap across windows is the cleanest evidence that the cluster has a durable identity distinct from its nearest neighbor.

Embed the stability table in the cohort concept note (not the per-actor notes) as a sub-section under `## Cluster validation`.

---

## Advanced diagnostics — four follow-on patterns

The basic cluster validation answers "is this a real cluster?" The follow-on diagnostics below answer deeper questions about cluster structure and behavior. Each is a reusable pattern that should be considered when a cluster has been validated and merits deeper analysis. All four patterns are documented working examples in [[Space pure-plays]] (May 2026).

### Pattern 1: Pre/post regime split

When a cluster's rolling PC1 explained variance shows a step-function shift in time, the right follow-up is to re-run the full validation diagnostic on the pre- and post-shift windows separately. Quantifies the structural change instead of leaving it as a visual observation.

Procedure:
1. Identify the regime-shift date from the rolling PC1 chart (per the Stability section above).
2. Run `cluster_analysis.py` or equivalent on the pre-shift window (e.g., Nov 2024 - Oct 2025 for the Nov 2025 Space pure-plays regime shift) and the post-shift window (Dec 2025 - May 2026) separately.
3. Compare intra-correlation, PC1 variance, PC2 variance, and pairwise-correlation floor between the two windows.

What to look for:
- Intra-correlation lifting (e.g., 0.466 → 0.656) = cohort consolidating as a single factor
- PC1 variance jumping (e.g., 51.9% → 71.2%) = single-factor structure strengthening
- PC2 variance collapsing (e.g., 21.2% → 7.9%) = secondary sub-structure disappearing
- Pairwise-correlation floor lifting from near-zero to 0.5+ = no more uncorrelated pairs

Cleanest signature of an "institutional basket construction" event: PC2 collapsing while PC1 rises. The cohort moves from multi-factor to single-factor structure as basket-level flows start dominating single-name fundamentals.

See [[Space pure-plays#Pre/post Nov 2025 regime — quantifying the structural shift]] for the worked example. The Nov 2025 regime shift was driven by three concurrent catalysts (WSJ SpaceX-Golden-Dome leak late Oct, USSF SBI prototype contracts Nov 29, Musk SpaceX-IPO confirmation Dec 11).

### Pattern 2: Event-study factor decomposition

For specific catalyst days, decompose each cluster name's return into factor (PC1-driven) and idiosyncratic (residual) components. Identifies which names participated as the factor predicted and which moved more or less.

Procedure:
1. Fit PCA on a representative window (typically 1Y).
2. For the catalyst day, project the day's return vector onto the PC1 loading to get the PC1 score.
3. For each name: factor return = PC1 loading × PC1 score; idiosyncratic = actual return - factor return.
4. Rank names by absolute idiosyncratic component.

Output reveals:
- Pure-factor names (idio < 2pp): rode the basket without name-specific news
- Idiosyncratic-heavy names (idio > 5pp): had name-specific catalysts on top of basket factor
- Basket co-movement vs single-name catalyst stack: how much of a name's move was the cohort factor vs unique news

Worked example: [[Space pure-plays#May 8 2026 — factor vs idiosyncratic decomposition]]. RKLB +34% on May 8 decomposed as +20% factor + +11.6pp idiosyncratic (Q1 print + Motiv + Golden Dome catalysts on top of basket-rally factor).

Useful for distinguishing "factor exposure" trades from "single-name catalyst" trades on a given day.

### Pattern 3: Multiple objectives produce different optimal subsets

The standard validation produces one "best 2-name subset" by factor-tracking correlation. But optimizing for *different* objectives produces different optimal pairs. Three common objectives that diverge in practice:

| Objective | What it captures | Trade implication |
|---|---|---|
| Maximum factor-tracking correlation | Cleanest factor exposure | Hedging / pair-trades against the basket |
| Maximum Sharpe ratio | Best risk-adjusted return on the thesis | Position sizing as part of a portfolio |
| Maximum cumulative return | Highest absolute payoff if thesis works | Single-name conviction trades |

In the Space pure-plays cohort over the 1Y window, these three objectives produced three different "best 2-name pairs": LUNR+BKSY (factor-tracking 0.942), RKLB+PL (Sharpe 2.03), LUNR+PL (cum return +253.7%). The factor-tracking optimum was 5th by Sharpe.

The structural reason: names with low PC1 loading (high idiosyncratic variance) can boost Sharpe in pair-combinations because their idiosyncratic returns are uncorrelated with the factor names' idiosyncratic returns — providing diversification benefit that improves risk-adjusted return at the cost of factor-tracking accuracy. PL was in 2 of 3 Space pure-plays optima despite having the lowest PC1 loading (0.30) because PL's residual returns happen to be high-Sharpe.

Procedure:
1. Enumerate all C(N,2) pairs (and optionally C(N,3) triples) in the cohort.
2. For each subset, compute: equal-weighted return series, correlation to full basket, Sharpe (rf=0), cumulative return, max drawdown.
3. Report top-5 subsets ranked by each objective separately.
4. Identify which names appear in multiple optima — those are the "Swiss Army knife" names; names that appear in only one optimum are objective-specific.

See [[Space pure-plays#Minimum-name expressions]] and [[#Best Sharpe 2-name pair — diversification beats factor-tracking]] for worked examples. Script: `scripts/cluster_subset_optimization.py` (generalizes to any cohort).

### Pattern 4: Complement test for subset validation

If a subset is claimed to "outperform the full basket" or "capture the factor cleanly," the cleanest test is the complement: build a basket of the names NOT in the proposed subset and compare. The ordering reveals whether the subset's outperformance is real or coincidental.

Procedure:
1. Define the proposed subset (e.g., LUNR + BKSY).
2. Build the complement basket (e.g., RKLB + RDW + ASTS + SPIR + PL).
3. Compute equal-weighted return + Sharpe + max DD for: subset, full basket, complement.
4. Expected ordering for a valid subset claim: subset > full > complement on all relevant metrics.

What it tells you:
- Monotonic ordering (subset > full > complement) = subset's outperformance is real, the excluded names are net drag
- Subset > complement but full ≈ subset = subset is fine but full basket is equivalent (no advantage)
- Subset ≈ complement = subset's apparent outperformance is sample noise

Worked example: [[Space pure-plays#Complement test — the 5 names WITHOUT LUNR/BKSY]]. LUNR+BKSY (Sharpe 1.74, cum +247%) > Full 7-name (1.43, +134%) > 5-name complement (1.21, +100%). Clean monotonic ordering confirms LUNR and BKSY are the Sharpe-enhancing names — removing them drops both return and risk-adjusted return materially.

### When to invoke these patterns

| Pattern | Invoke when |
|---|---|
| Pre/post regime split | Rolling PC1 chart shows a step-function shift (>5pp jump in <30 days) |
| Event-study decomposition | Single-day move >3σ for the basket; want to attribute name-specific vs factor |
| Multiple objectives subsets | User considering single-name positioning vs basket positioning |
| Complement test | Subset claim made; need to falsify or validate it rigorously |

All four patterns are deferred-by-default — they're not part of the standard `cluster_analysis.py` output. Invoke them when the basic validation has confirmed cluster status and the cohort merits deeper analysis.

---

## Where the diagnostic lives in the vault

Single source of truth: the durable cluster validation diagnostic lives in exactly one note — the `Sectors/` child note (or `Concepts/` note) that owns the cohort identity. Examples:

| Cohort note | Type | Cohort |
|---|---|---|
| [[Sectors/WFE\|WFE]] | Sectors/ child | ASML, AMAT, LRCX, KLA |
| [[Sectors/AI Compute\|AI Compute]] | Sectors/ child | TSMC + NVDA + AMD |
| [[Sectors/US Memory\|US Memory]] | Sectors/ child | MU, SNDK, WDC |
| [[Sectors/Space pure-plays\|Space pure-plays]] | Sectors/ child | RKLB, RDW, LUNR, BKSY, ASTS, SPIR, PL |
| [[Concepts/Boutique advisory consolidation\|Boutique advisory consolidation]] | Concepts/ | PWP, LAZ, EVR, MC, HLI, PJT |

Event notes that reference the cohort link to the cohort note instead of duplicating the diagnostic. The event note keeps the dated-event narrative (what happened, market reaction, structural reads); the cohort note keeps the durable diagnostic (intra-correlation, PC1, dendrogram, stability across windows).

Example: [[Space basket rally May 8 2026]] event note has a short `## Cluster validation` section that summarizes the headline numbers + links to [[Space pure-plays#Cluster validation diagnostic]]. The full diagnostic, charts, and stability table live in the cohort note, where they're refreshed as new data arrives.

Why: cluster diagnostics need periodic re-runs as the market evolves. If the diagnostic is duplicated in every event note that mentions the cohort, every update requires N edits and risks drift. Single source of truth fixes this.

---

## Embedding the result in the actor note

Add a `## Cluster validation` section after `## Sector correlation` (or as a sub-section if the actor is the primary of a small cluster). Standard structure:

```markdown
## Cluster validation

Mathematically validated cluster: [[Actor1]], [[Actor2]], [[Actor3]] (intra-corr X.XX, PC1 XX.X% explained variance, hierarchical clustering at distance 0.4 returns exactly these N names). Nearest-neighbor sectors: [[Adjacent1]] (intra advantage +X.XX), [[Adjacent2]] (intra advantage +X.XX). Most-distant comparator: [[Distant1]] (intra advantage +X.XX). Full analysis in [[Cluster theme concept note]].

![[{prefix}-dendrogram-1y.png]]
```

For concept notes that own the cluster identity (e.g., [[Boutique advisory consolidation]]), embed the full 4-section analysis directly with all four PNG plots and the diagnostic tables. The concept note is the canonical home; member actor notes link back to it.

### Status-header callout (required for all cluster-validated notes)

Every cluster-validated concept note must lead with an Obsidian callout immediately after the H1 title (before the first paragraph). The callout gives the verdict at a glance so readers don't have to scan to the bottom for the cluster status. Format:

```markdown
# Cluster theme

> [!success] Cluster status: validated (Mon YYYY)
> Intra-cluster correlation 0.XX, PC1 XX.X% explained variance. Hierarchical clustering at 0.4 returns exactly the N candidate names. [Most distinctive separation finding]. See "Cluster validation" section below.

[Body of note continues...]
```

Use one of three callout types based on diagnostic verdict:

| Callout type | When to use | Visual cue |
|---|---|---|
| `> [!success]` | Cluster status: validated | intra-corr ≥ 0.70 AND PC1 ≥ 70% AND hierarchical clustering returns ~candidate cohort |
| `> [!warning]` | Cluster status: partial OR weak | 0.50 ≤ intra-corr < 0.70, OR cluster boundary fuzzy / sub-structure revealed |
| `> [!failure]` | Cluster status: falsified | intra-corr < 0.50 OR hierarchical clustering returns all singletons OR cluster shows NEGATIVE intra-advantage vs comparators |

The callout body should include:
1. Status verdict (e.g., "validated", "partial validation", "weak cluster", "falsified as basket")
2. Validation date (month + year)
3. Intra-correlation and PC1 explained variance (the two headline numbers)
4. The single most important boundary finding (e.g., "all 5 names are singletons", "cyber pure-plays cluster but MSFT/CSCO trade differently", "TSM has subordinates not peers")
5. Pointer to the full "Cluster validation" section below

For falsified clusters where the falsification reveals a constructive sub-cluster, the callout should also link to the validated alternative (e.g., [[AI hyperscalers]] callout points to [[AI capex chain basket]] as the actual tradable cluster).

---

## Checklist (single-pass)

When you create or expand a public-company actor note:

1. Identify the candidate peer cohort (2-7 names typical).
2. Identify 2-3 adjacent-sector control groups + 3-4 broad ETFs.
3. Write `scripts/cluster_configs/{primary_ticker}.yaml`.
4. Run `python scripts/cluster_analysis.py --primary {ticker}`.
5. Read `results.txt`; verify:
   - Intra-cluster correlation > 0.5
   - Hierarchical clustering returns the proposed cohort (or a close variant)
   - PC1 explained variance > 50%
6. Iterate the candidate list if the math says the boundary is wrong.
7. Embed the dendrogram + summary table in the actor or concept note.
8. Log the validation in today's daily note: "validated [[Cluster name]] cohort (intra-corr X.XX, PC1 XX.X%)".

If steps 5-6 cannot reach a defensible cluster, the conclusion is "this actor is a sector orphan" — that is itself a valid finding (matches the existing `> [!warning] Sector Orphan` callout used by `add_sector_correlations.py`). Note it in the actor.

---

## Reference

- Script: `scripts/cluster_analysis.py`
- Config schema + example: `scripts/cluster_configs/boutique_advisory.yaml`
- Canonical write-up: `investing/Concepts/Boutique advisory consolidation.md` (see "Cluster validation — statistical analysis (May 2026)" section)
- Related lighter-weight tool: `scripts/add_sector_correlations.py` (single-actor vs ETFs)
