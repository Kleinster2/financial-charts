---
aliases: [GCP, Google Cloud Platform]
tags: [cloud, ai]
---
#actor #cloud

Google Cloud — cloud computing division of [[Alphabet]]/[[Google]], third-largest cloud provider behind [[AWS]] and [[Microsoft]] Azure. Offers [[Google]] [[TPU]] infrastructure alongside [[NVIDIA]] GPUs. Run since November 2018 by [[Thomas Kurian]], who joined from [[Oracle]] and is one of the named candidates to succeed [[Sundar Pichai]] as Alphabet CEO.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Alphabet]] / [[Google]] |
| CEO | [[Thomas Kurian]] (since Nov 2018) |
| Market position | #3 global cloud |
| Cloud market size | ~$418B (Apr 2026) |
| Market share | ~14% (up from ~7% in late 2018) |
| Q4 2025 revenue growth | +48% YoY |
| 2024 revenue | $43B |
| 2026 revenue track | >$70B |
| 2026 Alphabet capex guide | $185B |
| AI hardware | [[TPU]] (proprietary, 8th gen unveiled Apr 2026) + [[NVIDIA]] GPUs |

---

## Why Google Cloud matters for this vault

Google Cloud is the only top-three hyperscaler with proprietary frontier AI silicon ([[TPU]]), a frontier first-party model ([[Gemini]] / [[Google DeepMind]]), and a complete cloud distribution stack — all in-house. The Apr 2026 [[Anthropic]] anchor deal makes it the largest external [[TPU]] capacity provider, while the same chips power Google's own AI products. This creates a structural tension — selling scarce capacity to a [[Gemini]] rival — that [[Thomas Kurian]] runs as an explicit business decision rather than treating as a conflict to be resolved. The cycle the vault tracks is whether GCP's "full-stack" framing actually earns the gross-margin advantage Kurian claims, or whether the [[NVIDIA]] / [[CUDA]] ecosystem incumbency keeps GCP a structural #3.

---

## Market position and share growth

Under [[Thomas Kurian]] (Nov 2018 → Apr 2026), [[Google Cloud]] roughly doubled its share of the global cloud market from ~7% to ~14% (~$58B run rate inside a ~$418B market), but it remains a distant #3 to [[AWS]] and [[Microsoft]] [[Azure]]. Q4 2025 revenue grew 48% year on year — the fastest pace among the three hyperscalers — driven by AI workloads and the broadening external [[TPU]] customer base.

| Hyperscaler | Compute footprint (Epoch AI estimate, Apr 2026) | Cloud market share |
|---|---|---|
| Google | ~3.8M [[TPU]]s + ~1.3M GPUs (~25% of global AI compute) | ~14% |
| Microsoft | ~3.2M NVIDIA GPUs | #2 |
| Amazon ([[AWS]]) | Trainium/Inferentia + NVIDIA GPUs | #1 |

Source for Epoch estimate: report cited by [[FT]] (Apr 26 2026) — see [[Epoch AI]].

---

## Apr 22, 2026: Cloud Next 2026, TPU 8t / 8i unveiling

At Google Cloud Next 2026 in Las Vegas (Apr 22 2026), Google Cloud unveiled the 8th generation of [[TPU]] as two distinct chips: **TPU 8t** (training) and **TPU 8i** (inference, more memory). The agentic-era split tracks the broader industry move from a single all-purpose chip toward dedicated training-vs-inference silicon (see [[Training-inference convergence]] and [[Google TPU Competitive Position]] for competitive structure).

### Customer roster as named

[[Thomas Kurian]] said nine of the top ten AI labs use [[TPU]]. The publicly named or publicly disclosed customer set:

- [[Anthropic]] — largest external customer ("up to one million TPUs," 5 GW capacity, $40B Google equity)
- [[Apple]] — Apple Intelligence training partly on TPU
- [[Meta]] — multibillion-dollar multiyear deal signed Feb 2026
- [[OpenAI]] — now taking TPU capacity in 2026 (the FT framing of "[[Microsoft]] exclusivity" appears to be at least partly outdated as of Cloud Next)
- [[Safe Superintelligence]], [[Thinking Machines Lab]] ([[Mira Murati]]), [[Midjourney]], [[Salesforce]], [[Figma]], [[Palo Alto Networks]], [[Cursor]] — all named at Cloud Next
- [[Citadel Securities]], 17 US DoE national labs — enterprise / national-lab tier

The roster directly contradicts [[Jensen Huang]]'s "100 per cent of TPU demand comes from [[Anthropic]]" rhetorical claim.

### Huang's narrower critique survives

[[Jensen Huang]] criticised Google for not submitting [[TPU]]s to independent benchmark tests. TPU 8t / 8i have not been submitted to MLPerf. The chip-spec dispute is real even when the customer-share dispute is settled.

### Epoch compute-share datapoint

[[Epoch AI]] (cited by FT): Google ≈ 25% of global AI compute (~3.8M TPUs + ~1.3M GPUs) versus [[Microsoft]] ~3.2M [[NVIDIA]] GPUs. First publicly cited like-for-like compute-share number.

