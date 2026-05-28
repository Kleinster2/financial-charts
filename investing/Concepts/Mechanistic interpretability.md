---
aliases: [mech interp, mechanistic model interpretability, neural network interpretability]
tags: [concept, ai, safety, interpretability]
---

# Mechanistic interpretability

Mechanistic interpretability is the research program that tries to reverse-engineer neural networks into human-understandable mechanisms. In the investing vault it matters because [[Anthropic]] uses the field as one of its main claims that [[Claude]] can become safer and more trusted than rival frontier models: not merely better-behaved at the output layer, but internally observable, auditable, and eventually steerable.

---

## Synthesis

The field sits between neuroscience and software debugging. A conventional software system can be inspected because humans wrote the source code. A frontier model is trained, not directly programmed; its "source code" is a matrix of weights and activations that can perform sophisticated behavior without an obvious human-readable explanation. Mechanistic interpretability asks whether those internal states can be decomposed into features, circuits, and causal pathways that humans can inspect.

The research arc begins with vision models, where [[Chris Olah]] and collaborators showed that feature visualization could generate inputs that activate particular neurons or channels. That made internal representations visible enough to study. The Circuits thread then pushed the stronger claim: if researchers examine the connections between features across layers, they can find small algorithms inside the network. The analogy is biological circuits: not a complete theory of the brain, but a tractable study of parts.

[[Transformer]] language models made the problem harder. Single neurons are often polysemantic: one unit can respond to unrelated contexts because the model stores more sparse features than it has neurons. The superposition result reframed the unit of analysis. If features live in overlapping directions rather than isolated neurons, the right tool is not neuron naming but feature extraction. Sparse autoencoders and dictionary learning are the current workhorse: train a secondary model to reconstruct activations through a sparse bottleneck, then inspect the sparse features.

Anthropic's 2024 Scaling Monosemanticity result was the proof-of-scale moment. The team extracted millions of interpretable features from [[Claude]] 3 Sonnet and showed that some features were safety-relevant: scam-email recognition, sycophancy, secrecy, code backdoors, biological-weapons content, manipulation, and power-seeking. More importantly, feature interventions changed behavior. That makes the work operationally interesting: if features are causal handles, they may become tools for audits, steering, or model repair.

The open problem is conversion. Feature maps do not automatically tell researchers which circuits produce a behavior, whether every dangerous latent feature has been found, or how to certify safety at frontier scale. Anthropic itself says a full feature set would be prohibitively expensive under current methods, and understanding representations is not the same as understanding how the model uses them. The 2026 Natural Language Autoencoders work tries to make activations more directly readable, but it introduces its own reliability and cost constraints.

The investment implication is that mechanistic interpretability is both a safety technology and a trust product. If it works, it can support enterprise, government, and regulatory adoption by turning model safety into something closer to audit evidence. If it fails to scale, model labs remain dependent on output testing, red-teaming, and policy promises -- weaker tools exactly when model capability and autonomy are rising.

---

## Timeline

| Date | Milestone | Why it mattered |
|------|-----------|-----------------|
| 2017 | Distill feature visualization work by [[Chris Olah]], Alexander Mordvintsev, and Ludwig Schubert | Made neural-network features visually inspectable in image models |
| 2020 | OpenAI Circuits thread | Framed interpretability as finding meaningful algorithms in model weights |
| 2022 | Toy Models of Superposition | Explained why individual neurons can be polysemantic and why features can be stored in overlapping directions |
| 2023 | Towards Monosemanticity / dictionary learning | Showed small language-model layers could be decomposed into more interpretable sparse features |
| 2024 | Scaling Monosemanticity on [[Claude]] 3 Sonnet | Extracted millions of features from a production-grade LLM and demonstrated causal steering |
| 2026 | Natural Language Autoencoders | Translated activations into natural-language explanations for selective model audits |

---

## What to watch

- Feature coverage -- whether methods can capture a broad enough share of safety-relevant model concepts without compute costs exceeding model training.
- Circuit understanding -- whether researchers can move from "feature exists" to "this pathway caused the behavior."
- Reliability of explanations -- whether NLA-style text explanations can be independently corroborated rather than becoming another hallucination surface.
- Auditability -- whether regulators, customers, or independent researchers can use interpretability artifacts without relying entirely on the model lab's own claims.
- Model-edit loop -- whether discovered features lead to concrete model interventions, not only papers and demos.

---

## Related

- [[Chris Olah]] -- field pioneer and Anthropic interpretability lead
- [[Anthropic]] -- frontier lab making interpretability a safety differentiator
- [[Claude]] -- model family used in Anthropic's scaled interpretability work
- [[AI safety]] -- broader safety field this supports
- [[Chain-of-thought monitoring]] -- adjacent observability method in natural language rather than activations
- [[Artificial intelligence]] -- parent technology theme
- [[OpenAI]] -- former home of the Circuits work
- [[Google Brain]] -- former home of early feature-visualization work

### Cross-vault

- [Technologies: Mechanistic Interpretability](obsidian://open?vault=technologies&file=Mechanistic%20Interpretability) -- technical counterpart

---

## Sources

- [Distill - Feature Visualization](https://distill.pub/2017/feature-visualization/)
- [Distill - Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)
- [Transformer Circuits - Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/)
- [Anthropic - Decomposing Language Models Into Understandable Components](https://www.anthropic.com/research/decomposing-language-models-into-understandable-components)
- [Anthropic - Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Anthropic - Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)
