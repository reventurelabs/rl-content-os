---
name: rl-long-form-pipeline
description: >-
  Structured 10-step writing process, triggered by either of two independent
  conditions — long-form content (blog posts, whitepapers, essays, case
  studies, anything past ~800 words) OR high-stakes content regardless of
  length (a short statement going out under the company's name, an
  announcement with no room to walk back a bad framing). Cost-of-being-wrong
  is the real criterion; length is only one proxy for it. Orchestrates the
  existing writing skills (your content-generation and author-voice skills
  for generation, rl-writing-craft for structure/edit/audit/copyedit, plus an
  optional closing polish skill if you have one, e.g. ann-handley-voice) — it
  does not duplicate their rules, it sequences them. Adds what a single draft
  skips: define topic/angle/goal, interview the SME/author to surface
  specifics and resolve ambiguity, write a creative brief, outline before
  drafting, draft section by section, critique the draft against the brief,
  revise, run the writing suite, refine, and get explicit approval before
  anything is considered done. Trigger on "blog post," "whitepaper," "essay,"
  "long-form," "this needs to be right," "write this properly," or any
  explicit request for the structured/step-by-step process. For low-stakes
  quick-turn formats (a routine LinkedIn post, a routine email, social copy)
  use your content-generation or author-voice skill directly — this skill is
  overhead they don't need.
---

# Long-Form Pipeline — Structured 10-Step Writing Process

A tenth-lane orchestrator, not a sixth generator. This skill owns **sequencing**
for long-form or high-stakes pieces; it borrows every actual writing rule from
the skills that already have them:

- **your content-generation skill** / **your author-voice skill, if you have one** — generation, voice. "Your author-voice skill" resolves to an actual installed skill if you have one, or to `VOICE-PROFILE.md` at the repo root directly (produced by `rl-voice-discovery`) if that's what exists instead — check for the file before concluding there's no voice reference at all.
- **rl-writing-craft** — structure, grounding (Grounding Rules), line edit, anti-AI audit, copyedit. Always present — this is the one dependency that isn't optional.
- **an optional closing polish skill, if you have one** (e.g. ann-handley-voice) — a final voice/readability pass on top of rl-writing-craft's floor. Not required — skip this if you don't have one.

If you find yourself restating a rule those skills already own, stop — invoke
the skill instead of re-deriving its logic here.

**No content-generation or author-voice skill installed? This still works.**
Draft directly from the brief and outline (steps 3-4) at step 5, using
`rl-writing-craft`'s Grounding Rules as the floor — same as `rl-writing-craft`
itself works standalone with no author-voice skill present. What you lose
without a dedicated generation/voice skill is a tailored register — the draft
will read in a competent, neutral voice rather than *your* specific voice.
What you don't lose is the process: interview, brief, outline, adversarial
review, and the approval gate all run exactly the same either way. Building a
content-generation or author-voice skill later is worth doing for voice
quality, not for this pipeline to function. If you have real writing samples
(or none, and want the interview path), `rl-voice-discovery` builds that
starting profile — see `VOICE-PROFILE.md` at the repo root, which this skill
already checks for wherever it says "your author-voice skill."

## When to use this vs. the short pipeline

Two independent triggers, either one is enough — length is not the real
criterion, cost-of-being-wrong is:

- **Long-form**, where a wrong structural call is expensive to fix after the
  words are already written: blog posts, whitepapers, essays, case studies,
  thought-leadership pieces.
- **High-stakes, regardless of length** — a 150-word statement going out
  under the company's name, a short email where the wrong claim damages a
  relationship, an announcement with no room to walk back a bad framing. The
  interview, brief, and adversarial review steps catch exactly the mistakes
  that are cheap to fix here and expensive to fix after it's sent.

For a LinkedIn post, a routine email, or social copy that's genuinely
low-stakes — the kind where a bad opening line costs you nothing but a
slightly weaker post — go straight to your content-generation or author-voice
skill (see the `/write` command). Running all 10 steps there is pure
overhead. The overhead isn't earned by word count; it's earned by what a
mistake would cost.

## Why 10 steps, not one draft

Each step exists to catch a specific, well-documented failure mode:

- Drafting before the goal and audience are pinned down produces content that's
  fluent but aimless.
- Skipping the interview means the draft ships without the specifics —
  first-hand examples, a real opinion, a concrete number — that separate
  writing worth reading from generic AI output. Expert input arriving *after*
  a draft is already structured turns into rework, not refinement.
- Drafting without an approved outline means restructuring after the words are
  already written — the most expensive place to catch a shape problem.
- Reviewing "does this sound okay" instead of "does this hit the brief"
  produces polish without progress. A critique needs to name what's missing
  and where, or the revision has nothing to aim at.
- Skipping the writing suite ships something that reads competent but
  generic — uniform sentence rhythm, hedge-everything phrasing, no point of
  view. That's the exact signature readers now flag as AI-written.
- Treating a finished draft as a finished *deliverable* is how the wrong thing
  gets published. Nothing here is done until step 10 says so.

## The 10 Steps

### 1. Define topic, angle, goal

Pin down: topic, target reader, the angle/thesis (what position is this piece
taking, not just what it's about), the goal (educate, convert, thought
leadership, internal alignment), which venture or publication this is for, and
a rough length target. Infer whatever's already given in the request; ask only
what's genuinely missing — one consolidated question, not a checklist.

If the topic came from `rl-repo-topic-scout`, it already carries this from the
shortlist. Otherwise, check `AUTHOR-CONTEXT.md` at the repo root for who this
piece is for and why it's worth writing at all — same file `rl-repo-topic-scout`
reads, kept consistent so "who I write for" doesn't drift between the two
skills. If it's still the unfilled template, `rl-context-discovery` builds it
properly (evidence first, then a guided interview) rather than a one-off
question here.

