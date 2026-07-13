---
name: rl-context-discovery
description: >-
  Use when `AUTHOR-CONTEXT.md` is still the unfilled template, someone asks
  "help me figure out who I'm writing for," "why do I even write," "what
  should I actually be writing about," or when
  `rl-topic-scout`/`rl-content-pipeline` note the context isn't set
  up yet. Builds or refreshes `AUTHOR-CONTEXT.md` — who you are, who you
  write for, why you write, what "worth publishing" means to you — by
  checking existing
  evidence first (an about page, previously published content,
  README/CLAUDE.md files) and then running a guided interview specifically
  designed to get past generic, socially-acceptable answers (especially for
  "why do you write," which almost everyone answers with a
  marketing-flavored non-answer on the first try). Validates the draft
  against a hypothetical ranked topic shortlist before finalizing. This is
  the guided version of the "ask once, persist the answer" fallback
  `rl-topic-scout` already has — a one-time (or occasional refresh)
  discovery process, not a per-draft tool.
---

# Context Discovery

`rl-topic-scout` already has a thin fallback: if `AUTHOR-CONTEXT.md`
is blank, ask once and persist the answer.
That fallback is fine for someone who already knows exactly who they write
for and why. It's thin for everyone else, because "why do you write" is a
question almost everyone answers with a polished, generic non-answer on the
first try — not because they're being evasive, but because the honest
answer usually isn't the socially-presentable one. This skill exists to get
past that, the same way `rl-voice-discovery` gets past "how would you
describe your writing" by working from real samples instead of
self-description.

There's an asymmetry worth naming up front: voice can be extracted from
artifacts (real writing has the pattern whether or not the person can
describe it). Audience and motivation mostly can't — they live in the
person's head, not in a text you can analyze for tells. So this skill leans
harder on interview technique than `rl-voice-discovery` does, but it still
checks for real evidence first wherever evidence exists, for the same
reason: something you actually did is more reliable than something you say
about yourself in the abstract.

## Step 1: Check for existing evidence first

Before asking anything, look for material that already reveals part of the
answer:

- **A user-level or global CLAUDE.md, or a personal memory file** (e.g.
  `~/.claude/CLAUDE.md`, an existing memory system) — often already has
  real professional background or standing written down for Claude's own
  use, sitting there unused for this. Check it specifically for the "Who I
  am" section before running that part of the interview — it's usually the
  most direct source available, since it wasn't written to impress anyone,
  just to inform Claude.
- **An existing about page, bio, or company site** — often states an
  intended audience directly, even if in marketing language that needs
  translating into something more specific.
- **Previously published content** — what topics did they actually choose,
  in what formats, and (if visible) what got a real response versus
  silence. Actual choices are more reliable than stated preferences.
- **README / CLAUDE.md files** in relevant repos — often describe a
  project's purpose and intended audience implicitly, even when nobody
  wrote it down as "here's who this is for."
- **Any existing positioning material** — a brand brief, mission statement,
  elevator pitch, pitch deck. Treat these as a first draft to interrogate,
  not a final answer — positioning docs are often written for investors or
  customers, not as an honest account of who the writing itself is for.

If none of this exists, that's fine — proceed straight to the interview
with a blank slate. Note whether the result is evidence-informed or purely
interview-derived in the finished context file's source-note line (the
final italic line of the `AUTHOR-CONTEXT.md` template), the same way
`rl-voice-discovery` flags confidence level.

## Step 2: Interview for what evidence can't reveal

Four questions to answer, each with a specific technique for getting past
the generic first answer:

**Who are you?** Check step 1's evidence first — a global CLAUDE.md or
memory file often already answers this honestly, since it wasn't written
to impress anyone. If it's there, confirm it rather than re-asking from
scratch. If it isn't, resist the LinkedIn-headline answer. Not "a
consultant who helps companies do X" — that's positioning-speak, not
standing. Instead:
- "What do you actually spend your time doing, day to day, that your title
  doesn't capture?"
- "What do you know how to do — or have actually done — that most people
  writing about this topic don't?"
This is what gives the writing its authority: not a job title, a real
reason for the reader to trust what's being said.

**Who do you write for?** Push for distinctness, not a list. If there are
multiple audiences (several ventures, several publications, a personal
voice alongside a professional one), treat them separately. "Everyone who's
interested" is not an answer. Instead:
- "What does this audience specifically need that the others don't?" (asked
  per audience, not once for the whole list)
- "What's the one sentence that would make a wrong-audience reader
  immediately realize a piece isn't for them?"

**Why do you write?** The hardest one. Don't ask it directly first — it
invites a marketing answer. Instead:
- "What's actually stopping you from publishing more right now?" (surfaces
  the real obstacle, which is usually more honest than the stated
  motivation)
- "If nobody would ever see this, would you still write it? Why or why
  not?" (separates genuine motivation from audience-seeking)
- "What does writing get you that nothing else does?"
Only after one of these lands on something concrete, ask the direct
question again as a confirmation, not a first attempt.

**What does "worth publishing" mean to you?** Don't ask for a principle —
ask for cases:
- "Of the last five things you almost wrote about but skipped, which one
  do you regret skipping, and why didn't you write it?"
- "What's a piece someone else published that you wish you'd written —
  what made it land?"
The pattern across their actual answers is the real definition; a
principle stated in the abstract ("I only write about things I'm truly
passionate about") is usually too vague to rank anything against.

## Step 3: Draft AUTHOR-CONTEXT.md

Fill the first four sections — Who I Am, Who I write for, Why I write,
What "worth publishing" means to me — from steps 1 and 2 combined. Every
claim traceable to either real evidence or something the person actually
said in the interview; don't smooth a rough, specific answer into something
more generic-sounding on the way into the file. The rough version is
usually the useful one.

Leave the fifth section, Redirections, empty on a first write — it isn't
part of the interview. That section accumulates over time as
`rl-content-pipeline` captures durable corrections from real pieces (see
"Capturing durable preferences" there); this skill only creates the empty
section, it doesn't populate it.

## Step 4: Validate against a hypothetical ranking

Construct 2-3 candidate topics — real ones if there's a repo or recent work
to draw on, illustrative ones if not — and rank them according to the draft
context file. Show the ranking and ask directly: does this order feel right,
would you actually want to write the top pick before the others? A
correction here is higher-signal than anything from the interview, because
it's a reaction to a concrete ordering rather than a description of a
preference in the abstract. Fold in corrections; re-rank a second time if
the gap was significant.

## Step 5: Hand off

Once `AUTHOR-CONTEXT.md` is written and validated, it's live —
`rl-topic-scout` and `rl-content-pipeline` already read it, nothing
further to wire up. Mention that this is a snapshot, not a permanent
answer: ventures change, motivations shift, and nothing forces a refresh —
if the ranked shortlist from `/scout` (`rl-topic-scout`'s output)
starts feeling consistently off, that's the signal to run this again, not a
scheduled event.

## Notes

- A deterministic entry point for this skill is the `/context` command.
