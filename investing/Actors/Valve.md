---
aliases: [Valve Corporation, Valve Software]
tags: [actor, gaming, platform, hardware, usa, private]
---

# Valve

#actor #gaming #platform #hardware #usa #private

Valve is the private company behind [[Steam platform|Steam]], the dominant PC game storefront, and the only major platform holder trying to turn an open PC ecosystem into console-like hardware through [[SteamOS]], [[Steam Deck]], [[Steam Machine]], [[Steam Controller]], and [[Steam Frame]].

Valve matters because it controls the PC distribution layer rather than the device layer. The company can make hardware with lower strategic pressure than [[Sony]], [[Microsoft]], or [[Nintendo]] because the core economics still come from software distribution, marketplace fees, and first-party live-service games. A [[Steam Machine]] sale is useful, but the bigger prize is making [[SteamOS]] credible enough that the Steam library follows users from desk to couch to handheld to VR without [[Windows]] being the default operating layer.

The open question is whether Valve can make open PC hardware feel enough like a console without losing the economics that make consoles work. [[Steam Machine]] is an open PC: users can install other apps or even another operating system. That makes it harder to subsidize like [[Sony|PlayStation]] or [[Microsoft|Xbox]], because Valve cannot guarantee that every box becomes a captive software customer. The strategy therefore hinges on performance-per-dollar, ease of use, [[Proton (Valve)|Proton]] compatibility, and whether [[SteamOS]] creates a good enough couch experience to overcome the price gap with subsidized consoles.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 1996 |
| Founders | [[Gabe Newell]], [[Mike Harrington]] |
| Headquarters | Bellevue, Washington |
| Ownership | Private |
| Core platform | [[Steam platform|Steam]] |
| Hardware line | [[Steam Deck]], [[Steam Machine]], [[Steam Controller]], [[Steam Frame]], [[Steam Link]] |
| Operating system | [[SteamOS]] |
| Compatibility layer | [[Proton (Valve)|Proton]] |
| Key first-party games | [[Counter-Strike 2]], [[Dota 2]] |
| 2025 Steam scale | 42M peak concurrent users; 100 exabytes delivered; 5,863 games earned over $100K |

---

## Leadership

| Role | Person | Notes |
|------|--------|-------|
| CEO / president | [[Gabe Newell]] | Co-founder, majority owner, and controlling strategic voice |
| Co-founder | [[Mike Harrington]] | Co-founded Valve in 1996; left the company in 2000 |

Valve is unusually opaque by public-company standards. The practical leadership signal is Newell's founder-control position plus Valve's self-directed operating model rather than a conventional public-company executive bench.

---

## Ownership

| Holder | Stake | Notes |
|--------|-------|-------|
| [[Gabe Newell]] | ~50.1% | Forbes estimate; no public company cap table |
| Employees / former employees | Remainder | Forbes reports employees own the rest; individual stakes are not public |

Valve is private and does not publish audited financial statements, capitalization tables, or shareholder registers. Treat all ownership percentages as estimates.

---

## Funding history

| Date | Round | Amount | Lead/source | Notes |
|------|-------|--------|-------------|-------|
| 1996 | Founder funding | Undisclosed | [[Gabe Newell]] / [[Mike Harrington]] | Founded after both left [[Microsoft]]; no disclosed venture round |
| 1998-present | External equity funding | None disclosed | n/a | Valve remains privately held and has not disclosed institutional funding rounds |

---

## Financials

| Year | Revenue | Notes |
|------|---------|-------|
| 2023 | ~$5B estimated | Forbes estimate; Valve does not disclose audited revenue |
| 2025 | Steam platform indicators: 42M peak concurrent users; 100 exabytes delivered; 5,863 games earned over $100K | Platform activity, not company revenue |

---

## Evolution

The story of Valve is the story of a game studio that became the toll road for PC gaming, then used hardware to keep that road from being routed through someone else's operating system.

- 1996-2003: Valve began as a PC game studio and built credibility through first-party games before turning distribution into the strategic asset. [[Steam platform|Steam]] launched in 2003 as a patching and distribution system, then became the default PC storefront. The key economic shift was that Valve moved from selling hits to taking a recurring platform cut across other publishers' hits.

- 2013-2018: The first Steam Machines were the premature version of the strategy. Valve pushed [[SteamOS]], the original [[Steam Controller]], and OEM-built living-room PCs, but the product set was fragmented and [[Linux]] game compatibility was not ready. The effort faded by 2018, but the work did not disappear: [[Proton (Valve)|Proton]], Steam Input, Big Picture, and the [[Linux]] driver stack kept improving under the surface.

- 2022-2025: [[Steam Deck]] proved the second attempt could work. Valve controlled the hardware, the operating system, and the compatibility layer in one integrated device, while keeping PC openness. The result was a handheld that made SteamOS tangible rather than ideological. By 2025, Valve could credibly extend the same software stack across handheld, living room, and VR.

- 2025-2026: The new hardware wave makes the old Steam Machine thesis coherent. Valve announced [[Steam Machine]], [[Steam Controller]], and [[Steam Frame]] on November 12, 2025, then used the GDC 2026 Steam Hardware Talk to frame them as one SteamOS family rather than isolated devices. The [[Steam Controller]] shipped first on May 4, 2026 at $99; [[Steam Machine]] and [[Steam Frame]] still lacked final public price and launch dates as of the May 2026 source check, with memory and storage shortages pressuring the schedule.

---

## Platform economics

