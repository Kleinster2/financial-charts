#index #MOC

Research on the competitive dynamics of AI — oriented toward finding mispricings.

---

## Core question

Where is consensus wrong about AI?

---

## Supply side (→ [[Foundry Wars]])

Chips, memory, packaging, equipment. Covered in [[Foundry Wars]]. Key crossover:
- [[NVIDIA]] — supply constrained, CUDA moat
- [[Long memory]] — HBM demand from AI
- [[Advanced packaging]] — CoWoS bottleneck
- [[Power constraints]] — 44GW US shortfall

---

## Demand side (this index)

Who's buying compute, why, and what are they building?

### Hyperscalers (Tier 1)
- [[Microsoft]] — OpenAI partner, largest AI capex
- [[Google]] — Gemini, TPUs, vertical integration
- [[Amazon]] — Bedrock, Trainium, inference play
- [[Meta]] — Llama open-source, NVIDIA-heavy

### Model labs
- [[OpenAI]] — frontier leader, Microsoft-funded
- [[Anthropic]] — TPU route, safety-focused
- [[xAI]] — Musk, potential Samsung anchor
- Mistral — European, open-weight
- DeepSeek — China, efficiency focus

### Inference layer
- Groq — acquired by [[NVIDIA]] ($20B)
- Cerebras — wafer-scale, inference pivot
- Together AI, Fireworks — API providers

---

## Key concepts

**What's working**
- [[Agentic AI]] — 35% adoption, 66% seeing value, $7.9B market, 171% projected ROI
- Coding tools — 55% of enterprise AI spend, clear ROI (Claude Code, Copilot, Cursor)

**Economics (nuanced)**
- [[Model lab economics]] — OpenAI aggressive ($74B burn), Anthropic plausible (2028 break-even)
- [[Inference economics]] — 10-30x price collapse, commoditizing
- [[Open source commoditization]] — 0.3pt gap to frontier, DeepSeek destroying prices
- [[Enterprise AI adoption]] — 95% pilots fail *excluding* coding/agents

**Scaling & compute**
- Scaling laws — does more compute = better models?
- Training vs inference split — where does $ go?
- Hyperscaler capex — $600B in 2026, 94% of cash flows

**Moats**
- [[CUDA moat]] — software lock-in (also in Foundry Wars)
- Data moats — proprietary training data
- Distribution moats — who owns the user?
- Talent concentration — SF vs world

**Bottlenecks**
- [[Power constraints]] — hard limit on deployment
- GPU allocation — who gets NVIDIA capacity?
- Memory bandwidth — HBM scarcity

**Portfolios**
- [[AI trade portfolio]] — consensus AI longs (used as hedge)

---

## Open questions

- Is frontier AI a sustainable business?
- Does open-source commoditize model providers?
- Will inference be a race to zero margin?
- Can hyperscalers disintermediate model labs?
- China AI trajectory despite export controls?
- When does enterprise AI adoption inflect?

---

## Trade ideas (developing)

| Idea | Logic | Evidence | Status |
|------|-------|----------|--------|
| **Bullish agents/coding** | 35% adoption, 66% seeing value, 55% of spend | [[Agentic AI]], [[Enterprise AI adoption]] | **Strong signal** |
| **[[Long Anthropic]]** | Agentic code orchestrator moat, enterprise trust, IPO prep | Claude Code $1B, $350B valuation, 1M TPUs | **Strengthening** |
| **[[Long Broadcom]]** | ASIC explosion, hyperscaler custom silicon | $14.5B → $100B F27E, OpenAI $10B deal | **New thesis** |
| **Bearish OpenAI** | $74B losses, consumer-heavy, 2030 break-even | [[Model lab economics]] | Moderate signal |
| **Long hyperscalers** | Own distribution, can subsidize, patient capital | Microsoft/Google can wait | Moderate signal |
| **Bearish generic enterprise AI** | 95% no ROI (excluding coding/agents) | [[Enterprise AI adoption]] | Moderate signal |
| **Bearish inference margins** | 10-30x price collapse, commoditizing | [[Inference economics]], [[Open source commoditization]] | Strong signal |
| **Bullish agent infrastructure** | Agents consume lots of inference, need orchestration | [[Agentic AI]] | Exploring |
| Long power/utilities | AI = electricity demand, 44GW shortfall | [[Power constraints]] | Exploring |
| Long NVIDIA (momentum) | $275B backlog, Groq acquisition, ByteDance $14B | Existing — see [[NVIDIA]] | |

**Refined thesis**: AI is bifurcating. **Coding + agents = working** (bullish). Generic enterprise AI = struggling (bearish). Model labs diverge — Anthropic winning with agents, OpenAI burning cash. **Infrastructure wins regardless — memory, power, custom silicon.**

---

## What to track

- [x] Hyperscaler AI capex guidance — $600B 2026, 94% of cash flows (Dec 2025)
- [x] Inference pricing trends — 10-30x collapse, DeepSeek at $0.27 (Dec 2025)
- [x] Open-source model quality vs frontier gap — 0.3pt on MMLU (Dec 2025)
- [x] Enterprise AI adoption data — 95% no ROI, $37B spend (Dec 2025)
- [ ] **CES 2026 (Jan 6-9)** — Jensen keynote, Lisa Su keynote, Panther Lake, Rubin roadmap
- [ ] **Anthropic IPO timing** — Wilson Sonsini engaged, 2026 possible
- [ ] Model lab earnings/burn rate updates (quarterly)
- [ ] Hyperscaler AI revenue disclosure (watch for margin data)
- [ ] Open source benchmark updates (track DeepSeek, Llama, Mistral)
- [ ] Enterprise churn data (renewals, not just new sales)

---

## Relationship to [[Foundry Wars]]

```
AI Race (demand)          Foundry Wars (supply)
      │                          │
      │    ┌─────────────────┐   │
      └───→│ Chip demand     │←──┘
           │ Memory demand   │
           │ Power demand    │
           └─────────────────┘
```

The two indices share nodes but ask different questions:
- Foundry Wars: Who makes the chips?
- AI Race: Who needs them and why?

---

*Last updated: 2025-12-30 — initial research complete*
