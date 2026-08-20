# Function: `audit`

Dedicated anti-AI sweep. Mechanical pattern detection run clean against finished copy. This is
the final pass — it catches what survived the edit and what the edit introduced.

Run this even after a thorough `edit` pass. Editing fixes tells on the lines it touches; the
audit reads the whole finished piece fresh and catches what slipped through. Run the Logical
Consistency check (see `SKILL.md` → “Logical Consistency — Grave Errors”)
on this pass too.

### Severity Tiers

**P0 — fix before anything else:**
- Chatbot artifacts: "Certainly!", "Great question!", "I'd be happy to," "Feel free to reach
  out," "Let me know if you need anything else"
- Vague attribution: "experts believe," "studies show," "research suggests" with no named source
- Significance inflation on routine events ("marking a pivotal moment in the evolution of...")
- Any grounding-rule violation that survived edit: population quantifiers, invented interiority,
  manufactured experience, manufactured vulnerability, unearned capability claims, causal-superlative
  overclaims

**P1 — fix before publishing:**
- Grounding-rule strong flags that survived edit: unmeasured quantitative flourish, smuggled
  domain metaphor, studied neutrality
- Throat-clearing openers and section pivots
- AI connective tissue ("Which means...," "That's why...," "turns out to be")
- False callbacks
- "actually" and filler intensifiers
- Matched-cadence repetition; uniform sentence rhythm (3+ consecutive similar sentences)
- AI vocabulary (delve, utilize, leverage, robust, seamless, etc.)
- Hollow compound phrases; verdict adjectives
- Announcing the metaphor
- Generic conclusions; summary closes
- Synonym cycling

**P2 — fix when time allows:**
- Copula avoidance ("serves as," "boasts")
- Uniform paragraph length
- Compulsive rule of three (three parallel items used as a reflex — triple adjectives, triple
  examples, triple clauses — where one or two would do)
- Generic business language clusters
- Locally uniform sections (section-by-section scan)

### The Two-Pass Method

The audit runs twice on its own output:

**Pass 1** — read the finished copy, flag every tell by severity, fix.

**Pass 2** — re-read the result. Editing introduces new tells: a cut creates a matched cadence,
a rephrase reaches for an AI verb, a tightened transition becomes a soft reveal. Catch the
survivors and the new arrivals. If the second pass is clean, say so.

### Audit Output

When running `audit`, return: every tell found, quoted, grouped by severity; the corrected
text; a brief note on what changed; and the second-pass result. If the copy is clean, say that
plainly rather than inventing flags to look thorough.

---

Part of the `rl-writing-craft` skill. See `SKILL.md` for how this function
sequences with the other three and with an author-voice skill.
