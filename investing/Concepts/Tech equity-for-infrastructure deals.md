---
aliases: [equity-for-compute, equity-for-infrastructure, strategic tech equity deals]
---
#concept #corporatefinance #dealstructure #ai #hyperscaler

**Tech equity-for-infrastructure deals** — a variant of [[commercial warrants]] uniquely suited to technology because of high switching costs, ecosystem lock-in, and winner-take-most dynamics. Tech companies trade equity for committed infrastructure relationships at a scale and frequency unmatched in other industries.

---

## Why tech is different

The [[commercial warrants]] pattern exists everywhere — airlines, energy, pharma — but tech has structural features that make equity-for-volume deals especially powerful:

| Feature | Why it matters in tech | Less relevant elsewhere |
|---------|----------------------|------------------------|
| **Switching costs** | Migrating from one GPU stack/cloud/chip architecture is months of re-engineering | Switching commodity suppliers is weeks |
| **Software ecosystem lock-in** | Hardware choice determines software ecosystem ([[CUDA moat]]) | A barrel of oil is a barrel of oil |
| **Winner-take-most** | AI compute market trending toward 1-2 dominant GPU architectures | Most commodity markets support many suppliers |
| **Exponential demand** | AI capex doubling annually — today's deal is a fraction of tomorrow's | Industrial demand grows linearly |
| **Liquid, volatile equity** | Tech equity is attractive as deal sweetener — high upside optionality | Industrial company equity is less compelling |
| **Reflexive dynamics** | Adoption → ecosystem → more adoption. Volume commitments *create* the moat they bet on | Volume doesn't create structural advantage in commodities |

The last point is critical: in tech, the deal itself changes the competitive landscape. When Meta commits 6GW to AMD, it's not just buying chips — it's building the ecosystem that makes AMD viable. The warrant structure pays AMD in equity for what is functionally a **market-making commitment**.

---

## The modern landscape

### Hyperscaler → AI lab (equity for compute lock-in)

The cloud giants invest equity directly to lock AI labs into their infrastructure:

| Investor | Target | Equity | Cloud commitment | Lock-in |
|----------|--------|--------|-----------------|---------|
| [[Microsoft]] | [[OpenAI]] | ~$13B → 27% equity | **$250B Azure** | Through 2032, IP rights, exclusive cloud |
| [[Amazon]] | [[Anthropic]] | Up to $4B | AWS as primary cloud | Multi-year exclusive |
| [[Google]] | [[Anthropic]] | ~$2B | GCP as secondary cloud | Partial lock-in |
| [[Amazon]] | [[Anthropic]] | Additional $2.75B (2024) | Deepened AWS commitment | Extended |

**Pattern:** The AI lab is the scarce asset (breakthrough models). Hyperscalers compete with equity to capture the workload. Classic [[commercial warrants]] logic — equity flows toward the party with more leverage.

### Chip company → hyperscaler (warrants for volume)

[[AMD]] flipped the direction — the *supplier* gives equity to *buyers*:

| Supplier | Buyer | Warrants | Volume |
|----------|-------|----------|--------|
| [[AMD]] | [[OpenAI]] | 160M shares (~10%) | Undisclosed GW commitment |
| [[AMD]] | [[Meta]] | 160M shares (~10%) | 6GW Instinct GPUs |
| [[STMicro]] | [[Amazon]] | 24.8M shares at $28.38 | AWS semiconductor supply |

**Pattern:** The supplier needs the deal more — AMD needs hyperscaler validation to break the [[CUDA moat]], STMicro needs volume in a cyclical trough. Warrants flow from supplier to buyer.

### Platform → ecosystem (equity for distribution)

Earlier tech era examples where platform companies used equity to build ecosystems:

| Platform | Partner | Structure | Goal |
|----------|---------|-----------|------|
| [[Intel]] | PC OEMs (1990s-2000s) | Marketing subsidies + volume rebates | Lock x86 dominance |
| [[Apple]] | Suppliers (Foxconn, etc.) | Prepayments + capacity guarantees | Supply chain control |
| [[NVIDIA]] | Startups | Inception program + strategic investments | CUDA ecosystem growth |
| [[Google]] | [[Samsung]], OEMs | Revenue share (Android) | Mobile distribution |

These aren't always formal warrants, but the same mechanic: equity or quasi-equity consideration exchanged for commercial commitment and ecosystem lock-in.

---

## Two-way players

Some tech companies are large enough to sit on **both sides** of equity-for-infrastructure deals — as buyer of someone else's infrastructure *and* as seller/platform locking in demand. The direction of equity flow reverses depending on which side they're on.

