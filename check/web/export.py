"""Export frozen books to the website's book-reader format.

    python check/web/export.py B0 --out ../drharshmaheshwari/src/data/books/obesity-expertise
    python check/web/export.py --frozen --out ...      # every frozen book in map/BOOKS.yml

The reader on drharshmaheshwari.com (For Doctors > Books) reads one format, which this writes:

    <out>/series.json              the 196 books in build order, with status, Part and Part hue
    <out>/<id>/book.json           one book: title, version, date, colours, PDF link, outline
                                   (part -> section, with word counts), references, glossary
    <out>/<id>/sections/<rid>.json one section's blocks, in reading order

and copies every figure a book uses to <figures-out>/ (default check/_build/web/figures/), for
upload to Cloudflare R2 (`drhm-files`, under books/obesity-expertise/figures/). Figures and PDFs
never go into the website's git repository.

Nothing here changes a word of the book. The records are read directly, so practice, worked
answers, must-know points and the glossary arrive as separate fields the reader can make
interactive. The prose itself goes through check/build.py's own layer (`_prose`, `_notation`,
`_ids_to_labels`) and then pandoc, the same path the PDF takes, so superscripts, working blocks
and tables come out exactly as they print. The rendered HTML is then checked for the same leaks
`_caret_check` looks for: a literal caret or tilde, a record id, a repository path. Any of them
stops the export.
"""
import argparse
import html as _html
import json
import os
import re
import shutil
import struct
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
ROOT = os.path.dirname(CHECK)
sys.path.insert(0, CHECK)
sys.path.insert(0, os.path.join(CHECK, "pdf"))

import yaml  # noqa: E402

import build  # noqa: E402

FORMAT = 1
SERIES_SLUG = "obesity-expertise"
FILES = "https://files.drharshmaheshwari.com"
FIGURE_BASE = f"{FILES}/books/{SERIES_SLUG}/figures/"
SITE_BASE = f"/doctors/books/{SERIES_SLUG}/"


def _yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def slug(book_id):
    """The book's URL segment. The id is permanent, so the URL is too: B0 -> b0, S01-R1 -> s01-r1."""
    return book_id.lower()


def pdf_url(book_id, version):
    return f"{FILES}/books/{SERIES_SLUG}/{book_id}-v{version}.pdf"


# ---------------------------------------------------------------- pandoc

def _pandoc():
    exe = shutil.which("pandoc")
    if exe:
        return exe
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except Exception:
        sys.exit("pandoc is required (the PDF build needs it too): install pandoc, or pip install pypandoc_binary")


PANDOC = None
MARK = "<!--BLK:{}-->"


def to_html(chunks):
    """Many markdown chunks through one pandoc run, split back apart by marker comments."""
    global PANDOC
    PANDOC = PANDOC or _pandoc()
    src = "\n\n".join(f"{MARK.format(i)}\n\n{c}" for i, c in enumerate(chunks)) + f"\n\n{MARK.format(len(chunks))}\n"
    p = subprocess.run([PANDOC, "-f", "markdown-yaml_metadata_block", "-t", "html5", "--wrap=none"],
                       input=src, capture_output=True, text=True, check=True)
    out, parts = p.stdout, []
    for i in range(len(chunks)):
        a, b = out.index(MARK.format(i)) + len(MARK.format(i)), out.index(MARK.format(i + 1))
        parts.append(_tidy(out[a:b].strip()))
    return parts


def _tidy(h):
    # make_pdf.py does the same: pandoc's Working div becomes a class the page can style.
    h = re.sub(r'<div (?:data-)?custom-style="Working">', '<div class="working">', h)
    h = h.replace('<figcaption aria-hidden="true">', "<figcaption>")
    # Grid tables carry pandoc's column widths as inline styles; the reader sizes tables itself.
    h = re.sub(r'<colgroup>.*?</colgroup>', "", h, flags=re.S)
    return h


def inline(h):
    """A single paragraph's HTML without its <p> wrapper (headings, captions)."""
    m = re.fullmatch(r"<p>(.*)</p>", h.strip(), re.S)
    return m.group(1) if m else h


# ---------------------------------------------------------------- leaks

