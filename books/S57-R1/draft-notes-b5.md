# S57-R1 draft notes · batch b5 (C09, C10, C11)

## Records written

- `check/records/S57/S57-R1-C09.yml`: an earlier, interrupted run of this batch had drafted it. I
  re-checked it in full. Every quote is in its file, and the build shows no blocking for it. I
  revised the wording: the Bloom paragraph is split, "his slide" became "he opens with" because
  the source does not mention slides, "a real list" became "a list", and I shortened four
  must-know and exercise sentences that ran long. Its skill_ref is `S57-R1-K02`.
- `check/records/S57/S57-R1-C10.yml`: new. It covers matched items at the objective's level,
  constructive alignment (Biggs's abstract, and Chatterjee & Corral's "instructional alignment"
  with their intubation example), formative and summative use, and parallel forms with partner
  items matched on the thing that makes an item hard. It shows the counterbalancing arithmetic
  (made-up numbers) and uses `B0-R0-C30` for systematic error. Its India points are NMC CBME
  2024's K/KH/SH/P levels and "Suggested Assessment method" column, and internal assessment
  (day-to-day, can include quizzes, 50% needed for eligibility). Its skill_ref is `S57-R1-K02`.
- `check/records/S57/S57-R1-C11.yml`: new. It sets out the seven-part session plan and
  rebuilds a failing lecture plan into a 60-minute plan table for the C09 BMI objective. It
  counts the minutes (40 answering, 18 explaining, 2 objective) and says why each part is there.
  It carries the rung's **build** exercise (`skill_ref: S57-R1-K01`), plus a critique exercise
  (journal club) and a teaching exercise (a district health officer, on ASHA refresher
  trainings).

Build: `python check/build.py --check` shows 0 blocking for C09, C10 and C11. Four warnings
remain. Each is a long sentence or a reading grade just over 9 in an exercise that quotes a
whole objective (C09 ex 1 answer, C10 ex 1 prompt). A finished objective is one long sentence
by design. The quote check (`check_quotes`) is clean for all three.

## Unsourced or the course's own (deliberately)

- The definition of **formative** use is the course's own. No held file defines it (current NMC
  2024 text uses only "summative"; "formative" appears in the 2019 MCI instruments, not cited).
  Summative is backed by Dunlosky 2013's "high-stakes summative assessments that are
  administered to evaluate learning".
- The six parts of an objective (C09) and the seven-part plan order (C11) are this course's own
  devices. The verified.note says so each time.
- The C11 minutes (6-minute teaching parts, 10-minute tests) are the plan's own choices. The
  record says so in the prose and in analogy_breaks_when.
- Pairing partner items on near-equal BMI (C10) is derivable. The record states no cut-off
  values, so no BMI-category source is needed.
- C11 uses Weinstein et al. 2016 (reported in Weinstein 2018, **online modules**) as the only
  evidence on where questions go in a session. The record presents it as a boundary: spreading
  questions through a session is not shown to beat putting them at the end.
- Biggs 1996 is held as its abstract only. That is enough for the definition. The record makes
  no other claim about Biggs.

## Practice-set sizes

None. The inventory marks C09, C10 and C11 as not quantitative, and `quantitative: false` is set
on each. C10's counterbalancing arithmetic is shown once as a worked illustration, not as a
drill.

## Figures

- C09: `figure_note`. The section is about the wording of one sentence, and drawing its six
  parts would be a table drawn as a picture. This was kept from the earlier run.
- C10: `s57-r1-c10-swapped-forms.png`. Bars show a gain of 40 (A then B), 20 (B then A) and 30
  (whole group), from the illustration's table, with the checks `(y[0]+y[1])/2 = y[2]` and
  `y[0]-y[2] = 10`. I dropped a reference line at 30 because its label sat on top of the value
  label.
- C11: `s57-r1-c11-hour-plan.png`. Minutes by what fills the time (explaining 18, every learner
  answers in writing 40, objective 2), with the check `sum = 60`.
- A figure that would help but that the tool cannot draw: C10's alignment triangle (objective,
  activities, test, each pointing at the others). It is a diagram, not data. The planner can
  decide whether it is worth a new kind; the prose does the job without it.
- `draw.py --book S57-R1` ran with 12 figures and 0 problems, and I looked at both PNGs.

## Glossary rows (proposed; none of these terms is in prose/GLOSSARY.md)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| Bloom's taxonomy (revised) | a sorted list of kinds of thinking skill, in six levels from remember to create | `S57-R1-C09` |
| constructive alignment | Biggs's name for designing the objectives, the teaching and learning activities, and the assessment as one | `S57-R1-C10` |
| formative use (of a test) | using a test's result while the teaching is still going on, to decide what to teach next; it counts for little or nothing | `S57-R1-C10` |
| free recall | notes away, each learner writes down all they can about the topic | `S57-R1-C11` |
| grand rounds | a teaching talk for a whole department | `S57-R1-C09` |
| instructional alignment | Chatterjee and Corral's name for constructive alignment | `S57-R1-C10` |
| internal assessment | the day-to-day assessment of the CBME Curriculum 2024, whose marks decide who may sit the university examination | `S57-R1-C10` |
| item (of a test) | one question or task on a test, marked on its own | `S57-R1-C10` |
| learning objective | one sentence stating what a named learner will be able to do after the teaching, in a form someone else could watch or mark | `S57-R1-C09` |
| parallel forms | two versions of a test whose items pair up: same action, same kind of case, same level and difficulty, different case or numbers | `S57-R1-C10` |
| session plan | a written table of a session's parts in order: minutes, what the teacher does, what every learner does | `S57-R1-C11` |
| summative use (of a test) | recording a test's result to judge or report what a learner achieved, as in an examination | `S57-R1-C10` |

C09 also expands MBBS, ASHA and MH (malignant hyperthermia) at first use. C10 expands CBME and
NMC in its must-know point. The build reports no acronym-order problem for these records. The
book's first sections may already expand MBBS; the merge should keep the first expansion only.

## Caveats for the conductor

- C11's `concept_deps` names `S57-R1-C04`. That record now exists, from another batch.
- C10's must-know on internal assessment states "at least 50%" of the internal assessment marks.
  The source adds a minimum of 40% in theory and in practical separately. The record leaves that
  out on purpose, and the quote stops before a text-layer break ("practic al").
- The earlier run's scratch script (`/home/claude/scratch-b5/check.sh`, with its copy in
  `/home/claude/scratch-b5/repo`) was not run again. I deleted nothing, and I ran no `rm`
  anywhere. My own helper, `/home/claude/scratch-b5/qcheck.py`, only reads files.