| Layer | Valve position | Why it matters |
|-------|----------------|----------------|
| Storefront | [[Steam platform|Steam]] | Core distribution layer for PC games |
| Operating system | [[SteamOS]] | Reduces dependence on Windows for couch/handheld PC gaming |
| Compatibility | [[Proton (Valve)|Proton]] | Lets Windows-first games run on SteamOS with less developer work |
| Hardware | [[Steam Deck]], [[Steam Machine]], [[Steam Frame]] | Makes SteamOS useful in real form factors |
| Input | [[Steam Controller]], Steam Input | Solves PC-games-from-couch control problem |
| First-party games | [[Counter-Strike 2]], [[Dota 2]] | High-margin owned content and marketplace activity |

Valve's structural advantage is that it does not need to win the console market outright. If [[SteamOS]] hardware makes Steam a better default for PC gamers, Valve strengthens the storefront even when the hardware profit pool is small.

---

## Steam hardware strategy

[[Steam Machine]] is the living-room expression of the [[Steam Deck]] playbook: Valve-owned hardware, [[SteamOS]] as the default interface, [[Proton (Valve)|Proton]] for game compatibility, and Steam Input for controller adaptation. The 2026 version is much cleaner than the 2015 OEM program because the hardware target is singular: a roughly six-inch cube with semi-custom [[AMD]] CPU/GPU silicon, 16GB DDR5, 8GB GDDR6 VRAM, and 512GB or 2TB storage.

The strategic risk is pricing. Valve's own February 2026 FAQ said memory and storage shortages forced it to revisit exact schedule and pricing, especially for Steam Machine and Steam Frame. Separately, Valve engineer Pierre-Loup Griffais told Skill Up that Steam Machine pricing should be compared with equivalent PCs rather than subsidized consoles. That keeps the product honest as a PC, but it narrows the addressable audience if the final price sits closer to a compact gaming PC than to a $499 console.

[[Kalshi]]'s KXSTEAMPRICE-27 ladder confirms that this is the live market debate: as of the May 2026 API read, prediction-market pricing implied a center around $800-$899, with "at least $800" trading near 62c last and "at least $900" near 27c last. That reads as a PC-like price expectation rather than a console-subsidy expectation.

---

## What to watch

- Steam Machine price - if it lands near console pricing, Valve can test mainstream couch adoption; if it lands near boutique mini-PC pricing, the device is more likely to stay enthusiast-led.
- SteamOS verified library - GDC 2026 guidance says all Deck Verified games are Machine Verified; the breadth and trust of that badge determines plug-and-play credibility.
- Proton and anti-cheat compatibility - kernel anti-cheat and secure-boot-dependent games remain the main friction for a [[Linux]]-based gaming PC.
- Supply constraints - Valve's own timing update identified memory and storage as the schedule/pricing constraint.
- Controller attach rate - [[Steam Controller]] is the couch input layer; strong adoption makes Steam Machine more viable even before the box ships.
- Third-party SteamOS devices - if third-party OEMs expand SteamOS PCs, Valve wins platform share even without owning all hardware volume.

---

## Related

### Products
- [[Steam platform]] - PC game storefront and core economics
- [[SteamOS]] - gaming-first operating system
- [[Proton (Valve)|Proton]] - compatibility layer for Windows games on SteamOS
- [[Steam Deck]] - handheld proof point
- [[Steam Machine]] - living-room SteamOS PC
- [[Steam Controller]] - couch input layer
- [[Steam Frame]] - VR/non-VR headset
- [[Steam Link]] - earlier streaming device/app
- [[Counter-Strike 2]] - first-party live-service shooter
- [[Dota 2]] - first-party MOBA

### Sector
- [[Gaming]] - publishers and platforms
- [[Gaming Hardware]] - gaming PCs, peripherals, and hardware cycle

### Hardware suppliers and competitors
- [[AMD]] - semi-custom Steam Machine CPU/GPU supplier
- [[Microsoft]] - Xbox, Windows, and Game Pass
- [[Sony]] - PlayStation
- [[Nintendo]] - Switch ecosystem

---

## Sources

- [Valve / Steam hardware announcement mirrored by Gematsu](https://www.gematsu.com/2025/11/valve-announces-steam-machine-steam-frame-and-steam-controller) (Nov 12, 2025)
- [Valve timing and FAQ update mirrored by Gematsu](https://www.gematsu.com/2026/02/steam-machine-steam-frame-and-steam-controller-update-we-have-work-to-do-to-land-on-concrete-pricing-and-launch-dates) (Feb 4, 2026)
- [Valve GDC 2026 Steam Hardware Talk deck](https://steamcdn-a.akamaihd.net/steamcommunity/public/images/steamworks_docs/english/GDC_2026_HWTalk.pdf)
- [Forbes profile of Gabe Newell](https://www.forbes.com/profile/gabe-newell/)
- [Forbes magazine profile of Valve / Gabe Newell](https://www.forbes.com.au/covers/magazine/how-valve-founder-gabe-newell-turned-half-life-into-a-nearly-10-billion-fortune/)
- [Kalshi KXSTEAMPRICE-27 market](https://kalshi.com/markets/kxsteamprice/steam-machine/kxsteamprice-27) and public API snapshot (May 2026)
- [PC Gamer on Steam 2025 platform scale](https://www.pcgamer.com/gaming-industry/valve-says-over-5000-games-made-over-usd100k-on-steam-last-year/) (Mar 2026)
- [PCWorld on original Steam Machines](https://www.pcworld.com/article/401759/steam-machines-disappears-from-steams-hardware-tab-but-their-legacy-lives-on.html) (2018)

*Created 2026-05-19*
