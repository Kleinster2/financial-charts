# Cluster validation — standard for public actor notes

For every public-company actor note, the "where does this name actually trade" question must be answered mathematically, not by analogy. The procedure produces a single-page validation that confirms (or refutes) the actor's peer cluster, identifies its nearest neighbors in correlation space, and quantifies how single-factor the cluster is.

This is the rigorous version of the existing `## Sector correlation` section, which only correlates the actor against 3-4 ETFs. Cluster validation extends that to a candidate peer cohort + adjacent-sector controls + broad-market benchmarks, and runs three diagnostics.

---

## When to run

**Required:**
- Every new public-company actor note created with a securities companion (`investing/Assets/{Name} securities.md`).
- Every existing public-company actor note when it is materially expanded (e.g., a quarterly earnings ingestion that adds >100 lines, or a strategic re-classification).
- Every concept note that names a peer cluster (e.g., [[Boutique advisory consolidation]], [[AI SaaS Disruption]], [[Hyperscaler capex]]).

**Optional but useful:**
- After a major sector shock (e.g., the May 1 2026 boutique-advisory print), to test whether cluster cohesion held or broke.
- When evaluating whether a new ticker belongs to an existing cluster (add it to the candidate list, re-run, check whether the dendrogram includes it below the threshold).

**Skip:**
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

1. **The `cluster` group must be the smallest plausible candidate cohort.** Don't pre-include every name you suspect belongs — the whole point is to test the boundary. If in doubt, leave a candidate out and let the dendrogram tell you whether it belongs (it will appear in the same hierarchical cluster if it does).

2. **Include 2-3 adjacent-sector control groups, not the whole financial system.** Each adjacent group answers a specific question: "is the cluster really distinct from X?" For boutique advisory, the relevant questions were: distinct from bulge brackets? from mid-IBs? from asset managers? from insurance brokers? If you include 8 groups the heatmap becomes unreadable; if you include 0 there is nothing to test against.

3. **Always include broad ETFs (XLF/SPY for US financials, IWM for small-cap, sector-specific ETFs as appropriate).** The cluster's correlation to broad benchmarks tells you how much of the move is generic risk-on/risk-off vs cluster-specific.

### Choosing the threshold

The 1-|corr| distance threshold defaults to 0.4. Members with pairwise distance below the threshold are bundled into one cluster. Empirically:

- **0.3** = correlation > 0.7 required for cluster membership. Tight cluster definition. Use for highly cohesive cohorts (e.g., the same business in different jurisdictions: US/UK/EU regional banks).
- **0.4** = correlation > 0.6 required. Default. Picks up coherent industry sub-sectors that share a single dominant factor.
- **0.5** = correlation > 0.5 required. Loose cluster definition. Use only if the cohort is structurally noisy (e.g., specialty pharma, where idiosyncratic clinical-trial outcomes dominate).

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

- **>0.7 average** = strong cluster cohesion. The names trade together.
- **0.5-0.7** = moderate cohesion. Real cluster, but with idiosyncratic dispersion. Common for cohorts with one or two outlier business models.
- **<0.5** = weak cohesion. The candidate cohort is not actually a cluster; the names are loosely related by taxonomy but not by market behavior.

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

- **+0.30 or more** = clearly distinct. The cluster has a real cohesion factor not shared with this group.
- **+0.10 to +0.30** = moderately distinct. The cluster shares systematic factor exposure with this group but adds something specific.
- **<+0.10** = not distinct. The cluster moves with this group; the candidate cohort does not deserve a separate identity.

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

- **>70%** = single-factor cohort. Equal-weighted basket ≈ PC1. Useful for pair trades and event analysis.
- **50-70%** = dominant-factor cohort with meaningful sub-structure. PC2/PC3 may identify a within-cluster business-model split worth flagging.
- **<50%** = multi-factor cohort. The candidate cluster has at least two distinct trading regimes; the cluster validation is weaker.

PC1 loadings should all be positive and roughly equal. If they aren't (one name negative, or one name dramatically larger than others), that name has a different return profile from the rest — flag it as a candidate outlier.

### 5. Conclusions to draft

For the actor note, condense the output into a 5-row summary table + one paragraph. See `investing/Concepts/Boutique advisory consolidation.md` for the canonical write-up format.

---

## Embedding the result in the actor note

Add a `## Cluster validation` section after `## Sector correlation` (or as a sub-section if the actor is the primary of a small cluster). Standard structure:

```markdown
## Cluster validation

Mathematically validated cluster: **[[Actor1]], [[Actor2]], [[Actor3]]** (intra-corr X.XX, PC1 XX.X% explained variance, hierarchical clustering at distance 0.4 returns exactly these N names). Nearest-neighbor sectors: [[Adjacent1]] (intra advantage +X.XX), [[Adjacent2]] (intra advantage +X.XX). Most-distant comparator: [[Distant1]] (intra advantage +X.XX). Full analysis in [[Cluster theme concept note]].

![[{prefix}-dendrogram-1y.png]]
```

For concept notes that own the cluster identity (e.g., [[Boutique advisory consolidation]]), embed the full 4-section analysis directly with all four PNG plots and the diagnostic tables. The concept note is the canonical home; member actor notes link back to it.

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
