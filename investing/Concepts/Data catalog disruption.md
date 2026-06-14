---
aliases: [Data catalog disintermediation, Metadata catalog disruption, Catalog layer commoditization, Data governance vendor disruption]
tags: [concept, ai, data-infrastructure, disruption, thesis]
---

# Data catalog disruption

The data-catalog and metadata-governance layer — the software that records what a company's data means, where it lives, who can use it, and how a metric is calculated — is the part of the [[Modern data stack]] most exposed to commoditization by open, agent-readable knowledge formats. The catalyst is [[Open Knowledge Format]] (OKF), published by [[Google]] Cloud on June 12, 2026: the first credible attempt to turn the proprietary contents of a catalog into portable Markdown files any tool or AI agent can read without the vendor's software. This is the [[AI disintermediation]] pattern applied one layer below the application: the value of a standalone catalog falls as the thing it sells — the mapping of data to meaning — becomes a free interchange format and the consumer of that mapping shifts from humans to agents.

---

## Synthesis

The catalog vendors built a business on owning two things: the proprietary format that trapped a company's curated metadata inside their system, and the human workflow layered on top of it. [[Open Knowledge Format]] attacks the first directly by making the metadata a portable, git-hostable Markdown bundle that any tool or agent can read for free — so the format moat, historically the stickiest asset, becomes a commodity. The defensible remainder is governance: lineage, access policy, audit, and compliance are runtime control planes, not files, and the most regulated work is the least automatable. The investable read is therefore a value migration, not an extinction: as the description layer commoditizes, value accrues to whoever produces and serves knowledge to agents — the warehouse ([[Google]] BigQuery + Knowledge Catalog, [[Snowflake]], [[Databricks]] Unity Catalog) that already holds the data and can auto-generate OKF from its own metadata — while standalone governance pure-plays ([[Collibra]], [[Alation]]) must re-justify their price on workflow rather than on owning the format. The catch for trading it: every at-risk pure-play is private, so the thesis expresses as a private-markets watch and a warehouse-over-catalog tilt, not a listed basket. The strongest counter is structural and already visible: nine months before OKF, the incumbents pre-empted exactly this by forming [[Snowflake]]'s [[Open Semantic Interchange]] (OSI) — a 50+ vendor consortium that the catalog pure-plays, the warehouses, dbt, Salesforce and even Google all joined. They are choosing to commoditize the interchange collaboratively, on terms they co-govern, rather than be commoditized by one vendor's format. So the format moat erodes either way, but the catalogs are defending up-stack (governance, lineage, active metadata) rather than being passively disrupted, and the cleanest beneficiary is the standard-setter and serving owner — [[Snowflake]] (leads OSI) and the warehouses generally — more than any single format.

---

## The layer at risk

A data catalog sits between the warehouse and the people (or now agents) that query it. What the vendors actually sell:

| Function | What it does | Commoditizable by a format? |
|----------|--------------|------------------------------|
| Metadata storage | Records table/column descriptions, owners, definitions | Yes — this is exactly what OKF encodes |
| Business glossary | Defines "active customer," revenue rules, metric lineage | Yes — OKF concepts + prose |
| Search / discovery | Lets a human find the right dataset | Partly — agents traverse links instead of searching a UI |
| Lineage | Tracks how data flows source-to-report | Harder — needs runtime observation, not just description |
| Access governance | Enforces who can see/use what | No — policy enforcement is a runtime control plane, not a file |

The moat was always twofold: the proprietary format that locked metadata inside the vendor's system, and the human workflow built on top. OKF attacks the first directly — its stated advantage is that "a description written by one tool can be read by a different tool, without conversion." The second (governance, policy, automation) is more defensible.

---

## The vendor cohort

| Vendor | Status | Valuation / deal | Exposure |
|--------|--------|------------------|----------|
| [[Collibra]] | Private | ~$5.25B peak (2021) | High — governance-heavy, format-centric moat |
| [[Alation]] | Private | ~$1.7B (Series E) | High — discovery/catalog pure-play |
| [[Atlan]] | Private | $750M (2024) | Medium — modern, agent-positioned, may co-opt OKF |
| [[Informatica]] | [[Salesforce]] subsidiary | $8B acquisition (closed Nov 18, 2025) | Absorbed into a platform; catalog is one module |
| [[Microsoft]] Purview | Bundled | Part of Azure/M365 | Low — bundled, not a pure-play P&L |
| Google Dataplex / Knowledge Catalog | Bundled | Part of Google Cloud | Beneficiary — Google authored OKF and serves it |

