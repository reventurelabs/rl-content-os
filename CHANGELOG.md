# Changelog

All notable changes to the Reventure Labs Content OS plugin.

This project follows [Semantic Versioning](https://semver.org/). The `version`
field in `.claude-plugin/plugin.json` pins installs — it is bumped on every
release, or users keep their cached copy.

## 0.21.0 — 2026-08-20

Brings the plugin in line with current Claude Code plugin and Agent Skills
conventions. No behavior change to any writing process.

### Changed

- **Slash entry points are now skills.** Claude Code merged custom commands
  into skills, and the docs steer new plugins to `skills/`. The four files in
  `commands/` became dispatcher skills at `skills/{pipeline,scout,voice,context}/`.
  Each one now does nothing but invoke its underlying skill, instead of
  restating that skill's process in prose — the old wrappers carried their own
  summary plus a "where this summary and the skill differ, the skill wins"
  caveat, which is drift waiting to happen. `/pipeline`, `/scout`, `/voice`,
  and `/context` work exactly as before.
- **Dispatchers are user-invoke-only** (`disable-model-invocation: true`), so
  Claude reaches for the real skill instead of choosing between two
  near-identical descriptions of the same workflow.
- **`rl-writing-craft` split for progressive disclosure.** The docs cap a
  `SKILL.md` at ~500 lines; this one was 798 (48KB), and every function loaded
  even for a single copyedit. `SKILL.md` is now 201 lines, with each function's
  full rules in `structure.md`, `edit.md`, `audit.md`, and `copyedit.md`, loaded
  on demand. Rule text is unchanged — verified line-by-line against the base
  commit, the only differences being four headings promoted to H1 and four
  "(see above)" cross-references repointed at `SKILL.md`. The Aug-1 additions
  from #1 (studied-neutrality grounding rule, read-it-aloud rhythm check,
  expanded AI-vocabulary list) carry through into `edit.md` and `audit.md`.
- **Manifests filled out.** `plugin.json` gained `displayName`, `homepage`,
  `repository`, `license`, `keywords`, and `$schema`. `marketplace.json` gained
  `$schema`, an owner `url`, `category`, and `keywords`.
- **Dropped the redundant `skills` array** from the marketplace plugin entry.
  With `source: "./"`, an explicit list becomes the complete set, so a new skill
  would have silently failed to load until someone remembered to edit
  `marketplace.json`. The default `skills/` scan does the same job.
- **Removed the duplicated plugin `description`** from the marketplace entry;
  `plugin.json` is the single source. The two had already diverged.
- README install instructions rewritten: the marketplace path no longer needs a
  clone, and the claim that "command activation works differently from skill
  activation" is gone — it is no longer true.

### Added

- `.gitignore` covering `.DS_Store`, `__MACOSX/`, `*.zip`, and local settings.
- `license: MIT` on every skill (an Agent Skills spec field).
- This changelog.

### Removed

- **Five committed `.zip` skill archives.** Build output, tracked in git, padded
  with `__MACOSX` junk — and `rl-topic-scout.zip` had already gone stale against
  its own `SKILL.md`. Nothing in the plugin spec reads them.
- `commands/` — superseded by the dispatcher skills above.

### Notes

- The five `rl-*` content skills deliberately stay on the [Agent
  Skills](https://agentskills.io) spec's frontmatter fields, so they keep
  packaging for claude.ai and the Skills API. Only the four dispatchers use
  Claude Code-only fields.
- Skill `description` fields are capped at 1,536 characters (combined with
  `when_to_use`), not 1,024. The trim in 92e7e47 targeted a limit that doesn't
  exist at that number; the current descriptions all fit with headroom.
