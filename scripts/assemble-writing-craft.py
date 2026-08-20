#!/usr/bin/env python3
"""Reassemble rl-writing-craft into ONE self-contained document.

`skills/rl-writing-craft/SKILL.md` is a navigation file; the rules live in four
sibling files loaded on demand. Downstream consumers that need a single blob --
a Brightsy skill, a claude.ai upload, any single-prompt target -- must vendor the
assembled document, NOT SKILL.md alone. Vendoring SKILL.md by itself ships a
skill containing no rules.

    python3 scripts/assemble-writing-craft.py > /tmp/writing-craft.md

Output is the canonical single-document form: frontmatter stripped, the
Function Reference nav table removed, the four function files inlined in order,
and their cross-references restored to "(see above)".
"""
import pathlib, re, sys

D = pathlib.Path(__file__).resolve().parents[1] / "skills" / "rl-writing-craft"
FOOTER = re.compile(r"\n*---\n\nPart of the `rl-writing-craft` skill\..*?author-voice skill\.\n*$", re.S)
NAV = re.compile(r"\n---\n\n## Function Reference\n.*?(?=\n---\n\n## Running the Full Sequence)", re.S)
SEE_ABOVE = 'Run the Logical Consistency check (see `SKILL.md` → “Logical Consistency — Grave Errors”) on this pass too.'
SEE_ABOVE_WRAPPED = 'Consistency check (see `SKILL.md` → “Logical Consistency — Grave Errors”)\non this pass too.'

def body(name):
    t = (D / name).read_text()
    t = FOOTER.sub("", t)
    t = t.replace(SEE_ABOVE, "Run the Logical Consistency check (see above) on this pass too.")
    t = t.replace(SEE_ABOVE_WRAPPED, "Consistency check (see above) on this pass too.")
    return t.strip()

skill = (D / "SKILL.md").read_text()
skill = re.sub(r"^---\n.*?\n---\n", "", skill, count=1, flags=re.S)   # drop YAML frontmatter
skill = skill.replace(
    "\n\nEach function's full rules live in its own file next to this one — see "
    "[Function\nReference](#function-reference) below. Load the file for the function "
    "you're running.", "")
if not NAV.search(skill):
    sys.exit("error: Function Reference nav block not found -- SKILL.md structure changed")
skill = NAV.sub("", skill)

head, sep, tail = skill.partition("\n---\n\n## Running the Full Sequence")
if not sep:
    sys.exit("error: 'Running the Full Sequence' anchor not found")

parts = []
for n, f in enumerate(["structure.md", "edit.md", "audit.md", "copyedit.md"], 1):
    b = body(f)
    b = re.sub(r"^# Function: (`\w+`)", rf"## FUNCTION {n}: \1", b, count=1)
    parts.append(b)

print(head.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(parts)
      + "\n\n---\n\n## Running the Full Sequence" + tail.rstrip() + "\n")
