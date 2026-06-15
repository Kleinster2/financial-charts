---
aliases: [Online travel, OTA cluster, Online travel agencies, Online travel agency cluster, OTAs]
tags: [concept, cluster-validation, travel, consumer-discretionary, usa]
---

# Online travel

> [!warning] Cluster status: validated as a distinct travel factor, but moderate and eroding (Jun 2026)
> The three listed online travel agencies ([[Booking Holdings|BKNG]]/[[Airbnb|ABNB]]/[[Expedia|EXPE]]) form a real, distinct factor — intra-corr 0.585 (weekly 0.635), PC1 72.5%, all three cluster, rejects the random-basket null at p 0.0010, and carries a positive intra-advantage versus every control: the other travel cyclicals (+0.178 vs airlines/cruises), hotels (+0.190), and the market (+0.146). Unlike the commodity and managed-care cohorts, it is NOT ETF-replicable — there is no pure-OTA ETF, so the three-name basket is the genuine expression. But cohesion is only moderate and the threshold is FRAGILE (stable only [0.50–0.55]) and the holdout WEAKENED (0.73) — the OTA factor is real and distinct but looser and more eroding than the tight, durable [[Airlines]] and [[Cruise lines]] cohorts. This completes the travel-cyclical set as a third, separable factor.

The third leg of the travel-cyclical complex, after the validated [[Airlines]] and [[Cruise lines]] cohorts. The question was whether the online travel agencies are a distinct travel factor or just consumer-discretionary beta, and whether they split by model — agency ([[Booking Holdings]], [[Expedia]]) versus marketplace ([[Airbnb]]). They are distinct (positive advantage against airlines, cruises, hotels, and the market alike), they cohere as one factor (all three cluster, PC1 72%), and the model split is only second-order: the two agency names pair tightest, but Airbnb joins them inside the 0.5 cut. What separates this from the day's other cohorts is that it is genuinely un-replicable by an ETF — owning the OTA factor means owning the three names.

> [!note] Data-integrity provenance
> The first run of this cohort produced a false falsification (intra-corr 0.21, BKNG a 367%-vol singleton) because [[Booking Holdings]]'s DB series carried an un-back-adjusted 25-for-1 stock split — a spurious −96% return on 2025-12-24. Re-fetching the split-adjusted series corrected it and flipped the verdict to the validated result below. A clean, dramatic statistical finding is a reason to check the data, not to believe it.

## Cluster validation

