# Skill Parity

Shared investing-vault workflows live in three runtimes:

| Runtime | Path |
|---|---|
| Codex | `.agents/skills/` |
| Claude Code | `.claude/skills/` |
| OpenClaw | `C:\Users\klein\clawd\skills\` |

## Shared Workflow Set

The source of truth is [skills/shared-workflows.json](../skills/shared-workflows.json).

- `workflowSkills` lists skills expected to exist in all three runtimes.

## Rules

- Codex, Claude Code, and OpenClaw skills should match byte-for-byte after newline normalization.
- Runtime setup belongs outside the skill body. OpenClaw should set the working directory to `C:\Users\klein\financial-charts` and load project instructions through runtime configuration, not by forking workflow text.
- OpenClaw skills should not carry runtime-specific forks, alternate wording, or behavior changes.
- After editing any shared skill, promote the intended source into every runtime:
  ```powershell
  python scripts\promote_shared_skill.py story --from newest
  ```
- If the intended source is explicit, avoid mtime guessing:
  ```powershell
  python scripts\promote_shared_skill.py story --from openclaw
  python scripts\promote_shared_skill.py story --from claude
  ```
- Then run `python scripts/check_skill_parity.py --strict`.
- When adding or removing a shared workflow, update `skills/shared-workflows.json` first.
- For the normal repo check, run `npm run test:consistency`. It checks OpenClaw when the OpenClaw skills directory exists; in CI-only checkouts without OpenClaw, it still enforces Codex/Claude parity.

## Local Hook Setup

The repo tracks `.githooks/pre-commit` because it enforces project rules: skill parity and daily-note logging for staged investing notes. Enable it in a checkout with:

```powershell
git config core.hooksPath .githooks
```

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
