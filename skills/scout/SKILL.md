---
name: scout
description: Scan this repo's git history for evidence-grounded content topics, present a ranked shortlist, and hand the chosen one into the content pipeline.
argument-hint: '[lookback window, e.g. "past 2 weeks"] — defaults to since the last scout run, or 2 weeks'
disable-model-invocation: true
license: MIT
---

Invoke the `rl-topic-scout` skill now and run it against the current repo. That
skill file is the only source of truth for how scanning, grounding, client-work
tagging, and ranking work — read it and follow it rather than working from
memory.

**Request:** $ARGUMENTS

Scope note specific to this entry point: it defaults to the **current repo**.
The skill also supports a wider scope — a fixed list of repos, or a live rule
such as "top N by activity" — so name the repos or the rule in your request to
scan wider.
