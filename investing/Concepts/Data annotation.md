#concept #ai #labor #infrastructure

**Data annotation** — The human labor layer of AI. Every frontier model needs millions of labeled examples. A hidden bottleneck and labor arbitrage opportunity.

---

## Why annotation matters

AI models learn from labeled data:

| Model type | Annotation need |
|------------|-----------------|
| LLMs | RLHF (human preferences), instruction tuning |
| Vision | Object detection, segmentation |
| Autonomous vehicles | Road scene labeling |
| Medical AI | Expert diagnosis labels |

**No labels = no model improvement.** Even "self-supervised" models need human feedback for alignment.

---

## The RLHF dependency

Reinforcement Learning from Human Feedback is how frontier models become useful:

| Step | Human role |
|------|------------|
| 1. Preference data | Humans rank model outputs |
| 2. Reward model | Learns from preferences |
| 3. Fine-tuning | Model optimizes for reward |

**Scale**: ChatGPT's RLHF required millions of human preference labels. Each frontier model iteration needs fresh data.

---

## Labor arbitrage geography

Annotation is labor-intensive. Companies exploit wage differentials:

| Location | Wage ($/hr) | Role |
|----------|-------------|------|
| US/EU | $15-25 | Quality review, specialized |
| Philippines | $2-5 | General labeling |
| Kenya | $1-3 | Scale AI's Remotasks |
| Venezuela | $1-2 | Crisis economy labor |
| India | $2-4 | Technical tasks |

**The arbitrage**: A $100B model trained on $2/hour labor.

---

## Key players

| Company | Model | Status |
|---------|-------|--------|
| [[Scale AI]] | Platform + managed workforce | Meta 49% owner, $29B |
| [[Appen]] | Crowd workforce | Public (APX), struggling |
| Labelbox | Enterprise SaaS | Private |
| Sama | Ethical sourcing (Africa) | Private |
| Surge AI | Quality-focused | Acquired by Scale |
| Snorkel AI | Programmatic (less human) | Private |

[[Scale AI]] dominates with ~40% market share.

---

## The bottleneck risk

As models scale, annotation demand grows:

| Challenge | Implication |
|-----------|-------------|
| Quality ceiling | Human annotators make mistakes |
| Specialized knowledge | Medical/legal needs experts |
| Language coverage | Non-English data scarce |
| Speed | Annotation lags model training |
| Cost | Human labor doesn't scale like compute |

**Potential chokepoint**: Annotation workforce may not scale fast enough for frontier model ambitions.

---

## Geographic concentration

| Region | Strength |
|--------|----------|
| [[Philippines Tech]] | English fluency, scale |
| Kenya | Scale AI's Remotasks hub |
| India | Technical annotation |
| Venezuela | Low cost, educated |
| Eastern Europe | Quality, languages |

Philippines is the annotation capital — English-speaking, time zone flexibility, large workforce.

---

## Disruption vectors

### Synthetic data
- AI generates training data for AI
- Reduces human labeling need
- Quality concerns remain

### Self-supervised learning
- Models learn from unlabeled data
- Works for pre-training
- Still needs RLHF for alignment

### Constitutional AI
- [[Anthropic]]'s approach
- AI critiques AI
- Reduces but doesn't eliminate human feedback

**Timeline**: 3-5 years before human annotation significantly reduced. Near-term, demand grows.

---

## Investment implications

**Bull (annotation demand):**
- Frontier model training accelerating
- RLHF essential for alignment
- Specialized domains (medical, legal) need experts
- [[Scale AI]] revenue trajectory ($870M → $2B)

**Bear (annotation disruption):**
- Synthetic data improving
- Labor costs rising in key geographies
- [[Appen]] struggling suggests commoditization
- AI-on-AI feedback reducing need

---

## Related

- [[Scale AI]] — Dominant player
- [[Appen]] — Public comp, struggling
- [[Philippines Tech]] — Labor geography
- [[Anthropic]] — Constitutional AI approach
- [[OpenAI]] — Major annotation customer
