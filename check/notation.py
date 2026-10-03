"""Which signs, marks and Greek letters a book uses, and where each first appears.

    python check/notation.py check/_build/S57-R1.md     # prints the inventory and any unknown symbol

Read by check/pdf/make_pdf.py (the "Symbols used in this book" page) and by check/build.py
(a warning for a symbol with no row in check/notation.yml). Added 28 Sep 2026 from the
statistics-book lessons: a first-time reader meets these signs with no help.
"""
import os
import re
import sys
import unicodedata

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "notation.yml")

SUPERS = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵀᵏᵗᶻ")
SUBS = set("₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₔₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ")
PRECOMPOSED = {"ȳ": "̄", "ŷ": "̂", "ā": "̄", "ē": "̄", "ō": "̄", "ū": "̄", "Ū": "̄"}
IGNORE = set("—–’‘“”…·•é¢£€₹")


def table():
    with open(TABLE, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _key(ch):
    if ch in SUPERS:
        return "ˣ"
    if ch in SUBS:
        return "ₓ"
    if ch in PRECOMPOSED:
        return PRECOMPOSED[ch]
    return ch


def inventory(md: str):
    """[(symbol, first heading it appears under)] in order of first use, and the unknown symbols.

    Scans reader text only: fenced code, HTML comments, link targets and the references list are
    skipped, so a URL's characters are not counted as notation.
    """
    known = table()
    # Code blocks first, whole (2 Oct 2026): record fences (```r norun) and the booklet's
    # pandoc fences (```{.r}); no-op on text without them. Then any other fence, as before.
    import codeblocks
    md = codeblocks.md_strip(codeblocks.strip(md))
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"\]\([^)]*\)", "]", md)
    seen, order, unknown = {}, [], set()
    heading = ""
    for line in md.split("\n"):
        h = re.match(r"^#{1,4}\s+(.*)", line)
        if h:
            heading = re.sub(r"\{[^}]*\}\s*$", "", h.group(1)).strip()
            if re.match(r"(?i)references|sources", heading):
                heading = "__skip__"
            continue
        if heading == "__skip__":
            continue
        found = []
        for ch in line:
            if ord(ch) < 128 or ch in IGNORE:
                continue
            cat = unicodedata.category(ch)
            k = _key(ch)
            if k in known or cat in ("Sm", "Mn") or "GREEK" in unicodedata.name(ch, "") \
                    or ch in SUPERS or ch in SUBS:
                found.append(k)
        if re.search(r"\^\S", line) or "<sup>" in line:
            found.append("ˣ")
        if re.search(r"P\([^)]*\s\|\s", line):
            found.append("|")
        if re.search(r"\w\s~\s[A-Z]", line):
            found.append("~")
        for k in found:
            if k not in seen:
                seen[k] = heading
                order.append(k)
                if k not in known:
                    unknown.add(k)
    return [(k, seen[k]) for k in order], unknown


def rows(md: str):
    """Rows for the PDF page, grouped sign / mark / greek, each with its first section."""
    known = table()
    inv, _ = inventory(md)
    out = []
    for kind in ("sign", "mark", "greek"):
        for k, where in inv:
            t = known.get(k)
            if t and t.get("kind") == kind:
                shown = {"ˣ": "x², 10⁻³", "ₓ": "x₁, CO₂", "̄": "x̄", "̂": "p̂"}.get(k, k)
                out.append((kind, shown, t["read"], t["meaning"], where))
    return out


if __name__ == "__main__":
    text = open(sys.argv[1], encoding="utf-8").read()
    inv, unknown = inventory(text)
    for k, w in inv:
        print(f"{k!r:8} {w}")
    if unknown:
        print("no row in check/notation.yml:", " ".join(sorted(unknown)))
