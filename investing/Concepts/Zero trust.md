# Zero Trust

Security model built around the idea that no user, device, or network segment should be trusted by default. Access is continuously verified rather than granted because something sits inside a corporate perimeter.

---

## Why it matters

Zero Trust became a core enterprise-security architecture as work moved to cloud apps, remote devices, and API-heavy environments where the old inside/outside network boundary broke down.

---

## Common components

| Component | Function |
|-----------|----------|
| Identity verification | Confirm user and device posture |
| Least-privilege access | Limit each session to what it needs |
| Continuous policy checks | Re-evaluate trust during the session |
| Segmentation | Contain breaches and lateral movement |
| Logging and analytics | Detect abnormal behavior |

---

## SASE linkage

[[SASE]] is the commercial architecture that packages zero-trust access, secure web gateway, firewall-as-a-service, data-loss prevention, and network connectivity into one cloud-delivered control plane. Reuters' May 26, 2026 Zscaler earnings coverage framed SASE as one of the fastest-growing cybersecurity segments because cloud adoption and AI workloads keep moving users, devices, data, and applications outside the old perimeter.

The investment tension is now budget ownership. [[Zscaler]] remains the zero-trust/SASE pure-play, while [[Palo Alto Networks]], [[Fortinet]], [[Cloudflare]], and other platforms are bundling adjacent controls into larger account relationships. That means zero trust is still a structural architecture shift, but SASE economics increasingly depend on whether buyers prefer best-of-breed cloud proxy architecture or broad platform consolidation.

*Sources: [Reuters via StreetInsider, May 26 2026](https://www.streetinsider.com/Reuters/Zscaler%2Bsees%2Bdownbeat%2Bquarterly%2Brevenue%2Bas%2Bcompetition%2Bheats%2Bup%2Bin%2Bcybersecurity%2Bmarket/26550638.html); [Zscaler Q3 FY2026 release](https://ir.zscaler.com/news-releases/news-release-details/zscaler-announces-strong-third-quarter-fiscal-2026-results).*

---

## Related

- [[Cloudflare]] — sells Zero Trust access and secure-edge products
- [[Zscaler]] — another major Zero Trust platform
- [[SASE]] — architecture that packages zero-trust access into a cloud-delivered network/security service
