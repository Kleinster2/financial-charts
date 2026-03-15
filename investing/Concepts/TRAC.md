---
aliases:
  - Track
  - TRAC surveillance
  - non-biometric tracking
  - Jason Bourne app
tags:
  - concept
  - surveillance
  - AI
  - civil-liberties
  - law-enforcement
---

# TRAC

Non-biometric AI surveillance system built by [[Veritone]] (NASDAQ: VERI) that tracks individuals across video feeds using body attributes — clothing, hair color/style, body size, gender, accessories — rather than facial features. Used by 400+ law enforcement agencies, the DOJ (since Aug 2024), DHS, and DOD. Designed explicitly to circumvent the 15-state patchwork of facial recognition bans by avoiding biometric data. The [[ACLU]] calls it "the first non-biometric tracking system used at scale in the US" and warns it creates "a categorically new scale and nature of privacy invasion literally not possible any time before in human history."

## Synthesis

TRAC represents a structural inflection in surveillance technology. The legal hack is elegant: facial recognition bans prohibit analysis of *biometric* data (face, fingerprints, gait), so TRAC analyzes everything else — attributes the law defines as "changeable" even though, as ACLU attorney Nathan Wessler notes, "their profile is going to be the same day after day." The investable insight isn't Veritone specifically (micro-cap, never profitable) but the precedent: once governments discover they can track citizens without technically breaking biometric privacy laws, the demand for non-biometric surveillance tools will compound. This is the first product, not the last. The regulatory gap between "biometric" and "surveillance" will be the next battleground for privacy legislation.

## How it works

1. **Video ingestion**: Police feed footage from body cameras, drones, Ring doorbells, YouTube, social media, or citizen uploads
2. **Attribute menu**: Operators select attributes — jacket color, hairstyle, clothing type, gender, body size, accessories, shoes
3. **Search**: TRAC searches every video in its database for matches on the selected attribute combination
4. **Timeline assembly**: The system tracks a matched individual across different locations and video feeds, assembling movement timelines
5. **Access**: Available through [[Amazon Web Services|AWS]] and [[Microsoft]] Azure cloud platforms

**Current limitations:**
- Operates only on recorded video (not yet live feeds)
- Veritone says live video capability is <1 year away
- Skin tone is used as a differentiating attribute but not currently searchable by users
- Attribute list will continue to expand per CEO Ryan Steelberg

## Legal architecture

| Element | Detail |
|---------|--------|
| **Why it's legal** | Most facial recognition bans cover "biometric data" — permanent physical features. TRAC analyzes "changeable" attributes (clothes, hair, accessories) |
| **States with facial recognition bans** | 15 states + cities (San Francisco, Oakland) as of 2024 |
| **What triggered the bans** | Wrongful arrests, algorithmic bias, privacy violations, cases of imprisonment based on incorrect AI face matching |
| **The loophole** | Laws define biometric data narrowly; body attributes aren't classified as biometric even though they enable equivalent tracking |
| **ACLU position** | First non-biometric tracking system at scale; "categorically new privacy invasion"; potential for abuse at protests, on campuses |
| **Veritone position** | "Culling tool" to speed investigations; exonerates as much as convicts; doesn't replace human judgment |

## Adoption

| Customer | Status | Notes |
|----------|--------|-------|
| **DOJ / EOUSA** | Active since Aug 2024 | Criminal investigations |
| **DHS** | Active | Immigration agencies, broader suite including facial recognition |
| **DOD** | Active | $249M BPA for AI capabilities (broader Veritone contract) |
| **400+ local agencies** | Active | State/local police, universities nationwide |
| **States using it** | CA, WA, CO, NJ, IL | Many of which have facial recognition restrictions |

Departments can purchase TRAC without public hearings, independent testing, or transparency requirements.

## Privacy and civil liberties concerns

**The ACLU's argument (Nathan Wessler):**
- "It creates a categorically new scale and nature of privacy invasion and potential for abuse that was literally not possible any time before in human history"
- "You're now talking about not speeding up what a cop could do, but creating a capability that no cop ever had before"
- Even with face covered at protests, TRAC can track via jacket and shoes
- Campus movements trackable across every camera without knowing identity

**The false match problem:**
- People dressed similarly get flagged → wrongful identifications
- Same fundamental error mode as facial recognition (false positives) but applied to a broader attribute space
- No independent accuracy testing has been published

**Regulatory gap:**
- Current laws define "biometric data" too narrowly
- Non-biometric tracking achieves equivalent surveillance outcomes
- No federal framework addresses attribute-based tracking
- TRAC is available for purchase without oversight, hearings, or testing requirements

## Insights

- The pattern of "comply with the letter, violate the spirit" in surveillance technology is structural — every privacy law creates a market for workarounds. Facial recognition bans created the market for TRAC
- Public sector is only 6% of [[Veritone]]'s revenue, but TRAC gives the company disproportionate strategic positioning in government AI — once you're inside DOJ/DHS/DOD with one product, the cross-sell surface expands
- The "Jason Bourne app" branding (internal nickname) reveals the product's true positioning: real-time, omniscient person-tracking across camera networks. The "culling tool" framing is PR
- The next legislative cycle will likely expand "biometric data" definitions to include attribute-based tracking — but the 400+ agencies already deployed create institutional momentum that's hard to reverse

## Related

- [[Veritone]] — parent company (NASDAQ: VERI)
- [[Palantir]] — peer in government surveillance AI
- [[Clearview AI]] — facial recognition company (the technology TRAC circumvents)
- [[Axon Enterprise]] — body camera maker whose footage feeds into TRAC
- [[ACLU]] — primary civil liberties opponent
