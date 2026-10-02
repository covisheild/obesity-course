# Draft notes · S58-R1 · batch b3 (C06, C07, C08)

Task 2 drafter, 2 Oct 2026. Concept numbers are the NEW ones (old C05, C06, C07 in the intake logs
and source-file headers).

## Records written

| Record | Name | Type | Figures | Retrieval exercise |
| --- | --- | --- | --- | --- |
| `check/records/S58/S58-R1-C06.yml` | The parts of a sentence a writer works with | derivable | none: `figure_note` | yes |
| `check/records/S58/S58-R1-C07.yml` | The sentence as the unit of clarity | derivable | `s58-r1-c07-subject-verb-gap.png` | yes |
| `check/records/S58/S58-R1-C08.yml` | Words: the everyday word, one term for one thing, abbreviations that cost the reader | empirical | `s58-r1-c08-acronyms-per-100-words.png` | yes |

None of the three is quantitative, so none carries `practice[]` (inventory: practice only on C09,
C11, C17). C08 does one ratio in a `working` block (acronym density, 1956 against 2019).

All three carry `common_misreading` and `reporting_sentence`.

## Sources used, and anything unsourced

Every quote was checked by script against the `[TEXT]` passages only (never a header or `[NOTE]`),
whitespace-normalised. All pass. Sources: `openstax_writing_guide_handbook` (6.6, H3, H7, 3.6),
`plain_language_2011_guidelines`, `gopen_swan_1990_scientific_writing` (located by section; no page
numbers), `barnett_doubleday_2020_acronyms`, `icmje_2026_manuscript_preparation` (§IV.A.3.e and
§IV.A.3.k, quoted briefly), `mensh_kording_2017_structuring_papers` (Rules 2 and 4),
`nfhs5_india_factsheet` (indicators 86, 88, 89; column headings; the adult-rows heading).

Things written without a quote, by design:
- C06: the definition of "object" rests on OpenStax's "the object actually becomes the subject" (the
  object is what receives the action). No held source defines "object" by itself. The OpenStax list
  of subordinating words has no "if"; the definition adds it as an everyday example.
- C06, C07, C08: every "before" sentence and paragraph is made up and labelled so; where they carry
  NFHS-5 figures, those come from the registry.
- C07 ill. 2: "whether 'we' is welcome is a matter for the journal" is advice (look at its
  instructions), not a claim about any journal.
- C08: "significant" is glossed as "roughly, a difference too large to put down to chance", the
  wording S57-R1-C06 already uses; correlation and the Normal distribution are named and marked as
  not taught in this book.
- C08: Barnett and Doubleday's Results say 49% were used "between two and ten time times" (sic);
  their abstract says 79% "fewer than 10 times". The record uses the Results wording only and does
  not add 30 + 49.
- C08: the "18 meanings of UA" figure is Lang (2019) as reported by Barnett and Doubleday; the record
  says so.

## Practice-set size

None: no concept in this batch is quantitative.

## Figures

- C07: grouped bars, words in the sentence and words between subject and verb, for Gopen and
  Swan's first (42, 23) and third (62, 27) sentences and the made-up survey sentence before (45, 41)
  and after (27, 4). Data from the illustration's table; check `y2[2] - y2[3] = 37` (stated in the
  text). Drawn and looked at: labels clear at size [7.4, 3.2].
- C08: grouped bars, acronyms per 100 words, titles 0.7 (1950) and 2.4 (2019), abstracts 0.4 (1956)
  and 4.1 (2019). Checks: the two ratios, 10.25 and 3.43, worked in the text. Looked at.
- C06 has a `figure_note`. The figure that would teach is a marked-up sentence (subject, verb, object
  and doer labelled under "Written informed consent was obtained ... by the investigator", and its
  active twin), which `draw.py` does not draw. If a sentence-diagram kind is ever added, this is the
  figure to draw.

## numbers.yml keys used (none added)

`nfhs5_women_ow_ob_pct` (C06, C07, C08), `nfhs4_women_ow_ob_pct` (C07, C08),
`nfhs5_women_ow_ob_urban_pct`, `nfhs5_women_ow_ob_rural_pct`, `nfhs5_men_ow_ob_pct`,
`nfhs5_men_ow_ob_urban_pct`, `nfhs5_men_ow_ob_rural_pct` (C08).

Numbers written literally that another section may share (for the reconciler):
- 25.0 kg/m^2, the BMI cut-off of NFHS-5 indicators 88-89 (`nfhs5_india_factsheet`, row 88). Used in
  C07 and C08, and likely in C09, C21 and C23. Suggest key `nfhs5_ow_ob_bmi_cutoff`.
- 18.5 kg/m^2, the "below normal" cut-off of indicator 86 (`nfhs5_india_factsheet`). C08 only.
- 2015-16 and 2019-21, the survey years of NFHS-4 and NFHS-5 (column headings of the fact sheet).
  C07 and C08; C23 will need them.
- Barnett and Doubleday's 0.7, 2.4, 0.4, 4.1 per 100 words: C08 only, but C11 (readability of
  abstracts) may cite the same paper.
- C08's reporting sentence carries 25.0 literally (no key yet); C07's uses the registry keys.

## Notation rows needed

None new. The only non-ASCII signs printed are "≥" (inside the quoted fact-sheet row; row exists),
the em dash inside quotations, and the superscript in kg/m^2 (row "ˣ" exists).

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

