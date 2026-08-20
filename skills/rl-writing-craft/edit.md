# Function: `edit`

Line-level editing. Readability, cutting, grounding, rhythm. Anti-AI removal woven through.
Run the Logical Consistency check (see `SKILL.md` → “Logical Consistency — Grave Errors”) on this pass too.

### The Core Instinct: Cut

Default to cutting, not adding. When a line could go without loss, it goes. When in doubt,
cut it out. The default failure mode of a draft is excess — too long, too hedged, too eager
to re-explain — so the editing job is mostly subtraction. A shorter piece that makes its
point cleanly beats a longer one that makes it three times.

### Grounding Rules

These are the highest-value line edits. Every one is a form of writing reaching past what's
true or earned. The fix is always the same: cut to what's real — either a specific, grounded
account or a claim carried by a named source. The vague middle — plausible-sounding material
that asserts without grounding — never survives. Flag every instance.

Eight rules, two severities. The first five are HARD STOPS — P0 in the audit's severity tiers,
fixed before anything else. The last three are STRONG FLAGS — P1, fixed before publishing.

**Population quantifiers — HARD STOP.** Any claim that quantifies a population or a span into
a proportion. A sentence opening with "Most" is almost always making a claim the writer has no
standing to make. Not as an opener, not buried mid-sentence, not even about oneself ("most of
my days").

Examples: "Most people treat experience like..." "Most professionals never..." The inverse —
"Almost none of...," "Few ever...," "The majority of...," "Nearly all..." — is the identical
move pointed the other way, equally unfounded.

Replace with ONLY: (a) a specific account of what actually happened, or (b) a claim attributed
to a named source. No "in general," "tends to," "more often than not" as smuggled versions of
the same move.

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

**Manufactured vulnerability — HARD STOP.** Performing difficulty, struggle, or doubt as a rhetorical move.
"I have to admit..." "I used to be more disciplined about this." Real candor doesn't announce
itself. If there's genuine complexity, work through it without signaling that honesty is coming.

**Unearned capability claim — HARD STOP.** A confident assertion about quality, reliability, or
capability with no specific, checkable referent behind it. "Systems that hold up under real
use." "A comprehensive solution." "Built for scale." It's the subtlest violation in this list
because it doesn't look broken — the sentence is fluent and reads as professional, which is
exactly the problem: it's polish standing in for evidence. This is what "AI slop" actually is
more often than not; not bad prose, unearned prose.

The test: swap the subject for a competitor, or a hypothetical company that does none of this.
Does the sentence still read as true? If yes, it was never actually about the specific thing —
it's a slot that could hold anything.

Replace with ONLY: (a) the actual specific fact being gestured at — what, concretely, holds up,
and how would a reader check it — or (b) cut the sentence outright. Sounding confident is not
the same as being earned. Related, narrower mechanisms elsewhere in this file: Hollow compound
phrases (Vocabulary) catches the noun-phrase version of this same move; Verdict adjectives
(Vocabulary) catches the single-word version; the brand-brief test (Audience Calibration)
catches it from the angle of who would actually say the sentence out loud. This rule is the
general case all three are instances of.

**Causal-superlative overclaim — HARD STOP.** A claim that names one thing as *the* reason, *the*
point, or what *made something possible* — a sole-cause or existential frame — when the true claim
is smaller: it was a priority, one of several goals, or mattered without being decisive. "It's the
reason the product exists at all." "That's the entire point." "None of this works without X." The
tell is a sole-cause or existential frame doing work a more modest, checkable claim would do
honestly.

The test: say the smaller version out loud — "it was a goal from day one," "one of several things
we cared about," "it mattered, but the product would've shipped without it" — and ask which is
actually true. Superlative causal claims are rarely checkable and almost always inflate; the writer
usually knows the smaller version is the honest one when asked directly. Use the smaller true one
unless the big one is genuinely defensible with evidence.

This is the causal-origin sibling of Unearned capability claim (above): the same inflation, aimed at
*why something exists* rather than *how good it is* — so the swap-the-subject test doesn't catch it,
and this separate check exists to.

**Unmeasured quantitative flourish — STRONG FLAG.** Attaching measurement language to something never
measured. "Building the wrong habit, faster." "It taught him twice as much." "Faster," "more,"
"twice as much" imply data. If the rate or amount wasn't observed, don't imply it was.

**Smuggled domain metaphor — STRONG FLAG.** Carrying domain-specific language from a concrete
example into the general claim it illustrates. After a baseball scene, "keep your swing level
through the quarter" applied to office work. The scene illustrates; it doesn't keep coloring
the abstraction. Leave the domain fully behind in the general point — including in the verbs.

**Studied neutrality — STRONG FLAG.** Retreating to "there are tradeoffs on both sides," "it
depends," or a both-sides survey when the material actually gathered — the interview, the
evidence, the brief's own stated angle — supports taking a real position. Heavy AI use
measurably increases neutral-position-taking relative to a writer's own baseline; it's the
model's default gravity, not a neutral act of fairness, and left unchecked it's a direct
route to writing that reads like everyone else's. The test: does the material already in
hand support a specific verdict? If yes, state it, then handle real counterarguments by
naming and narrowing them precisely — not by diluting the claim into mush to avoid seeming
to take a side. Not every topic has a real verdict to take; accurately reporting a genuinely
close call isn't this violation. The flag is for retreating from a side the evidence already
supports, not for calling a toss-up a toss-up. (Referred to elsewhere in this skill suite as
"commit to a position" / "vary certainty" — this is that rule, made specific and checkable.)

### Throat-Clearing and False Cohesion

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

### Sentence Rhythm

**Burstiness.** Mix short sentences (3–8 words) with long ones (20+). Avoid the AI
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

**Readability baseline.** Independent of burstiness (which wants variety, including genuinely
long sentences): ~25 words is the default expectation a sentence should land under, and ~3
sentences / 6 lines the default for a paragraph. This is a baseline, not a cap on the long
half of the burstiness mix — a deliberate 30-word sentence for development is fine; a
paragraph that's wandered to eight dense sentences before its first break usually hasn't.

**Prefer active voice by default.** Passive constructions bury the actor and add words for no
gain — "the decision was made" instead of who made it. Default to active; flag passive used as
a default habit rather than a deliberate choice (procedural steps with no relevant actor,
emphasis on the object over the doer are legitimate reasons to keep it passive).

**Exclamation points — restraint.** One earns attention; three in a page reads as manufactured
enthusiasm. Cut all but the one that's actually doing work, if any.

**Read it aloud.** Before finalizing this pass, read the passage as if speaking it out loud
(silently is fine — the point is hearing it, not the volume). Mark every place you'd stumble,
run out of breath mid-sentence, or want to add a beat that isn't there — a sentence that's
technically correct but doesn't sound like something a person would actually say. This is the
single most reliable check for rhythm problems the mechanical rules above can miss, and it's
close to universal across every credible editing process, AI-assisted or not. Run it as a last
check on the whole passage, not sentence by sentence — rhythm problems compound across
sentences and often aren't audible from inside just one of them.

### Vocabulary

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
- intricate → detailed, complex · enhance → improve · crucial → key, necessary · harness → use, tap
- notably → cut · showcase, showcasing → show, display · vibrant → cut, or name the specific quality
- delve, embark, beacon, tapestry, paradigm, watershed, multifaceted → rewrite entirely
- "at the end of the day," "it's worth noting," "needless to say" → cut

This list drifts as models shift — GPT-4-era tells (delve, tapestry) gave way to GPT-4o's
"fostering" and "showcasing," and the next shift won't match either list exactly. Treat it as
living, not fixed: when a word keeps showing up in drafts and reads as off regardless of
whether it's written down here, add it.

**Hollow compound phrases — cut or make specific.** Multi-word stock phrases that sound like
strategy but say nothing: "durable competitive advantage," "sustainable growth trajectory,"
"meaningful organizational impact," "robust solution," "holistic approach." Each one is a slot
where a specific claim should be. Either name the actual advantage/growth/impact, or cut the
phrase. This is the noun-phrase form of Unearned capability claim (Grounding Rules) — same
failure, smaller unit. Verdict adjectives (below) are the same failure smaller still — a
single word instead of a phrase.

**Verdict adjectives — replace with the evidence that would earn them.** The single-word form
of Unearned capability claim (Grounding Rules) and Hollow compound phrases (above) — same
failure, smallest unit. Words like "generic," "hedged," "flat," "robust," "innovative,"
"disruptive," "boring," "vague" don't describe an observable property. They compress a judgment the reader has no way to check —
each one silently says "trust my verdict" instead of showing what specifically earned it.
This isn't about how many appear together. "The writing was generic" is exactly as unearned
as "generic, hedged, flat" — a list doesn't cause the problem, it just makes an existing one
easier to spot. Test any candidate: could a reader independently verify this from the text
itself, or do they just have to take the writer's word for it? "Flat" fails; "every sentence
lands within two words of the same length" passes. "Generic" fails; "swap the company name
and the sentence still reads true" passes — because that's the actual fact "generic" was
standing in for.

The fix is never a better adjective. It's the specific, checkable fact that would let a
reader reach the same verdict themselves — but only if that fact already exists somewhere
real: in the source material, the interview, something already established earlier in the
piece. When the piece describes a real system with source material behind it (code, a
spec, documentation, prior written work), check that source directly before concluding no
fact exists — the concrete mechanism a verdict adjective is standing in for is usually
sitting in the actual source, not missing entirely; the fastest way to accidentally
fabricate a "concrete example" is skipping that check and reaching for something merely
plausible instead. Never invent one to satisfy this rule. A fabricated "concrete example" manufactured
to sound specific is a Manufactured experience violation (Grounding Rules) wearing this
rule's fix as a disguise — worse than the adjective it replaced, because it now reads as
earned when it isn't. Same handling as Manufactured experience: if a real fact is available,
use it; if it isn't, don't paper over the gap — cut the adjective and flag it as a question
for the writer ("this needs a real example — do you have one?") rather than resolving it
yourself. And whatever replaces the adjective, real or flagged, gets checked again before
it's final — this is exactly the case "Replacement text inherits the check it replaced"
(Running the Full Sequence) exists for.

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

### Lists and Structured Content

**Convert parallel lists to prose where possible.** In long-form, a bulleted list of parallel
points usually wants to be a fragment run ("Drafting. Generating. Processing volume at speed.")
or the most important point developed as a paragraph. Reserve real bullet lists for genuinely
discrete, non-narrative items.

**When a list must stay a list, break its uniformity.** Identical-length items with identical
structure is a strong machine tell. Vary item length dramatically — one item is a sentence,
the next is four. Don't use the same grammatical frame for every item. Let the most important
item run longer. Parallel structure across every item is the tell; deliberate unevenness is
the fix.

### Section-by-Section Uniformity

Global checks miss locally uniform sections inside an otherwise varied piece. After the
whole-document pass, scan each major section on its own:
- Are consecutive sentences similar in length within this section?
- Does the section hold one flat tone throughout?
- Do the paragraph openings vary within this specific section?
- Is there a voice present, or only explanatory flatness?

A section can pass the global rhythm check and still be robotic on its own. Catch it locally.

### Audience Calibration

**Don't over-narrow the audience.** Ground examples in the subject itself — the craft, the
work, the universal version of the activity — not in a narrow tool or sub-practice that
excludes most readers. Know whether a topic is the *lens* of the piece or the *identity* of
the reader; don't collapse a broad argument into a niche one through the examples. When in
doubt, pick the example that includes more of the audience.

**The brand-brief test.** If a sentence sounds like a brand describing itself, rewrite it as
something that brand would say to a specific person standing in front of them. "We deliver
comprehensive solutions that drive results" is a brand describing itself. "You'll have
something running by Friday, not a slide deck" is something said to a person. The test catches
self-referential corporate voice that no individual would ever say out loud — the same failure
Unearned capability claim (Grounding Rules) names directly, approached from a different angle:
would a specific person say this to a specific other person, or only a brand say it to no one
in particular.

### Orient Before You Move

A concrete scene needs its frame before the specific details depend on it. Name the domain,
setting, or activity first — "my seven-year-old's *baseball* swing" before "tee" and "barrel."
Don't drop the reader into action and make them assemble the context from jargon. This rule
governs ordering *within* the opening scene — name the domain in the first concrete beat; the
cold-open rule governs *where* the piece starts. They compose, not conflict: open cold, and
let that first concrete detail carry its own frame.

### Editorial Output

When running `edit`, return the edited text with changes applied, a list of what changed and
why (grouped by type), and any flags that need the writer's ruling — grounding-rule violations
(a missing personal anchor, an unverifiable claim, a real-person attribution) and verdict
adjectives with no real fact behind them alike. Never fabricate to fill a flagged gap — surface
it.

---

Part of the `rl-writing-craft` skill. See `SKILL.md` for how this function
sequences with the other three and with an author-voice skill.
