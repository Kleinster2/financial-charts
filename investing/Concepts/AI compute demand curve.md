#concept #ai #compute #infrastructure #scaling

AI compute demand curve — the gigawatt-level projections for AI data center capacity through 2030, and why the supply chain can't keep up. The gap between what AI labs want and what the semiconductor industry can produce is the defining tension in AI infrastructure.

---

## Synthesis

The numbers are staggering and accelerating. ~20 GW of incremental AI data center capacity is being added in 2026. [[Sam Altman]] wants 52 GW/year by 2030. [[Elon Musk]] wants 100 GW/year. [[Anthropic]] and [[OpenAI]] each targeting ~10 GW by end of 2027. The semiconductor supply chain, constrained by [[ASML]] EUV tool production, can produce at most ~200 GW total by end of decade — and that's the ceiling with 100% AI allocation.

[[Dylan Patel]] ([[SemiAnalysis]], Mar 2026) frames the core problem: AI demand doubles or triples annually, but the supply chain thinks it's expanding fast at 10-15% annual growth. Every player in the chain is building X-1 (or X÷2) of what the AI labs actually need, because "they're not AGI-pilled." The information asymmetry flows one direction: the labs see the revenue and capability curves; the supply chain sees last year's orders.

Nearly $1T in CapEx is being invested in US data centers this year. The ROIC looks extremely high given [[Anthropic]]'s revenue trajectory ($4-6B/month adds). The question is no longer whether AI scaling happens — it's who captures the margin as each link in the chain becomes the binding constraint.

---

## Current and projected capacity

### AI lab compute (critical IT capacity)

| Entity | Current (early 2026) | Year-end 2026 | Year-end 2027 |
|--------|---------------------|---------------|---------------|
| [[Anthropic]] | ~2-2.5 GW | 5-6 GW | ~10 GW |
| [[OpenAI]] | ~2 GW (exited 2025) | 6+ GW | ~10 GW |
| [[Google]] | Undisclosed | Undisclosed | Undisclosed |
| [[Meta]] | Adding 2022-fleet-equivalent in 2026 alone | — | — |

Note: critical IT capacity. Gross up 20-30% for transmission losses, cooling, and capacity factors.

### Hyperscaler CapEx (2026)

| Company | 2026 CapEx | Notes |
|---------|-----------|-------|
| [[Amazon]] | ~$200B | Largest ever |
| [[Google]] | ~$180B | Includes turbine deposits for 2028-29 |
| [[Meta]] | ~$100B+ | Adding more capacity than entire 2022 fleet |
| [[Microsoft]] | ~$100B+ | — |
| Total Big 4 | ~$600B | ~$1T across full supply chain |

A big chunk of this is not for compute going online this year. Google's $180B includes turbine deposits for 2028-29, data center construction for 2027, and power purchasing agreements far into the future.

### Demand targets (2030)

| Source | Target | Notes |
|--------|--------|-------|
| [[Sam Altman]] | 52 GW/year | ~25% of total chip production — "very reasonable" |
| [[Elon Musk]] | 100 GW/year (in space) | Patel: "not this decade" |
| [[Anthropic]] | Comparable to OpenAI | Would need similar scale |
| [[Google]] | Aggressive (undisclosed) | "Absurdly AGI-pilled" since late 2025 |

### Supply ceiling

~200 GW total by end of decade, constrained by [[ASML]] EUV tool production (~700 cumulative tools ÷ 3.5 per GW). See [[Lithography as binding constraint]].

---

## Revenue math: why labs need the compute

### Anthropic's compute requirement

| Metric | Value |
|--------|-------|
| Revenue adds | $4B (Jan 2026), $6B (Feb 2026) |
| Projected annual adds | ~$60B over next 10 months (linear extrapolation — "bears would argue this is bearish") |
| Gross margins | Sub-50% (per The Information) |
| Implied compute spend | ~$40B for $60B revenue |
| Rental cost per GW | ~$10-13B |
| Inference capacity needed | ~4 GW just for revenue growth |
| Plus training fleet (flat) | ~1-1.5 GW |
| Total needed by year-end | 5-6 GW |

