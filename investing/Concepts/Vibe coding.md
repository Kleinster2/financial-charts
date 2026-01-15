# Vibe coding

#concept #ai #developer-tools #trend

**Vibe coding** — AI-assisted programming where users describe what they want in natural language and AI generates the code. Term coined by **Andrej Karpathy** (Feb 2025). Collins Dictionary Word of the Year 2025. **$4.7B market → $24B by 2031.** 41% of global code now AI-generated. Driving [[Supabase]], [[Vercel]] growth.

---

## Definition

> "Fully give in to the vibes, embrace exponentials, and forget that the code even exists."
> — [[Andrej Karpathy]], Feb 2025

**Key distinction from traditional AI coding:**
- User doesn't review or edit code
- Focus on iterative experimentation, not correctness
- Evaluate by results, not code quality

---

## Market size

| Metric | Value |
|--------|-------|
| 2024 market | $4.7B |
| 2027 projected | $12.3B |
| 2031 projected | **$24.5B** |
| CAGR | 24.3% |
| AI coding assistants (2030) | $100B |

Combined valuation of leading startups grew **350% YoY** (2024-2025): ~$8B → $36B+.

---

## Adoption statistics

| Metric | Value |
|--------|-------|
| US developers using AI tools daily | 92% |
| Global developers using weekly | 82% |
| Global code that is AI-generated | **41%** |
| Lines of AI code written (2024) | 256 billion |
| YC W25 batch with 95% AI code | 25% |

---

## Key players

### Pure-play vibe coding

| Company | Valuation | ARR | Notes |
|---------|-----------|-----|-------|
| **[[Lovable]]** | $6.6B | $200M+ | Fastest to $100M ARR ever |
| **Cursor** (Anysphere) | $29B | — | AI code editor, dev-focused |
| **Bolt.new** | — | — | AI app builder |
| **Replit** | $1B+ | — | AI coding environment |
| **v0** ([[Vercel]]) | Part of Vercel | — | AI web components |

### Infrastructure beneficiaries

| Company | How they benefit |
|---------|------------------|
| **[[Supabase]]** | Default backend for vibe-coded apps |
| **[[Vercel]]** | Default frontend deployment |
| **[[Neon]]** | Auto-provisioned databases |

### Cautionary tale

| Company | What happened |
|---------|---------------|
| **[[Builder.ai]]** | Claimed AI, used 700 humans, collapsed |

---

## The stack

Typical vibe-coded app auto-provisions:

```
User prompt
    ↓
Vibe coding tool (Lovable, Bolt, v0)
    ↓
Frontend → Vercel
Backend → Supabase
Database → Supabase/Neon
Auth → Supabase
```

**Investment implication:** Vibe coding growth flows to infrastructure providers.

---

## Why it matters now

### Enablers

| Factor | Impact |
|--------|--------|
| GPT-4/Claude quality | Code good enough to ship |
| Context windows | Can handle full apps |
| Supabase/Vercel integrations | Zero-config deployment |
| Open source models | Cost coming down |

### Demand drivers

| Driver | Impact |
|--------|--------|
| Developer shortage | 4M unfilled dev jobs globally |
| Speed expectations | Ship in hours, not weeks |
| Non-technical founders | Can now build MVPs |
| Prototyping | Validate ideas instantly |

---

## Concerns

### Technical debt

| Risk | Data |
|------|------|
| Junior devs deploying code they don't understand | 40%+ (Deloitte 2025) |
| Security vulnerabilities | Unreviewed AI code |
| Maintenance burden | No one understands the codebase |

### Quality limitations

[[Andrej Karpathy|Karpathy]] himself (who coined the term) tried vibe coding for a project in Oct 2025 — "didn't work well enough" and was "basically entirely handwritten."

**Pattern:** Good for MVPs and prototypes, questionable for production systems.

### Fraud risk

[[Builder.ai]] showed companies can claim "AI" while using human labor. Due diligence must verify actual AI capabilities.

---

## Investment framework

### Bull case

| Thesis | Reasoning |
|--------|-----------|
| **Long [[Lovable]]** | Pure-play leader, $200M ARR, 30x growth |
| **Long [[Supabase]]** | Infrastructure picks-and-shovels |
| **Long [[Vercel]]** | Frontend deployment default |

### Bear case

| Risk | Impact |
|------|--------|
| Big Tech competition | Microsoft (Copilot), Google (Gemini) |
| Quality ceiling | Enterprise won't trust vibe-coded apps |
| Commoditization | Models becoming commodity |

### Second-order plays

| Company | Angle |
|---------|-------|
| [[Anthropic]], [[OpenAI]] | Model providers (already priced) |
| [[NVIDIA]] | Compute (already priced) |
| Cloud providers | Usage growth |

---

## Related

### Key players
- [[Lovable]] — $6.6B pure-play leader
- [[Vercel]] — v0 + deployment platform
- [[Supabase]] — default backend
- [[Builder.ai]] — collapsed fraud

### Investors winning
- [[Menlo Ventures]] — Lovable Series B lead
- [[Accel]] — Lovable, Supabase, Vercel
- [[NVIDIA]] — Lovable investor via NVentures

### Adjacent concepts
- [[Open source commoditization]] — model layer commoditizing
- [[AI hyperscalers]] — compute providers

---

Sources:
- [Wikipedia - Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)
- [Market Clarity - Vibe coding market 2025](https://mktclarity.com/blogs/news/vibe-coding-market)
- [Second Talent - Vibe coding statistics](https://www.secondtalent.com/resources/vibe-coding-statistics/)
- [Vestbee - Vibe coding revolution](https://www.vestbee.com/insights/articles/who-and-how-is-driving-the-vibe-coding-revolution)

*Created 2026-01-14*
