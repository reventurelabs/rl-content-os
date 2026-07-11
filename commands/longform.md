---
description: Run the structured long-form writing pipeline — define → interview → brief → outline → draft → critique → revise → polish → refine → approve
argument-hint: <venture>, <format>, <topic>  e.g. "Reventure Labs blog post, why AI rollouts stall on sequencing not technology"
---

The user is producing a long-form piece. Run the `rl-long-form-pipeline` skill's full 10-step sequence now, in order. Do not skip a step, and do not collapse it into an ad-hoc draft.

**Request:** $ARGUMENTS

## Pipeline

1. **Define.** Topic, target reader, angle/thesis, goal, venture or publication, rough length. Infer what's given; ask only what's genuinely missing.
2. **Interview.** Self-interview if you're the SME; a fuller open-ended interview if a named third party is — either way, surface specifics (examples, numbers, positions), don't paraphrase from memory.
3. **Brief.** Objective, audience, key message(s), success criteria, non-goals, voice reference. One confirmation before moving on.
4. **Outline.** H2/H3 structure with talking points and examples per section. Approval gate before drafting.
5. **Draft.** Section by section, via your content-generation or author-voice skill, pulling in the interview's specifics. Honor `rl-writing-craft`'s Grounding Rules — never invent scenes, specifics, or claims about real people.
6. **Review against the brief.** Structured critique — does it hit the brief's success criteria and key messages? Name gaps specifically.
7. **Revise.** Address only what the critique flagged.
8. **Run the writing suite.** `rl-writing-craft` (structure → edit → audit → copyedit), then an optional closing polish skill if you have one (e.g. `ann-handley-voice`) for venture/brand content — skip for raw personal voice unless explicitly requested.
9. **Refine.** Fold in the suite's findings; confirm every section still carries a concrete, non-generic detail.
10. **Approve.** Present the finished piece as a gate — nothing here is publishable, posted, or sent until you've explicitly said so.

## Notes

- If venture, format, or topic is missing, infer from context — ask only if genuinely ambiguous.
- For quick-turn formats (a LinkedIn post, a single email, social copy) this pipeline is overhead — use `/write` instead.
- This command is the source-of-truth ordering; the `rl-long-form-pipeline` skill body documents the same sequence for ad-hoc (non-`/longform`) requests.
