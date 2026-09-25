# Draft notes · S36-R1 · batch b5

Drafter: Opus 5.5, 24 Sep 2026. Records written:

- `check/records/S36/S36-R1-C12.yml`: Reading a transcript, and what a code is
- `check/records/S36/S36-R1-C13.yml`: The quotation as data
- `check/records/S36/S36-R1-C14.yml`: Five pilot interviews (the build section)

`python check/build.py --check`: blocking 0 at hand-back, and no warnings on C12 to C14.
`python check/figures/draw.py --book S36-R1`: 7 figures, 0 problems. I looked at the C14 PNG.

## Decisions the conductor should see

1. **Textbook anchor (corrected on the coordinator's instruction).** Pope, Ziebland & Mays and Mays
   & Pope are back to `kind: primary`. Each record now has a `blackstone_2012` reference with
   `kind: textbook`.
   - C12: section 9.2, coding by reading and rereading, and line-by-line open coding. This carries
     the concept's core.
   - C13: section 9.2, the sentence introducing Table 9.1, where interview excerpts are shown as the
     data a code rests on. **The textbook does not carry C13's core**: the four checks on a
     quotation, keeping its context, and cherry-picking. Those rest on the primary references.
   - C14: section 7.2, a pilot study done early with a nonprobability sample, and section 9.2,
     transcribing your own interviews. **The textbook does not carry C14's core**: what a pilot
     interview tests, and the steps you run after each one. Those rest on DeJonckheere & Vaughn.
2. **"Code" has two senses in the book.** C07 uses "code" for R1, the label that stands in for a
   name. C12 teaches "code" as a label on a passage. C12 now says outright that this is a second
   sense. The cleaner fix is for C07 to say "label" for R1.
3. **Two made-up sets of five pilots.** C11 has five interviews (shares 23.0 to 52.5). C14 has a
   different set (46, 38, 26, 20, 43), and says so, because its point is change between pilots. Each
   has its own figure. The compression pass could merge them onto one set if that reads better.
4. **Consent for keeping transcripts.** C14 tells the reader to ask at consent whether transcripts
   may be kept for S36-R2, and to get their own institutional ethics committee's answer in writing.
   It says nothing about whether review is needed.

## Unsourced or derived

- "Do not pilot on your own patients" (C14) is my inference from DeJonckheere & Vaughn's Step 3
  sentence about participation not affecting care. `verified.note` says the article does not give
  the advice in those words.
- The seven-step order per pilot (C14) is assembled from DeJonckheere & Vaughn Steps 4, 5 and 8, the
  map's build target, and C07 to C12. No single source lists it.
- "Read the whole transcript before marking anything" (C12) rests on Pope, Ziebland & Mays' "read
  and reread". The framework approach's "familiarisation" stage says the same, but that stage is
  S36-R2, so I did not cite it.
- Every transcript line, respondent, count and clinic detail (the Saturday session, the kiln job)
  is made up, and the prose says so the first time in each illustration and exercise.

## OCR quotes

- `britten_1995`, p. 252, column 1, the running text beside Box 3 (C14, definition reference 7):
  `Thenoviceresearchinterviewerneedstonoticehow directiveheorsheisbeing,whetherleadingquestions are beingasked,whethercues are pickedup or ignored,andwhetherintervieweesaregivenenough timetoexplainwhattheymean.`
  Needs a check against the page image.

## Practice sets

None. The inventory marks C12, C13 and C14 not quantitative. C14's talk-share working reuses C11's
method, and C11 carries that drill set. The shares were recomputed in Python (46.0, 38.0, 26.0,
20.0, 43.0).

## Figures

- C14: `s36-r1-c14-talk-share.png`, a bar chart of the five made-up shares with a reference line at
  50 per cent, read from the illustration's table.
- C12 and C13 carry a `figure_note`. Their work is reading words against words. The only chart the
  tool could draw for C12 is a tally of codes, which is the counting the section warns against. No
  figure is wanted from the planner.

## Skill and bridge coverage

- C14 exercise 1 (build) carries `skill_ref: S36-R1-K01`. C14 exercise 2 (design, rewriting a guide
  question after a pilot) carries `S36-R1-K02`.
- bridge_ref: C12 → S36-R2-P02, C13 → S36-R2-P04. outcome_refs follow the S02 style (S36-R1-B,
  S36-R2-P2, and so on).

## Glossary rows

Checked against `prose/GLOSSARY.md`. None of these is there yet.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| cherry-picking | choosing only the quotations that fit the author's view, or cutting one until it fits | `S36-R1-C13` |
| code | (2) a short label written beside a passage of a transcript, saying what it is about, so it can be found and compared with others; distinct from (1) the label R1 that stands in for a respondent's name (`S36-R1-C07`) | `S36-R1-C07`, `S36-R1-C12` |
| deviant case (negative case) | a passage that runs against the pattern the other passages seem to show; kept and marked, not dropped | `S36-R1-C12` |
| memo | a note, written while you read, of what you notice and what you want to ask next | `S36-R1-C12` |
| pilot interview | a practice run of the whole interview procedure with a few people, testing the guide and the interviewer, not the study question | `S36-R1-C06` (named: "a guide is tried out before the study, in a pilot interview"), `S36-R1-C14` (taught in full). Merge with C06's wording if its batch proposes a row |