The structurally important point: the three at-risk pure-plays are all private, and the one that went public ([[Informatica]]) was taken private twice and ultimately absorbed by [[Salesforce]]. There is no clean listed pure-play short.

---

## The standards war — OKF vs OSI

The most important nuance, and the thing that reframes a naive "Google disrupts the catalogs" read: the catalog incumbents are not being blindsided. Nine months before OKF, [[Snowflake]] launched the [[Open Semantic Interchange]] (OSI) on September 23, 2025 — a vendor-neutral specification for the semantic model (how a metric like "active customer" is defined in machine-readable form, for consistency across BI and AI). By mid-2026 OSI was a 50+ organization coalition that includes essentially everyone with a stake: warehouses ([[Snowflake]], [[Databricks]]), the catalog pure-plays ([[Collibra]], [[Alation]], [[Atlan]]), [[Informatica]] / [[Salesforce]], dbt Labs, ThoughtSpot, Starburst, Qlik — and, tellingly, [[Google]] and AWS, which joined in November 2025.

So the landscape is two open standards at different altitudes, not one disruptor:

| | Open Semantic Interchange (OSI) | Open Knowledge Format (OKF) |
|---|---|---|
| Originator | [[Snowflake]]-led consortium | [[Google]] (single vendor) |
| Governance | 50+ member coalition | Google repo, contributions invited |
| Launched | Sept 23, 2025 | June 12, 2026 |
| Scope | Structured semantic model — metric/dimension definitions, business logic | Broad agent-readable knowledge — tables, metrics, playbooks, runbooks, prose |
| Form | Semantic-model spec (YAML) | Markdown bundles + YAML frontmatter |

The strategic read is that the incumbents chose to commoditize the interchange format collaboratively — so no single vendor owns it — while keeping their moats in the layers above (governance, lineage, automation, UX). That is the textbook incumbent response to a commoditizing standard: embrace it, co-govern it, and move the value up the stack. Google is hedging both sides — a member of OSI and the author of a parallel format it controls. The direction of the thesis (the metadata-description layer becomes a free interchange) is therefore confirmed twice over; what is contested is who captures the value the commoditization releases.

---

## Why agents change the economics

Catalogs were built for humans searching a UI. The new primary consumer is the AI agent, and agents have different requirements:

- An agent needs machine-readable context it can traverse programmatically, not a search box.
- An agent benefits from a portable bundle it can mount, not an API it must authenticate into per vendor.
- Every agent builder otherwise re-solves the same context-assembly problem against a different proprietary catalog API — the N×M problem [[MCP]] solved for tools, now for knowledge.

OKF reframes the catalog's crown-jewel asset (curated metadata) as a free, git-hostable artifact. Once the interchange is free, the vendor has to justify its price on governance, automation, and UX rather than on owning the metadata.

---

## Value migration: from catalog to serving layer

If the description format commoditizes, value accrues to whoever produces and serves the knowledge to agents — which is the warehouse, not the standalone catalog:

| Layer | Beneficiary | Why |
|-------|-------------|-----|
| Warehouse / serving | [[Google]] (BigQuery + Knowledge Catalog), [[Snowflake]], [[Databricks]] (Unity Catalog) | Owns the data and the agent-serving control plane; auto-generates OKF from its own metadata |
| Open format | The ecosystem | Free interchange lowers switching costs, erodes catalog lock-in |
| Standalone catalog | [[Collibra]], [[Alation]] | Loses the format moat; must defend on governance/UX |

[[Databricks]] open-sourced Unity Catalog (2024) and [[Snowflake]] built Horizon/Cortex into the warehouse for the same reason: the governance/semantic layer is being pulled into the platform that already holds the data. OKF accelerates that pull by making the metadata itself portable.

---

## Counter-thesis

- Governance is not a format. Lineage, access policy, audit, and compliance are runtime control planes; a Markdown bundle describes data, it does not enforce who may touch it. The hardest, most-regulated work survives.
- OKF is v0.1 from a single vendor with no incumbent adoption yet — the same posture as Google's Agent2Agent protocol. "Open standard" is an aspiration, and the catalog vendors can simply emit and ingest OKF (Atlan already positions as agent-ready), making it a feature rather than a disruptor.
- Enterprise inertia. Catalog deployments are multi-year, sticky, and tied to compliance sign-off. Formats change faster than procurement.
- UX and active metadata. Atlan's pitch is that it wins on workflow and active metadata, not on owning a proprietary file format — a dimension OKF does not touch.

