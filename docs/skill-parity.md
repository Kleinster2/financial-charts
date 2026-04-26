# Skill Parity

Shared investing-vault workflows live in three runtimes:

| Runtime | Path |
|---|---|
| Codex | `.agents/skills/` |
| Claude Code | `.claude/skills/` |
| OpenClaw | `C:\Users\klein\clawd\skills\` |

## Shared Workflow Set

These skills are expected to exist in all three runtimes:

- `news`
- `ingest`
- `earnings`
- `report`
- `deepdive`
- `newsletter`
- `story`
- `morning-scan`
- `replicate`

## Rules

- Codex and Claude Code skills should match byte-for-byte after newline normalization.
- OpenClaw skills may differ only when they are runtime-adapted ports listed in `scripts/check_skill_parity.py`.
- After editing a Claude workflow skill, run `python scripts/sync_codex_skills.py` to copy it into `.agents/skills/`.
- After editing any shared skill, run `python scripts/check_skill_parity.py --strict`.
- For the normal repo check, run `npm run test:consistency`. It checks OpenClaw when the OpenClaw skills directory exists; in CI-only checkouts without OpenClaw, it still enforces Codex/Claude parity.

## OpenClaw Path Override

If OpenClaw is checked out somewhere other than `C:\Users\klein\clawd`, set `OPENCLAW_SKILLS_DIR`:

```powershell
$env:OPENCLAW_SKILLS_DIR = "D:\path\to\clawd\skills"
npm run test:consistency
```

or pass the path explicitly:

```powershell
python scripts\check_skill_parity.py --strict --openclaw-skills D:\path\to\clawd\skills
```