LEAKS = []


def leak_check(where, h):
    """build._caret_check, applied to every piece of HTML this writes rather than to one page."""
    text = _html.unescape(re.sub(r"<[^>]+>", "", h))
    for m in re.finditer(r"[\^~]", text):
        LEAKS.append(f"{where}: literal caret/tilde: ...{text[max(0, m.start() - 50):m.end() + 20]}...")
    for p in sorted(set(re.findall(r"(?<![/\w.])(?:sources|check|books)/[\w./-]+", text))):
        LEAKS.append(f"{where}: repository path reached the page: {p}")
    for i in sorted(set(re.findall(r"\b(?:B0|S\d\d)-R\d-[CK]\d\d\b", text))):
        LEAKS.append(f"{where}: record id reached the page: {i}")


# ---------------------------------------------------------------- glossary

def glossary():
    """prose/GLOSSARY.md rows: [{term, head, plain, ids}]. `head` is the term without its
    bracketed sense, which is what appears in running text."""
    rows = []
    with open(os.path.join(ROOT, "prose", "GLOSSARY.md"), encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("| "):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or cells[0] in ("Term",) or set(cells[0]) <= set("- "):
                continue
            ids = re.findall(r"(?:B0|S\d\d)-R\d-C\d\d", cells[2])
            if not ids:
                continue
            head = re.sub(r"\s*\([^)]*\)\s*$", "", cells[0]).strip()
            rows.append({"term": cells[0], "head": head, "plain": cells[1], "ids": ids})
    return rows


# Single words that are also ordinary English. A tap on "work" in "work out the rate" that
# offers the physics definition misleads; a missed tap costs nothing. So these are never marked,
# and a term is marked only as written (no plural), and only from the section that teaches it on.
EVERYDAY = set("""
action argument authority base baseline bin bond boundary ceiling cell code comparison complement
conclusion condition correction counter definition deviation dimension distribution domain e element
energy entry equation error estimate evaluate event evidence executive expression feasible feedback
flow fluency frame function gap graph heat identity impossible implausible independent instrument
interest item learning length lever limit linear locate management margin mark mean measurement memo
menu move objective origin outcome parameter passage performance population power premise probe
programme prompt protocol range rate reaction reference regulation resolution rise rule run sample
scale scheme shape size solution spacing stage standard statistic stock subject supply surroundings
system table temperature trace transmission turn unit variable weights window work
""".split())

SKIP_TAGS = {"a", "code", "sup", "sub", "h1", "h2", "h3", "h4", "h5", "h6", "table", "figure",
             "figcaption", "dfn", "button", "blockquote"}


def mark_terms(h, terms, seen, at=(0, 0)):
    """Wrap the first use in this section of each glossary term in <dfn data-g="i">.

    Only running prose is marked: never inside working blocks, tables, headings, quotations,
    links or citation marks. Matching is whole-word and exact; a term written with a capital
    (Act, ADP) matches only as written, a lower-case one in either case. A term is marked only at
    or after the section that first teaches it (`at` is this section's position).
    """
    if not terms:
        return h
    pat = re.compile(r"(?<![\w-])(" + "|".join(t["rx"] for t in terms) + r")(?![\w-])")
    index = {}
    for t in terms:
        index.setdefault(t["key"], t)

    out, stack = [], []
    for tok in re.split(r"(<[^>]+>)", h):
        if tok.startswith("<"):
            m = re.match(r"<(/?)(\w+)([^>]*)>", tok)
            if m and not tok.endswith("/>") and m.group(2) not in ("br", "img", "hr", "col"):
                name = m.group(2)
                skip = name in SKIP_TAGS or 'class="working"' in m.group(3) or 'class="cite"' in m.group(3)
                if m.group(1):
                    if stack:
                        stack.pop()
                else:
                    stack.append(skip)
            out.append(tok)
            continue
        if any(stack) or not tok.strip():
            out.append(tok)
            continue

        def rep(m):
            word = m.group(1)
            t = index.get(word.lower()) if word.lower() in index else None
            if t is None or (t["cased"] and word != t["head"]):
                return m.group(0)
            if t["key"] in seen or t["from"] > at:
                return m.group(0)
            seen.add(t["key"])
            return f'<dfn data-g="{t["gid"]}">{m.group(0)}</dfn>'
        out.append(pat.sub(rep, tok))
    return "".join(out)


def book_terms(book_id, number_of, recs, b0_label):
    """The glossary a book may use: terms first taught in this book or in an earlier one.

    Returns (entries for book.json, matchers for mark_terms). Several senses of one term are
    one entry with several senses; the reader shows them all, this book's own first.
    """
    mine_n = number_of.get(book_id, 0)
    groups = {}
    for row in glossary():
        books = {reader_book(i) for i in row["ids"]}
        if not any(number_of.get(b, 999) <= mine_n for b in books):
            continue
        key = row["head"].lower()
        if len(key) < 3 or key in EVERYDAY:
            continue
        first = min(position(i, recs, number_of) for i in row["ids"])
        where = ", ".join(sorted({label_for(i, recs, b0_label, number_of) for i in row["ids"]}))
        sense = {"term": row["term"], "plain": inline_md(row["plain"], recs, b0_label, number_of),
                 "where": where, "own": book_id in books}
        g = groups.setdefault(key, {"head": row["head"], "senses": [], "from": first})
        g["senses"].append(sense)
        g["from"] = min(g["from"], first)
    entries, matchers = [], []
    for gid, (key, g) in enumerate(sorted(groups.items())):
        g["senses"].sort(key=lambda s: not s["own"])
        entries.append({"term": g["head"], "senses": [{k: s[k] for k in ("term", "plain", "where")} for s in g["senses"]]})
        cased = g["head"] != g["head"].lower()
        rx = re.escape(g["head"]) if cased else "(?i:" + re.escape(g["head"]) + ")"
        matchers.append({"key": key, "head": g["head"], "cased": cased, "rx": rx, "gid": gid, "from": g["from"]})
    # Longest first, so "adipose tissue" wins over "tissue".
    matchers.sort(key=lambda t: -len(t["head"]))
    return entries, matchers


def position(rid, recs, number_of):
    """(book number, section sequence): where a record sits in the series' reading order."""
    return (number_of.get(reader_book(rid), 999), (recs.get(rid) or {}).get("sequence", 0))


def reader_book(rid):
    return "B0" if rid.startswith("B0") else rid.rsplit("-C", 1)[0]


def label_for(rid, recs, b0_label, number_of):
    r = recs.get(rid)
    if not r:
        return rid
    if rid.startswith("B0"):
        return f"Book 0, {b0_label.get(r.get('sequence'), rid)}"
    return f"Book {number_of.get(reader_book(rid), '?')}, section {r.get('sequence')}"


def inline_md(text, recs, b0_label, number_of):
    """Glossary cells: backticked ids become labels, backticks go, *italic* stays."""
    text = re.sub(r"`?\(?`?((?:B0|S\d\d)-R\d-C\d\d)`?\)?`?",
                  lambda m: f"({label_for(m.group(1), recs, b0_label, number_of)})", text)
    s = _html.escape(text.replace("`", ""))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)


