---
aliases: [AI research automation, full AI R&D automation, automated AI R&D, ASARA, SAR]
tags: [concept, ai, compute, model-labs]
---

# AI R&D automation

AI R&D automation is the point at which AI systems can perform enough frontier-model research that human research labor stops being the main constraint on AI progress. In the investing vault it matters because it changes compute from a training input into a combined training, experimentation, and AI-labor input.

---

## Synthesis

The market-facing version of the AI R&D automation question is not "does the singularity happen?" It is whether model progress becomes materially faster before any true runaway. [[Ryan Greenblatt]]'s May 2026 Redwood Research post is useful because it argues that the answer can be yes even when the software feedback loop is subcritical. Full automation can create a large one-time research-speed step-up, and it can raise the return to every marginal unit of compute by making compute improve the AI labor force that is doing the research.

That reframes the [[AI compute demand curve]]. Before full automation, more compute mostly means bigger training runs, more experiments, and more inference. After full automation, more compute also means more AI researchers, faster AI researchers, and better AI researchers. A model lab with more compute is not only serving more revenue; it is potentially buying a faster capability-improvement loop.

The important caveat is that this is a forecast framework, not a settled empirical fact. Greenblatt's own post distinguishes between model output and his actual expectation, notes that earlier partial automation would consume some of the one-time gains before "full automation," and flags that compute scaling could be slower by the time full AI R&D automation arrives. The investable consequence is therefore conditional: if frontier labs approach AI R&D automation while compute remains scarce, the value of reliable, deliverable compute rises because it affects both revenue capacity and research velocity.

---

## Mechanism

| Channel | Before AI R&D automation | After AI R&D automation |
|---------|--------------------------|-------------------------|
| Research labor | Human researchers and engineers are the scarce cognitive input | AI labor can run more of the research loop directly |
| Compute | Used for training, inference, and experiments | Also used to run, speed up, and improve the AI researchers |
| Lab lead | Model lead can decay as competitors hire talent and buy compute | Software lead may convert into compute/revenue advantage faster |
| Bottleneck | Human taste, experiment design, compute, data, organizational speed | Compute, verification, taste, safety controls, and physical scale-up |

Greenblatt's core claim is that even if the recursive software loop has `r < 1` and therefore does not become a sustained [[Software-only singularity]], the first year after full automation can still be a large discontinuity. His cited model run with `r=0.7` produces about 3.5 years of progress in the first year with no compute scale-up; his adjusted intuition after accounting for prior partial automation is closer to 2.5 years.

The second mechanism is more directly market-relevant. Once AI labor is doing AI R&D, each additional unit of compute can support more experiments, bigger training runs, more AI laborers, faster AI laborers, and better future AI laborers. That makes compute demand more convex around the automation boundary.

## Control protocol design: retrying vs resampling

Redwood's May 29 2026 follow-up narrows the control problem from "monitor the untrusted model" to "choose protocols that do not teach the untrusted model how to evade the monitor." The experiment reruns Ctrl-Z-style control in a stronger setting, using [[Claude]] Opus 4.6 as the untrusted model and MiMo-V2-Flash as the trusted monitor in BashArena, with a live audit budget of 0.3% of honest-model steps.

| Protocol | Mechanism | Control read |
|----------|-----------|--------------|
| Retrying | Ask the model to retry after a suspicious action | Leaks information to the attacker; detailed monitor feedback can teach stealthier behavior |
| Resampling | Sample extra candidate actions and select or audit with a monitor | Safer cost curve because it does not give the attacker retry feedback |
| Trusted monitoring | Audit suspicious steps under a tight budget | In the stronger setting, naive highest-performing Ctrl-Z techniques underperformed trusted monitoring |

The market implication is straightforward: if AI R&D automation makes untrusted AI labor economically attractive, control protocols become part of the cost and throughput stack. Redwood reports that four resamples added 10.2 percentage points of safety, but about 60% of that safety gain could be recovered with only 10% of the extra sampling cost, or roughly 0.4 extra samples per step. The investable version is not "more monitoring always works"; it is that some controls leak adversarial information and some controls buy safety more cheaply.

*Source: [[Redwood Research]], ["Retrying vs Resampling in AI Control", May 29 2026](https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control). Source figures were extracted into text/tables; no source images were copied.*

---

## Implications

- [[AI compute demand curve]] - AI R&D automation is a demand-curve steepener because compute affects both product capacity and research velocity.
- [[Model lab economics]] - the economics shift from "can revenue cover burn?" toward "does compute spend buy faster algorithmic progress than peers?"
- [[Anthropic vs OpenAI compute race]] - deliverable compute becomes strategic lead time, not only customer-serving capacity.
- [[AI infrastructure financing risk]] - if labs chase compute because it controls research velocity, circular financing can intensify before ordinary revenue proof catches up.
- [[AI safety]] - compressed research cycles reduce the time available for evaluation, control, and governance responses.

---

## Related

- [[Ryan Greenblatt]] - May 2026 framework source
- [[Redwood Research]] - AI safety organization and source publication
- [[Software-only singularity]] - runaway version of the feedback loop
- [[AI compute demand curve]] - market-facing compute demand
- [[AI scaling laws]] - capability scaling context
- [[Model lab economics]] - lab revenue / burn / capital structure
- [[Anthropic vs OpenAI compute race]] - frontier-lab capacity competition
- [[AI safety]] - safety and governance context
- [[Prompt injection]] - rendered-output and instruction-channel threat model

## Cross-vault

- [Technologies: AI R&D Automation](obsidian://open?vault=technologies&file=AI%20R%26D%20Automation) - technical capability and safety architecture counterpart.

## Sources

- Ryan Greenblatt, ["Full automation of AI R&D probably yields a large speed up even without a software-only singularity"](https://blog.redwoodresearch.org/p/full-automation-of-ai-r-and-d-probably), Redwood Research Blog, May 27 2026.
- Redwood Research, ["Retrying vs Resampling in AI Control"](https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control), May 29 2026.
- [Forethought, "Will AI R&D Automation Cause a Software Intelligence Explosion?"](https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion), 2025.
- [Forethought, "Will Compute Bottlenecks Prevent a Software Intelligence Explosion?"](https://www.forethought.org/research/will-compute-bottlenecks-prevent-a-software-intelligence-explosion), 2025.
