# Reventure Labs Content OS

A Claude Code skill suite for structured long-form writing and
evidence-driven topic scouting.

Most people who build things don't write about them — not for lack of
anything to say, but because the work before the writing (finding a topic,
structuring it, knowing when it's actually done) is its own unglamorous task,
and that task is what loses the priority fight. This suite exists to make
that work cheap enough that publishing becomes routine instead of a rare
burst of motivation, without lowering the bar on what gets published.

It takes the opposite failure mode just as seriously: a draft that's fast to
produce and not worth reading. Every step in `rl-content-pipeline` exists
because skipping it produces a specific, known failure:

- Drafting before the goal is pinned down — fluent-but-aimless copy.
- Skipping the outline gate — restructuring after the words are already
  written.
- Self-review by the same context that drafted — the weakest possible judge
  of the draft.

The subtlest version doesn't even look broken. It's a claim that sounds
professional and confident, phrased well enough that nobody checks whether
it's actually true — "systems that hold up under real use," "a comprehensive
solution," anything that reads smoothly and means nothing specific once you
press on it. That's the exact failure mode `rl-writing-craft`'s Grounding
Rules exist to catch. Not bad writing. Unearned writing.

Before anything reaches a human approval gate, the pipeline runs a
criteria-scored review and a blind adversarial pass — a fresh, context-free
reviewer whose only job is to try to kill the draft. And the pipeline isn't
only for long pieces: it triggers just as much on high-stakes content
regardless of length — a short statement going out under the company's name,
an announcement with no room to walk back a bad framing. The real criterion
is cost-of-being-wrong, not word count.

## Who needs what

**Everyone** gets `rl-content-pipeline`, `rl-writing-craft`, `rl-voice-discovery`,
`rl-context-discovery`, and `AUTHOR-CONTEXT.md` — the writing process, the
craft floor, the voice profile, and the context file apply to any writer,
technical or not.

**Anyone with a recurring source of real work** also gets `rl-topic-scout`
and, optionally, a recurring scheduled digest built on top of it (see
[SCHEDULED-DIGEST-TEMPLATE.md](./SCHEDULED-DIGEST-TEMPLATE.md)) — built for
surfacing topics from work already done: a repo's commits and diffs, a
Slack thread, a meeting, or your own sent email. Repos are the most common
case, not a requirement. If none of that applies to you, skip both
entirely. You can still run `/pipeline` directly on your own topic
ideas — `rl-topic-scout` feeds `rl-content-pipeline`, it isn't required by
it.

## What's here

| Skill / command | What it does |
|---|---|
| `rl-content-pipeline` | Structured 10-step process for long-form content — blog posts, whitepapers, essays, case studies — or high-stakes content regardless of length: a short statement going out under the company's name, an announcement with no room to walk back a bad framing. Define, interview, brief, outline, draft, critique, revise, run the writing suite, refine, approve. Nothing ships until you explicitly say so. |
| `rl-topic-scout` | Scans a repo's git history, README/CLAUDE.md, and structural changes — or Slack threads, meeting transcripts, and sent email, where connected — to surface 3-5 grounded topic candidates — each with evidence, an angle, and a "why now." Ranks candidates against the context file (`AUTHOR-CONTEXT.md`), and tags client/work-for-hire sources `[CLIENT WORK — confidential source]` rather than silently including or excluding them. Hands the pick straight into the content pipeline. |
| `rl-writing-craft` | Self-contained writing-quality skill: structure (architecture, flow, opens, closes), edit (line-level cutting, grounding, rhythm, anti-AI removal), audit (dedicated anti-AI pattern sweep), and copyedit (grammar, punctuation, usage, consistency, proofreading). General craft for any writer; layers under whatever author-voice skill you bring, which wins on register and rhythm. Works standalone too — it just won't impose a specific voice. |
| `rl-voice-discovery` | Builds `VOICE-PROFILE.md` from real writing samples (or a structured interview if none exist), validated against a test passage. A one-time discovery process, not a per-draft tool — `rl-content-pipeline` and `rl-writing-craft` already check for the resulting file wherever they reference "your author-voice skill." |
| `rl-context-discovery` | Builds or refreshes `AUTHOR-CONTEXT.md` — checks existing evidence (about page, published content, README/CLAUDE.md) first, then a guided interview specifically designed to get past generic first answers, validated against a hypothetical ranked topic shortlist. The guided version of the "ask once" fallback `rl-topic-scout` already has. |
| `/pipeline` | Deterministic entry point for the 10-step content pipeline — deterministic meaning typing the slash command always invokes this exact skill, rather than relying on Claude to infer the right skill from your request. |
| `/scout` | Deterministic entry point for repo topic scouting, handing its pick straight into `/pipeline`. |
| `/voice` | Deterministic entry point for building your voice profile. |
| `/context` | Deterministic entry point for building or refreshing `AUTHOR-CONTEXT.md`. |

A `/scout` shortlist looks like this (illustrative — repos, commits, and
topics are all fictional):

```text
1. Cutting cold-start time 40s → 6s in `queue-runner` — evidence: commits
   3f2a91..8bc04d, lazy-loading the plugin registry; angle: the profiling
   dead-end that made the fix obvious; why now: shipped this week.
2. Replacing the retry decorator with an outbox table in `sync-engine` —
   evidence: commit series reworking `sync/retry/`; angle: at-least-once
   delivery is a data-model decision, not a library pick.
3. [CLIENT WORK — confidential source] Rate-limit backoff rewrite in
   `acme-integrations` — surfaced so you can decide; won't be drafted
   without your explicit clearance.
```

`AUTHOR-CONTEXT.md` at the repo root is a blank template — who you are, who you write for,
why you write, and what "worth publishing" means to you. `rl-topic-scout`
and `rl-content-pipeline` both read it before ranking or defining a topic,
so filling it in once keeps both skills consistent about who you're actually
writing for. In multi-repo or scheduled use, "repo root" stops being
well-defined — there the context file's location is a configured path (see
the `[PATH TO YOUR AUTHOR-CONTEXT.md]` placeholder in the digest template).
Run `/context` for a guided version of filling it in, rather
than answering a single ad hoc question the first time a skill notices it's
still blank.

