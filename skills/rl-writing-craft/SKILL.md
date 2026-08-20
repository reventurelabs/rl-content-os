---
name: rl-writing-craft
description: "Self-contained writing-quality skill with four functions: structure (architecture, flow, openings, closes), edit (line-level cutting, grounding, rhythm, anti-AI removal woven in), audit (dedicated anti-AI pattern sweep), and copyedit (grammar, punctuation, usage, consistency, proofreading). Use whenever writing or editing prose — articles, posts, essays, emails, reports, any written content. Invoked generically ('edit this,' 'tighten this,' 'make this better,' 'run the writing skill') it runs the full sequence: structure, edit, audit, copyedit. Single functions run by name: 'structure pass,' 'line edit,' 'anti-AI pass,' 'copyedit,' 'proofread,' 'check grammar.' General craft for any writer; layers under an author-voice skill which wins on register and rhythm. Copyedit corrects errors in service of voice, never imposing style rules a voice deliberately breaks. Does not set voice itself."
license: MIT
---

# Writing Craft — Structure, Edit, Audit, Copyedit

A general writing-quality skill. Four functions, each independently callable, defaulting
to a full sequence when invoked generically.

This skill does **not** set voice. Register, rhythm, and the things that make writing
sound like a specific person belong to the author-voice skill layered on top. This skill
shapes the architecture, tightens the lines, and removes machine-writing patterns. The
author-voice skill always wins where they touch the same sentence.

---

## The Four Functions

**1. `structure`** — Architectural editing. The bones. Where the piece opens, how it
moves, what each section does, how it closes. Run when a draft's argument is sound but
its shape is wrong, or before drafting to plan the build.

**2. `edit`** — Line-level editing. Readability, cutting, grounding, sentence rhythm.
Anti-AI pattern removal is woven through this pass — tells are cheapest to fix while
editing the line they live on. Run when a piece is structurally sound and needs tightening.

**3. `audit`** — Dedicated anti-AI sweep. Mechanical pattern detection run clean against
finished copy. Catches what survived the edit pass, including tells the editing itself
introduced.

**4. `copyedit`** — Grammar, punctuation, usage, consistency, and proofreading. The
mechanical-correctness layer a copyeditor and proofreader provide. Runs last, against
near-final copy. Corrects unambiguous errors only — it never imposes style rules the
author's voice deliberately breaks (fragments, sentence-initial conjunctions, etc.).

**Default: full sequence.** When invoked generically, run all four in order — structure,
edit, audit, copyedit. Name a single function to run it alone.

