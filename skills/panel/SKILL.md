---
name: panel
description: Run the blind review panel on a content draft — structure and stakes, claims, the reader's access, honest persuasion, and story for narrative pieces — and get back one consolidated list of diagnoses.
argument-hint: '<the draft, or a path to it> [--light]  e.g. "drafts/turnover-tax.md"'
disable-model-invocation: true
license: MIT
---

Invoke the `rl-review-panel` skill now and run it on the draft named below. That
skill file is the only source of truth for the lenses, the finding format, and
how the Keeper consolidates — read it and follow it rather than working from
memory.

**Request:** $ARGUMENTS

Default is blind and parallel: each lens in its own fresh sub-agent. `--light`
runs every lens in one fresh agent instead. The panel reviews content only; if
the draft is a strategy document, a brand foundation, a voice profile, a brief,
or a plan, say so and stop.