## Bring your own voice

**Only `rl-writing-craft` is a hard dependency.** This suite doesn't bundle
a content-generation skill or a closing-polish skill — bring your own (or
write one) if you want a tailored register beyond what `rl-voice-discovery`
produces. Without a voice reference at all, `rl-content-pipeline` still
runs the full process (interview, brief, outline, adversarial review,
approval gate) and drafts directly from the brief/outline using
`rl-writing-craft`'s floor — you get a competent, neutral-voiced draft
instead of one tailored to a specific voice. The process doesn't degrade;
only the register does. Run `/voice` first if you want that register from
the start.

## Install

Three ways to get the skills active in Claude Code. They install the same
files; pick whichever fits your workflow. **None of them install the
commands** (`/pipeline`, `/scout`, `/voice`, `/context`) — those need the
symlink or plugin-marketplace path regardless of how you get the skills
themselves, since command activation works differently from skill
activation. See step 2 below either way.

### Option A — CLI (fastest for just the skills)

This repo's `skills/rl-*/SKILL.md` files already match the flat layout the
[`skills` CLI](https://github.com/vercel-labs/skills) auto-discovers, so no
special setup is needed on this end:

```bash
npx skills add reventurelabs/rl-content-os --skill '*' -a claude-code
```

Or install one at a time: `npx skills add reventurelabs/rl-content-os --skill rl-content-pipeline -a claude-code`.
Use `--list` first to see what's available without installing anything.

**One caveat:** this only installs `SKILL.md` files, not the
`commands/` directory — you'll still want step 2 below for `/pipeline`
etc.

### Option B — Plugin marketplace (recommended once you want ongoing updates)

```bash
git clone https://github.com/reventurelabs/rl-content-os.git
```

Add the cloned repo as a local plugin marketplace source in Claude Code,
then install the `rl-content-os` plugin from it. This is the one
path that installs skills *and* commands together, and `git pull` picks up
future updates automatically.

### Option C — Manual symlinks (best if you want to edit skills in place)

```bash
git clone https://github.com/reventurelabs/rl-content-os.git
cd rl-content-os

ln -s "$PWD/skills/rl-content-pipeline" ~/.claude/skills/rl-content-pipeline
ln -s "$PWD/skills/rl-topic-scout" ~/.claude/skills/rl-topic-scout
ln -s "$PWD/skills/rl-writing-craft"    ~/.claude/skills/rl-writing-craft
ln -s "$PWD/skills/rl-voice-discovery"  ~/.claude/skills/rl-voice-discovery
ln -s "$PWD/skills/rl-context-discovery" ~/.claude/skills/rl-context-discovery
ln -s "$PWD/commands/pipeline.md"       ~/.claude/commands/pipeline.md
ln -s "$PWD/commands/scout.md"          ~/.claude/commands/scout.md
ln -s "$PWD/commands/voice.md"          ~/.claude/commands/voice.md
ln -s "$PWD/commands/context.md"        ~/.claude/commands/context.md
```

Edits to the repo are live immediately — no reinstall step.

### After installing, either way

**1. Fill in your context.** Run `/context` for a guided interview (checks
existing evidence first, then asks with technique designed to get past
generic first answers), or open `AUTHOR-CONTEXT.md` at the repo root
directly and fill in the bracketed placeholders yourself if you already
know the answers — either way, do this before running `/scout` or
`/pipeline` for real.

**2. Optional: build your voice.** Run `/voice` if you want `/pipeline`
drafting in your own register instead of a neutral one — it'll ask for
writing samples (or interview you if you don't have any) and produce
`VOICE-PROFILE.md`.

**3. Optional: set up the recurring digest.** See
[SCHEDULED-DIGEST-TEMPLATE.md](./SCHEDULED-DIGEST-TEMPLATE.md) — copy the
template, fill in the bracketed placeholders for whichever source(s) apply
to you (repos, Slack channels, a meeting tool, sent email), the cadence,
the context file's path, delivery channel, and delivery destination, and
ask Claude to create the scheduled task from it.

## Credit

Built and maintained by [Reventure Labs](https://reventurelabs.com).

## License

MIT — see [LICENSE](./LICENSE).
