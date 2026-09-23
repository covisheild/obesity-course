# Handover · Book 0 Part D (D1–D7)

## Close-out, second chat of 2026-09-23 — read this first

**Part D is fixed and verified: zero defects open.** Tasks 1–4 are done; the compression pass
(Task 5) has not started. The account below this section is the first chat's and is kept as the
history; where it says "open", this section supersedes it.

What ran:

1. **D6–D7 verification**, fresh Opus auditor: the fixer's "49 of 49" was false — 34 closed, 15
   partly. 32 defects open (C29 15, C30 17), including both issues the first chat had found.
   `DEFECTS-part-D-verification-d6d7.md`.
2. **Rulings M16–M19** added to `DECISIONS-part-D-fix.md`: stated-case numbers are not registered
   in `numbers[]`, except the two simulation outputs `draw.py` reads back (M16); every "VIM 4.14"
   sits beside 4.14's own words (M17); M1's "only table" wording narrowed (M18); no pipeline words
   such as "the anchor" reach the reader (M19).
3. **Per-section fix and verify** (Opus fixers, one per record, each given only its defect file,
   its record and a source-excerpt file; a fresh Opus verifier per record). All 82 open defects
   were split into `books/B0/defects/B0-R0-C24.md` … `C30.md`. Round 1 closed all 82 and
   introduced 7 new small defects in changed passages; round 2 closed those 7.
4. **Glossary pass** found §10 drift: seven terms glossed twice in different words, five first met
   as a symbol or a standards quote only. Ruling **M20** (one plain-words gloss per term, at first
   use). Fixed in C24, C26, C29 and C30 and verified: 10 items, all closed.
5. **`prose/glossary-inbox-D.md`** written from the records as they now stand: 60 rows. Two rows of
   `GLOSSARY.md` need changing at merge: *calibration* is first taught in C30, not C32; *precision*
   gets both senses.

Every defect file carries the fixer's and verifier's line under each item. Tally: 99 items across
the seven files, every one's last verifier line reads closed.

Build after the close-out: **blocking 0, warnings 51** (was 73). No warning names C24–C30 except the
derived-number notices M13 expects. `d6-sample-means.png` and `d7-two-scales.png` redraw
byte-identically.

Still true from the first chat and not in this chat's scope: `provenance.bridge_ref` is empty on
all seven; the Notion Build Tracker has not been updated; the acronym check's coin-toss false
positives (HH, HTT) in C25 belong in `build.py` between rounds.

**Next:** Task 5, the compression pass, with Parts A to C released into the scratch directory.

---

## First chat

Chat of 2026-09-23. Ran Tasks 1 to 4 of `PIPELINE.md` for Part D, once each, and stopped part-way
through verifying the fix. **Part D is not finished.** Two of the three batches still have open
defects, and nobody has verified the third batch's fixes. The compression pass (Task 5) and your
read (Task 6) have not started.

Branch `book0/part-D`, rebased onto `origin/main` at `1be5024`, so it sits on top of the Part C
close-out (`0beba57`), Part E and F2. On that base the build gives **blocking 0 and 73 warnings**
across 43 records. `--subject B0` renders, the caret check passes, and every figure regenerates
byte-identically from its record.

---

## What was written

| § | Record | Section | Practice | Must-know | Figure |
| --- | --- | --- | --- | --- | --- |
| D1 | `B0-R0-C24` | What a probability is | 9 | 5 | — |
| D2 | `B0-R0-C25` | Counting outcomes; independence | 13 | 6 | — |
| D3 | `B0-R0-C26` | Conditional probability through the two-way table | 13 | 7 | — |
| D4 | `B0-R0-C27` | Variation: what differs and by how much | 11 | 6 | — |
| D5 | `B0-R0-C28` | Average and spread, and why the average is not the person | 16 | 7 | `d5-mean-median.png` |
| D6 | `B0-R0-C29` | Sampling: how a part can tell you about a whole | 11 | 6 | `d6-sample-means.png` |
| D7 | `B0-R0-C30` | Random error and systematic error as different things | 12 | 7 | `d7-two-scales.png` |

All seven are `derivable` and `quantitative`, and all seven practice sets reach all four bands.
You decided three things at the inventory stage, and all three were applied: the Kiran paper is the
real material, D5 and D6 compute a standard deviation and state the square-root law, and D1 teaches
odds.

## Sources added

Every source is held as text, so the build checks every quote. That makes Part D the first Part
whose definitions carry `claim_located: true`.

