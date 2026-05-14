# Newsletter & Substack Sources

Sources scanned by `/substacks`. Each URL is the archive/homepage where the most recent posts are listed.

These are high-signal, low-noise voices — they publish analysis before or instead of mainstream outlets, so the daily news scan and the morning scan miss them.

## Sources

| Publication | URL | Vault(s) | Focus |
|-------------|-----|----------|-------|
| **Vizier Report** | https://vizier.report | Geopolitics | Middle East, Iran, strategic analysis |
| **Robin J. Brooks** | https://robinjbrooks.substack.com | Geopolitics, Investing | Macro, trade flows, energy markets, AIS shipping data |
| **Chips and Wafers** | https://chipsandwafers.substack.com | Investing | Semiconductor equipment, test ecosystem, packaging |
| **Ideas in Development** | https://ideasindevelopment.substack.com | Investing | Development economics, AI + emerging markets, VoxDev podcast |
| **Jason's Chips** | https://jasonschips.substack.com | Investing | Semiconductor technology primers, packaging, process nodes |
| **Jimi Finance** | https://jimifinance.substack.com | Investing | Taiwan/Asia semi analysis (Chinese), ASIC test, AI chip supply chain |
| **Sergey Vakulenko** | https://svakulenko.substack.com | Investing, Geopolitics | Russian oil/energy sector, upstream economics, OPEC+, sanctions impact (Carnegie) |
| **Zero to Pete** | https://www.zerotopete.com | Technologies, Business | AI tools, coding workflows, founder/operator lessons |
| **Robert Pape (Escalation Trap)** | https://escalationtrap.substack.com | Geopolitics | Airpower effectiveness, escalation dynamics, Iran war analysis, disruption-to-damage threshold |
| **HelloChinaTech** | https://hellochinatech.com | Investing, Technologies | China AI ecosystem, token economy, ByteDance/Alibaba/Tencent cloud strategy, MaaS |
| **Matt Sheehan / ChinaTalk** | https://mattsheehan.substack.com | Geopolitics, Investing | China AI policy, governance, CCP tech regulation, AI & jobs, US-China tech competition |
| **TechStock01** | https://techstock01.substack.com | Investing | Memory/semiconductor analysis, HBM, DRAM/NAND pricing, supply chain data, demand modeling |
| **Asia Tech Lens** | https://www.asiatechlens.com | Investing, Technologies | China/Asia AI deployment, platform strategy, enterprise adoption, subsidy economics |
| **Rush Doshi** | https://rdoshi.substack.com | Geopolitics, Investing | US-China industrial competition, tech policy, Little Giants, defense industrial base |
| **Recode China AI** | https://recodechinaai.substack.com | Investing, Technologies, Geopolitics | China AI industry, labor displacement, tech policy |
| **Gianluca Benigno** | https://gianlucabenigno.substack.com | Investing | Central bank policy, monetary economics, inflation, oil/geopolitics |
| **Chartbook (Adam Tooze)** | https://adamtooze.substack.com | Investing, Geopolitics, History | Macro history, geopolitics, financial crises |
| **Shanaka Anslem Perera** | https://shanakaanslemperera.substack.com | Investing | Macro, development economics, inference economics, structural fractures |
| **FT Alphaville** | https://ftav.substack.com | Investing | Markets, financial analysis, macro |
| **Alap Shah** | https://alapshah1.substack.com | Investing, Technologies | AI infrastructure, semiconductor strategy, intelligence economics |
| **Quiet Capital (Michael Bloch)** | https://michaelxbloch.substack.com | Investing, Technologies | AI investment themes, intelligence economics |
| **David Oks** | https://davidoks.blog | Investing, Geopolitics | Economic development, global poverty, tech & society, AI & labor (a16z research partner, ex-quant HF) |
| **Critical Supply** | https://substack.com/@criticalsupply | Investing, Geopolitics | Trade policy, supply chains, EU-US-China economic relations (Eduardo Castellet Nogués) |
| **Gridlocked and Unlocked** | https://gridlockedunlocked.substack.com | Investing | Power markets, grid modernization, data center electricity demand, energy transition (Tam Kemabonta) |
| **Carolyn Kissane (Energy Common Sense)** | https://carolynkissane157206.substack.com | Investing, Geopolitics | Energy geopolitics, oil/LNG markets, energy security (NYU) |
| **Alex Epstein** | https://alexepstein.substack.com | Investing | Energy policy, fossil fuels, energy security |
| **Aurelion Research** | https://aurelionresearch.substack.com | Investing | Independent equity research — small/mid-cap, shipping, offshore drilling, chemicals, fertilizers, oil |
| **Inverteum Capital** | https://blog.inverteum.com | Investing, Geopolitics | Long-short algorithmic trading (Hong Kong), geopolitics, China/Taiwan, market commentary |
| **Principled Perspectives (Ray Dalio)** | https://raydalio.substack.com | Investing, Geopolitics | Global macro, world order, debt cycles, AI (Bridgewater founder) |
| **China Uncensored** | https://chinauncensored.substack.com | Geopolitics | Chinese politics, economy, CCP analysis, Iran/Taiwan angles |
| **The More Things Change (Norman Ricklefs)** | https://normanricklefs.substack.com | Geopolitics, History | History, complex systems, military strategy, unintended consequences (NAMEA Group) |
| **ChinaTalk (Jordan Schneider)** | https://www.chinatalk.media | Geopolitics, Investing, Technologies | China tech, US policy, war, policymaker interviews (parent pub — distinct from Matt Sheehan's contributor Substack) |
| **Hey AI News (Veronica Hylak)** | https://heyainews.substack.com | Technologies | AI news explained for non-technical audiences — gen AI, robotics, LLMs |
| **War and Peace (Mark Urban)** | https://markurban.substack.com | Geopolitics | Defence, diplomacy, intelligence, counter-terrorism, military history |
| **ENERGY Pipeline (Felipe Germini)** | https://fgermini.substack.com | Investing, Geopolitics | Brazil energy, oil trading, gas markets (ex-Schlumberger Country MD) |
| **The Merchant's News (Giacomo Prandelli)** | https://themerchantsnews.substack.com | Investing, Geopolitics | Oil, gas, LNG, metals, geopolitics, commodity-linked stocks (12K+ subs) |
| **Jared Bernstein** | https://econjared.substack.com | Investing | US economic/fiscal policy, crypto regulation, budgeting (former Biden CEA Chair) |
| **The Register (Security)** | https://www.theregister.com/security/ | Investing, Technologies | Cybersecurity, AI infrastructure breaches, supply chain attacks |
| **BleepingComputer** | https://www.bleepingcomputer.com/news/ | Investing, Technologies | Data breaches, ransomware, vulnerability disclosures |

## Maintenance

This list is mirrored in the OpenClaw workspace at `~/clawd/TOOLS.md`. The two should stay byte-for-byte aligned on the table contents. When adding or removing a source, update both locations.

## How `/substacks` uses it

The skill reads this file as input, scans each archive/homepage for posts in the configured window (default 48 hours), cross-references against the vault, and presents candidates. See `.claude/skills/substacks/SKILL.md`.
