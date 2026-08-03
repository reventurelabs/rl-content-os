---
name: rl-content-pipeline
description: >-
  Structured 10-step writing process for long-form content (blog posts,
  whitepapers, essays, case studies, past ~800 words) OR high-stakes content
  regardless of length (a statement under the company's name, an
  announcement with no room to walk back a bad framing) — cost-of-being-wrong
  is the real criterion, length is only a proxy. Orchestrates existing
  writing skills (content-generation and author-voice for generation,
  rl-writing-craft for structure/edit/audit/copyedit, plus an optional
  closing polish skill e.g. ann-handley-voice) — sequences them, does not
  duplicate their rules. Adds what a single draft skips: define
  topic/angle/goal, interview the SME, write a brief, outline, draft section
  by section, review against the brief, revise, run the writing suite,
  refine, get explicit approval. Trigger on "blog post," "whitepaper,"
  "essay," "long-form," "this needs to be right." For low-stakes quick-turn
  formats (routine LinkedIn post, email, social copy) use content-generation
  or author-voice directly.
---

# Content Pipeline — Structured 10-Step Writing Process

An orchestrator, not another generator. This skill owns **sequencing**
for long-form or high-stakes pieces; it borrows every actual writing rule from
the skills that already have them:

- **your content-generation skill** / **your author-voice skill, if you have one** — generation, voice. "Your author-voice skill" resolves to an actual installed skill if you have one, or to `VOICE-PROFILE.md` at the repo root directly (produced by `rl-voice-discovery`) if that's what exists instead — check for the file before concluding there's no voice reference at all.
- **rl-writing-craft** — structure, grounding (Grounding Rules), line edit, anti-AI audit, copyedit. Always present — this is the one dependency that isn't optional.
- **an optional closing polish skill, if you have one** (e.g. ann-handley-voice) — a final voice/readability pass on top of rl-writing-craft's floor. Not required — skip this if you don't have one.

This skill assumes a lane architecture — a router/generator skill, a craft
skill, a polish skill — with the lane boundaries as listed above. If your
content-generation skill documents its own orchestration rules, defer to
those wherever the boundaries seem unclear.

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
- **High-stakes, regardless of length** — a 150-word statement carrying the
  company's name, a short email where the wrong claim damages a
  relationship, an announcement whose bad framing can't be retracted once
  it's out. The interview, brief, and adversarial review steps catch exactly
  the mistakes that are cheap to fix here and expensive to fix after it's
  sent.

For a LinkedIn post, a routine email, or social copy that's genuinely
low-stakes — the kind where a bad opening line costs you nothing but a
slightly weaker post — go straight to your content-generation or author-voice
skill. Running all 10 steps there is pure
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

If the topic came from `rl-topic-scout`, it already carries this from the
shortlist. Otherwise, check `AUTHOR-CONTEXT.md` at the repo root for who this
piece is for and why it's worth writing at all — same file `rl-topic-scout`
reads, kept consistent so "who I write for" doesn't drift between the two
skills. If it's still the unfilled template, `rl-context-discovery` builds it
properly (evidence first, then a guided interview) rather than a one-off
question here.

### 2. Interview the SME/author

Adaptive, based on who the expertise belongs to:

- **The writer is the SME** (most of their own ventures/projects) — a short,
  pointed interview. Ask 2-4 open-ended questions aimed at surfacing the
  specifics a draft would otherwise invent or skip: a real example, a number,
  a position you'd defend, something that didn't work. Don't ask what's already
  answered by step 1.
- **A named third party is the SME** (a client, a guest expert, a partner) —
  a fuller interview. Ask open-ended questions so they can surface
  things you wouldn't have thought to ask about, and explicitly ask them to
  quantify or define anything they state in vague or abstract terms. Record
  what they say rather than paraphrasing from memory.