| Citekey | File | What |
| --- | --- | --- |
| `openstax_intro_stats_2e` | `openstax_intro_stats_2e.txt` | Textbook anchor: sections 1.1, 1.2, 2.3, 2.5, 2.7, 3.1–3.4 and 7.1 |
| `openstax_contemporary_math_odds` | `openstax_contemporary_math_7_7.txt` | The anchor for odds, s.7.7. Added after the audit found odds defined with no source behind them |
| `jcgm_vim3` | `jcgm_vim3.txt` | The VIM3 vocabulary: error, systematic and random error, accuracy, trueness, precision, resolution, zero error |
| `kiran_2022_muac_nc` | `kiran_2022_muac_nc.txt` | Kiran, Harshitha and Bhargava, *Heliyon* 2022, full text with tables. The file header lists **eight** places where the paper contradicts itself |

**A citekey collision was caught on rebase.** F2 had already used `openstax_contemporary_math`
for s.8.2 of the same book, pointing at a different file. Because `INDEX.yml` maps one citekey to one
file, one of the two would have been checked against the wrong text. Part D's key is renamed to
`openstax_contemporary_math_odds`. **Parallel chats must check `library.bib` and `INDEX.yml` on
`origin/main` before choosing a key.** A same-book key feels safe to reuse, and here it was not.

---

## Which checks ran, and which did not

| Step | Who | D1–D3 | D4–D5 | D6–D7 |
| --- | --- | --- | --- | --- |
| Task 2 draft | Sonnet subagent | ran | ran | ran |
| Task 3 audit | Opus subagent, not the drafter | ran: 63 defects | ran: 39 defects | ran: 49 defects |
| Main-thread decisions | this chat | `DECISIONS-part-D-fix.md`, M1–M15 | same | same |
| Task 4 fix | Sonnet subagent | ran, reported 63/63 closed | ran, reported 39/39 closed | ran, reported 49/49 closed |
| Verification of the fix | the same Opus auditor, resumed | **ran**: 53 closed, 8 partly, 2 not; **27 open** | **ran**: 28 closed, 10 partly, 1 not; **23 open** | **not run.** You stopped the session just before it started |
| Main-thread edits after the fix | this chat | — | SD expansion, figure | NFHS-5 sentence removed; a paragraph telling the reader to run Python replaced; figures; acronym expansions |

**The two fixers that were checked both overstated.** Each reported every defect closed, and the
verifications found 11 and 11 items not fully closed. **So treat the D6–D7 fixer's "49 of 49" as
unverified.** It is the first job for the next chat.

Every file in this list is committed: the audit reports (`DEFECTS-part-D-d1d3.md`, `-d4d5.md`,
`-d6d7.md`), each with the fixer's `## Resolution (fix pass)` appended at its end, the two
verification reports, the decisions file, the drafters' notes and the inventory.

---

## Open defects

The full text of each defect, with its field and the smallest fix, is in the verification files.
This is the index.

### D1–D3 · `DEFECTS-part-D-verification-d1d3.md` — 27 open (13 error, 1 floor, 13 style)

- **C24:** V1-1 (error) the level 9 answer still applies the national ceiling to a district. V1-2
  (error) the journalist answer says odds and probability part "away from the middle", when they
  agree only near 0. V1-3 (error) the anchor's own sentence defining odds is not the one quoted.
  V1-4 to V1-6 are style.
- **C25:** V2-1 (error) the level 10 problem still takes a household-of-four bound from a ceiling
  on persons, which M2 forbids. V2-2 (sourcing, minor). V2-3 to V2-6 are style.
- **C26:**
  - V3-1 (error) "fell by about a third … while the prevalence fell by more than half". The real
    falls are about a quarter and 38 per cent.
  - V3-2 (error) "the only whole-person table that reproduces both 86 and 74 exactly" is false:
    39 splits of 131 do it. It is true only among the groups the paper prints. M1's own wording
    carries the same slip.
  - V3-3 (error) the mismatch is overstated as certainly the paper's.
  - V3-4 (error) the one-in-five re-application was tied back to the NFHS-4 planning figure,
    against M1.
  - V3-5 (error) the neck-row problem at level 10 draws a conclusion its own numbers cannot
    support.
  - V3-6 and V3-7 (errors).
  - V3-8 (error) a derived number is not marked as derived.
  - V3-11 (floor).
  - V3-9, V3-10 and V3-12 to V3-15 are style.

### D4–D5 · `DEFECTS-part-D-verification-d4d5.md` — 23 open (12 error, 2 floor, 9 style)

- **C27:**
  - V4-1 (error) says the abstract comes "a few pages later" than the Methods. It comes first.
  - V4-2 (error) credits the divide-count-by-total check with catching the 83-versus-98 error. It
    cannot, because 83 ÷ 282 is 29.4. What catches it is checking the label against the band.
  - V4-3 (error) the shape lesson misdescribes its own middle band.
  - V4-4 (error) a new practice problem carries an unsourced claim about weight moving within a
    day.
  - V4-5 (error) calls the paper's stated strength a "limitation".
  - V4-6 to V4-10: see the file.
