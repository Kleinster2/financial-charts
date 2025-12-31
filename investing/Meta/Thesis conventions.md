#meta #conventions

# Thesis conventions

How to read thesis names in this vault.

---

## Long X

**Meaning**: Long X, hedged against all systematic factors (market, sector, style, macro).

**What you're betting on**: Idiosyncratic alpha — X outperforms what its factor exposure would predict.

**Example**: `Long Anthropic`
- Not betting "AI will do well"
- Betting Anthropic specifically outperforms its peer group and factor-adjusted expected return
- Hedge out: AI sector, growth factor, private equity risk, etc.
- Profit if Anthropic-specific thesis plays out (agentic code moat, enterprise trust)

---

## Short X

**Meaning**: Short X, hedged against all systematic factors.

**What you're betting on**: X underperforms what its factor exposure would predict.

**Example**: `Short OpenAI` (if it existed)
- Not betting "AI will fail"
- Betting OpenAI specifically underperforms vs peers
- Hedge out: AI sector exposure
- Profit if OpenAI-specific risks materialize (burn rate, consumer churn)

---

## Short X Long Y (or Long Y Short X)

**Meaning**: Pairs trade between two highly correlated stocks. Direction-agnostic. Betting on spread widening.

**What you're betting on**: Y outperforms X on a relative basis, regardless of absolute direction.

**Requirements**:
- X and Y must be highly correlated (same sector, similar factor exposure)
- Thesis resolution widens the spread between them
- Market/sector moves cancel out

**Example**: `Short TSMC Long Korea`
- TSMC and Samsung/SK Hynix are highly correlated (semis, Asia, similar drivers)
- Thesis: Korea outperforms TSMC on relative basis
- Outcomes:
  - Both +20%, Korea +25% → win
  - Both -20%, TSMC -25% → win
  - TSMC +10%, Korea +15% → win
- Resolution events: AMD signs Samsung, SK Hynix packaging wins, Taiwan risk reprices
- Direction doesn't matter — only the spread

---

## Position sizing implication

| Type | Directional exposure | Thesis purity |
|------|---------------------|---------------|
| Long X | Hedged | Pure idiosyncratic |
| Short X | Hedged | Pure idiosyncratic |
| Long/Short | Zero (pairs) | Pure relative value |

Long/short pairs have the cleanest expression — no market beta, no sector beta, pure thesis.

---

## Practical notes

- "Long X" on a private company (e.g., Anthropic) requires finding derivative exposure or waiting for IPO
- Long/short pairs require both legs to be tradeable and borrowable
- Factor hedging can be approximate (sector ETF, basket of peers) or precise (multi-factor model)

---

Related: [[Foundry Wars]], [[AI Race]]
