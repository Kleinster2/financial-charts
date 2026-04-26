#!/usr/bin/env python3
"""Shared helpers for repo workflow skill manifests."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_WORKFLOW_MANIFEST = REPO_ROOT / "skills" / "shared-workflows.json"


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
