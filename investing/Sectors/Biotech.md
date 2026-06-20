---
aliases: [Biotech, Big biotech, Biotechnology, Large-cap biotech, Biotech cluster]
tags: [sector, healthcare, biotech, cluster-validation]
---

# Biotech

> [!failure] Cluster status: falsified — biotech is healthcare/biotech-ETF beta, not a distinct factor; it shatters on idiosyncratic pipelines (Jun 2026)
> The large-cap biotechs ([[Gilead|GILD]]/[[Amgen|AMGN]]/[[Vertex|VRTX]]/[[Regeneron|REGN]]/[[Biogen|BIIB]]) do NOT trade as one factor — intra-corr 0.420 (weekly 0.350, lower), PC1 only 54%, the tightest pair joins above the cut (GILD+AMGN 0.518), and the cohort barely beats the random-basket null (p 0.009) via shared healthcare beta. The decisive numbers: a NEGATIVE −0.023 intra-advantage versus the biotech ETFs (the names correlate more with IBB/XBI/XLV than with each other) and only +0.041 versus big pharma. The cohort shatters — only [[Amgen|AMGN]]+[[Vertex|VRTX]] cluster (with IBB/XBI/XLV); [[Gilead|GILD]], [[Regeneron|REGN]], [[Biogen|BIIB]] are idiosyncratic singletons. Each biotech trades its own pipeline, patent cliff, and clinical-trial calendar, not a shared "biotech" factor. Own IBB/XBI for healthcare-risk beta; there is no distinct big-biotech basket. This completes the healthcare falsification set ([[Pharma majors|pharma]], [[GLP-1 receptor agonists|GLP-1]], [[Medtech]], [[DTC Telehealth]] — all shattered).

The purest idiosyncratic-driver sector. A biotech's value is its specific franchise and pipeline — Vertex's cystic-fibrosis monopoly, Gilead's HIV/oncology base, Regeneron's Eylea/Dupixent, Biogen's Alzheimer's and MS franchises, Amgen's biosimilars and obesity entry — and those move on drug-specific data, approvals, and patent cliffs that are uncorrelated across names. So beyond broad healthcare/risk beta (captured by IBB, XBI, or XLV), there is no shared big-biotech factor to own. The clinical-trial calendar is the anti-cluster: it makes every name a single-stock story.

## Cluster validation

