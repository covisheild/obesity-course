"""Draw every S47-R1 figure with the build's {{n:key}} substitution applied first.

check/figures/draw.py reads records raw, so a number the prose writes as {{n:key}} looks unstated to
it, while check/build.py (load_records -> reader_checks.apply_numbers) sees the value. check/** is
frozen while other books run (PARALLEL.md), so this book-local wrapper calls the unchanged tools on
substituted records. Contract-change item: make draw.py apply the numbers registry itself.
Usage: python books/S47-R1/draw_figures.py
"""
import glob, os, sys, yaml
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path[:0] = [os.path.join(ROOT, "check"), os.path.join(ROOT, "check", "figures")]
import reader_checks, figspec, draw
recs = {}
for p in sorted(glob.glob(os.path.join(ROOT, "check", "records", "S47", "S47-R1-C*.yml"))):
    with open(p, encoding="utf-8") as fh:
        r = yaml.safe_load(fh)
    recs[r["concept_id"]] = r
recs = reader_checks.apply_numbers(recs)
bad = drawn = 0
for rid, rec in recs.items():
    for f in rec.get("figures") or []:
        if not f.get("spec"):
            continue
        probs = figspec.verify(rec, f)
        if probs:
            bad += 1
            for p in probs:
                print("NOT DRAWN", rid, p)
            continue
        draw.draw_spec(rec, f, draw.HERE, "S47-R1")
        drawn += 1
print(f"S47-R1: {drawn} drawn, {bad} with problems")