---

## Tradeability — why there is no basket

This is a structural watch, not a tradeable cluster, for a concrete reason: the at-risk pure-plays ([[Collibra]], [[Alation]], [[Atlan]]) are all private, so there are no securities to assemble into a cohort or run cluster validation on. The public read-throughs are individual and diffuse, not a peer basket:

- [[Google]] / [[Alphabet]] — net beneficiary (authored OKF, serves it from BigQuery), but far too large for this to move the stock.
- [[Snowflake]] / [[Databricks]] (private) — neutral-to-beneficiary as the serving layer; the semantic layer migrating into the warehouse is additive.
- [[Salesforce]] — owns [[Informatica]]; catalog is one module inside a much larger platform story dominated by [[Agentforce]] seat-vs-consumption dynamics.

The cleanest expression is therefore a private-markets watch (do Collibra/Alation/Atlan valuations compress or get acquired into platforms?) plus a second-order tilt toward warehouse owners over standalone-governance vendors — not a long/short basket. No Gate-11 cluster validation applies because no tradeable cohort exists.

The at-risk pure-plays are all private, so there is no public price series to chart. (Market data not applicable.)

---

## Reality check — is OKF real? (June 2026)

One day after the blog post, the signal is "real but not yet consensus":

- Traction: the GoogleCloudPlatform/knowledge-catalog repo (created May 4, 2026, Apache-2.0) carried ~713 stars, 51 forks, 7 contributors and 19 open issues, with commits the same day — and the open issues are substantive spec-design debates (give OKF its own first-class repo; whether `[[wikilinks]]` belong; provenance/trust as a `timestamp` seam), i.e. genuine external engagement, not a dead drop.
- But not the consensus standard: the industry had already coalesced around [[Snowflake]]'s [[Open Semantic Interchange]] (50+ members, including the catalog incumbents and Google itself). OKF is a Google-led entrant alongside a Snowflake-led consortium, differentiated on scope (broad prose knowledge vs OSI's structured semantic model) and on Google's own serving integration.

Net: the commoditization of the description layer is real and now arriving from two directions; "Google's OKF specifically wins" is the unproven part.

---

## Confirm / kill watch-list

Confirms the thesis (value migrates off the standalone catalog):

- Standalone catalog ARR growth decelerates; a pure-play down-round or platform acquisition (most likely [[Collibra]] or [[Alation]]).
- [[Snowflake]] / [[Databricks]] / [[Google]] ship semantic + knowledge serving (OSI/OKF native) inside the warehouse and agent stack, de-emphasizing third-party catalogs.
- OKF or OSI adoption shows up as a default in shipped agent products.

Kills / counters the thesis (incumbents defend):

- Catalog vendors reposition successfully as governance / active-metadata control planes (Atlan's explicit bet) and keep growing ARR.
- OSI governance keeps the format neutral, so no single warehouse captures the released value and the catalogs retain the layers above.
- OKF stays Google-Cloud-only and fizzles — in which case the specific "Google commoditizes catalogs" leg is moot even if OSI carries the broader trend.

---

## Related

- [[Open Knowledge Format]] — the catalyst standard (market-side node; technical vault-of-record in the technologies vault)
- [[Open Semantic Interchange]] — the parallel open standard: [[Snowflake]]-led 50+ vendor consortium, semantic-model scope; the incumbents' collaborative defense
- [[Modern data stack]] — the ecosystem this layer sits in
- [[AI disintermediation]] — the parent pattern (value collapses for intermediaries between buyer and product/meaning)
- [[Agentic search infrastructure]] — the agent-facing retrieval cohort; same "build for agents, not humans" shift
- [[AI agents]] — the new primary consumer of catalog metadata
- [[MCP]] — the analogous N×M standardization, for tools rather than knowledge
- [[Collibra]] / [[Alation]] / [[Atlan]] — the at-risk pure-play cohort
- [[Informatica]] — absorbed into [[Salesforce]]
- [[Snowflake]] / [[Databricks]] — warehouse serving-layer beneficiaries
- [[Data gravity]] — why the warehouse accretes switching costs

### Cross-vault
- [Technologies: Open Knowledge Format](obsidian://open?vault=technologies&file=Open%20Knowledge%20Format) — the technical specification (format, frontmatter, design principles)

*Created 2026-06-13*
