#concept #autonomous #ai #transportation

**Autonomous vehicles** — Self-driving technology spanning ADAS to full autonomy. Waymo leads robotaxi. Aurora leads trucking. Tesla pursuing different path. Multi-decade, capital-intensive race.

---

## The autonomy spectrum

| Level | Name | Driver role | Examples |
|-------|------|-------------|----------|
| L0 | No automation | Full control | Base cars |
| L1 | Driver assistance | Hands on | Adaptive cruise |
| L2 | Partial automation | Eyes on road | Tesla Autopilot, GM SuperCruise |
| L2+ | Advanced assist | Eyes off (limited) | [[Mobileye]] SuperVision |
| L3 | Conditional | Hands off, ready to take over | Mercedes Drive Pilot |
| L4 | High automation | No driver needed (geo-fenced) | [[Waymo]], [[Cruise]] |
| L5 | Full automation | Anywhere, any conditions | Doesn't exist |

**Key insight**: L2 → L3 is the hardest gap (liability transfer). L4 works by constraining geography.

---

## Two philosophies

### Camera-first (Tesla)

| Aspect | Approach |
|--------|----------|
| Sensors | Cameras only (removed radar, ultrasonic) |
| Data | Billions of miles from customer fleet |
| Training | End-to-end neural networks |
| Goal | L4/L5 everywhere |
| Status | L2 supervised only |

**Bet**: Vision + AI can match human driving.

### Sensor fusion (Waymo, Cruise, Aurora)

| Aspect | Approach |
|--------|----------|
| Sensors | Lidar + cameras + radar |
| Data | Fleet of dedicated test vehicles |
| Mapping | HD maps of operating areas |
| Goal | L4 in geo-fenced areas |
| Status | Waymo commercial, others developing |

**Bet**: Redundancy + mapping = safety.

---

## The players

### Robotaxi

| Company | Parent | Status | Cities |
|---------|--------|--------|--------|
| [[Waymo]] | Alphabet | **Commercial** | SF, Phoenix, LA, Austin |
| [[Cruise]] | GM | Paused | — |
| [[Zoox]] | Amazon | Testing | SF, Vegas |
| [[Baidu]] Apollo | Baidu | Commercial | Wuhan, Beijing |
| WeRide | Independent | Commercial (China) | Guangzhou |
| Pony.ai | Independent | Commercial (China) | Multiple |

**US winner**: Waymo (only scaled commercial robotaxi).

### Autonomous trucking

| Company | Status | Routes |
|---------|--------|--------|
| [[Aurora]] | **Commercial** | Dallas-Houston |
| Kodiak | Testing | Regional |
| TuSimple | Failed | — |
| Embark | Shut down | — |

**Trucking thesis**: Highways simpler than cities. Driver shortage acute. Economics compelling.

### ADAS suppliers

| Company | Product | Market position |
|---------|---------|-----------------|
| [[Mobileye]] | EyeQ chips | 70%+ front camera |
| [[NVIDIA]] | Drive platform | High-end compute |
| Qualcomm | Snapdragon Ride | Challenger |

---

## Why robotaxi is hard

| Challenge | Impact |
|-----------|--------|
| **Edge cases** | Infinite long tail of scenarios |
| **Unit economics** | Each city = $100M+ investment |
| **Regulation** | City-by-city, state-by-state approval |
| **Safety bar** | One incident = permits revoked (Cruise) |
| **Liability** | Who's responsible when things go wrong? |
| **Public trust** | Slow to build, fast to lose |

**Waymo's 15-year journey**: Still not profitable after $5B+ invested.

---

## Why trucking may win first

| Factor | Trucking advantage |
|--------|-------------------|
| **Routes** | Highway = simpler than urban |
| **Economics** | Driver shortage, fatigue limits |
| **Customers** | B2B = rational buyers |
| **Regulation** | Less pedestrian interaction |
| **Safety** | Fewer edge cases per mile |

Aurora commercial before Waymo profitable.

---

## Tesla's different bet

| Aspect | Tesla approach | Traditional approach |
|--------|---------------|---------------------|
| Fleet | 5M+ customer cars | Hundreds of test vehicles |
| Data | Billions of miles | Millions of miles |
| Cost | Customers pay | Company pays |
| Liability | Customer (L2) | Company (L4) |
| Hardware | Consumer-grade | Expensive lidar stacks |

**FSD status (2025)**:
- Still L2 (supervised)
- "Full self-driving" name controversial
- Promised robotaxi delayed
- Cybercab announced, not shipped

**Bull case**: Data advantage + AI leads to L4.
**Bear case**: Camera-only can't achieve L4 safety.

---

## China's parallel race

| Player | Status | Approach |
|--------|--------|----------|
| [[Baidu]] Apollo | Commercial robotaxi | Waymo-like |
| Pony.ai | Commercial | Toyota-backed |
| WeRide | Commercial | Renault-Nissan partner |
| Huawei | ADAS supplier | Mobileye competitor |
| Horizon Robotics | ADAS chips | Chinese Mobileye |

**Key difference**: Faster regulatory approval, more permissive testing.

---

## Investment framework

### Pure plays (public)

| Company | Ticker | Focus | Risk |
|---------|--------|-------|------|
| [[Aurora]] | AUR | Trucking | Execution |
| [[Mobileye]] | MBLY | ADAS chips | China loss |

### Embedded in conglomerates

| Company | Ticker | AV asset | % of value |
|---------|--------|----------|------------|
| Alphabet | GOOGL | Waymo | ~5-10% |
| Amazon | AMZN | Zoox | <1% |
| GM | GM | Cruise | Negative |
| Intel | INTC | Mobileye (88%) | Significant |

### Suppliers

| Company | AV exposure |
|---------|-------------|
| [[NVIDIA]] | Drive platform, simulation |
| Luminar | Lidar (struggling) |
| Velodyne/Ouster | Lidar (merged) |

---

## The cautionary tales

| Company | What happened | Lesson |
|---------|--------------|--------|
| **Cruise** | 2023 incident, cover-up | Safety + transparency paramount |
| **TuSimple** | China ties, delisted | Geopolitical risk |
| **Embark** | Ran out of money | Capital intensity |
| **Argo AI** | Ford/VW pulled plug | OEM patience limited |
| **Apple Car** | Cancelled 2024 | Even Apple couldn't crack it |

---

## Timeline reality check

| Prediction | Made | Actual |
|------------|------|--------|
| Elon: "Robotaxi 2020" | 2016 | Still supervised (2025) |
| Waymo profitable | Various | Still losing money |
| L4 everywhere | 2010s hype | Geo-fenced only |

**Pattern**: Timelines always slip. L4 harder than expected.

---

## Investment implications

**Avoid**:
- Pure lidar plays (commoditizing)
- Pre-revenue AV startups
- OEMs betting future on autonomy

**Consider**:
- ADAS suppliers with current revenue (Mobileye)
- Trucking (Aurora) — better unit economics
- Waymo via Alphabet (small % of value, optionality)

**Watch for**:
- Tesla FSD to L3/L4 (would be transformational)
- Waymo profitability milestone
- China robotaxi scaling

---

## Related

- [[Waymo]] — Robotaxi leader
- [[Cruise]] — Cautionary tale
- [[Aurora]] — Trucking leader
- [[Zoox]] — Amazon's bet
- [[Mobileye]] — ADAS chips
- [[Tesla]] — Camera-only approach
- [[Baidu]] — China leader
- [[Automotive semiconductors]] — ADAS chip market
- [[NVIDIA]] — Drive platform