# ---------------------------------------------------------------- figures

def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None, None
    return struct.unpack(">II", head[16:24])


# ---------------------------------------------------------------- one section

WORDS = re.compile(r"[A-Za-z0-9][\w'’.-]*")


def words(h):
    return len(WORDS.findall(_html.unescape(re.sub(r"<[^>]+>", " ", h))))


def block_html(blocks):
    """Every piece of reader-facing HTML in a section's blocks."""
    for b in blocks:
        for k in ("html", "prompt", "answer", "caption"):
            if b.get(k):
                yield b[k]
        for p in b.get("points") or []:
            yield p["html"]


def section_blocks(r, cites, label, book_id, recs, own, figs_used):
    """The blocks of one record, in the order check/build.py's concept_md prints them."""
    fix_ids = (lambda t: build._ids_to_labels(t, recs, own)) if book_id != "B0" else (lambda t: t)
    md, meta = [], []

    def add(kind, text, **kw):
        md.append(fix_ids(text))
        meta.append({"kind": kind, **kw})

    def prose(text):
        return build._prose(text)

    jl = "Worked journey: " if r.get("journey") else ""
    add("heading", build._notation(jl + r["name"]))
    asof = (r.get("review") or {}).get("as_of")
    if asof and r.get("concept_type") != "derivable":
        add("note", f"*Checked against the sources as they stood on {asof}.*")
    mark = cites.mark(r)
    refs = mark.strip("[]").split(", ") if mark else []
    add("prose", prose(r["definition"]["text"]), label="Definition", role="definition", refs=refs)
    add("prose", prose(r["simplified_explanation"]), label="In plain terms", role="plain")
    for f in (r.get("figures") or []):
        if not isinstance(f, dict) or not f.get("file"):
            continue
        path = os.path.join(build.FIGURES_DIR, f["file"])
        if not os.path.exists(path):
            sys.exit(f"{r['concept_id']}: figure {f['file']} is not in check/figures/")
        w, h = png_size(path)
        figs_used.add(f["file"])
        add("figure", build._notation(" ".join((f.get("caption") or "").split())),
            src=f["file"], alt=" ".join((f.get("alt") or "").split()), width=w, height=h)
    ills = build._illustrations(r)
    for n, ill in enumerate(ills, 1):
        lab = "Illustration" if len(ills) == 1 else f"Illustration {n}"
        nmark = cites.mark_numbers(ill)
        add("prose", prose(ill["body"]), label=lab, role="illustration",
            numbers=nmark.strip("[]").split(", ") if nmark else [])
        if (ill.get("analogy_breaks_when") or "").strip():
            add("prose", prose(ill["analogy_breaks_when"]), label="Where this picture breaks", role="breaks")
    mk = [q for q in (r.get("must_know") or []) if isinstance(q, dict) and (q.get("point") or "").strip()]
    for q in mk:
        add("point", prose(" ".join(q["point"].split())), tag=q.get("kind"), bearing=q.get("bearing"))
    if (r.get("common_misreading") or "").strip():
        add("prose", prose(r["common_misreading"]), label="Common misreading", role="misread")
    if (r.get("reporting_sentence") or "").strip():
        add("prose", prose(r["reporting_sentence"]), label="Reporting it", role="report")
    for i, ex in enumerate(r.get("exercises") or [], 1):
        add("q", prose(ex["prompt"]), group="exercise", n=i, type=ex.get("type"),
            confidence=bool(ex.get("confidence_first")))
        add("a", prose(ex["answer"]))
    prac = sorted([q for q in (r.get("practice") or []) if isinstance(q, dict)], key=lambda q: q.get("level", 0))
    for i, q in enumerate(prac, 1):
        add("q", prose(q["prompt"]), group="practice", n=i, level=q.get("level"))
        add("a", prose(q["answer"]))
    return md, meta


