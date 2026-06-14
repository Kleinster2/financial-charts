---
aliases: [Cluster terminology, Cluster vocabulary, Cluster glossary, Cluster validation glossary, Cohort vs cluster vs basket, Basket vs cluster vs cohort, Sector vs cluster, Sector vs sub-sector]
tags: [concept, framework, cluster-validation, glossary, terminology]
---

# Cohort, cluster, basket

Glossary codifying the three terms the cluster-validation framework uses for what is, at each stage, the same set of tickers. They are not synonyms — they are three stages of one object: the candidate you propose ([[#Cohort]]), the verdict the math returns ([[#Cluster]]), and the position you would hold to trade it ([[#Basket]]). A fourth term — sector — sits on a different axis: the classification substrate these groupings are carved from and filed under, not a stage in the lifecycle (see [[#Related axis — sector]]). Reference for [[Vault cluster taxonomy]] and `docs/cluster-validation.md`.

*This is a terminology glossary — no chart data applicable. The diagnostics these terms describe are charted in the per-cohort notes and summarized in [[Vault cluster taxonomy]].*

## The distinction

| Term | What it is | Layer | Test |
|---|---|---|---|
| Cohort | The candidate set of names you propose and test, grouped by a shared story — business model, end-market, capital-stack role, or thesis | Analytical (input) | A set is a cohort whether or not it passes |
| Cluster | The statistical verdict that the cohort's members actually trade as one factor: high intra-correlation, dominant PC1, membership that holds at the dendrogram cut | Structural (finding) | A cohort is or isn't a cluster |
| Basket | The tradeable expression of a validated cluster: the investable portfolio you would hold to capture the factor (equal-weighted or PC1-mimic weighted) | Investable (instrument) | A cluster can be expressed as a basket — or replicated by an existing ETF |

One-line mnemonic: cohort is the input, cluster is the finding, basket is the instrument.

## Cohort

The candidate grouping — the hypothesis. You assemble a cohort by analogy (these names share an end-market / business model / thesis) and then test whether the market agrees. It is a cohort regardless of the outcome; a falsified grouping is still a cohort, just not a cluster.

In a `scripts/cluster_configs/{name}.yaml` config the candidate cohort is the group literally named `cluster` (see [[#Caveats]] — this is the main source of confusion). In prose the framework says "candidate cohort," "N-name cohort," "cross-cohort." Cohort never becomes a note title: there are zero `*cohort*.md` notes in the vault, because a cohort is the thing being measured, not a durable entity.

## Cluster

The structural verdict. A cohort earns the word "cluster" only when the diagnostics confirm its members move as one factor:

- average intra-cluster correlation above the floor (≥ 0.50 moderate, ≥ 0.70 strong),
- a dominant first principal component (PC1 ≥ 50%, ≥ 70% single-factor),
- membership that holds together when hierarchical clustering cuts the 1-|corr| distance tree.

The framework's hinge sentence, `docs/cluster-validation.md`: "the candidate cohort is not actually a cluster; the names are loosely related by taxonomy but not by market behavior." The `> [!success|warning|failure] Cluster status:` callout records the verdict at the head of every validated note. Notes titled "X cluster" foreground the structural finding — usually the falsified ([[Mag 7 cluster]]) or the small / purely-structural ([[UAS defense micro-cluster]]) cases. See [[Vault cluster taxonomy]] for the cross-cohort comparison and the verdict thresholds.

## Basket

The tradeable expression. Once a cohort validates as a cluster, the basket is the position you would actually hold to capture the factor — equal-weighted across members, or PC1-mimic weighted (inverse-volatility, the raw-return weights that best replicate the standardized common factor). `docs/cluster-validation.md`: "Equal-weighted basket ≈ PC1"; the "PC1 replication basket" is the investable construct.

Performance, valuation, weighting, and tracking live in basket notes; the cluster diagnostic deliberately does not rank attractiveness (structure, not performance — `docs/cluster-validation.md`). Internally-constructed baskets are tagged `basket/internal` ([[Defense primes basket]], [[Mega banks basket]], [[Payments basket]]). Real third-party products are the external counterpart: [[GS US Software Basket]], [[UBS European AI Disruption Basket]].

A cluster does not always deserve a bespoke basket. If a liquid sector ETF already holds the names, the ETF replicates the basket and the hand-built version adds nothing — see the nuclear worked example below.

## Related axis — sector

Sector is not a fourth stage of this lifecycle; it is the substrate the lifecycle runs on. Cohort → cluster → basket tracks one grouping through validation; sector is the classification layer that grouping is carved from and the validated cluster is filed under. It answers a different question — what industry is this, who competes here, what is the value chain — so it is best treated as an adjacent axis, not a fourth term in the sequence.

The vault redefinition. In standard finance "sector" is a GICS bucket assigned a priori. This vault rejects that ([[Linking and hierarchy]]): "Sectors are correlation clusters, not GICS categories" — 80+ flexible, overlapping clusters, not 11 fixed buckets. A vault sector is therefore the informal, persistent, scaffolded name for a cluster, organized as a hierarchy:

- Sector — broad industry hub ([[Defense]], [[AI Infrastructure]]).
- Sub-sector — a "cluster of actors that compete" (the [[Linking and hierarchy]] test: do they mostly compete with each other and not with actors in other clusters?).
- Sister concept — explains why the sub-sector matters.

So sector and cluster overlap in intent but differ in rigor and role. A sub-sector asserts co-movement and gives it a permanent home with a value chain and competitive map; the cluster validation is the Gate-11 math that confirms or refutes that assertion. A sub-sector hub is, in effect, a candidate cluster with a permanent address.

Placement fork. The cohort-owner note — the home of the cluster diagnostic — lives in one of two folders, and the choice is exactly the question "is this grouping an industry or a theme?":

- Sectors/ child — a recognized industry sub-sector ([[WFE]], [[Space pure-plays]]).
- Concepts/ — a thematic or cross-sector grouping ([[AI SaaS Disruption]], [[Boutique advisory consolidation]], [[Defense primes basket]], the [[Nuclear renaissance]] basket).

Sector as the comparison surface. Inside a cluster run, sector is never the candidate — it is the benchmark you test distinctness against: the adjacent-sector control groups in the YAML (nuclear utilities, for the nuclear cohort), the sector ETF used as a benchmark (and sometimes the punchline — URA/NLR are the uranium sector ETF that replicated the nuclear basket), the lightweight `## Sector correlation` section that cluster validation is "the rigorous version of," and the `Sector Orphan` warning callout for a name that fits no cluster.

The two-note pattern. The same names can carry a sector hub and a basket note doing different jobs: [[Defense Primes]] is the industry scaffold (parent [[Defense]], sister [[Defense IT Services]], value chain, an informal "trades as a moderate cluster"); [[Defense primes basket]] is the formal cohort/cluster/basket with the Gate-11 validation. The hub says "one industry"; the basket note says "the math confirms a six-name factor, here is the tradeable form."

## Worked examples

| Stage | Nuclear / SMR | Defense primes |
|---|---|---|
| Cohort | The seven names grouped by the [[Long nuclear]] story: OKLO, SMR, NNE, LEU, CCJ, BWXT, UEC | The seven listed US primes grouped by DoD-customer end-market |
| Cluster | Validated as a real one-factor cluster (intra 0.645, PC1 69.9%, passes nulls incl. vol-matched) — but not a distinct one (URA/NLR share the cluster) | Validated at the 6-name core (intra 0.556, PC1 64.3%); 7-name partial — LDOS drags |
| Basket | Collapses to the URA/NLR uranium ETF; bespoke value only in isolating the SMR-developer sub-sleeve | [[Defense primes basket]] — equal-weighted 6-core (LMT/RTX/NOC/GD/HII/LHX) |

The [[Defense primes basket]] note shows all three terms in one place: titled "basket" (the tradeable identity, tag `basket/internal`), carrying a "Cluster status: validated" callout (the verdict), with prose measuring "the 7-name cohort" (the candidate). They are stages, not separate files. The [[Nuclear renaissance#Cluster validation|Nuclear / SMR]] case is the cleaner teaching example because the three diverge: the cohort is a cluster, but the basket is an existing ETF.

## Caveats

1. Config-level overload. The YAML names the candidate-cohort group `cluster` before any validation runs (`docs/cluster-validation.md`: "REQUIRED group name; the candidate cohort being tested"). So at the config layer "cluster" means "the cohort I am hoping is a cluster." This is the single biggest source of confusion; the doc flags it itself.
2. Geographic homonym. "Cluster" also means a physical or industrial agglomeration — [[China AI clusters]], [[Hangzhou Robotics Cluster]] — co-located firms, nothing to do with return-correlation structure. Context disambiguates.
3. One note, three hats. A cohort-owner note typically carries the basket identity (title / tag), the cluster verdict (callout), and the cohort measurement (prose) at once. Don't expect three separate files.
4. Prose blurs them. Day-to-day writing uses the three loosely; this glossary is the precise reference. When precision matters: cohort = input, cluster = finding, basket = instrument.

## Synthesis

The three words look interchangeable and get used loosely, but conflating them hides the two decisions that actually matter. Cohort-to-cluster is the validation question — does the market trade these names as one factor, or did taxonomy just group them by analogy? Cluster-to-basket is the construction question — given a real factor, is a bespoke basket worth building, or does a liquid ETF already replicate it? Keeping the words distinct keeps those two questions distinct. The [[Nuclear renaissance#Cluster validation|Nuclear / SMR]] case is the clean illustration: a cohort that passes the first question (it is a cluster) but fails the second (the basket is just URA/NLR) — a distinction the single word "cluster" would have flattened.

## Related

- [[Vault cluster taxonomy]] — cross-cohort meta-analysis, verdict thresholds, structural patterns
- [[Note structures]] — note-type templates and enforced rules
- [[Linking and hierarchy]] — folder rules (cohort-owner notes: Sectors/ child or Concepts/)
- [[Mag 7 cluster]] — canonical falsified cluster (a cohort that is not a cluster)
- [[Defense primes basket]] — a note carrying all three terms at once
- [[Defense Primes]] — the sector hub for the same names (the two-note pattern: industry scaffold vs validated basket)
- [[Nuclear renaissance#Cluster validation|Nuclear / SMR cluster validation]] — cohort that is a cluster but not a distinct basket
- `docs/cluster-validation.md` — the framework standard

*Created 2026-06-13.*
