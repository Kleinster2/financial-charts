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

*Updated 2026-03-21*

---

## Related

- [[DeepSeek day]] — event (efficiency panic)
- [[Inference economics]] — context (cost dynamics)
- [[Long NVIDIA]] — thesis (demand durability)
- [[Agentic AI]] — driver (agents multiply inference demand)
- [[Open source commoditization]] — driver (cheaper models = more deployment)
- [[AutoResearch]] — cheaper research → more research
- [[Andrej Karpathy]] — ATM/bank teller analogy for AI jobs (Mar 2026)
