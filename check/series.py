"""The whole series: Book 0 plus one book per rung of the frozen subject map, in build order.

    python check/series.py            # rewrite map/BOOKS.yml and check it
    python check/series.py --check    # check only; non-zero exit if the file is stale

`map/BOOKS.yml` is generated, never hand-edited. It is what the conductor reads to choose the next
book ("the next book in the build order") and what every PDF prints as "the series, and where this
book sits". Both must agree, so both read this one file.

**The build order**, stated once so it can be changed once. Book 0 first. Then every rung-1 book,
then every rung-2 book, and so on. Within a rung, lower dependency tier first (the map's own
topological ordering), then subject number. That gives two guarantees the map's own order does
not: a subject's rungs come in ladder order, and every prerequisite subject's rung at the same
level comes earlier. It is a proposal Harsh can override: edit `ORDER_KEY` below, rerun, commit.

**Status** is read from each book's `books/<ID>/book.yml` (`status: frozen | in progress`), so the
list never claims a book is done because someone typed it here.
"""
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "map", "subject-map-v3-FROZEN.md")
OUT = os.path.join(ROOT, "map", "BOOKS.yml")
LEVELS = {1: "Introductory", 2: "Intermediate", 3: "Advanced", 4: "Expert"}


def ORDER_KEY(b):
    return (b["rung"], b["tier"], b["subject_no"])


def subjects():
    """The register table: number, name, part, target, rungs, prerequisites, tier."""
    out = []
    with open(MAP, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^\|\s*(S\d\d)\s*\|(.+)$", line)
            if not m:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            sid, name, part, target, rungs, prereq, tier = cells[:7]
            out.append({"id": sid, "no": int(sid[1:]), "name": name, "part": part,
                        "target": target.strip("*"), "rungs": int(rungs),
                        "prerequisites": [] if prereq in ("—", "-", "") else
                        re.findall(r"S\d\d", prereq), "tier": int(tier)})
    return out


def rung_headings():
    """{(S01, 1): 'Introductory (recognise and route)'} from the map's own rung headings."""
    found = {}
    with open(MAP, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^###\s+(S\d\d)\s+·\s+Rung\s+(\d)\s+—\s+(.+?)\s*$", line)
            if m:
                found[(m.group(1), int(m.group(2)))] = m.group(3)
    return found


def status_of(book_id):
    p = os.path.join(ROOT, "books", book_id, "book.yml")
    if not os.path.exists(p):
        return "not started"
    with open(p, encoding="utf-8") as fh:
        return (yaml.safe_load(fh) or {}).get("status", "in progress")


def build():
    subs, heads = subjects(), rung_headings()
    books = []
    for s in subs:
        for r in range(1, s["rungs"] + 1):
            books.append({"id": f"{s['id']}-R{r}", "subject": s["id"], "subject_no": s["no"],
                          "subject_name": s["name"], "part": s["part"], "rung": r,
                          "level": LEVELS[r], "rung_heading": heads.get((s["id"], r), ""),
                          "tier": s["tier"]})
    books.sort(key=ORDER_KEY)
    out = [{"number": 0, "id": "B0", "title": "Ground floor", "part": "Book 0",
            "level": "Ground floor", "status": status_of("B0")}]
    for i, b in enumerate(books, 1):
        out.append({"number": i, "id": b["id"],
                    "title": f"{b['subject_name']} · Rung {b['rung']}",
                    "subject": b["subject"], "part": b["part"], "level": b["level"],
                    "tier": b["tier"], "status": status_of(b["id"])})
    return subs, heads, out


def problems(subs, heads, out):
    bad = []
    if len(subs) != 61:
        bad.append(f"expected 61 subjects in the register, found {len(subs)}")
    total = sum(s["rungs"] for s in subs)
    if total != 195:
        bad.append(f"expected 195 rungs, the register sums to {total}")
    if len(heads) != total:
        bad.append(f"register says {total} rungs, map has {len(heads)} rung headings")
    for s in subs:
        for r in range(1, s["rungs"] + 1):
            if (s["id"], r) not in heads:
                bad.append(f"{s['id']} rung {r} has no heading in the map")
    # every prerequisite subject's same-level rung (if it has one) comes earlier
    pos = {b["id"]: b["number"] for b in out}
    rungs = {s["id"]: s["rungs"] for s in subs}
    for s in subs:
        for r in range(1, s["rungs"] + 1):
            for p in s["prerequisites"]:
                q = f"{p}-R{min(r, rungs.get(p, 0))}" if rungs.get(p) else None
                if q and pos.get(q, 10 ** 6) > pos[f"{s['id']}-R{r}"]:
                    bad.append(f"{s['id']}-R{r} comes before its prerequisite {q}")
    return bad


def dump(out):
    head = ("# GENERATED by check/series.py from map/subject-map-v3-FROZEN.md. Do not edit by hand.\n"
            "# Book 0 plus 195 rung books = 196. Order: Book 0, then by rung, tier, subject number.\n"
            "# status comes from books/<ID>/book.yml.\n")
    return head + yaml.safe_dump({"books": out}, allow_unicode=True, sort_keys=False, width=200)


def main():
    subs, heads, out = build()
    bad = problems(subs, heads, out)
    for b in bad:
        print("  SERIES", b)
    text = dump(out)
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            print("  SERIES map/BOOKS.yml is stale: run python check/series.py")
            return 1
        return 1 if bad else 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"  {len(out)} books written to map/BOOKS.yml; {len(bad)} problem(s)")
    return 1 if bad else 0


def load():
    with open(OUT, encoding="utf-8") as fh:
        return yaml.safe_load(fh)["books"]


if __name__ == "__main__":
    sys.exit(main())
