---
aliases: [Valve Steam Machine, Steam Machine 2026, Fremont]
tags: [product, gaming, hardware, pc, steamos]
parent_actor: "Valve"
---

# Steam Machine

#product #gaming #hardware #pc #steamos

Steam Machine is [[Valve]]'s living-room [[SteamOS]] PC, announced November 12, 2025 as part of the new Steam hardware family with [[Steam Controller]] and [[Steam Frame]]. The 2026 version is a Valve-built cube rather than the fragmented OEM program that launched in 2015.

---

## The story

Valve is trying to make a PC that behaves like a console without becoming a closed console.

The original Steam Machines failed because the software stack was not ready. [[Linux]] game compatibility was thin, OEM hardware varied widely, and the value proposition was muddied by [[Steam Link]], which let users stream from an existing PC for far less money. The new version is different because [[Steam Deck]] already proved the software stack: [[SteamOS]] as a console-like interface, [[Proton (Valve)|Proton]] as the compatibility layer, Steam Input as the control abstraction, and Valve-controlled hardware as the integration point.

The new Steam Machine is therefore not just a device. It is the living-room test of whether [[SteamOS]] can scale beyond handhelds. Valve's GDC 2026 developer deck says all Deck Verified games are Machine Verified, with performance expectations framed around 30 frames per second at 1080p for verification and hardware roughly six times Steam Deck performance. Valve's consumer pitch is higher: most Steam titles should run at 4K/60 with [[FidelityFX Super Resolution|FSR]] upscaling, though the February FAQ acknowledges some demanding games may need heavier upscaling or lower frame-rate/VRR targets to preserve internal resolution.

The economic question is price. Steam Machine is an open PC: users can install apps, peripherals, and even another operating system. That openness is the point, but it also weakens the closed-console subsidy model. If Valve prices it like an equivalent compact PC, the machine may appeal most to existing Steam users who want a couch box. If it comes close to console pricing despite memory/storage shortages, it becomes a more serious platform-expansion weapon.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Valve]] |
| Announced | November 12, 2025 |
| Planned release | 2026; final date not public as of May 2026 source check |
| Price | Not announced |
| Form factor | Roughly 6-inch cube |
| OS | [[SteamOS]] 3 |
| CPU | Semi-custom [[AMD]] Zen 4, 6 cores / 12 threads, up to 4.8GHz, 30W TDP |
| GPU | Semi-custom [[AMD]] RDNA3, 28 CUs, 8GB GDDR6 VRAM, 2.45GHz max sustained clock, 110W TDP |
| Memory | 16GB DDR5 plus 8GB GDDR6 VRAM |
| Storage | 512GB or 2TB NVMe SSD; microSD expansion |
| Connectivity | Wi-Fi 6E, Bluetooth 5.3, integrated 2.4GHz Steam Controller radio |
| Display outputs | DisplayPort 1.4 and HDMI 2.0 |
| Power | Internal power supply |
| Claimed performance | Over 6x [[Steam Deck]]; 4K/60 target with [[FidelityFX Super Resolution|FSR]] |

---

## Specifications

| Category | Detail |
|----------|--------|
| CPU | Semi-custom [[AMD]] Zen 4 6C/12T, up to 4.8GHz, 30W TDP |
| GPU | Semi-custom [[AMD]] RDNA3 28CU, 8GB GDDR6, 2.45GHz max sustained clock, 110W TDP |
| RAM | 16GB DDR5 SODIMM |
| Storage | 512GB or 2TB NVMe; supports M.2 2230 and 2280 replacement per Valve FAQ/reporting |
| External storage | High-speed microSD |
| Ports | DisplayPort 1.4, HDMI 2.0, gigabit Ethernet, USB-C 3.2 Gen 2, two front USB-A 3.2 Gen 1, two rear USB-A 2.0 |
| Size | 152mm tall, 162.4mm deep, 156mm wide |
| Weight | 2.6kg |
| Controller link | Integrated [[Steam Controller]] wireless adapter supports up to four controllers |

---

## Market discovery timeline

| Date | Event | Market reaction |
|------|-------|-----------------|
| 2013-2015 | Valve launches first Steam Machine initiative through OEM partners | Strategic flop: fragmented hardware, immature Linux compatibility, low consumer traction |
| 2018 | Steam Machines disappear from Steam hardware tab | Confirms the original living-room PC push had effectively faded |
| Feb 25, 2022 | [[Steam Deck]] launches | [[SteamOS]] becomes a real consumer hardware platform rather than a living-room experiment |
| Nov 12, 2025 | Valve announces new [[Steam Machine]], [[Steam Controller]], and [[Steam Frame]] | No public ticker reaction because Valve is private; AMD supplier read-through is small relative to AI/data-center business |
| Nov 2025 | Hands-on coverage confirms Zen 4/RDNA3 specs and 512GB/2TB models | Early press frames it as more coherent than 2015 but price-sensitive |
| Feb 4, 2026 | Valve says memory/storage shortages require revisiting exact schedule and pricing | Launch-window confidence weakens; pricing risk rises |
| Mar 2026 | Valve GDC deck says all Deck Verified games are Machine Verified | Developer burden appears low; verification system becomes the trust bridge |
| May 4, 2026 | [[Steam Controller]] ships first at $99 | Controller demand validates interest in couch/Steam input layer, but Steam Machine price/date still pending |

---

## Strategic read

