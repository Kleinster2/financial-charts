#concept #batteries #energy #science #primer

**Battery chemistry primer** — foundational electrochemistry and manufacturing concepts for battery investing. Understanding the technology helps evaluate EV range claims, grid storage economics, and supply chain vulnerabilities.

> **Key insight:** Batteries are a materials problem. Chemistry determines energy density, cost, safety, and lifespan. There is no perfect battery — every chemistry is a tradeoff.

---

## How batteries work

Batteries store energy in chemical bonds. Discharge releases electrons (electricity). Charge reverses the reaction.

```
Discharge:
  Anode (−) → releases electrons → External circuit → Cathode (+)
                                         ↓
                               Powers your device
```

| Component | Function | Materials |
|-----------|----------|-----------|
| **Cathode** (+) | Stores lithium ions | NMC, LFP, NCA |
| **Anode** (−) | Releases electrons | Graphite, silicon |
| **Electrolyte** | Ion transport | Liquid, solid |
| **Separator** | Prevents short circuit | Polymer membrane |

**Cathode determines chemistry name.** When people say "LFP battery" or "NMC battery," they mean the cathode material.

---

## Lithium-ion chemistries

### LFP (Lithium Iron Phosphate)

| Property | Value |
|----------|-------|
| Cathode | LiFePO₄ |
| Energy density | 150-180 Wh/kg |
| Cycle life | 2,000-4,000 cycles |
| Safety | Excellent (stable) |
| Cost | **Lowest** |
| Temperature | Poor in cold |

**Use cases:** Standard-range EVs, grid storage, commercial vehicles.

**Leaders:** [[CATL]], [[BYD]] (Blade Battery).

**Why LFP is winning:** No cobalt or nickel = cheaper, more stable supply chain. China dominates.

### NMC (Nickel Manganese Cobalt)

| Property | Value |
|----------|-------|
| Cathode | LiNiₓMnᵧCo₂O₂ |
| Energy density | 230-270 Wh/kg |
| Cycle life | 1,000-2,000 cycles |
| Safety | Moderate |
| Cost | Higher |
| Temperature | Better |

**Variants:** NMC 532, NMC 622, NMC 811 (numbers = Ni:Mn:Co ratio). Higher nickel = more energy, less stability.

**Use cases:** Long-range EVs, premium vehicles.

**Leaders:** LG Energy, SK On, Samsung SDI.

### NCA (Nickel Cobalt Aluminum)

| Property | Value |
|----------|-------|
| Cathode | LiNiCoAlO₂ |
| Energy density | 250-300 Wh/kg |
| Cycle life | 500-1,000 cycles |
| Safety | Lowest |
| Cost | High |

**Use cases:** Tesla Model S/X (historically), high-performance.

**Leader:** Panasonic (Tesla partnership).

---

## Energy density — why it matters

| Metric | Definition | Impact |
|--------|------------|--------|
| **Gravimetric** | Wh/kg | Vehicle range (lighter = better) |
| **Volumetric** | Wh/L | Pack size (smaller = better) |

| Chemistry | Wh/kg | Wh/L |
|-----------|-------|------|
| LFP | 150-180 | 250-300 |
| NMC | 230-270 | 400-500 |
| NCA | 250-300 | 500-600 |
| Solid-state (future) | 400+ | 700+ |

**Tradeoff:** Higher energy density usually means lower cycle life, higher cost, worse safety.

---

## Cell formats

| Format | Shape | Use | Examples |
|--------|-------|-----|----------|
| **Cylindrical** | Can (18650, 21700, 4680) | EVs, laptops | Tesla |
| **Prismatic** | Rectangular box | EVs, ESS | BYD, CATL |
| **Pouch** | Flat foil bag | EVs, phones | LG, SK |

**4680:** Tesla's new cylindrical format. 46mm diameter × 80mm length. 5x energy, 6x power vs 21700. Tabless design reduces internal resistance.

---

## Degradation — why batteries die

| Mechanism | Cause | Effect |
|-----------|-------|--------|
| **SEI growth** | Electrolyte decomposition | Capacity loss |
| **Lithium plating** | Fast charging in cold | Shorts, fire risk |
| **Dendrites** | Uneven lithium deposition | Shorts |
| **Cathode cracking** | Volume change | Resistance increase |

**Cycle life:** Number of full charge/discharge cycles before 80% capacity.

**Calendar aging:** Degradation from time, even when not used. ~2-3% per year.

**Fast charging tradeoff:** Higher C-rates accelerate degradation. DC fast charging is hard on batteries.

---

## Manufacturing process

