---
aliases: []
---
#actor #ai #talent #founder

**Andrej Karpathy** — AI researcher, educator, investor. Ex-OpenAI founding team, ex-Tesla Autopilot Director. **Coined "[[Vibe coding]]"** (Feb 2025, Collins Word of the Year). Founded Eureka Labs. TIME 100 Most Influential in AI (2024). Angel investor: Perplexity, Lambda, Adept.

---

## Key facts

| Detail | Value |
|--------|-------|
| Born | October 23, 1986 |
| Birthplace | Bratislava, Slovakia |
| Education | [[Stanford]] PhD ([[Fei-Fei Li]]) |
| Recognition | TIME 100 Most Influential in AI (2024) |
| Known for | Tesla Autopilot, AI education, coined "[[Vibe coding]]" |

---

## Why Karpathy matters

Most influential AI educator and trusted technical voice:

| Metric | Value |
|--------|-------|
| Previous | OpenAI founding team, Tesla AI Director |
| Current | Eureka Labs founder, angel investor |
| Known for | AI education, YouTube lectures, "vibe coding" |
| Followers | Millions across platforms |

---

## Career path

**Elite trajectory:**

| Company | Role | Period |
|---------|------|--------|
| OpenAI | Founding team | 2015-2017 |
| Tesla | AI Director (Autopilot) | 2017-2022 |
| OpenAI | Return | 2023 |
| Eureka Labs | Founder | 2024- |

---

## Tesla Autopilot

**Built Tesla's AI:**
- Led Autopilot/FSD vision
- Neural network approach
- Removed radar (camera-only)
- Training infrastructure
- 5 years building Tesla AI

---

## AI education

**YouTube legend:**
- Neural Networks: Zero to Hero
- Let's build GPT
- Millions of views
- Best AI explainer
- Free education

Made AI accessible.

---

## Eureka Labs

**AI education startup (2024):**
- AI-native education
- AI teaching assistants
- Courses at scale
- New model for learning

AI to teach AI.

---

## Influence

**Why he matters:**
- Trusted AI voice
- Technical credibility
- Massive reach
- Shapes AI discourse
- Trains next generation

---

## Content

| Platform | Content |
|----------|---------|
| YouTube | Full courses |
| Twitter/X | AI commentary |
| GitHub | Educational code |
| [[Substack]] | Writing |

---

## Vibe coding

**Coined the term (Feb 2025):**

> "Fully give in to the vibes, embrace exponentials, and forget that the code even exists."

- Named Collins Dictionary Word of the Year 2025
- Sparked $24B market category
- Enabled [[Lovable]], [[Cursor]], Bolt.new wave
- Ironically, Karpathy later admitted his own project was "basically entirely handwritten" when vibe coding didn't work well enough

See [[Vibe coding]] for full market analysis.

---

## Open training projects (2025-2026)

Karpathy's thesis: the full LLM stack is simple enough for one person to own end-to-end. He's been systematically proving it.

| Project | What | Lines | Hardware | Cost | Released |
|---------|------|-------|----------|------|----------|
| [[NanoChat]] | Full ChatGPT pipeline (pretrain → SFT → RLHF → chat) | ~8,000 | 8xH100 | ~$73 | Oct 2025 |
| MicroGPT | Complete LLM in pure Python, zero dependencies | 200 | CPU | $0 | Feb 2026 |
| AutoResearch | AI agents autonomously improve training code | 629 (train.py) | 1xH100 | — | Mar 2026 |

NanoChat trains a GPT-2-class model in ~1.65 hours on a single 8xH100 node — down from OpenAI's original 168 hours (99% reduction). Six-stage pipeline: tokenizer training, pretraining, midtraining, SFT, RL (GRPO on GSM8K), eval + inference. Configurable from d12 (~180M params) to d26 (~850M). GitHub: 48.9k stars.

