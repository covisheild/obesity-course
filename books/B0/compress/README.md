# The compression pass on Part A · working files

Run 20 September 2026, all three steps in one task, per `claude.md` §12 and `PIPELINE.md` Task 5.
Kept so the pass can be audited rather than believed.

| File | What it is |
| --- | --- |
| `<SEC>-prose.yml` | the five reader-facing prose fields, extracted from the record |
| `<SEC>-original.md` | the section as the booklet prints it — what step 5a read |
| `<SEC>-pass1-prose.yml` | step 5a's cut |
| `<SEC>-pass1.md` | the cut section, assembled — what went into the scratch directory |
| `COLDREAD-REPORT.md` | step 5b's gap report |
| `RESTORE.yml` | step 5c's decisions, each keyed to the gap that justifies it |
| `<SEC>-final-prose.yml` | what was written back into the record |
| `LEAST-SURE-CUTS.md` | the cut each cutter was least sure about, written before the test |
| `validate.py` | the mechanical check on a cut or a restore |

**The one thing worth knowing before running this again.** The cutters never touched the
exercises or the practice problems, and could not have: `<SEC>-pass1.md` is assembled from the
cutter's prose plus the exercises and the ten prompts copied out of the record, so the test set is
byte-identical to the original's by construction rather than by instruction. `validate.py` closes
the other half — it fails a cut whose surviving sentences are not the original's word for word,
which is how "delete, never compress" is enforced rather than hoped for.

`<SEC>-final-prose.yml` is built by walking the *original* and keeping a sentence if the cut kept
it or `RESTORE.yml` names it. Nothing new can enter a restore, because nothing new is ever in the
input.

## Part E, paused before the compression pass

Set up on 23 September 2026 and stopped there. `prepare.py extract` has written `E1`–`E8`'s
`-prose.yml` and `-original.md`, and `prepare.py release A B C` has written the earlier Parts the
cold reader will need. **Nothing has been cut.** Step 5a was never run.

One orphan was deleted rather than committed: `E5-pass1-prose.yml`, a 46 per cent cut of E5 written
by a cutter that was stopped before it finished and before it validated. One cut section out of
eight is worse than none, because the next chat finds a `-pass1-prose.yml` on disk and has no way to
tell a completed step from an abandoned one — which is the half-finished claim `PARALLEL.md` warns
about, arriving inside a Part rather than across chats. The pass regenerates it in a minute.

Part D is not written, so `release` covered A, B and C only. When Part D lands, the cold reader for
Part E needs it too: `prepare.py release A B C D`.

**Regenerated on merging Part E onto `main`, 23 September 2026.** The Part E chat had written the
`-released.md` copies of Parts A–C from `997228b`, before A1 gained negative numbers and the order
of operations and before the Part C close-out. A cold reader given those would test Part E against
a book that no longer exists. All of them, and E1–E8's extracts, were rewritten from the merged
records. Regenerate again immediately before step 5a in any case — `release` is cheap and a stale
copy is silent.

## Parts D, E and F, compressed 23 September 2026

All twenty sections cut (5a), cold-read one Part at a time against the released text of every
earlier Part (5b: `COLDREAD-REPORT-part-{D,E,F}.md`), restored (5c: `restore-lists/`), and written
back. Holes the original did not fill are in `HOLES-part-{D,E,F}.md`, triaged in
`TRIAGE-part-{D,E,F}.md`, and fixed and verified through `books/B0/defects/*-compression.md`.

**`restore.py` bug, fixed.** It matched a kept bullet or quote by its sentence with the marker still
on, against a kept-set built with markers stripped, and never matched table rows. Every kept bullet,
block quote and table row was silently dropped. D–F outputs were byte-identical after the fix; A7,
C2 and C9 had lost lines since their own compression, and those were put back.


## Tools moved, 23 September 2026

`prepare.py`, `restore.py` and `validate.py` now live in `check/compress/` and take `--subject`
(`B0`, or a rung book such as `S01-R1`). The three files here are thin wrappers that add
`--subject B0`, so every command above still works. `restore.py` is now sentence-level and
`validate.py` checks a `-final-prose.yml` for anything the cut kept and the restore lost. Run
against the files here, that check flags `A7-final-prose.yml` (it lacks the quote the cut kept,
the bug fixed on 23 September; the record itself was repaired) and the mean check flags
`A2-final-prose.yml` (12.18 -> 12.35, from Part A's hand-run pass, before the tools existed).
Both predate the change, and neither file is read by anything. See `books/S01-R1/TOOLING-NOTES.md`.
