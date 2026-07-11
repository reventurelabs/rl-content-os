---
name: rl-writing-craft
description: "Self-contained writing-quality skill with four functions: structure (architecture, flow, openings, closes), edit (line-level cutting, grounding, rhythm, anti-AI removal woven in), audit (dedicated anti-AI pattern sweep), and copyedit (grammar, punctuation, usage, consistency, proofreading). Use whenever writing or editing prose — articles, posts, essays, emails, reports, any written content. Invoked generically ('edit this,' 'tighten this,' 'make this better,' 'run the writing skill') it runs the full sequence: structure, edit, audit, copyedit. Single functions run by name: 'structure pass,' 'line edit,' 'anti-AI pass,' 'copyedit,' 'proofread,' 'check grammar.' General craft for any writer; layers under an author voice skill which wins on register and rhythm. Copyedit corrects errors in service of voice, never imposing style rules a voice deliberately breaks. Does not set voice itself."
---

# Writing Craft — Structure, Edit, Audit, Copyedit

A general writing-quality skill. Three functions, each independently callable, defaulting
to a full sequence when invoked generically.

This skill does **not** set voice. Register, rhythm, and the things that make writing
sound like a specific person belong to the author skill layered on top. This skill shapes
the architecture, tightens the lines, and removes machine-writing patterns. The author
skill always wins where they touch the same sentence.

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

---

## Sequencing With an Author Skill

The full pipeline, when an author voice skill is present:

1. **Draft** — content produced
2. **Author voice skill** — sets register and rhythm (e.g. sean-voice)
3. **`structure`** — shapes the architecture
4. **`edit`** — tightens lines, removes tells, applies grounding rules
5. **`audit`** — final mechanical sweep
6. **`copyedit`** — grammar, punctuation, usage, consistency, proofreading (errors only)

The author skill runs first because voice decisions shape what the structure should be.
The audit runs last because it catches tells introduced by every prior pass. If no author
skill is present, check for `VOICE-PROFILE.md` at the repo root (produced by
`rl-voice-discovery`) before concluding there's no voice reference at all — treat it the
same as an author skill would be treated in step 2. Only with neither present does this
skill run with no imposed register.

**Carve-out:** Intentional structural techniques are not AI tells. Section breaks (`* * *`),
one-sentence paragraphs for percussion, sentence fragments for rhythm, em-dashes as breath
marks, a cold open that drops the reader into the middle of something — these are craft, not
machine patterns. Do not flag them. Flag only *overuse* (e.g. em-dashes above ~1 per 1,000
words in body prose), never the technique itself.

---

# FUNCTION 1: `structure`

Architectural editing. The order, the shape, the joints. What goes where and why.

## Opening

The opening earns the read or loses it. Two patterns work:

**Cold open — drop into the middle of something.** A specific moment, an action already
underway, a claim already in motion. No throat-clearing, no context-setting, no "in today's
world." The reader assembles the frame from the first concrete detail.

**Declared verdict — state the position, then earn it.** The first sentence is the claim
the rest of the piece will defend. No windup, no question, no scene.