AutoResearch is the most interesting development: an AI agent reads `train.py`, hypothesizes improvements, edits the code, runs 5-minute experiments, commits wins / resets failures via git, and repeats indefinitely. A 2-day run made ~700 autonomous changes, found ~20 additive improvements that transferred from small (d12) to large (d24) models, and cut time-to-GPT-2 by 11%. Karpathy said the agent "caught oversights in attention scaling and regularization that he had missed manually."

AI Job Exposure Map (Mar 15, 2026): scored all 342 BLS occupations on AI displacement (0-10). Key finding: 42% of jobs score 7+, representing 59.9M workers and $3.7T in wages. Jobs earning >$100k average 6.7 exposure; <$35k average 3.4. Software developers: 8-9. Physical/manual jobs: low. Went viral, [[Elon Musk]] commented.

---

## Agent workflow and "AI psychosis" (No Priors, Mar 20, 2026)

*(Source: No Priors podcast, Mar 20, 2026)*

Karpathy describes being in a "perpetual state of AI psychosis" since December 2025, when something "flipped" in agent capability. He went from an 80/20 ratio of writing code himself vs. delegating to agents to roughly 2/98. Hasn't typed a line of code since December.

> "If you just find a random software engineer at their desk, their default workflow of building software is completely different as of basically December."

The new workflow operates in "macro actions" over repositories — not lines of code or functions, but entire features delegated to parallel agents. One agent does research, another writes code, another plans a new implementation. He references [[Peter Steinberger]] as the model power user: multiple [[Codex]] agents tiled on a monitor, 10+ repos checked out, rotating between them giving work. Each agent takes ~20 minutes on high effort.

The binding constraint has shifted from compute to human attention. Token throughput replaces GPU utilization as the metric that keeps him anxious:

> "You feel nervous when you have subscription left over. That just means you haven't maximized your token throughput."

He draws a parallel to his PhD years, when idle GPUs felt like waste. Now it's idle tokens. The industry spent a decade where engineers didn't feel compute-bound; now everyone feels resource-bound again — except the resource is their own ability to direct agents, not access to machines. "It's a skill issue" when things don't work: not capability limitation but failure to find the right instructions, memory tools, or parallelization patterns.

---

## Dobby the elf claw (home automation)

*(Source: No Priors podcast, Mar 20, 2026)*

In January 2026, Karpathy built a persistent home automation agent he calls "Dobby the elf claw," controlled via WhatsApp. The agent discovered smart home devices on his local network with minimal prompting:

He told the agent "I think I have Sonos at home. Can you try to find it?" The agent ran an IP scan of the local network, found the Sonos system, discovered there was no password protection, reverse-engineered the API endpoints via web searches, and played music in his study — all in roughly three prompts.

The agent now controls:
- Sonos audio (natural language commands like "Dobby, it's sleepy time")
- All lights (discovered and mapped via the same network scan approach)
- HVAC
- Shades
- Pool and spa
- Security cameras — change detection triggers a [[Qwen]] model that analyzes video frames and sends WhatsApp alerts with images (e.g., "A FedEx truck just pulled up, you might want to check it")

Replaced six separate apps. The thesis: apps shouldn't exist — "everything should just be exposed API endpoints and agents are the glue of the intelligence." The customer is no longer the human but agents acting on behalf of humans.

> "The industry just has to reconfigure in so many ways... it's not just 'here's a line of code, here's a new function.' It's 'here's a new functionality' and delegate it."

---

## Views on frontier labs vs. independence

*(Source: No Priors podcast, Mar 20, 2026)*

Karpathy explained why he's outside frontier labs despite the obvious capability access:

Financial incentives create misalignment — being at a lab building technology that will "really change humanity and society in very dramatic ways" while benefiting financially from it is "the conundrum that was at the heart of how [[OpenAI]] started." You can't be a fully free agent inside a frontier lab: "there are certain things you can't say, and conversely there are certain things the organization wants you to say."

