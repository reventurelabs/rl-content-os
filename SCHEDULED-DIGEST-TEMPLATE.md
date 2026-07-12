# Scheduled digest — setup template

A recurring autonomous draft cycle isn't something you install by cloning
this repo — scheduled tasks are a Claude Code platform feature, requested
directly from Claude in an interactive session, not a file that ships with
a skill suite. This is a copyable template for that request: fill in the
placeholders, paste the whole thing to Claude, and ask it to create a
scheduled task from it.

This is for anyone with a recurring source of real work to draw from — a
repo, a Slack workspace, recurring meetings, or your own sent email. Repos
are the most common case, not a requirement; pick whichever source (or
combination) actually matches where your real work happens. If none of
that applies to you, skip this entirely — run `/pipeline` directly on your
own topic ideas instead.

## What to ask Claude

> Create a scheduled task, [YOUR CADENCE — e.g. "Saturdays at 5am"], that:
>
> 1. Scans [pick one or more — this isn't repo-only]:
>    - Every git repo under [YOUR REPO DIRECTORY] (recomputed fresh every
>      run, no memory of prior runs), ranked by commit count over the last
>      90 days, top [N, e.g. 10] selected.
>    - [YOUR SLACK CHANNELS], for threads with real back-and-forth or a
>      decision reached.
>    - Meeting transcripts from [YOUR MEETING TOOL], for moments where
>      something got explained or decided out loud.
>    - Sent email from [YOUR EMAIL], for anything long and thoughtful
>      enough to be worth generalizing.
> 2. For each candidate source, follows the `rl-topic-scout` skill's
>    process with a lookback window matching the cadence (7 days for a
>    weekly digest) — the same evidence-and-safety pattern regardless of
>    source. Reads [PATH TO YOUR AUTHOR-CONTEXT.md] first and weights
>    candidates by fit with it — fit sets the ranking, evidence strength
>    and recency only break ties. Follows the scope-safety rules exactly:
>    tags client/work-for-hire material `[CLIENT WORK — confidential
>    source]`, never silently includes or excludes it, never assumes a
>    source's status from a prior run.
> 3. Combines everything into one ranked shortlist of 5-8 candidates,
>    regardless of which source(s) they came from — title, angle,
>    evidence, why now, likely audience, source, and the client tag if
>    applicable.
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
> Constraints: read-only with respect to every source scanned — never
> write, commit, push, or send anything on your behalf in any connected
> tool. Never scan outside what's listed above. Never message or share
> anywhere except [YOUR DELIVERY DESTINATION]. Never treat the draft as
> approved or final — that's my call, made later, not this task's.

## Simpler starting point

If full autonomous drafting feels like too much to start with, drop steps
4-5 — auto-select is pointless without drafting. A scheduled task that only
does steps 1-3 (scan, scout, rank) and delivers step 3's ranked shortlist
alone is a safer, smaller first version. Add auto-selection and drafting
later once you trust the ranking.

## After creating it

The platform's own approval flow is the safety check on the schedule itself
— you'll be asked to confirm before it goes live. Separately, click "run
now" once from the Scheduled section to pre-approve the tools it needs
(reads on whichever source(s) you picked, the Agent call for the
adversarial pass, whatever delivery channel you chose) — otherwise the
first real run may pause on a permission prompt instead of running
unattended.
