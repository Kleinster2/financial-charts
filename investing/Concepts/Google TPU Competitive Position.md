#concept #ai #semiconductors #google

**Google TPU Competitive Position** — tracking how [[Google]]'s custom [[TPU]] silicon is gaining ground against [[NVIDIA]]'s GPU dominance, driven by pricing advantages, independent sales growth, and structural tailwinds from GPU financing difficulties.

---

## The shift (early 2026)

For years, TPUs were an internal Google tool with limited external relevance. That's changing:

| Signal | Detail | Date |
|--------|--------|------|
| TPU v7 reaches NVIDIA parity | 94% of GB200 TFLOPs (first time) | Dec 2025 |
| Anthropic $21B TPU purchase | Via [[Broadcom]], largest external TPU deal ever | Disclosed Feb 2026 |
| FluidStack $100M investment | Google pushing TPUs into "neo cloud" | Feb 2026 |
| GPU financing tightening | [[Blue Owl]] balked at $4B [[CoreWeave]] DC | Feb 2026 |
| Alphabet +4% on positioning | Analysts see "pole position" in AI commercialization | Feb 21, 2026 |

---

## Pricing advantage

[[Broadcom]]'s disclosure that [[Anthropic]] bought **$21B worth of TPUs** provided the first concrete external pricing data point. Key finding: **TPUs are undercutting NVIDIA on price.**

This matters because:
- NVIDIA's GPU margins (~75% gross) have been treated as untouchable
- TPU pricing pressure could force NVIDIA to compete on price for the first time
- Hyperscalers increasingly have a credible alternative at scale

Google's cost structure advantage: TPUs are designed by [[Broadcom]] (taking ~55% gross margin, ~$15B/yr), fabbed at [[TSMC]]. Google is attempting to escape this "Broadcom tax" via dual-path TPUv8 (Sunfish = Broadcom status quo, Zebrafish = direct + [[MediaTek]]). See [[Hyperscaler disintermediation]].

---

## Independent sales growth

TPUs are moving beyond Google-internal use:

| Customer | Deal | Structure |
|----------|------|-----------|
| [[Anthropic]] | ~1M TPUv7 ($21B) | Direct from Broadcom, [[FluidStack]] deploys |
| [[Hut 8]] | $7B (15yr, 245MW) | Via FluidStack |
| [[TeraWulf]] | 200MW (10yr) | Via FluidStack |

**[[FluidStack]]** is the key intermediary — Google invests, FluidStack handles deployment and operations at crypto-miner-turned-DC sites. WSJ reported Google looking to invest **$100M into FluidStack** (Feb 2026) to push TPUs further into the "neo cloud" ecosystem.

---

## GPU financing headwinds help TPUs

The [[GPU Financing Risk]] dynamic benefits Google:

1. **Lenders pulling back** — [[Blue Owl]] balked at $4B [[CoreWeave]] data center financing
2. **GPU collateral concerns** — depreciation risk, high leverage, CDS spreads elevated
3. **Google self-finances** — no third-party credit risk, no lender dependency
4. **NVIDIA's ecosystem weakens** — if neoclouds can't get financed, they can't buy GPUs

The structural advantage: Google doesn't need external financing for AI infrastructure. [[CoreWeave]], [[Lambda Labs]], and other GPU neoclouds do.

---

## Remaining limitations

| Limitation | Status |
|------------|--------|
| GCP-only availability | Still true — no on-premise TPUs |
| CUDA moat | PyTorch ecosystem still GPU-native; JAX adoption growing but niche |
| CoWoS bottleneck | TSMC packaging constrained; NVIDIA locked >50% through 2027 |
| 2026 production cut | ~4M → ~3M units due to TSMC constraints |
| Broadcom margin capture | ~55% gross margin "tax" until disintermediation succeeds |

TPUs win on price and vertical integration. NVIDIA wins on ecosystem breadth and software. The question is whether price + scale tips the balance.

---

## Apr 2026: $3.5 GW expansion, MediaTek stumbles, Gemini tensions

