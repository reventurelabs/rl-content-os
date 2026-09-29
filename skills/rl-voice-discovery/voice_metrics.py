#!/usr/bin/env python3
"""Measure a writer's surface style, and check whether a revision moved away from it.

Deterministic counts, not a model's estimate — an LLM asked for "comma density per 100
words" guesses; this counts. Standard library only.

Profile one or more texts (writes the numbers `rl-voice-discovery` puts in VOICE-PROFILE.md):

    python3 voice_metrics.py samples/*.md
    python3 voice_metrics.py --block samples/*.md      # markdown block ready to paste

Compare a revision against the writer's baseline (the review panel's Keeper uses this):

    python3 voice_metrics.py --baseline VOICE-PROFILE.md before.md after.md
    python3 voice_metrics.py --baseline samples/*.md -- before.md after.md

`--baseline` takes sample texts, or a file containing a block written by `--block`
(VOICE-PROFILE.md). With a baseline and two texts, every metric where the second text sits
further from the baseline than the first is marked AWAY. That is a question for the writer,
not a verdict: a revision can move away for a good reason.
"""
import json, math, re, sys

BEGIN, END = "<!-- voice-metrics:begin -->", "<!-- voice-metrics:end -->"

FUNCTION_WORDS = """the of and to a in that is it for on with as was but be at by this
not are from or have an they which you we he she his her their its if so what there
all would about can will just than then also because when some only very how more
no out up into do could who""".split()

HEDGES = ["maybe", "perhaps", "might", "possibly", "probably", "likely", "seems", "seem",
          "somewhat", "arguably", "i think", "i guess", "i suspect", "in my experience",
          "sort of", "kind of", "a bit", "fairly", "rather"]
INTENSIFIERS = ["very", "really", "just", "quite", "actually", "truly", "extremely"]
CONTRACTION = re.compile(r"\b\w+(?:n't|'re|'ll|'ve|'m|'d)\b|\b(?:it|that|there|here|what|let|who|he|she)'s\b", re.I)
WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")

# Metric name -> (label, format). Order is the report order.
METRICS = [
    ("sentence_mean", "Sentence length, mean (words)", "{:.1f}"),
    ("sentence_sd", "Sentence length, spread (SD)", "{:.1f}"),
    ("short_share", "Short sentences, ≤8 words (%)", "{:.0f}"),
    ("long_share", "Long sentences, ≥25 words (%)", "{:.0f}"),
    ("para_sentences", "Paragraph length (sentences)", "{:.1f}"),
    ("contractions_100", "Contractions per 100 words", "{:.2f}"),
    ("hedges_100", "Hedges per 100 words", "{:.2f}"),
    ("intensifiers_100", "Intensifiers per 100 words", "{:.2f}"),
    ("first_person_100", "I / me / my per 100 words", "{:.2f}"),
    ("second_person_100", "You / your per 100 words", "{:.2f}"),
    ("dash_1000", "Dashes per 1,000 words", "{:.1f}"),
    ("semicolon_1000", "Semicolons per 1,000 words", "{:.1f}"),
    ("colon_1000", "Colons per 1,000 words", "{:.1f}"),
    ("paren_1000", "Parentheses per 1,000 words", "{:.1f}"),
    ("question_1000", "Questions per 1,000 words", "{:.1f}"),
    ("exclaim_1000", "Exclamations per 1,000 words", "{:.1f}"),
    ("comma_100", "Commas per 100 words", "{:.2f}"),
    ("mattr", "Vocabulary variety (MATTR, 100-word window)", "{:.3f}"),
    ("fk_grade", "Flesch-Kincaid grade", "{:.1f}"),
]


