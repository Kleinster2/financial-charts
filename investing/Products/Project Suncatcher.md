---
aliases: [Suncatcher]
---
#product #space #datacenter #constellation

**Project Suncatcher** — [[Google]]'s orbital data center initiative. Announced November 2025 under the Paradigms of Intelligence research group. Solar-powered satellite constellation carrying [[Google]]'s [[Trillium]] [[TPU]]s, networked by dense wavelength-division multiplexing free-space optical links, with prototype launches by early 2027 partnered with [[Planet Labs]] for satellite hardware. The most concrete near-term Google space-compute initiative. When Google opts to *build* its own constellation rather than purchase capacity from [[SpaceX]] [[Terrafab]], [[Blue Origin]] [[Project Sunrise]], or [[NVIDIA]] [[Vera Rubin Space 1]] customers, the platform-war thesis crosses from concept to confirmed. The May 12 WSJ report that Google is now in talks to use [[SpaceX]] as launch provider materially shortens the path from research moonshot to hardware in orbit — and exposes the structural awkwardness that the only credible heavy-lift partner is the same company building Google's biggest orbital-compute competitor.

---

## Quick stats

| Metric | Value |
|---|---|
| Operator | [[Google]] |
| Research group | Paradigms of Intelligence (Travis Beals, Senior Director) |
| Announced | November 2025 |
| Hardware partner | [[Planet Labs]] |
| Launch-provider talks | [[SpaceX]] (WSJ, May 12 2026) |
| Initial deployment | 2 prototype satellites |
| Prototype launch target | Early 2027 |
| Illustrative production cluster | 81 satellites |
| Orbit | Dawn-dusk sun-synchronous LEO, ~650 km altitude |
| Cluster geometry | ~1 km radius, ~100-200 m inter-satellite separation (oscillating) |
| Compute | [[Trillium]] (TPU v6e) class |
| Inter-satellite link | DWDM + spatial multiplexing; 800 Gbps each-way (1.6 Tbps total) on bench demonstrator |
| Power | Solar (panels ~8x more productive vs Earth in dawn-dusk SSO) |
| Launch-cost assumption | <$200/kg to LEO by mid-2030s |

---

## Strategic positioning

Google's path to orbital data centers differs from peers:

| Player | Strategy |
|---|---|
| [[SpaceX]] / [[xAI]] | Vertically integrate launch + chip ([[Terrafab]]) + DC |
| [[Blue Origin]] | Vertically integrate launch + DC ([[Project Sunrise]] 51,600 sats) |
| [[NVIDIA]] | Sell hardware ([[Vera Rubin Space 1]]) to all builders |
| **[[Google]]** | **Custom hardware (TPU) + solar constellation; partner-launched** |

Google is the only Big Tech hyperscaler making a direct orbital DC bet that doesn't depend on either Bezos or Musk's launch infrastructure for its long-term operations. The Planet Labs partnership for the satellite bus side keeps Google focused on the chip + workload layer.

Per [[Space Capital]] (Chad Anderson, Apr 26, 2026): "When Google builds its own constellation rather than buying capacity from someone else, the thesis is confirmed."

---

## System architecture (Google Research, Nov 2025)

The illustrative production system Google's Paradigms of Intelligence group described in the November 2025 research blog is a cluster of 81 satellites flying in a ~1 km-radius formation at ~650 km altitude in a dawn-dusk sun-synchronous LEO. The orbital choice is load-bearing — in that specific orbit a solar panel is approximately 8x more productive than its terrestrial equivalent and produces power nearly continuously, which is the entire economic case for moving compute off Earth. Each satellite holds station within a roughly 100-200 m oscillation envelope relative to its neighbors so that an optical mesh can knit the 81 nodes into a single distributed-training fabric.

The fabric layer is the part most outsiders underestimate. Earth-side AI training is bottlenecked on cross-rack and cross-datacenter bandwidth, and existing space-to-space radio links cap out far below what modern accelerators consume. Google's design uses dense wavelength-division multiplexing (DWDM) with spatial multiplexing on free-space optical links; the bench-scale demonstrator achieved 800 Gbps each-way, or 1.6 Tbps aggregate per link. That is in the same order of magnitude as the inter-rack NVLink fabric inside a single Earth-side training pod — which is the threshold below which orbital training is uneconomic and above which it stops being a thought experiment.

The third load-bearing assumption is launch cost. The system economics in the paper are written against a target of less than $200/kg to LEO by the mid-2030s. Current SpaceX rideshare pricing per the Q1 2026 [[Space Capital]] briefing is in the $6,000-7,000/kg range and Falcon 9 dedicated is materially higher — so the entire program is structurally a [[Starship]]-economics bet. If Starship full reusability does not converge to the assumed $/kg curve, Suncatcher does not pencil at production scale even if every other technical assumption holds. This is why the WSJ-reported May 12 talks with SpaceX matter beyond the immediate launch question.

---

## Trillium radiation testing

Google tested the [[Trillium]] (TPU v6e) silicon in a 67 MeV proton beam to estimate space hardness for the dawn-dusk SSO mission profile. The relevant results from the November 2025 paper:

| Metric | Value |
|---|---|
| Expected 5-year shielded mission dose | 750 rad(Si) |
| Cumulative dose threshold for first HBM irregularities | 2 krad(Si) — ~2.7x the mission dose |
| Maximum single-chip cumulative dose tested | 15 krad(Si) — ~20x the mission dose |
| Google's framing | "surprisingly radiation-hard for space applications" |

