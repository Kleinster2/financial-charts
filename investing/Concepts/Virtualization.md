---
aliases: []
---
#concept #infrastructure

**Virtualization** — Running multiple operating systems on single physical hardware. [[VMware]] created mainstream x86 virtualization (1998).

---

## Why virtualization matters

Foundation of modern cloud computing:

- **Server utilization**: ~15% → 80%+ (massive efficiency gains)
- **Cloud enabler**: AWS, Azure, GCP all built on virtualization
- **Cost reduction**: Fewer physical servers needed
- **Flexibility**: Spin up/down workloads instantly

---

## Types

| Type | Description |
|------|-------------|
| **Server** | Multiple VMs on one server (VMware vSphere) |
| **Desktop** | Virtual desktops (VMware Horizon, Citrix) |
| **Network** | Software-defined networking (VMware NSX) |
| **Storage** | Software-defined storage (VMware vSAN) |
| **Containers** | Lighter-weight than VMs (Docker, Kubernetes) |

---

## Key players

| Company | Product |
|---------|---------|
| [[VMware]] | vSphere, NSX, vSAN (now [[Broadcom]]) |
| [[Microsoft]] | Hyper-V |
| [[Red Hat]] | KVM (via RHEL) |
| Citrix | XenServer |

---

## Evolution

| Era | Technology |
|-----|------------|
| 1960s | IBM mainframe virtualization |
| 1999 | VMware brings x86 virtualization to market |
| 2006 | AWS EC2 launches (virtualization at scale) |
| 2013+ | Containers (Docker) complement VMs |

---

## Related

- [[VMware]] — market creator
- [[Diane Greene]] — VMware co-founder
- [[Cloud computing]] — built on virtualization
- [[Broadcom]] — VMware owner