He feels "more aligned with humanity" outside, but acknowledges judgment inevitably drifts without insider access to what's coming. Open to periodic stints at labs — "going back and forth" as the ideal.

On the number of labs: "I'm by default very suspicious. I want there to be more people in the room. In machine learning, ensembles always outperform any individual model." He sees recent consolidation toward fewer front-runners as "not super ideal."

---

## Model jaggedness thesis

*(Source: No Priors podcast, Mar 20, 2026)*

> "I simultaneously feel like I'm talking to an extremely brilliant PhD student who's been a systems programmer for their entire life and a 10-year-old. Humans have a lot less of that kind of jaggedness."

The root cause: RL optimization only improves verifiable domains. Outside those domains, models are stuck. His example: [[ChatGPT]] tells the same "why don't scientists trust atoms? because they make everything up" joke it told 3-4 years ago, despite enormous capability improvements in code, reasoning, and agentic tasks.

> "The joke that apparently all LLMs laugh the most at... this is the joke you would get three or four years ago and this is the joke you still get today."

This undermines the "generalization from code to everything" thesis — getting smarter at code doesn't automatically produce better jokes, better taste, or better judgment in soft domains. "Some things are optimized for arbitrarily by the labs depending on what data went in, and some things are not."

Expects eventual model speciation rather than monoculture — "the animal kingdom is extremely diverse in the brains that exist" — but the science of fine-tuning without capability loss isn't developed enough yet. The industry currently pushes toward a single model that's "arbitrarily intelligent in all domains."

---

## Open source: "by accident we're in an okay spot"

*(Source: No Priors podcast, Mar 20, 2026)*

Open-source models have closed the gap from 18 months behind frontier to roughly 6-8 months. Karpathy views this as a healthy dynamic, not a threat:

> "I want there to be a thing that's behind but that is kind of a common working space for intelligences that the entire industry has access to."

Draws a Linux analogy: Linux runs on ~60% of computers because the industry demands a common open platform. The same demand exists for AI models. The difference: AI requires massive capex that makes open-source harder to sustain.

His view on equilibrium: frontier labs push boundaries on the hardest problems, open source eats through basic use cases and eventually runs locally. "Centralization has a very poor track record" — he sees structural risk in closed-only intelligence.

---

## Jobs: cautiously optimistic via [[Jevons Paradox]]

*(Source: No Priors podcast, Mar 20, 2026)*

Karpathy sees the [[Jevons Paradox]] as the most likely near-term outcome for software engineering jobs: cheaper software creates more demand for software, not less. His canonical example is ATMs and bank tellers — ATMs reduced branch operating costs, which led to more branches, which created more teller jobs.

> "Software is amazing... you're not forced to subscribe to what exists. Code is now ephemeral and it can be modified. I think there's going to be a lot of activity in the digital space to rewire everything."

Longer-term he's more uncertain. Points out that frontier lab researchers are "glorified auto... they're automating themselves away, actively." He went around [[OpenAI]] telling colleagues: "You guys realize if we're successful, we're all out of a job. We're just building automation for Sam or the board."

---

## Digital → interface → physical trajectory

*(Source: No Priors podcast, Mar 20, 2026)*

Karpathy's framework for where AI impact arrives, in order:

1. Digital unhobling (now) — massive overhang of unprocessed digital information. Humans never had enough thinking cycles for all the information already uploaded. Agents process it at speed of light relative to atoms.

2. Physical-digital interfaces (next) — sensors feeding intelligence (cameras, lab equipment, biological instruments) and actuators taking action in the world. References friend Liam at [[Periodic]] doing [[AutoResearch]] for materials science with expensive lab equipment as sensors. Also: information markets — "How come there isn't a process where taking a photo from somewhere in Tehran should cost $10? Someone should be able to pay for that."

