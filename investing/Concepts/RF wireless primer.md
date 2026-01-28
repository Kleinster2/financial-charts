#concept #wireless #telecom #rf #primer

**RF wireless primer** — foundational radio frequency and wireless technology concepts for telecom investing. Understanding wireless helps evaluate spectrum value, [[5G]] economics, and network infrastructure.

> **Key insight:** Spectrum is finite, demand is infinite. Wireless networks are constrained by physics — coverage vs capacity tradeoffs, interference limits, propagation characteristics. The best spectrum is the most valuable real estate in tech.

---

## Radio frequency basics

### Electromagnetic spectrum

| Band | Frequency | Wavelength | Characteristics |
|------|-----------|------------|-----------------|
| Low-band | <1 GHz | >30 cm | Great coverage, limited capacity |
| Mid-band | 1-6 GHz | 5-30 cm | Balance of coverage and capacity |
| High-band (mmWave) | >24 GHz | <12 mm | High capacity, poor coverage |

### Fundamental tradeoffs

```
Lower frequency → Longer range, better penetration, less capacity
Higher frequency → Shorter range, poor penetration, more capacity
```

| Property | Low-band | Mid-band | mmWave |
|----------|----------|----------|--------|
| Range | 10+ miles | 1-5 miles | <1 mile |
| Building penetration | Excellent | Good | Poor |
| Capacity | Low | Medium | High |
| Spectrum available | Scarce | Medium | Abundant |

---

## Spectrum bands (US mobile)

### Low-band (<1 GHz)

| Band | Frequency | Owner | Notes |
|------|-----------|-------|-------|
| 600 MHz | 617-698 MHz | T-Mobile | Best coverage |
| 700 MHz | 698-806 MHz | AT&T, Verizon | Good coverage |
| 850 MHz | 824-894 MHz | AT&T, Verizon | Legacy cellular |

### Mid-band (1-6 GHz)

| Band | Frequency | Owner | Notes |
|------|-----------|-------|-------|
| AWS | 1710-2200 MHz | All carriers | Core LTE |
| PCS | 1850-1995 MHz | All carriers | Legacy 2G/3G/LTE |
| **C-band** | 3700-3980 MHz | Verizon, AT&T | [[5G]] sweet spot |
| **CBRS** | 3550-3700 MHz | Shared | Private networks |
| 2.5 GHz | 2496-2690 MHz | T-Mobile | [[5G]] capacity |

### High-band (mmWave)

| Band | Frequency | Use |
|------|-----------|-----|
| 28 GHz | 27.5-28.35 GHz | [[5G]] hotspots |
| 39 GHz | 37-40 GHz | [[5G]] capacity |
| 47 GHz | 47.2-48.2 GHz | Future [[5G]] |

**C-band is the prize:** Best balance of coverage and capacity for [[5G]]. Verizon and AT&T spent $80B+ acquiring it.

---

## Wireless generations

| Gen | Era | Peak speed | Key tech | Use |
|-----|-----|------------|----------|-----|
| 2G | 1990s | 64 Kbps | GSM, CDMA | Voice, SMS |
| 3G | 2000s | 2 Mbps | UMTS, EVDO | Mobile internet |
| 4G/LTE | 2010s | 100+ Mbps | OFDMA | Smartphones, video |
| **[[5G]]** | 2020s | 1+ Gbps | OFDM, massive MIMO | IoT, low latency |
| 6G | 2030s | 100+ Gbps | THz, AI-native | TBD |

---

## [[5G]] technology

### Three flavors of [[5G]]

| Type | Spectrum | Speed | Coverage | Status |
|------|----------|-------|----------|--------|
| **Low-band [[5G]]** | 600-900 MHz | 50-200 Mbps | Wide | Nationwide |
| **Mid-band [[5G]]** | 2.5-4 GHz | 200-900 Mbps | Medium | Expanding |
| **mmWave [[5G]]** | 24-40 GHz | 1-4 Gbps | Very limited | Urban hotspots |

### Key [[5G]] technologies

| Technology | What it does |
|------------|--------------|
| **Massive MIMO** | Many antennas (64-256) for capacity + beamforming |
| **Beamforming** | Direct signal to specific user vs broadcast |
| **Carrier aggregation** | Combine multiple spectrum bands |
| **Network slicing** | Virtual networks for different use cases |
| **Small cells** | Dense deployment for capacity |

### MIMO explained

Multiple Input, Multiple Output — use multiple antennas to increase throughput.

| Configuration | Antennas | Capacity gain |
|---------------|----------|---------------|
| 2x2 MIMO | 2 TX, 2 RX | 2x |
| 4x4 MIMO | 4 TX, 4 RX | 4x |
| Massive MIMO | 64+ TX | 10x+ |

**Massive MIMO:** [[5G]] base stations with 64-256 antenna elements. Serves many users simultaneously via spatial multiplexing.

---

## Network architecture

### Traditional RAN (Radio Access Network)

```
User device ←→ Base station ←→ Backhaul ←→ Core network ←→ Internet
```

| Component | Function |
|-----------|----------|
| **UE (User Equipment)** | Phone, modem |
| **RAN** | Radio access (base stations) |
| **Backhaul** | Connects RAN to core (fiber, microwave) |
| **Core** | Routing, authentication, mobility |

### Open RAN (O-RAN)

Disaggregate RAN into modular, interoperable components.

| Traditional | Open RAN |
|-------------|----------|
| Proprietary, integrated | Open interfaces |
| Single vendor | Multi-vendor |
| Hardware-defined | Software-defined |

**O-RAN promise:** Lower costs, more innovation, reduce Ericsson/Nokia dominance.

