"""Checks that make two book chats safe to run at once (PARALLEL.md, "Two books at once").

Added 24 September 2026 on Harsh's instruction. Three commands:

  python check/parallel.py deps S37-R1        may this book start? Every book it depends on
                                              must be frozen on GitHub's main, not on a branch.
  python check/parallel.py registries         the shared registries after a merge: no citekey,
                                              source key or glossary term defined twice.
  python check/parallel.py ready S37-R1       the pre-bundle gate: fetches GitHub, then requires
                                              that local main already contains origin/main (so
                                              Harsh's `git pull --ff-only` cannot fail), that
                                              deps and registries pass, and that map/BOOKS.yml
                                              is current, and that the book's source gate
                                              was released by Harsh (check/sourcegate.py).

What a book depends on, from the frozen map: Book 0; its own subject's rung below; each
prerequisite subject's rung at the same level (or its top rung, if it has fewer), which is the
rule `check/series.py` already orders the series by; and, once records exist, every other book a
record names in `concept_deps`.

Why each registry check exists: YAML and the .bib parser both keep the *last* of two entries
with the same key, silently, so a collision between two chats' sources would not fail the
build; it would quietly cite the wrong file. Two glossary rows for one term break claude.md §10
across books, which nothing else checks.
"""
import glob
import os
import re
import subprocess
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import series  # noqa: E402

BIB = os.path.join(HERE, "references", "library.bib")
INDEX = os.path.join(ROOT, "sources", "INDEX.yml")
GLOSSARY = os.path.join(ROOT, "prose", "GLOSSARY.md")
REF = "origin/main"


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r


def book_of(record_id):
    """'S01-R1-C04' -> 'S01-R1'; 'B0-R0-C12' -> 'B0'."""
    m = re.match(r"(S\d\d-R\d+|B0)", record_id)
    return m.group(1) if m else None


def map_deps(book_id):
    if book_id == "B0":
        return []
    m = re.fullmatch(r"(S\d\d)-R(\d+)", book_id)
    if not m:
        raise SystemExit(f"not a book id: {book_id}")
    sid, r = m.group(1), int(m.group(2))
    subs = {s["id"]: s for s in series.subjects()}
    if sid not in subs or r > subs[sid]["rungs"]:
        raise SystemExit(f"{book_id} is not in the frozen map")
    deps = ["B0"]
    if r > 1:
        deps.append(f"{sid}-R{r - 1}")
    for p in subs[sid]["prerequisites"]:
        deps.append(f"{p}-R{min(r, subs[p]['rungs'])}")
    return deps


def record_deps(book_id):
    sid = book_id.split("-")[0]
    out = set()
    for path in glob.glob(os.path.join(HERE, "records", sid, f"{book_id}-C*.yml")):
        with open(path, encoding="utf-8") as fh:
            rec = yaml.safe_load(fh) or {}
        for d in rec.get("concept_deps") or []:
            b = book_of(str(d))
            if b and b != book_id:
                out.add(b)
    return sorted(out)


def status_at(book_id, ref):
    r = git("show", f"{ref}:books/{book_id}/book.yml", check=False)
    if r.returncode:
        return "absent"
    return (yaml.safe_load(r.stdout) or {}).get("status", "unknown")


def cmd_deps(book_id, ref=REF):
    deps = sorted(set(map_deps(book_id)) | set(record_deps(book_id)))
    bad = []
    for d in deps:
        st = status_at(d, ref)
        mark = "ok " if st == "frozen" else "NOT"
        print(f"  {mark} {d:8} {st} on {ref}")
        if st != "frozen":
            bad.append(d)
    if bad:
        print(f"  DEPS {book_id} may not start: {', '.join(bad)} not frozen on {ref}")
    else:
        print(f"  DEPS {book_id}: all {len(deps)} dependencies frozen on {ref}")
    return 1 if bad else 0


class _DupLoader(yaml.SafeLoader):
    pass


