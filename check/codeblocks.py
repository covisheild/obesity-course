"""Code fences in reader-facing prose: ```r, ```output and ```sh (added 2 Oct 2026 for S52-R1).

One parser, used by everything that reads a prose field, so that every tool agrees on where a
code block starts and ends:

    check/build.py           rendering (verbatim, monospace) and the exemptions below
    check/reader_checks.py   the numbers registry ({{n:key}} is never substituted inside code)
    check/compress/*.py      a code block is one atomic unit, never a run of sentences
    check/code_gate.py       runs the code and checks each ```output block against a fresh run

A code fence opens with three or more backticks, a tag and optional attributes:

    ```r                    R code, run by the code gate
    ```r norun              shown, never run (install.packages(), a personal absolute path)
    ```r file=code/x.R      the content of a script the reader saves; written, not run
    ```r error              expected to stop with an error (without it, an error fails the gate)
    ```output               what the r or sh block immediately above printed
    ```sh                   a shell command, run with bash in the project folder

and closes with a line of at least as many backticks and nothing else. Everything between is
verbatim: no notation layer, no escaping, no number substitution, no sentence checks. An untagged
fence, ```working, ```calc and ```table keep their meaning (display arithmetic and tables); this
module does not touch them.
"""
import re

CODE_TAGS = ("r", "output", "sh")
RUNNABLE = ("r", "sh")
OPEN = re.compile(r"^([ \t]*)(`{3,})[ \t]*(r|output|sh)(?=[ \t]|$)([^`\n]*?)[ \t]*$")
ATTR = re.compile(r"^(?:norun|error|file=[^\s]+)$")
# Any fence line with a word tag. Used only to report a tag nobody knows (```R, ```python).
ANY_TAGGED = re.compile(r"^[ \t]*`{3,}[ \t]*([A-Za-z][\w+-]*)\b")
KNOWN_TAGS = ("working", "calc", "table") + CODE_TAGS


def parse_open(line):
    """The opening line of a code fence -> {indent, fence, tag, attrs, bad} or None."""
    m = OPEN.match(line)
    if not m:
        return None
    attrs, bad = {}, []
    for tok in m.group(4).split():
        if not ATTR.match(tok):
            bad.append(tok)
        elif tok.startswith("file="):
            attrs["file"] = tok[5:]
        else:
            attrs[tok] = True
    return {"indent": len(m.group(1).expandtabs()), "fence": m.group(2), "tag": m.group(3),
            "attrs": attrs, "bad": bad}


def _closes(line, fence):
    s = line.strip()
    return len(s) >= len(fence) and set(s) == {"`"}


def has_code(text):
    """Cheap test first: no backtick fence, no code. Records without code pay only this."""
    if not isinstance(text, str) or "```" not in text:
        return False
    return any(OPEN.match(l) for l in text.split("\n"))


def blocks(text):
    """Every code block in a text, in order.

    Each is a dict: tag, attrs, bad (unknown attribute tokens), open (the opening line), body
    (list of lines, the fence's own indent removed), start and end (line indexes of the opening
    and closing fence; end is None for an unclosed fence, which runs to the end of the text).
    """
    out, lines, i = [], str(text).split("\n"), 0
    while i < len(lines):
        o = parse_open(lines[i])
        if not o:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not _closes(lines[j], o["fence"]):
            j += 1
        body = []
        for l in lines[i + 1:j]:
            k = len(l) - len(l.lstrip(" "))
            body.append(l[min(k, o["indent"]):])
        out.append({**o, "open": lines[i], "body": body, "start": i,
                    "end": j if j < len(lines) else None})
        i = j + 1
    return out


def segments(text):
    """[("text", str) | ("code", block)] in order; joining the text parts and the blocks' raw
    lines with newlines gives the original back."""
    lines, out, pos = str(text).split("\n"), [], 0
    for b in blocks(text):
        if b["start"] > pos:
            out.append(("text", "\n".join(lines[pos:b["start"]])))
        out.append(("code", b))
        pos = (b["end"] if b["end"] is not None else len(lines) - 1) + 1
    if pos < len(lines):
        out.append(("text", "\n".join(lines[pos:])))
    return out