def assemble(md, meta, terms, rid, glossary_seen, at):
    """Pandoc, then fold the flat list into the section's block list."""
    htmls = to_html(md)
    blocks, mk = [], None
    heading = None
    for m, h in zip(meta, htmls):
        kind = m["kind"]
        where = f"{rid} {m.get('label') or kind}"
        leak_check(where, h)
        if kind == "heading":
            heading = inline(h)
            continue
        if kind == "figure":
            blocks.append({"t": "figure", "src": m["src"], "alt": m["alt"], "w": m["width"], "h": m["height"],
                           "caption": inline(h)})
            mk = None
            continue
        if kind == "point":
            if mk is None:
                mk = {"t": "mustknow", "points": []}
                blocks.append(mk)
            mk["points"].append({"html": mark_terms(h, terms, glossary_seen, at), "tag": m.get("tag"), "bearing": m.get("bearing")})
            continue
        mk = None
        if kind == "a":
            blocks[-1]["answer"] = mark_terms(h, terms, glossary_seen, at)
            continue
        if kind == "q":
            b = {"t": m["group"], "n": m["n"], "prompt": mark_terms(h, terms, glossary_seen, at)}
            if m["group"] == "exercise":
                b.update({"type": m["type"], "confidence": m["confidence"]})
            else:
                b["level"] = m["level"]
            blocks.append(b)
            continue
        if kind == "note":
            blocks.append({"t": "note", "html": h})
            continue
        b = {"t": "prose", "label": m["label"], "role": m["role"], "html": mark_terms(h, terms, glossary_seen, at)}
        if m.get("refs"):
            b["refs"] = [int(x) for x in m["refs"]]
        if m.get("numbers"):
            b["numberRefs"] = [int(x) for x in m["numbers"]]
        blocks.append(b)
    return heading, blocks


