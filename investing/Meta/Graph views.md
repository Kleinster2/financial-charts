# Graph Views

Obsidian graph filters for exploring the vault.

---

## How to use

1. Open graph view (Ctrl/Cmd + G)
2. Click filter icon (top left)
3. Enter filter string
4. Adjust depth slider for local graphs

---

## By folder

| View | Filter |
|------|--------|
| All Actors | `path:Actors/` |
| All Concepts | `path:Concepts/` |
| All Theses | `path:Theses/` |
| Exclude daily notes | `-path:Daily/` |

---

## By thesis

| Thesis | Filter |
|--------|--------|
| Memory bet | `tag:#memory OR [[Long memory]]` |
| Nuclear/power | `tag:#nuclear OR tag:#power OR tag:#energy` |
| Korea vs Taiwan | `tag:#korea OR tag:#taiwan` |
| Broadcom/ASIC | `[[Broadcom]] OR tag:#asic` |
| WFE picks | `tag:#wfe` |

---

## By sector

| Sector | Filter |
|--------|--------|
| Semiconductors | `tag:#semiconductor OR tag:#foundry OR tag:#fabless` |
| AI infrastructure | `tag:#datacenter OR tag:#hyperscaler OR tag:#neocloud` |
| Power for AI | `tag:#nuclear OR tag:#power OR tag:#energy OR tag:#utility` |
| Submarine cables | `tag:#cable OR tag:#submarine` |
| Crypto pivot plays | `tag:#crypto` |
| Robotics/autonomous | `tag:#robotics OR tag:#autonomous` |

---

## By geography

| Region | Filter |
|--------|--------|
| USA | `tag:#usa` |
| China | `tag:#china` |
| Korea | `tag:#korea` |
| Japan | `tag:#japan` |
| GCC/Middle East | `tag:#gcc OR tag:#saudi OR tag:#uae` |
| LATAM | `tag:#brazil OR tag:#mexico OR tag:#chile` |
| Southeast Asia | `tag:#singapore OR tag:#indonesia OR tag:#vietnam` |

---

## By type

| Type | Filter |
|------|--------|
| Public companies | `tag:#public` |
| Private companies | `tag:#private` |
| Individuals | `tag:#individual OR tag:#founder OR tag:#talent` |
| Investors/VCs | `tag:#vc OR tag:#investor` |
| Sovereign players | `tag:#sovereign OR tag:#government` |

---

## Combining filters

Use AND (space) and OR:

```
tag:#semiconductor tag:#usa          → US semiconductor actors
tag:#nuclear OR tag:#fusion          → All nuclear plays
path:Actors/ tag:#china              → Chinese actors only
-tag:#private path:Actors/           → Public actors only
```

---

## Local graph tips

- Right-click any note tab → "Open local graph"
- Depth 1: Direct connections only
- Depth 2: Friends of friends (usually best)
- Depth 3+: Gets noisy fast

---

## Graph groups (coloring)

Settings → Graph → Groups:

| Group | Query | Color suggestion |
|-------|-------|------------------|
| Theses | `path:Theses/` | Gold |
| Actors | `path:Actors/` | Blue |
| Concepts | `path:Concepts/` | Green |
| Events | `path:Events/` | Red |
| Hubs (NVIDIA, TSMC) | `[[NVIDIA]] OR [[TSMC]]` | Orange |

---

## Recommended starter views

1. **Thesis exploration**: Open a thesis note → local graph depth 2
2. **Sector deep-dive**: Filter `tag:#nuclear` → see ecosystem
3. **Actor context**: Open actor → local graph → see what it connects to
4. **Gap finding**: Full graph → look for isolated clusters

---

## Related

- [[CLAUDE]] — Vault conventions
- [[Thesis conventions]] — How theses are structured