def strip(text):
    """The text with every code block replaced by a blank line: what prose checks should see.
    Identical to the input when there is no code block."""
    if not has_code(text):
        return text
    out = []
    for kind, part in segments(text):
        out.append(part if kind == "text" else "")
    return "\n".join(out)


def outside(text, fn):
    """Apply fn to the parts of text that are not code; code passes through untouched."""
    if not has_code(text):
        return fn(text)
    out = []
    for kind, part in segments(text):
        if kind == "text":
            out.append(fn(part))
        else:
            lines = str(text).split("\n")
            end = part["end"] if part["end"] is not None else len(lines) - 1
            out.append("\n".join(lines[part["start"]:end + 1]))
    return "\n".join(out)


def pairs(text):
    """[(code_block, output_block_or_None)] for r/sh blocks, plus the orphans:
    output blocks that do not immediately follow an r/sh block (blank lines between allowed)."""
    lines, bl = str(text).split("\n"), blocks(text)
    res, orphans, used = [], [], set()
    for n, b in enumerate(bl):
        if b["tag"] not in RUNNABLE:
            continue
        nxt = bl[n + 1] if n + 1 < len(bl) else None
        follows = (nxt is not None and nxt["tag"] == "output" and b["end"] is not None
                   and all(not l.strip() for l in lines[b["end"] + 1:nxt["start"]]))
        res.append((b, nxt if follows else None))
        if follows:
            used.add(n + 1)
    for n, b in enumerate(bl):
        if b["tag"] == "output" and n not in used:
            orphans.append(b)
    return res, orphans


def unknown_tags(text):
    """Fence tags nobody renders (```R, ```python): they would reach the page through the
    notation layer, with every caret escaped."""
    if not isinstance(text, str) or "```" not in text:
        return []
    return sorted({m.group(1) for l in text.split("\n") for m in [ANY_TAGGED.match(l)]
                   if m and m.group(1) not in KNOWN_TAGS})


# ---------------------------------------------------------------- markdown for the renderer

MD_CLASS = {"r": "{.r}", "sh": "{.bash}", "output": "{.output}"}
MD_OPEN = re.compile(r"^[ \t]*(`{3,})\{\.(?:r|bash|output)\}[ \t]*$")


def to_markdown(b):
    """A pandoc fenced code block, verbatim. pandoc gives it Word's Source Code style and an
    HTML <pre>; the class picks the PDF's style for code or output."""
    longest = max((len(m) for l in b["body"] for m in re.findall(r"`+", l)), default=0)
    fence = "`" * max(3, longest + 1)
    return ["", fence + MD_CLASS[b["tag"]], *b["body"], fence, ""]


def md_outside(md, fn):
    """Apply fn to an assembled booklet's markdown, leaving the code blocks this module wrote
    untouched. Identical to fn(md) when the booklet has none."""
    if "{.r}" not in md and "{.bash}" not in md and "{.output}" not in md:
        return fn(md)
    lines, out, buf, i = md.split("\n"), [], [], 0
    while i < len(lines):
        m = MD_OPEN.match(lines[i])
        if not m:
            buf.append(lines[i])
            i += 1
            continue
        if buf:
            out.append(fn("\n".join(buf)))
            buf = []
        j = i + 1
        while j < len(lines) and not _closes(lines[j], m.group(1)):
            j += 1
        out.append("\n".join(lines[i:j + 1]))
        i = j + 1
    if buf:
        out.append(fn("\n".join(buf)))
    return "\n".join(out)


def md_strip(md):
    """An assembled booklet's markdown with the code blocks this module wrote blanked out."""
    if "{.r}" not in md and "{.bash}" not in md and "{.output}" not in md:
        return md
    lines, out, i = md.split("\n"), [], 0
    while i < len(lines):
        m = MD_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not _closes(lines[j], m.group(1)):
            j += 1
        out.append("")
        i = j + 1
    return "\n".join(out)
