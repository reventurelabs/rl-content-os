---
description: Build a voice profile from real writing samples (or a structured interview if none exist), validate it against a test passage, and write VOICE-PROFILE.md
argument-hint: [nothing needed — the skill will ask for writing samples]
---

Run the `rl-voice-discovery` skill now.

**Request:** $ARGUMENTS

## Pipeline

1. **Gather material.** Ask for 5-10 pieces of real writing across a few different formats (not just volume — variety of context matters more). If none exist, fall back to a structured interview and flag the resulting profile as interview-derived, lower confidence.
2. **Extract patterns.** Sentence rhythm, formality baseline and how it shifts, contraction rate, hedging frequency, signature phrases, what's explicitly avoided, emotional range, opening/closing patterns — from what's actually in the samples, not a self-description.
3. **Draft `VOICE-PROFILE.md`.** Every claim traceable to the samples; say explicitly where a category isn't determinable rather than guessing.
4. **Validate.** Write a short test passage on a neutral topic, get direct feedback on where it doesn't sound right, fold in corrections.
5. **Hand off.** `rl-long-form-pipeline` and `rl-writing-craft` already look for this file wherever they reference "your author-voice skill" — nothing further to wire up.

## Notes

- This is a one-time (or occasional refresh) discovery process, not a per-draft tool.
- Produces a starting profile, not a finished, continuously-evolving voice system — that comes from tracking your own corrections over real drafts afterward.
