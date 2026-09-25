# Draft notes · S36-R1 · batch b4

## Records written

- `check/records/S36/S36-R1-C10.yml`: Recording and transcribing. Derivable, not quantitative, 7 must-know points, 2 exercises, 1 figure.
- `check/records/S36/S36-R1-C11.yml`: Who did the talking: the talk share. Derivable, quantitative, 7 must-know points, 1 exercise (skill_ref S36-R1-K01), 11 practice problems, 2 figures.

Build: `python check/build.py --check` shows no blocking lines for C11. C10 has one: `concept_deps` names S36-R1-C03, which another batch has not written yet. It clears once C03 lands. Warnings: C11's `openstax_prealgebra_2e` anchor is not opened (see below). There are no prose warnings on either record.

## Sources and anything unsourced

- **C10.** Every factual claim is quoted from `mcmullin_2023`, `pope_ziebland_mays_2000` or `dejonckheere_vaughn_2019`: the hours, the page count, the choices, full verbatim and cleaned, time marks, speech-to-text accuracy and cloud privacy, the 41 per cent, and "who transcribed". `pope_ziebland_mays_2000` is given `kind: textbook` because its footnote says it is taken from the second edition of the BMJ Books text *Qualitative Research in Health Care*. The book itself was not opened. **The auditor should rule on whether that kind is acceptable.** A derivable concept needs a textbook-kind reference, and no other held source for C10 is a book.
- **C10, unanchored.** The advice to keep the transcript in the language spoken and to say which version a count or quotation comes from (must_know 6, and the C10 exercise answer) has no held source. INTAKE says the same. It is written as reasoning that follows from "transcription is a set of choices", not as what researchers do. The simple transcription marks are offered as "one simple set", not as a standard. McMullin says there is no single set of rules. The advice that full verbatim suits a pilot is the course's own reasoning, not a sourced claim.
- **C11.** No held source states the talk share or its gate. As READY.md and INTAKE provide, the gate is the map's ("the respondent speaks more than you do"). The arithmetic is Book 0 A4, A5 and D5. The textbook anchor is `openstax_prealgebra_2e` ch. 6, which is Book 0 C04's anchor. It is marked `opened: false` because I did not open it, and it only warns. DeJonckheere and Vaughn are cited as context only ("prioritising listening over talking", and the DiCicco-Bloom and Crabtree quotation), with a note that they set no number and do not say the participant should do most of the talking. The prose says in two places that the 50 per cent line is this course's gate and not a published standard. "Aim well under half" is argued from the counting choices, not sourced.
- Every exchange, transcript and word count is made up, and the prose says so each time. No real participant is quoted.

## OCR quotes

None. No quote in C10 or C11 comes from `kitzinger_1995`, `britten_1995` or `pope_mays_1995`.

## Practice-set size (C11)

There are 11 problems, at levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 9 and 10. The inventory suggested 6 to 8. The technique has five moves: count words turn by turn, share, ratio, the mean across interviews, and working backwards to a word budget. It also has three distinct confusions, and each needs its own diagnostic: turns for words, a ratio called a share, and a mean of shares read as the pooled share. So 11 problems.

## Figures

- `s36-r1-c10-transcribing-hours.png`: grouped bars, hours of typing for 1 to 5 one-hour interviews at 3 and 8 hours per hour of audio. It is drawn from the illustration's table and has fits y = 3x and y = 8x.
- `s36-r1-c11-five-shares.png`: the interviewer's share in five made-up pilots, with reference lines at 50 (the gate) and 27.2 (the mean), and a check that the mean holds.
- `s36-r1-c11-turns-and-words.png`: the two excerpts, three turns each, as word counts per speaker.

All three were drawn by `draw.py` with 0 problems, and I looked at each PNG. None needs a new kind.

## Glossary rows (proposed; none of these terms is in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| cleaned transcription (intelligent verbatim) | a transcript tidied into readable sentences, with fillers and repeats taken out | `S36-R1-C10` |
| full verbatim | a transcript that keeps everything said: every filler, repeat, false start and slip | `S36-R1-C10` |
| pooled share | all the interviewer's words across several interviews, divided by all the words in them | `S36-R1-C11` |
| talk share | a speaker's words divided by all the words in the transcript, times a hundred | `S36-R1-C11` |
| transcript | a written version of a recording, made by someone who chose what went in | `S36-R1-C10` |
| turn | one unbroken stretch of speech by one speaker | `S36-R1-C11` |

## For the auditor or conductor

- McMullin's licence is PMC's COVID-19 permission (see INTAKE). The quotes are short and are for audit only.
- C10 expands NCD again in its illustration. Drop that if C01 or an earlier section already expands it, when the compression pass runs.
- My scratch files are in `/home/claude/scratch-b4/`. `verify.py` recounts every transcript table in C11 from the record and recomputes every answer.