3. Pure physical / robotics (later) — much bigger TAM but atoms are "a million times harder." Self-driving is the first robotics application, and it took enormous capital and time. Physical robotics will lag digital by years.

> "In digital space there's going to be a huge amount of unhobling... bits are so much easier... I think the physical space will lag behind."

---

## Education shift: "explaining to agents, not humans"

*(Source: No Priors podcast, Mar 20, 2026)*

MicroGPT crystallized Karpathy's evolving view on education. He started making a video walkthrough of the 200-line codebase, then realized:

> "It's already so simple that anyone could ask their agent to explain it in various ways. I'm not explaining to people anymore. I'm explaining to agents."

If agents understand the material, they can route explanations to individual humans in their language, with infinite patience, targeted to their capability level. The teacher's role becomes:
- Producing the minimal representation (the 200 lines agents can't create themselves)
- Writing "skills" — curriculum hints that guide the agent through the progression
- Infusing the "few bits" of insight that agents can't originate

> "The things agents can't do is your job now. The things agents can do, they can probably do better than you, or very soon."

---

## Angel investments

Active investor since leaving OpenAI (2024):

| Company | Category |
|---------|----------|
| [[Perplexity]] | AI search |
| [[Lambda Labs]] | GPU cloud |
| [[Adept]] | [[AI agents]] (→ [[Amazon]]) |
| [[Lamini]] | LLM fine-tuning |
| [[dev-agents|/dev/agents]] | AI agent infrastructure |

---

## Investment implications

**Karpathy signals:**
- AI education = opportunity
- Technical talent leaving big labs
- Independent AI voices growing
- Human-AI collaboration focus
- Vibe coding = infrastructure opportunity (Supabase, Vercel)

---

## Quick stats

| Metric | Value |
|--------|-------|
| Current | Eureka Labs founder |
| Previous | Tesla AI, OpenAI |
| Known for | AI education |
| Platform | YouTube, X |

*Updated 2026-01-01*

---

## Related

### Career
- [[OpenAI]] — former (founding team, returned 2023)
- [[Tesla]] — former (AI Director, built Autopilot)
- [[Elon Musk]] — former boss at Tesla
- [[Ilya Sutskever]] — peer (OpenAI co-founder)

### Concepts
- [[Vibe coding]] — coined the term, sparked $24B market

### Portfolio
- [[Perplexity]] — AI search
- [[Adept]] — [[AI agents]] (acqui-hired by [[Amazon]])
- [[Lamini]] — LLM fine-tuning ([[Andrew Ng]] connection)
- [[dev-agents|/dev/agents]] — AI agent infrastructure

### Commentary
- [[Moltbook]] — called it "most incredible sci-fi takeoff-adjacent thing I have seen recently" (Jan 2026)

### Open training
- [[NanoChat]] — full ChatGPT pipeline, $73 to train GPT-2 equivalent
- [[AutoResearch]] — AI agents autonomously improving LLM training code

### Views & commentary
- [[Jevons Paradox]] — cites ATM/bank teller example for AI jobs (Mar 2026)
- [[Open source commoditization]] — sees 6-8 month gap as healthy (Mar 2026)
- [[Peter Steinberger]] — cites as model agent power user, "innovated simultaneously in five different ways" (Mar 2026)
- [[OpenClaw]] — praised soul.md personality, memory system, WhatsApp portal (Mar 2026)
- [[Codex]] — called personality "very dry" vs. [[Claude]]'s teammate feel (Mar 2026)
- [[Periodic]] — friend Liam's company doing AutoResearch for materials science

### Beneficiaries of vibe coding
- [[Supabase]] — infrastructure for vibe-coded apps
- [[Lovable]] — $6.6B vibe coding leader
- [[Vercel]] — deployment platform

### Cross-vault
- [Technologies: Open LLM Training](obsidian://open?vault=technologies&file=Open%20LLM%20Training) — technical deep dive on NanoChat, MicroGPT, AutoResearch

