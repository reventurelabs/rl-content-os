---
name: rl-voice-discovery
description: >-
  Use when someone has no author-voice skill set up yet, asks "help me find
  my voice," "build a voice profile," "what does my writing actually sound
  like," or when `rl-content-pipeline` notes no author-voice skill is
  configured. Builds a portable voice profile — register, rhythm, phrase
  preferences, what to avoid — from real writing samples (preferred when
  they exist), a structured interview (when there are no samples, or when
  the person wants to name a voice they are building toward rather than the
  one already on the page), or both together, then validates it against a
  test passage before finalizing. Produces `VOICE-PROFILE.md` at the repo
  root, which `rl-content-pipeline` and `rl-writing-craft` reference
  generically as "your author-voice skill." A one-time (or occasional
  refresh) process, not invoked per-draft — once the file exists, other
  skills read it directly. Does not replace a fuller, continuously-evolving
  voice skill built from ongoing corrections — this produces the seed, not
  the finished thing.
license: MIT
---

# Voice Discovery

Most people can't accurately describe their own writing voice in the
abstract — they describe how they *want* to sound, or a generic idea of
"professional but approachable." Real writing beats a vague description of
writing every time: patterns stated about yourself in the abstract are
often wrong; patterns pulled from what you actually wrote are grounded.

That doesn't rule out intent. Wanting to sound like a voice you haven't
fully written into yet is a real, legitimate target, not a bias to correct
for — people hire ghostwriters with direction all the time, and there's
nothing dishonest about building toward a voice on purpose. The actual
distinction this skill draws isn't existing-voice-good,
wanted-voice-bad — it's specific versus vague. A concrete answer to "what's
a phrase you'd never say out loud" is signal whether it describes what's
already true or what someone's building toward. A vague answer to "how
would you describe your voice" is noise either way. This skill's design
follows from that distinction, not from a preference for the past over the
future.

Output is `VOICE-PROFILE.md` at the repo root — a structured reference the
rest of the suite already knows to look for wherever "your author-voice
skill" is mentioned. This is a discovery process, not a per-draft tool: run
it once to build the profile, run it again later only to refresh it (a
voice can drift, or you might want to capture a second register — e.g. a
more technical one for a different audience).

## Step 1: Get real material — and ask about intent

Ask for **5-10 pieces of real writing**, in whatever formats the person
writes most: emails they actually sent, posts they actually published,
messages written fast and not overthought. Minimum useful sample is roughly
500 words total; more is better, and variety of format matters more than
raw volume — three genuinely different contexts (an email, a LinkedIn post,
a Slack message) reveal more than nine similar emails.

**If they have samples:** work from those first — don't ask them to also
describe their voice in the abstract, let the samples speak, then check
your read against their reactions in step 4. But also ask directly: is this
profile meant to describe how you already write, or is there a voice
you're building toward that these samples don't fully show yet? Both are
legitimate answers. If they want the second, run the structured interview
below alongside the sample analysis, and keep the two sources
distinguishable in the profile (Step 3) rather than quietly blending them
into one voice that overstates what the samples actually show.

**Run the structured interview** when there are no samples (a brand-new
writer, or someone who's never published anything), or whenever the person
wants it regardless of samples — direction toward a voice they're aiming
for, not just a description of the one they already have. Ask open-ended
questions that surface concrete preferences rather than abstractions — not
"how would you describe your voice" (too abstract, people default to
flattering generalities either way, whether describing the past or the
future) but things like: "read this paragraph out loud in your head — does
it sound like you, or like a brand?", "what's a phrase you'd never say out
loud?", "when you write fast and don't edit, what do you sound like?" —
and, when it's about intent specifically, "who's a writer whose voice you'd
want this to have some of?", "what would this sound like if you'd already
become the writer you're trying to be?"

Interview answers describing an **existing** voice with no samples to check
them against are a rougher first draft than sample-derived ones — flag that
portion "interview-derived, lower confidence" until real samples validate
it. Interview answers naming an **aspirational** voice don't get that same
flag; they're not claiming to describe current behavior, so there's nothing
to validate them against. They're a direction, stated as one.

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

**Source:** [samples provided / interview-derived — note confidence level;
if aspirational interview answers are layered on top of samples, say so
here, e.g. "samples (extracted) + interview (aspirational, marked inline
below)"]
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

Where an aspirational interview answer changes or adds to what the samples
show, mark that item inline — e.g. "(aspirational — not yet reflected in
samples)" — rather than presenting it as an already-established pattern.
The profile is still the operative target other skills write toward either
way; the marker is about honesty in the profile's own account of itself,
not a hedge on whether to use it.

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

**A signal for when the profile itself is the problem.** If drafts keep needing
heavy rewrites well after the profile is in place and the Corrections section
already has real entries in it, that's usually not a sign the drafts need more
editing — it's a sign the profile's own rules are still too abstract to steer
generation. As a rough rule of thumb, not a hard threshold: light-to-moderate
revision on most drafts is normal; heavy revision on nearly every draft is the
signal. When that happens, go back to Step 3 and replace whatever's still a
vibe-descriptor ("conversational," "direct") with the concrete, checkable
version Step 2 was supposed to extract, rather than concluding the writer just
needs to keep editing harder.

## Notes

- A deterministic entry point for this skill is the `/voice` command.
- `VOICE-PROFILE.md` covers how you sound. The suite reads a second file,
  `AUTHOR-CONTEXT.md` (the context file — who you write for and why);
  `rl-context-discovery` is the matching discovery tool for that one.
