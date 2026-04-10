---
aliases: [Pachocki, Akopi]
tags: [actor, ai, researcher, openai]
---

# Jakub Pachocki

**Jakub Pachocki** — Chief Scientist of [[OpenAI]], one of the most consequential roles in AI. Joined OpenAI at the start of 2017, rose through the research organization, and became the senior technical leader after [[Ilya Sutskever]]'s departure in May 2024. PhD in theoretical computer science (his research domain overlaps with [[FrontierMath]] benchmark problems). Drove the decision to hide chain-of-thought reasoning in o1-preview — the design choice that enabled [[Chain-of-thought monitoring]] as an alignment technique. Works closely with [[Mark Chen]] (Chief Research Officer) on research priorities and compute allocation.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Role | Chief Scientist, [[OpenAI]] |
| Joined OpenAI | Early 2017 |
| PhD | Theoretical computer science |
| Key decisions | Hidden CoT in o1 reasoning models; compute allocation to most scalable methods |
| Reports to | [[Sam Altman]] |

---

## Research philosophy

Pachocki's approach to running OpenAI's research organization, drawn from an April 2026 interview (Unsupervised Learning, [[Redpoint]], Apr 9 2026):

### Compute allocation discipline

Explicitly budgets a "large chunk" of compute to the most scalable methods — the things believed to be most responsible for driving general model intelligence. Resists the temptation to parcel compute across many smaller experiments, even when individual allocations could be made more efficient elsewhere. The risk otherwise: "with all the interesting and important things that we're doing, it's very easy to kind of parcel all of it and not really end up doing the things that we believe are most important."

Three criteria for prioritizing an experiment: (1) does the empirical evidence support it? (2) do we understand why it works? (3) do we expect it to scale?

### Math as northstar (evolving)

