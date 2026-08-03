---
description: Run the structured content pipeline — define → interview → brief → outline → draft → critique → revise → writing suite → refine → approve
argument-hint: <venture>, <format>, <topic>  e.g. "Reventure Labs blog post, why AI rollouts stall on sequencing not technology"
---

The user is producing a long-form or high-stakes piece. Run the `rl-content-pipeline` skill's full 10-step sequence now, in order. Do not skip steps or collapse the sequence into an ad-hoc draft (step 5's short-piece exception, documented in the skill, still applies).

**Request:** $ARGUMENTS

## Pipeline

1. **Define.** Topic, target reader, angle/thesis, goal, venture or publication, rough length. Infer what's given; ask only what's genuinely missing.
2. **Interview.** Self-interview if you're the SME; a fuller open-ended interview if a named third party is — either way, surface specifics (examples, numbers, positions), don't paraphrase from memory.
3. **Brief.** Objective, audience, key message(s), success criteria, non-goals, voice reference. One confirmation before moving on.
4. **Outline.** H2/H3 structure with talking points and examples per section. Approval gate before drafting.
5. **Draft.** Section by section, via your content-generation or author-voice skill, pulling in the interview's specifics. Honor `rl-writing-craft`'s Grounding Rules — never invent scenes, specifics, or claims about real people.
6. **Review against the brief.** Three mandatory passes. (a) Judge pass: score the draft against the brief's success criteria and key messages — name gaps specifically. (b) Blind adversarial pass: spawn a fresh `Agent` call with no context on how the piece was written, told to find the weakest part and try to kill it — named, specific objections only. (c) Fact-check pass: verify every checkable claim (stat, date, name, quote, attributed source) against an independent source; flag what can't be verified rather than publishing it unchecked. After step 7's revision, re-run the adversarial pass once more to confirm the fix landed, and re-verify any claim the revision touched.
7. **Revise.** Address only what the critique flagged.
8. **Run the writing suite.**
   - `rl-writing-craft`'s full sequence: structure → edit → audit → copyedit.
   - Then a closing polish skill (e.g. `ann-handley-voice`) on venture/brand content, if one exists.
   - Skip the polish pass for raw personal voice unless explicitly requested.
9. **Refine.** Fold in the suite's findings; confirm every section still carries a concrete, non-generic detail.
10. **Approve.** Present the finished piece as a gate — nothing here is publishable, posted, or sent until you've explicitly said so.

## Notes

- If venture, format, or topic is missing, infer from context — ask only if genuinely ambiguous.
- For quick-turn formats (a LinkedIn post, a single email, social copy) this pipeline is overhead — use your content-generation or author-voice skill directly instead.
- The `rl-content-pipeline` skill file is the source of truth; where this summary and the skill differ, the skill wins.
