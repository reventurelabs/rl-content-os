---
name: rl-review-panel
description: "Blind review panel for finished content drafts — articles, posts, newsletters, emails, case studies, web and landing copy, decks, scripts, announcements. Several independent lenses (Architect, Checker, Stranger, Conscience, plus a Storyteller for narrative pieces) each read the draft cold, in their own context, and return diagnoses, never rewrites; a non-voting Keeper states what the piece is before they read and merges their findings after, filtering out anything that would turn the piece into something other than a better version of itself. Runs as the panel pass in rl-content-pipeline's step 6, or standalone via /panel. Trigger on 'panel review,' 'run the panel,' 'review this draft,' 'what would an editor say.' Content only: not for strategy documents, brand foundations, positioning or messaging frameworks, voice profiles, briefs, or plans. Cites rl-writing-craft's rules; never restates them. Does not do line editing, copyediting, or the anti-AI sweep — rl-writing-craft does."
license: MIT
---

# Review Panel

A panel of blind readers for a finished content draft. Each lens asks one question of the whole
piece, from one side. None of them writes a fix. The writer — or the author-voice layer — writes
the fix, so revisions stay in the writer's register instead of drifting toward the panel's.

One rule governs every finding: **it must make the piece a better version of what it already is,
not turn it into something else.** (Robert Gottlieb's test, from his criticism of editors who
rewrote writers toward their own aesthetic.) The panel serves many writers with different voices;
it critiques without homogenizing.

The rules the lenses enforce live in `rl-writing-craft`. A lens names the rule it is applying; it
never restates it. If you find yourself writing a rule into a finding, stop and cite it instead.

---

## Scope: content only

**Reviews:** content meant to be read by an audience — articles, blog posts, essays, newsletters,
emails, case studies, landing and web copy, sales and pitch decks, scripts, press releases,
social posts, announcements.

**Does not review:** strategy documents; brand foundations (brand story, positioning, messaging
frameworks, audience definitions, content playbooks); voice profiles and `AUTHOR-CONTEXT.md`;
briefs, outlines, and plans. Those are inputs the writer decides, not drafts an audience reads,
and the lenses below would judge them against the wrong standard. If asked to panel one, say so
and stop.

---

## When it runs

- **In `rl-content-pipeline`, step 6** — the panel pass, alongside the judge, adversarial, and
  fact-check passes. See that skill for how the passes fit together.
- **Standalone, via `/panel`** — on any content draft.

**Never from the context that drafted the piece.** Self-review by the drafting context is the
weakest possible judge (`rl-content-pipeline`, step 6). Every lens runs in a fresh context.

**Inputs:** the draft; the brief if one exists; `AUTHOR-CONTEXT.md`; the author-voice skill or
`VOICE-PROFILE.md` if present. Nothing about how the draft was produced. The brief goes to the
Keeper only; the lenses get the Keeper's statement of it, so they judge the piece on the page
rather than the plan behind it.

---

## The Keeper (chair, non-voting)

The Keeper owns voice and intent. It does not judge prose quality and never blocks a HARD STOP on
voice grounds. It runs in a fresh context too — never the drafting one. Under `--light`, the one
fresh agent that runs the lenses also plays the Keeper.

**Opens — once per piece, before any lens reads.** A short statement every lens receives:
- **What the piece is:** form, audience (from `AUTHOR-CONTEXT.md` or the brief), purpose.
- **Voice markers:** the deliberate features of this writer's voice, from the voice profile —
  signature phrases, fragment habits, sentence shape, register, profanity, anything the profile
  marks as chosen. Mark aspirational items as such; they are never grounds for a finding.
- **Narrative or not:** whether the Storyteller is seated.

In the pipeline, write it from the brief (step 3) and the voice profile; don't re-derive it.

**Closes — after every lens reports.** Consolidate (see Output), then run the voice check after
revision (see Deferring to Voice).

---

## The Lenses

Each lens is defined by its question, the signature questions it reads with, the rules it cites,
and what it must not do. The signature questions come first: they are how a good editor reads.
The rules are how the finding gets checked.

### Architect — structure, stakes, and promises
**Question:** does every part earn its place, in this order, for this reader?
**Reads with:** What is at stake, and for whom? Where does the reader first learn the point — and
is that where it should be? If this section went, what would the reader lose? Does the title
promise what the piece delivers? Is the best material buried late?
**Cites:** `structure.md` → Stakes · Titles · Opening · Flow and Section Logic · The Close ·
Format Defaults.
**Must not:** impose one template on every genre (answer-first suits a memo, not an essay or a
story); line-edit; change the piece's form or intent.

