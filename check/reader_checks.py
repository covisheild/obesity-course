"""Checks added 28 Sep 2026 from the lessons of Harsh's statistics book
(project doc claude/lessons-from-stats-book.md). Called by check/build.py.

1. Running-numbers registry. `books/<ID>/numbers.yml` names every number a book reuses across
   sections (a cohort's size, a fitted slope, a prevalence). Prose writes {{n:key}} for its own
   book or {{n:S01-R1/key}} for another book's; load_records() substitutes the value, so one
   number cannot drift between sections. The statistics book printed r = 0.82 and R^2 = 0.62 for
   the same regression, and per month in one section, per year in another.
2. Banned boilerplate (check/banned_phrases.yml): filler and internal vocabulary.
3. A "recall" that points forward: prose recalling a section of the same book that comes later.
4. Wikipedia and similar sources: leads only, never a citation.
5. Version history kept out of the reader's book (Harsh, 28 Sep 2026): no "what's new" in book.yml.
6. What a new book must carry: prerequisites and a page budget in book.yml, a COVERAGE.md against
   outside standards, and at least one retrieval exercise per section.
7. Symbols a book prints that check/notation.yml cannot explain.

Books frozen before these rules (sourcegate.LEGACY) get warnings where a new book gets blocks.
"""
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
BOOKS = os.path.join(REPO, "books")
NUM = re.compile(r"\{\{n:(?:([A-Z0-9]+(?:-R\d)?)/)?([A-Za-z0-9_.\-]+)\}\}")
ID = re.compile(r"\b((?:B0|S\d\d)-R\d-C\d\d)\b")
RECALL = re.compile(r"(?i)\b(recall|as (?:we )?(?:saw|showed|found)|as (?:shown|covered|built|taught|derived) (?:in|earlier)|earlier in)\b[^.\n]{0,90}?\b((?:B0|S\d\d)-R\d-C\d\d)\b")
BAD_SOURCE = re.compile(r"(?i)wikipedia\.org|wikiwand|fandom\.com|quora\.com|reddit\.com|chatgpt|openai\.com/chat")
HISTORY = re.compile(r"(?i)what'?s new|new in (?:this )?version|change ?log|changes in version|previous version|since version \d")

NUMBER_ISSUES = []   # filled by apply_numbers, read by problems()


def book_of(rid_or_rec):
    rid = rid_or_rec if isinstance(rid_or_rec, str) else rid_or_rec.get("concept_id", "")
    m = re.match(r"^(B0|S\d\d-R\d)", rid)
    return "B0" if rid.startswith("B0") else (m.group(1) if m else "")


def _load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except FileNotFoundError:
        return {}


def registries():
    """{book_id: {key: entry}} from every books/<ID>/numbers.yml."""
    out = {}
    if not os.path.isdir(BOOKS):
        return out
    for b in sorted(os.listdir(BOOKS)):
        p = os.path.join(BOOKS, b, "numbers.yml")
        if os.path.exists(p):
            try:
                d = _load(p)
            except yaml.YAMLError as e:
                NUMBER_ISSUES.append(("block", b, f"books/{b}/numbers.yml does not parse: {e}"))
                continue
            nums = d.get("numbers") or {}
            for k, v in nums.items():
                if not isinstance(v, dict) or "value" not in v:
                    NUMBER_ISSUES.append(("block", b, f"numbers.yml: {k} has no value"))
            out[b] = {k: v for k, v in nums.items() if isinstance(v, dict) and "value" in v}
    return out


USED = set()


def apply_numbers(recs):
    """Replace {{n:key}} in every string of every record, except quotes (which are the source's
    own words). Unknown keys are reported; the marker is left so the page shows the fault."""
    reg = registries()

    def sub(text, rid):
        def rep(m):
            b = m.group(1) or book_of(rid)
            k = m.group(2)
            e = reg.get(b, {}).get(k)
            if e is None:
                NUMBER_ISSUES.append(("block", rid, f"{{{{n:{m.group(0)[4:-2]}}}}} is not in books/{b}/numbers.yml"))
                return m.group(0)
            USED.add((b, k))
            return str(e["value"])
        return NUM.sub(rep, text)

    def walk(node, rid, key=None):
        if isinstance(node, dict):
            return {k: (v if k in ("quote", "verified", "_raw", "_path") else walk(v, rid, k)) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v, rid, key) for v in node]
        if isinstance(node, str) and "{{n:" in node:
            return sub(node, rid)
        return node

    for rid in list(recs):
        recs[rid] = walk(recs[rid], rid)
    for b, entries in reg.items():
        for k in entries:
            if (b, k) not in USED:
                NUMBER_ISSUES.append(("warn", b, f"numbers.yml: {k} is registered but no record uses {{{{n:{k}}}}}"))
    return recs


