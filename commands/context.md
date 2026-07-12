---
description: Build or refresh AUTHOR-CONTEXT.md through a guided interview — who you write for, why, and what's worth publishing
argument-hint: [nothing needed — the skill will check for existing evidence and then interview]
---

Run the `rl-context-discovery` skill now. The skill file is the source of truth; where this summary and the skill differ, the skill wins.

**Request:** $ARGUMENTS

## Pipeline

1. **Check existing evidence.** An about page, previously published content, README/CLAUDE.md files, any existing positioning material — treat these as a first draft to interrogate, not a final answer.
2. **Interview for the rest**, with technique specifically designed to get past generic first answers:
   - Who: push for distinctness per audience, not a list.
   - Why: don't ask directly first — use "what's actually stopping you from publishing more," "would you still write this if nobody would see it," to get past the marketing answer.
   - What's worth publishing: ask for cases ("what did you regret skipping"), not a stated principle.
3. **Draft `AUTHOR-CONTEXT.md`'s three sections** — every claim traceable to evidence or something actually said, not smoothed into something more generic. Note whether the result is evidence-informed or interview-derived in the context file's source-note line.
4. **Validate.** Rank 2-3 candidate topics against the draft, ask if the order feels right, fold in corrections — re-rank a second time if the gap was significant.
5. **Hand off.** `rl-repo-topic-scout` and `rl-content-pipeline` already read this file — nothing further to wire up.

## Notes

- One-time (or occasional refresh) discovery process, not a per-draft tool.
- If the ranked shortlist from `/scout` starts feeling consistently off, that's the signal to run this again.