- **A voice memo, dictated stream-of-consciousness, or existing meeting
  transcript** (e.g. a Granola recording) is a valid interview answer in its
  own right — often lower-friction and more specific than typed answers,
  since talking through an idea surfaces the real example or the actual
  number faster than composing it in writing. If one already exists for this
  topic, use it directly as raw material instead of asking the person to
  re-type answers to questions it already answers.

In every case, this step's output is raw material — quotes, numbers, opinions,
examples — not prose. That material is what step 5 draws on instead of
inventing connective filler.

**Optional: outside validation.** Off by default — offer it, don't run it
automatically. When the angle rests on a claim about what people currently
think, want, or are struggling with (not just on the author's own
experience), ask whether it's worth checking against outside discourse
before writing. If a recent-discourse research skill is installed (e.g.
`last30days-skill`, installable via `npx skills add mvanhorn/last30days-skill`),
use it to check current discussion on the topic — does the angle hold up
against what people are actually saying, or is it a stale take a week of
real discourse would contradict? If no such skill exists, continue without
it — this is a strengthening step, never a blocker.

### 3. Creative brief / executive summary

Synthesize steps 1-2 into a short brief: objective, audience, key message(s),
success criteria (what does this piece need to do to have worked), non-goals
(what it's deliberately not trying to do), and a voice reference — point at
your content-generation skill's venture/audience context or your author-voice
profile, don't restate their rules here. Show the brief and get one
confirmation before moving on — a quick yes/adjust, not a document review.

### 4. Outline with talking points

Build the H2/H3 structure: each section's job, its key talking points, and
which specific example or data point from step 2 belongs where. This is the
cheapest point in the whole process to catch a shape problem — get it
approved before writing a single section. If the writer redirects the
outline, that's the process working, not a delay.

### 5. Draft section by section

Section by section means a review checkpoint per section, not just an
authoring order. Draft one outline item, show it, and let the writer (the human you're
working with) react before moving to the next — the same approval-gate
pattern as step 4's
outline, applied one level down. Writing the whole piece in one continuous
pass and calling it "section by section" because you moved through the
outline in order skips the actual point: catching a section-level problem
(wrong angle, missing specific, wrong register) while it's cheap to fix,
instead of after it's already propagated into every section that followed
it or been buried in a full-piece review at step 6.

For each section: use your content-generation skill's rules for venture/brand
content, or your author-voice skill directly for personal-voice pieces. Pull
the specifics surfaced in step 2 into the section where the outline placed
them. Follow `rl-writing-craft`'s Grounding Rules throughout — never invent
scenes, specifics, or claims about real people; leave a gap and flag it
rather than papering over it.

Exception: for a short piece where the outline is only two or three sections,
or when the writer explicitly says to draft the whole thing and they'll
react to it as one piece, skip the per-section checkpoint — the overhead
isn't earned at that scale. Default to per-section review; drop to a single
pass only on explicit signal.

### 6. Review the draft against the brief

Three distinct passes, not one vague "review." A single self-review from the
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

**Fact-check pass (verify against sources).** Independent of both passes above —
this one checks accuracy, not shape or argument. List every checkable claim in
the draft: a stat, date, name, quote, or attributed study. Verify each against
an independent source (web search/fetch tools, if available in the current
session). `rl-writing-craft`'s Grounding Rules already stop the model from
*inventing* a claim; this catches the different failure of a claim that's real
but wrong — a source misremembering a percentage, a stat quoted from a
secondary write-up that misstated the original. Where a claim checks out, move
on. Where it's wrong, note the correct figure. Where it can't be verified
either way, flag it for the writer rather than publishing it unchecked or
quietly cutting it — the writer may have a source the search didn't surface.
If no search/fetch capability is available in the session, say so and flag
every checkable claim for the writer's own verification instead of skipping
the pass silently.

Only named, specific objections from any of the three passes become revision
targets.

**Re-check (after step 7).** After step 7's revision, re-run the adversarial
pass once more against the revised draft to confirm the fix actually landed
rather than trusting that it did — a revision can fix the flagged issue while
introducing a new one, and the only way to know is to check again with the
same blind rigor. Re-verify the fact-check pass too, but only for claims the
revision actually touched or added — re-running it against unchanged claims is
wasted work.

Reserve the full multi-agent adversarial-verification pattern (several
independent skeptics voting) for higher-stakes review work — one blind pass is
proportionate here; a swarm is overhead a single piece doesn't need.

### 7. Revise

Address only what step 6 flagged. Don't re-litigate decisions the critique
didn't raise a problem with — targeted revision, not a rewrite. After
revising, return to step 6's adversarial pass once (see Re-check).

### 8. Run the writing suite

Invoke `rl-writing-craft`'s full sequence — `structure` → `edit` → `audit` →
`copyedit` — against the revised draft. Then, if you have a closing polish
skill (e.g. `ann-handley-voice`), run it on venture/brand content — skip this
sub-step entirely if you don't have one; `rl-writing-craft`'s `audit` already
provides the floor, a closing polish skill is a bonus layer on top of it, not
a requirement. For raw personal voice, skip the polish pass unless the
writer asks for it or types its trigger phrase — the writer's voice outranks
the framework, per your content-generation skill's existing rule. If no
content-generation skill is installed, the rule defaults the same way: skip
the polish pass for personal voice unless the writer asks.

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
shipped — until the writer has actually said so. If the request came in with an
implicit "and then post it," that posting step still waits for explicit
confirmation here; this skill only produces the approved draft.

## Capturing durable preferences

Corrections and redirections happen throughout this process — at the
interview, on the outline, mid-draft, during revision. Most are specific to
the piece at hand and don't need to outlive it. Some aren't: a word the
writer never wants used again, an insistence that a process gets explained
in a particular order, a scope call ("this framing is optional, not
required") that will come up on the next piece too. The test is simple —
would this same correction be worth making again on a *different* piece,
about a *different* topic? If yes, it's durable; write it down before the
session ends, don't rely on remembering it next time.

A fact isn't a preference, even when it shows up as a correction. If the
writer fixes something because a draft got a detail wrong (mischaracterized
how a tool works, misstated a number, described a step incorrectly), that's
a one-time accuracy fix — fix it in the piece and move on. It doesn't
belong in either file below, and forcing it in as if it were a style
preference is itself the kind of error this section exists to prevent. The
signal isn't "was I corrected" — it's "would the *same* correction apply to
unrelated future work."

Route durable ones by type, immediately, not batched at the end:

- **Word choice, phrasing, register** — append to `VOICE-PROFILE.md`'s
  Corrections section, if that file exists. ("Whomever" → the writer wants
  plain word choice, not formal correctness, is this kind of entry.)
- **Everything else genuinely durable** — how a process should be
  explained, what stays optional versus load-bearing, a structural or scope
  preference that will recur across unrelated pieces — append to
  `AUTHOR-CONTEXT.md`'s Redirections section.
- **Neither file exists yet?** Note the correction inline in this session
  and mention that running `/voice` or `/context` would give it a
  permanent home — don't block on it, and don't invent a file structure to
  hold it instead.

Each entry: what the correction was, and why, in one or two lines — enough
for a future run to apply it without re-deriving the reasoning. Don't wait
for the writer to ask for this explicitly; recognize a durable correction
when it happens and capture it as part of doing the step, the same way a
grounding-rule flag gets surfaced without being asked for. If genuinely
unsure whether a correction is durable or one-off, ask rather than guess —
but don't ask about every edit; that's friction the writer didn't sign up
for.

This is not a substitute for a fuller, continuously-evolving author-voice
skill — it's the same idea `rl-voice-discovery` already names as the thing
that outperforms a one-time discovery pass, given a concrete mechanism
instead of staying aspirational.

## Notes

- If a step's output already exists (you hand over a topic *and* a brief,
  say), don't redo the work — confirm it's still current and move to the next
  step.
- A deterministic entry point for this sequence is the `/pipeline` command.
