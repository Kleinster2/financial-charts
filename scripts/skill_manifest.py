#!/usr/bin/env python3
"""Shared helpers for repo workflow skill manifests."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_WORKFLOW_MANIFEST = REPO_ROOT / "skills" / "shared-workflows.json"
SKILL_PARITY_SCOPES_MANIFEST = REPO_ROOT / "skills" / "skill-parity-scopes.json"
DEFAULT_OPENCLAW_SKILLS_DIR = Path(
    os.environ.get("OPENCLAW_SKILLS_DIR", r"C:\Users\klein\clawd\skills")
)


@dataclass(frozen=True)
class SkillParityScope:
    name: str
    description: str
    root: Path
    skills: list[str]
    runtimes: dict[str, Path]
    optional: bool = False


def read_manifest_list(key: str) -> list[str]:
    """Read an ordered skill list from the shared workflow manifest."""
    with SHARED_WORKFLOW_MANIFEST.open(encoding="utf-8") as handle:
        manifest = json.load(handle)

    values = manifest.get(key)
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"{SHARED_WORKFLOW_MANIFEST} must contain a string list at {key!r}")

    seen = set()
    duplicates = []
    for item in values:
        if item in seen:
            duplicates.append(item)
        seen.add(item)
    if duplicates:
        names = ", ".join(sorted(set(duplicates)))
        raise ValueError(f"{SHARED_WORKFLOW_MANIFEST} has duplicate entries at {key!r}: {names}")

    return values


def _read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _dedupe_strings(values: Any, source: str) -> list[str]:
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"{source} must be a string list")

    seen: set[str] = set()
    duplicates: list[str] = []
    deduped: list[str] = []
    for item in values:
        if item in seen:
            duplicates.append(item)
            continue
        seen.add(item)
        deduped.append(item)

    if duplicates:
        names = ", ".join(sorted(set(duplicates)))
        raise ValueError(f"{source} has duplicate entries: {names}")

    return deduped


def _resolve_path(value: str, base: Path) -> Path:
    if value == "$OPENCLAW_SKILLS_DIR":
        return DEFAULT_OPENCLAW_SKILLS_DIR

    expanded = os.path.expandvars(value)
    path = Path(expanded)
    if not path.is_absolute():
        path = base / path
    return path


def _read_scope_skills(scope_data: dict[str, Any], source: str) -> list[str]:
    if "skills" in scope_data:
        return _dedupe_strings(scope_data["skills"], f"{source}.skills")

    skills_from = scope_data.get("skillsFrom")
    if not isinstance(skills_from, dict):
        raise ValueError(f"{source} must contain either skills or skillsFrom")

    manifest_value = skills_from.get("path")
    key = skills_from.get("key")
    if not isinstance(manifest_value, str) or not isinstance(key, str):
        raise ValueError(f"{source}.skillsFrom must contain string path and key")

    manifest_path = _resolve_path(manifest_value, REPO_ROOT)
    with manifest_path.open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise ValueError(f"{manifest_path} must contain a JSON object")
    return _dedupe_strings(manifest.get(key), f"{manifest_path}.{key}")


def read_skill_parity_scopes() -> tuple[str, list[SkillParityScope]]:
    """Read registered skill parity scopes."""
    manifest = _read_json(SKILL_PARITY_SCOPES_MANIFEST)
    default_scope = manifest.get("defaultScope")
    scopes_data = manifest.get("scopes")
    if not isinstance(default_scope, str):
        raise ValueError(f"{SKILL_PARITY_SCOPES_MANIFEST} must contain defaultScope")
    if not isinstance(scopes_data, list):
        raise ValueError(f"{SKILL_PARITY_SCOPES_MANIFEST} must contain a scopes list")

    scopes: list[SkillParityScope] = []
    seen: set[str] = set()
    for index, scope_data in enumerate(scopes_data):
        source = f"{SKILL_PARITY_SCOPES_MANIFEST}.scopes[{index}]"
        if not isinstance(scope_data, dict):
            raise ValueError(f"{source} must be a JSON object")

        name = scope_data.get("name")
        description = scope_data.get("description", "")
        root_value = scope_data.get("root")
        runtimes_data = scope_data.get("runtimes")
        optional = scope_data.get("optional", False)

        if not isinstance(name, str) or not name:
            raise ValueError(f"{source}.name must be a non-empty string")
        if name in seen:
            raise ValueError(f"{SKILL_PARITY_SCOPES_MANIFEST} has duplicate scope: {name}")
        seen.add(name)
        if not isinstance(description, str):
            raise ValueError(f"{source}.description must be a string")
        if not isinstance(root_value, str):
            raise ValueError(f"{source}.root must be a string")
        if not isinstance(runtimes_data, dict):
            raise ValueError(f"{source}.runtimes must be an object")
        if not isinstance(optional, bool):
            raise ValueError(f"{source}.optional must be a boolean when present")

        root = _resolve_path(root_value, REPO_ROOT)
        runtimes: dict[str, Path] = {}
        for runtime, path_value in runtimes_data.items():
            if not isinstance(runtime, str) or not isinstance(path_value, str):
                raise ValueError(f"{source}.runtimes keys and values must be strings")
            runtimes[runtime] = _resolve_path(path_value, root)

        scopes.append(
            SkillParityScope(
                name=name,
                description=description,
                root=root,
                skills=_read_scope_skills(scope_data, source),
                runtimes=runtimes,
                optional=optional,
            )
        )

    if default_scope not in seen:
        raise ValueError(f"defaultScope {default_scope!r} is not registered")

    return default_scope, scopes


def get_skill_parity_scope(name: str) -> SkillParityScope:
    _, scopes = read_skill_parity_scopes()
    for scope in scopes:
        if scope.name == name:
            return scope
    names = ", ".join(scope.name for scope in scopes)
    raise ValueError(f"Unknown skill parity scope {name!r}. Registered scopes: {names}")
