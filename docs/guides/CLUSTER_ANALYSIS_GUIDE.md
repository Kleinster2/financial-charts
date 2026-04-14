# Cluster Analysis Guide

Guide to the cluster-analysis methods already present in this project, how to use them, and how to turn cluster output into durable vault notes.

---

## Why this exists

This repo already has several cluster-analysis paths, but they are not equally mature.

The main distinction:

- **Ward hierarchical clustering** is the core visual pipeline already wired into the sandbox.
- **`scripts/cluster_movers.py`** is the stronger event-day / coordinated-move analysis path, but it is still CLI-only.
- **K-means** exists only as exploratory one-off work and should not be treated as the default cluster framework.

---

## Capability map

| Status | Method | Main files | What it does | Recommended use |
|--------|--------|------------|--------------|-----------------|
| **Production-worthy** | Ward hierarchical clustering | `hierarchical_analysis.py`, `charting_sandbox/chart-dendrograms.js`, `charting_app/content_routes.py` | Generates dendrograms and clustermaps for stock groups and serves them through the sandbox | Default structural cluster view |
| **Salvageable** | Custom excess-return correlation clustering | `scripts/cluster_movers.py` | Clusters beta-adjusted excess returns and flags statistically unusual coordinated group moves | Event-day / regime-day cluster detection |
| **Exploratory** | K-means | `scripts/one_off/cluster_analysis.py`, `scripts/one_off/plot_cluster_portfolios_refactored.py` | Experimental grouping and proxy-portfolio work | Comparison baseline only |
| **Not meaningfully present** | HRP / NCO / Louvain / Leiden / DBSCAN / MST | — | Not implemented in a durable way | Future work |

---

## Best default method for this repo

If you need one default cluster method here, use:

**hierarchical clustering on correlations, with Ward linkage, visualized through dendrograms and clustermaps.**

Why this is the default:

- it is already the most integrated path in the repo
- it does not require choosing `k` up front
- it handles nested market structure better than plain k-means
- it maps naturally to note-making because the output is interpretable

If the question is not "what is the structural map?" but "what group is moving together abnormally right now?", use:

**`scripts/cluster_movers.py`**

That script is better for identifying coordinated repricings that broad sector buckets miss.

---

## Current Ward pipeline

### Core files

- `hierarchical_analysis.py`
- `charting_sandbox/chart-dendrograms.js`
- `charting_app/content_routes.py`
- `README.md` (Dendrogram System section)

### What it now does

`hierarchical_analysis.py`:

- loads prices from `stock_prices_daily`
- calculates log returns
- builds correlation matrices
- converts correlations into a symmetric distance matrix
- applies **Ward linkage**
- generates:
  - truncated dendrograms
  - detailed dendrograms
  - top-50 clustermaps
  - sector/country dendrograms
  - sector/country clustermaps
- writes outputs to:
  - `charting_sandbox/dendrograms/`

### Regeneration

```powershell
python hierarchical_analysis.py
```

### Viewing

```powershell
python charting_app\app.py
```

Then open:

- `http://localhost:5000/sandbox/`

The sandbox viewer loads cluster images from:

- `/sandbox/dendrograms/`

---

## Current analytical cluster path

### `scripts/cluster_movers.py`

This is not just another visualization script. It is a separate analytical workflow.

It:

- extracts tickers from the vault
- fetches price history
- computes **beta-adjusted excess returns** versus `SPY`
- builds clusters using an **average-linkage style correlation rule**
- scores whether the group move is statistically unusual

Use this when the question is:

- what cluster moved together on a shock day?
- what hidden group move is not obvious from individual screeners?
- which names are being priced as one risk bucket right now?

This is especially useful for:

- safety-trade unwinds
- war-premium repricings
- sector splits that are not visible in standard GICS buckets
- event-driven cluster detection

### Basic usage

```powershell
python scripts\cluster_movers.py
python scripts\cluster_movers.py --show-all
python scripts\cluster_movers.py --verbose
```

Most important parameters:

- `--corr-threshold`
- `--min-cluster`
- `--cluster-sigma`
- `--corr-lookback`
- `--beta-lookback`
- `--vol-lookback`

---

## K-means status

K-means exists in this repo, but only as exploratory work:

- `scripts/one_off/cluster_analysis.py`
- `scripts/one_off/plot_cluster_portfolios_refactored.py`

Treat it as:

- a rough comparison tool
- a baseline for experimentation
- not the main cluster architecture

Why it is not the default:

- it forces a pre-chosen number of clusters
- financial clusters are usually nested, not spherical
- it is less interpretable for note design than hierarchical methods
- it is not integrated into the sandbox or main docs workflow

---

## Recommended workflow

Use two separate workflows depending on the question.

### A. Structural cluster workflow

Use when asking:

- what are the durable groupings in this market?
- which names belong to the same structural bucket?
- how should we visualize the landscape?

Steps:

1. run `python hierarchical_analysis.py`
2. inspect dendrograms and clustermaps in `/sandbox/`
3. compare the same group across multiple windows:
   - full history
   - yearly
   - quarterly
   - monthly
4. identify the **core members**, not just the full branch
5. write or update the appropriate note

### B. Event / coordinated-move workflow

Use when asking:

- what moved together today?
- what cluster is repricing during this regime?
- what market-implied grouping appeared during a shock?

Steps:

