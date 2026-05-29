---
aliases: [Glassworm, GlassWorm, Glassworm takedown, Glassworm botnet]
tags: [event, cybersecurity, software-supply-chain, 2026]
---

# Glassworm botnet takedown May 2026

On May 26 2026 at 14:00 UTC, [[CrowdStrike]], [[Google]], and the Shadowserver Foundation disrupted the Glassworm botnet by hitting all four of its command-and-control channels simultaneously. The campaign matters because it targeted developers as the supply-chain entry point, not consumers or ordinary endpoints.

---

## Synthesis

Glassworm is the developer-toolchain version of the security-control-point thesis. CrowdStrike described it as a self-propagating, credential-stealing worm active since at least early 2025, spreading through poisoned software packages and developer tooling. The Register reported that [[Koi]] first spotted the campaign in October 2025 and that Glassworm used invisible Unicode-based code injection, blockchain-based C2, and Google Calendar as a backup command channel.

The takedown was notable because the botnet was designed to survive ordinary infrastructure removals. Its C2 stack used [[Solana]] transaction memo fields, BitTorrent DHT, Google Calendar event titles, and traditional VPS infrastructure. Taking down one layer would have left the others available for reconstitution, so the operation had to hit all four channels at once.

For the investing vault, the read-through is that developer environments are now a high-value enterprise security perimeter. A compromised workstation or extension can expose source repositories, GitHub tokens, npm publishing credentials, SSH keys, cloud accounts, CI/CD pipelines, and package registries. That supports spend on endpoint telemetry, developer identity, secret management, code/package scanning, and supply-chain governance. It also reinforces the distinction between [[AI cybersecurity disruption basket]] names vulnerable to AI commoditizing detection and [[Security control points]] names that own mandatory telemetry, policy, or recovery surfaces.

---

## Mechanics

| Layer | Glassworm pattern | Why it mattered |
|-------|-------------------|-----------------|
| Developer tooling | Trojanized VS Code/OpenVSX extensions disguised as ordinary productivity tools | Extensions run inside trusted developer environments |
| Package ecosystems | Compromised npm and Python packages used install scripts and setup paths | Routine dependency installation became execution |
| Source repositories | More than 300 [[GitHub]] repositories were poisoned with stolen developer credentials | Repository trust distributed payloads downstream |
| Cross-platform reach | [[Windows]], macOS, and [[Linux]] systems were affected | Developer fleet heterogeneity did not contain the campaign |
| C2 resilience | Solana, BitTorrent DHT, Google Calendar, and VPS servers | Each channel backed up the others, forcing simultaneous disruption |

CrowdStrike said infected machines now beacon to the benign CrowdStrike-operated indicator `164.92.88[.]210`, which organizations can use in network logs and endpoint telemetry as a Glassworm infection signal.

---

## Market read-through

- [[CrowdStrike]] - validates endpoint telemetry and threat-intelligence role in live supply-chain disruption, not just post-breach response.
- [[Google]] - platform participant because abused Google Calendar infrastructure was part of the C2 path and because developer/security trust affects AI and cloud adoption.
- [[Software supply chain attacks]] - creates the durable concept home for developer-toolchain compromise cases.
- [[Cybersecurity]] - adds another data point to the 2026 shift from network perimeter risk toward developer and CI/CD control surfaces.
- [[Agentic AI security]] - adjacent because [[AI agents]], plugins, and skills inherit the same trust-by-default supply-chain problem.

---

## Sources

- CrowdStrike, ["Inside CrowdStrike's Takedown of a Developer-Targeting Botnet"](https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/), May 2026.
- Jessica Lyons, ["CrowdStrike, Google shatter Glassworm botnet"](https://www.theregister.com/cyber-crime/2026/05/27/crowdstrike-google-shatter-glassworm-botnet/5247337), *The Register*, May 27 2026.
- Lorenzo Franceschi-Bicchierai, ["CrowdStrike and Google take down botnet used by hackers to target open source software developers"](https://techcrunch.com/2026/05/27/crowdstrike-and-google-take-down-botnet-used-by-hackers-to-target-software-developers-in-supply-chain-attacks/), *TechCrunch*, May 27 2026.
