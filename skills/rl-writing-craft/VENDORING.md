# Vendoring rl-writing-craft downstream

`SKILL.md` is a **navigation file**, not the rules. Since v0.21.0 the four functions
live in `structure.md`, `edit.md`, `audit.md`, and `copyedit.md`, loaded on demand so a
single copyedit does not pull all four into context.

**Consequence for downstream consumers:** any target that needs one self-contained blob —
a Brightsy skill, a claude.ai upload, a single-prompt system — must vendor the *assembled*
document. Vendoring `SKILL.md` alone ships a skill containing no rules at all.

## Assemble

```bash
python3 scripts/assemble-writing-craft.py > writing-craft.md
```

Output is the canonical single-document form: frontmatter stripped, the Function Reference
nav table removed, the four function files inlined in order, and their `(see SKILL.md → …)`
cross-references restored to `(see above)`. Verified byte-identical to the pre-split file.

The script fails loudly if `SKILL.md`'s structure changes rather than emitting a partial
document. If it exits with an error, fix the script — do not hand-assemble.

## Known downstream consumers

| Consumer | Target | Adaptations |
|---|---|---|
| StoryCycle (`sc.writing-craft`) | Brightsy account skill | Estate wrapper + four in-body references, below |

### `sc.writing-craft` estate adaptations

Re-apply these four after assembling. They are the only in-body edits; everything else is
vendored verbatim.

1. **Voice-layer naming** — "content-generation skill (venture/brand lane) or your author-voice
   skill (personal lane)" becomes the per-type `sc.*-craft` skill (brand lane) or
   `sc.park-howell-voice` / `sc.sean-schroeder-voice` (author lane).
2. **Voice layer, step 2 of the sequence** — same substitution in the numbered pipeline.
3. **Voice-profile lookup** — `VOICE-PROFILE.md` at the repo root (produced by
   `rl-voice-discovery`) becomes the brand's `author_voice_profile` record, read via
   `sc.foundation-context`.
4. **Closing sourcing note** — the generic "a skill like `ann-handley-voice`" pointer becomes
   the estate's own: `sc.park-howell-voice` for StoryCycle and Park-methodology work,
   `sc.sean-schroeder-voice` for Sean's own writing, with ABT and Story Cycle element rules
   in `sc.abt-construction`, `sc.story-cycle-framework` and `sc.story-cycle-storyboard`
   outranking anything here. Name those slugs individually — a `sc.story-cycle-*` glob reads
   as a dangling slug to StoryCycle's `validate-skill-references`.

## Before you vendor

**Pull first.** Vendoring from a stale local checkout ships stale rules, and the staleness is
invisible downstream — the vendored copy looks complete. This has already happened once: the
Aug 18 2026 vendor of `sc.writing-craft` was taken from a checkout pinned behind
`origin/main`, and shipped to production without the studied-neutrality rule, the
read-it-aloud check, or the refreshed AI-vocabulary list.

```bash
git fetch origin && git status -sb   # confirm you are not behind before assembling
```

## Size and the review panel (v0.22.0)

v0.22.0 added the rules `rl-review-panel` cites — Reader Access, Persuasion Integrity,
Stakes, Titles, Narrative Pieces — plus two `edit`-pass rules, stress position and buried
action, and the assembled
document grew by about 1,300 words. A consumer that holds its vendored copy to a size
ceiling (StoryCycle's `sc.writing-craft` is baselined at net ≤0) has to decide what to
take before re-vendoring; the assembly script does not trim. For StoryCycle, two notes:

- The panel is content-only, so the new rules matter where content is reviewed.
- Narrative Pieces overlaps `sc.abt-construction`, `sc.story-cycle-framework` and
  `sc.case-study-craft`, which already outrank this skill there (adaptation 4). A
  StoryCycle panel's Storyteller should cite those skills, and this section can stay
  out of the vendored copy.
