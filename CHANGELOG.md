# Changelog

All notable changes to the Reventure Labs Content OS plugin.

This project follows [Semantic Versioning](https://semver.org/). The `version`
field in `.claude-plugin/plugin.json` pins installs — it is bumped on every
release, or users keep their cached copy.

## 0.22.0 — 2026-09-28

### Added

- **`rl-review-panel`**, a blind review panel for finished content drafts, and its
  `/panel` dispatcher. Four lenses — Architect, Checker, Stranger, Conscience — plus a
  Storyteller for narrative pieces each read the draft in their own fresh context and
  return diagnoses, never rewrites. A non-voting Keeper states what the piece is
  before they read and merges their findings after. A finding counts only if it cites
  an `rl-writing-craft` rule or reports an observable effect on a reader; style
  prescriptions without either are dropped. Content only: strategy documents, brand
  foundations, voice profiles, briefs, and plans are out of scope. Line-level lenses
  (cutting, rhythm, specificity) are deliberately not seated — `rl-writing-craft`'s
  `edit` pass already runs them at step 8, after revision has settled the sentences.
- **New `rl-writing-craft` rules**, in the house test-and-fix format. The panel cites the
  first, second and fourth groups; the third belongs to the `edit` pass:
  - `edit.md` → **Reader Access**: unintroduced reference, undefined insider term
    (including one concept under several names), skipped step, condescension.
  - `edit.md` → **Persuasion Integrity**: manufactured urgency and disproportionate
    fear (HARD STOP); bait framing, unverifiable social proof, insecurity lever
    (STRONG FLAG).
  - `edit.md` → **End on the new information** (stress position) and **Buried action**
    (nominalization).
  - `structure.md` → **Stakes**, **Titles**, and a conditional **Narrative Pieces**
    section.
  - `audit.md` severity tiers list the new rules.

### Changed

- `rl-content-pipeline` step 6 runs a fourth pass, the panel pass. The re-check after
  step 7 re-runs only the lenses that raised a P0 or P1; panel findings are written into
  the fix in the author's voice, not pasted. Step 9 ends with the Keeper's voice check on
  everything revision and the suite changed, since both rewrite sentences.
- `edit.md` → AI connective tissue now states its boundary with Skipped step: cut a
  connective that announces a link the text already makes; supply one that's missing.

### Fixed

- `edit.md` → Grounding Rules said "Eight rules… the first five are HARD STOPS." It
  lists nine, six of them HARD STOPs.

### Downstream

- The assembled `rl-writing-craft` grows by about 1,300 words (7,365 → 8,669). Size
  is a guideline, not a hard limit: a consumer re-vendoring it should weigh the added
  length against what the rules buy, not refuse them on size alone. See `VENDORING.md`.

## 0.21.2 — 2026-08-20

### Fixed

- `VENDORING.md` adaptation 4 spelled the Story Cycle skills as a `sc.story-cycle-*`
  glob, which StoryCycle's `validate-skill-references` reads as a dangling slug. Names
  `sc.story-cycle-framework` and `sc.story-cycle-storyboard` individually, so the next
  re-vendor doesn't reintroduce the warning.

## 0.21.1 — 2026-08-20

### Added

- `scripts/assemble-writing-craft.py` and `skills/rl-writing-craft/VENDORING.md`.
  The v0.21.0 split made `SKILL.md` a navigation file, which silently broke the recipe
  downstream consumers use to vendor this skill as a single blob — following the
  documented path now yields a skill with no rules in it. The script reassembles the
  five files into the canonical single document (verified byte-identical to the
  pre-split original); `VENDORING.md` records the recipe, the four adaptations
  StoryCycle's `sc.writing-craft` re-applies, and a `git fetch` step, because the
  Aug 18 vendor was taken from a checkout behind `origin/main` and shipped without
  the studied-neutrality rule, the read-it-aloud check, or the refreshed vocabulary.

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
