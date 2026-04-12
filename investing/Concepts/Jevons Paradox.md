#concept #economics #demand

**Jevons Paradox** — Efficiency improvements in resource use increase total consumption, not decrease it. Named after William Stanley Jevons (1865) who observed coal consumption rose as steam engines became more efficient.

> **Key insight:** When something gets cheaper/more efficient, demand doesn't stay flat — it explodes. This is the core counter-argument to "efficiency will reduce GPU demand."

---

## The paradox explained

| Intuition | Reality |
|-----------|---------|
| More efficient → less demand | More efficient → lower cost → more use cases → more demand |

**Historical examples:**

| Technology | Efficiency gain | Consumption outcome |
|------------|-----------------|---------------------|
| Steam engines | 3x efficiency | Coal use increased 10x |
| LED lighting | 80% less power | Lighting usage exploded |
| Cloud compute | 90% cost reduction | Compute usage 100x |
| Air travel | Cheaper per mile | Total miles flown soared |
| Storage | $/GB dropped 1000x | Data storage exploded |
| [[Kubernetes]] (late 2010s) | Run multiple apps per server — significantly better hardware efficiency | Initial fear of reduced server/memory demand; actual outcome was lower costs driving much greater compute usage |

---

## Application to AI compute

**The [[DeepSeek]] day debate:**

| Bear case (efficiency reduces demand) | Bull case (Jevons Paradox) |
|--------------------------------------|----------------------------|
| Better algorithms → fewer GPUs needed | Cheaper inference → more AI deployed |
| MoE reduces compute per query | Lower cost → new use cases emerge |
| [[China]] proves efficiency can substitute | Total compute demand still grows |

**The resolution:** Both can be true. Compute per task falls, but number of tasks grows faster.

---

## Why Jevons applies to AI

| Factor | Why it increases demand |
|--------|------------------------|
| Price elasticity | Demand is elastic — cheaper = much more usage |
| Latent demand | Millions of use cases waiting for lower costs |
| Enterprise deployment | Companies deploy more AI when ROI improves |
| [[Consumer]] products | More AI features when inference is cheap |
| Agentic workloads | Agents run 100x more queries than humans |

---

## Counterargument: When Jevons doesn't apply

| Condition | Example |
|-----------|---------|
| Inelastic demand | Medical procedures (need-based, not price-driven) |
| Saturated market | Refrigerators (everyone already has one) |
| Regulatory limits | Carbon emissions (capped by policy) |

**Does AI fit these exceptions?** No. AI demand is highly elastic, market is unsaturated, no hard caps.

---

## Investment implications

**For [[Long NVIDIA]]:**
- Efficiency gains are real but don't kill the thesis
- Cheaper inference = more inference = more GPUs (eventually)
- Watch for demand elasticity evidence

**For [[DeepSeek day]] interpretation:**
- Market panicked about efficiency killing demand
- Jevons Paradox suggests panic was overdone
- Recovery confirmed this interpretation

**The key metric:** Total AI compute consumed, not compute per query.

---

## Application to software engineering jobs

[[Andrej Karpathy]] (No Priors, Mar 20 2026) applied the paradox to the AI-jobs debate. His canonical example: ATMs and bank tellers. ATMs were expected to eliminate tellers, but they reduced branch operating costs so much that banks opened more branches, creating more teller positions.

He sees the same dynamic for software engineering: AI agents make software dramatically cheaper to produce, which unlocks latent demand for software that was previously too expensive. Code becomes "ephemeral and modifiable" — people aren't forced to subscribe to imperfect existing tools. The demand for software "rewiring everything" could be enormous.

Karpathy is "cautiously optimistic" near-term but uncertain long-term. He points out that frontier lab researchers are actively automating themselves away — the very people building the tools acknowledge they're building their own replacement.

---

## Application to memory chips — TurboQuant (Mar-Apr 2026)

[[Google]] Research's [[TurboQuant]] algorithm (unveiled Mar 25, 2026) claimed 6x KV-cache compression and 4-8x reduction in cost-per-token for LLM inference. First-order reading: memory demand falls, [[HBM]] loses. [[Samsung]] and [[SK Hynix]] shares fell sharply, along with [[Micron]] and [[SanDisk]].

The Jevons counter-reading came from multiple voices in Seoul (Financial Times, Apr 12 2026):

- Professor Kwon Seok-joon (Sungkyunkwan University): "dramatically cheaper inference unlocks workloads previously too expensive to run" — real-time coding assistants, multiple concurrent [[AI agents|agent]] sessions — "driving total compute demand higher, not lower."
- Kim Young-gun ([[Mirae Asset]] Securities): "déjà vu" over [[Kubernetes]]. When that [[Google]]-designed containerization technology spread in the late 2010s, there were concerns that server and memory demand would fall because companies could get more from the same hardware. "In practice, the opposite occurred, with lower costs encouraging much greater usage." Kim read TurboQuant as the same shape.
- Ray Wang ([[SemiAnalysis]]): "The market has largely misread TurboQuant. We continue to believe that increasing memory demand will be required for both training and inference as AI models evolve and innovation advances."

[[Samsung]]'s Apr 8 Q1 guidance (record KRW 57.2T operating profit, [[HBM]] revenue tripled YoY) provided a real-time data point against the near-term demand-destruction reading. The guidance came two weeks after the TurboQuant blog post. Full-cycle evidence requires a longer window — TurboQuant is presented at [[ICLR]] Rio in late April 2026, and large-scale hyperscaler deployment is what will actually test the Jevons hypothesis for AI memory.

---

*Updated 2026-04-12*

---

## Related

- [[DeepSeek day]] — event (efficiency panic)
- [[TurboQuant]] — event (Mar-Apr 2026 memory-demand panic over KV-cache compression)
- [[Inference economics]] — context (cost dynamics)
- [[Long NVIDIA]] — thesis (demand durability)
- [[Agentic AI]] — driver (agents multiply inference demand)
- [[Open source commoditization]] — driver (cheaper models = more deployment)
- [[AutoResearch]] — cheaper research → more research
- [[Andrej Karpathy]] — ATM/bank teller analogy for AI jobs (Mar 2026)
- [[HBM]] — memory product at center of TurboQuant demand debate
- [[Kubernetes]] — late-2010s precedent cited by Mirae Asset's Kim Young-gun
- [[Memory shortage 2025-2026]] — the cycle TurboQuant was feared to interrupt