# ---------------------------------------------------------------- one book

def export_book(book_id, out, figures_out, recs, series, books):
    meta = build.book_meta(book_id)
    entry = next(b for b in books if b["id"] == book_id)
    if entry.get("status") != "frozen" or meta.get("status") != "frozen":
        sys.exit(f"{book_id} is not frozen; only frozen books are published")
    number_of = {b["id"]: b["number"] for b in books}
    outline = build.load_book0_outline()
    b0_label = {s["index"]: s["id"] for p in outline for s in p["sections"]}
    where = {s["index"]: (p, s) for p in outline for s in p["sections"]}

    rung_book = build.RUNG_BOOK.match(book_id)
    if book_id == "B0":
        mine = sorted([r for r in recs.values() if r.get("subject") == "B0"], key=lambda r: r.get("sequence", 0))
    else:
        subject, rung = rung_book.group(1), int(rung_book.group(2))
        mine = sorted([r for r in recs.values() if r.get("subject") == subject and r.get("rung") == rung],
                      key=lambda r: r.get("sequence", 0))
    own = {r["concept_id"]: r.get("sequence") for r in mine}

    entries, terms = book_terms(book_id, number_of, recs, b0_label)
    # Imported here so a missing WeasyPrint (which make_pdf does not import at module level) is no issue.
    import make_pdf
    t = make_pdf.theme(entry, series)

    bdir = os.path.join(out, slug(book_id))
    sdir = os.path.join(bdir, "sections")
    if os.path.isdir(sdir):
        shutil.rmtree(sdir)
    os.makedirs(sdir)

    cites = build.Cites(build._bib_entries())
    parts, refs, figs_used = [], [], set()
    cur = None

    def flush_refs(key):
        if not cites.order:
            return
        idents = list(cites.order)
        texts = to_html([cites._format(i) for i in idents])
        items = []
        for ident, h in zip(idents, texts):
            leak_check(f"{book_id} references {key}", h)
            items.append({"n": cites.num[ident], "html": inline(h)})
        refs.append({"part": key, "items": items, "note": inline(to_html([build.Cites.UNVERIFIED_NOTE])[0]) if cites.unverified else None})
        cites.order, cites.num, cites.unverified = [], {}, set()

    total_words = 0
    for r in mine:
        rid = r["concept_id"]
        if book_id == "B0":
            part, sec = where.get(r.get("sequence"), (None, None))
            if part and (cur is None or cur["id"] != part["letter"]):
                if cur is not None:
                    flush_refs(cur["id"])
                cur = {"id": part["letter"], "title": f"Part {part['letter']} · {part['title']}", "sections": []}
                parts.append(cur)
            label = sec["id"] if sec else str(r.get("sequence"))
        else:
            if cur is None:
                level = build.LEVELS[int(rung_book.group(2)) - 1]
                cur = {"id": f"R{rung_book.group(2)}", "title": f"Rung {rung_book.group(2)} · {level}", "sections": []}
                parts.append(cur)
            label = str(r.get("sequence"))
        seen = set()
        md, meta_ = section_blocks(r, cites, label, book_id, recs, own, figs_used)
        heading, blocks = assemble(md, meta_, terms, rid, seen, position(rid, recs, number_of))
        n_words = sum(words(h) for h in block_html(blocks))
        total_words += n_words
        sid = rid.lower()
        cur["sections"].append({"id": sid, "label": label, "title": heading, "words": n_words,
                                "practice": sum(1 for b in blocks if b["t"] in ("practice", "exercise"))})
        with open(os.path.join(sdir, f"{sid}.json"), "w", encoding="utf-8") as fh:
            json.dump({"format": FORMAT, "id": sid, "label": label, "title": heading, "part": cur["id"],
                       "blocks": blocks}, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    if cur is not None:
        flush_refs(cur["id"] if book_id == "B0" else "")

    # What this book stands on: the books its records point back to (concept and ground-floor deps).
    requires = sorted({reader_book(d) for r in mine for d in (r.get("concept_deps") or []) + (r.get("ground_floor_deps") or [])
                       if reader_book(d) != book_id and d in recs}, key=lambda b: number_of.get(b, 999))

    about = to_html([meta.get("why") or "", meta.get("how_to_read") or "", meta.get("prerequisites") or ""])
    for i, h in enumerate(about):
        leak_check(f"{book_id} book.yml", h)
    book = {
        "format": FORMAT,
        "id": book_id,
        "slug": slug(book_id),
        "url": f"{SITE_BASE}{slug(book_id)}/",
        "series": series["series_title"],
        "number": entry["number"],
        "title": meta["title"],
        "subtitle": meta.get("subtitle"),
        "coverLine": meta.get("cover_line"),
        "subject": entry.get("subject"),
        "level": entry.get("level"),
        "part": entry.get("part"),
        "hue": t["hue"],
        "colours": {k: t[k] for k in ("ink", "accent", "accent2", "tint", "tint2", "rule")},
        "version": str(meta["version"]),
        "date": str(meta["last_updated"]),
        "author": series["author"],
        "licence": "CC BY-NC-SA 4.0",
        "pdf": pdf_url(book_id, meta["version"]),
        "figureBase": FIGURE_BASE,
        "about": {"why": about[0], "howToRead": about[1], "prerequisites": about[2] or None},
        "blurb": " ".join((meta.get("back_blurb") or "").split()),
        "requires": requires,
        "words": total_words,
        "outline": parts,
        "references": refs,
        "glossary": entries,
    }
    with open(os.path.join(bdir, "book.json"), "w", encoding="utf-8") as fh:
        json.dump(book, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    os.makedirs(figures_out, exist_ok=True)
    for f in sorted(figs_used):
        shutil.copy2(os.path.join(build.FIGURES_DIR, f), os.path.join(figures_out, f))
    n_sec = sum(len(p["sections"]) for p in parts)
    print(f"  {book_id}: {n_sec} sections, {total_words} words, {len(figs_used)} figures, "
          f"{len(entries)} glossary terms -> {bdir}")
    return figs_used


def export_series(out, series, books):
    rows = []
    for b in books:
        rows.append({k: b.get(k) for k in ("number", "id", "title", "subject", "part", "level", "tier", "status")}
                    | {"slug": slug(b["id"]), "hue": series["hues"].get(b.get("part"))})
    data = {"format": FORMAT, "title": series["series_title"], "subtitle": series["series_subtitle"],
            "url": SITE_BASE, "hues": series["hues"], "books": rows}
    with open(os.path.join(out, "series.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("books", nargs="*", help="book ids, e.g. B0 S01-R1")
    ap.add_argument("--frozen", action="store_true", help="every frozen book in map/BOOKS.yml")
    ap.add_argument("--out", default=os.path.join(CHECK, "_build", "web", "books"))
    ap.add_argument("--figures-out", default=os.path.join(CHECK, "_build", "web", "figures"))
    a = ap.parse_args()

    series = _yaml(os.path.join(CHECK, "pdf", "series.yml"))
    books = _yaml(os.path.join(ROOT, "map", "BOOKS.yml"))["books"]
    ids = [b["id"] for b in books if b.get("status") == "frozen"] if a.frozen else a.books
    if not ids:
        ap.error("name a book id or pass --frozen")
    recs = build.load_records()
    os.makedirs(a.out, exist_ok=True)
    export_series(a.out, series, books)
    for bid in ids:
        export_book(bid, a.out, a.figures_out, recs, series, books)
    if LEAKS:
        print(f"\n{len(LEAKS)} leak(s) in the rendered HTML; nothing a reader sees may carry these:")
        for l in LEAKS[:40]:
            print("  " + l)
        sys.exit(1)


if __name__ == "__main__":
    main()
