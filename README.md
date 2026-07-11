# Reventure Labs Content OS

A Claude Code skill suite for structured long-form writing and repo-driven
topic scouting.

Most people who build things don't write about them — not for lack of
anything to say, but because the work before the writing (finding a topic,
structuring it, knowing when it's actually done) is its own unglamorous task,
and that task is what loses the priority fight. This suite exists to make
that work cheap enough that publishing becomes routine instead of a rare
burst of motivation, without lowering the bar on what gets published.

It takes the opposite failure mode just as seriously: a draft that's fast to
produce and not worth reading. Every step in `rl-long-form-pipeline` exists
because skipping it produces a specific, known failure — drafting before the
goal is pinned down produces fluent-but-aimless copy, skipping an outline
gate means restructuring after the words are already written, and a
self-review from the same context that wrote the draft is the weakest
possible judge of it. Before anything reaches a human approval gate, the
pipeline runs a criteria-scored review and a blind adversarial pass — a
fresh, context-free reviewer whose only job is to try to kill the draft.

## Who needs what

**Everyone** gets `rl-long-form-pipeline`, `rl-writing-craft`, `rl-voice-discovery`,
and `AUTHOR-CONTEXT.md` — the writing process, the craft floor, and the voice
profile apply to any writer, technical or not.

**Developers with repos** also get `rl-repo-topic-scout` and, optionally, a
recurring scheduled digest built on top of it (see
[SCHEDULED-DIGEST-TEMPLATE.md](./SCHEDULED-DIGEST-TEMPLATE.md)) — these are
specifically for surfacing topics from what you've actually built: commits,
diffs, structural changes. If you don't have code repos, or don't want topics
sourced that way, skip both entirely. You can still run `/longform` directly
on your own topic ideas — `rl-repo-topic-scout` feeds `rl-long-form-pipeline`,
it isn't required by it.

## What's here

| Skill / command | What it does |
|---|---|
| `rl-long-form-pipeline` | Structured 10-step process for long-form content — blog posts, whitepapers, essays, case studies. Define, interview, brief, outline, draft, critique, revise, run the writing suite, refine, approve. Nothing ships until you explicitly say so. |
| `rl-repo-topic-scout` | Scans a repo's git history, README/CLAUDE.md, and structural changes to surface 3-5 grounded topic candidates — each with evidence, an angle, and a "why now." Hands the pick straight into the long-form pipeline. |
| `rl-writing-craft` | Self-contained writing-quality skill: structure (architecture, flow, opens, closes), edit (line-level cutting, grounding, rhythm, anti-AI removal), audit (dedicated anti-AI pattern sweep), and copyedit (grammar, punctuation, usage, consistency). General craft for any writer; layers under whatever author-voice skill you bring, which wins on register and rhythm. Works standalone too — it just won't impose a specific voice. |
| `rl-voice-discovery` | Builds `VOICE-PROFILE.md` from real writing samples (or a structured interview if none exist), validated against a test passage. A one-time discovery process, not a per-draft tool — `rl-long-form-pipeline` and `rl-writing-craft` already check for the resulting file wherever they reference "your author-voice skill." |
| `rl-context-discovery` | Builds or refreshes `AUTHOR-CONTEXT.md` — checks existing evidence (about page, published content, README/CLAUDE.md) first, then a guided interview specifically designed to get past generic first answers, validated against a hypothetical ranked topic shortlist. The guided version of the "ask once" fallback `rl-repo-topic-scout`/`rl-long-form-pipeline` already have. |
| `/longform` | Deterministic entry point for the 10-step long-form pipeline. |
| `/scout` | Deterministic entry point for repo topic scouting, handing its pick straight into `/longform`. |
| `/voice` | Deterministic entry point for building your voice profile. |
| `/context` | Deterministic entry point for building or refreshing `AUTHOR-CONTEXT.md`. |

`AUTHOR-CONTEXT.md` at the repo root is a blank template — who you write for,
why you write, and what "worth publishing" means to you. `rl-repo-topic-scout`
and `rl-long-form-pipeline` both read it before ranking or defining a topic,
so filling it in once keeps both skills consistent about who you're actually
writing for. Run `/context` for a guided version of filling it in, rather
than answering a single ad hoc question the first time a skill notices it's
still blank.

This suite doesn't bundle a content-generation skill or a closing-polish
skill — bring your own (or write one) if you want a tailored register beyond
what `rl-voice-discovery` produces. Only `rl-writing-craft` is a hard
dependency. Without a voice reference at all, `rl-long-form-pipeline` still
runs the full process (interview, brief, outline, adversarial review,
approval gate) and drafts directly from the brief/outline using
`rl-writing-craft`'s floor — you get a competent, neutral-voiced draft
instead of one tailored to a specific voice. The process doesn't degrade;
only the register does. Run `/voice` first if you want that register from
the start.

## Install

Custom skills in Claude Code are activated one of two ways: as a plugin
marketplace, or via symlinks into `~/.claude/`. Either works; pick whichever
fits your workflow.

**1. Clone this repo:**

```bash
git clone https://github.com/<your-fork-or-org>/reventure-content-os.git
```

**2a. Plugin marketplace (recommended for staying up to date via `git pull`):**

Add this repo as a local plugin marketplace source in Claude Code, then
install the `reventure-content-os` plugin from it. Pulling the repo picks up
any updates to the skills or commands automatically.

**2b. Symlinks (if you want to edit skills in place and have them live
instantly):**

```bash
ln -s /path/to/reventure-content-os/skills/rl-long-form-pipeline ~/.claude/skills/rl-long-form-pipeline
ln -s /path/to/reventure-content-os/skills/rl-repo-topic-scout   ~/.claude/skills/rl-repo-topic-scout
ln -s /path/to/reventure-content-os/skills/rl-writing-craft      ~/.claude/skills/rl-writing-craft
ln -s /path/to/reventure-content-os/skills/rl-voice-discovery    ~/.claude/skills/rl-voice-discovery
ln -s /path/to/reventure-content-os/skills/rl-context-discovery  ~/.claude/skills/rl-context-discovery
ln -s /path/to/reventure-content-os/commands/longform.md         ~/.claude/commands/longform.md
ln -s /path/to/reventure-content-os/commands/scout.md            ~/.claude/commands/scout.md
ln -s /path/to/reventure-content-os/commands/voice.md            ~/.claude/commands/voice.md
ln -s /path/to/reventure-content-os/commands/context.md          ~/.claude/commands/context.md
```

**3. Fill in your context.** Run `/context` for a guided interview (checks
existing evidence first, then asks with technique designed to get past
generic first answers), or open `AUTHOR-CONTEXT.md` at the repo root
directly and fill in the bracketed placeholders yourself if you already
know the answers — either way, do this before running `/scout` or
`/longform` for real.

**4. Optional: build your voice.** Run `/voice` if you want `/longform`
drafting in your own register instead of a neutral one — it'll ask for
writing samples (or interview you if you don't have any) and produce
`VOICE-PROFILE.md`.

## Credit

Built and maintained by [Reventure Labs](https://reventurelabs.com).

## License

MIT — see [LICENSE](./LICENSE).
