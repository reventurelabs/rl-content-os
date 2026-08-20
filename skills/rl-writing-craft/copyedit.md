# Function: `copyedit`

The mechanical-correctness layer — grammar, punctuation, usage, consistency, proofreading.
What a copyeditor and proofreader provide after the writing and editing are done. Runs last,
against near-final copy. Run the Logical Consistency check (see `SKILL.md` → “Logical Consistency — Grave Errors”) on this pass too.

### The Governing Principle: Style Over Form

**Correct errors. Never impose style rules the voice deliberately breaks.** This is the line
the whole function turns on. There are two categories, and the function only touches one.

**Errors — fix these.** Things that are simply wrong, that create ambiguity, or that a reader
would trip on as a mistake. The author didn't choose them; they're slips. Fix silently or flag,
per the type.

**Style rules — leave these alone.** Preferences that strict grammar guides assert but that a
distinctive voice routinely overrides: sentence fragments, sentence-initial "And"/"But"/"So,"
ending a sentence on a preposition, the occasional comma splice used for rhythm, one-sentence
paragraphs, deliberately short or deliberately long sentences. The author chose these. They are
voice, not error. **Do not "correct" them.** If the author-voice skill protects a move (fragments
for percussion, em-dashes as breath), this function honors that protection absolutely.

The test for any flagged item: *did the writer choose this, or slip?* A fragment for emphasis is
a choice. "Their going to the store" is a slip. Fix slips. Leave choices.

When genuinely unsure whether something is a deliberate stylistic choice or an error, flag it as
a question rather than fixing it — never silently overwrite a possible voice decision.

### Grammar — Fix (Unambiguous Errors)

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

### Punctuation — Fix (Mechanical Errors)

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

### Usage and Word-Level — Fix or Flag

- **Wrong word / malapropism:** "for all intensive purposes" → "intents and purposes";
  "could care less" → flag (idiom debate, author's call).
- **Redundancy that's an error, not a voice choice:** "ATM machine," "PIN number," "free gift"
  — flag; the writer may want the colloquial form.
- **Misused literally**, "begs the question" (if precision matters to the audience) — flag,
  don't force.

### Consistency — Fix (Silent Where Obvious)

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

### Proofreading — Fix

- **Typos and misspellings.**
- **Doubled words** ("the the"), **missing words** ("going to store").
- **Transposed letters**, **wrong homophone** introduced by autocorrect.
- **Stray or missing punctuation**, unclosed quotes or parentheses.
- **Inconsistent or broken formatting** — a heading that doesn't match its siblings, a list with
  a missing marker.

### What `copyedit` Never Does

- Never "fixes" intentional fragments, sentence-initial conjunctions, or one-sentence paragraphs.
- Never converts deliberate rhythm choices (short punchy sentences, a long breathless one) into
  "balanced" prose.
- Never imposes the active voice where passive is a deliberate or correct choice.
- Never flattens voice in the name of grammar. If a "rule" and the author's voice conflict, the
  voice wins — this function only catches what the writer would agree is a mistake.
- Never overrides a protection set by the author-voice skill (the voice layer's deliberate moves).

### Copyedit Output

When running `copyedit`, return: the corrected copy; a list of fixes grouped by type (grammar,
punctuation, usage, consistency, proofreading); and a separate list of *flagged judgment calls*
— items that might be deliberate voice choices, presented as questions for the writer rather
than silent fixes. If the copy is mechanically clean, say so plainly.

---

Part of the `rl-writing-craft` skill. See `SKILL.md` for how this function
sequences with the other three and with an author-voice skill.