`subject (of a formula)` exists (`B0-R0-C16`). Per the glossary's rule for two senses, the
reconciler should either number that row's senses or add the second as its own row; proposed as its
own row below.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| abbreviation | a shortened form of a word or phrase, spelled out with the short form in brackets at first mention | `S58-R1-C08` |
| acronym (as Barnett and Doubleday count it) | a word in which half or more of the characters are capital letters, such as DNA or mRNA | `S58-R1-C08` |
| active voice | the subject of the sentence does the action of the verb: "We measured the weight" | `S58-R1-C06` |
| clause | a group of words with a subject and a verb | `S58-R1-C06` |
| doer | whoever or whatever performs the action, whether or not it is the subject | `S58-R1-C06` |
| hidden verb | an action turned into a noun ("assessment", "increase") and carried by an empty verb ("was done", "was observed") | `S58-R1-C07` |
| main clause | a clause that can stand alone as a sentence; it carries the main idea | `S58-R1-C06` |
| nickname (for a long name) | a short plain name used instead of an abbreviation, such as "the centre" for the primary health centre | `S58-R1-C08` |
| noun string | three or more nouns in a row, so that the reader has to guess how they relate | `S58-R1-C07` |
| object (of a verb) | the noun that receives the action of the verb | `S58-R1-C06` |
| passive voice | the subject receives the action; the verb takes a form of "to be" and a past participle, and the doer moves after "by" or disappears | `S58-R1-C06` |
| past participle | the form of a verb that follows "has" or "was": measured, taken, given | `S58-R1-C06` |
| predicate | the verb together with everything that completes it | `S58-R1-C06` |
| stress position | the end of a sentence, where a reader puts the most weight; the place for the new information | `S58-R1-C07` |
| subject (of a sentence) | what the clause is about, the thing the verb is said of; find the verb, then ask "who or what" in front of it | `S58-R1-C06` |
| subordinate clause | a clause with its own subject and verb that opens with a word such as because, when or although and cannot stand alone | `S58-R1-C06` |
| topic position | the start of a sentence, where a reader looks for the link to what came before and for whose story the sentence tells | `S58-R1-C07` |
| verb | the word for what happens: an action, an occurrence or a state of being | `S58-R1-C06` |
| voice | which of the doer and the thing acted on is the subject; not the same as tense | `S58-R1-C06` |

## Notes for others

- **C09 (numbers):** C07 and C08 write percentages as "per cent" in prose and "%" only inside a
  made-up "before" sentence. C08's critique exercise flags a sentence for "significantly" with no
  test; C09 should not contradict that by reporting a P value without naming the test.
- **C10 (paragraphs):** C07 names the topic position and the stress position at sentence level, and
  routes the full reader-expectation treatment to R2. C10's topic sentence is a paragraph-level idea;
  please do not call it the "topic position", which C07 uses for the start of a sentence. C07 also
  uses Gopen and Swan's "Each unit of discourse ... to make a single point", which C10 can reuse for
  the paragraph. Skill K01 (a paragraph that makes one point) is not claimed by any exercise in
  this batch; C10 should carry it.
- **C11 (measuring a draft):** C07's must-know 2 and common misreading say sentence length is not the
  defect, citing Gopen and Swan (10-word sentences impenetrable, 100-word ones easy). Gopen and Swan
  also say "The creators of readability formulas would have us believe there exists some fixed number
  of words (the favorite is 29)". C11 may want that sentence; it fits its "trip-wire, not a target".
  Barnett and Doubleday cite Plavén-Sigray et al. 2017 in their Introduction.
- **C12 (cutting):** C07 defines "split, not compressed": compressing is fusing ideas into a noun
  string (Plain Language's three-noun warning) or an empty-verb sentence. C12's "cutting is not
  compressing" should use the same sense. C07 does not teach deleting words; the Plain Language
  "Omit unnecessary words" section and OpenStax's wordiness examples are left for C12.
- **C21, C23:** use "overweight or obesity" as the one term for NFHS-5 indicators 88-89, defined once
  as a BMI of 25.0 kg/m^2 or more, with "women with overweight or obesity" (person first). C08 teaches
  that "obesity" alone is a claim the fact sheet does not report, and that the adult rows cover ages
  15 to 49 only. Please keep both.
- **All sections:** C08 teaches no more than three abbreviations, each spelled out at first mention.
  NFHS, BMI and ICMJE are the three this book leans on. ASHA is spelled out where used.
- **Acronym check:** C08 illustration 2 deliberately shows "UA" and "HR" (Barnett and Doubleday's
  examples). "HR" is expanded; "UA" has 18 meanings and is left unexpanded on purpose, so the render's
  acronym list may print it.

## Self-check (SELFCHECK.md)

- 1-2: every quote read alone against the sentence it backs; every number's quote states it.
- 3: every figure about the world has a citekey and an `illustration.numbers` entry; every made-up
  sentence is said to be made up.
- 4b: C08 says the acronym count measured use, not understanding, in English-language titles and
  abstracts only, and that "nearly a quarter" is not a figure for all adults. C06 and C07 say their
  word counts are for one sentence, not limits.
- 6a: NFHS figures through `{{n:}}` in every reader-facing field; literal only in quotes and
  `numbers` values. The cut-offs 25.0 and 18.5 and the survey years are literal (no key yet).
- 7: "overweight or obesity" throughout; "anganwadi" in C06's exercise uses the S37 gloss.
- 10: word counts (41, 4, 45, 27, 13, 17, 17) and the ratios (3.43, 10.25) recomputed in Python.
- 14a: no new symbol.
- 20-22: no banned phrase, no version history, no "recall".

## Build state at hand-back

`check/build.py`'s `check()` run on 2 Oct 2026 after the last edit: 0 blocking in the whole build,
none in these records. Three warnings remain, left on purpose: C07's reporting sentence (29 words; it
keeps the subject next to its verb and the survey years beside each round), C07 exercise 2's prompt
(the deliberately bad 28-word clinic-audit sentence), and C08 exercise 2's 26-word rewrite. Figures
redrawn after the last text edit; `draw.py --book S58-R1` reports 0 problems.
