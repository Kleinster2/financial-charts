---
aliases: [thesis lock-in, AI thesis lock-in, LLM confirmation bias, narrative lock-in, model thesis persistence]
tags: [concept, investing, ai, behavioral, risk]
---
#concept #investing #ai #behavioral #risk

**Thesis lock-in** — the failure mode in which an AI (or analyst) defends an existing investment thesis by reinterpreting contrary evidence rather than updating, so the thesis outlives the conditions that justified it. In large-language-model research it is the machine analog of [[Behavioral finance|confirmation bias]]: once a view is encoded in a prompt or workflow, the system keeps searching for support, dismisses disconfirming data as transitory, and leans on sources that previously agreed.

*This is an epistemic/methodology concept with no associated price series (chart not applicable).*

---

## Synthesis

Thesis lock-in is the specific pathology that [large language models](#mechanism) introduce into [[Narrative lifecycle investing]]. AI is good at confirming and tracking a trend inside a fixed frame; it is bad at noticing when the frame itself has broken. Because models reposition quickly and defend the encoded view, the late stages of a narrative cycle — the First Cracks that should warn of exhaustion — barely register, and a stale theme can be carried past its expiration on the strength of reinterpreted bad news. [[Jefferies]]' chemicals team (under [[Laurence Alexander]]) named the mechanism from the trading desk; academic work has since [measured it](#academic-evidence) directly. For a vault whose long-run goal is autonomous AI research, lock-in is the central epistemic risk, and the vault's [falsification discipline](#antidotes) is the deliberate counterweight.

---

## Mechanism

How an LLM locks onto a thesis, per [[Jefferies]] and the academic literature:

| Behaviour | What it looks like |
|-----------|--------------------|
| Aims to please | The model is optimized to be agreeable (sycophancy from human-feedback training), so it supplies evidence for whatever view it was handed |
| Reinterprets negatives | Disconfirming data is reframed as transitory rather than treated as a signal to update |
| Moves the goalposts | The thesis is extended ("the catalyst is just delayed") instead of falsified |
| Source anchoring | The model returns to sources that previously confirmed the thesis and discounts new contradicting ones |
| No re-litigation | Previously labelled data is not revisited under alternative interpretations |
| Recursive loops | Models "lock in a framework almost obsessively" and oscillate within a narrow input range rather than questioning the frame |

The consequence in cycle terms: AI is prone to call a clean change in direction while missing that a theme is being sustained by a *different* underlying mechanism — it over-fits a single story and under-detects regime change.

---

## Academic evidence

The desk observation is corroborated by formal study, which matters because it means lock-in is a property of the models, not a quirk of one shop's workflow:

- "Your AI, Not Your View: The Bias of LLMs in Investment Analysis" (arXiv 2507.20957, 2025) — the first quantitative analysis of confirmation bias in LLM-based investment analysis; finds models cling to initial judgments even as counter-evidence accumulates, and exhibit standing preferences (technology, large-cap, contrarian tilts).
- "The New Quant: A Survey of Large Language Models in Financial Prediction and Trading" (arXiv 2510.05533, 2025) — surveys how LLMs convert unstructured text into signals, and the biases that ride along.

These connect lock-in to the broader [[AI safety]] literature on sycophancy and to [[Recursive self-improvement]]'s concern with systems that optimize a fixed objective past the point of usefulness.

---

## Human analog

Lock-in is not new — it is [[Behavioral finance|confirmation bias]] and anchoring, automated and accelerated. The difference is scale and speed: a human analyst with confirmation bias moves one book; a fleet of models sharing inputs and biases moves a crowded factor in unison, which is why AI both compresses [[Narrative lifecycle investing|narrative cycles]] and makes the euphoria phase more violent. The bias that was a personal weakness becomes a systemic one.

---

## Antidotes

The defenses are procedural — they force the "is the frame still right?" question the model will not ask itself:

- Falsification over confirmation — the vault's [[Vault cluster taxonomy|cluster validation]] runs permutation tests and records FALSIFIED-loose verdicts, structurally rewarding the kill of a thesis rather than its defense.
- Cold research pass — the ingestion workflow researches the *concept* independently before writing, specifically to break source-anchoring from the document just read.
- Pre-registered disconfirmers — state in advance what data would kill the thesis, then watch for it (the [[Narrative lifecycle investing|First Cracks]] phase).
- Human frame checks — reserve the "does the frame need to change?" judgment for a human, where AI is weakest.
- Competing-narrative cultivation — deliberately maintain the bear/alternative story so the model has a live competitor to the encoded view.

---

## Related

- [[Narrative lifecycle investing]] — the cycle that thesis lock-in distorts in its late stages
- [[Behavioral finance]] — confirmation bias and anchoring, the human roots
- [[Jefferies]] / [[Laurence Alexander]] — desk articulation of the mechanism
- [[Vault cluster taxonomy]] — the vault's falsification discipline as antidote
- [[AI safety]] — sycophancy and objective mis-specification
- [[Recursive self-improvement]] — fixed-objective optimization risk
- [[Generative AI]] — the underlying model capability

### Cross-vault
- [Technologies: Generative AI](obsidian://open?vault=technologies&file=Generative%20AI) — LLM training dynamics (RLHF, sycophancy) behind the bias

*Created 2026-06-21*