The candidate cohort is the five large-cap profitable biotechs — [[Gilead|GILD]], [[Amgen|AMGN]], [[Vertex|VRTX]], [[Regeneron|REGN]], [[Biogen|BIIB]] — tested against big pharma ([[Pfizer|PFE]]/[[Merck|MRK]]/[[AbbVie|ABBV]]) and benchmarks (IBB Nasdaq-biotech ETF, XBI equal-weight biotech, XLV healthcare, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.420 [0.332–0.482] | below the 0.50 floor; weekly 0.350 (LOWER — no persistent factor) |
| PC1 explained variance | 53.7% | barely above 50%, with big PC2/PC3 (14%/13%) — multi-factor |
| Independence null p | 0.0001 | series co-move at all |
| Random-basket null p | 0.0093 | marginal — barely beats a random 5-pick, via shared healthcare beta |
| Vol-matched null p | 0.017 / 0.022 | marginal |
| Holdout (2Y split) | STABLE 0.88 | durably LOOSE (train 0.395 → test 0.349) — consistently weak, not eroding |
| Threshold clean width | 0.00 | never isolates; IBB/XBI/XLV join from 0.50 |
| Intra-adv vs big pharma (PFE/MRK/ABBV) | +0.041 | NOT distinct — biotech ≈ pharma, one healthcare complex |
| Intra-adv vs ETFs (IBB/XBI/XLV/SPY) | −0.023 | NEGATIVE — the names track the ETFs more than each other |

All US-listed. Config: `scripts/cluster_configs/amgn.yaml`; registry row 2026-06-19.

### Boundary — the cohort shatters; only AMGN+VRTX cluster (with the ETFs)

![[biotech-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort does not hold: only [[Amgen|AMGN]]+[[Vertex|VRTX]] cluster, and they cluster with the biotech/healthcare ETFs (IBB/XBI/XLV) — i.e., as ETF beta. [[Gilead|GILD]], [[Regeneron|REGN]], and [[Biogen|BIIB]] are singletons; the pharma control (PFE/MRK) forms its own pair. Five proposed names, no biotech cluster.*

The threshold scan never returns the cohort as a clean cluster (zero width), and the candidate join sequence is the tell: the tightest pair (GILD+AMGN) joins only at 0.518 — already above the 0.5 cut — so nothing clusters at threshold. From 0.50 the biotech/healthcare ETFs (IBB/XBI/XLV) contaminate, and from 0.60 the pharma names join. This is the grade-2 falsification: the names beat random baskets only marginally and only via shared healthcare/risk beta (negative intra-advantage vs the ETFs), with no biotech-specific factor. The one micro-pair (AMGN+VRTX) is itself ETF-coincident, not a constructive sub-cluster.

### Topology — no cluster forms; every name a singleton at 0.5

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | GILD + AMGN | 0.518 | "tightest" pair — but already above the 0.5 cut |
| 2 | VRTX + (GILD+AMGN) | 0.531 | |
| 3 | BIIB + core | 0.575 | |
| 4 | REGN + core | 0.625 | the cohort closes far above the cut |

Every join is above the 0.5 threshold — the cohort never forms a cluster. The names are each closer to the healthcare ETFs than to one another. PC1 explains only 53.7% (vs >70% for a real cluster), with sizeable PC2 (14%) and PC3 (13%) — a genuinely multi-factor set, one factor per franchise.

### PC1 index weights

![[biotech-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 53.7% (weekly 48.1%) with large secondary components — a multi-factor cohort, the signature of a non-cluster.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| GILD | 0.436 | 19.5% | 26.1% | 21.7% |
| AMGN | 0.490 | 21.9% | 27.6% | 23.1% |
| VRTX | 0.463 | 20.7% | 27.6% | 21.8% |
| REGN | 0.408 | 18.3% | 33.4% | 15.9% |
| BIIB | 0.435 | 19.5% | 32.4% | 17.5% |

Loadings are middling and similar, but PC1 captures barely half the variance — there is no dominant common factor to weight. [[Amgen]] and [[Vertex]] carry the highest loadings (consistent with their being the only pair that clusters), the higher-vol [[Regeneron]]/[[Biogen]] the lowest.

### Distinctness — = the healthcare/biotech ETFs, not distinct from pharma

![[biotech-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. No uniformly-hot biotech block; the names are about as warm against IBB/XBI/XLV and against the pharma pair as against each other.*

The decisive number is the −0.023 intra-advantage versus the ETFs: the biotechs correlate with IBB/XBI/XLV more than with one another, so there is no biotech-specific factor beyond healthcare/risk beta. And +0.041 versus big pharma — negligible — so biotech and pharma are not separable; they are one healthcare complex. The investable read collapses to the ETF: own IBB or XBI (or XLV) for healthcare-risk exposure; picking [[Vertex]] over [[Gilead]] is a pure single-drug/pipeline bet, not a factor bet.

### Historical tightness evolution

![[biotech-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Persistently loose — 0.35–0.44 every year, never a tight cluster.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.421 | 54.2% |
| 2021 | 0.358 | 50.4% |
| 2022 | 0.441 | 55.4% |
| 2023 | 0.348 | 48.2% |
| 2024 | 0.354 | 48.8% |
| 2025 | 0.361 | 49.6% |
| 2026 | 0.429 | 54.6% |

Latest 90-day reading: intra 0.410, PC1 53.3%. Biotech is durably loose — never above 0.44 in six years (the holdout's STABLE 0.88 just means it is *consistently* weak, not eroding). It is the canonical structurally-noisy cohort: idiosyncratic clinical-trial and patent-cliff outcomes dominate, so the names never cohere into a factor. Together with [[Pharma majors|pharma]] (also +0.04 vs the ETFs), [[GLP-1 receptor agonists|GLP-1]], [[Medtech]], and [[DTC Telehealth]], it completes the campaign's healthcare result: no healthcare sub-sector is a distinct equity factor — the only healthcare factor is broad XLV/IBB/XBI beta, because every name is its own pipeline story.

## Related

- [[Pharma majors]] — the sibling healthcare falsification (= healthcare beta); biotech is not distinct from it (+0.041)
- [[GLP-1 receptor agonists]], [[Medtech]], [[DTC Telehealth]] — the rest of the healthcare falsification set
- [[Gilead]], [[Amgen]], [[Vertex]] — the higher-cohesion names (AMGN/VRTX the one ETF-coincident pair)
- [[Regeneron]], [[Biogen]] — the idiosyncratic singletons
- [[Eli Lilly]] — the GLP-1 outlier that broke even the pharma cohort
- [[Athletic footwear and apparel]] — the sibling falsification by idiosyncratic drivers (regime-dependent, where biotech is durably loose)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/amgn.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
