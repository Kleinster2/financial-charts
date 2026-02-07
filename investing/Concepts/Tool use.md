---
aliases: [function calling, AI tool use, agentic capabilities]
---

LLMs calling external tools — web search, code interpreters, APIs. A key capability unlock.

## Why it matters

Solves hallucination partially: instead of memorizing facts, model can search. Instead of doing math in weights, model calls calculator.

"Who won the World Cup in 1998?" → model searches FIFA website → gets correct answer reliably.

## Current state

Proprietary LLMs (ChatGPT, Claude) have deep tool integration. Open models lagging — harder because you need general reasoning engine that works with multiple tools.

**Jamba** notable as first open-weight model trained specifically with tool use in mind.

## The trust problem

Tool use requires giving LLM permission to act. Do you want LLM accessing your emails? Your file system? Most people not comfortable yet.

Need containerized, sandboxed environments before this scales.

## Closed vs open model dynamics

Closed models: deeply integrate specific tools into experience (search, code execution).

Open models: must work with arbitrary tools for arbitrary use cases. Harder to optimize.

## Enables agentic workflows

[[Inference-time scaling]] + tool use = agentic AI. Model can:
- Try a tool
- See results
- Try another approach
- Iterate until solved

This is why Claude Code and Cursor work.

## The unlock for coding

Models learned tool use through [[RLVR]] training. They quickly learn to:
- Run CLI commands
- Handle Git
- Search codebases
- Check outputs

Year ago this wasn't possible. Now transformative.

## Related

- [[AI extensibility]] — tool use is the foundation of the extensibility stack
- [[Inference-time scaling]] — enables iterative tool use
- [[RLVR]] — training that taught tool use
- [[Claude Code]] — product built on this
- [[Cursor]] — product built on this
- [[Agentic AI]] — broader category