def _no_dups(loader, node, deep=False):
    seen, dups = set(), []
    for k, _ in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in seen:
            dups.append(key)
        seen.add(key)
    if dups:
        raise ValueError(f"line {node.start_mark.line + 1}: key(s) defined twice: {dups}")
    return loader.construct_mapping(node, deep=deep)


_DupLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dups)


def registry_problems():
    bad = []
    # library.bib: one entry per citekey
    if os.path.exists(BIB):
        keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", open(BIB, encoding="utf-8").read())
        for k in sorted({k for k in keys if keys.count(k) > 1}):
            bad.append(f"library.bib: citekey '{k}' defined {keys.count(k)} times")
    # sources/INDEX.yml: no key twice at any level, no two keys on one file, every file present
    if os.path.exists(INDEX):
        try:
            idx = yaml.load(open(INDEX, encoding="utf-8"), Loader=_DupLoader) or {}
        except ValueError as e:
            bad.append(f"sources/INDEX.yml: {e}")
            idx = yaml.safe_load(open(INDEX, encoding="utf-8")) or {}
        files = {}
        for key, entry in (idx.get("files") or {}).items():
            f = (entry or {}).get("file")
            if f:
                files.setdefault(f, []).append(key)
                if not os.path.exists(os.path.join(ROOT, "sources", f)):
                    bad.append(f"sources/INDEX.yml: '{key}' names {f}, which is not in sources/")
        for f, ks in files.items():
            if len(ks) > 1:
                bad.append(f"sources/INDEX.yml: {f} is filed under {len(ks)} keys: {ks}")
    # prose/GLOSSARY.md: one row per term
    if os.path.exists(GLOSSARY):
        terms = {}
        for n, line in enumerate(open(GLOSSARY, encoding="utf-8"), 1):
            m = re.match(r"\|\s*([^|]+?)\s*\|", line)
            if m and not re.fullmatch(r"-+|Term", m.group(1)):
                terms.setdefault(m.group(1).lower(), []).append(n)
        for t, lines in sorted(terms.items()):
            if len(lines) > 1:
                bad.append(f"GLOSSARY.md: '{t}' has {len(lines)} rows (lines {lines}); "
                           "merge them, numbering the senses")
    return bad


def cmd_registries():
    bad = registry_problems()
    for b in bad:
        print("  REGISTRY", b)
    print(f"  REGISTRY {len(bad)} problem(s)")
    return 1 if bad else 0


def cmd_ready(book_id):
    git("fetch", "origin", "main")
    fails = []
    if git("merge-base", "--is-ancestor", REF, "main", check=False).returncode:
        fails.append("local main does not contain origin/main: run `git checkout main && "
                     "git merge origin/main`, resolve (PARALLEL.md, 'Two books at once'), rebuild")
    if cmd_deps(book_id):
        fails.append("dependencies not frozen on origin/main")
    if cmd_registries():
        fails.append("shared registries have collisions")
    sys.path.insert(0, HERE)
    import sourcegate
    if sourcegate.problems(book_id):
        fails.append("source gate not released by Harsh (check/sourcegate.py)")
    if subprocess.run([sys.executable, os.path.join(HERE, "series.py"), "--check"],
                      cwd=ROOT).returncode:
        fails.append("map/BOOKS.yml stale: run python check/series.py")
    ahead = git("rev-list", "--count", f"{REF}..main").stdout.strip()
    for f in fails:
        print("  READY FAIL", f)
    if not fails:
        print(f"  READY {book_id}: main is {ahead} commit(s) ahead of origin/main and contains it; "
              "the bundle will fast-forward. Run check/build.py --check once more, then bundle.")
    return 1 if fails else 0


def main(argv):
    if len(argv) >= 2 and argv[0] == "deps":
        ref = argv[argv.index("--ref") + 1] if "--ref" in argv else REF
        return cmd_deps(argv[1], ref)
    if argv[:1] == ["registries"]:
        return cmd_registries()
    if len(argv) >= 2 and argv[0] == "ready":
        return cmd_ready(argv[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