### Checker — claims and evidence
**Question:** does the evidence support each claim at the strength it's stated?
**Reads with:** Who says so, and what exactly did they say? How could the writer know this? Is
this claim stronger than its source? What's the denominator behind "most"?
**Cites:** `edit.md` → Grounding Rules · `audit.md` → vague attribution · `SKILL.md` → Logical
Consistency (personal vs. sourced knowledge; causal chains that swap their terms).
**Note:** the pipeline's fact-check pass decides whether a claim is *true*. The Checker judges
whether it is *stated* at the strength the evidence carries.
**Must not:** demand citations in genres that don't carry them — it asks for verifiability, not
footnotes; treat labeled opinion as a factual claim.

### Stranger — the reader's side of the page
**Question:** can a smart newcomer follow this, trust it, and not feel talked down to?
**Reads with:** Who is this, and why should I know them? What step did the writer skip because it
felt obvious? Where did I have to reread? Is this one thing or several things with different
names? Where did the writer explain what I already know?
**Cites:** `edit.md` → Reader Access · Orient Before You Move · Audience Calibration ·
`SKILL.md` → Logical Consistency (antecedents, definite references).
**Must not:** flatten specialist writing for a specialist audience — read `AUTHOR-CONTEXT.md`
first; simulate a specific customer persona's reaction (that's an audience-persona review, not
this one).

