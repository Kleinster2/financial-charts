---
aliases: [Fable 5, Claude Fable, claude-fable-5]
tags: [product, ai]
parent_actor: "Anthropic"
parent_concept: "Frontier models"
---

# Claude Fable 5

[[Anthropic]]'s first publicly available Mythos-class [[Claude]] model, released June 9, 2026. Fable 5 is the general-availability, safety-gated half of a paired launch: Fable 5 (`claude-fable-5`, GA) and [[Claude Mythos|Claude Mythos 5]] (`claude-mythos-5`, restricted to [[Project Glasswing]]) share the same underlying model, specs, and pricing — the only difference is that Fable 5 ships with safety classifiers that can decline requests and fall back to [[Claude Opus|Opus 4.8]], while Mythos 5 has those classifiers lifted. Anthropic calls it its most capable widely released model, built for the most demanding reasoning and long-horizon agentic work.

The naming encodes the distinction: Fable from the Latin *fabula* ("that which is told"), Mythos from the Greek *mythos* — same story, the safeguards are what separate the two.

---

## Suspended — June 12, 2026 (US export-control ban)

On June 12, 2026, [[Anthropic]] disabled Fable 5 for every customer to comply with a [[Commerce Department]] export-control directive — a letter from Secretary [[Howard Lutnick]] to [[Dario Amodei]] placing Fable 5 and [[Claude Mythos|Mythos 5]] off-limits to foreign nationals inside and outside the US. Because the restriction reaches foreign customers and some of Anthropic's own foreign-born employees, Anthropic took both models fully offline rather than partially comply: "we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance." All other [[Claude]] models remain available, and Anthropic says it will restore access "as soon as possible."

The trigger was a jailbreak of Fable 5's safety classifiers (the cyber / bio-chem / distillation layer described below) demonstrated by [[Amazon]] researchers. Anthropic says the technique surfaced only "previously known, minor vulnerabilities" with "no Mythos-specific uplift," discoverable by other public models without a bypass. Full event detail, quotes, and market read in [[Anthropic#Jun 12 — Commerce export ban; Fable 5 / Mythos 5 taken offline|Anthropic]].

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Tier | Capybara (above [[Claude Opus]]); Mythos-class |
| Released | June 9, 2026 |
| Status | Suspended for all customers June 12, 2026 (US export-control directive) |
| API model ID | `claude-fable-5` |
| Restricted sibling | [[Claude Mythos]] 5 (`claude-mythos-5`, [[Project Glasswing]] only) |
| Context window | 1M tokens (default) |
| Max output | 128K tokens / request |
| Pricing | $10 / M input, $50 / M output |
| Thinking | Adaptive thinking only; raw chain-of-thought never returned |
| Data retention | 30-day (Covered Model; no zero-retention option) |
| Public bridge before launch | [[Claude Opus]] 4.8 (May 28 2026) |

---

## Same model, two products

Fable 5 and [[Claude Mythos|Mythos 5]] are the same underlying weights with identical 1M-token context, 128K max output, and $10/$50 pricing. What distinguishes them is a layer of safety classifiers present in Fable 5 and absent in Mythos 5. This is the mechanism that let [[Anthropic]] put Mythos-class capability into general release: it preserves the commercial model while routing the small share of high-risk traffic to a weaker, already-public model.

[[Claude Mythos|Mythos]] was unveiled in April 2026 and held inside [[Project Glasswing]], a restricted defensive-cyber program, because of its vulnerability-discovery capability. At the [[Claude Opus|Opus 4.8]] launch on May 28, Anthropic said Mythos-class models would reach all customers "in the coming weeks" once stronger cyber safeguards were in place. Fable 5 is that release. At $10/$50 it is priced at "less than half the price of Claude Mythos Preview," implying the restricted Preview tier ran above $20/$100.

[[Claude Mythos|Mythos 5]] is the successor to Mythos Preview and remains [[Project Glasswing]]-only; customers without Glasswing access use Fable 5, which Anthropic says offers the same capabilities.

---

## Safety architecture

The classifiers are the defining feature of the product, not a footnote. Three domains trigger a refusal and a fallback to [[Claude Opus|Opus 4.8]]:

| Domain | What it catches |
|--------|-----------------|
| Cybersecurity | Offensive tasks, exploitation, agentic hacking |
| Biology / chemistry | Gene therapy, viral design, bioweapons-adjacent queries |
| Distillation | Attempts to extract capabilities for unauthorized model training |

Mechanics that matter for anyone building on the model:

- A declined request returns `stop_reason: "refusal"` as a successful HTTP 200, not an error, and names which classifier declined it.
- Fallback to another Claude model can be server-side (the `fallbacks` parameter), client-side (SDK middleware), or manual. Fallback credit refunds the prompt-cache cost of switching, and a request refused before any output is generated is not billed.
- Refusal-and-fallback fires in fewer than 5% of sessions — roughly 95% run entirely on Fable 5.
- An external bug bounty produced no universal jailbreaks in over 1,000 hours of testing; one external partner rated Fable 5's cyber safeguards the most robust it had tested.
- Both Fable 5 and Mythos 5 carry mandatory 30-day data retention — applied even to customers with prior zero-data-retention agreements — used only to run safety classifiers, then deleted. Both are designated Covered Models with no zero-retention option.

---

## Capabilities and benchmarks

