# Draft notes · S58-R1 · batch b1 (C01, C02, C03)

Task 2 drafter, 2 Oct 2026. Exemplars: S57-R1-C10 (derivable), S57-R1-C14 (institutional).

## Records written

| Record | Type | Figure | Retrieval exercise | Optional blocks |
| --- | --- | --- | --- | --- |
| `check/records/S58/S58-R1-C01.yml` What a research paper is | institutional (ICMJE guideline; Sollaci & Pereira and Mensh & Kording off-type, held, quoted) | `s58-r1-c01-imrad-adoption.png` (scatter: 0 % 1935, 20 % 1955, 100 % 1985) | yes | `common_misreading` |
| `check/records/S58/S58-R1-C02.yml` A paper is an argument | derivable (Mensh & Kording; ICMJE and Chalmers & Glasziou off-type, held, quoted) | `s58-r1-c02-unusable-reports.png` (bar: 60 against 90 per cent) | yes | `common_misreading`, `reporting_sentence` |
| `check/records/S58/S58-R1-C03.yml` The one message | derivable (Mensh & Kording; ICMJE off-type) | none: `figure_note` | yes | `common_misreading`, `reporting_sentence` |

All 67 quotes were checked by script as whitespace-normalised substrings of a `[TEXT]` passage (none from a
`[NOTE]` or header); every quote cited for a number states it. Every number in a `working` block and every
answer was recomputed in Python (24.0 - 20.6 = 3.4; 22.9 - 18.9 = 4.0; 90 - 60 = 30; 410/640 = 0.641,
152/640 = 0.2375, 96/640 = 0.15; 1/4, 1/5; "Overweight and obesity rose in India" = 31 letters + 5 spaces =
36 characters). `draw.py --book S58-R1`: 0 problems for C01 and C02; both PNGs looked at.

## Anything unsourced

- C01 must-know 7 (`india_deviation`): "The thesis followed your university's rules. The paper follows the
  journal's." No university or NMC thesis regulation is held; the point is written as a procedure (read the
  journal's instructions afresh) and claims nothing about what any university requires. Cut it if the
  auditor wants an instrument.
- Invented material, each labelled made up where it appears: the C01 draft introduction and methods (31 per
  cent; 412 and 380), the C01 critique (260, 214, 58 per cent), the C02 diary paragraph (real NFHS numbers,
  invented wording), the C02 clinic-audit critique (640, 410, 152, 96), the C03 three candidate messages,
  the C03 planted "3.6" in a draft abstract, the C03 critique's three thesis messages.
- Mensh & Kording's "the methods section is read least of all" is their statement without a measurement;
  C01 says it in their name.
- Chalmers & Glasziou's 60 and 90 per cent are from their reference 22, not their own work; C02 says so.
- Sollaci & Pereira's 100 per cent in 1985 is derived (the last two of four journals fully adopted IMRAD in
  1985), recorded under `derived`.

## Practice-set size

None of C01-C03 is quantitative; no `practice[]`.

## Figures wanted

None beyond those drawn. C03 has a `figure_note`. In the C01 PNG the 1935 point sits on the x axis and the
1985 point on the top edge of the plot (y_range 0-100); a `y_range` of [0, 105] would need 105 stated in the
text, so it was left.

## numbers.yml

Used: `nfhs5_women_ow_ob_pct`, `nfhs4_women_ow_ob_pct`, `nfhs5_men_ow_ob_pct`, `nfhs4_men_ow_ob_pct`,
`nfhs5_women_ow_ob_change_pp`, `nfhs5_men_ow_ob_change_pp`. **No key added.** Numbers written literally
that another section may want (for the reconciler):

| Value | Meaning | Source |
| --- | --- | --- |
| 40 | characters, the usual upper limit for a short title where a journal requires one (letters and spaces) | `icmje_2026_manuscript_preparation` IV.A.3.a |
| 36 | characters in the short title "Overweight and obesity rose in India" | arithmetic, C03 |
| 1,297 | original articles in Sollaci & Pereira's sample | `sollaci_pereira_2004_imrad` |

## Notation rows needed