```
1. Electrode production
   - Mix active material + binder + conductive additive
   - Coat onto metal foil (Al for cathode, Cu for anode)
   - Dry, compress, cut

2. Cell assembly
   - Stack or wind electrodes with separator
   - Insert into housing
   - Fill with electrolyte
   - Seal

3. Formation
   - Initial charge/discharge cycles
   - Forms protective SEI layer
   - Takes days, uses significant energy

4. Aging & testing
   - Rest period (weeks)
   - Capacity/impedance testing
   - Grade and sort
```

**Manufacturing cost breakdown:**

| Component | % of cell cost |
|-----------|---------------|
| Cathode | 40-50% |
| Anode | 10-15% |
| Separator | 10-15% |
| Electrolyte | 10-15% |
| Housing/other | 10-20% |

---

## Raw materials — supply chain risk

| Material | Use | Dominant source | Risk |
|----------|-----|-----------------|------|
| **Lithium** | All Li-ion | Australia, Chile | Price volatility |
| **Cobalt** | NMC, NCA | DRC (70%) | Ethical, supply |
| **Nickel** | NMC, NCA | Indonesia, Russia | Geopolitical |
| **Graphite** | Anode | China (65%) | Export controls |
| **Manganese** | NMC, LFP | South Africa | Stable |
| **Iron** | LFP | Global | Abundant |

**LFP advantage:** No cobalt, no nickel = no DRC, no Russia, no Indonesia risk.

See [[Lithium]], [[Critical minerals]].

---

## Next-generation technologies

### Solid-state batteries

Replace liquid electrolyte with solid material.

| Property | Solid-state | Li-ion |
|----------|-------------|--------|
| Energy density | 400+ Wh/kg | 250-300 |
| Safety | No fire risk | Thermal runaway |
| Cycle life | TBD | 1,000-4,000 |
| Manufacturing | **Very hard** | Mature |
| Cost | Very high | Declining |

**Challenges:** Solid-solid interface degrades. Scaling manufacturing. Still 5+ years from mass production.

**Players:** [[QuantumScape]], Toyota, Samsung SDI, Solid Power.

### Silicon anodes

Replace graphite with silicon for higher capacity.

| Anode | Capacity (mAh/g) |
|-------|-----------------|
| Graphite | 372 |
| Silicon | 4,200 |

**Problem:** Silicon expands 300% during charge → cracks → degrades. Current solutions use silicon-graphite blends (5-10% silicon).

### Sodium-ion

Sodium instead of lithium. Cheaper, abundant, but lower energy density.

| Property | Sodium-ion | LFP |
|----------|------------|-----|
| Energy density | 100-150 Wh/kg | 150-180 |
| Cost | Lower | Low |
| Cycle life | Good | Excellent |
| Cold performance | Better | Poor |

**Use cases:** Grid storage, low-cost EVs. [[CATL]] shipping sodium-ion in 2024.

---

## Grid storage vs EV requirements

| Requirement | EV | Grid storage |
|-------------|-----|--------------|
| Energy density | Critical | Less important |
| Weight | Critical | Not important |
| Cycle life | 1,000-2,000 | 4,000-10,000 |
| Cost/kWh | <$100 target | <$50 target |
| Safety | Important | Critical (large scale) |

**Implication:** LFP dominates grid storage. NMC/NCA for long-range EVs.

---

## Cost trajectory

| Year | Pack price ($/kWh) |
|------|-------------------|
| 2010 | ~$1,100 |
| 2015 | ~$400 |
| 2020 | ~$140 |
| 2024 | ~$115 |
| 2030E | ~$70-80 |

**$100/kWh:** Historical target for EV cost parity with ICE. Achieved for LFP cells.

**Learning rate:** ~18% cost reduction per doubling of cumulative production.

---

## Key metrics for investors

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **GWh shipped** | Capacity deployed | Market share |
| **Cell cost $/kWh** | Manufacturing efficiency | Margin, competitiveness |
| **Utilization** | Factory capacity used | Profitability |
| **Energy density** | Wh/kg, Wh/L | Technology position |
| **Cycle life** | Warranty proxy | Quality, returns |

---

## Competitive landscape

| Company | Chemistry focus | Strength |
|---------|-----------------|----------|
| [[CATL]] | LFP, NMC, sodium | Scale (#1 globally) |
| [[BYD]] | LFP (Blade) | Vertical integration |
| LG Energy | NMC, pouch | Premium EVs |
| Panasonic | NCA, cylindrical | Tesla partnership |
| [[SK Hynix]] (SK On) | NMC | Growth |
| Samsung SDI | NMC, prismatic | Diversified |

**China dominance:** ~80% of global cell production. [[China battery leverage]] is real.

---

## Related

- [[Lithium]] — key raw material
- [[CATL]] — market leader
- [[BYD]] — vertical integration
- [[China battery leverage]] — tech transfer restrictions
- [[EV transition]] — demand driver
- [[Battery supply chain]] — full value chain
- [[Critical minerals]] — supply risks
- [[QuantumScape]] — solid-state bet
