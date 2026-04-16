---
aliases: [WireGuard VPN, WireGuard protocol]
tags: [concept, networking, cryptography, open-source, vpn]
---

WireGuard — modern VPN protocol built into the Linux kernel (since 5.6, March 2020). Written by Jason Donenfeld. Designed as a replacement for [[IPsec]] and [[OpenVPN]]: ~4,000 lines of code vs hundreds of thousands, fewer configurable knobs, fixed cryptographic suite (Curve25519, ChaCha20-Poly1305, BLAKE2s, SipHash24, HKDF).

## Why it matters

WireGuard turned VPNs from a plumbing problem into a thin-client problem. The protocol handles packet encryption, key exchange, and peer authentication in a small, auditable core. Everything above — user identity, device enrollment, NAT traversal coordination, ACLs, DNS — became the product surface. That decomposition enabled a generation of mesh VPN products ([[Tailscale]], ZeroTier adopting it, [[Cloudflare]] WARP, Mullvad) that compete on orchestration rather than cryptographic primitives.

## Adoption

| Year | Milestone |
|------|-----------|
| 2015 | Initial release by Jason Donenfeld |
| 2018 | Linus Torvalds endorses it as "a work of art" |
| 2020 | Merged into Linux kernel 5.6 |
| 2020+ | [[Tailscale]], Mullvad, NordLynx (NordVPN), Cloudflare WARP adopt |

## Technical properties

- Stateless handshake, silent on idle
- Roaming without reconnect (floats across network changes)
- No negotiation of crypto primitives — single fixed suite eliminates downgrade attacks
- Symmetric key rotation every 2 minutes

## Related

- [[Tailscale]] — mesh VPN orchestration on top of WireGuard
- [[Cloudflare]] — WARP uses WireGuard
- [[Zero Trust]] — architectural pattern WireGuard-based products fit

## Sources

- [WireGuard Whitepaper](https://www.wireguard.com/papers/wireguard.pdf)
- [Linux kernel 5.6 release notes](https://kernelnewbies.org/Linux_5.6)