None. The records print no sign, Greek letter or mark outside quotes (the `≥` in the NFHS-5 quotes is the
source's, and already has a row). "Percentage points" is written in words throughout.

## Glossary rows

Not already in `prose/GLOSSARY.md` (checked: `argument`, `premise`, `conclusion` and `reference` are there,
from Book 0, and are used in their existing senses; `gap` exists only as "gap (between study sessions)").

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| abstract (of a paper) | a short summary of the whole paper, printed before it: the context and the gap, what was done, the main result, and what it means | `S58-R1-C01` |
| claim (of a paper) | what the paper says it found; in Book 0's terms, the conclusion its data are offered for | `S58-R1-C02` |
| gap (in a paper) | what is not yet known, which the paper sets out to fill | `S58-R1-C01` |
| IMRAD structure | the four sections an original research article is usually divided into: Introduction, Methods, Results and Discussion | `S58-R1-C01` |
| one message (of a paper) | the paper's central claim in one or two sentences, what it found and why that matters, written before the draft | `S58-R1-C03` |
| original research article | a journal paper that reports a study for the first time | `S58-R1-C01` |
| report of activities | a write-up that records what the authors did in the order they did it, as against an argument | `S58-R1-C02` |
| short title | a shortened title some journals require, usually no more than 40 characters, letters and spaces counted | `S58-R1-C03` |

## Notes for others

- **ICMJE** is cited as Section IV.A throughout, quoted in short phrases, and linked at
  https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html. C01
  expands ICMJE and IMRAD at first use; later sections may use both bare.
- **C04 (argument across sections):** C01 already gives each section's job in ICMJE's words (introduction:
  context and purpose, no data or conclusions from the study; methods: enough to reproduce, only what was
  known when the protocol was written, everything obtained during the study goes to results; results: main
  findings first; discussion: summary, other evidence, limitations). C04 should build on this, not restate
  it. C02 puts a results paragraph's claim first (ICMJE "main or most important findings first"); Mensh &
  Kording Rule 7 has results paragraphs open on the question and close on the answer. If C04 or C10 teaches
  the Rule 7 shape, say how the two fit (e.g. section-level order against paragraph-level shape) rather than
  contradict C02.
- **C05 (referencing):** C01 names the reference list and quotes ICMJE's "attest that the references cited
  support the associated statement"; numbering and NLM style are left entirely to C05.
- **C09 (numbers):** C02's rewritten paragraph and reporting sentence give the NFHS percentages without
  counts. The fact sheet gives no count per indicator, only the total sample (724,115 women, 101,839 men
  interviewed). C09 should say what a writer does when the source gives no numerator, rather than imply C02
  broke the rule.
- **C10 (paragraphs):** C02's design exercise (C/E/S marking of sentences, skill_ref `S58-R1-K01`) is a
  precursor of the reverse outline; keep the letters or say they are dropped.
- **C14 (one figure, one claim)** and **S58-R2-P03 (talk, poster):** C03 says the same one message serves the
  talk, poster and journalist; do not teach a different message per form.
- **C23 (journey):** C02 already rewrites the NFHS diary paragraph into the claim paragraph, and C03 writes the
  one message ("rose in women and in men ... about one woman in four and more than one man in five"), the full
  title ("Overweight and obesity rose among women and men aged 15-49 in India between 2015-16 and 2019-21: a
  comparison of two National Family Health Surveys") and the short title "Overweight and obesity rose in
  India" (36 characters). Reuse them or say why the journey changes them. Both sections state the limits:
  ages 15-49 only, overweight and obese counted together (the fact sheet has no separate obese row), and two
  surveys show the rise, not its cause.
- **Running case:** C03's abstract example says the fifth round's India fact sheet "prints the fourth round's
  figures beside its own but does not state the change". Do not contradict it.
- Bridge refs used: C01 `S58-R2-P01`, `S58-R2-A02`; C02 `S58-R2-P01`, `S58-R2-P05`; C03 `S58-R2-P03`,
  `S58-R2-A01`, `S58-R2-R3`. Outcome refs: `S58-R1-O1` (all three), `S58-R1-G` (C02, C03).