HBM is the weakest link in the test — which tracks with the broader [[Memory|memory]] industry's view that high-bandwidth memory stacks are the most radiation-sensitive component in modern accelerators. The 2 krad threshold being roughly 2.7x the expected lifetime dose means the silicon has a real margin without resorting to mil-spec rad-hardening, which is the historical reason orbital compute has been economically prohibitive — every other space-grade chip program eats a 10-100x cost penalty for rad-hard substrates. Google's read is that consumer/datacenter silicon may already be in the regime where it is "good enough" for LEO with normal aluminum shielding, which is one of the more important enabling claims for the entire orbital-DC thesis if it survives flight validation.

---

## SpaceX launch-provider talks (May 12, 2026)

The Wall Street Journal reported on May 12 that [[Google]] is in active discussions with [[SpaceX]] to launch the Suncatcher prototype payloads. The talks were confirmed in parallel by Bloomberg, Reuters, and TechCrunch on the same day. As of writing the discussions are described as exploratory and no contract has been signed; the existing [[Planet Labs]] hardware partnership and ~early-2027 prototype timeline are unchanged.

The structural read has three layers:

1. **Capacity reality, not partnership preference.** SpaceX is the only launch provider currently flying at the cadence required to deploy a multi-satellite Suncatcher prototype on the announced timeline. Per the Q1 2026 [[Space Capital]] briefing, [[Falcon 9]] is launching roughly every two days at 99% reliability across ~700 cumulative flights, and rideshare slots are the bottleneck rather than rocket availability. [[Rocket Lab]] and [[Blue Origin]] do not yet match that cadence or payload economics on heavier classes. Google needed a partner that could actually deliver in 2027, and that constraint narrowed the field to one name.

2. **Existing equity and board entanglement.** [[Google]] has owned ~6.1% of [[SpaceX]] since the 2015 Series G ($900M at $7.75 split-adjusted), and Google executive Don Harrison sits on the SpaceX board. The talks are partly an inside conversation already, not a cold negotiation between strategic adversaries. That entanglement also caps how aggressively either side can use the relationship against the other in the orbital-DC platform war.

3. **Strategic awkwardness.** The same vehicle that lifts Google's Suncatcher prototypes is built by the company developing the most credible competing orbital-DC stack ([[SpaceX]] / [[xAI]] vertical integration with [[TERAFAB]] silicon, 100 GW capacity vision, lunar manufacturing pipeline). Every Suncatcher launch on Falcon 9 / Starship is revenue to a competitor that uses launch margin to fund competing compute infrastructure. This is the same pattern that has played out repeatedly in semiconductors ([[NVIDIA]] funding [[TSMC]] capacity that competitors share) and cloud ([[AWS]] hosting workloads from rivals). The platform-war thesis says Google would prefer not to be in this position; the operational reality says it has no choice on the 2027 timeline.

The clean read: the talks confirm Google is willing to compromise on strategic independence at the launch layer in exchange for hardware-in-orbit credibility on schedule. This is structurally analogous to [[Anthropic]] taking compute from [[SpaceX]] [[Colossus 1]] in May despite being a frontier-model competitor to [[xAI]] [[Grok]] — when the asset is scarce enough, ideological positioning gives way to capacity access.

*Sources: [Bloomberg — Google in Talks to Use SpaceX to Launch Space Data Centers: WSJ](https://www.bloomberg.com/news/articles/2026-05-12/google-in-talks-to-use-spacex-to-launch-space-data-centers-wsj) (May 12 2026); [TechCrunch — Report: Google and SpaceX in talks to put data centers into orbit](https://techcrunch.com/2026/05/12/report-google-and-spacex-in-talks-to-put-data-centers-into-orbit/) (May 12 2026); Reuters via [Investing.com / TradingView](https://www.investing.com/news/stock-market-news/google-spacex-in-talks-to-explore-data-centers-in-orbit-wsj-reports-4681547) (May 12 2026).*

---

## TPU connection

The TPU choice is significant. Google has invested ~10 years in developing custom silicon (TPU v1 through v6+) optimized for transformer workloads. A space-qualified TPU variant lets Google validate the orbital compute thesis without exposing critical TPU IP to NVIDIA's supply chain or to competing constellations.

If Project Suncatcher reaches production, it positions Google as one of two hyperscalers ([[Microsoft]] being the other major TPU-class customer via OpenAI partnership) with end-to-end vertical integration on AI infrastructure — terrestrial and orbital.

---

## Timeline

| Phase | Target |
|---|---|
| Announce | November 2025 |
| Prototype satellites (2) | Early 2027 |
| Operational constellation | TBD (post-2030 industry consensus per orbital DC field) |

---

## Related

- [[Alphabet]] — parent operator
- [[Google]] — division running Suncatcher
- [[Planet Labs]] — satellite hardware partner
- [[SpaceX]] — launch-provider in talks (May 12 2026)
- [[Trillium]] — TPU v6e silicon, the radiation-tested compute substrate
- [[TPU]] — Google's custom AI silicon family
- [[Starship]] — full-reusability dependency for sub-$200/kg launch economics
- [[Falcon 9]] — near-term launch vehicle for the 2027 prototype
- [[Space data centers]] — concept
- [[Project Sunrise]] — Blue Origin competing constellation
- [[Vera Rubin Space 1]] — NVIDIA orbital compute module
- [[TERAFAB]] — SpaceX/xAI chip program (competing orbital-DC silicon path)
- [[Colossus 1]] — SpaceX terrestrial compute (cross-relationship parallel)
- [[Sundar Pichai]] — public CEO framing of orbital DCs as "new normal" within a decade
- [[Power constraints]] — terrestrial problem orbital DCs aim to solve
- [[Sovereign AI stack]] — competing vertical-integration frame

*Created 2026-04-27 · Expanded 2026-05-13 with Google Research technical specs and May 12 SpaceX launch talks*
