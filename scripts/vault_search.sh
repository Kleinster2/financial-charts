#!/usr/bin/env bash
# Ripgrep fallback for `Obsidian.com search query=`.
# Usage: vault_search.sh <vault> <query>
#
# Emits one .md path per matching file (relative to repo root for investing,
# absolute for sibling vaults). Mirrors the case-insensitive list-of-files
# semantics of the Obsidian CLI search command.
#
# Reason for fallback: Obsidian's search index is built lazily per vault when
# the search pane is opened in the GUI. Per Decision 6 (Quartz migration plan),
# investing is no longer opened in Obsidian, so its search index never primes
# and the CLI silently returns empty results. ripgrep is vault-state-independent.
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <vault> <query>" >&2
  echo "Vaults: investing, geopolitics, brazil, history, technologies, art, risk-parity" >&2
  exit 2
fi

vault="$1"
query="$2"

case "$vault" in
  investing)    root="$HOME/financial-charts/investing" ;;
  geopolitics)  root="$HOME/obsidian/geopolitics" ;;
  brazil)       root="$HOME/obsidian/brazil" ;;
  history)      root="$HOME/obsidian/history" ;;
  technologies) root="$HOME/obsidian/technologies" ;;
  art)          root="$HOME/obsidian/art" ;;
  risk-parity)  root="$HOME/obsidian/risk-parity" ;;
  *) echo "unknown vault: $vault" >&2; exit 1 ;;
esac

if [[ ! -d "$root" ]]; then
  echo "vault root not found: $root" >&2
  exit 1
fi

grep -rilZ --include="*.md" -- "$query" "$root" | tr '\0' '\n'
