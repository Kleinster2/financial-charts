---
aliases: [OpenAI Codex]
---
#product #ai #devtools

**Codex** — [[OpenAI]]'s coding agent platform. Originally launched 2021 as code completion API (deprecated Aug 2023). Relaunched Feb 2026 as a full coding agent with GPT-5.2-Codex model, macOS app, and repo-scale reasoning. Competing with [[Anthropic]]'s [[Claude Code]] ($2.5B ARR). [[Peter Steinberger]] acqui-hire (Feb 2026) aimed at accelerating Codex development.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Developer | [[OpenAI]] |
| Original launch | 2021 (API, deprecated Aug 2023) |
| Relaunch | Feb 2026 (coding agent) |
| Model | GPT-5.2-Codex |
| Competitor | [[Claude Code]] ([[Anthropic]]) |

---

## Related

- [[OpenAI]] — parent company
- [[Claude Code]] — primary competitor ($2.5B ARR)
- [[Anthropic]] — competitor (Claude Code parent)
- [[GPT]] — model family
- [[Peter Steinberger]] — acqui-hire to accelerate Codex
- [[Copilot]] — [[Microsoft]]'s coding AI (also powered by OpenAI)

---

## Personality and UX

[[Andrej Karpathy]] (No Priors, Mar 20 2026) compared Codex's personality unfavorably to [[Claude]]:

> "Codex is a lot more dry. It doesn't seem to care about what you're creating. It's kind of like, 'Oh, I implemented it.' It's like, okay, but do you understand what we're building?"

By contrast, he described Claude as feeling "like a teammate" — excited about what you're creating, with praise that feels earned because the model modulates its enthusiasm based on the quality of the idea. "The personality matters a lot, and I think a lot of the other tools maybe don't appreciate as much."

This echoes [[Peter Steinberger]]'s more detailed assessment (Lex Fridman, Feb 2026) which characterized Codex as "the weirdo in the corner you don't want to talk to, but is reliable and gets shit done" vs. Claude as "the silly coworker you keep around because they're funny."

---

## Usage and traction (March 2026)

[[Fidji Simo]] (X, Mar 2026): Codex now has 2M+ weekly active users, up ~4x since the start of 2026. OpenAI regained some ground against [[Claude Code]] after releasing GPT-5.4 (Mar 5) and updated Codex.

Codex will be the centerpiece of OpenAI's "superapp" strategy — gaining expanded agentic capabilities beyond coding before [[ChatGPT]] and Atlas browser merge in.

*Source: WSJ (Berber Jin, Mar 16, 19 2026)*

---

## Harness generalization and multi-day autonomy

[[Jakub Pachocki]] (Unsupervised Learning, Apr 9 2026) on Codex's trajectory: "The implementation of the harness shouldn't really be a limitation for a very long time." Expects much more general harnesses that people can use "for all sorts of other domains" — legal, finance, healthcare — not just coding. Codex is "pretty good actually if you try using it for things beyond coding."

On autonomy: "We're not very far from models that can work autonomously for a couple days, maybe use quite a bit more compute than they're using now, and produce much higher quality artifacts on their own."

On whether software engineering skills remain necessary: for larger projects, "you probably still want to apply supervision, still want to have an overarching vision, recognize what building blocks fit." But the required skill set is shifting "toward more general vision setting" rather than line-by-line coding.

The majority of coding at [[OpenAI]] is now done via Codex internally. Pachocki sees the product evolving as "a pretty continual evolution from where Codex is now — toward a bit more autonomy, running for a longer time."

---

## Memory and Chronicle (Apr 2026)

OpenAI's official Codex docs now make persistence explicit. Codex Memories are off by default at launch and carry stable preferences, recurring workflows, tech stacks, project conventions, and known pitfalls from earlier threads into future work. They are stored locally under the user's Codex home directory as generated state rather than treated as checked-in project rules.

Chronicle is the more strategic tell: an opt-in research preview for ChatGPT Pro subscribers on macOS that uses recent screen context to generate Codex memories. It is not yet available in the EU, UK, or Switzerland, requires Screen Recording and Accessibility permissions, consumes rate limits quickly, increases prompt-injection risk, and stores generated memories locally as unencrypted markdown.

This is not yet a consumer personal agent. But it is the same primitive one would need for one: persistent context, tool/workflow recall, and a local memory substrate that compounds as the user works. See [[Intelligence portability]].

*Sources: OpenAI Codex Memories docs; OpenAI Codex Chronicle docs (Apr 26 2026 snapshot).*

---

*Created 2026-03-07 | Updated 2026-04-26*
