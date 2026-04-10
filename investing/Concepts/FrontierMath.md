---
aliases: [Frontier Math, FrontierMath benchmark]
tags: [concept, ai, benchmark, math]
---

# FrontierMath

**FrontierMath** — a math benchmark designed by "respected mathematicians and theoretical computer scientists" who release problems representative of their day-to-day research work, unpublished anywhere, so that AI models can attempt them without training data contamination. Unlike competition math ([[IMO]]), FrontierMath targets working research-level mathematics — the kind of problems a PhD mathematician grapples with over days or weeks, not hours.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Type | Research-level math benchmark |
| Problems | Curated by domain experts; unpublished |
| Key feature | No training contamination (problems never published before) |
| Notable result | [[OpenAI]] model solved problems in ~1 hour that would take [[Jakub Pachocki]] (PhD in the field) 1-2 weeks |
| First major test | Week-long deadline, dropped with no advance warning |

---

## Why it matters

Competition math ([[IMO]], AIME) tests speed and technique on well-structured problems with known solution types. FrontierMath tests whether models can produce novel mathematical insight on problems that have no published approach — closer to actual research than to competitions.

The FrontierMath challenge was dropped "without any advanced warning" with a week-long deadline. [[OpenAI]]'s James Lee, in charge of a model training run at the time, began prompting the model by hand. [[Jakub Pachocki]] described watching the model solve problems from his own PhD domain: ideas he would have been "quite proud to come up with in a week or two" were produced in roughly an hour.

The organizers commented that AI solutions felt like "19th century mathematics — brute force, computation-heavy approaches rather than elegant modern techniques." Pachocki is unconcerned: models produce "so much more reasoning in a short time than a person" that computational brute force may be an artifact of scale rather than a fundamental limitation. He noted that for at least one problem, the model "actually produced a pretty nice proof that was quite a bit shorter than the intended one."

---

## FrontierMath tier 4

[[OpenAI GPT-5.4]] solved a tier 4 FrontierMath problem curated ~20 years ago. The reviewing mathematician called it his "personal Move 37" — referencing [[AlphaGo]]'s famous unexpected strategy in Game 2 against Lee Sedol.

---

## Implications

FrontierMath results chip away at the "pattern matcher" narrative — the claim that AI models can only recombine existing knowledge and cannot produce genuinely novel insight. Pachocki's counter: "Was Alpha Zero a pattern matcher? Our Dota bot — they did come up with new strategies for the respective games." He expects "a lot of definitional debates for a while" but views the evidence as accumulating steadily.

The benchmark also illustrates a practical advantage of math for AI evaluation: "It's much easier to tell whether you've actually solved the math problem than whether you've produced a good piece of software." This is why math served as [[OpenAI]]'s northstar for reasoning model development (o1 through o3), though that focus is now shifting toward real-world utility.

---

## Related

- [[Jakub Pachocki]] — OpenAI Chief Scientist; solved problems from his PhD domain
- [[OpenAI GPT-5.4]] — tier 4 breakthrough ("personal Move 37")
- [[GPT]] — model family; math as reasoning northstar
- [[OpenAI]] — developer
- [[AlphaGo]] — precedent for AI discovering novel strategies
- [[Frontier models]] — category