- **C28:**
  - V5-1 (error, **not closed**) the interquartile range is still called an interval in eleven
    places, against M6.
  - V5-2 and V5-3 (sourcing) a locator names the wrong section, and a quote cites a heading that
    does not exist.
  - V5-4 (error) attributes to the textbook a reason for n minus 1 that the textbook does not give.
  - V5-5 (error) the definition makes "average" mean "mean", then calls the sample variance "the
    average of the squared deviations".
  - V5-10 (sourcing) derived quotes cite only part of the cells they were counted from.
  - V5-6 to V5-9 and V5-11 to V5-13: see the file.
  - Both records still carry sentence-length and reading-grade warnings. The fixer said they
    carried none.

### D6–D7 · no verification yet

Known before verification, all found by this chat and none fixed:

- **C29:** two sentences still describe the NFHS-4 figure as covering "India generally", at about
  lines 739 and 780. The paper gives no population for it. The verification must also re-check
  M12, the rule that no NFHS figure appears as a fact about India. The 19 and 21 per cent are still
  in the record, attributed to the paper.
- **C30:** "Sixty and a half kilograms, close to reading by reading" does not parse.

### Across the Part

- **The glossary inbox was not written.** `prose/glossary-inbox-D.md` does not exist. The drafters'
  term tables are in `draft-notes-part-D-*.md`. The fix pass then changed several first-use
  wordings, so those tables are stale. M5, M8, M9 and M10 set the words for population, sample,
  relative frequency, bias and precision.
- **`provenance.bridge_ref` is empty on all seven**, as on every Book 0 record. The intended bridges
  to S03, S08 and S02 are tabled in the inventory.
- **The Notion Build Tracker was not updated** for D1–D7.
- **The acronym check flags coin-toss outcomes** (HH, HTT and so on) in C25. These are false
  positives from a capitals pattern, not defects. The fix belongs in `build.py` between rounds.
- D5 points back to "the section on counting" for negative numbers. That pointer is true now that
  the Part C close-out is on `main` (C01 teaches them). The step of multiplying a negative by a
  negative is shown in D5 itself.

---

## Numbers that will need re-checking, and their triggers

| Figure | Where | Trigger |
| --- | --- | --- |
| 75 per cent rural and 50 per cent urban coverage | C24, C25, from NFSA s.3(2) | Any amendment to the NFSA. The held copy is the Act as enacted in 2013, and s.9 lets the Centre set State shares |
| Every Kiran figure | C26 to C30 | An erratum or correction notice for doi:10.1016/j.heliyon.2022.e12173 |
| The VIM wording | C30 | A VIM4 publication by the JCGM |
| Textbook quotes | all seven | The "web version last updated" date on each OpenStax details page |
| 0.633 and 0.317 | C29 and its figure | None: they come from a fixed draw (Python `random`, seed 110) that `draw.py` reruns, and the figure fails to draw if the draw stops matching |

---

## Things the next chat would otherwise learn the hard way

- **TinyFish `fetch_content` reaches hosts the sandbox cannot.** openstax.org, jcgm.bipm.org and
  ebi.ac.uk all refuse direct downloads at the proxy, and TinyFish returns the page text whole.
  Europe PMC's `.../rest/PMC<id>/fullTextXML` returns a paper **with its tables**, which neither
  PubMed Central's page nor the PubMed tool does. A result too large for the chat is saved to a
  file, and that is the cheapest way to get a long source onto disk without re-typing it.
- **A fixer's "all closed" is a claim, not a result.** It was false for both batches that were
  checked, and in the same way both times. Items that needed the same change in many places were
  fixed in some places and not others.
- **The paper really is inconsistent, and the audit found two of the eight inconsistencies.** The
  "overweight" row of Table 3 fits the 25–29.9 band, not the "BMI ≥ 25" label printed on it. That
  finding is now the lead of D3. Before any record quotes a paper's percentages, check that they
  divide back into whole people.
- **Figures that reproduce a draw can fail on purpose.** `d6_sample_means()` reruns the seeded draw
  and stops with an error if the record's figures no longer match. That is a stronger guarantee
  than reading numbers out of a table, and worth copying for any figure built on a simulation.

---

## Next, in order

1. **Verify D6–D7's fix pass** with a fresh Opus auditor, the same way the other two batches were
   verified. The prompt is in this chat's history, and the files it needs are all committed.
2. **One short Sonnet fix pass on all seven records**, working from the three verification files.
   Then run `python check/build.py --check`, and read Part D in the assembled booklet from the
   first line to the last.
3. **Write `prose/glossary-inbox-D.md`** from the records as they stand after step 2, not from the
   drafters' notes.
4. **Task 5, the compression pass**, with A, B and C in released form in the scratch directory.
   Run `prepare.py release A B C`, following the Part C lessons in the project doc
   `claude/coordination-for-parts-D-and-E.md`.
5. **Task 6**, your read.
