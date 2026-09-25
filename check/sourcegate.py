"""The source-collection stop: no book is drafted until Harsh releases its source gate.

Added 25 September 2026 on Harsh's instruction (mandatory, every book from #5 on). Why: intake
could not open sources behind CAPTCHAs, logins or robot blocks, and books were then built from
whatever the sandbox could reach, so the missing sources silently lowered quality.

The procedure (CONDUCTOR.md §1 step 2 and §2; PIPELINE.md, "Before anything: the source gate"):
after inventory and intake, the conductor writes books/<ID>/SOURCE-GATE.md listing every source
the book needs, which were obtained, and which could not be obtained (with URL and why), sends
Harsh that list, and STOPS. Nothing is drafted until Harsh either

  (a) supplies the missing sources - each "Not obtained" row is then marked provided, with the
      file it was filed as, and the release line becomes `release: sources-provided`; or
  (b) writes, in his own words in the chat, exactly
        Proceed with incomplete sources and start building the book
      - the release line becomes `release: proceed-incomplete`, and the phrase is quoted, with
      the date, on the `harsh-said:` line.

Only Harsh's message releases the gate. A subagent, a handover note or the conductor's own
judgement never does.

  python check/sourcegate.py S47-R1     exit 0 if released, 1 if not (says why)
  python check/sourcegate.py --all      every rung book with records (used by build.py)

Enforced by check/build.py (blocking: records for a rung whose gate is not released) and by
check/parallel.py ready. Books frozen before this rule existed are exempt (LEGACY).

SOURCE-GATE.md format (plain lines the checker reads; the tables are for Harsh):

  release: pending | sources-provided | proceed-incomplete
  released-on: YYYY-MM-DD
  harsh-said: "Proceed with incomplete sources and start building the book"   (proceed only)

  ## Not obtained
  | Source | Needed for | URL tried | Why not obtained | Provided |
  | ... | C03, C07 | https://... | CAPTCHA | no |      <- "no", or "yes: sources/<file>.txt"
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PHRASE = "Proceed with incomplete sources and start building the book"
# Built before 25 Sep 2026, when this gate did not exist.
LEGACY = {"B0", "S01-R1", "S02-R1", "S36-R1", "S37-R1", "S55-R1", "S57-R1"}


def _norm(s):
    return re.sub(r"\s+", " ", s.strip().strip('"').strip("“”").strip()).rstrip(".").lower()


def problems(book_id):
    if book_id in LEGACY:
        return []
    path = os.path.join(ROOT, "books", book_id, "SOURCE-GATE.md")
    if not os.path.exists(path):
        return [f"{book_id}: no books/{book_id}/SOURCE-GATE.md - inventory and intake first, "
                "then list the sources and stop for Harsh"]
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^release:\s*(\S+)", text, re.M)
    rel = m.group(1) if m else None
    if rel not in ("pending", "sources-provided", "proceed-incomplete"):
        return [f"{book_id}: SOURCE-GATE.md has no valid `release:` line"]
    if rel == "pending":
        return [f"{book_id}: source gate not released - waiting for Harsh to supply the missing "
                f"sources or to say \"{PHRASE}\""]
    bad = []
    if not re.search(r"^released-on:\s*\d{4}-\d\d-\d\d", text, re.M):
        bad.append(f"{book_id}: SOURCE-GATE.md released without a `released-on:` date")
    # rows of the Not obtained table
    sec = re.search(r"^## Not obtained\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    rows = []
    if sec:
        for l in sec.group(1).splitlines():
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if l.strip().startswith("|") and len(cells) >= 5 and not set(cells[0]) <= set("- :") \
                    and cells[0].lower() != "source":
                rows.append(cells)
    elif rel == "sources-provided":
        bad.append(f"{book_id}: SOURCE-GATE.md has no `## Not obtained` section")
    if rel == "sources-provided":
        for c in rows:
            pm = re.match(r"yes:\s*(sources/\S+)", c[-1].replace("`", ""))
            if not pm:
                bad.append(f"{book_id}: '{c[0][:60]}' is not provided - supply it, or Harsh "
                           "must say the proceed phrase")
            elif not os.path.exists(os.path.join(ROOT, pm.group(1))):
                bad.append(f"{book_id}: '{c[0][:60]}' says {pm.group(1)}, which does not exist")
    if rel == "proceed-incomplete":
        hm = re.search(r"^harsh-said:\s*(.+)$", text, re.M)
        if not hm or _norm(hm.group(1)) != _norm(PHRASE):
            bad.append(f"{book_id}: proceed-incomplete needs `harsh-said: \"{PHRASE}\"`, "
                       "quoted from Harsh's own message")
    return bad


def books_with_records():
    ids = set()
    for p in glob.glob(os.path.join(HERE, "records", "*", "*.yml")):
        m = re.match(r"(S\d\d-R\d)-C\d+", os.path.basename(p))
        if m:
            ids.add(m.group(1))
    return sorted(ids)


def main(argv):
    if argv[:1] == ["--all"]:
        ids = books_with_records()
    elif argv:
        ids = argv[:1]
    else:
        print(__doc__)
        return 2
    fails = [p for b in ids for p in problems(b)]
    for f in fails:
        print("  SOURCE GATE", f)
    if not fails:
        print("  source gate released:", ", ".join(b for b in ids if b not in LEGACY) or "(legacy only)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