### Conscience — honest persuasion
**Question:** does this persuade by honest means?
**Reads with:** Would this framing survive the reader learning the whole truth? What happens if
the reader waits a month? Is emotion showing the stakes or replacing the argument? Would the
writer be comfortable if the reader saw exactly how this was built?
**Cites:** `edit.md` → Persuasion Integrity · Manufactured vulnerability · Exclamation points ·
`audit.md` → significance inflation.
**Must not:** ban emotion, story, or strong opinion; moralize at the writer; judge factual truth
(the Checker's job).

### Storyteller — seated for narrative pieces only
Case studies, customer and brand stories, founder narratives, memoir, fiction.
**Question:** does the story work as a story?
**Reads with:** Who wants what, and what's in the way? Where would the reader want to be in the
room? Whose eyes are we looking through? Does the ending pay off what the opening set up? Who
changes — the customer, or the brand?
**Cites:** `structure.md` → Narrative Pieces · `edit.md` → Grounding Rules (invented interiority,
manufactured experience).
**Must not:** invent scene detail or interiority — it asks; push a non-narrative piece into story
form.

### Not seated, on purpose
- **Line-level cutting, rhythm, and specificity** — `rl-writing-craft`'s `edit` pass. In the
  pipeline it runs at step 8, after revision; a line lens at step 6 would judge sentences the
  revision is about to rewrite.
- **The anti-AI sweep and copyedit** — `rl-writing-craft`'s `audit` and `copyedit`, last.
- **The hostile skeptic** — the pipeline's blind adversarial pass already exists; keep it separate.
  It reads the whole draft trying to kill it; the lenses read it from defined sides. They catch
  different things.

---

## Findings

Two kinds of finding count. Anything else is dropped.

- **Rule finding** — names the `rl-writing-craft` rule it enforces.
- **Reader-response finding** — reports an observable effect on the reader, quoted to the place it
  happened: *I reread this. I lost the thread here. I didn't know who this was. I stopped caring
  here. I couldn't tell what this promised.* It must also name what the reader was missing or what
  caused the effect — the undefined term, the absent premise, the repeated point — so the writer
  can check it. An effect on a reader, with its cause, is evidence of a flaw even when no rule
  names it. An effect with no nameable cause is taste; drop it.

**Dropped:** a finding that prescribes a style without a reader effect or a rule — "this would be
punchier as…," "consider a more formal tone." That's taste, and taste belongs to the writer.

Every finding uses this format:

```
[LENS] Stranger
[KIND] rule | reader
[LOCATION] "short quote from the draft"
[BASIS] edit.md → Reader Access → Undefined insider term   (rule findings)
        or: the reader effect, in one line                (reader findings)
[SEVERITY] P0 | P1 | P2
[FINDING] one sentence naming the problem
[DIRECTION] a question for the writer, or a direction for the fix — never a rewrite
```

**Severity.** LLM critics asked to find problems over-find them and inflate severity (see
`docs/research/2026-09-28-llm-review-panel-evidence.md`), so the scale is anchored and P0 is narrow.

| Severity | Means | Only when | Anchor example |
|---|---|---|---|
| **P0** — blocks publishing | The reader would come away believing something false, or be persuaded by a manipulative frame | The finding cites a HARD STOP rule, **or** it shows the passage leaves the reader with a false belief about the subject | "Most teams report 40% faster onboarding" with no source (Population quantifiers); a deadline that doesn't exist (Manufactured urgency); the page says the suite has five skills when it ships six |
| **P1** — fix before publishing | The reader stumbles, loses the thread, or trusts the piece less; the piece works worse than it should | STRONG FLAG rules, `structure.md` checks (stakes, titles, opening, flow, close, narrative), and Logical Consistency errors that confuse without misleading | "That problem" pointing back to a problem never named; the same point made in three sections; an undefined acronym |
| **P2** — fix when time allows | A real but small cost | MINOR rules; anything a reader would notice only on a second read | Condescending "simply"; a buried verb |

Logical Consistency errors are P1 by default — they still block publishing, but a dangling
antecedent is not a false claim. They rise to P0 only when the error leaves the reader believing
something false (a recap that silently drops the case the piece is about, a causal chain that swaps
its terms). A reader finding takes the severity of the nearest rule, or P1 if the reader stops
following the piece, P2 otherwise. **When in doubt between two levels, take the lower.** A P0 needs
its reason stated in the `[FINDING]` line: which HARD STOP, or what false belief.

**At most six findings per lens,** most severe first. "Clean for this lens" is a complete and
often correct answer — say it in one line. Never invent findings to look thorough.

**Ask, never supply.** When a fix needs something only the writer has — a source, an example, the
missing step, the real stakes — the direction is a question. A lens that invents the missing
detail commits the Grounding Rules violation it exists to catch.

---

## How it runs

**Default: blind and parallel.** Each seated lens runs as its own fresh sub-agent, all at once.
Each receives the draft, the Keeper's opening statement, `AUTHOR-CONTEXT.md`, and the voice
profile — not the other lenses' findings, not the brief's history, not the drafting conversation.
Independence is the point: no lens sees another's work, and lenses never debate — debate makes
models abandon correct findings to agree, and plain aggregation captures most of what it adds.

**Model family.** Where the platform lets you choose, run the lenses, the verifier, and the Keeper
on a different model family from the one that drafted the piece: judges rate their own family's
writing higher. A different family does not remove the wider bias toward smooth, predictable text,
so the Keeper still never ranks a finding up because its fix would read more smoothly. When every
agent is the drafter's family — sub-agents in Claude Code are Claude — say so in the output
("same-family review").

**Verify before the writer sees it.** After the lenses report and before the Keeper consolidates,
one more fresh agent — the verifier — takes every P0 and P1 finding and re-reads the draft at the
quoted location. For each: **confirmed** (the problem is there as described), **downgraded** (real
but at a lower severity — say which), or **rejected** (the quote doesn't show it, the rule doesn't
apply, or the finding breaks a lens's *must not*). The verifier sees the findings and the draft,
not the lenses' reasoning, and applies the severity table above. Rejected findings are dropped and
counted in one line; downgraded ones take the new severity. Skip the verifier only under `--light`.

**`--light`:** one fresh agent (never the drafting context) runs every seated lens in turn,
reporting each in its own section. Cheaper and less independent; use it when sub-agents aren't
available or the piece is short.

The panel advises. The only gate is the writer's approval (`rl-content-pipeline`, step 10).

---

## Output — the Keeper's consolidation

The writer reads this, not the raw lens reports. Forty findings is an audit; ten is an editor.

1. **Merge duplicates.** Same passage, same problem, different lenses → one item, listing every
   lens that raised it.
2. **Drop** taste findings (see Findings) and anything that violates a lens's *must not*.
3. **Rank:** every confirmed P0 first; then confirmed P1s; then P2s. Within a level, an item raised
   by lenses on **different model families** ranks first. Agreement between lenses on the same
   model is noted ("raised by Architect and Stranger") but not ranked up: models share blind spots,
   so same-model agreement is weaker evidence than it looks.
4. **Present:**
   - **Blockers** — every P0, in full.
   - **Top items** — up to ten more, in full, in rank order.
   - **Everything else** — one line each, below.
   - **Forks** — conflicts the precedence below can't settle, as both findings plus the Keeper's
     recommendation. The writer decides.
   - **Clean lenses** — one line naming them.
   - **Verification** — one line: how many findings were confirmed, downgraded, and rejected.
   - **Review family** — one line: which model family ran the panel, and "same-family review" if
     it matches the drafter's.

### When lenses conflict

Precedence, highest first:
1. **HARD STOP findings, from any lens.** Voice can't justify a false claim or a manipulative frame.
2. **Claim and persuasion flags (Checker, Conscience, P1).** Voice can soften how a claim is put,
   never let it stand at a strength the evidence doesn't carry.
3. **Reader access (Stranger).** Beats economy: context the reader needs stays.
4. **Voice (Keeper).** Beats structure and economy on register, rhythm, and form.
5. **Structure (Architect, Storyteller).** Section decisions before sentence decisions.

---

## Deferring to voice

1. **Diagnose, don't rewrite.** Directions, not replacement text.
2. **Check the markers first.** A voice marker from the Keeper's statement can be flagged for
   overuse, never for existing.
3. **Deliberate or default?** Flag unchosen habits, not choices. Short sentences aren't a flaw in a
   writer whose profile says short sentences; a pile-up past that writer's own norm might be.
4. **Voice check after the last rewrite.** Once revision and the writing suite are done (pipeline
   step 9; standalone, after the writer's revision), the Keeper checks voice two ways, because an
   LLM reading for voice shares the bias toward smooth, generic text that flattens it:
   - **Measured.** Run `voice_metrics.py` (in the `rl-voice-discovery` skill folder) on the draft
     before revision and after, against the `VOICE-PROFILE.md` Measured Baseline or the writer's
     samples: `python3 voice_metrics.py --baseline VOICE-PROFILE.md before.md after.md`. Name every
     metric where the revision moved *away* from the writer's baseline — shorter sentence spread,
     lost contractions, vanished dashes, flattened hedging. A move away is a question for the writer,
     not a verdict: a revision can drift for a good reason (cutting a filler word the writer
     overuses). If the script or a baseline isn't available, say so and rely on the read.
   - **Read.** Every changed passage against the profile — its Distinctive Elements, Critical Voice
     Guidelines, and Corrections, plus the writer's own samples if they're at hand: does this still
     read like the author, or like competent neutral prose?
   Name any passage that drifted. With no voice reference at all, skip the check and say so. Two
   limits:
   - **Never undo a HARD STOP fix** to restore voice. Flag the passage for the author-voice layer
     to re-voice the corrected text instead.
   - **Never add voice markers to pass the check.** Inserting a signature phrase into a section
     that lost its voice is manufactured personality, which `rl-writing-craft` forbids. The fix is
     to re-voice what's there, in the author-voice layer.
5. **No proxy voice.** No lens uses one writer's preferences as the standard for another's work.

---

## Revision limits

The writer accepts or rejects every change a panel finding leads to — changes are presented as a
list, each tied to its finding, not folded silently into a new draft. And the loop is short: **one
revision, one re-check, then stop.** Critique-and-revise gains come in the first round or two;
further rounds drift toward generic prose. A P0 still open after the re-check goes to the writer as
a fork; the panel does not run again on its own.

---

## Recurring findings

The panel keeps no memory between pieces. When a finding is one the writer recognizes as
recurring — they say it keeps coming up, or the same correction appears in this session's earlier
pieces — the Keeper proposes a durable entry under `rl-content-pipeline`'s *Capturing durable
preferences* routing — word
choice and register to `VOICE-PROFILE.md` → Corrections, structural or scope preferences to
`AUTHOR-CONTEXT.md` → Redirections. The writer approves every entry; the panel never writes to
either file on its own.

---

## What this skill does not do

- Rewrite, line-edit, copyedit, or run the anti-AI sweep — `rl-writing-craft` does.
- Verify facts against sources — the pipeline's fact-check pass does.
- Gate publishing — the writer's approval does.
- Review strategy, foundations, voice profiles, briefs, or plans — see Scope.
- Simulate a specific audience's reaction — that's an audience-persona review.

---

## Sourcing note

The lenses are modeled on editorial practice, not invented roles: Gottlieb's "better version of
what it already is" and Maxwell Perkins's "the book belongs to the author" (the Keeper); Barbara
Minto's answer-first structure for argument formats and George Gopen's reader-expectation work
(the Architect); The New Yorker's checking tradition (the Checker); Steven Pinker on the curse of
knowledge and Tracy Kidder and Richard Todd's "to write is to talk to strangers" (the Stranger);
Orwell's "Politics and the English Language" and Kidder and Todd on trustworthiness (the
Conscience); Kidder and Todd on stakes and point of view and Ursula K. Le Guin's *Steering the
Craft* (the Storyteller). Several quotations reached the research through secondary sources.
