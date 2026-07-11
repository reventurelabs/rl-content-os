---
description: Scan this repo's git history for potential blog topics, then hand the chosen one into /longform
argument-hint: [lookback window, e.g. "past 2 weeks"] — defaults to since the last scout run, or 2 weeks
---

Run the `rl-repo-topic-scout` skill against the current repo now.

**Request:** $ARGUMENTS

## Pipeline

1. **Scan.** Git log over the lookback window, diffs on notable commits, README/CLAUDE.md changes, structural changes (new/deleted directories, dependency swaps, new modules). Ground everything in what's actually there — no inventing the "why" behind a change that isn't visible in the commit message or diff.
2. **Shortlist.** Present 3-5 candidate topics: title, angle, evidence (specific commits/dates/files), why now, likely audience/venue. Options to pick from, not an open question.
3. **Hand off.** Once a topic is picked, feed it straight into the `rl-long-form-pipeline` skill's define/interview steps (1-2) with the gathered evidence attached — don't restart from a blank page.

## Notes

- Read-only — this command never writes, commits, or publishes anything.
- For the actual long-form write-up once a topic is chosen, this hands off to `/longform`.