| Company | As buyer (gives equity/cash) | As seller (receives commitment/equity) |
|---------|------------------------------|---------------------------------------|
| **[[Microsoft]]** | $13B → 27% of [[OpenAI]] | OpenAI commits $250B to Azure |
| **[[Amazon]]** | $6.75B → [[Anthropic]] equity | AWS gets exclusive cloud commitment; receives warrants from [[STMicro]], [[Rivian]], [[Plug Power]] |
| **[[Google]]** | ~$2B → [[Anthropic]] equity; subsidized cloud credits for startups | GCP gets Anthropic as secondary cloud; [[TPU]] ecosystem lock-in |

**Microsoft** is the most intertwined — the same deal simultaneously gives equity (buying the AI lab's loyalty) *and* locks in $250B of demand (selling cloud). Buyer and seller in one transaction.

**Amazon** does it as separate deals — investing in Anthropic on the buy side, extracting warrants from suppliers on the sell side. See [[Amazon commercial warrants]].

**Google** is less formal — it subsidizes cloud credits rather than issuing structured warrants, but the economic logic is identical: equity-like consideration exchanged for ecosystem commitment.

### Who's absent

**[[Meta]]** — purely a buyer. Doesn't sell cloud to third parties, so it only appears on the buy side (NVIDIA deal, AMD deal). If Meta ever opens its infrastructure to third parties, expect it to flip to both sides.

**[[NVIDIA]]** — purely a seller. ~90% GPU market share means it doesn't need to offer equity to anyone. **The day NVIDIA starts offering warrants or strategic equity to lock in customers is the signal that the GPU monopoly is genuinely under threat.** Watch for this.

---

## The reflexivity problem

What makes tech equity-for-infrastructure unique is **reflexivity**: the deal changes the value of the equity being exchanged.

When Meta commits 6GW to AMD:
1. AMD's credibility increases → stock rises → warrants become more valuable to Meta
2. More customers follow Meta → AMD ecosystem grows → [[CUDA moat]] weakens
3. Weaker CUDA moat → more AMD adoption → AMD stock rises further

This creates a **virtuous cycle if execution works** — the deal bootstraps the very outcome it's betting on.

But the reverse is also true (see [[Rivian]] cautionary tale in [[commercial warrants]]): if AMD fails to deliver MI450 at scale, Meta deprioritizes → other customers lose confidence → AMD ecosystem stalls → stock falls → warrants go underwater → alignment mechanism collapses.

Tech amplifies both directions because **market perception and ecosystem adoption are self-reinforcing** in ways that commodity markets are not.

---

## The AI capex era (2024-2027)

The current wave of equity-for-infrastructure deals is unprecedented in scale. Total committed:

| Relationship | Equity at stake | Commercial value |
|-------------|----------------|-----------------|
| Microsoft → OpenAI | ~$13B (27% stake) | $250B Azure |
| Amazon → Anthropic | ~$6.75B | Multi-year AWS exclusive |
| Google → Anthropic | ~$2B | GCP secondary |
| AMD → Meta (warrants) | ~10% of AMD | 6GW / multi-year |
| AMD → OpenAI (warrants) | ~10% of AMD | Multi-GW / multi-year |

**Why now:** AI capex is the largest infrastructure buildout since the internet. $300B+ annual hyperscaler capex creates immense pressure to lock in both supply (chips) and demand (workloads). Equity is the currency because:
- Cash alone doesn't create alignment — the other party can walk
- Equity creates **shared fate** — both sides profit only if the relationship works
- At this scale, even 10% dilution is cheap if it buys a permanent market position

---

## What to watch

- **NVIDIA's response:** Does NVIDIA ever need to offer equity-for-volume, or does ~90% market share mean it never has to? If NVIDIA starts offering warrants, that's a signal of competitive pressure.
- **More AMD deals:** Expect AMD to repeat this with other hyperscalers ([[Google]], [[Oracle]], [[CoreWeave]]).
- **AI lab leverage:** As labs grow (OpenAI $300B valuation), they may demand equity from *cloud providers* rather than giving it. The direction of equity flow will track who has more leverage.
- **Custom silicon threat:** If hyperscalers succeed with in-house chips ([[Google]] TPUs, [[Amazon]] Trainium, [[Meta]] MTIA), the entire equity-for-compute dynamic shifts — they won't need AMD or NVIDIA warrants.

---

## Related

- [[Commercial warrants]] — broader concept (this note covers tech-specific dynamics)
- [[Amazon commercial warrants]] — Amazon's playbook (both directions)
- [[Meta-AMD 6GW deal]] — Feb 24, 2026
- [[AMD]] — equity-for-volume to break CUDA moat
- [[CUDA moat]] — the competitive barrier driving AMD's warrant strategy
- [[OpenAI]] — AMD warrant deal (Oct 2025) + Microsoft equity investment
- [[Microsoft]] — $13B/27% equity in OpenAI for $250B Azure lock-in
- [[Anthropic]] — Amazon + Google equity investments for cloud lock-in
- [[AI hyperscalers]] — the buyers in this landscape