Steam Machine sits between three markets:

| Comparison | Where Steam Machine wins | Where it is exposed |
|------------|--------------------------|---------------------|
| Console | Full Steam library, no online-subscription gate, PC openness | Likely higher price if not subsidized |
| DIY gaming PC | Integrated SteamOS couch experience, compact/quiet design | Less upgradeable than a standard desktop |
| Docked [[Steam Deck]] | Much higher performance and living-room thermal headroom | No handheld screen; separate purchase |

The best case is that Steam Machine becomes the default recommendation for people who want a gaming PC in the living room but do not want to administer Windows. The narrower case is that it remains an enthusiast SteamOS box and still helps Valve by hardening the SteamOS ecosystem for third-party devices.

---

## Pricing market

[[Kalshi]]'s KXSTEAMPRICE-27 contract ladder is a useful real-time [[Prediction markets|prediction-market]] read on the unresolved launch-price question. The contracts resolve based on the first price announced by [[Valve]] for the new Steam Machine. As of the May 2026 API read, the market was not pricing a console-subsidized box; it was centered closer to a compact gaming PC.

| Contract threshold | Last price | Bid / ask | Read |
|--------------------|------------|-----------|------|
| At least $400 | 99c | 97c / 100c | Effectively assumed |
| At least $500 | 96c | 93c / 96c | Effectively assumed |
| At least $600 | 92c | 90c / 92c | High confidence |
| At least $700 | 78c | 74c / 80c | Likely |
| At least $800 | 62c | 51c / 61c | Near the market's center |
| At least $900 | 27c | 28c / 33c | Material tail, not base case |
| At least $1,000 | 12c | 5c / 11c | Low-probability tail |
| At least $1,100 | 1c | 0c / 5c | Remote |
| At least $1,200 | 1c | 0c / 6c | Remote |

The crude implied band from the last-price ladder is $800-$899: the market gives a majority probability to at least $800 but not to at least $900. That matters strategically because a sub-$600 price would read like a console attack, while an $800-ish price reads more like a living-room PC for committed Steam users.

---

## Compatibility and verification

Valve's GDC 2026 deck makes the verification logic explicit:

| Rule | Implication |
|------|-------------|
| All Deck Verified games are Machine Verified | Existing Steam Deck verification work carries over |
| Same input expectations as Deck | [[Steam Controller]] and Steam Input become the baseline |
| 30FPS at 1080p for Verified | Verification standard is lower than the marketing 4K/60 target |
| Not testing display resolution or legibility | Living-room display differences are treated as less binding than handheld legibility |
| Updated API to detect hardware | Developers can set defaults for Steam Machine directly |

The main compatibility gap is not ordinary Steam games; it is Windows-centric multiplayer titles with anti-cheat or secure-boot assumptions that still resist [[SteamOS]].

---

## What to watch

- Final price - the whole category changes if Valve gets close to console pricing; it stays niche if it lands near premium mini-PC pricing.
- Storage/RAM bill - Valve identified these as the schedule and pricing constraint in February 2026.
- 8GB VRAM ceiling - modern AAA games at high settings may pressure the 4K/60-with-upscaling promise.
- HDMI VRR and upscaling work - Valve said it is working on HDMI VRR, improved upscaling, and ray-tracing driver performance.
- Deck Verified carryover - if users trust Machine Verified, the device avoids the original Steam Machine compatibility confusion.
- Third-party SteamOS adoption - Steam Machine can be a reference design even if other OEM SteamOS PCs do the volume.

---

## Related

- [[Valve]] - parent company and platform owner
- [[Steam platform]] - storefront/library layer
- [[SteamOS]] - operating system
- [[Proton (Valve)|Proton]] - game compatibility layer
- [[Steam Deck]] - handheld proof point
- [[Steam Controller]] - input layer
- [[Steam Frame]] - sibling VR/non-VR headset
- [[Steam Link]] - earlier living-room streaming approach
- [[AMD]] - CPU/GPU supplier
- [[FidelityFX Super Resolution]] - upscaling technology used in the 4K/60 target
- [[Gaming Hardware]] - sector context
- [[Gaming]] - platform-holder context

---

## Sources

- [Valve / Steam hardware announcement mirrored by Gematsu](https://www.gematsu.com/2025/11/valve-announces-steam-machine-steam-frame-and-steam-controller) (Nov 12, 2025)
- [Valve timing and FAQ update mirrored by Gematsu](https://www.gematsu.com/2026/02/steam-machine-steam-frame-and-steam-controller-update-we-have-work-to-do-to-land-on-concrete-pricing-and-launch-dates) (Feb 4, 2026)
- [Valve GDC 2026 Steam Hardware Talk deck](https://steamcdn-a.akamaihd.net/steamcommunity/public/images/steamworks_docs/english/GDC_2026_HWTalk.pdf)
- [Tom's Hardware hands-on/specs](https://www.tomshardware.com/video-games/console-gaming/valve-brings-back-steam-machine-and-steam-controller-hands-on-with-valves-new-amd-based-living-room-gaming-hardware) (Nov 12, 2025)
- [PC Gamer hands-on/performance discussion](https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-specs-availability/) (Nov 12, 2025)
- [Kalshi KXSTEAMPRICE-27 market](https://kalshi.com/markets/kxsteamprice/steam-machine/kxsteamprice-27) and public API snapshot (May 2026)

*Created 2026-05-19*
