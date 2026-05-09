---
aliases: [Privy wallet, Stripe Privy]
---
#product #fintech #private #wallet #ai-agents

Privy — Embedded wallet-as-a-service product, owned by [[Stripe]] (acquired 2025). Reference wallet implementation for AWS Bedrock AgentCore Payments alongside [[Coinbase]]'s [[x402]].

Privy is a developer-focused wallet infrastructure that lets applications spin up custodial or self-custodial wallets for end-users without users managing seed phrases. Acquired by Stripe in 2025 and integrated as the default wallet layer for Stripe's stablecoin infrastructure (Bridge). In May 2026 it became one half of the Amazon AWS Bedrock AgentCore Payments stack: Privy provides the wallet, [[Coinbase]]'s [[x402]] protocol provides the HTTP-level payment standard, and AWS provides the agent runtime.

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Stripe]] |
| Acquired | 2025 |
| Type | Embedded wallet SaaS |
| Reference deployment | Amazon AWS Bedrock AgentCore Payments (May 7, 2026) |

## Why it matters for the investing vault

For [[Coinbase]]: Privy is complementary, not competitive — Privy provides the wallet, x402 provides the payment protocol, both ship together in the AWS reference architecture.

For [[Stripe]]: Privy is the wallet leg of Stripe's stablecoin payment stack (Bridge for stablecoin issuance/treasury, Privy for end-user wallets, x402 for the agent payment standard).

## Related

- [[Stripe]] — parent (acquired 2025)
- [[Coinbase]] — co-deployed via AWS Bedrock AgentCore Payments
- [[x402]] — payment protocol standard paired with Privy in agentic-commerce stack
- [[Stablecoins]]
- [[AgentKit]]
