---
name: The global AI data-center buildout
type: report
topic: "[[Data Centers]]"
lens: neutral
deepdive: false
generated: 2026-06-23 13:10
sources_read: 14
tags: [report]
---

# The global AI data-center buildout — one trade in name, four factors in fact, rationed by power

The cleanest thing to say about the AI data-center buildout is that there is no such thing as "the" AI data-center trade. The ~$725B of 2026 hyperscaler capex is a single number that the market reads at least four incompatible ways, and the correlation structure in [[Data Centers]] proves it: the whole "data center" label correlates at just 0.39, splitting into [[DC REITs]] (0.69 intra-cluster — the tightness of the names' co-movement) and [[Crypto-to-AI]] (0.61), which barely correlate with each other (0.08–0.20). Push one layer further and even the [[Neocloud financing|neoclouds]] (GPU-cloud operators renting accelerator capacity, many ex-bitcoin-miners) do not trade as one basket: since its April-2025 IPO [[CoreWeave]] tracks [[NVIDIA]] at roughly +90%, levered-Nvidia-beta, while [[IREN]] and [[Nebius]] run idiosyncratically to +700–1100%. The same $725B is bullish for the picks-and-shovels ([[Vertiv]], [[Schneider Electric]], and the power names), mixed for the wholesale REITs (every dollar a hyperscaler self-builds is a lease [[Digital Realty]] does not sign), and binary for the neoclouds whose levered, single-asset balance sheets only work if the hyperscaler shortfall persists. "Long data centers" is not a position; it is a category error.

What actually rations the buildout is neither capital nor chips — it is power. Capital stopped being the constraint when the [[Project Stargate]] joint venture, originally a financing innovation to fund a lossmaking lab with no credit rating, was quietly abandoned for bilateral deals as capital markets normalized around AI infrastructure; the IEA's 2025 marker that data-center spending ($580B) overtook new oil supply ($540B) is the same point from the macro side. Chips are abundant in the US. Power is not: Morgan Stanley puts the 2025–28 US shortfall at 44 GW (the output of ~44 nuclear plants), [[Ashburn]] interconnection queues (the wait to connect new load to the grid) run to seven years, and Dublin closed greater-Dublin grid connections until 2028 — exactly why `## Ireland (Dublin)` is the cautionary case and why [[India]]'s constraint shows up not as national capacity but as site-level delivery. That scarcity is why the answers are physical: nuclear restarts, [[Power constraints|BYOP]] (bring-your-own-power), and now the oil majors selling firm power at the wellhead — [[Chevron]]'s Project Kilby on stranded [[Permian Basin|Waha-Hub]] gas (the West Texas benchmark that often clears negative). The bottleneck, not the capex, sets the map.

The binding constraint flips by geography, and that is where the geopolitics vault sharpens the read. The entire non-China map now runs on the American stack: the Gulf is the flagship, where [[Stargate UAE]] (5 GW, [[G42]] 60% sovereign control) runs on US silicon only because G42 divested its Chinese tech to qualify — export promotion and export control meeting in one transaction ([Geopolitics: American AI Export Program](obsidian://open?vault=geopolitics&file=Concepts%2FAmerican%20AI%20Export%20Program); [Geopolitics: Digital Sovereignty](obsidian://open?vault=geopolitics&file=Concepts%2FDigital%20Sovereignty)). [[China]] is the counter-example that inverts every variable: under [[East Data West Compute]] it has abundant, state-directed power (212 GW of solar in one year) but is walled off from frontier accelerators, so it builds on domestic [[Inference Hardware|Ascend silicon]] ([Technologies: Chinese AI Stack](obsidian://open?vault=technologies&file=Chinese%20AI%20Stack)) and makes compute efficiency, not capacity, the national priority. The US has the best chips and can't power them; China has the power and can't get the chips; the Gulf is the synthesis — US silicon plus sovereign cheap power — which is precisely why Abu Dhabi and Dubai vaulted to the world's #1–2 emerging markets. Brazil, Mexico (Querétaro), Japan, and Johor are variations on the same two levers (cheap/clean power, proximity), none yet resolving the silicon-vs-power tension the way the Gulf does.

The one-line: the AI buildout is priced as one trade, financed three ways (US bilateral, Gulf sovereign-on-US-stack, China walled-off), and rationed by the one input that is neither abundant capital nor abundant chips — deliverable 24/7 power. The durable question for each layer is not "is AI demand real" but "whose scarce input can I underwrite" — power for the REITs and the gas/nuclear suppliers, Nvidia allocation for the neoclouds, and a sovereign chip-access bargain for everyone building outside the US and China.

## Other vault references

- [[Power constraints]] — the 44 GW gap, BYOP, the $1T-runs-on-gas valuation framing, the China power/chip inversion
- [[DC REITs]] / [[Crypto-to-AI]] — the two validated cohorts; the factor-split evidence (and PC2 splitting pure miners from AI-pivots)
- [[Project Stargate]] — the US flagship that dissolved from JV into bilateral deals; Abilene 1.2 GW
- [[Aligned Data Centers]] — the $40B BlackRock/GIP/MGX deal that puts Abu Dhabi capital on both sides of the global build
- [Geopolitics: American AI Export Program](obsidian://open?vault=geopolitics&file=Concepts%2FAmerican%20AI%20Export%20Program) — the US-stack-to-allies policy that the Gulf build is the flagship destination for
- [Technologies: Data Center Infrastructure](obsidian://open?vault=technologies&file=Data%20Center%20Infrastructure) / [Chinese AI Stack](obsidian://open?vault=technologies&file=Chinese%20AI%20Stack) — the chip/efficiency layer beneath the real estate

## Gaps

- Cold cross-check deferred: the mandatory WebSearch calibration pass was skipped — WebSearch was rate-limited at generation time (resets 11:30pm ET 2026-06-23). The synthesis rests on vault material that was largely web-verified earlier the same session, so staleness risk is low, but the report has not been stress-tested against an independent outside framing. Re-run after the reset to confirm no contrary consensus read.
- [[Stargate UAE]] is referenced across investing + geopolitics but has no dedicated note in either vault (it lives inside [[Project Stargate]] and [[American AI Export Program]]); a standalone note may be warranted if it recurs.
- No dedicated investing note for the US power-geography migration beyond [[Power-constrained geography]] / [[Ashburn]] — the Texas (Abilene/ERCOT) vs Northern Virginia shift is narrated across several notes but not hubbed.