This is why [[Anthropic]] is scrambling — conservative compute strategy is now the binding constraint on revenue growth. "The reliability of Claude is quite low because they're so compute constrained."

### The ROIC argument

~$50B of CapEx was laid out by hyperscalers to support Anthropic's current $20B ARR. If Anthropic 10x's revenue again ("when, not if" — Patel), the ROIC on data center CapEx is extremely high.

China hasn't made comparable infrastructure investments. If fast takeoff continues, the US diverges from China economically. If AI disappoints, the US has over-invested and China's indigenous supply chain catches up.

---

## Where margin accrues

In a chip-constrained world, who captures the margin depends on the bottleneck:

| Supply chain position | Margin capture |
|----------------------|---------------|
| Model vendors ([[Anthropic]], [[OpenAI]]) | Rising — must destroy demand via pricing because capacity-constrained |
| Cloud providers ([[CoreWeave]], hyperscalers) | Limited by long-term contracts (98%+ on 3+ year deals) — incremental adds priced higher |
| Chip vendors ([[NVIDIA]]) | Massive — $90B in long-term contracts, 3-year memory deals |
| Memory vendors ([[SK Hynix]], [[Samsung]], [[Micron]]) | Rising — prices tripled, signing long-term AI deals |
| [[TSMC]] | Could take more but conservative |
| [[ASML]] | Leaves margin on table — "most generous company in the world" |

The margin distribution is unstable. Whoever controls the scarcest resource at any given moment extracts the margin — until [[TSMC]] or [[ASML]] decide to charge more.

---

## The AGI-pill gradient

Patel's key insight: each link in the supply chain is less "AGI-pilled" than the one above it.

```
AI labs (most AGI-pilled) → want X
NVIDIA → builds X - 1
Hyperscalers → X - 1
Memory vendors → X - 1 or X ÷ 2
TSMC → X ÷ 2
ASML → X ÷ 2
Zeiss/Cymer → X ÷ 2 ("we're growing a lot because of AI")
```

The whip takes years to propagate. By the time [[Carl Zeiss SMT|Zeiss]] understands they need to double lens production, the labs have already been capacity-constrained for 2-3 years.

---

## Fast timelines vs long timelines (US vs China)

| Scenario | Winner | Why |
|----------|--------|-----|
| Fast takeoff (AGI by 2028-2030) | US/West | $1T+ CapEx deployed, revenue compounding, labs at 10+ GW |
| Slow takeoff (AGI by 2035+) | [[China]] | Fully indigenized supply chain, more engineers, more capital, verticalized |

Currently: [[Opus 4.6]] and [[GPT-5.4]] have "really pulled away" from Chinese models. US labs scaling to 10 GW each by 2027. China hasn't built comparable infrastructure. But if timelines extend, China could produce 100+ DUV tools/year by 2030 (ASML does hundreds), have working EUV, and potentially out-scale the fragmented Western supply chain.

---

## Related

- [[Lithography as binding constraint]] — the ultimate ceiling on compute scaling
- [[GPU depreciation cycle]] — why GPU value increases as models improve
- [[Hyperscaler capex]] — the spending driving demand
- [[Power constraints]] — prior bottleneck (now solvable)
- [[Memory shortage 2025-2026]] — memory as co-constraint
- [[ASML]] — EUV tool production ceiling
- [[TSMC]] — fabrication capacity
- [[NVIDIA]] — chip supply and pricing power
- [[Anthropic vs OpenAI compute race]] — how labs compete for scarce capacity
- [[SemiAnalysis]] — data source for supply chain tracking
- [[Space data centers]] — proposed alternative (not viable this decade)
- [[AI Infrastructure]] — sector overview

*Source: [[Dylan Patel]] ([[SemiAnalysis]]) on Dwarkesh Patel podcast, Mar 13, 2026*

*Created 2026-03-16*
