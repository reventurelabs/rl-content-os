---
description: Scan this repo's git history for potential blog topics, then hand the chosen one into /pipeline
argument-hint: '[lookback window, e.g. "past 2 weeks"] — defaults to since the last scout run, or 2 weeks'
---

Run the `rl-repo-topic-scout` skill against the current repo now.

**Request:** $ARGUMENTS

## Pipeline

1. **Load the context file.** Read `AUTHOR-CONTEXT.md` at the repo root first, every run, before ranking anything — the shortlist gets weighted by fit with it, not by evidence strength alone.
2. **Scan.** Git log over the lookback window, diffs on notable commits, README/CLAUDE.md changes, structural changes (new/deleted directories, dependency swaps, new modules), and open questions or TODOs left in code or commit messages. Ground everything in what's actually there — no inventing the "why" behind a change that isn't visible in the commit message or diff. Client/work-for-hire repos get every candidate tagged `[CLIENT WORK — confidential source]` — never silently included, never silently excluded.
3. **Shortlist.** Present 3-5 candidate topics: title, angle, evidence (specific commits/dates/files), why now, likely audience/venue. Options to pick from, not an open question.
4. **Hand off.** Once a topic is picked, feed it straight into the `rl-content-pipeline` skill's define/interview steps (1-2) with the gathered evidence attached — don't restart from a blank page. Client-tagged topics keep their tag through the handoff.

## Notes

- The skill file is the source of truth; where this summary and the skill differ, the skill wins.
- This command defaults to the current repo. The skill also supports a wider scope — a fixed list of repos or a live rule ("top N by activity") — name the repos or the rule in your request to scan wider.
- Read-only — this command never writes, commits, or publishes anything.
- For the actual long-form write-up once a topic is chosen, this hands off to `/pipeline`.
