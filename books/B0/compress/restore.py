"""Put back, word for word and in their original positions, the sentences the cold read proved were needed.

    python books/B0/compress/restore.py C7 restore-C7.txt

The restore file lists one sentence-opening per line - enough words to identify it uniquely -
optionally prefixed with `field::` to limit it to one field. Blank lines and `#` comments are
ignored.

Why a script rather than an edit. Step 3 of the pass says: put back the original's own
sentences, word for word, in their original positions, and write nothing new. Doing that by
hand is how a restorer ends up writing a bridging clause "just to make it read". So the
rebuild walks the **original** field from the top and keeps a sentence if the cutter kept it
or the cold read earned it back. Position, wording and paragraph structure are then the
original's by construction, and the only judgement left in the step is which sentences to name.

Fenced blocks are the awkward case and the rule for them is stated rather than guessed: a
```working or ```table block comes back only if the cutter kept it, or if the prose paragraph
immediately before it got a sentence restored. A block belongs to the sentence that
introduces it, and restoring an introduction without its arithmetic - or arithmetic without
its introduction - is how this step produces something neither version ever said.
"""
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "..", "check")))
import build  # noqa: E402

FENCE = re.compile(r"^\s*```", re.M)


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()


def sentences_of(text):
    return [norm(s) for p in build._paragraphs(str(text)) for s in build._sentences(p) if norm(s)]


def split_blocks(text):
    """[(kind, raw)] where kind is 'fence' or 'prose', preserving order and indentation."""
    out, buf, in_fence = [], [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            if in_fence:
                buf.append(line)
                out.append(("fence", "".join(buf)))
                buf, in_fence = [], False
            else:
                if buf:
                    out.append(("prose", "".join(buf)))
                buf, in_fence = [line], True
            continue
        buf.append(line)
    if buf:
        out.append(("fence" if in_fence else "prose", "".join(buf)))
    return out


def _wrap(sentences, indent, width):
    """One paragraph, re-wrapped. Words are the original's; only the line breaks are new."""
    out, line = [], ""
    for word in " ".join(sentences).split():
        if line and len(line) + 1 + len(word) > width:
            out.append(indent + line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(indent + line)
    return "\n".join(out)


def rebuild(original, cut_text, wanted):
    """The original's paragraphs, minus the ones neither the cutter nor the cold read kept.

    Paragraphs are rebuilt from their surviving sentences and re-wrapped, rather than having
    the dead sentences spliced out of the raw text. Splicing leaves the remainder of a
    paragraph hanging off a stray space and wrapped to line breaks that belonged to sentences
    no longer there - " The form\nit is stated in does not matter." - which is not the
    original's prose and is not anybody's. Re-wrapping changes line breaks and nothing else,
    so every word and every sentence is still the original's, which is what the validator
    checks.
    """
    kept = set(sentences_of(cut_text))
    # Bullets, quotes and table rows are matched as whole lines as well as by sentence. The
    # sentence set above comes from build._paragraphs, which strips list markers and skips
    # tables, so a kept bullet's "- adding ..." never matched its own "adding ...", and a
    # kept table row matched nothing. Every kept bullet, quote and table was silently dropped
    # (found 23 Sep 2026 in A7, C2 and C9, already written back).
    kept_lines = {norm(l) for l in str(cut_text).splitlines() if l.strip()}
    kept_fences = {norm(b) for k, b in split_blocks(str(cut_text)) if k == "fence"}
    indent = re.match(r"[ \t]*", str(original).lstrip("\n")).group(0)
    width = max((len(l) for l in str(original).splitlines()), default=96)
    out, prev_restored = [], False

    for kind, raw in split_blocks(str(original)):
        if kind == "fence":
            if norm(raw) in kept_fences or prev_restored:
                out.append(raw.rstrip("\n") + "\n")
            continue

        pieces, restored_here = [], False
        for chunk in re.split(r"\n\s*\n", raw):
            if not chunk.strip():
                continue
            body = chunk.strip("\n")
            first = body.lstrip()
            # Bullets, block quotes and headings are kept or dropped whole: they are one
            # unit of meaning and re-wrapping one would destroy its markers.
            atomic = first.startswith(("-", "*", "+", ">", "#", "|")) or "\n" in body and all(
                l.lstrip().startswith(("-", "*", "+", ">")) for l in body.splitlines() if l.strip())
            sents = [s for s in build._sentences(body) if norm(s)]
            asked = any(any(w in norm(s) for w in wanted) for s in sents)
            if asked:
                restored_here = True
            if atomic:
                if (asked or any(s in kept for s in sentences_of(body))
                        or any(norm(l) in kept_lines for l in body.splitlines() if l.strip())):
                    pieces.append(body)
                continue
            if asked:
                pieces.append(_wrap(sents, indent, width))
                continue
            alive = [s.strip() for s in sents if norm(s) in kept]
            if alive:
                pieces.append(_wrap(alive, indent, width))

        if pieces:
            out.append("\n\n".join(pieces) + "\n")
        prev_restored = restored_here and bool(pieces)

    # A blank line between every block. Joining with a single newline glues a fenced block
    # onto the prose above it, and the sentence splitter then reads the arithmetic inside the
    # fence as part of the sentence before it - which the validator correctly reports as a
    # sentence that is not in the original.
    joined = "\n\n".join(p.rstrip("\n") for p in out if p.strip())
    return re.sub(r"\n{3,}", "\n\n", joined).strip() + "\n"


def main(label, listfile):
    o = yaml.safe_load(open(os.path.join(HERE, f"{label}-prose.yml"), encoding="utf-8"))
    c = yaml.safe_load(open(os.path.join(HERE, f"{label}-pass1-prose.yml"), encoding="utf-8"))

    wanted = {}
    with open(listfile, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#")[0].strip()
            if not line:
                continue
            field, sep, text = line.partition("::")
            if not sep:
                field, text = "*", field
            wanted.setdefault(field.strip(), []).append(norm(text))

    unused = {w for ws in wanted.values() for w in ws}
    out, gained = {}, 0
    for k, original in o.items():
        want = wanted.get(k, []) + wanted.get("*", [])
        before = len(sentences_of(c.get(k, "")))
        text = rebuild(str(original), c.get(k, ""), want)
        for w in want:
            if w in norm(text):
                unused.discard(w)
        after = len(sentences_of(text))
        gained += after - before
        if after != before:
            print(f"    {k}: {before} -> {after}")
        out[k] = text

    if unused:
        print("  WARNING - these restore lines matched nothing:")
        for u in sorted(unused):
            print(f"    {u[:70]}")

    path = os.path.join(HERE, f"{label}-final-prose.yml")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        yaml.safe_dump(out, fh, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, width=10 ** 6)
    print(f"  {label}: +{gained} sentences -> {os.path.basename(path)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