What never opens a piece: broad context before the point ("In the rapidly evolving
landscape of..."), a definition, a rhetorical question the reader can't yet care about,
a statistic before there's a reason to want it, or autobiography that hasn't earned its
place ("I've always been fascinated by...").

## Flow and Section Logic

Each section advances. Test every section against the one before it: does it add something
new — a turn, a complication, a deepening — or restate what's already established? If it
restates, cut it.

**The paragraph-reshuffle test.** Can you swap two body sections without breaking the piece?
If yes, the sections are modules, not an argument. A real argument has order — each beat
depends on the one before. Reorder or cut until the sequence is load-bearing.

**The treadmill test.** Ask of each paragraph: what's actually new here? If a paragraph
restates the premise in fresh words instead of moving the argument, it's spinning. If you
can cut 40–60% of a stretch and lose no information, the stretch was treadmilling.

**Restatement disguised as development.** The most common structural failure: after a
concrete scene or example proves the point, later sections restate that same point in the
abstract. The piece makes its case once vividly, then makes it again two or three times with
no new information — and sags in the middle-to-end. This usually happens because the abstract
version predates the concrete one in the draft and both got left in. When a strong concrete
beat is present, cut the abstract versions it replaces. They don't stack.

## Logical Consistency — Grave Errors

Separate from structure and line quality: does the argument actually hold together? Treat
every item below as a blocking error, not a style preference — smooth prose can still be
logically broken, and that's a worse failure than awkward prose, because it survives every
pass that only reads for tone.

- **A label must match what it does.** If a passage is called a "test," it has to function as
  one — a procedure the reader could run. If it's actually a description, an account, or a
  framework, name it that instead. (Caught in Article 3: "the cleanest test I know" introduced
  two conditions to weigh, not a procedure — fixed to "the clearest account I've found.")
- **A recap must cover what it claims to recap.** When a section establishes multiple
  failure modes, causes, or conditions, any later diagnostic or summary invoking that same
  framework must include all of them — especially the one the piece's own central example
  demonstrates. Silently dropping one is a logical gap, not a trim. (Caught in Article 3:
  Hogarth's framework named feedback that's late, missing, *or drowned in too much of it* —
  but the diagnostic recap later listed only the first two, omitting the exact failure mode
  the article's opening story was about.)
- **Pronouns need an antecedent before they're used, not after.** "Arguing opposite sides of
  it" when "it" is named as "intuition" only in the following clause leaves the reader with
  nothing to attach the pronoun to in the moment they read it. This is a comprehension gap,
  not just a style nit.
- **Claims of personal knowledge vs. sourced knowledge must be accurate.** "The cleanest test
  I know" claims lived, personal ownership of something that was actually learned from
  research. That's a misattribution of the claim's own epistemic status, not a tone issue.
- **A causal or comparative chain can't quietly swap its terms.** If two distinct conditions
  are introduced (e.g., "the right training" vs. "the right environment"), later sections
  can't conflate them or leave it ambiguous which one a diagnosis is actually about.

Run this check on every pass, not just `copyedit` — a logical inconsistency can be introduced
during `structure` (a recap that outlives the framework it referenced) or `edit` (a fix to one
sentence that breaks a pronoun's antecedent two sentences later). Surface it explicitly even
when the surrounding prose reads cleanly.

## The Close

The last line does something the second-to-last line cannot. It is not a summary, not a
recap, not a restatement of the opening.

Two closes that work:

**Return to the opening with new meaning** — the piece opened on something (a moment, a
person, a question); the close returns to it, but the reader now understands it differently
than they could have at the start.

**Forward pointer** — the close opens a door instead of shutting one, pointing at what comes
next (in a series) or what the reader now has to reckon with.

What never closes a piece: a thesis restatement, a motivational flourish ("the future belongs
to those who..."), a moralizing line about what this means for the reader's character, a call
to action bolted onto an argument, or a summary paragraph. If the last paragraph could be
deleted without losing anything, it's the wrong close — find the real one, usually the line
just before the summary.

## Format Defaults

The opening/flow/close principles above are universal. These are the concrete parameters for
common formats — apply the format's defaults on top of the general principles, not instead of
them.

**LinkedIn post:** 150–200 words. Open with a declared verdict — no warmup. Body earns it with
one specific insight. End on a question the audience can't answer yet — not a CTA, not a
summary.

**Landing page hero:** Headline = declared position (not a question, not a benefit list).
Subhead = reframe of the problem. Body = specific to the actual context, one idea developed
fully. CTA = structural offer, declarative and specific.

**Blog post:** Open with a verdict — no warmup, no scene-setting. Middle earns the opening claim
section by section. Close on the thing the reader hasn't considered yet, not the thing just
explained.

**Email:** Subject = structural fact or declared position. Open by naming the friction the
audience is currently living. Body = one insight fully developed. Close = a consequence or
structural offer depending on funnel stage.

**Newsletter:** Written to one subscriber, not a segment — the letter frame, not the broadcast
frame. Send from a real human address with reply-to enabled; a no-reply/info@ sender undercuts
the letter frame before the body even starts. The welcome/first email matters disproportionately
— it sets expectations for cadence and content, which heads off unsubscribes and complaints more
cheaply than any later re-engagement effort.

**Personal voice / newsletter-as-yourself:** These format defaults are for brand/venture
content. Writing as yourself (Substack, personal LinkedIn, direct outreach) follows your own
voice instead — the author-voice skill layered on top wins here, not this section.

## Structural Output

When running `structure`, return: what the opening is doing and whether it earns the read;
where the flow stalls, treadmills, or restates; whether any sections are reshuffleable modules;
and whether the close does real work. Propose specific cuts and reorderings. Don't rewrite
lines — that's the `edit` function.

---

# FUNCTION 2: `edit`

Line-level editing. Readability, cutting, grounding, rhythm. Anti-AI removal woven through.

## The Core Instinct: Cut

Default to cutting, not adding. When a line could go without loss, it goes. When in doubt,
cut it out. Most drafts are too long, too hedged, and too eager to re-explain — the editing
job is mostly subtraction. A shorter piece that makes its point cleanly beats a longer one
that makes it three times.

## Grounding Rules (Hard Stops)

These are the highest-value line edits. Every one is a form of writing reaching past what's
true or earned. The fix is always the same: cut to what's real — either a specific, grounded
account or a claim carried by a named source. The vague middle — plausible-sounding material
that asserts without grounding — never survives. Flag every instance.

**Population quantifiers — HARD STOP.** Any claim that quantifies a population or a span into
a proportion. "Most people treat experience like..." "Most professionals never..." And the
inverse — "Almost none of...," "Few ever...," "The majority of...," "Nearly all..." A sentence
opening with "Most" is almost always making a claim the writer has no standing to make. The
inverse is the identical move pointed the other way, equally unfounded. Not as an opener, not
buried mid-sentence, not even about oneself ("most of my days"). Replace with ONLY: (a) a
specific account of what actually happened, or (b) a claim attributed to a named source. No
"in general," "tends to," "more often than not" as smuggled versions of the same move.

**Invented interiority — HARD STOP.** Narrating what a person thought, felt, was trying to
do, or realized — when the source never said so. "It named the thing I'd been trying to say."
"She knew immediately." Manufactures an internal state to inflate a moment. Let the concrete
detail carry the weight; if the action or emphasis already shows it, the interior narration is
redundant and invented.

**Manufactured experience — HARD STOP.** Inventing an anecdote, career arc, or lived moment
to fill a structural slot. The most damaging invention because it trades on the reader's trust
in first-person testimony. When a paragraph wants a personal anchor and there isn't a real one,
CUT the paragraph — don't fabricate. Ask the writer for the real example first; if there isn't
one, cut. If the structural point can be made plainly without the anecdote, make it plainly.

**Manufactured vulnerability.** Performing difficulty, struggle, or doubt as a rhetorical move.
"I have to admit..." "I used to be more disciplined about this." Real candor doesn't announce
itself. If there's genuine complexity, work through it without signaling that honesty is coming.

**Unmeasured quantitative flourish.** Attaching measurement language to something never
measured. "Building the wrong habit, faster." "It taught him twice as much." "Faster," "more,"
"twice as much" imply data. If the rate or amount wasn't observed, don't imply it was.

**Smuggled domain metaphor.** Carrying domain-specific language from a concrete example into
the general claim it illustrates. After a sports scene, describing the reader's work in the
sport's vocabulary. The scene illustrates; it doesn't keep coloring the abstraction. Leave the
domain fully behind in the general point — including in the verbs.

## Throat-Clearing and False Cohesion

**Throat-clearing.** Any phrase that warms up to the point instead of making it: "Here's the
thing," "The truth is," "Let me be clear," "What you need to understand is," "So what do you
do with this," "It's important to remember that," "In my opinion." Also section-pivot
announcements and any sentence whose only job is to say something is coming. Cut to the point.

**Announcing the metaphor.** Telling the reader a scene was illustrative instead of trusting
them to see it: "That's the whole thing in a backyard," "This is the lesson here." Cut. The
reader got it.

**False callback.** Referencing prior structure that was never established: "the same test,"
"as we saw," "that framework" pointing at something absent. Every callback needs a referent.
Check each backward reference against the text.

**AI connective tissue.** Transitions that announce a connection instead of making it: "Which
means..." leading a conclusion, "That's why..." restating what was just proven, "This is the
key insight:" before the insight, "It's worth noting that," soft reveals like "turns out to
be" that dramatize a connection the reader can already see.

**False antithesis ("not X, but Y").** The "not X, but Y" construction is an AI staple — it
manufactures a pivot that sounds insightful but often isn't. Only use it when X is something
the audience genuinely believes right now, so the correction does real work. "Not a tool, but
a teammate" is empty if nobody thought it was just a tool. If X is a strawman the reader never
held, cut the construction and state Y directly.

## Sentence Rhythm

**Burstiness.** Mix very short sentences (3–8 words) with long ones (20+). Avoid the AI
pattern of consistent 12–18 word sentences. Short sentences land; long ones develop. A
fragment works. A one-sentence paragraph works. If three or more consecutive sentences fall
in a similar length-and-structure band, break the block.

**Matched-cadence repetition.** Two sentences with the same rhythmic shape landing near each
other, even when content differs entirely. "It runs on a few conditions, and they're strict."
... "There's a specific goal, and it's narrow." Survives a vocabulary pass because no words
repeat — but the ear hears the matched construction as repetition. Watch sentence *shape*, not
just word choice. Break it: run into the second with a lead-in, vary the construction.

**The "no twins" scan.** After drafting, search for repeated sentence patterns: three
consecutive sentences opening with the same word ("Your... Your... Your..."), multiple
sentences with identical structure, consecutive paragraphs opening the same way. Break them
deliberately.

**Readability ceiling.** Independent of burstiness (which wants variety, including genuinely
long sentences): most sentences should still land under ~25 words, and most paragraphs under
~3 sentences / 6 lines. This is a baseline floor, not a cap on the long half of the burstiness
mix — a deliberate 30-word sentence for development is fine; a paragraph that's wandered to
eight dense sentences before its first break usually hasn't.

**Prefer active voice by default.** Passive constructions bury the actor and add words for no
gain — "the decision was made" instead of who made it. Default to active; flag passive used as
a default habit rather than a deliberate choice (procedural steps with no relevant actor,
emphasis on the object over the doer are legitimate reasons to keep it passive).

**Exclamation points — restraint.** One earns attention; three in a page reads as manufactured
enthusiasm. Cut all but the one that's actually doing work, if any.

## Vocabulary

**Banned filler — cut on sight:**
- *actually* — almost always deletable. "That's actually what led me" → "That's what led me."
  Adds nothing; weakens the sentence it sits in. One of the most overused words in drafts.
- *very, really, just, quite, somewhat* — intensifiers that dilute. Keep under ~2% of words.
- *in order to* → "to." Never needs the extra two words.
- *in this article, in this post, in this piece* → cut. The reader knows what they're reading.

**AI vocabulary — replace:**
- delve into → explore, dig into · utilize → use · leverage (verb) → use · facilitate → help
- robust → strong · comprehensive → thorough · seamless → smooth · meticulous → careful
- testament to → shows · underscores → highlights · pivotal → key · foster → build, support
- navigate (metaphor) → work through · landscape (metaphor) → field, space · realm → area
- delve, embark, beacon, tapestry, paradigm, watershed → rewrite entirely
- "at the end of the day," "it's worth noting," "needless to say" → cut

**Hollow compound phrases — cut or make specific.** Multi-word stock phrases that sound like
strategy but say nothing: "durable competitive advantage," "sustainable growth trajectory,"
"meaningful organizational impact," "robust solution," "holistic approach." Each one is a slot
where a specific claim should be. Either name the actual advantage/growth/impact, or cut the
phrase.

**Generic business language — translate to specific human language:**
- "billable capacity" → "hours you can actually charge for"
- "strategic thinking" → "the thinking that grows the business"
- "demonstrates expertise" → "shows you know your stuff"
- "leverage synergies" → name the actual combined effect
- Limit: no more than two generic business terms per paragraph. Clusters of business jargon
  read as machine-generated; replace the cluster with how a person would say it out loud.

**Synonym cycling.** Don't rotate synonyms to avoid repeating a word ("developers...
engineers... practitioners... builders" for the same group). If the same noun is right,
repeat it. Forced variation reads as thesaurus abuse.

**Copula avoidance.** Don't swap "is" and "has" for fancier verbs by default — "serves as,"
"features," "boasts," "represents." Use "is" or "has" unless a specific verb genuinely adds
meaning.

## Lists and Structured Content

**Convert parallel lists to prose where possible.** In long-form, a bulleted list of parallel
points usually wants to be a fragment run ("Drafting. Generating. Processing volume at speed.")
or the most important point developed as a paragraph. Reserve real bullet lists for genuinely
discrete, non-narrative items.

**When a list must stay a list, break its uniformity.** Identical-length items with identical
structure is a strong machine tell. Vary item length dramatically — one item is a sentence,
the next is four. Don't use the same grammatical frame for every item. Let the most important
item run longer. Parallel structure across every item is the tell; deliberate unevenness is
the fix.

## Section-by-Section Uniformity

Global checks miss locally uniform sections inside an otherwise varied piece. After the
whole-document pass, scan each major section on its own:
- Are consecutive sentences similar in length within this section?
- Does the section hold one flat tone throughout?
- Do the paragraph openings vary within this specific section?
- Is there a voice present, or only explanatory flatness?

A section can pass the global rhythm check and still be robotic on its own. Catch it locally.

## Audience Calibration

**Don't over-narrow the audience.** Ground examples in the subject itself — the craft, the
work, the universal version of the activity — not in a narrow tool or sub-practice that
excludes most readers. Know whether a topic is the *lens* of the piece or the *identity* of
the reader; don't collapse a broad argument into a niche one through the examples. When in
doubt, pick the example that includes more of the audience.

**The brand-brief test.** If a sentence sounds like a brand describing itself, rewrite it as
something that brand would say to a specific person standing in front of them. "We deliver
comprehensive solutions that drive results" is a brand describing itself. "You'll have
something running by Friday, not a slide deck" is something said to a person. The test catches
self-referential corporate voice that no individual would ever say out loud.

## Orient Before You Move

A concrete scene needs its frame before the specific details depend on it. Name the domain,
setting, or activity first — "my seven-year-old's *baseball* swing" before "tee" and "barrel."
Don't drop the reader into action and make them assemble the context from jargon.

## Editorial Output

When running `edit`, return the edited text with changes applied, a list of what changed and
why (grouped by type), and any grounding-rule flags that need the writer's ruling (a missing
personal anchor, an unverifiable claim, a real-person attribution). Never fabricate to fill a
flagged gap — surface it.

---

# FUNCTION 3: `audit`

Dedicated anti-AI sweep. Mechanical pattern detection run clean against finished copy. This is
the final pass — it catches what survived the edit and what the edit introduced.

Run this even after a thorough `edit` pass. Editing fixes tells on the lines it touches; the
audit reads the whole finished piece fresh and catches what slipped through.

## Severity Tiers

**P0 — fix before anything else:**
- Chatbot artifacts: "Certainly!", "Great question!", "I'd be happy to," "Feel free to reach
  out," "Let me know if you need anything else"
- Vague attribution: "experts believe," "studies show," "research suggests" with no named source
- Significance inflation on routine events ("marking a pivotal moment in the evolution of...")
- Any grounding-rule violation that survived edit: population quantifiers, invented interiority,
  manufactured experience, manufactured vulnerability

**P1 — fix before publishing:**
- Throat-clearing openers and section pivots
- AI connective tissue ("Which means...," "That's why...," "turns out to be")
- False callbacks
- "actually" and filler intensifiers
- Matched-cadence repetition; uniform sentence rhythm (3+ consecutive similar sentences)
- AI vocabulary (delve, utilize, leverage, robust, seamless, etc.)
- Announcing the metaphor
- Generic conclusions; summary closes
- Synonym cycling

**P2 — fix when time allows:**
- Copula avoidance ("serves as," "boasts")
- Uniform paragraph length
- Compulsive rule of three
- Generic business language clusters
- Locally uniform sections (section-by-section scan)

## The Two-Pass Method

The audit runs twice on its own output:

**Pass 1** — read the finished copy, flag every tell by severity, fix.

**Pass 2** — re-read the result. Editing introduces new tells: a cut creates a matched cadence,
a rephrase reaches for an AI verb, a tightened transition becomes a soft reveal. Catch the
survivors and the new arrivals. If the second pass is clean, say so.

## Audit Output

When running `audit`, return: every tell found, quoted, grouped by severity; the corrected
text; a brief note on what changed; and the second-pass result. If the copy is clean, say that
plainly rather than inventing flags to look thorough.

---

# FUNCTION 4: `copyedit`

The mechanical-correctness layer — grammar, punctuation, usage, consistency, proofreading.
What a copyeditor and proofreader provide after the writing and editing are done. Runs last,
against near-final copy.

## The Governing Principle: Style Over Form

**Correct errors. Never impose style rules the voice deliberately breaks.** This is the line
the whole function turns on. There are two categories, and the function only touches one.

**Errors — fix these.** Things that are simply wrong, that create ambiguity, or that a reader
would trip on as a mistake. The author didn't choose them; they're slips. Fix silently or flag,
per the type.

**Style rules — leave these alone.** Preferences that strict grammar guides assert but that a
distinctive voice routinely overrides: sentence fragments, sentence-initial "And"/"But"/"So,"
ending a sentence on a preposition, the occasional comma splice used for rhythm, one-sentence
paragraphs, deliberately short or deliberately long sentences. The author chose these. They are
voice, not error. **Do not "correct" them.** If the author skill protects a move (fragments for
percussion, em-dashes as breath), this function honors that protection absolutely.

The test for any flagged item: *did the writer choose this, or slip?* A fragment for emphasis is
a choice. "Their going to the store" is a slip. Fix slips. Leave choices.

When genuinely unsure whether something is a deliberate stylistic choice or an error, flag it as
a question rather than fixing it — never silently overwrite a possible voice decision.

## Grammar — Fix (Unambiguous Errors)

- **Subject–verb agreement.** "The list of items are long" → "is long."
- **Pronoun–antecedent agreement** where it creates real confusion (not singular "they," which
  is accepted and often correct).
- **Pronoun case** in unambiguous error: "between you and I" → "between you and me."
- **Dangling and misplaced modifiers** that create actual ambiguity or unintended meaning.
  "Walking to the store, the rain started" — the rain isn't walking. Flag or fix.
- **Faulty parallelism in a series.** "She likes hiking, swimming, and to bike" → make the
  series parallel. (But don't force parallelism across separate sentences where the variation
  is rhythmic.)
- **Verb tense consistency** within a passage, unless the shift is intentional and clear.
- **Common usage errors:** its/it's, your/you're, their/there/they're, affect/effect (when
  misused), fewer/less (countable vs. mass), who/whom only where the error is jarring,
  comprise/compose, lay/lie where misused.

## Punctuation — Fix (Mechanical Errors)

- **Comma splices** that read as errors (two independent clauses joined by a comma) — but NOT
  when used deliberately for rhythm in a short, balanced pair ("I came, I saw"). Judgment call;
  flag if unsure.
- **Run-on / fused sentences** — two independent clauses with no punctuation between them.
- **Restrictive vs. non-restrictive commas.** "My brother, who lives in Ohio, called" (one
  brother, non-restrictive) vs. "My brother who lives in Ohio called" (distinguishing among
  brothers, restrictive). Fix when the comma usage contradicts the intended meaning.
- **That vs. which** for restrictive/non-restrictive clauses — fix where it changes meaning;
  leave where house style is loose and meaning is clear.
- **Apostrophes:** possessive vs. plural ("the 90s" not "the 90's"), it's/its, possessive of
  names ending in s (consistency, not dogma).
- **Hyphenation of compound modifiers** before a noun: "a well-known author" (hyphen) vs. "the
  author is well known" (no hyphen). "Twenty-year career." Fix for clarity.
- **Semicolon vs. colon vs. comma** where one is mechanically wrong — but don't relocate a
  writer's deliberate dash or period choices. (Em-dash *overuse* is the audit's job; mechanical
  misuse is this function's.)
- **Quotation mark and punctuation placement** per consistent convention (US: periods and
  commas inside; logical/UK if that's the established style — match the document, don't impose).

## Usage and Word-Level — Fix or Flag

- **Wrong word / malapropism:** "for all intensive purposes" → "intents and purposes";
  "could care less" → flag (idiom debate, author's call).
- **Redundancy that's an error, not a voice choice:** "ATM machine," "PIN number," "free gift"
  — flag; the writer may want the colloquial form.
- **Misused literally**, "begs the question" (if precision matters to the audience) — flag,
  don't force.

## Consistency — Fix (Silent Where Obvious)

- **Spelling convention:** US vs. UK throughout (-ize/-ise, -or/-our, traveled/travelled). Pick
  what the document predominantly uses and make it consistent.
- **Number style:** spell out vs. numeral, applied consistently (e.g., spell out under ten,
  numerals for ten and up — or whatever the piece establishes). Dates, times, percentages
  consistent.
- **Capitalization** of recurring terms, headings, and defined terms — consistent throughout.
- **Serial (Oxford) comma:** match whatever the piece uses; make it consistent. Don't impose a
  preference if the writer is consistently the other way.
- **Hyphenation consistency** for recurring compounds (e-mail vs. email — pick one).
- **Spacing:** one space after periods (unless the document is deliberately otherwise), no
  double spaces, consistent spacing around dashes.

## Proofreading — Fix

- **Typos and misspellings.**
- **Doubled words** ("the the"), **missing words** ("going to store").
- **Transposed letters**, **wrong homophone** introduced by autocorrect.
- **Stray or missing punctuation**, unclosed quotes or parentheses.
- **Inconsistent or broken formatting** — a heading that doesn't match its siblings, a list with
  a missing marker.

## What `copyedit` Never Does

- Never "fixes" intentional fragments, sentence-initial conjunctions, or one-sentence paragraphs.
- Never converts deliberate rhythm choices (short punchy sentences, a long breathless one) into
  "balanced" prose.
- Never imposes the active voice where passive is a deliberate or correct choice.
- Never flattens voice in the name of grammar. If a "rule" and the author's voice conflict, the
  voice wins — this function only catches what the writer would agree is a mistake.
- Never overrides a protection set by the author skill (the voice layer's deliberate moves).

## Copyedit Output

When running `copyedit`, return: the corrected copy; a list of fixes grouped by type (grammar,
punctuation, usage, consistency, proofreading); and a separate list of *flagged judgment calls*
— items that might be deliberate voice choices, presented as questions for the writer rather
than silent fixes. If the copy is mechanically clean, say so plainly.

---

# Running the Full Sequence

When invoked generically ("run the writing skill," "edit this," "make this better"), run all
four in order and return the result of each stage:

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

---

# What This Skill Does Not Do

- **Set voice register or rhythm signature** — that's the author skill layered on top. This
  skill won't make writing sound like a specific person; it makes writing structurally sound,
  tight, grounded, and free of machine patterns.
- **Inject personality to defeat detection** — this skill cuts to what's earned; it never adds
  manufactured asides, vulnerability, or current-events backdrop to seem more human. Humanity
  comes from real specifics and a real voice (the author skill's job), not from injected tics.
- **Fabricate to fill gaps** — flags missing anchors and unverifiable claims for the writer;
  never papers over them.
- **Make series or project-level architecture decisions** — those belong to the writer and
  the project brief.

---

# Sourcing Note

The structural principles (cold opens, callback discipline, closes that point forward instead
of summarizing) draw on general editing craft shared across journalism and writing-craft
traditions broadly — not any single author's specific named method. The anti-AI detection draws
on systematic pattern research. The copyedit function draws on standard usage and style
references (Strunk & White's *The Elements of Style*, the *Chicago Manual of Style*, Garner's
usage) — applied in service of voice, never over it. This is a general craft skill; it layers
under whatever author-voice or closing-polish skill is in use, and doesn't implement any one
person's specific named framework (a skill like `ann-handley-voice`, where one exists, is where
that layer belongs).