*Sources: FT (Apr 26 2026); Google Cloud Next 2026 keynote (Apr 22 2026); CNBC, TechCrunch, Digitimes (Apr 22-23 2026); SemiAnalysis on TPUv7 → TPU 8 lineage.*

---

## Kurian on stack economics (Apr 2026)

In the same FT interview, [[Thomas Kurian]] framed Google Cloud's cost structure as the source of its competitive advantage: "We're not just a hyperscaler reselling other people's technology. Our differentiation comes down to the fact that we own the IP, the model and the chips are ours. For every dollar of revenue, we're not shipping 80 per cent of it to either a model or chip provider, which allows us to invest more."

The structural argument:

- [[AWS]] and [[Azure]] sell mostly [[NVIDIA]]-powered AI compute, which means a large share of revenue passes through to [[NVIDIA]]'s ~75% gross margin and to [[OpenAI]]/[[Anthropic]]/[[Mistral]]/etc. in licence economics.
- Google internalises both layers: [[TPU]]s are designed by [[Broadcom]] and fabbed at [[TSMC]] (with the dual-path TPUv8 attempt to escape the Broadcom margin), and [[Gemini]] / [[Google DeepMind]] is the first-party model.
- The 12-year [[Google DeepMind]] investment is what Kurian pointed to as the source of compounded chip-and-model improvement, and what other hyperscalers cannot replicate without an in-house frontier lab.

The verifiable parts of this claim are pricing-sensitive: the [[Google TPU Competitive Position]] note tracks whether external [[TPU]] pricing is in fact undercutting [[NVIDIA]] enough to translate Kurian's "more to invest" argument into share gains.

---

## Kurian on AI shakeout (Apr 2026)

Kurian also publicly forecast a multi-year AI provider shakeout, identifying the funding model as the binding constraint: "Those AI providers depend on private capital markets, which are reaching a saturation point. If you're going to go public, you can't be lossmaking forever. And if you stay private, you cannot raise venture money forever."

He projected: "Over the next year to two you will see some shakeout in the market. Whether particular providers are going to make it or not largely comes down to the economics."

This is the most direct statement to date from a hyperscaler CEO that the private AI lab layer is approaching a financing ceiling — coming from someone whose own [[Google Cloud]] business is benefiting from the same labs' compute commitments. Kurian's incentive to make this call out loud is non-trivial: it pre-positions [[Anthropic]] (a Google customer / investee) as the survivor and reframes Google Cloud's $40B Anthropic commitment as a vote of confidence rather than balance-sheet risk.

For the broader cycle context see [[Hyperscaler capex]], [[AI infrastructure financing risk]], and [[Anthropic vs OpenAI compute race]].

*Source: FT, Apr 26 2026.*

---

## 2026 capex

[[Alphabet]] guided 2026 capital expenditure to ~$185B, a sharp increase from the 2025 levels reported in [[Hyperscaler capex]]. Kurian framed the spending as justified by customer demand and the resulting cloud-revenue trajectory — the same narrative he is using to defend the [[Anthropic]] capacity allocation against internal [[Gemini]] / [[Google DeepMind]] concerns.

---

## Anthropic capacity anchor (Apr 2026)

[[Anthropic]] has become one of Google Cloud's most important AI infrastructure customers. The Apr 2026 package combines a reported 5 GW of Google Cloud capacity over five years with [[Google]]'s $10B upfront / up to $40B total equity commitment to Anthropic. This sits on top of the Apr 6 Google + [[Broadcom]] agreement for multiple gigawatts of next-generation [[TPU]] capacity starting in 2027, later reported at about 3.5 GW.

The strategic tension is that Google Cloud is selling scarce TPU capacity to the strongest independent rival to [[Gemini]]. The cloud logic is still clear: if frontier-model demand is the bottleneck, Google can win by being a platform supplier even when Google DeepMind is not the model winner.

See [[Anthropic hyperscaler financing surge April 2026]] and [[Anthropic vs OpenAI compute race]].

---

## Related

- [[Thomas Kurian]] — CEO since Nov 2018
- [[Google]] — parent company
- [[Alphabet]] — holding company
- [[Sundar Pichai]] — Alphabet CEO
- [[Google DeepMind]] — sister AI division (12-year investment, Gemini origin)
- [[Gemini]] — first-party frontier model
- [[TPU]] — proprietary silicon (8th gen unveiled Apr 2026)
- [[Google TPU Competitive Position]] — competitive structure
- [[AWS]] — cloud competitor (#1)
- [[Microsoft]] — Azure cloud competitor (#2)
- [[NVIDIA]] — GPU supplier and rival; [[Jensen Huang]] criticised TPU benchmarking
- [[Anthropic]] — anchor TPU customer (Apr 2026 deal)
- [[Anthropic hyperscaler financing surge April 2026]] — event detail
- [[Mira Murati]] / [[Thinking Machines Lab]] — TPU customer
- [[Epoch AI]] — source for compute-share estimates
- [[Hyperscaler capex]] — Alphabet $185B 2026 guide
- [[AI infrastructure financing risk]] — circular financing context
- [[Anthropic vs OpenAI compute race]] — relative-positioning context