**O-RAN reality:** Integration challenges, performance gaps, slower rollout.

---

## Cell site economics

### Macro cell (traditional tower)

| Component | Cost |
|-----------|------|
| Tower lease | $2,000-3,000/month |
| Equipment | $50,000-200,000 |
| Backhaul | $500-2,000/month |
| Power | $500-1,500/month |
| Maintenance | $1,000-2,000/month |

**Total cost:** $5,000-10,000/month per macro site.

### Small cells ([[5G]] densification)

| Type | Coverage | Cost |
|------|----------|------|
| Macro | 1-10 miles | High |
| Small cell | 100-1,000 ft | Low-medium |
| Femtocell | 30-50 ft | Low |

**[[5G]] economics:** Need 5-10x more cell sites for same coverage with mmWave. Small cells critical.

---

## Spectrum economics

### Spectrum value

| Factor | Impact on value |
|--------|-----------------|
| Frequency | Lower = more valuable (coverage) |
| Bandwidth | More MHz = more capacity |
| License type | Exclusive > shared |
| Geography | Urban > rural |
| Incumbency | Easier to expand than enter |

### Spectrum auctions (US)

| Auction | Year | Total | Winner |
|---------|------|-------|--------|
| AWS-3 | 2015 | $45B | AT&T, Verizon, T-Mobile |
| C-band | 2021 | $81B | Verizon ($45B), AT&T ($23B) |
| 3.45 GHz | 2022 | $22B | AT&T, Dish, T-Mobile |

**C-band dominance:** Verizon bet big. Now has mid-band advantage.

---

## Key equipment vendors

### RAN equipment

| Vendor | Market share | Strength |
|--------|--------------|----------|
| **[[Huawei]]** | ~30% global | Cost, scale (banned in US/[[Europe]]) |
| **Ericsson** | ~25% | Technology leadership |
| **Nokia** | ~20% | Diversified |
| **[[Samsung]]** | ~10% | Growing, US wins |
| **ZTE** | ~10% | [[China]] (sanctions risk) |

### Infrastructure

| Category | Key players |
|----------|-------------|
| Towers | American Tower, Crown Castle, SBA |
| Small cells | Crown Castle, CommScope |
| Fiber backhaul | Zayo, Lumen, regional providers |
| DAS (indoor) | CommScope, [[Corning]] |

---

## US carrier landscape

| Carrier | Spectrum position | Strategy |
|---------|-------------------|----------|
| **Verizon** | Strong mid-band (C-band) | Premium, reliability |
| **AT&T** | Balanced | Business, fiber convergence |
| **T-Mobile** | Best low + mid-band (2.5 GHz) | Coverage, value |
| **Dish** | New entrant (AWS, 600 MHz) | Building O-RAN network |

### Spectrum holdings comparison

| Band | Verizon | AT&T | T-Mobile |
|------|---------|------|----------|
| Low-band | Weak | Medium | Strong (600 MHz) |
| Mid-band | Strong (C-band) | Medium | Strong (2.5 GHz) |
| mmWave | Strong | Medium | Weak |

---

## Wireless metrics

### Network performance

| Metric | Definition |
|--------|------------|
| **Throughput** | Data rate (Mbps) |
| **Latency** | Delay (ms) |
| **Coverage** | Area served |
| **Reliability** | Uptime, dropped calls |
| **Spectral efficiency** | Bits/Hz |

### Business metrics

| Metric | Definition |
|--------|------------|
| **ARPU** | Average revenue per user |
| **Churn** | Customer cancellation rate |
| **Postpaid adds** | Higher-value subscribers |
| **Prepaid adds** | Lower-value subscribers |
| **Capex/Revenue** | Network investment intensity |

---

## Emerging wireless technologies

### Wi-Fi 6/6E/7

| Gen | Frequency | Speed | Use |
|-----|-----------|-------|-----|
| Wi-Fi 6 | 2.4/5 GHz | 9.6 Gbps | Current standard |
| Wi-Fi 6E | + 6 GHz | Same | More spectrum |
| Wi-Fi 7 | 2.4/5/6 GHz | 46 Gbps | 2024+ |

**Wi-Fi vs [[5G]]:** Complementary. Wi-Fi for indoor/offload, cellular for mobility.

### Private [[5G]] (CBRS)

Enterprises deploy own [[5G]] networks using shared CBRS spectrum.

| Use case | Industry |
|----------|----------|
| Factory automation | Manufacturing |
| Warehouse logistics | Retail, logistics |
| Campus coverage | Enterprise, education |
| Remote operations | Mining, oil & gas |

### Fixed Wireless Access (FWA)

[[5G]] as home broadband alternative.

| Carrier | Subscribers |
|---------|-------------|
| T-Mobile | 5M+ |
| Verizon | [[3M]]+ |

**Economics:** Low marginal cost if network has excess capacity. Competitive threat to cable.

---

## Key investment themes

| Theme | Expression |
|-------|------------|
| Spectrum value | Carriers with best mid-band |
| Tower growth | American Tower, Crown Castle |
| [[5G]] equipment | Ericsson, Nokia (O-RAN wild card) |
| Private [[5G]] | [[Cisco]], CommScope |
| FWA disruption | T-Mobile, Verizon vs cable |

---

## Related

- [[Telecom]] — sector overview
- [[Verizon]] — C-band leader
- [[T-Mobile]] — coverage leader
- [[AT&T]] — balanced carrier
- [[American Tower]] — tower REIT
- [[Crown Castle]] — tower/small cell REIT
- [[Ericsson]] — equipment vendor
- [[Nokia]] — equipment vendor
- [[Satellite primer]] — non-terrestrial wireless
