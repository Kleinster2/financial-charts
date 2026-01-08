# Brazil Vault Merge Discussion

**Date:** 2026-01-08
**Status:** Pending decision

---

## Source vault

**Location:** `C:\Users\klein\Brazil News & Analysis`

**Structure (758 files):**

| Folder | Count | Notes |
|--------|-------|-------|
| People | 334 | Politicians, business leaders |
| Analysis | 123 | Research/analysis notes |
| Companies | 111 | Brazilian companies |
| Institutions | 68 | Government, orgs |
| Events | 52 | Historical/current events |
| States | 27 | Brazilian states |
| Culture | 21 | Cultural topics |
| Parties | 12 | Political parties |
| Concepts | 6 | Ideas/frameworks |
| Organizations | 2 | — |
| News | 1 | — |

---

## Options

### Option 1: Subfolder (Recommended)

Import as `investing/Brazil/` preserving internal structure.

```
investing/
├── Brazil/
│   ├── Analysis/
│   ├── Companies/
│   ├── People/
│   ├── States/
│   └── ...
├── Actors/
├── Sectors/
└── ...
```

**Pros:**
- Preserves Brazil vault organization
- Clean separation
- Brazil-specific folders (States, Parties, Culture) make sense

**Cons:**
- Two parallel structures
- Companies/People not in main Actors/

### Option 2: Full merge

Map Brazil folders into investing structure:
- Companies → Actors
- People → Actors
- Institutions → Actors
- Events → Events
- Concepts → Concepts
- Analysis → new Analysis/ folder

**Pros:**
- Unified vault
- Single source of truth

**Cons:**
- 445 new Actors would overwhelm existing 498
- Loses Brazil-specific organization
- States/Parties/Culture don't fit

### Option 3: Hybrid

- Merge Companies → Actors (with Brazil tag)
- Keep Brazil-specific content (States, Parties, People) in subfolder
- Link between vaults via [[wikilinks]]

**Pros:**
- Companies integrated
- Brazil context preserved

**Cons:**
- Most complex
- Unclear boundaries

---

## Recommendation

**Option 1 (Subfolder)** — The Brazil vault is substantial (758 files) and has Brazil-specific categories (States, Parties, Culture) that don't map cleanly to the investing vault structure.

Import as `investing/Brazil/` and link between vaults:
- [[Regions/LATAM]] can link to Brazil/ content
- [[Petrobras]] (in Actors) can link to Brazil/Companies/Petrobras if needed

---

## To execute

```bash
# Copy Brazil vault (excluding .git and .obsidian)
cp -r "/c/Users/klein/Brazil News & Analysis/"* investing/Brazil/
rm -rf investing/Brazil/.git investing/Brazil/.obsidian
```

---

## Related

- [[Regions/LATAM|LATAM]] — regional hub
- [[Petrobras]] — already in Actors
- [[B3]] — already in Actors