Each function's full rules live in its own file next to this one — see [Function
Reference](#function-reference) below. Load the file for the function you're running.

---

## Sequencing With an Author-Voice Skill

The full pipeline, when a voice layer is present. The voice layer is your
content-generation skill (venture/brand lane) or your author-voice skill (personal lane)
— two distinct optional roles; the sequence is the same for both:

1. **Draft** — content produced
2. **Voice layer** — sets register and rhythm (your content-generation skill or your
   author-voice skill)
3. **`structure`** — shapes the architecture
4. **`edit`** — tightens lines, removes tells, applies grounding rules
5. **`audit`** — final mechanical sweep
6. **`copyedit`** — grammar, punctuation, usage, consistency, proofreading (errors only)

The voice layer runs first because voice decisions shape what the structure should be.
The audit runs last because it catches tells introduced by every prior pass. If no
author-voice skill is present, check for `VOICE-PROFILE.md` at the repo root (produced by
`rl-voice-discovery`) before concluding there's no voice reference at all — treat it the
same as an author-voice skill would be treated in step 2. Only with neither present does
this skill run with no imposed register.

(The step-by-step mechanics of the four-function run live in "Running the Full Sequence"
near the bottom of this file.)

**Carve-out:** Intentional structural techniques are not AI tells. Section breaks (`* * *`),
one-sentence paragraphs for percussion, sentence fragments for rhythm, em-dashes as breath
marks, a cold open that drops the reader into the middle of something — these are craft, not
machine patterns. Do not flag them. Flag only *overuse* (e.g. em-dashes above ~1 per 1,000
words in body prose), never the technique itself.

---

## Logical Consistency — Grave Errors

Separate from structure and line quality: does the argument actually hold together? Treat
every item below as a blocking error, not a style preference — smooth prose can still be
logically broken, and that's a worse failure than awkward prose, because it survives every
pass that only reads for tone.

- **A label must match what it does.** If a passage is called a "test," it has to function as
  one — a procedure the reader could run. If it's actually a description, an account, or a
  framework, name it that instead. (Example: "the cleanest test I know" introduced
  two conditions to weigh, not a procedure — fixed to "the clearest account I've found.")
- **A recap must cover what it claims to recap.** When a section establishes multiple
  failure modes, causes, or conditions, any later diagnostic or summary invoking that same
  framework must include all of them — especially the one the piece's own central example
  demonstrates. Silently dropping one is a logical gap, not a trim. (Example:
  Hogarth's framework named feedback that's late, missing, *or drowned in too much of it* —
  but the diagnostic recap later listed only the first two, omitting the exact failure mode
  the piece's opening story was about.)
- **Pronouns need an antecedent before they're used, not after.** "Arguing opposite sides of
  it" when "it" is named as "intuition" only in the following clause leaves the reader with
  nothing to attach the pronoun to in the moment they read it. This is a comprehension gap,
  not just a style nit. The same applies to **definite references** — "the structure," "this
  approach," "that problem" — which assert the noun was already introduced. A section *heading*
  does not count as that introduction: "Structure is what does the work" reads fine as a fresh
  claim under a heading, but "*The* structure is what does the work" points back at a body
  sentence that never ran. Drop the article, or introduce the noun in prose first.
- **Claims of personal knowledge vs. sourced knowledge must be accurate.** "The cleanest test
  I know" claims lived, personal ownership of something that was actually learned from
  research. That's a misattribution of where the claim's authority comes from, not a tone
  issue.
- **A causal or comparative chain can't quietly swap its terms.** If two distinct conditions
  are introduced (e.g., "the right training" vs. "the right environment"), later sections
  can't conflate them or leave it ambiguous which one a diagnosis is actually about.

Run this check on every pass, not just `copyedit` — a logical inconsistency can be introduced
during `structure` (a recap that outlives the framework it referenced) or `edit` (a fix to one
sentence that breaks a pronoun's antecedent two sentences later). Surface it explicitly even
when the surrounding prose reads cleanly.

---

## Function Reference

Each function's full rules live in its own file. Load the one you need; the whole
set does not have to be in context at once.

| Function | File | What it covers |
|---|---|---|
| `structure` | [structure.md](structure.md) | Opening, flow and section logic, the close, format defaults, output shape |
| `edit` | [edit.md](edit.md) | Cutting, Grounding Rules, throat-clearing, rhythm, vocabulary, lists, audience calibration |
| `audit` | [audit.md](audit.md) | Severity tiers, the two-pass method, output shape |
| `copyedit` | [copyedit.md](copyedit.md) | Grammar, punctuation, usage, consistency, proofreading, and what it never does |

The Grounding Rules in [edit.md](edit.md) are the ones other skills in this suite
cite by name — read that file before drafting, not just before editing.

---

## Running the Full Sequence

When invoked generically ("run the writing skill," "edit this," "make this better"), run all
four in order and return the result of each stage. (How this sequence slots under a voice
layer is covered in "Sequencing With an Author-Voice Skill" near the top of this file.)

1. **`structure`** — report architectural issues and apply agreed reorderings/cuts. If the
   structure needs the writer's decision (which of two openings, whether to cut a section),
   surface the fork with options rather than guessing.
2. **`edit`** — tighten every line, apply grounding rules, remove tells, fix rhythm. Surface
   grounding-rule flags for the writer's ruling.
3. **`audit`** — two-pass anti-AI sweep on the edited copy.
4. **`copyedit`** — final mechanical pass: grammar, punctuation, usage, consistency,
   proofreading. Errors fixed; possible voice choices flagged as questions, not overwritten.
   Runs last because it works against near-final copy.

Between stages, pause at genuine forks — a missing personal anchor, an unverifiable claim, a
choice between two valid structures. Don't fabricate to keep moving. A flagged gap the writer
fills beats a smooth invention.

**Replacement text inherits the check it replaced.** A fix applied mid-sequence — a line
rewritten because `edit` flagged it, a sentence swapped out during a later revision pass, a
rewrite made in response to the writer's own redirection — is new text, not a patch exempt
from scrutiny. Run it back through whichever check flagged the original problem, Grounding
Rules at minimum, before treating the fix as final. A rewrite that trades one violation for a
different one (a vague sentence replaced with a fabricated fact, a cliché replaced with an
unmeasured quantitative claim) is not a fix. Catching that is the same job `audit`'s two-pass
method already does for a whole draft — apply it to the one line that just changed, every time
a line changes after the first pass, not just at the end.

This holds above the line level too. A heading renamed mid-conversation, a section added or
reordered, a subtitle changed after the headings were already set — each of these is a
structural edit, and it inherits `structure`'s checks the same way a line inherits Grounding
Rules: run the heading-collision check and the paragraph-reshuffle test again against the
*whole* document, not just confirm the one changed piece reads fine on its own. An edit that
only checks itself, in isolation from what it now sits beside, is exactly how a heading rename
quietly collides with a heading three sections down that nobody re-read at the same time.

---

## What This Skill Does Not Do

- **Set voice register or rhythm signature** — that's the author-voice skill layered on top. This
  skill won't make writing sound like a specific person; it makes writing structurally sound,
  tight, grounded, and free of machine patterns.
- **Inject personality to defeat detection** — this skill cuts to what's earned; it never adds
  manufactured asides, vulnerability, or current-events backdrop to seem more human. Humanity
  comes from real specifics and a real voice (the author-voice skill's job), not from injected tics.
- **Fabricate to fill gaps** — flags missing anchors and unverifiable claims for the writer;
  never papers over them.
- **Make series or project-level architecture decisions** — those belong to the writer and
  the project brief.

---

## Sourcing Note

The structural principles (cold opens, callback discipline, closes that point forward instead
of summarizing) draw on general editing craft shared across journalism and writing-craft
traditions broadly — not any single author's specific named method. The anti-AI detection draws
on systematic pattern research. The copyedit function draws on standard usage and style
references (Strunk & White's *The Elements of Style*, the *Chicago Manual of Style*, Garner's
usage) — applied in service of voice, never over it. This is a general craft skill; it layers
under whatever author-voice or closing-polish skill is in use, and doesn't implement any one
person's specific named framework (a skill like `ann-handley-voice`, where one exists, is where
that layer belongs).
