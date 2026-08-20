---
name: pipeline
description: Run the structured content pipeline on a long-form or high-stakes piece — define, interview, brief, outline, draft, critique, revise, writing suite, refine, approve.
argument-hint: <venture>, <format>, <topic>  e.g. "Reventure Labs blog post, why AI rollouts stall on sequencing not technology"
disable-model-invocation: true
license: MIT
---

Invoke the `rl-content-pipeline` skill now and run its full 10-step sequence in
order. That skill file is the only source of truth for the process — read it and
follow it rather than working from memory, and don't collapse the sequence into
an ad-hoc draft.

**Request:** $ARGUMENTS

If venture, format, or topic is missing above, infer them from context and ask
only what's genuinely ambiguous.
