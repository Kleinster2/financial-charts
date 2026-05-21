# Global Skill Parity

Neutral runner for repo-scoped agent skill parity. Repos keep their own scope manifests; this global registry points to those manifests and checks or promotes every registered scope from one command.

## Source And Install

The tracked source lives in `C:\Users\klein\financial-charts\agent-tools\skill-parity`.
The installed runtime copy lives in `C:\Users\klein\.agents\skill-parity`.

After editing the tracked source, install it with:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\klein\financial-charts\agent-tools\skill-parity\install.ps1
```

## Commands

```powershell
C:\Users\klein\.agents\skill-parity\skill-parity.cmd check --all-scopes --strict --optional-openclaw
```

Promote a repo-scoped skill family from Claude into Codex and OpenClaw mirrors:

```powershell
C:\Users\klein\.agents\skill-parity\skill-parity.cmd promote --scope personal-vault --from claude
```

Dry-run first when changing a broad scope:

```powershell
C:\Users\klein\.agents\skill-parity\skill-parity.cmd promote --scope personal-vault --from claude --dry-run
```

## Registry

`registry.json` lists scope manifests. Scope manifests can live in any repo; each manifest defines:

- scope name and root
- runtime skill directories for Claude, Codex, and OpenClaw
- expected skills, either inline or via another manifest such as `skills/shared-workflows.json`

The global runner checks behavior parity. It does not flatten repo-local skills into one global skill set.
