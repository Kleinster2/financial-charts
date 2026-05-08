---
aliases: [Beagle malware, Beagle Windows backdoor]
tags: [concept, cybersecurity, malware, ai]
---

# Beagle backdoor

**Beagle backdoor** is a Windows malware payload surfaced in May 2026 through fake [[Claude]] installer campaigns. It is distinct from the older Beagle/Bagle worm family documented in 2004.

## Why it matters

The May 2026 campaign used `claude-pro[.]com` and a trojanized `Claude-Pro-windows-x64.zip` installer to exploit demand for [[Anthropic]] tools. The installer behaved like a plausible Claude client while running a PlugX-style chain in the background: signed `NOVupdate.exe` side-loading `avk.dll`, decrypting `NOVupdate.exe.dat`, loading DonutLoader, then injecting Beagle into memory.

Beagle's command set is basic but operationally useful:

| C2 verb | Function |
|---------|----------|
| `cmd` | Execute shell |
| `upload` / `download` | Move files |
| `ls` | List directory contents |
| `mkdir` / `rename` / `rm` | File-system operations |
| `uninstall` | Remove agent |

The C2 observed in the campaign used `license[.]claude-pro[.]com`, TCP 443 and/or UDP 8080, with a hardcoded AES key protecting exchanges. Related samples submitted February-April 2026 used different delivery paths, including decoy PDFs and impersonated update sites for security vendors.

## Investment read

Beagle is small by itself, but the distribution pattern matters. Frontier AI brands are now phishing lures in the same way banks, VPNs, and browser updates were in earlier cycles. The security category is not "model safety" alone; it includes endpoint protection, signed-binary abuse, cloud-hosted C2, and brand-protection workflows around AI tools. See [[Agentic AI security]] for the broader framework.

## Related

- [[Agentic AI security]] — broader attack-surface framework
- [[Anthropic]] — Claude parent company and brand impersonated by the campaign
- [[Claude]] — lure brand
- PlugX — similar historical loader/backdoor activity referenced by researchers; no vault note created because the pre-create check collides with [[Plug Power]]'s PLUG alias
- [[Alibaba Cloud]] — C2 IP range reportedly associated with [[Alibaba]] Cloud service

*Source: BleepingComputer, "Fake Claude AI website delivers new 'Beagle' Windows malware," May 7, 2026.*