Anthropic positions Fable 5 as state of the art at coding, knowledge work, vision, and computer use, and emphasizes sustained autonomy — executing coding and knowledge work for extended periods without intervention.

| Benchmark / test | Result |
|------------------|--------|
| FrontierCode ([[Cognition]]) | Highest among frontier models, at medium effort |
| Finance benchmark ([[Hebbia]]) | Highest of any model; senior-level reasoning |
| Core analytics benchmark | First to break 90% (a ~10-point jump over [[Claude Opus]]) |
| Slay the Spire (memory test) | 3x improvement over Opus 4.8 with file-based memory |
| Pokémon FireRed | Completed the game vision-only, no helper harness |
| AAV gene-therapy design | Outperformed protein language models on Dyno Therapeutics candidates |

Customer proof points at launch: [[Cursor]] (CEO Michael Truell) called it "state of the art" on CursorBench; [[GitHub]] (CPO Mario Rodriguez) reported it "exceeded previous benchmarks" on long-horizon coding; [[Stripe]] said it compressed months of engineering into days, running a 50-million-line Ruby migration in a day against an estimated two months by hand.

---

## Availability and pricing

- Fable 5 is generally available on the [[Claude]] API, [[Claude Code]], Amazon Bedrock and Claude Platform on [[Amazon]] AWS, [[Vertex|Vertex AI]] ([[Google]]), and [[Microsoft]] Foundry. GitHub Copilot added it the same day.
- [[Claude Mythos|Mythos 5]] is limited to [[Project Glasswing]] approved customers.
- On subscription plans (Pro, Max, Team, seat-based Enterprise), Fable 5 was included at no extra cost June 9–22; from June 23 it requires usage credits, pending capacity restoration — a rationing signal on a capacity-constrained model.
- At $10 input / $50 output per million tokens, Fable 5 is priced at exactly [[Claude Opus|Opus 4.8]]'s fast-mode rate and at double Opus 4.8's standard $5/$25 — a premium tier landing into enterprises already managing large AI budgets.

Technical notes for builders: adaptive thinking is the only thinking mode (the `effort` parameter controls depth; thinking cannot be disabled), and raw chain-of-thought is never returned (only a summary or an empty block). Supported at launch: effort, task budgets (beta), the memory tool, code execution, programmatic tool calling, context editing (beta), compaction, and vision. Migration guides cover Opus 4.8 → Fable 5 and Mythos Preview → Mythos 5.

---

## Market and strategic read

Fable 5 converts the [[Claude Mythos|Mythos]] story from a restricted-capability event into a commercial tier. The investable signal the Mythos note flagged — AI vulnerability discovery becoming cheap enough that human disclosure and patching capacity becomes the scarce resource — now reaches every API customer, but in a deliberately safety-shaped form. The classifier-plus-fallback design is the product innovation that made that possible: Anthropic monetizes the frontier capability broadly while diverting the dangerous slice to an older model.

The timing carries a visible tension. Fable 5 shipped June 9, days after Anthropic publicly urged frontier labs to adopt a "coordinated brake pedal" on AI development and warned about [[Recursive self-improvement]] (its June 4 "When AI builds itself" essay). Releasing its most powerful public model in the same week it called for slowing the frontier is the central read on Anthropic's posture: capability deployment and safety advocacy run in parallel, with the safeguards offered as the reconciling mechanism. This is the commercial face of the same capability that pulled [[Claude Mythos|Mythos]] into the financial-stability perimeter in April, when [[Scott Bessent]] and [[Jerome Powell]] convened major bank CEOs over its cyber risk.

The release lands into a crowded competitive and capital-markets window: [[OpenAI]] is readying [[OpenAI Spud|Spud]], and the [[Anthropic IPO 2026|Anthropic]]/[[OpenAI]]/[[SpaceX]] IPO cohort is converging on late 2026. A premium-priced, capacity-rationed flagship with a June 23 credit cliff is consistent with a model where compute, not demand, is the binding constraint.

---

## Related

- [[Anthropic]] — parent company; the June 9 release is the realization of the Mythos commercial path
- [[Claude]] — product family
- [[Claude Mythos]] — same underlying model; the restricted (Glasswing) sibling and the cyber / financial-stability story
- [[Claude Opus]] — the fallback model for refused requests (Opus 4.8) and the prior public flagship
- [[Project Glasswing]] — restricted program that still gates Mythos 5
- [[Recursive self-improvement]] — the frontier-risk warning Anthropic issued days before the release
- [[AI safety]] — classifier-and-fallback as a deployment-safety mechanism
- [[Cursor]], [[GitHub]], [[Stripe]] — launch customer proof points
- [[Cognition]], [[Hebbia]] — benchmark sources
- [[OpenAI Spud]] — competing next-gen model
- [[Anthropic IPO 2026]] — capital-markets backdrop

### Cross-vault
- [Technologies: Claude Mythos](obsidian://open?vault=technologies&file=Claude%20Mythos) — model-tier taxonomy and technical architecture
- [Technologies: Recursive self-improvement](obsidian://open?vault=technologies&file=Recursive%20self-improvement) — the "When AI builds itself" frontier-risk frame

## Sources

- [Anthropic, "Claude Fable 5 and Claude Mythos 5"](https://www.anthropic.com/news/claude-fable-5-mythos-5), June 9, 2026
- [Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5" (API docs)](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), June 9, 2026
- [TechCrunch, "Anthropic's Claude Fable 5 is a version of Mythos the public can access today"](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/), June 9, 2026
