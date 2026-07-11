# Scheduled digest — setup template

A recurring autonomous draft cycle isn't something you install by cloning
this repo — scheduled tasks are a Claude Code platform feature, requested
directly from Claude in an interactive session, not a file that ships with
a skill suite. This is a copyable template for that request: fill in the
placeholders, paste the whole thing to Claude, and ask it to create a
scheduled task from it.

This is for **developers with repos** (see "Who needs what" in the main
README). If that's not you, skip this entirely — run `/pipeline` directly
on your own topic ideas instead.

## What to ask Claude

> Create a scheduled task, [YOUR CADENCE — e.g. "Saturdays at 5am"], that:
>
> 1. Scans every git repo under [YOUR REPO DIRECTORY] (recomputed fresh
>    every run, no memory of prior runs) and ranks them by commit count
>    over the last 90 days. Selects the top [N, e.g. 10].
> 2. For each selected repo, follows the `rl-repo-topic-scout` skill's
>    process with a lookback window matching the cadence (7 days for a
>    weekly digest). Reads [PATH TO YOUR AUTHOR-CONTEXT.md] first and
>    weights candidates by fit with it. Follows the scope-safety rules
>    exactly: tags client/work-for-hire repos with `[CLIENT WORK —
>    confidential source]`, never silently includes or excludes them,
>    never assumes a repo's status from a prior run.
> 3. Combines everything into one ranked shortlist of 5-8 candidates —
>    title, angle, evidence, why now, likely audience, source, and the
>    client tag if applicable.
> 4. Auto-selects the highest-ranked candidate that is **not**
>    client-tagged. Skips client-tagged candidates for drafting no matter
>    how high they rank — deciding what's safe to say about client work
>    needs a human present, and there isn't one in this run. If every
>    candidate is client-tagged, sends just the shortlist with a note
>    explaining why nothing was drafted, and stops.
> 5. Drafts the selected topic autonomously — `rl-content-pipeline`
>    steps 1 through 9, adapted for no live interview: draft from
>    gathered evidence only, keep an explicit "things I couldn't
>    determine" list rather than inventing, include the brief and outline
>    in the final output for transparency, run the judge + blind
>    adversarial review exactly as the skill specifies, run
>    `rl-writing-craft`'s full suite. **Stop before step 10** — never
>    approve, publish, or send the draft anywhere except to me for review.
> 6. Delivers [YOUR CHOSEN CHANNEL — e.g. "as a Slack canvas, with a DM
>    linking to it, to [your Slack user ID]" or "as an email to
>    [your email]"] containing: the finished draft, the "couldn't
>    determine" list, the brief and outline, and the remaining shortlist
>    (client-tagged candidates included, clearly marked).
>
> Constraints: read-only with respect to every scanned repo — never
> write, commit, or push anything. Never scan outside [YOUR REPO
> DIRECTORY]. Never message or share anywhere except [YOUR DELIVERY
> DESTINATION]. Never treat the draft as approved or final — that's my
> call, made later, not this task's.

## Simpler starting point

If full autonomous drafting feels like too much to start with, drop step 5
entirely — a scheduled task that only does steps 1-4 (scan, scout, rank,
shortlist) and delivers the shortlist alone is a safer, smaller first
version. Add auto-drafting later once you trust the ranking.

## After creating it

The platform's own approval flow is the safety check on the schedule itself
— you'll be asked to confirm before it goes live. Separately, click "run
now" once from the Scheduled section to pre-approve the tools it needs
(git reads, the Agent call for the adversarial pass, whatever delivery
channel you chose) — otherwise the first real run may pause on a permission
prompt instead of running unattended.

## Adding more input sources

Repos are one source of topic evidence, not the only one. See
`rl-repo-topic-scout`'s "Beyond repos" section for the pattern to follow if
you want to add Slack conversations, meeting transcripts, or email as
additional sources feeding the same shortlist.