### $3.5 GW Anthropic deal

[[Anthropic]] expanded its Google [[TPU]] partnership to ~3.5 GW starting 2027 (confirmed by press releases from both Anthropic and Google Cloud, Apr 6). [[Broadcom]] supply assurance agreement through 2031 ([[Mizuho]] estimates $80B+ cumulative revenue; AVGO +6%). ~$175B all-in at ~$50B/GW rule of thumb. Orders of magnitude beyond the original 1 GW commitment.

### [[MediaTek]] struggling

[[MediaTek]]'s Google TPU work faces delays. The bottleneck is [[TSMC]]'s limited CoWoS advanced packaging capacity plus Google engineering changes that pushed tape-out to mid-2026; volume production unlikely before 2027 (Digitimes, SemiWiki). If MediaTek can't deliver on schedule, the Zebrafish disintermediation path weakens — and [[Broadcom]]'s ~55% gross margin "tax" persists longer. Google's diversification strategy depends on MediaTek execution that is slipping.

### Internal Google tension: Gemini vs GCP

[[NEA]]'s Neimucha (The Information, Apr 7) characterized internal friction at [[Google]]: the [[Gemini]] / [[Google DeepMind]] team unhappy that GCP ([[Thomas Kurian]]) is allocating TPU capacity to [[Anthropic]] — a direct competitor. No independent corroboration of this claim found in Bloomberg, Reuters, or other reporting. However, the structural tension is plausible: GCP is incentivized on cloud revenue, DeepMind on frontier research progress, Search on defending ad revenue — different business models competing for the same TPU capacity. Neimucha: "this big tech aggregation political dynamic story ends up being a big part of whether they're able to work through it."

Google has also been criticized for not booking enough [[TSMC]] capacity overall — a strategic undercommitment compared to [[OpenAI]]'s aggressive approach.

*Sources: Anthropic press release (Apr 6), Google Cloud press release (Apr 6), Bloomberg (Apr 6), CNBC (Apr 6), Digitimes (Apr 7), Mizuho (Apr 7). Internal tension claim: Neimucha on The Information (Apr 7) only — uncorroborated.*

---

## Apr 22, 2026: 8th-gen unveiling at Cloud Next 2026, customer roster, Epoch compute share

At Google Cloud Next 2026 in Las Vegas (Apr 22 2026), [[Google Cloud]] unveiled the 8th generation of [[TPU]] as two distinct chips:

- **TPU 8t** — training-optimised, the successor to TPU v7 ("Ironwood") at the frontier-training tier.
- **TPU 8i** — inference-optimised with more memory, designed for the agentic-era inference workload.

Split-purpose design is the headline architectural shift, tracking the industry move toward dedicated training-vs-inference silicon (see [[Training-inference convergence]]).

### Customer roster (Cloud Next 2026 + FT)

[[Thomas Kurian]] said nine of the top ten AI labs use [[TPU]]. The publicly named or publicly disclosed customer set as of Apr 2026:

| Customer | Status |
|---|---|
| [[Anthropic]] | Largest external TPU customer; Apr 2026 deal "up to one million TPUs" plus 5 GW [[Google Cloud]] capacity over 5 years; [[Broadcom]]-fabricated supply through 2031 |
| [[Apple]] | Apple Intelligence training partly on TPU |
| [[Meta]] | Multibillion-dollar multiyear deal signed Feb 2026 — new development |
| [[OpenAI]] | Now taking TPU capacity in 2026 — meaningfully revises the prior "Microsoft-exclusive" framing Kurian gave the FT |
| [[Safe Superintelligence]] | Named at Cloud Next 2026 |
| [[Thinking Machines Lab]] | Named by Kurian (FT) — confirms [[Mira Murati]]'s lab on TPU |
| [[Midjourney]] | Named at Cloud Next 2026 |
| [[Salesforce]] | Named at Cloud Next 2026 |
| [[Figma]] | Named at Cloud Next 2026 |
| [[Palo Alto Networks]] | Named at Cloud Next 2026 |
| [[Cursor]] | Named at Cloud Next 2026 |
| [[Citadel Securities]] | Quant research workflows on TPU |
| All 17 [[US]] DoE national labs | AI co-scientist software on TPU |

