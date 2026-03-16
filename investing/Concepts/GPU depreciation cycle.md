#concept #gpu #economics #depreciation

GPU depreciation cycle — the conventional assumption that each new GPU generation destroys the value of prior generations. The bear case ([[Michael Burry]] et al.) assumes 2-3 year useful life. The bull case: GPU value *increases* over time as models improve, because the same chip produces more tokens of a better model.

---

## Synthesis

The bear thesis is wrong in a supply-constrained world. [[Dylan Patel]] ([[SemiAnalysis]], Mar 2026) laid out why: an [[H100]] running [[GPT-5.4]] produces more tokens per GPU than it did running [[GPT-4]], because 5.4 is a sparser MoE with fewer active parameters per forward pass. The chip's economic value is set not by hardware comparisons but by the model running on it. GPT-4's TAM was maybe tens of billions of dollars. GPT-5.4's is "probably north of $100 billion." Same chip, higher value. "An H100 is worth more today than it was three years ago. That's crazy."

The depreciation argument only holds if you can build infinite quantities of the next-generation chip. You can't — [[ASML]] makes ~70 [[EUV lithography|EUV]] tools per year, growing to ~100 by 2030. So older chips get repriced to the value they can extract from newer models, not to the comparative price of newer hardware that doesn't exist in sufficient quantity. H100 rental prices have *inflected upward* — labs are signing deals as high as $2.40/hr for 2-3 year terms on hardware that costs $1.40/hr to deploy over five years.

Position: The depreciation bears are fighting the wrong model. In a chip-constrained world with rapidly improving models, GPU useful life extends, not shrinks. Long-term contract holders at old prices have locked in massive margin advantages.

---

## The bear case (Burry et al.)

| Assumption | Claim |
|-----------|-------|
| Depreciation cycle | 2-3 years (vs industry standard 5) |
| NVIDIA triples performance every 2 years | Hopper → Blackwell → Rubin |
| Price increase per generation | Only 50-100% |
| Result | Older GPU worth half or less in 2 years |

The math: if Blackwell delivers 3x performance at 2x price, the [[H100]] should drop from $2/hr to $1/hr. When Rubin ships (another 3x at ~1.5x price), the H100 falls to $0.70/hr. Standard depreciation logic.

---

## Why the bear case breaks

### 1. Model efficiency increases GPU utility

[[GPT-5.4]] is both cheaper to serve AND better than [[GPT-4]]:
- Sparser MoE → fewer active parameters per forward pass
- Training advances (RL, architecture, data quality) compound
- An H100 produces more tokens of 5.4 than it did of 4

The TAM expansion per chip generation: GPT-4 tokens maybe $10B-$30B addressable. GPT-5.4 tokens: $100B+. If AGI-class models arrive, a single H100 producing knowledge-worker-equivalent output could repay itself in months.

### 2. Supply constraint reprices old hardware UP

In a world where [[ASML]] EUV tool production (~70/year) limits total chip output to ~200 GW by end of decade, you can't build enough Rubin to replace all Hopper. So Hopper gets repriced to the value of the models running on it, not the theoretical price of newer hardware.

[[SemiAnalysis]] (Mar 2026): labs have signed H100 rental deals at $2.40/hr for 2-3 years — well above the $1.40/hr 5-year TCO. That's 70%+ gross margin for whoever locked in the supply.

### 3. Long-term contracts create margin lock-in

[[OpenAI]] signed 5-year deals at 2023-2024 pricing. Three years in, spot prices are up 50-70%. The long-term buyer has a structural margin advantage over anyone trying to acquire compute at modern pricing.

[[CoreWeave]]: 98%+ of compute on 3+ year contracts. They can't flex price on existing deals — but every incremental GW they add gets transacted at the new, higher price.

---

## The Alchian-Allen effect on AI models

Dwarkesh Patel raised an economics parallel (Mar 2026): if GPU prices rise by a fixed amount (say $1/hr), the ratio between running the best model ([[Opus 4.6]]) and a cheaper model ([[Sonnet 4.6]]) narrows. Previously Opus was 2x the cost — now it's 1.5x. So users shift to the best model, because they're paying the GPU cost anyway.

Implication: in a compute-constrained world, all the revenue concentrates on the best models. This is what [[Anthropic]] and [[OpenAI]] are seeing — "all the volumes are on the best models today."

---

## H100 pricing evidence

| Period | H100 rental rate | Notes |
|--------|-----------------|-------|
| 2024 launch | ~$2.00/hr | Market rate at volume deployment |
| Mid-2025 | $1.80-2.00/hr | Blackwell ramp expected to push down |
| Early 2026 | $2.00-2.40/hr | *Prices inflected up* — supply constrained |

5-year TCO: $1.40/hr (includes data center, networking, power, maintenance, spare parts).

At $2.40/hr on a 3-year contract, gross margins are ~70% — far above the ~35% margin at $1.90/hr over 5 years.

---

## Implications

| Stakeholder | Impact |
|-------------|--------|
| Neocloud operators ([[CoreWeave]], [[Lambda Labs]], [[Nebius]]) | Winners if locked in long-term supply at old prices |
| [[NVIDIA]] | Pricing power sustained — can charge more for each generation |
| Bears (Burry thesis) | Wrong — depreciation is slower, not faster, than hardware cycle suggests |
| AI labs | Those who committed early ([[OpenAI]]) have margin advantage over conservative buyers ([[Anthropic]]) |
| Memory makers | [[HBM]] in older GPUs still valuable → no secondhand price collapse |

---

## Related

- [[GPU deployment bottleneck]] — supply constraints that sustain pricing
- [[GPU Financing Risk]] — neocloud leverage tied to GPU residual value
- [[GPU-as-collateral]] — lending against hardware that appreciates
- [[GPU rental price index]] — tracking market rates
- [[Neocloud financing]] — how depreciation assumptions affect debt covenants
- [[H100]] — primary example of value appreciation
- [[Blackwell]] — next generation, 20x inference improvement on some workloads
- [[Rubin]] — upcoming generation
- [[ASML]] — EUV tool bottleneck that constrains new chip supply
- [[Lithography as binding constraint]] — why you can't build enough new chips
- [[SemiAnalysis]] — source of supply chain data and pricing analysis
- [[AI compute demand curve]] — demand side of the equation
- [[Anthropic vs OpenAI compute race]] — how compute strategy affects margins

*Source: [[Dylan Patel]] ([[SemiAnalysis]]) on Dwarkesh Patel podcast, Mar 13, 2026*

*Created 2026-03-16*
