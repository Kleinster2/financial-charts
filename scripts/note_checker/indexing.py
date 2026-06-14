"""Index + per-file alias cache for NoteChecker (mixin).

Extracted from check_note_compliance.py. Builds existing_notes / known_aliases /
cross_vault_index, with a per-file (mtime, size) alias cache so only changed
files are re-read.
"""
import json
import re
from pathlib import Path


class IndexMixin:
    # Cross-vault directories to check for matching notes
    CROSS_VAULTS = {
        "geopolitics": Path("C:/Users/klein/obsidian/geopolitics"),
        "technologies": Path("C:/Users/klein/obsidian/technologies"),
        "history": Path("C:/Users/klein/obsidian/history"),
    }

    def _index_existing_notes(self) -> set[str]:
        """Index all existing note names (without .md extension)."""
        notes = set()
        for md_file in self.vault_root.rglob("*.md"):
            # Skip Daily notes, Meta folder, and disposable Reports
            if "/Daily/" in str(md_file) or "\\Daily\\" in str(md_file):
                continue
            if "/Meta/" in str(md_file) or "\\Meta\\" in str(md_file):
                continue
            if "/Reports/" in str(md_file) or "\\Reports\\" in str(md_file):
                continue
            notes.add(md_file.stem)
        return notes

    # --- Per-file alias index cache -------------------------------------------
    # Alias indexing reads file content (vault headers + full cross-vault notes),
    # which dominates NoteChecker() startup. The cache memoizes parsed aliases
    # per file, keyed by (mtime_ns, size), so only changed files are re-read.
    # existing_notes above is rglob-only (no reads) and stays uncached.
    INDEX_CACHE_VERSION = 1

    @staticmethod
    def _parse_frontmatter_aliases(text: str) -> list[str]:
        """Extract aliases from a note's leading YAML frontmatter (inline or block)."""
        out: list[str] = []
        if not text.startswith("---"):
            return out
        end = text.find("---", 3)
        if end == -1:
            return out
        fm = text[3:end]
        inline = re.search(r'^aliases:\s*\[([^\]]*)\]', fm, re.MULTILINE)
        if inline:
            for a in inline.group(1).split(","):
                a = a.strip().strip('"').strip("'")
                if a:
                    out.append(a)
            return out
        block = re.search(r'^aliases:\s*\n((?:\s+-\s+.+\n?)+)', fm, re.MULTILINE)
        if block:
            for a in re.findall(r'^\s+-\s+(.+?)$', block.group(1), re.MULTILINE):
                a = a.strip().strip('"').strip("'")
                if a:
                    out.append(a)
        return out

    def _index_cache_path(self) -> Path:
        """Sidecar cache path, keyed to the vault root's parent so temporary test
        vaults write into their own tempdir and never touch the real cache."""
        return self.vault_root.parent / ".note_index_cache.json"

    def _scope_signature(self) -> list[str]:
        """Roots the cache depends on; if this set changes the cache is rebuilt."""
        sig = [str(self.vault_root)]
        for name, path in self.CROSS_VAULTS.items():
            if path.exists():
                sig.append(f"{name}:{path}")
        return sorted(sig)

    def _load_index_cache(self) -> dict:
        """Load the per-file alias cache, or {} on miss / format change / disabled."""
        if not self._use_index_cache:
            return {}
        try:
            raw = json.loads(self._index_cache_path().read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}
        if raw.get("version") != self.INDEX_CACHE_VERSION:
            return {}
        if raw.get("scopes") != self._scope_signature():
            return {}
        return raw.get("files", {})

    def _save_index_cache(self, new_cache: dict) -> None:
        """Atomically persist the rebuilt per-file alias cache."""
        if not self._use_index_cache:
            return
        payload = {
            "version": self.INDEX_CACHE_VERSION,
            "scopes": self._scope_signature(),
            "files": new_cache,
        }
        try:
            path = self._index_cache_path()
            tmp = path.with_name(path.name + ".tmp")
            tmp.write_text(json.dumps(payload), encoding="utf-8")
            tmp.replace(path)  # atomic; tolerant of concurrent sessions
        except OSError:
            pass

    def _file_aliases(self, md_file: Path, cache: dict, scope: str, header_only: bool) -> list[str]:
        """Frontmatter aliases for a file, reusing the cache when (mtime, size) match.

        Reads the file only on a cache miss — the expensive part of indexing. The
        kept/rebuilt entry is recorded in self._new_index_cache for persistence.
        """
        key = str(md_file)
        try:
            st = md_file.stat()
        except OSError:
            return []
        hit = cache.get(key)
        if (hit and hit.get("mtime_ns") == st.st_mtime_ns
                and hit.get("size") == st.st_size and hit.get("scope") == scope):
            self._new_index_cache[key] = hit
            return hit["aliases"]
        try:
            if header_only:
                with open(md_file, "r", encoding="utf-8") as f:
                    text = f.read(2048)
            else:
                text = md_file.read_text(encoding="utf-8", errors="ignore")
        except (OSError, UnicodeDecodeError):
            return []
        aliases = self._parse_frontmatter_aliases(text)
        self._new_index_cache[key] = {
            "mtime_ns": st.st_mtime_ns, "size": st.st_size,
            "scope": scope, "aliases": aliases,
        }
        return aliases

    def _index_aliases(self, cache: dict) -> set[str]:
        """Index frontmatter aliases across the vault so [[Alias]] links resolve.

        Without this, links like [[NVIDIA]] (alias of Nvidia.md) are flagged
        dead even though Obsidian resolves them. Alias parsing is cached per file
        (see _file_aliases); only changed files are re-read from disk.
        """
        aliases = set()
        for md_file in self.vault_root.rglob("*.md"):
            path_str = str(md_file)
            if any(seg in path_str for seg in (
                "/Daily/", "\\Daily\\", "/Meta/", "\\Meta\\", "/Reports/", "\\Reports\\",
            )):
                continue
            for a in self._file_aliases(md_file, cache, scope="investing", header_only=True):
                aliases.add(a)
        return aliases

    def _index_cross_vaults(self, cache: dict) -> dict[str, list[tuple[str, str, str]]]:
        """Index notes in cross-vaults by name and aliases.

        Returns dict mapping lowercased name/alias -> list of (vault_name, note_stem, relative_path).
        Only indexes vaults that exist on disk. Alias parsing is cached per file
        (see _file_aliases); only changed files are re-read from disk.
        """
        index: dict[str, list[tuple[str, str, str]]] = {}

        for vault_name, vault_path in self.CROSS_VAULTS.items():
            if not vault_path.exists():
                continue
            for md_file in vault_path.rglob("*.md"):
                # Skip changelog, daily, templates, meta
                rel = str(md_file.relative_to(vault_path))
                skip_dirs = ("Daily", "Meta", "Templates", "templates", ".obsidian")
                if any(rel.startswith(d) for d in skip_dirs):
                    continue
                if md_file.stem.startswith("."):
                    continue

                stem = md_file.stem
                rel_path = rel.replace("\\", "/").replace(".md", "")

                # Index by filename
                index.setdefault(stem.lower(), []).append((vault_name, stem, rel_path))

                # Index by aliases from frontmatter (cached, full read on miss)
                for alias in self._file_aliases(md_file, cache, scope=vault_name, header_only=False):
                    index.setdefault(alias.lower(), []).append((vault_name, stem, rel_path))

        return index