def prose(text):
    """Keep running prose: drop code blocks, tables, headings, HTML tags, link targets."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    keep = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(("#", "|")) or re.fullmatch(r"[-*_]{3,}", s or "x"):
            keep.append("")
            continue
        keep.append(re.sub(r"^([-*+]|\d+\.)\s+", "", s).replace("**", "").replace("`", ""))
    return "\n".join(keep)


def sentences(par):
    parts = re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z0-9\"'(\[])", par.strip())
    return [p for p in parts if WORD.search(p)]


def syllables(word):
    w = word.lower()
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 and not w.endswith("le") else 0)
    return max(1, n)


def measure(text):
    body = prose(text)
    paragraphs = [p for p in re.split(r"\n\s*\n", body) if WORD.search(p)]
    sents = [s for p in paragraphs for s in sentences(p)]
    words = WORD.findall(body)
    n = len(words) or 1
    lens = [len(WORD.findall(s)) for s in sents] or [0]
    mean = sum(lens) / len(lens)
    sd = math.sqrt(sum((x - mean) ** 2 for x in lens) / len(lens))
    lower = body.lower()
    low_words = [w.lower() for w in words]
    stems = [w.split("'")[0] for w in low_words]  # "I'd" counts as "I", same as "I would"

    def per(count, base):
        return 100.0 * count / n if base == 100 else 1000.0 * count / n

    def phrase_count(phrases):
        return sum(len(re.findall(r"\b" + re.escape(p) + r"\b", lower)) for p in phrases)

    window = 100
    if len(low_words) > window:
        ttrs = [len(set(low_words[i:i + window])) / window for i in range(len(low_words) - window + 1)]
        mattr = sum(ttrs) / len(ttrs)
    else:
        mattr = len(set(low_words)) / n
    syl = sum(syllables(w) for w in words)
    fk = 0.39 * (n / max(1, len(sents))) + 11.8 * (syl / n) - 15.59
    fw = {w: 0 for w in FUNCTION_WORDS}
    for w in low_words:
        if w in fw:
            fw[w] += 1
    return {
        "words": len(words),
        "sentences": len(sents),
        "sentence_mean": mean,
        "sentence_sd": sd,
        "short_share": 100.0 * sum(1 for x in lens if x <= 8) / len(lens),
        "long_share": 100.0 * sum(1 for x in lens if x >= 25) / len(lens),
        "para_sentences": len(sents) / max(1, len(paragraphs)),
        "contractions_100": per(len(CONTRACTION.findall(body)), 100),
        "hedges_100": per(phrase_count(HEDGES), 100),
        "intensifiers_100": per(phrase_count(INTENSIFIERS), 100),
        "first_person_100": per(sum(1 for w in stems if w in ("i", "me", "my", "mine")), 100),
        "second_person_100": per(sum(1 for w in stems if w in ("you", "your", "yours")), 100),
        "dash_1000": per(len(re.findall(r"—|–|\s--\s", body)), 1000),
        "semicolon_1000": per(body.count(";"), 1000),
        "colon_1000": per(len(re.findall(r":(?!//)", body)), 1000),
        "paren_1000": per(body.count("("), 1000),
        "question_1000": per(body.count("?"), 1000),
        "exclaim_1000": per(body.count("!"), 1000),
        "comma_100": per(body.count(","), 100),
        "mattr": mattr,
        "fk_grade": fk,
        "function_words": {k: v / n for k, v in fw.items()},
    }


def cosine_distance(a, b):
    keys = FUNCTION_WORDS
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0) ** 2 for k in keys))
    return 1.0 - dot / (na * nb) if na and nb else 1.0


def load_baseline(paths):
    texts = []
    for p in paths:
        t = open(p, encoding="utf-8").read()
        m = re.search(re.escape(BEGIN) + r"\s*```json\s*(\{.*?\})\s*```\s*" + re.escape(END), t, re.S)
        if m:
            return json.loads(m.group(1))
        texts.append(t)
    return measure("\n\n".join(texts))


def block(m):
    slim = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in m.items() if k != "function_words"}
    slim["function_words"] = {k: round(v, 5) for k, v in m["function_words"].items()}
    lines = ["## Measured Baseline", "",
             "Counted by `voice_metrics.py` from the samples above — not estimated. The review panel's",
             "Keeper compares revisions against these numbers. Regenerate with `--block`; don't hand-edit.",
             "", "| Metric | Value |", "|---|---|"]
    for key, label, fmt in METRICS:
        lines.append(f"| {label} | {fmt.format(m[key])} |")
    lines += ["", f"*{m['words']} words, {m['sentences']} sentences.*", "", BEGIN, "```json",
              json.dumps(slim, indent=1), "```", END]
    return "\n".join(lines)


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--block":
        print(block(measure("\n\n".join(open(p, encoding="utf-8").read() for p in argv[1:]))))
        return 0
    if argv[0] == "--baseline":
        rest = argv[1:]
        if "--" in rest:
            i = rest.index("--")
            base_paths, texts = rest[:i], rest[i + 1:]
        else:
            base_paths, texts = rest[:-2] if len(rest) > 2 else rest[:1], rest[-2:] if len(rest) > 2 else rest[1:]
        if not base_paths or not texts:
            print("need a baseline and one or two texts", file=sys.stderr)
            return 2
        base = load_baseline(base_paths)
        ms = [measure(open(p, encoding="utf-8").read()) for p in texts]
        head = "| Metric | Baseline | " + " | ".join(texts) + (" | Revision |" if len(ms) == 2 else " |")
        print(head)
        print("|---" * (2 + len(ms) + (1 if len(ms) == 2 else 0)) + "|")
        away = 0
        for key, label, fmt in METRICS:
            row = [label, fmt.format(base[key])] + [fmt.format(m[key]) for m in ms]
            if len(ms) == 2:
                d0, d1 = abs(ms[0][key] - base[key]), abs(ms[1][key] - base[key])
                scale = max(abs(base[key]), 1.0)
                moved = (d1 - d0) / scale
                flag = "AWAY" if moved > 0.10 else ("toward" if moved < -0.10 else "—")
                away += flag == "AWAY"
                row.append(flag)
            print("| " + " | ".join(row) + " |")
        dists = [cosine_distance(base["function_words"], m["function_words"]) for m in ms]
        row = ["Function-word distance from baseline (0 = identical)", "0"] + [f"{d:.3f}" for d in dists]
        if len(ms) == 2:
            row.append("AWAY" if dists[1] > dists[0] * 1.10 + 0.002 else "—")
        print("| " + " | ".join(row) + " |")
        if len(ms) == 2:
            print(f"\n{away} of {len(METRICS)} metrics moved away from the baseline by more than 10%.")
        return 0
    m = measure("\n\n".join(open(p, encoding="utf-8").read() for p in argv))
    print(f"{m['words']} words, {m['sentences']} sentences\n")
    for key, label, fmt in METRICS:
        print(f"{label}: {fmt.format(m[key])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