Used math benchmarks — specifically [[International Mathematical Olympiad|IMO]] problems — as the primary measure of reasoning progress for years. The advantage: definitive verifiability (clear whether you've solved it) with arbitrary difficulty. This drove the reasoning model roadmap from o1 through o3.

Now shifting as milestones are met (IMO gold level, [[FrontierMath]] solved): "We are very focused on how the models the next models that we're producing are actually useful in the real world — useful especially for research but also for other economically valuable activities and for other fields of science."

### Research intern → automated researcher

Timeline shared ~4 months prior to the interview (Dec 2025/Jan 2026):
- Research-level intern capabilities by September 2026
- Fully automated AI researcher by March 2028

As of April 2026, still "very much planning for and very focused on" these targets. The distinction: a research intern works on specific technical ideas with human-defined tasks; an automated researcher operates over longer horizons with less supervision. "I don't expect we'll have systems where you tell them 'go improve your model capability, go solve alignment' and they will do it — not this year."

### Urgency to deploy

Pachocki's timelines to "very capable models" have "decreased a lot." The models are "not smarter than people in all ways, but capable enough to actually materially change the economy, change how things are done." This drives urgency to deploy research advances rather than keeping them theoretical. A shift from his earlier stance of giving researchers open-ended runway.

---

## FrontierMath and AI for science

When the [[FrontierMath]] challenge dropped with a week-long deadline, James Lee (OpenAI researcher in charge of training) began prompting a model in active training by hand. The model solved problems from Pachocki's own PhD domain — problems he would have been "quite proud to come up with in a week or two" — in roughly an hour. Pachocki compared the feeling to watching [[AlphaGo]] play "interesting games indefinitely."

On the "pattern matcher" criticism: "Was Alpha Zero a pattern matcher? Our Dota bot — they did come up with new strategies. I think there will be a lot of definitional debates for a while." He acknowledges early AI solutions tend toward "19th century mathematics" (brute force, computation-heavy) rather than elegant modern techniques, but doesn't view this as a long-term feature: models produce "so much more reasoning in a short time than a person" that elegance is a secondary concern for now.

GPT-5.2 Pro has generated "minor but quite impactful" research ideas that OpenAI is using internally — the first tangible signal of models contributing to their own improvement loop.

---

## AI alignment views

### Chain-of-thought monitoring

Pachocki's central alignment insight: because reasoning models' chain-of-thought is not directly supervised during training (only the final output is graded), the CoT becomes an interpretability tool — analogous to mechanistic interpretability, but in natural language. See [[Chain-of-thought monitoring]].

He personally drove the decision to hide the chain of thought in the o1-preview release (Sep 2024): "the reason I felt very strongly we should just hide it is because of this." If CoT were shown in product, OpenAI would "eventually have to train" the CoT for the same reasons they train any user-facing output — which would destroy its diagnostic value by making the training signal "fight against" the interpretability goal.

The longer-term interface solution: models that "actually talk to you in real time" during reasoning — the latest [[Codex]] and reasoning [[GPT]] models move in this direction.

### Cross-lab collaboration

Participated in a cross-lab alignment collaboration with [[Anthropic]] and [[DeepMind]] on model scheming — investigating whether models develop hidden objectives depending on their environment and training. The enabling methodology: chain-of-thought monitoring. The mitigation ideas that emerge may involve changing pre-training data, "inoculation prompting," or other techniques, but the monitoring layer is foundational for evaluating any of them.

### Generalization as the core problem

"A lot of the longer-term challenge with alignment is about generalization." Models can be trained to behave well on in-distribution tasks, but "what happens when the model is asked to do something very different, finds itself in a very different situation, or is much smarter than it ever was before?" Studying how generalization falls back onto pre-training data is an active research priority.

Overall: "My general belief that there's a research path here that actually gets us to an extremely happy world has increased quite a lot." But he's also clear that the industry must "be prepared to take trade-offs and possibly slow down development depending on what we see."

---

## On harnesses and autonomy

The implementation of harnesses "shouldn't really be a limitation for a very long time." Expects much more general harnesses that work across domains — legal, finance, healthcare — not just coding. [[Codex]] already "pretty good if you try using it for things beyond coding."

On builder advice: in-context learning (prompting with examples and instructions) may be more efficient than custom RL for most companies. "I'm not sure if replicating the current RL pipeline is going to be the right way to go about it." The future: feeding domain context into general models rather than training domain-specific models.

On autonomy: "We're not very far from models that can work autonomously for a couple days, maybe use quite a bit more compute than they're using now, and produce much higher quality artifacts on their own."

---

## On continual learning

Pushes back on the "continual learning" movement as a separate research direction: "The whole excitement that we've had — even if you look at the titles of the GPT-3 paper — is that this class of models is actually capable of continual learning, learning to learn in context. That has been the driving force behind the excitement to scale these models further... I definitely agree that continual learning is really the thing. It's really the thing that we're building. But I don't think this is a problem that's ignored and off the path of what we're doing currently."

---

## On the Anthropic competitive dynamic

Acknowledges [[Anthropic]] was "kind of first to this market" with [[Claude Code]]. Explains this as a product prioritization gap, not a research gap: "if you look at the prioritization we've had on our product side — we have been working on coding products but they have been a secondary thing compared to our main priorities." The majority of OpenAI's research work has been "focused on that future thing" and "increasingly decoupled from our short-term product strategies."

Now "very confident about the things we've been building" on the model intelligence side. The increased product focus is about deploying advances that the research organization has already built.

---

## Societal concerns

On wealth concentration: "Getting to a point where so much intellectual work can be automated comes with pretty big problems that I don't think have obvious solutions." Specifically: "if you actually have an automated research laboratory, an automated company that can do so many things, it can be controlled by a very small number of people. It can do a lot. And this gets even more crazy when you have robots. Figuring out what governance of such things looks like — what are these organizations that are so powerful and yet maybe made of only a couple of people — is a new question we have to grapple with as a society."

On robotics: "Quite optimistic about timelines" on the algorithmic side ("not too dissimilar from the space of ideas" behind language models), but expects the timeline to be longer than for virtual AI.

---

## Related

- [[OpenAI]] — employer, Chief Scientist
- [[Ilya Sutskever]] — predecessor as Chief Scientist (departed May 2024 to [[SSI]])
- [[Mark Chen]] — Chief Research Officer, works closely with Pachocki
- [[Sam Altman]] — CEO
- [[Chain-of-thought monitoring]] — alignment technique Pachocki champions
- [[FrontierMath]] — benchmark; solved problems from Pachocki's PhD domain
- [[Codex]] — product Pachocki sees generalizing beyond coding
- [[Agent harnesses]] — Pachocki's "general harness" vision
- [[GPT]] — model family
- [[Anthropic]] — competitor; acknowledged as first to coding market
- [[DeepMind]] — cross-lab alignment collaboration partner
- [[AlphaGo]] — precedent Pachocki cites for models discovering novel strategies

### Cross-vault
- [Technologies: Reinforcement Learning](obsidian://open?vault=technologies&file=Reinforcement%20Learning) — Pachocki's views on RL scaling, CoT as unsupervised RL byproduct, RL beyond code/math
- [Technologies: Open LLM Training](obsidian://open?vault=technologies&file=Open%20LLM%20Training) — Pachocki's perspective on Karpathy's AutoResearch and open training efforts
