# Model Context Protocol

Open standard for connecting AI models to external tools, data sources, and applications. Often described as "USB-C for AI" — a universal connector layer for agentic systems.

## Overview

Introduced by [[Anthropic]] in November 2024. Donated to [[Linux Foundation]] in December 2025 under the new Agentic AI Foundation (AAIF).

**Core primitives:**
- **Resources** — data sources AI can access
- **Tools** — actions AI can perform
- **Prompts** — structured interaction patterns

Architecture inspired by Language Server Protocol (LSP), which standardized code editor support across programming languages.

## Agentic AI Foundation

Formed Dec 2025 under Linux Foundation. Founding projects:

| Project | Owner | Purpose |
|---------|-------|---------|
| MCP | [[Anthropic]] | Universal protocol for AI-tool connections |
| goose | [[Block]] | Open-source local-first AI agent framework |
| AGENTS.md | [[OpenAI]] | Standard for project-specific AI guidance |

**Platinum members:** AWS, Anthropic, Block, Bloomberg, Cloudflare, [[Google]], [[Microsoft]], [[OpenAI]]

## Adoption

| Metric | Value | Date |
|--------|-------|------|
| Monthly SDK downloads | 97M | Dec 2025 |
| Public MCP servers | 10,000+ | Dec 2025 |

**Key adopters:**
- [[OpenAI]] — integrated across ChatGPT desktop app (Mar 2025), publicly embraced MCP
- [[Microsoft]] — publicly embraced MCP (Feb 2026)
- [[Google DeepMind]]
- Zed, Sourcegraph, other developer tools

**Feb 2026 status:** MCP becoming the de facto industry standard for AI-tool connections. Both OpenAI and Microsoft publicly embraced the protocol, validating Anthropic's open-source strategy.

## Investment Implications

- Standardization reduces moat around proprietary agent frameworks
- Benefits tooling/infrastructure layer (developer tools, API providers)
- Linux Foundation governance = vendor-neutral, broad coalition buy-in
- Accelerates agentic AI adoption by reducing integration friction

## Related

- [[Anthropic]] — creator, donated to AAIF
- [[OpenAI]] — AAIF founding member, adopted MCP
- [[Google]] — AAIF platinum member
- [[Microsoft]] — AAIF platinum member
- [[Linux Foundation]] — governance body for AAIF
- [[AI agents]] — primary use case for MCP
