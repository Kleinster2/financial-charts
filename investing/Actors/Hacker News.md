---
aliases: [HN, news.ycombinator.com, Startup News]
---
#actor #media #usa #product

**Hacker News** — Social news platform run by [[Y Combinator]], the de facto town square for Silicon Valley's technical and startup community.

~10M pageviews/day, ~2M+ registered users, no ads, no algorithm — purely upvote-ranked links and comments. Its front page drives meaningful traffic spikes and shapes tech discourse disproportionate to its modest scale. HN sentiment often leads mainstream tech narrative by days or weeks — front-page posts have moved stocks, driven product launches viral, and surfaced security vulnerabilities before traditional media picks them up. The audience (founders, VCs, senior engineers, security researchers, tech journalists) makes it the highest-signal tech community on the internet.

---

## Quick stats

| Metric | Value |
|--------|-------|
| URL | [news.ycombinator.com](https://news.ycombinator.com) |
| Owner | [[Y Combinator]] |
| Founded | February 19, 2007 |
| Founder | [[Paul Graham]] |
| Moderators | Daniel Gackle (dang), Tom Howard (tomhow) |
| Written in | Arc (programming language) |
| Pageviews | ~10M/day (2022 estimate) |
| Users | ~2M+ registered |
| Revenue model | None (no ads, no subscriptions) |
| API | Public, Firebase-backed (`hacker-news.firebaseio.com/v0/`) |

---

## How it works

Hacker News is a link aggregator with threaded comments. Users submit URLs or text posts ("Ask HN", "Show HN", "Tell HN"). Content is ranked by upvotes with a time-decay algorithm. No algorithmic personalization — everyone sees the same front page.

Key mechanics:
- Upvoting available to all registered users
- Downvoting requires 501+ karma (upvotes received minus downvotes)
- Flagging requires 30+ karma
- Stealth banning (shadowbanning) used for spam/bad actors
- Voting ring detection
- Active human moderation by dang and tomhow
- No ads, no promoted content, no paywall

Content scope: "anything that gratifies one's intellectual curiosity" — in practice, heavily skewed toward programming, startups, AI/ML, security, science, and tech business.

---

## Why Hacker News matters

HN punches far above its traffic weight because of who reads it:
- Founders, VCs, and engineers at major tech companies
- Open source maintainers and security researchers
- Tech journalists (many stories start on HN before reaching mainstream media)
- Hiring managers (monthly "Who is hiring?" threads are a major recruiting channel)

A front-page HN post can generate 15-50K visits in hours, crash small sites ("HN hug of death"), and create lasting SEO effects from backlinks.

HN is where:
- Security vulnerabilities get disclosed and amplified
- New developer tools gain initial traction ("Show HN" launches)
- Corporate missteps get surfaced (layoffs, dark patterns, pricing changes)
- Technical deep dives on earnings, architectures, and business models circulate
- Sentiment shifts on companies often appear days before mainstream coverage

---

## Relationship to Y Combinator

HN was created by [[Paul Graham]] as a side project to test the Arc programming language and build a community around [[Y Combinator]]. It serves as YC's public-facing community but is not a commercial product — it generates no revenue and runs no ads.

YC-backed startups get natural amplification on HN (founders and alumni are active users), but the site has no formal bias mechanism. Moderation actively combats accusations of YC favoritism.

Graham stepped away from daily HN management in March 2014 when he reduced his role at YC. Daniel Gackle (dang) has been the primary moderator since ~2016, joined by Tom Howard (tomhow) in April 2025.

---

## API

Public API, no authentication required:
- Base URL: `https://hacker-news.firebaseio.com/v0/`
- Endpoints: top stories, new stories, best stories, ask/show/job stories
- Individual items: `/v0/item/{id}.json`
- User profiles: `/v0/user/{id}.json`
- Real-time via Firebase SDK
- No rate limit published, but reasonable use expected

Widely used for sentiment analysis, trend detection, and content monitoring tools.

---

## Related

- [[Y Combinator]] — parent organization, operator
- [[Paul Graham]] — founder
- [[Reddit]] — closest comparable (HN was created to be "like early Reddit")

