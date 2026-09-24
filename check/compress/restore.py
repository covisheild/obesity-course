"""Put back, word for word and in their original positions, the sentences the cold read proved were needed.

    python check/compress/restore.py --subject B0 C7 restore-lists/C7.txt
    python check/compress/restore.py --subject S01-R1 S01-R1-C03 restore-lists/S01-R1-C03.txt

Reads `<label>-prose.yml` (the original) and `<label>-pass1-prose.yml` (the cut) from the
book's working folder and writes `<label>-final-prose.yml`. The list file is looked for as
given, then inside the working folder.

The restore file lists one sentence-opening per line - enough words to identify it uniquely -
optionally prefixed with `field::` to limit it to one field. Blank lines and `#` comments are
ignored.

Why a script rather than an edit. Step 3 of the pass says: put back the original's own
sentences, word for word, in their original positions, and write nothing new. Doing that by
hand is how a restorer ends up writing a bridging clause "just to make it read". So the
rebuild walks the **original** field from the top and keeps a sentence if the cutter kept it
or the restore list names it. Position, wording and paragraph structure are then the
original's by construction, and the only judgement left in the step is which sentences to name.

**Sentence by sentence.** Naming one sentence brings back that sentence and nothing else. It
returns inside its own paragraph, between the kept sentences of that paragraph, in the
original order. (Until 23 September 2026 naming one sentence brought back its whole paragraph,
which put back more than the cold read had earned.) Markup inside a sentence - bold, italic,
code - comes back with it: the split is made on the original's raw text, at the same
boundaries `check/build.py` uses to measure it.

The units that are not plain paragraphs, and the rule for each:

  - a **list item** (`-`, `*`, `+`, `1.`) is a small paragraph with a marker: its surviving
    sentences are kept, the marker is kept, and an item with no surviving sentence goes.
  - a **block quote** (`>`) is a quotation of a source and is kept or restored whole: a
    half-quoted source says something the source did not.
  - a **table row** or **heading** outside a fence is kept if the cut kept that exact line
    or the restore list names it.
  - a **fenced block** (```working, ```table) comes back only if the cutter kept it, if the
    prose paragraph immediately before it got a sentence restored, or if the restore list names
    words inside it (added 24 Sep 2026: a table that follows another fence directly has no
    introducing paragraph, so it could not be restored at all; S02-R1 C15). It comes back whole. A block belongs to the
    sentence that introduces it, and restoring an introduction without its arithmetic - or
    arithmetic without its introduction - is how this step produces something neither version
    ever said.

A unit whose every sentence survives is copied byte for byte, line breaks included. Only a
paragraph that lost a sentence is re-wrapped, and re-wrapping changes line breaks and nothing
else. Nothing kept by the cut can be lost: `validate.py` checks that every sentence, row and
block of `-pass1-prose.yml` is still in `-final-prose.yml`.
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _book import Book, build, take_opts  # noqa: E402

BULLET = build.BULLET
MARKUP = "*_`"


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()


def sentences_of(text):
    return [norm(s) for p in build._paragraphs(str(text)) for s in build._sentences(p) if norm(s)]


def raw_sentences(para):
    """build._sentences(para), but each piece cut from the raw text so its markup survives.

    build._sentences deletes `*_\\``, collapses whitespace, and splits. Walk the raw text
    alongside that flattened string, so every flattened sentence maps back to a raw span; the
    span is then widened over any markup touching it (the `**` either side of "**Bold.**").
    The boundaries are therefore exactly the ones the measurement uses.
    """
    flat_chars, where = [], []
    prev_space = True
    for i, ch in enumerate(para):
        if ch in MARKUP:
            continue
        if ch.isspace():
            if prev_space:
                continue
            flat_chars.append(" ")
            where.append(i)
            prev_space = True
        else:
            flat_chars.append(ch)
            where.append(i)
            prev_space = False
    flat = "".join(flat_chars)
    out, pos = [], 0
    for s in build._sentences(para):
        k = flat.find(s, pos)
        if k < 0:                       # cannot happen unless build changes; fail loudly
            raise RuntimeError(f"sentence not found while mapping markup: {s[:60]!r}")
        a, b = where[k], where[k + len(s) - 1] + 1
        while a > 0 and para[a - 1] in MARKUP:
            a -= 1
        while b < len(para) and para[b] in MARKUP:
            b += 1
        out.append(" ".join(para[a:b].split()))
        pos = k + len(s)
    return out


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


def _wrap(text, first, rest, width):
    """Words re-flowed to width. Words are the original's; only the line breaks are new."""
    out, line, pre = [], "", first
    for word in text.split():
        if line and len(pre) + len(line) + 1 + len(word) > width:
            out.append(pre + line)
            line, pre = word, rest
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(pre + line)
    return "\n".join(out)


def units(chunk):
    """One blank-line-separated chunk -> [(kind, raw_lines)].

    kind: 'item' (list item, marker on its first line), 'quote', 'row' (table row),
    'heading', or 'para'. The chunk's first line decides, exactly as build._paragraphs
    decides: a chunk that opens with a list marker is a list, one that opens with `|` or `#`
    is rows or headings line by line, one that opens with `>` is one quote, anything else
    is one paragraph.
    """
    lines = [l for l in chunk.splitlines() if l.strip()]
    if not lines:
        return []
    first = lines[0].lstrip()
    if BULLET.match(lines[0]):
        out = []
        for line in lines:
            if BULLET.match(line) or not out:
                out.append(("item", [line]))
            else:
                out[-1][1].append(line)        # continuation of the item above
        return out
    if first.startswith(("|", "#")):
        return [("heading" if l.lstrip().startswith("#") else "row", [l]) for l in lines]
    if first.startswith(">"):
        return [("quote", lines)]
    return [("para", lines)]


def _item_parts(lines):
    """A list item's marker, its continuation indent, and its text with the marker removed."""
    m = BULLET.match(lines[0])
    marker = lines[0][:m.end()]
    cont = re.match(r"[ \t]*", lines[1]).group(0) if len(lines) > 1 else " " * len(marker)
    text = " ".join([lines[0][m.end():]] + [l.strip() for l in lines[1:]])
    return marker, cont, text


