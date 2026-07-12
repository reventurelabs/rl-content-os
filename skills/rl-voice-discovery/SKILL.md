---
name: rl-voice-discovery
description: >-
  Use when someone has no author-voice skill set up yet, asks "help me find
  my voice," "build a voice profile," "what does my writing actually sound
  like," or when `rl-content-pipeline` notes no author-voice skill is
  configured. Builds a portable voice profile — register, rhythm, phrase
  preferences, what to avoid — from either real writing samples (preferred)
  or a structured interview when no samples exist, then validates it
  against a test passage before finalizing. Produces `VOICE-PROFILE.md` at
  the repo root, which `rl-content-pipeline` and `rl-writing-craft` already
  reference generically as "your author-voice skill." This is a one-time
  (or occasional refresh) discovery process, not something invoked
  per-draft — once `VOICE-PROFILE.md` exists, the other skills read it
  directly. Does not replace a fuller, continuously-evolving voice skill
  (one built from your own ongoing corrections over time will always be
  more accurate than a one-time discovery pass) — it produces the seed, not
  the finished thing.
---

# Voice Discovery

Most people can't accurately describe their own writing voice — they describe
how they *want* to sound, or a generic idea of "professional but approachable."
Real writing beats a description of writing every time: patterns you state
about yourself are often wrong; patterns pulled from what you actually wrote
are grounded. This skill's whole design follows from that one fact.

Output is `VOICE-PROFILE.md` at the repo root — a structured reference the
rest of the suite already knows to look for wherever "your author-voice
skill" is mentioned. This is a discovery process, not a per-draft tool: run
it once to build the profile, run it again later only to refresh it (a
voice can drift, or you might want to capture a second register — e.g. a
more technical one for a different audience).

## Step 1: Get real material, not a self-description

Ask for **5-10 pieces of real writing**, in whatever formats the person
writes most: emails they actually sent, posts they actually published,
messages written fast and not overthought. Minimum useful sample is roughly
500 words total; more is better, and variety of format matters more than
raw volume — three genuinely different contexts (an email, a LinkedIn post,
a Slack message) reveal more than nine similar emails.

**If they have samples:** work from those. Don't ask them to also describe
their voice first — let the samples speak, then check your read against
their reactions in step 4, not before.

**If they have no samples** (a brand-new writer, or someone who's never
published anything): fall back to a structured interview instead. Ask
open-ended questions that surface concrete preferences rather than
abstractions — not "how would you describe your voice" (too abstract, people
default to flattering generalities) but things like: "read this paragraph
out loud in your head — does it sound like you, or like a brand?", "what's a
phrase you'd never say out loud?", "when you write fast and don't edit, what
do you sound like?" Treat interview-derived answers as a rougher first draft
than sample-derived ones, and say so in the output — flag the profile as
"interview-derived, lower confidence" until real samples validate it.

## Step 2: Extract the actual patterns

Read the samples for what's *there*, not what they say about themselves.
Cover, at minimum:

- **Sentence rhythm** — average length, variance, how short sentences get
  used (for emphasis? fragments?), how long ones get built (subordinate
  clauses stacked, or simple additive "and... and...").
- **Formality baseline** — where it sits on a scale, and whether it shifts
  by context (more formal for technical explanation, looser for a personal
  anecdote, say) — most real voices modulate, they aren't a single flat
  register.
- **Contraction usage** — near-universal in casual writing, near-absent in
  some formal registers; note the actual rate, not an assumption.
- **Hedging frequency** — how often claims get qualified ("I think," "maybe,"
  "in my experience") versus stated flatly. Both are legitimate voices; the
  point is to capture which one this person actually does.
- **Signature phrases and vocabulary** — words or short constructions that
  recur enough to be a tell (not generic words everyone uses — the specific,
  slightly unusual ones this person reaches for repeatedly).
- **What they explicitly never do** — no exclamation points, never opens
  with a question, never uses em-dashes, whatever the samples consistently
  avoid. Absence patterns are as much a signature as presence patterns.
- **Emotional range and vulnerability level** — how much personal
  admission, humor, or emotional register shows up, and whether it's
  proportional (real vulnerability) or performed (announced candor —
  `rl-writing-craft`'s Grounding Rules already flag manufactured
  vulnerability; this step is about the person's actual baseline, not
  policing it).
- **Opening and closing patterns** — how pieces tend to start (cold open?
  a question? context-setting?) and end (summary? forward-pointer? a
  specific callback?).

## Step 3: Draft the profile

Write `VOICE-PROFILE.md` with these sections — the template below is the
shape:

```
# Voice Profile

**Source:** [samples provided / interview-derived — note confidence level]
**Formats covered:** [what kinds of writing the samples spanned]

## Tonal Architecture
[Formality baseline + how it shifts by context. Emotional range and
vulnerability level. Humor approach, if any, and its frequency.]

## Distinctive Elements
[The 3-6 things that most make this voice recognizable — specific patterns,
not generic descriptors like "conversational" or "direct."]

## Sentence Mechanics
[Rhythm, contraction rate, hedging frequency, signature phrases, what's
explicitly avoided.]

## Opening and Closing Patterns
[How pieces tend to start and end, with a real example from the samples
where possible.]

## Critical Voice Guidelines
[The handful of rules that most protect this voice from getting flattened
by editing — the equivalent of `rl-writing-craft`'s audit function and
Grounding Rules, but specific to this person: what would make a draft stop
sounding like them.]

## Corrections
[Empty at first write. This section accumulates over time — see "Capturing
durable preferences" in `rl-content-pipeline`. Each entry is a specific
word-choice or register correction the writer made on a real draft, not a
guess: what got corrected, and why, so the same fix doesn't need making
twice.]
```

Every claim in the profile should be traceable to something in the actual
samples — don't invent a pattern because it sounds plausible. If a category
above genuinely isn't determinable from the samples given (too few, too
narrow a format range), say so explicitly in that section rather than
guessing.

## Step 4: Validate against a test passage

Write a short (~200-300 word) passage on a neutral topic — something not in
the original samples — applying the draft profile. Show it to the person and
ask directly: does this sound like you, and where specifically does it not?
Their corrections here are higher-signal than anything in step 2, because
they're reacting to a concrete attempt rather than describing an abstraction.
Fold corrections into the profile and, if the gap was significant, run a
second test passage before finalizing.

## Step 5: Hand off

Once `VOICE-PROFILE.md` is written and validated, it's live — `rl-content-pipeline`
and `rl-writing-craft` already check for "your author-voice skill" and will
find this file. Tell the person this is a starting point, not a finished
system: a voice skill that evolves through their ongoing corrections over
real drafts (the way a continuously-maintained author-voice skill does)
will always outperform a one-time discovery pass. That's what the
Corrections section is for — `rl-content-pipeline` appends to it directly
as real redirections happen on real pieces (see "Capturing durable
preferences" there), so the profile keeps improving without another
discovery pass. This skill produces the seed, not the finished thing.

## Notes

- A deterministic entry point for this skill is the `/voice` command.
- `VOICE-PROFILE.md` covers how you sound. The suite reads a second file,
  `AUTHOR-CONTEXT.md` (the context file — who you write for and why);
  `rl-context-discovery` is the matching discovery tool for that one.
