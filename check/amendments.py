"""Approved amendments to the frozen subject map: load, validate, apply, and check coverage.

    python check/amendments.py --check          # validate map/AMENDMENTS-v3.1.yml against the map
    python check/amendments.py --rung S26-R1    # a rung's terminal requirements, amendments applied,
                                                # plus the next rung's (what a bridge rung must reach)
    python check/amendments.py --summary        # amendments per rung, in build order

**Why this exists.** The map (`map/subject-map-v3-FROZEN.md`) stays frozen. On 23 September 2026 an
external audit (`map/audit-2026-09/REPORT.md`) found verified gaps against
clinical, policy, causal-system, professional and Indian frameworks, and Harsh approved closing all of
them. Closing them by editing the map would break its freeze; closing them by memory would not survive
the next chat. So they live in one file that the inventory reads (claude.md section 5, step 1) and that
the build enforces (below). The curriculum is the frozen map plus this file.

**Kinds.** `concept` and `skill` add a line to a rung. `revise` replaces the text of one existing map
line in place: a bullet (target = the bullet without its leading "- "), or with `field: build` /
`field: gate` the build target or gate (target = the text after the bold label).

**Ids.** Every amendment has an id `Sxx-Rn-Ann`. A record that serves an amendment names that id:
in `provenance.outcome_refs` when the amendment belongs to the record's own rung, in
`provenance.bridge_ref` when it belongs to the rung above (the bridge). A record serving a revised line
names the revise id as well as the line's own outcome label, so the revision is checkably taught.

**Enforcement** (`coverage`, called by `build.py check`). For every rung that has records, every
amendment of that rung must appear in some record's `outcome_refs` (or, for a skill, an exercise's
`skill_ref`), and for a bridge rung every amendment of the rung above must appear in some record's
`bridge_ref`. Missing coverage is a warning while the rung is being drafted, and blocking once any
record of the rung is `verified` or `released`, or its `books/<ID>/book.yml` says `frozen`.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "map", "subject-map-v3-FROZEN.md")
AMEND = os.path.join(ROOT, "map", "AMENDMENTS-v3.1.yml")
KINDS = {"concept", "skill", "revise"}
FIELDS = {"build": "**Build target.**", "gate": "**Gate to the next rung.**"}
ID_RE = re.compile(r"^(S\d\d)-R([1-4])-A(\d\d)$")


def _yaml():
    try:
        import yaml
        return yaml
    except ModuleNotFoundError:
        sys.exit("pyyaml is required: run in the course-build environment.")


def map_lines() -> list:
    with open(MAP, encoding="utf-8") as fh:
        return fh.read().split("\n")


def rungs(lines=None) -> dict:
    """{'S26-R2': {'concepts': [(line_no, text)], 'skills': [...], 'build': (n, text), 'gate': (n, text)}}"""
    lines = lines or map_lines()
    out, cur, sec = {}, None, None
    for i, l in enumerate(lines, start=1):
        m = re.match(r"^###\s+(S\d\d)\s+·\s+Rung\s+(\d)\s+—", l)
        if m:
            cur = f"{m.group(1)}-R{m.group(2)}"
            out[cur] = {"concepts": [], "skills": [], "build": None, "gate": None}
            sec = None
            continue
        if l.startswith("## ") or l.startswith("# "):
            cur, sec = None, None
            continue
        if cur is None:
            continue
        if l.startswith("**Concepts"):
            sec = "concepts"
        elif l.startswith("**Skills"):
            sec = "skills"
        elif l.startswith(FIELDS["build"]):
            out[cur]["build"] = (i, l[len(FIELDS["build"]):].strip())
            sec = None
        elif l.startswith(FIELDS["gate"]):
            out[cur]["gate"] = (i, l[len(FIELDS["gate"]):].strip())
            sec = None
        elif l.startswith("- ") and sec:
            out[cur][sec].append((i, l[2:].strip()))
    return out


def load() -> list:
    if not os.path.exists(AMEND):
        return []
    with open(AMEND, encoding="utf-8") as fh:
        return _yaml().safe_load(fh) or []


def problems(amends=None, R=None) -> list:
    """Everything wrong with the amendments file. Empty list means valid."""
    amends = load() if amends is None else amends
    R = R or rungs()
    bad, seen = [], set()
    for e in amends:
        aid = e.get("id", "?")
        m = ID_RE.match(aid)
        if not m:
            bad.append(f"{aid}: id is not Sxx-Rn-Ann")
            continue
        if aid in seen:
            bad.append(f"{aid}: duplicate id")
        seen.add(aid)
        rung = f"{m.group(1)}-R{m.group(2)}"
        if e.get("rung") != rung:
            bad.append(f"{aid}: rung field '{e.get('rung')}' disagrees with the id")
        if rung not in R:
            bad.append(f"{aid}: {rung} is not a rung of the frozen map")
            continue
        kind = e.get("kind")
        if kind not in KINDS:
            bad.append(f"{aid}: kind '{kind}' is not one of {sorted(KINDS)}")
        if not (e.get("text") or "").strip():
            bad.append(f"{aid}: empty text")
        if not (e.get("gap") or "").strip():
            bad.append(f"{aid}: no audit gap named")
        if kind == "revise":
            field, target, n = e.get("field"), (e.get("target") or "").strip(), e.get("map_line")
            if field in FIELDS:
                have = R[rung][field]
                if not have or have[0] != n or have[1] != target:
                    bad.append(f"{aid}: {field} target does not match map line {n} of {rung}")
            elif field is None:
                lines = dict(R[rung]["concepts"] + R[rung]["skills"])
                if lines.get(n) != target:
                    bad.append(f"{aid}: target does not match bullet at map line {n} of {rung}")
            else:
                bad.append(f"{aid}: field '{field}' is not build or gate")
    # one revision per map line, or the second silently overwrites the first
    targets = {}
    for e in amends:
        if e.get("kind") == "revise":
            k = e.get("map_line")
            if k in targets:
                bad.append(f"{e.get('id')}: revises map line {k}, already revised by {targets[k]}")
            targets[k] = e.get("id")
    return bad


def by_rung(amends=None) -> dict:
    out = {}
    for e in (load() if amends is None else amends):
        out.setdefault(e["rung"], []).append(e)
    return out


def effective(rung: str, R=None, amends=None) -> dict:
    """The rung's terminal requirements with amendments applied.

    Map items keep their position labels (concepts O1.., skills S1.., build B, gate G; for the rung
    above: P1.., R1..). Revised items carry `revised_by`. Added items are labelled by amendment id."""
    R = R or rungs()
    A = by_rung(amends).get(rung, [])
    rev = {e["map_line"]: e for e in A if e["kind"] == "revise"}
    base = R[rung]
    out = {"concepts": [], "skills": [], "build": None, "gate": None}
    for key, lab in (("concepts", "C"), ("skills", "K")):
        for idx, (n, text) in enumerate(base[key], start=1):
            e = rev.get(n)
            out[key].append({"pos": idx, "text": e["text"] if e else text,
                             "revised_by": e["id"] if e else None, "map_line": n})
        kind = "concept" if key == "concepts" else "skill"
        for e in A:
            if e["kind"] == kind:
                out[key].append({"pos": None, "id": e["id"], "text": e["text"]})
    for f in ("build", "gate"):
        if base[f]:
            n, text = base[f]
            e = rev.get(n)
            out[f] = {"text": e["text"] if e else text, "revised_by": e["id"] if e else None}
    return out


def _print_rung(rung, eff, labels):
    cl, kl = labels
    print(f"\n## {rung}")
    for tag, key, lab in (("Concepts", "concepts", cl), ("Skills", "skills", kl)):
        print(f"\n{tag}:")
        for it in eff[key]:
            name = f"{lab}{it['pos']}" if it["pos"] else it["id"]
            extra = f"  [revised by {it['revised_by']}]" if it.get("revised_by") else ""
            print(f"- {name}: {it['text']}{extra}")
    for f, lab in (("build", "B"), ("gate", "G")):
        if eff[f]:
            extra = f"  [revised by {eff[f]['revised_by']}]" if eff[f]["revised_by"] else ""
            print(f"\n{f.capitalize()} ({lab}): {eff[f]['text']}{extra}")


def coverage(recs: dict, book_status=lambda rung: None) -> tuple:
    """(blocking, warnings) for amendment coverage in every rung that has records."""
    block, warn = [], []
    A = by_rung()
    if not A:
        return block, warn
    present = {}
    for r in recs.values():
        sid, rung = r.get("subject"), r.get("rung")
        if not sid or sid == "B0" or not rung:
            continue
        present.setdefault(f"{sid}-R{rung}", []).append(r)
    for rk, rs in sorted(present.items()):
        served, bridged, skilled = set(), set(), set()
        for r in rs:
            p = r.get("provenance") or {}
            served |= set(p.get("outcome_refs") or [])
            bridged |= set(p.get("bridge_ref") or [])
            for ex in r.get("exercises") or []:
                if ex.get("skill_ref"):
                    skilled.add(ex["skill_ref"])
        hard = book_status(rk) == "frozen" or any(r.get("status") in ("verified", "released") for r in rs)
        sink = block if hard else warn
        for e in A.get(rk, []):
            if e["id"] not in served and e["id"] not in skilled:
                sink.append(f"{rk}: amendment {e['id']} ({e['kind']}) is served by no record's outcome_refs")
        sid, n = rk.split("-R")
        above = f"{sid}-R{int(n) + 1}"
        for e in A.get(above, []):
            if e["id"] not in bridged and e["id"] not in served:
                sink.append(f"{rk}: bridge to {above} - amendment {e['id']} discharged by no record's bridge_ref")
    return block, warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--rung")
    ap.add_argument("--summary", action="store_true")
    a = ap.parse_args()
    R = rungs()
    if a.check or not (a.rung or a.summary):
        bad = problems(R=R)
        A = load()
        print(f"amendments {len(A)} | rungs touched {len(by_rung(A))} | problems {len(bad)}")
        for b in bad:
            print("  BAD", b)
        if a.check:
            return 1 if bad else 0
    if a.summary:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import series
        order = [b["id"] for b in series.build()[2]]
        A = by_rung()
        for pos, rk in enumerate(order):
            if rk in A:
                kinds = ", ".join(f"{e['id'].split('-')[-1]} {e['kind']}" for e in A[rk])
                print(f"#{pos:<4}{rk:<8}{len(A[rk])}: {kinds}")
    if a.rung:
        if a.rung not in R:
            sys.exit(f"{a.rung}: not a rung of the frozen map")
        _print_rung(a.rung, effective(a.rung, R), ("O", "S"))
        sid, n = a.rung.split("-R")
        above = f"{sid}-R{int(n) + 1}"
        if above in R:
            print(f"\n# Bridge: what {a.rung} must carry the reader to (rung above)")
            _print_rung(above, effective(above, R), ("P", "R"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
