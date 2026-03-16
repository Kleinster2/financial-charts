#concept #ai #compute #strategy #competition

Anthropic vs OpenAI compute race — the divergent strategies on securing AI compute capacity, and why [[Anthropic]]'s conservatism is now costing it while [[OpenAI]]'s aggression is paying off.

---

## Synthesis

The compute race between [[Anthropic]] and [[OpenAI]] is a case study in commitment vs optionality under uncertainty. [[OpenAI]] went aggressive: signed "crazy fucking deals" with [[CoreWeave]], [[Oracle]], [[SoftBank]], NScale, and others before having the money to pay for them. Got roasted for it in H2 2025 when credit markets freaked out and stock prices tanked. Then raised $110B and validated the entire approach.

[[Anthropic]] was conservative: [[Dario Amodei]] explicitly said he didn't want to "go crazy on compute" and risk bankruptcy. Signed principled contracts, purposely undershot estimates. Now scrambling as revenue moons ($4-6B/month adds) and compute is the binding constraint on growth. "The reliability of Claude is quite low because they're so compute constrained."

[[Dylan Patel]] ([[SemiAnalysis]], Mar 2026): Anthropic "screwed the pooch compared to OpenAI." They have to go to lower-quality providers and pay premium spot rates. OpenAI has "way more access to compute than Anthropic by the end of the year." But both converge to ~10 GW by end of 2027.

---

## The strategic divergence

### OpenAI: commit early, worry about payment later

| Move | Detail |
|------|--------|
| 5-year contracts | Vast majority of compute on long-term deals at 2023-2024 prices |
| Provider diversity | [[Microsoft]], [[Google]], [[Amazon]], [[CoreWeave]], [[Oracle]], SoftBank Energy, NScale |
| SoftBank Energy | "Never built a data center in their life" — building them now for OpenAI |
| Risk acceptance | Signed deals before having the capital |
| H2 2025 fallout | Credit markets panicked — "OpenAI signed all these deals but didn't have the money" |
| Resolution | Raised $110B → "Oh wait, they can pay for it. Fine." |
| Year-end 2026 capacity | 6+ GW (slightly above Anthropic) |

### Anthropic: be principled, don't risk bankruptcy

| Move | Detail |
|------|--------|
| Conservative contracts | "Sign contracts, but be principled. Purposely undershoot" |
| Provider selection | Historically best providers — [[Google]], [[Amazon]] |
| Dario's rationale | "If my revenue inflects at a different rate... I don't want to go bankrupt" |
| Problem | Revenue inflected far faster than expected |
| Now scrambling | Going to lower-quality providers it wouldn't have chosen before |
| Paying premium | H100 spot deals at $2.40/hr for 2-3 years (vs $1.40/hr TCO) |
| Revenue share costs | 50% markup via Bedrock/Vertex/Foundry revenue shares |
| Year-end 2026 capacity | 5-6 GW (via own + Bedrock/Vertex/Foundry) |

---

## The Google TPU deal

One of the most revealing episodes in the compute race.

[[Google]] sold 1 million [[TPU]] v7s (Ironwood) to [[Anthropic]]. [[Google DeepMind]] people "were like, 'This is insane. Why did we do this?'" But Google Cloud saw a different calculus.

Timeline:
1. Early Q3 2025: Anthropic's compute team (both ex-Google) saw a dislocation
2. Over 6 weeks, TPU capacity requests went up multiple times
3. Google had to explain to [[TSMC]] why they needed a sudden capacity increase
4. Much of that increase was for selling to Anthropic
5. Then Gemini Nano Banana / Gemini 3 caused Google's own user metrics to skyrocket
6. Google leadership: "Oh. We need to double compute every six months"
7. Went to TSMC for more capacity → "Sorry, sold out. Maybe 5-10% more for 2026, really working on 2027"

Information asymmetry: Anthropic saw the revenue inflection before Google did. Anthropic's compute team knew what was coming. Google was still looking at near-zero Gemini ARR through Q1-Q3 2025. By Q4, Google hit $5B Gemini ARR — but by then TSMC was allocated.

---

## Cost of being late

### Premium spot compute

Labs signing H100 deals at $2.40/hr for 2-3 years — on hardware that costs $1.40/hr to deploy over 5 years. This is 70%+ gross margin for the provider, paid because the buyer needs capacity NOW.

The neoclouds ([[CoreWeave]], [[Lambda Labs]], [[Nebius]], [[Together AI]]) had a higher percentage of [[Hopper]] and shorter-term deals. As contracts roll off, the highest bidder (AI labs) crowd out prior customers.

### Revenue share tax

[[Anthropic]] doesn't need to own all its compute directly. [[Amazon]] can serve via Bedrock, [[Google]] via Vertex, [[Microsoft]] via Foundry — with revenue share. But that's a 50% margin hit compared to owning the compute outright.

### Opportunity cost

Revenue growth is constrained by compute availability. Every month of capacity constraint = billions in foregone revenue. "The reliability of Claude is quite low because they're so compute constrained."

---

## Who controls what (by year-end 2026)

| Entity | Estimated capacity | Notes |
|--------|-------------------|-------|
| [[OpenAI]] | 6+ GW | Slightly above Anthropic; diverse provider base |
| [[Anthropic]] | 5-6 GW | Via own + Bedrock/Vertex/Foundry; was "way above initial plans" |
| [[Google]] | Undisclosed | "Absurdly AGI-pilled" since late 2025; buying energy companies, turbine deposits |
| [[Meta]] | Adding 2022-fleet-equivalent this year | ~100% internal use |

By year-end 2027: both OpenAI and Anthropic targeting ~10 GW each.

---

## Lessons

1. In a takeoff, commitment beats optionality. The margin advantage of early long-term contracts compounds — OpenAI locked in 2023 prices that are now 50-70% below spot.

2. Revenue is the best fundraising argument. OpenAI couldn't get deals signed for 4 months in H2 2025 ("you don't have the money"). After raising $110B: "we believed you the whole time."

3. Information asymmetry creates first-mover advantage. Anthropic's compute team (ex-Google) saw the TPU dislocation before Google did. But Anthropic's leadership was too conservative to fully exploit it.

4. Having the best model is a durable advantage — not because the model lead lasts, but because the revenue it generates lets you sign the compute deals that lock in margins for years.

5. "Commitment issues" is a meme for a reason. Patel: "In Anthropic fashion, there's a bit of a meme that they have commitment issues and are sort of polyamorous."

---

## Related

- [[Anthropic]] — the conservative player
- [[OpenAI]] — the aggressive player
- [[Google]] — woke up late, now "absurdly AGI-pilled"
- [[CoreWeave]] — major OpenAI provider, 98%+ on 3+ year contracts
- [[GPU depreciation cycle]] — why early commitment pays off
- [[AI compute demand curve]] — the demand driving the race
- [[Lithography as binding constraint]] — why compute is scarce
- [[GPU rental price index]] — tracking spot prices
- [[Neocloud financing]] — provider economics
- [[SemiAnalysis]] — supply chain data source

*Source: [[Dylan Patel]] ([[SemiAnalysis]]) on Dwarkesh Patel podcast, Mar 13, 2026*

*Created 2026-03-16*
