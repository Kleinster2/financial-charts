---
aliases: [Query Markup Documents, qmd search]
tags: [actor, tools, ai, search, local]
---

#actor #tools #ai #search

**QMD** — Local semantic search engine for markdown docs, notes, and knowledge bases. Built by Tobi Lütke ([[Shopify]] CEO). Combines BM25 keyword search, vector semantic search, and LLM re-ranking — all running locally via GGUF models. Exposes an MCP server for direct integration with [[Claude Code]], Codex, and other AI coding agents.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Creator | Tobi Lütke ([[Shopify]] CEO) |
| Repo | github.com/tobi/qmd |
| Runtime | Node.js / Bun |
| Models | All local (GGUF via node-llama-cpp) |
| License | Open source |
| MCP | Yes (stdio + HTTP transport) |

---

## How it works

QMD indexes markdown files into a local SQLite database with both full-text (FTS5/BM25) and vector (embedding) indexes. Three search modes:

| Mode | Command | Speed | Quality |
|------|---------|-------|---------|
| **Keyword** | `qmd search` | Fast | Exact matches |
| **Semantic** | `qmd vsearch` | Medium | Conceptual similarity |
| **Hybrid** | `qmd query` | Slower | Best — RRF fusion + LLM reranking |

### Hybrid pipeline

1. **Query expansion** — LLM generates 2 alternative phrasings (original gets 2x weight)
2. **Parallel retrieval** — each query searches both BM25 and vector indexes (6 result lists)
3. **RRF fusion** — Reciprocal Rank Fusion combines all lists; top-rank bonus preserves exact matches
4. **LLM re-ranking** — Qwen3-reranker scores top 30 candidates (yes/no + logprobs)
5. **Position-aware blending** — top 1-3 results: 75% retrieval / 25% reranker; deeper results trust reranker more

### Local models

| Model | Purpose |
|-------|---------|
| embeddinggemma | Embeddings |
| Qwen3 | Query expansion |
| qwen3-reranker | Re-ranking |

Chunking: 900 tokens per chunk, 15% overlap, prefers markdown headings as boundaries.

---

## Key feature: context tree

Collections can have contextual descriptions that get returned with matching sub-documents. This helps LLMs make better choices about which documents are relevant — essentially a lightweight knowledge graph on top of flat files.

```
qmd context add qmd://notes "Personal notes and ideas"
qmd context add qmd://meetings "Meeting transcripts and notes"
```

---

## Ghost integration

**Ghost** (github.com/notkurt/ghost) is a companion tool that auto-captures Claude Code sessions and indexes them into QMD:

1. **Hooks** fire on prompt submit, file write, and turn completion (each <100ms)
2. Captures everything as markdown: prompts, file changes, timestamps
3. On session end: summarizes via Claude, extracts decisions + mistakes into ledgers, attaches git notes to HEAD
4. Indexes into QMD for semantic search
5. On next session: auto-injects relevant context from past sessions (warm resume)

**Key files (stored in `.ai-sessions/`):**
- `mistakes.md` — auto-extracted mistake ledger
- `decisions.md` — decision log with context
- `knowledge.md` — auto-generated project knowledge base
- `tags.json` — tag-to-session index

The combination creates **persistent agent memory across sessions** — the agent literally learns from its own past mistakes.

---

## Relevance

| Use case | Fit |
|----------|-----|
| Indexing large Obsidian vaults for semantic search | Strong |
| AI agent session memory / warm resume | Strong (with Ghost) |
| Replacing manual MEMORY.md / daily note review | Moderate — automates what's currently manual |
| Small note collections (<100 files) | Overkill — keyword search sufficient |

**vs OpenClaw's memory_search:** QMD's hybrid pipeline (BM25 + vector + reranker) is more sophisticated than simple semantic search, but requires local GGUF models and more setup. Best suited for large, unstructured collections where keyword search breaks down.

---

## Related

- [[Shopify]] — Tobi Lütke's company
- [[Claude Code]] — primary integration target (MCP + hooks)
- [[OpenClaw]] — alternative agent platform (has built-in memory_search)
- [[Obsidian]] — natural fit for vault indexing

*Created 2026-03-05.*