def cut_inventory(cut_text):
    """What the cut kept, in the same units the rebuild walks: sentences, lines, fences."""
    kept = set(sentences_of(cut_text))
    lines, fences = set(), set()
    for kind, raw in split_blocks(str(cut_text)):
        if kind == "fence":
            fences.add(norm(raw))
            continue
        for chunk in re.split(r"\n\s*\n", raw):
            for k, ls in units(chunk):
                lines.update(norm(l) for l in ls)
                if k == "item":
                    kept.update(norm(s) for s in raw_sentences(_item_parts(ls)[2]))
                elif k == "para":
                    kept.update(norm(s) for s in raw_sentences("\n".join(ls)))
                elif k == "quote":
                    kept.add(norm(" ".join(l.lstrip()[1:] if l.lstrip().startswith(">") else l
                                           for l in ls)))
    kept.discard("")
    return kept, lines, fences


def rebuild(original, cut_text, wanted):
    """The original, keeping each sentence the cut kept or `wanted` names, and nothing else."""
    kept, kept_lines, kept_fences = cut_inventory(cut_text)
    width = max((len(l) for l in str(original).splitlines()), default=96)

    def asked(s):
        n = norm(s)
        return any(w in n for w in wanted)

    out, prev_restored = [], False
    for kind, raw in split_blocks(str(original)):
        if kind == "fence":
            named = asked(raw) and norm(raw) not in kept_fences
            if norm(raw) in kept_fences or prev_restored or named:
                out.append(raw.rstrip("\n"))
            prev_restored = named
            continue

        pieces, restored_here = [], False
        for chunk in re.split(r"\n\s*\n", raw):
            lines_out = []
            for k, ls in units(chunk):
                if k in ("row", "heading"):
                    if norm(ls[0]) in kept_lines or asked(ls[0]):
                        lines_out.append(ls[0])
                        restored_here |= norm(ls[0]) not in kept_lines
                    continue
                if k == "quote":
                    body = " ".join(l.lstrip()[1:] if l.lstrip().startswith(">") else l
                                    for l in ls)
                    was_kept = (norm(body) in kept or any(norm(l) in kept_lines for l in ls)
                                or any(s in kept for s in sentences_of("\n".join(ls))))
                    if was_kept or asked(body):
                        lines_out += ls
                        restored_here |= not was_kept
                    continue
                if k == "item":
                    marker, cont, text = _item_parts(ls)
                else:
                    marker, cont, text = "", "", "\n".join(ls)
                sents = raw_sentences(text)
                keep = [s for s in sents if norm(s) in kept or asked(s)]
                restored_here |= any(norm(s) not in kept for s in keep)
                if not keep:
                    continue
                if len(keep) == len(sents):
                    lines_out += ls                     # untouched: byte for byte
                elif k == "item":
                    lines_out.append(_wrap(" ".join(keep), marker, cont, width))
                else:
                    ind = re.match(r"[ \t]*", ls[0]).group(0)
                    lines_out.append(_wrap(" ".join(keep), ind, ind, width))
            if lines_out:
                pieces.append("\n".join(lines_out))
        if pieces:
            out.append("\n\n".join(pieces))
        prev_restored = restored_here and bool(pieces)

    # A blank line between every block. Joining with a single newline glues a fenced block
    # onto the prose above it, and the sentence splitter then reads the arithmetic inside the
    # fence as part of the sentence before it - which the validator correctly reports as a
    # sentence that is not in the original.
    joined = "\n\n".join(p.rstrip("\n") for p in out if p.strip())
    return re.sub(r"\n{3,}", "\n\n", joined).strip() + "\n"


def read_list(listfile):
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
    return wanted


def restore(book, label, listfile):
    with open(book.f(f"{label}-prose.yml"), encoding="utf-8") as fh:
        o = yaml.safe_load(fh)
    with open(book.f(f"{label}-pass1-prose.yml"), encoding="utf-8") as fh:
        c = yaml.safe_load(fh)
    if not os.path.exists(listfile) and os.path.exists(book.f(listfile)):
        listfile = book.f(listfile)
    wanted = read_list(listfile)

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

    path = book.f(f"{label}-final-prose.yml")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        yaml.safe_dump(out, fh, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, width=10 ** 6)
    print(f"  {label}: +{gained} sentences -> {os.path.basename(path)}")


def main(argv):
    opts, args = take_opts(argv)
    if len(args) != 2:
        sys.exit(__doc__)
    restore(Book.from_opts(opts), args[0], args[1])


if __name__ == "__main__":
    main(sys.argv[1:])
