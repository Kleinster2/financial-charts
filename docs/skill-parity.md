# Skill Parity

Shared workflow skills live in three runtimes:

| Runtime | Path |
|---|---|
| Codex | scope-relative `.agents/skills/` |
| Claude Code | scope-relative `.claude/skills/` |
| OpenClaw | `C:\Users\klein\clawd\skills\` |

## Registered Scopes

The source of truth for parity scope registration is [skills/skill-parity-scopes.json](../skills/skill-parity-scopes.json).

- `financial-charts` uses [skills/shared-workflows.json](../skills/shared-workflows.json) for the investing/cross-vault workflow set.
- `personal-vault` tracks repo-local communications workflows in `C:\Users\klein\obsidian\personal`.
- Optional external scopes are skipped when their root checkout is absent, so CI-only checkouts do not fail on local vault paths.

## Global Runner

The global orchestration entrypoint is:

```powershell
C:\Users\klein\.agents\skill-parity\skill-parity.cmd check --all-scopes --strict --optional-openclaw
```

Its registry lives at `C:\Users\klein\.agents\skill-parity\registry.json` and points to scope manifests such as this repo's `skills/skill-parity-scopes.json`. Keep repo-owned skill lists in their repo manifests; the global runner only discovers and executes registered scopes.

The tracked source for that installed runner lives at `agent-tools/skill-parity/`. After changing it, run:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\klein\financial-charts\agent-tools\skill-parity\install.ps1
```

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
- For a repo-scoped skill, select that scope:
  ```powershell
  python scripts\promote_shared_skill.py --scope personal-vault comms-sweep --from claude
  python scripts\check_skill_parity.py --scope personal-vault --strict
  ```
- Then run `python scripts/check_skill_parity.py --all-scopes --strict`.
- When adding or removing a financial-charts workflow, update `skills/shared-workflows.json` first.
- When adding a new parity group or repo-local skill family, update `skills/skill-parity-scopes.json`.
- For the normal repo check, run `npm run test:consistency`. It checks OpenClaw when the OpenClaw skills directory exists; in CI-only checkouts without OpenClaw, it still enforces Codex/Claude parity. The same command also runs focused note-compliance regressions and the live `--market-reaction-peer-sweep`.

## Local Hook Setup

The repo tracks `.githooks/pre-commit` because it enforces project rules: consistency-sensitive edits run `npm run test:consistency`, and staged investing-note edits must satisfy the daily-note log gate. Enable it in a checkout with:

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