def _bib_urls():
    p = os.path.join(HERE, "references", "library.bib")
    if not os.path.exists(p):
        return {}
    src = open(p, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", src, re.S):
        out[m.group(1)] = m.group(2)
    return out


def _citekeys(r):
    keys = []
    def walk(n):
        if isinstance(n, dict):
            if "citekey" in n:
                keys.append(n["citekey"])
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
    walk(r)
    return keys


def problems(recs, prose_fields, legacy):
    """(block, warn) lists of strings."""
    block, warn = [], []

    def add(book, rid, msg, hard=True):
        (block if (hard and book not in legacy) else warn).append(f"{rid}: {msg}")

    for kind, who, msg in NUMBER_ISSUES:
        (block if kind == "block" else warn).append(f"{who}: {msg}")

    banned = _load(os.path.join(HERE, "banned_phrases.yml")).get("phrases") or []
    bib = _bib_urls()
    seq = {rid: (book_of(rid), r.get("sequence") or 0) for rid, r in recs.items()}
    books = {}
    for rid, r in recs.items():
        books.setdefault(book_of(rid), []).append(rid)

    for rid, r in recs.items():
        b = book_of(rid)
        for field, text in prose_fields(r):
            for item in banned:
                if re.search(item["pattern"], text, re.I):
                    add(b, rid, f"{field}: banned phrase '{item['pattern']}' ({item.get('why', '')})")
            for m in RECALL.finditer(text):
                tgt = m.group(2)
                if tgt in seq and seq[tgt][0] == b and seq[tgt][1] > seq[rid][1]:
                    add(b, rid, f"{field}: '{m.group(1)}' points forward to {tgt}, taught later")
            for m in ID.finditer(text):
                if m.group(1) not in recs:
                    warn.append(f"{rid}: {field} names {m.group(1)}, which has no record")
        for ck in set(_citekeys(r)):
            if BAD_SOURCE.search(bib.get(ck, "")):
                add(b, rid, f"cites {ck}, a Wikipedia-type source: use it as a lead and cite what it cites")
        exs = r.get("exercises") or []
        if b not in legacy and not any(isinstance(e, dict) and e.get("type") == "retrieval" for e in exs):
            warn.append(f"{rid}: no retrieval exercise (a from-memory prompt; claude.md §7)")

    for b, rids in books.items():
        if b in legacy or b == "":
            continue
        meta = _load(os.path.join(BOOKS, b, "book.yml"))
        frozen = meta.get("status") == "frozen"
        for fld in ("why", "how_to_read", "back_blurb", "prerequisites", "subtitle", "cover_line"):
            if HISTORY.search(str(meta.get(fld) or "")):
                block.append(f"{b}: book.yml {fld} carries version history; it goes in books/{b}/CHANGE-RECORD.md")
        for fld in ("prerequisites", "page_budget"):
            if not meta.get(fld):
                (block if frozen else warn).append(f"{b}: book.yml has no {fld}")
        if not os.path.exists(os.path.join(BOOKS, b, "COVERAGE.md")):
            (block if frozen else warn).append(f"{b}: no COVERAGE.md (the rung checked against outside standards)")

    # symbols a book prints that the series table cannot explain
    try:
        import notation
        known = notation.table()
        for b, rids in books.items():
            text = "\n".join(t for rid in rids for _, t in prose_fields(recs[rid]))
            _, unknown = notation.inventory(text)
            unknown = {u for u in unknown if u not in known}
            if unknown:
                warn.append(f"{b}: symbols with no row in check/notation.yml: {' '.join(sorted(unknown))}")
    except Exception as e:
        warn.append(f"notation inventory skipped: {e}")
    return block, warn