The roster directly contradicts [[Jensen Huang]]'s "100 per cent of TPU demand comes from [[Anthropic]]" framing. Anthropic is the largest external customer in dollar terms, but it is not the only one — multiple top-tier frontier labs and large enterprise buyers are publicly disclosed.

### OpenAI on TPU is the more significant new datapoint

[[Kurian]] told [[FT]] that [[OpenAI]] is excluded by [[Microsoft]] exclusivity. Independent reporting around [[Cloud Next 2026]] indicates [[OpenAI]] is now taking [[TPU]] capacity in 2026 anyway. If correct, that is a structural break in the [[OpenAI]] / [[Microsoft]] / [[Azure]] arrangement and a tail-risk to Microsoft's incumbent position in the most valuable AI customer relationship. Worth tracking through Q2/Q3 2026 reporting.

### Epoch global compute share

[[Epoch AI]] (cited by [[FT]]): [[Google]] now controls roughly **25% of global AI computing power**, comprising **~3.8M TPUs and ~1.3M GPUs**. [[Microsoft]] is the next largest holder at **~3.2M [[NVIDIA]] GPUs**. First publicly cited like-for-like compute-share comparison; the cleanest data point for the "Google is closing the AI gap" thesis.

### Huang's narrower critique still lives

Independent benchmark submission (MLPerf etc.) is the part of [[Jensen Huang]]'s critique that survives the customer-list contradiction. TPU 8t / 8i have not been submitted to MLPerf. Until they are, the chip-spec dispute is real even when the customer-share dispute is resolved. See [[Jensen Huang]] for the full rebuttal.

### Internal tension on TPU allocation — corroborated

Independent reporting around Cloud Next 2026 corroborates the earlier Neimucha/The Information account (Apr 7) of internal Google tension over [[TPU]] allocation between [[Google Cloud]] (under [[Thomas Kurian]]), [[Google DeepMind]] / [[Gemini]], and consumer-Google products. The structural reading: [[Kurian]] received expanded allocation authority that lets [[Google Cloud]] sell scarce [[TPU]] capacity directly to external customers — including the [[Anthropic]] anchor — rather than route through approval from another Google unit. This is the source of the tension: [[DeepMind]] and the [[Gemini]] team argue capacity allocated to a frontier rival is capacity not training their own next model.

[[Sundar Pichai]] has framed [[Google Cloud]] as "one of the most important priorities for [[Alphabet]]," which reads as cover for the allocation decision rather than a resolution of the trade-off.

[[FT]] Anthropic deal context: total Anthropic Google package now reads as ~$200B+ over five years (5 GW of [[Google Cloud]] capacity + up to $40B equity from [[Google]]), see [[Anthropic hyperscaler financing surge April 2026]] and [[Google Cloud]] for the deal mechanics.

*Sources: FT, Apr 26 2026; Google Cloud Next 2026 keynote, Apr 22 2026; CNBC, TechCrunch, Digitimes (Apr 22-23 2026); SemiAnalysis (TPUv7 → TPU 8 lineage); The Information (internal tension reporting, Apr 7 + Apr 22-23); Stratechery / Ben Thompson interview with Kurian (Apr 2026).*

---

## Related

- [[TPU]] — product detail (architecture, versions, specs)
- [[Google]] — parent actor
- [[NVIDIA]] — competitor
- [[Broadcom]] — TPU design partner, $21B Anthropic disclosure
- [[Anthropic]] — largest external TPU customer ($21B)
- [[FluidStack]] — deployment layer for external TPU deals
- [[Hyperscaler disintermediation]] — Broadcom margin escape
- [[GPU Financing Risk]] — structural tailwind for TPU adoption
- [[CoreWeave]] — GPU neocloud facing financing headwinds
- [[AI accelerators]] — broader competitive landscape