The candidate cohort is the three listed online travel agencies — [[Booking Holdings|BKNG]], [[Airbnb|ABNB]], [[Expedia|EXPE]] — tested against the validated travel cyclicals (airlines DAL/UAL, cruises CCL/RCL), hotel operators (MAR/HLT), and benchmarks (XLY consumer-discretionary ETF, SPY).

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.585 [0.500–0.697] | moderate; weekly 0.635 (small-cap reaction-timing, not async — all US-listed) |
| PC1 explained variance | 72.5% | dominant single factor |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0010 (PC1 0.0011) | rejects — real cohesion, not a random 3-pick |
| Holdout (2Y split) | WEAKENED 0.73 | factor present but eroding (loadings corr 0.19) |
| Threshold clean width | 0.05 [0.50–0.55] | FRAGILE — validation depends on the cut |
| Intra-adv vs travel cyclicals (airlines/cruises) | +0.178 | a distinct, third travel factor |
| Intra-adv vs hotels (MAR/HLT) | +0.190 | distinct from hotel operators |
| Intra-adv vs market (XLY/SPY) | +0.146 | distinct from consumer-discretionary beta — and not ETF-replicable |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/bkng.yaml`; registry row 2026-06-15. Terminology: [[Cohort, cluster, basket]].

### Boundary — OTAs cluster apart from airlines, cruises, hotels

![[online-travel-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The three OTAs (ABNB/BKNG/EXPE, green) form their own cluster and join the rest only at 0.585. Airlines (DAL/UAL), cruises (CCL/RCL), hotels (MAR/HLT), and the market (XLY/SPY) form a separate combined block — OTAs are distinct from all of them.*

The OTA cohort is intact and isolated only in a narrow threshold band [0.50–0.55]; below 0.50 the marketplace name (Airbnb) detaches, above 0.55 the broad travel/market block contaminates. So it is a real but fragile boundary — distinct from the other travel cyclicals (it never merges with airlines or cruises below 0.585), but not a wide, robust island like cruises.

### Topology — agency pair tightest, marketplace joins

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BKNG + EXPE | 0.303 | the agency pair (corr 0.70) |
| 2 | ABNB + (BKNG+EXPE) | 0.471 | Airbnb (marketplace) joins inside the 0.5 cut |

The faint model split is visible but not decisive: the two agency OTAs ([[Booking Holdings]], [[Expedia]]) pair at 0.303, and the marketplace [[Airbnb]] joins at 0.471 — inside the cut, so it is a cohort member, not an outlier. Booking and Expedia share the hotel/flight-agency commission model; Airbnb's short-term-rental marketplace is adjacent enough to trade with them.

### PC1 index weights

![[online-travel-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 72.5% with near-equal loadings (0.54–0.60) — a coherent single factor with a modest PC2 (17.6%, the agency/marketplace axis).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Booking Holdings (BKNG) | 0.604 | 34.9% | 34.5% | 36.8% |
| Airbnb (ABNB) | 0.538 | 31.1% | 29.3% | 38.6% |
| Expedia (EXPE) | 0.588 | 34.0% | 50.2% | 24.6% |

Near-equal loadings; the lower-vol [[Airbnb]] takes the largest raw PC1-mimic weight and the higher-vol [[Expedia]] the smallest.

### Distinctness — a third travel factor, not ETF-replicable

![[online-travel-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The OTA block is warm internally and cooler against airlines, cruises, hotels, and the market.*

The positive intra-advantage against every control is the key result and the contrast with the day's other cohorts: OTAs are +0.178 distinct from the other travel cyclicals (airlines/cruises trade on fuel/demand and leverage; OTAs on booking volume, take-rate, and ad spend), +0.190 from hotel operators, and +0.146 from consumer-discretionary beta. Because there is no pure online-travel ETF, that last number means the factor is not ETF-replicable — unlike oil (=XLE) or managed care (=IHF), the only way to own the OTA factor is the three names. Travel is therefore at least three distinct equity factors — airlines, cruises, and OTAs — split by where in the trip-economics chain a name sits.

### Historical tightness evolution

![[online-travel-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Tight in 2022–23 (0.74–0.76), a sharp 2024 dip (0.48), re-tightened in 2025 (0.74), easing into 2026 (0.63) — the eroding tightness the holdout flags.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2022 | 0.740 | 82.7% |
| 2023 | 0.762 | 84.1% |
| 2024 | 0.480 | 65.4% |
| 2025 | 0.739 | 82.7% |
| 2026 | 0.625 | 75.1% |

The OTA factor is real but regime-sensitive — it tightens in clear travel-cycle regimes (the 2022–23 post-COVID recovery, the 2025 re-acceleration) and loosens when the names trade on company-specific stories (the 2024 dip; Airbnb's regulation and Expedia's turnaround diverging from Booking's steady compounding). Weaker and less durable than [[Cruise lines]] (0.81, holdout STABLE) or [[Airlines]] (0.76, STRENGTHENING) — the OTAs are the loosest of the three travel cyclicals, fitting their more idiosyncratic, platform-specific business models.

## Related

- [[Booking Holdings]], [[Airbnb]], [[Expedia]] — the three OTA members
- [[Airlines]] — the validated travel cyclical (distinct, +0.178)
- [[Cruise lines]] — the validated travel cyclical (distinct, +0.178)
- [[Travel]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-15. 1Y daily log returns through 2026-06-12; config `scripts/cluster_configs/bkng.yaml`; registry row 2026-06-15. Validated on split-adjusted BKNG data after correcting an un-back-adjusted 25:1 split. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
