# S01-R1 · tooling fixed before the first subject book

23 September 2026, branch `book/S01-R1`. The three known gaps in `CONDUCTOR.md` that block a rung
book's Task 5 and PDF.

## What changed

**Compression tools take `--subject`.** `check/compress/prepare.py`, `restore.py`, `validate.py`
(shared helper `check/compress/_book.py`). `--subject B0` or `--subject S01-R1`; the working folder
is `books/<ID>/compress/`. A rung book reads `check/records/S01/`, keeps only ids starting
`S01-R1-`, and labels each section by its concept_id (`S01-R1-C03-prose.yml`). With no ids,
`extract`/`assemble`/`writeback` take the whole book. `release` for a rung book writes every Book 0
section named in the rung's `ground_floor_deps` (labelled as Book 0 prints them, `A5-released.md`),
every section of the subject's earlier rungs, and any Book 0 Parts named. `--out` and `--records`
redirect the working folder and records, for testing. `books/B0/compress/*.py` are now wrappers
that add `--subject B0`.

**Restore is sentence-level.** Naming a sentence brings back that sentence only, inside its
original paragraph, between that paragraph's kept sentences, in original order. The sentences are
cut from the raw text at `check/build.py`'s own sentence boundaries, so bold and italics survive.
A unit with every sentence surviving is copied byte for byte. List items are sentence-level with
their marker kept. Block quotes, table rows, headings and fences are kept or restored whole (a
fence also returns with its restored introduction, as before). `validate.py` adds a survival check
for a `-final-prose.yml`: every sentence, row, heading and fence of the `-pass1-prose.yml` must
still be there. No tolerance was added: mean and longest sentence still may not rise.

**A rung renders as its own book.** `check/build.py --subject S01-R1` writes
`check/_build/S01-R1.md` (+ docx, html) with only rung 1's records, and `make_pdf.py` makes
`S01-R1.pdf` from `books/S01-R1/book.yml`. "Before you start" names Book 0 sections as `A5 · name`,
not by id. `--subject B0` and `--subject S01` are unchanged.

## How it was tested

- **Book 0 prepare, identical.** Old vs new tool, all 43 Book 0 records, `extract` + `release A–F`:
  129 files, zero diff. Against committed files: all 20 `-released.md` that still match today's
  records (A1–A6, A8, B1–B6, C1, C3–C8) are byte-identical, and 25 `-original.md` + `-prose.yml`
  (C1–C4, C9, D1–D7, E1–E8, F1–F5) are byte-identical when regenerated from the records as they
  stood when each was committed (`--records` from `git archive`). The rest were written before
  `prepare.py` existed (A, B) or before figures were added (C5–C8).
- **Sentence-level restore.** On C9, D3, C2 and E5, two cut sentences named each: exactly those two
  came back, nothing else; `validate.py` passes (e.g. C9 mean 13.05 -> 12.62, longest 29 -> 29).
  All 29 real restore lists (C1–F5) re-run with the new tool: 29/29 pass, including survival; they
  bring back 179 fewer sentences than the committed paragraph-level finals. A bullet deleted by hand
  from C2's final is caught by the survival check.
- **Rung book.** In a temp copy of the tree with one throwaway record (`S01-R1-C01`, made from a
  Book 0 record, deps A1 and A5): `--check` blocking 0; `--subject S01-R1` produced `S01-R1.md`,
  docx, html and a 22-page PDF with the S01-R1 cover; `prepare --subject S01-R1 extract/release`
  wrote the section plus `A1-released.md` and `A5-released.md` (identical to Book 0's copies); a
  fake cut, `assemble`, `restore`, `validate` ran clean. Old vs new `booklet_md` for B0 and S01:
  identical. Real tree: `python check/build.py --check` blocking 0, warnings 48 (48 before).

## Still open

- `validate.py` on the committed Part A finals: `A7-final-prose.yml` fails survival (the quote lost
  by the old restore bug; the record was repaired), and `A2-final-prose.yml` fails mean (12.18 ->
  12.35, hand-run Part A). Historical files, not records.
- A block quote the cutter half-kept comes back whole (a half-quoted source is a misquote).
- A sentence that occurs twice in one field is kept at both places if the cut kept either.
