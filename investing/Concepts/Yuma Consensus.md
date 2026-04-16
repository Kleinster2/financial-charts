---
aliases:
  - Yuma
tags:
  - concept
  - crypto
  - ai
  - bittensor
  - consensus
---

# Yuma Consensus

Yuma Consensus is the reward algorithm used by [[Bittensor]] to aggregate validator scores of miner outputs and determine TAO (and [[Dynamic TAO|alpha token]]) distribution across each subnet. Validators submit individual rankings; Yuma combines them into a network-wide scoring vector and pays out emissions proportionally.

---

## Role in the protocol

| Layer | Function |
|-------|----------|
| Subtensor base chain | Proof-of-Authority ordering |
| Yuma Consensus | Aggregation of validator rankings → reward distribution |
| Per-subnet incentive | Subnet-specific scoring logic set by subnet owner |

Yuma is not a block-consensus algorithm — Subtensor handles block ordering via PoA. Yuma is an aggregation layer that converts many independent validator opinions into a single truth about which miners performed best in each subnet.

---

## Why it matters

- Makes validator collusion economically costly — validators whose rankings diverge from consensus are penalized.
- Enables "market for intelligence" model: every subnet is a distinct scoring game but the distribution layer is shared.
- Designed by the [[Opentensor Foundation]] as Bittensor's core contribution to decentralized-AI protocol design.

---

## Related

- [[Bittensor]] — parent protocol
- [[Opentensor Foundation]] — developer
- [[Dynamic TAO]] — upgrade that runs under Yuma
- [[Ridges AI]] — subnet using Yuma rewards to pay coding-agent miners