### 2. Interview the SME/author

Adaptive, based on who the expertise belongs to:

- **You are the SME** (most of your own ventures/projects) — a short,
  pointed self-interview. Ask 2-4 open-ended questions aimed at surfacing the
  specifics a draft would otherwise invent or skip: a real example, a number,
  a position you'd defend, something that didn't work. Don't ask what's already
  answered by step 1.
- **A named third party is the SME** (a client, a guest expert, a partner) —
  a fuller interview. Ask open-ended questions so they can surface
  things you wouldn't have thought to ask about, and explicitly ask them to
  quantify or define anything they state in vague or abstract terms. Record
  what they say rather than paraphrasing from memory.

Either way, this step's output is raw material — quotes, numbers, opinions,
examples — not prose. That material is what step 5 draws on instead of
inventing connective filler.

**Optional: outside validation.** Off by default — offer it, don't run it
automatically. When the angle rests on a claim about what people currently
think, want, or are struggling with (not just on the author's own
experience), ask whether it's worth checking against outside discourse
before writing. If the `last30days-skill` is available in this session, use
it to check current Reddit/X/HN/web discussion on the topic — does the
angle hold up against what people are actually saying, or is it a stale
take a week of real discourse would contradict? If it isn't installed, say
so and how to get it (`npx skills add mvanhorn/last30days-skill`), then
continue without it — this is a strengthening step, never a blocker.

### 3. Creative brief / executive summary

Synthesize steps 1-2 into a short brief: objective, audience, key message(s),
success criteria (what does this piece need to do to have worked), non-goals
(what it's deliberately not trying to do), and a voice reference — point at
your content-generation skill's venture/audience context or your author-voice
profile, don't restate their rules here. Show the brief and get one
confirmation before moving on — a quick yes/adjust, not a document review.

### 4. Outline with subitems

Build the H2/H3 structure: each section's job, its key talking points, and
which specific example or data point from step 2 belongs where. This is the
cheapest point in the whole process to catch a shape problem — get it
approved before writing a single section. If you redirect the outline,
that's the process working, not a delay.

### 5. Draft section by section

Write each outline item using your content-generation skill's rules
for venture/brand content, or your author-voice skill directly for
personal-voice pieces. Pull the specifics surfaced in step 2 into the sections where the outline
placed them. Follow `rl-writing-craft`'s Grounding Rules throughout — never
invent scenes, specifics, or claims about real people; leave a gap and flag
it rather than papering over it.

### 6. Review the draft against the brief

Two distinct passes, not one vague "review." A single self-review from the
same context that just drafted the piece is the weakest possible judge of it —
it's blind to exactly the generic phrasing and shape problems it just wrote.

**Judge pass (criteria-scored).** For each of the brief's success criteria and
key messages: does the draft actually hit it, and if not, where specifically
and what needs to change? Name gaps in terms the next step can act on
directly — "the third section asserts the claim but never earns it" beats
"needs more work."

**Adversarial pass (blind, via a fresh `Agent` call).** Spawn a sub-agent with
no context on how the piece was written, what it's "supposed" to do, or what
process produced it — just the finished draft and the instruction to actively
try to kill it: find the weakest section, the sentence that could describe any
company or any founder's story, the paragraph a reader bails on, anything that
reads like AI wrote it. It must return specific, named objections tied to a
location in the draft — "consider tightening the middle" doesn't count as a
finding.

Only named, specific objections from either pass become revision targets.
After step 7's revision, re-run the adversarial pass once more against the
revised draft to confirm the fix actually landed rather than trusting that it
did — a revision can fix the flagged issue while introducing a new one, and
the only way to know is to check again with the same blind rigor.

Reserve the full multi-agent adversarial-verification pattern (several
independent skeptics voting) for higher-stakes review work — one blind pass is
proportionate here; a swarm is overhead a single piece doesn't need.

### 7. Revise

Address only what step 6 flagged. Don't re-litigate decisions the critique
didn't raise a problem with — targeted revision, not a rewrite.

### 8. Run the writing skill suite

Invoke `rl-writing-craft`'s full sequence — `structure` → `edit` → `audit` →
`copyedit` — against the revised draft. Then, if you have a closing polish
skill (e.g. `ann-handley-voice`), run it on venture/brand content — skip this
sub-step entirely if you don't have one; `rl-writing-craft`'s `audit` already
provides the floor, a closing polish skill is a bonus layer on top of it, not
a requirement. For your own raw personal voice, skip the polish pass unless
you ask for it or type its trigger phrase — your voice outranks the
framework, per your content-generation skill's existing rule.

### 9. Refine

Fold in whatever the suite pass surfaced. Do one last signal check across the
whole piece: does every section still carry at least one concrete,
non-generic detail from step 2, or did a revision pass quietly sand it back
down to something that could describe any company? Flag any section that
reads generic and fix it before moving on — this is the same check the suite
audit runs, done once more at the whole-piece level.

### 10. Approve

Present the finished piece as a decision point, not a delivery. This step
exists specifically so nothing gets treated as publishable — posted, sent,
shipped — until you've actually said so. If the request came in with an
implicit "and then post it," that posting step still waits for explicit
confirmation here; this skill only produces the approved draft.

## Notes

- This skill assumes a lane architecture — a router/generator skill, a craft
  skill, a polish skill — like the one your content-generation skill
  documents in its own "Orchestration & Lanes" section. Read that section
  first if the lane boundaries are unclear.
- If a step's output already exists (you hand over a topic *and* a brief,
  say), don't redo the work — confirm it's still current and move to the next
  step.
- A deterministic entry point for this sequence is the `/longform` command.