1. run `python scripts\cluster_movers.py`
2. review the flagged clusters and their z-scores
3. compare the result to raw market narrative
4. decide whether the group represents:
   - structural cluster
   - event cluster
   - narrative/risk-factor cluster
5. write or update the note that best fits the cluster's function

---

## How to identify a real cluster

Do not create notes from a single chart or one pretty branch.

A cluster is more likely to be real if several of these are true:

- it appears across multiple windows
- it survives after market beta is removed
- it has a clear economic mechanism
- it explains behavior that sector labels do not
- it has a stable core, even if edge members rotate

### Questions to ask

#### 1. Is it structural?

Examples:

- same business model
- same bottleneck
- same customer type
- same capital structure sensitivity
- same regulatory constraint

These usually deserve **sector notes** or durable **concept notes**.

#### 2. Is it market-implied?

Examples:

- the market treats these names alike even if fundamentals differ
- the group appears mainly in excess-return space
- the cluster expresses a pricing bucket or narrative premium

These usually deserve **concept notes**.

#### 3. Is it event-driven?

Examples:

- ceasefire repricing
- tariff shock
- earnings-day factor unwind
- managed-agents selloff

These usually deserve **event notes**.

#### 4. Is it investable enough to track?

If yes, it may deserve a **basket note** and a synthetic index script.

---

## Cluster note design

The cluster result is not the note. The note should explain what the cluster means.

### Hard rule

**Do not create a cluster note unless the note is more useful than the individual actor notes plus links.**

### Pick the right note type

| If the cluster is mainly about... | Best note type |
|-----------------------------------|----------------|
| an operating arena / ecosystem | `Sectors/` |
| a pricing mechanism / market logic | `Concepts/` |
| a dated shock or repricing | `Events/` |
| a trackable expression | basket concept note + synthetic index |

### Best structure for a durable cluster note

1. **Plain-English preamble**
   - what the cluster is
   - why these names belong together
   - why it matters

2. **What binds the cluster**
   - revenue exposure
   - customer overlap
   - balance-sheet sensitivity
   - same bottleneck
   - same narrative bucket
   - same market classification error

3. **Core vs. peripheral members**
   - core members
   - adjacent members
   - false friends

4. **When it clusters and when it breaks**
   - crisis regime
   - easing regime
   - commodity shock
   - policy shock
   - normal market environment

5. **Market signal**
   - what does this group tell us?
   - what repricing is it capturing?
   - what does broad sector language miss?

6. **Evidence**
   - cluster output
   - z-score or event-day move
   - clustermap or dendrogram when useful
   - links to related actor / sector / concept / event notes

7. **Related trade expression**
   - basket
   - ratio to another basket
   - comparison set

---

## When a cluster note is justified

A new note is justified when the cluster does at least one of these jobs:

- names a market structure the vault does not already capture
- explains a repricing mechanism better than existing sector notes
- serves as the canonical home for a cross-actor event
- supports a durable basket worth tracking over time

A new note is **not** justified when:

- the cluster appears only once and has no causal story
- an existing note already captures the mechanism
- the note would be obsolete in a month
- the output is just a list of names with no explanatory value

---

## Recommended note-routing rules

### Create a `Sectors/` note when:

- the cluster describes a real operating domain
- the members share industry mechanics
- the grouping is durable beyond one event

Examples:

- edge cloud
- data-center REITs
- grid gear / large power equipment

### Create a `Concepts/` note when:

- the cluster is mostly a pricing mechanism
- the group is real in markets even if the operating businesses differ
- the note explains how capital is classifying risk

Examples:

- AI control points
- war premium carriers
- SaaS-as-safety unwind
- runtime leakage / control-plane risk

### Create an `Events/` note when:

- a dated shock touched 3+ actor notes
- the detailed move would otherwise be duplicated everywhere
- the event is the right canonical home for the market reaction

Examples:

- managed-agents selloff
- ceasefire repricing
- tariff shock day

### Create a basket note when:

- the group has a stable enough membership list
- weighting logic is defensible
- the group is worth tracking as an expression over time

---

## Practical checklist before creating a cluster note

- [ ] Did the cluster appear in more than one window or view?
- [ ] Is there a clear economic or market-pricing mechanism?
- [ ] Can we name the core members confidently?
- [ ] Does an existing sector/concept/event note already cover it?
- [ ] Is the cluster structural, market-implied, event-driven, or trackable?
- [ ] Will the note still matter in six months?
- [ ] If it needs tracking, should it become a basket?

If the answer to most of these is no, do not create the note.

---

## Best next upgrades

If cluster analysis becomes a higher-priority part of this repo, the best upgrades are:

1. **promote `cluster_movers.py` into a real API/UI feature**
2. add **rolling stability diagnostics**
3. add **shrinkage / denoised correlations**
4. add a **graph/community-detection path** as a second lens
5. connect the output more directly to basket creation and note suggestions

---

## Bottom line

For this project:

- **Ward hierarchical clustering** is the main structural cluster framework
- **`cluster_movers.py`** is the best event-day / coordinated-move framework
- **K-means** should stay a secondary exploratory lens

For vault design:

- use **sector notes** for real operating ecosystems
- use **concept notes** for pricing logic and market-implied groupings
- use **event notes** for dated shocks
- use **basket notes** when the cluster becomes a durable expression worth tracking
