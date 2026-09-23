# Instructions for this project

Read this file before doing anything. It is the whole contract. Everything below it in this
folder is either the material you write from, the checks you must pass, or finished work you
should match.

## What this project is

A teaching course on obesity, written from first principles for one reader: a community medicine
postgraduate in India who can read English and use a calculator, and who has no remembered
mathematics, no law and no civics. Book 0 teaches the ground floor once. Sixty-one subject
booklets stand on it.

## The one rule that matters more than the others

**A claim without a source you have opened is not written down as a fact.**

Every reference in a record carries `verified.opened`. It is set to true by whoever obtained the
source and read the passage, and by nobody else. If you cannot open a source, write the concept
with `opened: false`, name the instrument you would need in `verified.note`, and leave it in the
citation backlog. Never smooth over the gap with confident prose.

This is not a formality. The point of the whole course is to be something that cannot be routed
around, and that rests entirely on every citation holding when somebody hostile checks it.

## How the work is divided

| Step | Who | What |
| --- | --- | --- |
| 1 | Opus | Structure. Which concepts a rung needs, in what order, what each must cover, which sources each will need, and which of them are quantitative and so owe ten practice problems. Output: an inventory table, no prose. |
| 2 | Sonnet | Draft. The four reader-facing blocks per concept, written to the register below, into the record YAML. Plus, on every quantitative concept, the ten practice problems of section 7a. |
| 3 | Opus | Audit. Open every source in `sources/` and check every claim against it. Recompute every practice answer. Check currency. Output: a numbered defect list, not a rewrite. |
| 4 | Sonnet | Fix. Apply the defect list. Run `python check/build.py --check` until blocking is zero. |
| 5 | Human | Read it. |

**Step 3 audits the practice answers too**, by recomputing them rather than by reading them. Eighty worked answers is eighty chances to ship a wrong one, and a wrong answer in the appendix is worse than a wrong sentence in the prose, because the reader who disagrees with it assumes they are the one who erred.

**Step 3 is an audit against files, not a read-through.** Three factual errors survived step 2
in the pilot and every one of them read as plausible prose: a section of an Act said to be silent
when it is not, a laying requirement described as a condition of validity, and a claim about one
statute's copies that had been verified only for another. Reading the draft cannot catch these.
Opening `sources/fss_act_2006.txt` and searching it can.

## Before a book starts

A book only enters the pipeline when its source pack is complete. Each book folder carries a
`READY.md` listing every instrument the inventory needs, with obtained yes or no. If anything
says no, stop and tell the human which file to go and get. Do not start and work around it.

## What is in this folder

- `sources/` — statute texts already obtained and read. These are the ground truth for step 3.
- `map/` — the frozen subject map (v3), the subject index, the cluster keys. The map does not change.
- `plan/` — Book 0's scope, the pilot inventories, the S48 source map and verification note.
- `check/records/B0/` — the finished Book 0 records, and `done/B0-as-published.docx` for the
  booklet as published. **Match these.** They
  carry more information about what is wanted than the rules below do.
- `check/` — the build. `python check/build.py --check` validates every record; `--subject B0`
  assembles and renders. Blocking failures are not negotiable.

## The register, and everything else about how to write

What follows is the style sheet exactly as it stands. Section 11 is the one to read twice: it was
written after the reader rejected a passage, and section 11a records what changed when two drafts
were compared blind.

---

# Authoring style sheet

The daily-use document. the specification below says what a record must contain; this says how it is written. Every rule here is checkable by a second reader, which is the test of whether it belonged in a style sheet at all.

---

## 1. Register

Write for an intelligent adult who knows nothing about this subject and is not stupid about anything else. Not a textbook voice, not a lecture voice, and not a chatty one. The nearest register is a good explanation given by a colleague who has decided to take the time.

- **One idea per sentence.** Not two joined by a semicolon, not four joined by "and". If a sentence carries a list of four things the reader has just met, it is four sentences or a list. The build warns above 35 words and above seven sentences in a paragraph; those are trip-wires, not targets, and a 22-word sentence carrying three ideas is the same defect.
- **Second person, present tense, for anything the reader is meant to do.** "Search inside the document for 279A", not "the document was searched". Reporting work that has already happened teaches nothing, however true it is: the reader watches someone else being competent.
- Say the thing rather than naming it. "Resolving it produced the Act's text" uses a word the reader met one paragraph ago and asks them to unpack it. "Open the Act. The text comes up." does the same work and costs nothing.
- No writerly phrases. "Borrowing the appearance of support" sounds good and tells a beginner nothing; "the citation is real and does not say what it was cited for" tells them everything.
- The next sentence connects to the previous one.
- No throat-clearing. The first sentence of a section is about the subject, not about the section.
- No false friendliness and no exclamation. No emoji anywhere in the corpus.
- Prefer the concrete to the abstract on first encounter, and give the abstraction afterwards once it has something to attach to.
- Never write "simply", "obviously", "just" or "of course" about a step the reader has not been taught. These words do no work and they tell a stuck reader that the problem is them.

**Notation: words first, then symbols, then symbols.** The book writes "divided by", "times" and "ten to the power seven" the first time each appears, immediately alongside the standard form — `450 divided by 700`, then `450 ÷ 700`. After that section, the symbol is used on its own. Writing out every operator for the whole book is the failure this rule exists to prevent: a reader who finishes Book 0 having never met `÷`, `×`, a superscript exponent or `log₁₀` cannot read the next thing they pick up, which is the one job the ground floor has. Introducing a symbol is a kindness; withholding it is not.

Write exponents as `10^7` and logarithms as `log10` in the record. A bracketed exponent works too, including one written in words: `10^(5 plus 2)`. The build typesets them as real superscripts and subscripts, so nobody writes markup in a YAML field. **No caret or tilde may reach the reader as itself**, and the build checks that on the rendered HTML after every render, because a record can be perfectly correct while the renderer drops a raw caret on the page — which is how `10^5 times 10^2 = 10^(5 plus 2)` sat in Part A with a live caret between two proper superscripts from the day Part A shipped. If that check prints, widen the pattern; never work round it by rewording the record. Set display arithmetic in a ```` ```working ```` block; an untagged fence still works and is flagged, and a bare four-space indent is a legacy form that used to make Word typeset arithmetic as computer source code.

**Anything with columns is a table, and must be tagged ```` ```table ````.** Columns set with spaces cannot survive: the page is typeset in a proportional face, so alignment that looks right in the record arrives as ragged prose. Write the cells separated by two or more spaces and the build draws the table. Where a header sits over some columns and not others, or a cell has to be empty, write the row with pipes instead — one piped row makes the whole block explicit, and `| 10^6 | 10,00,000 | | one million |` says what spaces cannot. A list of equations is not a table and stays in a working block; the build tells the two apart by the `=`, and warns when a working block has columns in it.

## 2. Floor compliance

The six operational tests in the specification below §1 are the hard rules. In practice:

1. **Name every symbol in words at first use**, in the same sentence. Not "where ρ is density" as an afterthought — "the letter rho, written ρ, stands for density".
2. **Introduce every unit** before it is used in a number, including kcal, kJ, mmol/L, kg/m².
3. **Say the equation in words immediately before writing it.** The words are the content; the equation is the compression.
4. **Every algebraic move is either taught in Book 0 or shown in full.** No skipped rearrangement.
5. **No clinical or biological premise arrives unestablished.** If a concept needs the pancreas, either Book 0 E8 covers it or this record does.
6. **Define or point.** A term of art is defined here, or linked to the `concept_id` that defines it. Never left to context.

A sentence that fails any of these is a defect with a fix, not a matter of taste.

## 3. First principles, honestly

The source document's own warning applies to the writing, not only to the research: first-principles reasoning is excellent at building understanding and unreliable at settling empirical questions. So the treatment follows the concept type, and the three are never blurred:

- **derivable** — build it. The reader should be able to reconstruct it from the floor. A derivation that skips is worse than no derivation.
- **empirical** — do not pretend to derive it. Say plainly that this is how the world turns out to be, give the evidence, give the effect size, and say what would overturn it. Deriving an empirical fact from plausible-sounding premises is the failure mode the source document names first: thermodynamics correctly implies energy balance governs weight, and the naive derivation that eating less is sufficient is wrong, because physiological compensation was not deducible.
- **institutional** — never present as a fact of nature. "The GST Council set this rate in September 2025" is the claim; "carbonated drinks are taxed at 40%" is not, because it will stop being true without anything about the world changing.

## 4. Illustrations

**How many.** One by default, and as many as earn their place. A concept that turns on a single
move needs one; a concept whose difficulty is that two situations look alike and behave
differently needs the two cases side by side, and giving it one is a false economy. Use the
`illustrations` list when there is more than one; `illustration` stays valid for a single one. The
test for a second illustration is the same as for a first: does the reader do something in it that
they could not do after the one before. An illustration that restates the previous one with
different numbers is a practice problem in the wrong place.

**Where the source lives is not the reader's problem.** An illustration that says "open
`sources/nfsa_2013.txt`" is written for someone holding this repository, which no reader is. Name
the instrument as its own title and give the public URL the bibliography would give; the search
string, the clause and the thing the reader is meant to notice all stay exactly as they were. The
locator in the record is the audit trail and belongs to the auditor. What the reader gets is a
citation number and a reference they can open.

- **An illustration is something the reader does, not something they are told about.** Give them the claim, the search string, the page, the step — in the present tense, addressed to them. If you find yourself writing "this was done and it showed", rewrite it as "do this, and watch what happens".
- **Lead with the failure where there is one.** A worked case that succeeds teaches the procedure; a worked case that fails teaches why the procedure exists. When a real attempt broke instructively, that goes first, and the clean case follows as contrast so the reader can feel the difference. Ending on the easy case is fine. Starting on it wastes the reader's attention at the moment they have most of it.
- **Real material, real dead ends.** The failures in this corpus are ones that actually happened while building it. An invented failure is a story; a real one is evidence, and the reader can go and reproduce it.
- **Indian context wherever the concept has Indian specificity** — foods, prices, institutions, cohorts, datasets, regional patterns. Elsewhere, Indian context by default anyway, because imported examples are a large part of why existing material is unusable here. A physics example may be a bicycle and a roti rather than a treadmill and a bagel.
- **Every illustration carries `analogy_breaks_when`.** Required, including for numerical examples, where it states the range over which the number holds. An analogy without its failure boundary teaches a misconception alongside the concept, and the reader has no way to know which part was the analogy.
- Worked calculations show every line. A reader who cannot follow line three cannot skip to line four.
- Real numbers, not invented ones, wherever a real one exists; and every number listed in `illustration.numbers` with its unit and citekey so the numbers register can audit it without re-reading prose.

## 5. Must-know points for you

Printed under that heading, in the second person, because they are addressed to one reader with one purpose: becoming someone whose analysis, data and testimony cannot be routed around. They are not a summary of the section and not a revision box.

**A `boundary` point names a limit of the technique, never the scope of the section.** "This catches an error of a factor of ten and never one of a factor of two, so it cannot be used to argue that an effect is big enough to matter" is a boundary: it tells the reader when to stop trusting the tool, which changes what they do with it. "This section gets you the arithmetic of a percentage" is not. It is a table of contents entry in the one place meant to survive after the section is forgotten, and four of them shipped in Part A before anyone noticed. The test is the same one every point faces — would it change what the reader does, says, accepts or refuses — and a sentence whose subject is *this section* almost never passes it.

**The number is not fixed.** As many points as the concept demands and no more. A small concept may carry three; a load-bearing one may carry eight. Padding to a template and cutting to a template are the same defect. The build's soft cap is nine, and going past it is a prompt to ask whether some of the material belongs in the illustration or in an exercise instead.

**Admission test.** A point earns its place only if it changes something you would **do, say, accept or refuse**. A statement that is true, interesting and changes nothing belongs in the illustration, or nowhere. Apply the test out loud: *knowing this, what would I do differently in clinic, in a protocol, in a committee room, in front of a journalist?* If the answer is "nothing", cut it.

**Every point declares its `bearing`** — which capacity of the expert it arms. This is what keeps the points pointed at the person being built rather than at general interest, and the build tallies them so a corpus that has drifted into all-methodology-no-clinic is visible rather than assumed.

| `bearing` | The point changes |
| --- | --- |
| `clinical` | What you do or say in front of a patient |
| `methodological` | What you accept as evidence, or how you design or critique a study |
| `policy` | What you say in a consultation, a committee or testimony |
| `teaching` | What you teach, or how you correct a trainee |
| `public` | What you say to a journalist or in public |

**`kind` is an optional tag**, for the author's own discipline and for composing revision sets later: `misconception`, `number`, `india_deviation`, `boundary`, `trap`, `consequence`, `dispute`, `move`. The build warns when a concept has no `misconception` and no `trap`, because "what does a reader who half-knows this get wrong?" is a question worth being made to answer every time. It warns, rather than blocks, because some concepts genuinely have no trap in them.

**Writing them.** One point, one paragraph, consequence inside the sentence rather than implied. Not a heading with the content left to the reader. `misconception` points state the error **as the error** and then correct it. `number` points carry one figure with its unit and source, not a list.

## 6. Teaching prompts and the audience triad

The source document scores explanation against three audiences, so the same three are reused across the corpus rather than invented per concept. Repetition is the point: it builds the competency by drill.

- **A first-year resident** — ten minutes, may use a whiteboard, expects mechanism.
- **A journalist** — three minutes, no jargon, one quotable sentence, and calibrated confidence including "the evidence is weak" said without becoming useless to them.
- **A health secretary** — one page, answer first, costed if a cost exists, no methods section.

A teaching exercise names which audience it is for. Prompts that would produce the same answer for all three are not teaching prompts.

## 7. Exercises

**Types** — fixed taxonomy. `integrative` is reserved for the interleaving booklets and is not authored inside a subject booklet.

| Type | Asks the reader to |
| --- | --- |
| `retrieval` | Produce a fact or definition from memory |
| `calculation` | Compute a quantity and state its units |
| `interpretation` | Read a table, figure or abstract and say what it does and does not show |
| `critique` | Find the specific flaw in a given claim, design or statement |
| `teaching` | Explain to a named audience from the triad, in the stated time |
| `design` | Specify a study, instrument, intervention or analysis |
| `build` | Produce the rung's artefact — the capstone |
| `integrative` | Solve a problem requiring concepts from several subjects (interleaving sets only) |

**Rules.**

- Every rung skill from the frozen map is demonstrated by at least one exercise somewhere in that rung. Checked by the build; `skill_ref` is how.
- Every build target in the map becomes the rung's `build` exercise. No exceptions — this is the mechanical link that keeps course and map in step.
- **Answers live in the appendix, never beside the prompt.** Worked reasoning, not just the result.
- `confidence_first: true` on exercises where recording a numerical confidence before checking is useful. This trains S59 calibration for free and costs a line.

## 7a. The drill set

**Every concept that teaches a mathematical technique carries a set of practice problems, in
ascending difficulty, unsolved in the text, answered in the appendix. This is mandatory. The
count is between three and eighteen, chosen from the technique, and the build blocks outside
that range unless `practice_note` says why.**

A reader who has worked one example of a technique has not learned it. A section can be read,
agreed with, and found impossible to use twenty minutes later; the drill set is what closes that
gap, and it is the cheapest thing in the whole method. That much is not negotiable.

**The count is, and the history of this rule is the reason to say so plainly.** Ten was written
here as a working figure and then enforced as an equality, so a concept with one move padded up to
ten and a concept with six moves stopped at ten. The count started driving the teaching instead of
following it. What has to hold is that the ladder below is climbed: the reader meets the technique
mechanically, applies it to a real quantity, diagnoses a broken version of it, and carries it
somewhere new. A technique with a single move reaches that in four problems. Logarithms, or
anything whose moves compose, may need eighteen and be right to.

The contrast with §5 survives at lower resolution: must-know points are as many as the concept
demands, and practice is as many as the *reader's fingers* demand, which is usually more. Err
high. An unnecessary problem costs a reader four minutes; a missing one costs them the technique.

**Which concepts.** A concept is quantitative when the reader has to be able to *carry something
out*, as against being able to *state* something. `quantitative: true` in the record says so. Left
out, it is derived: a Book 0 record in Part A, B, C or D is quantitative and one in E or F is not.
Set it explicitly on a subject record whose rung teaches a calculation, and explicitly to false on
a mathematical-Part record that genuinely teaches no technique. Getting this wrong in the
permissive direction is cheap; getting it wrong in the other direction means a technique shipped
that nobody can perform.

**The ladder.** Every problem carries a `level` from 1 to 10 and the band decides what the problem
is *for*. Levels may repeat and may be skipped — three mechanical problems all at level 2 is
normal — but the set must reach both ends: the build blocks a drill set with no mechanical problem
or no transfer problem, and warns when it touches fewer than three of the four bands. A set that is
all level 2 with different numbers is the failure this table exists to prevent; so is a set that
opens at level 7.

| Level | Band | The problem asks for |
| --- | --- | --- |
| 1–3 | mechanical | The technique on bare numbers. One step. No context, no unit, nothing to interpret. The reader is checking that their hands know the move |
| 4–6 | applied | A real quantity, with its unit and its label kept attached to the answer. Indian material by default, and a figure from `sources/` wherever one exists |
| 7–8 | diagnostic | A worked answer that is **wrong**. The reader finds the step that broke and says why the wrong answer looks reasonable. This is the band that transfers to reviewing other people's work |
| 9–10 | transfer | A claim in words — a sentence from a note, a press line, a thing said in a meeting. The reader decides what to compute, computes it, and then says what the answer does **not** establish |

Levels 9 and 10 are where the course's actual purpose sits, so they are not optional garnish on a
set of sums. A reader who can do levels 1 to 8 is numerate. A reader who can do 9 and 10 is
someone whose analysis cannot be routed around.

**Writing them.**

- **The prompt is unsolved.** No worked fragment, no hint, no restatement of the method. If the
  prompt contains the shape of the answer, it is a worked example and belongs in the illustration.
- **The answer shows every line**, exactly as §4 requires of any calculation. A reader who cannot
  follow line three cannot skip to line four, and in the appendix there is nobody to ask.
- **Real figures or none.** A problem quoting a real number names its `citekey` in `refs`, and the
  build rejects a citekey that is not in `check/references/library.bib`. Where no real figure exists, use bare
  numbers and say nothing about the world. **Never invent a statistic to make a problem feel
  applied** — an invented prevalence in a practice problem is the same defect as an invented one
  in the prose, and it is worse, because the reader is about to do arithmetic on it and remember
  the result.
- **Vary the move, not just the numbers.** Ten problems that differ only in their digits teach
  one problem ten times. Across a set, change what is given and what is asked for, and reverse
  the direction at least once.
- §9 applies here in full. A practice problem is where a course that teaches S35 and breaches it
  in a worked example gets caught.

**Where they go.** `practice[]` in the record, never `exercises[]`. The two do different jobs and
mixing them destroys both: `exercises` carry `skill_ref` against the frozen map and the rung's
build target, and ten drills dropped among them drown that signal. A quantitative concept carries
both — its exercises and its ten.

### Arithmetic is checked, and it is the only check that asks whether anything is true

Every other blocking check in the build is structural. This one evaluates both sides of every equation in reader-facing prose and blocks when they differ. It exists because a worked answer with a slip in it passes every structural gate, reaches the reader, and teaches the slip — and in a book made of arithmetic that is the defect that matters most.

Two exemptions are built in, both because the material needs them. The prompt of a level 7 or 8 problem holds a **deliberately wrong** worked answer for the reader to break, so diagnostic-band prompts are not checked; their answers are. And tolerance is set from the digits the text itself shows, so `17 divided by 7 = 2.428571429` passes and does not have to be written to full precision to do so.

It only checks what it can fully parse — plain arithmetic with the operators written as words, which §1 requires anyway. An equation it cannot parse is skipped silently rather than guessed at. That makes it a floor, not a proof: it catches the slip, not the wrong method.

## 7b. Where sources come from, and the one thing never to do

**Never write a claim from what the model knows and then attach a citation to it.** That is the
defect this section exists to prevent, and Part A shipped with eight instances of it: the prose
was written from model knowledge and given a `pending_arithmetic_text` anchor that named no real
book. A citation that cannot be opened is not a weak citation. It is a false one, because it
asserts a chain of provenance that does not exist, and it is worse than no citation at all —
an empty field invites a check, a plausible one does not.

The order is: **obtain the source, read the passage, then write.** `READY.md` and the source gate
already say this. Part A bypassed it on the reasoning that arithmetic is derivable, which was
true and which established a habit that is not survivable anywhere else.

**How much this matters depends on the concept type, and the build now enforces the difference.**
A `derivable` concept can be checked without its source — the reader rebuilds it from the floor,
and the anchor is where they go to confirm, not the evidence for the content. An unopened anchor
there is a debt, and it warns. An `empirical` or `institutional` concept cannot be checked that
way at all: it is true because a study measured it or a body decided it, and with the source
unopened nothing stands behind the claim except whoever drafted it. Where that was a model, that
means nothing stands behind it. **It blocks.** No booklet in the clinical, policy or epidemiological
subjects can be built without its sources in hand, and that is the intended consequence.

**§4's textbook widening does not soften this.** An `empirical` concept resting on a canonical
text still blocks until somebody has opened that text and located the passage. Settled science
changes which *kind* of source may stand behind a claim; it changes nothing about whether anyone
has read it. A textbook citation written from what the model already knew is the same defect as
`pending_arithmetic_text`, wearing a real title.

**Free, openly licensed, genuinely citable material covers most of what this course needs.** Prefer
it — not on principle but because a source the reader can open in one click is a source they will
actually check.

| Need | Where |
| --- | --- |
| Mathematics and statistics | OpenStax (CC-licensed, full texts), OpenIntro Statistics |
| Clinical and physiological reference | NCBI Bookshelf — Endotext and StatPearls are free, authored and dated |
| Primary evidence | PubMed Central open-access subset; Cochrane reviews |
| Indian statutes and rules | India Code; the issuing ministry's own site for notifications |
| Indian food regulation | FSSAI's own compendium PDFs, never a law firm's summary of them |
| Indian dietary and nutrient standards | ICMR-NIN |
| Indian survey data | NFHS and IIPS report PDFs, not news coverage of them |
| Guidelines and consensus | WHO; the relevant Indian professional body's own statement |

Two traps in that list. A secondary description of an instrument is not the instrument — a
consultancy's summary of the FSSAI labelling rules cannot be cited for what those rules say. And
an open textbook has a scope: Part A needed two anchors rather than one because OpenStax
*Prealgebra* does not cover logarithms, which was found by opening its table of contents and would
have been got wrong by anyone working from memory.

## 8. Citations

**What the reader sees.** A bracketed number in the text and a numbered list at the end of that Part. Nothing else: no file path, no author-date, no locator carried through the prose. Each entry gives the instrument or work, the clause consulted, and a resolvable URL, because a reference the reader cannot open is a claim rather than a citation. An entry whose source has not been obtained is marked outstanding and says so in plain words, under the list, so an unchecked claim can never look like a checked one. Numbering restarts at each Part.

**What the record carries** is the audit trail, and it is not the same object. Numbering is per source-and-clause, so a number always names exactly what was consulted.

- One reference minimum on every definition, of the `kind` the concept type requires.
- **`locator` is mandatory** — page, section, clause or table. A citation without a locator is not checkable and does not count.
- **`quote` is mandatory whenever the source is a file in `sources/`**, and it is the field that makes the audit real. Copy the exact words the claim rests on; the build searches the file for them and blocks if they are not there. Before this existed, the audit was a prompt telling a subagent to find the words, and the words went into the subagent's report and then nowhere — so a claim that was never in the instrument passed exactly as cleanly as one that was, and the only artefact of the check was the checker's assurance that it had checked. A number taken from a statute carries a quote for the same reason, and for a stronger one: a figure nobody can trace back to its words is the one kind of error a reader has no way to catch.
- **A number's quote must state the number.** Being in the source is not enough. Six figures in released sections — two protein values, the 5 kg and 35 kg entitlements twice over, and a count from the Constitution — once passed the quote check on words that were in the source and did not contain them: "5. Nutritional support to children", "35. Power to delegate", the heading ARRANGEMENT OF SECTIONS. Each was the first place the value's digits happened to occur in the file. Every one of the six figures was correct; none of the evidence was evidence. The build now reads the numbers a quote states, in digits or in words ("thirty-five", "ten lakh"), ignores list labels and clause numbers, and blocks unless the value is among them. **Never fill a quote by searching the source for the value's digits and taking the first hit** — that is exactly how all six were made. Find the sentence that gives the figure and quote that. A number counted from a passage rather than stated in it ("three Lists") carries a `derived` field saying how; the build passes it and reports it, because a derivation is a claim someone should be able to read.
- **`sources/INDEX.yml` says which file backs which citekey**, and it is not guessable from the filename. `constitution` resolves to `constitution_current.txt`; `constitution.txt` is a pre-2003 consolidation that does not contain Article 279A at all and is marked do-not-cite. Citing a do-not-cite file blocks. It is for the auditor; the reader meets it inside the reference entry, never in the sentence.
- `verified.opened` is set true only by the person who obtained and read the source. Never inferred, never copied from another record, never set because the citation looks right.
- A source that could not be obtained is recorded as such in `verified.note`, and the definition is marked `drafted`, not `verified`. An unobtainable source is a known state; a fabricated one is not recoverable.
- Institutional references cite the instrument, with its number and date, and the record carries `review.as_of`.

## 9. Language on weight and the people who have it

Non-negotiable, and it applies to every example, exercise, illustration and aside — not only to the clinical subjects. A course that teaches S35 and breaches it in a practice question is worse than one that never raised the subject.

- People-first construction: a person with obesity, never an obese person, never "the obese".
- No moral vocabulary for eating or weight: no cheating, no being good, no indulgence, no guilt, no bad foods.
- Weight change is described, not praised or deplored. No before-and-after framing anywhere, in text or image.
- Regain is described as a physiological outcome with a mechanism, never as a lapse.
- Illustrative patients have circumstances, not character defects. No example turns on a person's willpower.
- Prevalence and risk framing is checked for whether it makes life harder for people who already have the condition — and if it does, rewritten rather than footnoted.

## 10. The sequence read

An editorial commitment, not an aspiration: **read from the top in order, the material must be an easy read.** Not easy material — the subjects are not easy — but an easy read. The reader should never have to stop, go back, or hold something unexplained in their head while they wait for it to be explained.

**The test.** Before any booklet is released, read the assembled booklet — not the records — from the first line to the last, cold, in one sitting. Every place you have to re-read a sentence is a defect with a fix. Mark it as you go and fix it afterwards; do not stop to fix, because the point of the pass is the momentum.

**The rules that make it possible.**

1. **A section may assume everything before it and nothing after it.** Within a subject the build blocks a forward reference; within Book 0 the same rule holds by sequence and is on the author.
2. **A term is introduced once**, where the reader first meets it, and afterwards used in the same words. Synonym drift — "regulation", then "rule", then "the instrument" for the same thing — costs the reader a re-read every time.
3. **Acronyms are expanded at first use in document order.** The build lists acronyms used before anything expands them, and it catches the case where the expansion lives in a later section.
4. **At most one new term of art per paragraph.** Two is a paragraph the reader reads twice.
5. **A section that stands on the previous one says so in its first sentence**, in ordinary words, and does not assume the reader remembers the concept ID.
6. **Difficulty escalates by small steps.** Each section may be a little harder than the one before it. None may require a step the reader cannot take from where the previous one left them.

**Read this section with §11.** The sequence read is about order; §11 is about the words. A booklet can pass every rule here and still be unreadable, which is what happened.

**Authoring mechanics that affect the read.** Every prose field in a record is a YAML literal block, `|`, never a folded block, `>`. A folded block collapses each blank line into a single newline, which silently destroys every paragraph break and every markdown table in the field. The record looks correct, the booklet renders as a wall of text, and nothing reports it. The build now blocks on a folded prose field, and that check exists because the corpus shipped this defect once.

## 11. Plain language — the standard

This section exists because a sentence shipped that the reader could not read:

> *Indian statutes are frequently republished in consolidated editions of differing vintage, and official repositories host several at once without making the currency obvious. Checking the latest amendment a text mentions is a cheap and necessary habit.*

Nothing in it is false. Every rule in §1 to §10 passed it. It is still unusable: *vintage* means wine, *currency* means money, *repositories host* is computing, and three abstract nouns are stacked where one picture was needed.

**The standard, chosen by the reader this course is for:**

> *Here is the trap with Indian law online. One Act can exist in several copies, made at different times, all sitting on the same government website. None of them says "this one is old". So you do it yourself: open the copy, find the list of amendments, look at the newest date. If that date is older than the thing you are checking, you have the wrong copy.*

That is the register. Longer in sentences, shorter in each one, and every sentence is a thing you can picture or do.

**The rules it obeys, in the order they matter.**

1. **The everyday word wins.** If there is a word a person would say out loud, use that one. *Copy*, not edition. *Website*, not repository. *Old*, not of earlier vintage. *Up to date*, not current. *Get*, not obtain. The hard-word list in `prose/hardwords.yml` carries the ones this corpus has already tripped over, each with its replacement, and the build names the replacement in the warning.
2. **Never use a word metaphorically when its everyday meaning is commoner.** The reader's first meaning of *currency* is money and of *vintage* is wine. They will take that meaning, find it makes no sense, and re-read. Every re-read is a defect.
3. **One idea per sentence, then stop.** Where the sentence wants a comma and an *and*, give it a full stop instead. Sentences run to about fifteen words in this register and the build warns above twenty-five.
4. **Verbs, not piles of nouns.** "Checking the latest amendment a text mentions is a cheap and necessary habit" is a noun doing a verb's job. "Find the newest amendment it lists" is the same instruction, done. Two abstract nouns next to each other is a rewrite.
5. **Say what to do with your hands.** Open it. Search inside it for these words. Look at the date. Write it down. A procedural point that names no physical action has not been written yet.
6. **Name the trap, then the fix.** "Here is the trap with Indian law online" tells the reader what they are about to spend attention on. Then the fix, as steps.
7. **Consequences as if-then, in the reader's words.** "If that date is older than the thing you are checking, you have the wrong copy." Not "the edition may therefore be inapplicable".
8. **Terms of art: teach once, then use freely.** A short list survives because the subject needs it — statute, regulation, notification, Gazette, amendment, instrument, premise, inference, denominator. They are in `teach_once` in the hard-word list, each with the plain words it gets at first use. Everything else that sounds like a term of art is decoration and goes.
9. **Length is not the enemy; density is.** This register makes the book longer. That is accepted, and it is the trade the reader asked for. Do not win the length back by re-stacking clauses.
10. **`definition.text` is the one exception.** It stays technically exact, because a specialist has to find nothing in it to correct, and the build holds it to a looser threshold. That is precisely why `simplified_explanation` exists directly beneath it — the definition may be hard, and then the next field owes the reader the same thing in the register above.

**Checked, not hoped for.** The build measures every reader-facing field: sentence length, a reading-grade score, and every hit from the hard-word list. The thresholds are pinned to the two passages at the top of this section — the standard passes them, the sentence that started this passes none of them — so the numbers mean something rather than being picked to feel strict.

### 11a. What the reader's own comparison changed

Two drafts of the same section were written to the rules above, one pass each, and read unlabelled. The reader picked the one that **scored worse on every measure here**: reading grade 7.3 against 4.9, mean sentence 14.7 words against 10.1, longest sentence 31 words against 26.

That result is kept, and the measure is demoted, because the measure was answering a question nobody asked. Chopping prose into five-word fragments drives the grade down and makes the page harder to stay with, not easier. Three rules change:

11. **The reading grade is a ceiling, not a target.** Above 9 is a defect. Below it, the score says nothing useful, and a floor was tried and withdrawn: the chosen draft's own step-by-step passage runs at a mean of 9.9 words a sentence, under any floor that would catch real choppiness elsewhere. So rhythm is not measured. Aim where the chosen draft sits overall — mean sentence around fifteen words, grade around seven — and judge the clipped passages by reading them. The build scores whole fields of sixty words or more and says nothing about a single bullet, because a grade computed over one sentence is noise.
12. **Teach a hard word inline, with a dash, and keep going.** "Parliament passes a statute — a law made by elected lawmakers, voted on, signed off." Not a sentence of prose, then a sentence of definition, then a resumption. This is what made the chosen draft readable: nothing stops. §8's teach-once list says *which* words survive; this says how they are taught.
13. **Signposting in bold is rationed.** The rejected draft carried a bold label on almost every paragraph. Read cold, the labels fragment the page rather than guiding it. Use them where the reader genuinely needs to find their place again — steps of a procedure they will run — and nowhere else.

**The general lesson, for the next disagreement of this kind.** A measure that contradicts the reader loses. It stays in the build because it catches the sentence that started §11, and that is all it is for.

## 12. The compression pass

§11a settled how a sentence is written. This settles how much of the section survives, and it was settled the same way — by the reader reading unlabelled drafts and choosing.

**What the comparison was.** Book 0 section F4, at 917 reader-facing words, was cut three ways under identical constraints and read blind. Two versions were single-pass cuts by a model asked to remove what did not earn its place: they came back at 749 and 773 words. The third was cut by the method below and came back at 568. The reader chose the 568-word version, and not narrowly.

**What that result is evidence for, and what it is not.** The two single-pass cuts were made by different models, on the same brief, and landed 24 words apart — under three per cent of the section. So the model doing the cutting is not the lever, and choosing one is not a decision worth spending time on. The method is the lever. The prediction that a stronger model would over-cut, and a weaker one should therefore hold the knife, was made before the test and was wrong in its direction: both models under-cut, by almost exactly the same margin. Caution is the common failure here, not recklessness.

**Why a single pass under-cuts.** A model deciding whether a line is load-bearing has already read the section and understands it. When it tries to imagine the passage without that line, it fills the gap from its own understanding, silently, and concludes the line was unnecessary. It is not simulating a reader; it is consulting itself. The method below removes that problem structurally rather than hoping a model overcomes it, by making the cutter and the checker different contexts, and by giving the checker a text it has never seen whole.

**The method. Three steps, and the middle one is the point.**

1. **Cut hard.** The cutter is told to remove roughly half, to err toward cutting, and that a test downstream will catch its mistakes. It is not asked to be right. Being allowed to be wrong is what lets it cut at all.
2. **Test cold.** A reader in a fresh context is given *only* the cut text — not the original, not the rest of the book — and asked to do the section's exercises, list what the section taught, and then, exactingly, list every place it had to guess or supply something the text did not give it. This last instruction carries the whole method: a fluent read is exactly what hides a hole, so the checker is told to assume holes exist and hunt them.
3. **Restore only what the test proved.** The restorer puts back the original's own sentences, word for word, in their original places, and only where the gap report shows the reader was actually unable to do something. A passage does not come back because it reads well.

**What a fresh context requires, and what it does not.** The checker must not hold the full-length text, and must not be able to reach it. Those are two conditions, not one, and only the first is about context. A separate session that clones the repository can open `_build/` and read the original at will, so splitting the steps across sessions buys the first condition and leaves the second resting on an instruction the checker is free to disregard. The second is therefore enforced by what the checker can reach rather than by what it is told: the cut sections are copied into a directory holding nothing else, and that directory is what the checker is given. The first is satisfied by any context that has not seen the original, which a delegated subagent is by construction — it does not inherit the conversation that cut the text. The steps may therefore run inside one session, provided the thread that did the cutting never performs the cold read itself and the checker's directory is clean. A thread that has read the original cannot check it, whatever it has been instructed.

**The constraints, which bind every step.** Words are removed by deleting whole sentences and whole paragraphs, never by compressing. Two sentences are not fused into one longer one. A second idea is not pushed into a sentence that had one. §11a rule 9 stands: length is not won back by re-stacking clauses, and a compression pass that raised the mean sentence length has failed whatever its word count says. In the comparison the mean sentence ran 12.4 words in the original and 11.6 in the chosen version, with the longest sentence at 25 in both. The headings survive even where almost nothing survives under them. The exercises are not touched, and neither is the practice set: ten problems are ten problems after compression as before it, and a pass that cut two of them has changed what the reader can do rather than how much they had to read.

**The test set, and the constraint that §6 places on it.** Step 2 tests the cut against the section's own exercises. That is sufficient only for a concept nothing is built on. Where `provenance.bridge_ref` records that a later concept discharges a presupposition against this one, the cold reader's test set **must also include that presupposition**, stated as a task: *from this text alone, can you do the thing the dependent concept will assume you can do?* A cut that satisfies a section's own exercises can still strand the concept two rungs above it, and nothing in the section itself would show that. The bridge-sufficiency test is what makes this checkable; a compression pass run without it is safe for standalone sections and unsafe everywhere else.

**The second output, which is not optional.** The gap report will name holes the restorer cannot close, because the full-length original never filled them either. In the comparison, four of the five gaps found were of this kind — a term used throughout and never defined, a method asserted and never demonstrated, a generalisation the exercises depend on and the text nowhere states. These go to `DEFECTS.md` and back through the audit. They are the class of defect the audit cannot otherwise see, because the audit checks claims against sources and these are gaps between claims. A compression pass that reports only a word count has thrown away half of what it produced.

**Where it sits.** After the fix, not before it. Compressing before the defect list is applied means editing lines that are about to be deleted and deleting lines the defect list points at. The reader's own cold read of the assembled booklet stays last.

**What the word count is not.** It is not a target. 568 from 917 is what one section gave up under this method; another section will give up less, and a section that gives up nothing has passed rather than failed. A cutter told to hit a number will start compressing sentences to reach it, which is the one thing forbidden here.


---

# The specification

The authoring contract: what a record must contain, how concepts are inventoried, what the build
checks and why.

---

# Course specification

The authoring contract for the obesity expertise course. One concept record per teachable concept; records assemble into Book 0 and 61 per-subject booklets, and later into interleaving problem sets. This document fixes the rules. the style sheet above governs how the prose is written; `schema/concept.schema.json` is the machine-checkable form of what follows.

Derived against the frozen subject map, version id `fc19c8bc-a216-4131-99fb-ebe3f19cec4a`.

---

## 1. The reader floor

The floor is hard and it is low. Everything above it is taught.

**Assumed.** The reader can read English, can operate a calculator, and is willing to work a pen-and-paper example.

**Not assumed.** Anything else. No medicine, no physiology, no biology, no chemistry. No remembered mathematics — fractions, percentages, ratios, powers, algebra and rearrangement, graphs, functions, rates of change and elementary probability are all taught, in Book 0, from nothing.

This is deliberately below a class-10 syllabus, because a class-10 pass ten years old is not a class-10 syllabus. A reader who half-remembers something will be carried by material written for a reader who remembers none of it; the reverse is not true.

**Operational tests for a floor violation.** Any one of these is a defect, not a stylistic preference:

1. A symbol appears that has not been named in words at first use, including Greek letters.
2. A unit appears without having been introduced, including kcal, kJ, mmol/L and kg/m².
3. A term of art appears without a definition or a pointer to the record that defines it.
4. An equation appears without the sentence, immediately before it, that says in words what it claims.
5. A step in a derivation requires an algebraic move not taught in Book 0 or in the booklet's refresher.
6. A clinical or biological fact is used as a premise without having been established.

**Consequence for the mathematical subjects.** S02, S03 and S04 have an Introductory layer that is, for most of its length, a mathematics course. That is expected and is not a reason to raise the floor.

---

## 2. What the frozen map is, and is not

The map's rung-one bullets are **outcome statements** — descriptors of what that level means. They are **not** a concept inventory, and no concept count is fixed by them or anywhere else at this stage. Inventories are produced per subject by the method in section 5 and are expected to be substantially larger than the outcome lists, because an Introductory rung has to carry a reader from the floor to the doorstep of the Intermediate rung.

The scope gate is therefore **not** "is this bullet in v3". It is: **does this concept serve a stated outcome, a rung skill, the build target, the gate, or a bridge requirement?** A concept serving none of those is cut. Every record carries `provenance.outcome_refs` naming what it serves, so this is checkable rather than asserted.

Reading the bullets as outcomes rather than as an inventory is a change of use, not a change of content. The map stays frozen at v3; no v4 is required.

---

## 3. Introductory does two different jobs

| | Bridge rung | Terminal rung |
| --- | --- | --- |
| Subjects | 60 | S61 only |
| Purpose | Carry the reader from the floor to the start of the Intermediate rung | Deliver recognise-and-route competence, which is the whole of the subject's target |
| Scoped against | Rung-one outcomes **and** everything rung two presupposes | Rung-one outcomes and its own gate |
| Completeness criterion | The bridge-sufficiency test, section 6 | Gate satisfied; no bridge to build |

S61 is the one subject whose target level *is* Introductory. Its booklet is a routing directory, not a foundation course, and it must not be written as a bridge to nowhere.

---

## 4. Concept types, sourcing and review clocks

Every concept is exactly one of three kinds. The kind determines its treatment, the sort of source that may define it, and how fast it goes stale.

| Type | What it is | Treatment | Reference kind | Stability | Review trigger |
| --- | --- | --- | --- | --- | --- |
| **derivable** | Can be built from the reader floor by argument alone — conservation of energy, probability axioms, stocks and flows, what a matrix does | Derive it. Show the steps. The reader should be able to rebuild it | `textbook` (canonical text for the subject) | long | five years |
| **empirical** | Cannot be derived; true as a matter of observed fact — appetite circuitry, the thin-fat phenotype, activity dose-response | Assert with evidence. State the effect size and **what would overturn it** | `primary` or `systematic_review`; `textbook` for settled science, below | medium | two to three years |
| **institutional** | True because a body decided it — RDA values, statutes, tax slabs, cut-points, prices | Cite the instrument. Stamp an as-of date. Never present as a fact of nature | `instrument`, `guideline` or `consensus_statement` | short | **event**, not date |

**Event triggers** are named explicitly, not left as "when it changes": *next FSSAI notification*, *next GST Council revision*, *next NFHS round*, *next ICMR-NIN RDA revision*, *next Lancet Commission update*, *next patent or price change*.

**The four known short-stability items in the Introductory layer.** Measured against frozen v3, only four of the 309 Introductory concept and skill items carry a date, price or percentage. They are the most volatile content in the corpus and they sit in chapter one of their subjects:

- **S24** — semaglutide Indian patent expiry (20 March 2026) and generic price levels
- **S29** — ICMR-NIN RDA (2020); Indian Food Composition Tables (2017)
- **S41** — the 40% GST demerit slab on carbonated and caffeinated beverages (22 September 2025)

Every concept derived from these carries `review.stability: short` and an event trigger. Everything else in the Introductory layer is genuinely durable, which is what makes writing it first the right decision.

**Settled science, and why `empirical` accepts a textbook.** Added 23 September 2026, at the reader's direction, when Book 0 Part E was inventoried. Parts A to D are mathematics and Part F is reading, so until then every concept was either rebuildable from the floor or a decision some body took. Part E is the first that is neither. A plasma membrane is not reconstructible from arithmetic, so the concept cannot be `derivable` — §3 means that word literally. It is also not a finding with an effect size, so requiring `primary` would mean citing a research paper for the existence of the cell, which is worse scholarship than citing a canonical text and produces exactly the citation nobody checks.

So `textbook` is now an accepted kind on an `empirical` concept, and the discipline moves from the build to the author:

- **A claim with a number attached to it is not settled science.** An effect size, a risk, a dose-response, a prevalence, a measured rate — any of these still needs `primary` or `systematic_review`. A textbook anchor under a measured quantity is the failure this widening makes possible, and the audit is what has to catch it, because no mechanical check can tell the two apart.
- **Everything else about `empirical` is unchanged.** Stability stays medium, the review clock stays two to three years, and §7b's block on an unopened source applies in full: a textbook anchor that nobody opened blocks exactly as a primary one does.
- **Part E carries the first worked examples of the split.** The structure of a cell membrane is settled and takes a textbook. Atwater's 4/9/4 is `institutional`, because a body adopted those rounded values and can revise them. Resting metabolic rate and the thermic effect of food are measured, and take primary evidence.

**Consistency is enforced.** The build rejects a record with no reference of the kind its `concept_type` requires, and one whose `review.stability` does not match its type. A concept may also carry references of another kind — E2 is measured chemistry that rests in part on statutory energy factors — but an off-type reference must be held in `sources/` and quote the words it relies on, so it vouches for one checked passage and never for the concept as a whole. The sources of figures quoted in an illustration reach the reader's reference list on their own, marked where the figures appear.

---

## 5. The concept inventory method

Repeatable, and it terminates. Run it per subject per rung.

1. **Collect the terminal requirements.** From frozen v3: the rung's outcome statements, its skills, its build target and its gate. For a bridge rung, add everything the **next** rung's concepts and skills presuppose. This union is what the reader must hold or be able to do when the chapter ends.
2. **Regress each requirement.** For each, ask: *what must a reader already know for this sentence to mean anything?* Record the answer as a candidate concept. Repeat on each answer.
3. **Terminate only at the floor.** A chain ends when it reaches the reader floor of section 1 or an existing Book 0 concept. It may not end at "assume familiarity with", at a class-10 topic, or at a medical prerequisite. An unterminated chain is an incomplete inventory.
4. **Promote shared candidates to Book 0.** A candidate that appears in chains for two or more subjects and is not specific to any of them is Book 0 material, not booklet material. This is the rule that stops arithmetic being written 61 times.
5. **Cut anything unattached.** Every surviving candidate must name what it serves in `provenance.outcome_refs`. Interesting but unattached concepts are cut, not parked.
6. **Order by dependency.** Topologically sort on `concept_deps` and `ground_floor_deps`, assign `sequence`. The build fails on a forward reference within a subject, which is what makes the chain unbroken rather than nominally unbroken.
7. **Run the bridge-sufficiency test.** Section 6. Until it passes, the inventory is a draft.

The method makes inventory size an **output**, discovered per subject, not a budget set in advance.

---

## 6. The bridge-sufficiency test

The completeness criterion. Without it, "have I covered enough?" is a matter of taste.

**Procedure.** Enumerate every presupposition of the subject's Intermediate rung — each concept it names, each skill it demands, each term it uses without explaining. For each, identify the Introductory concept record that discharges it, and record the link in `provenance.bridge_ref`.

**Pass condition.** Every presupposition is discharged either by an Introductory concept in this subject, by a Book 0 concept, or by a named concept in a prerequisite subject that the reader is told to complete first. Nothing is discharged by assumption.

**Failure modes and what they mean.** An undischarged presupposition means the inventory is short. A concept discharging nothing and serving no outcome means the inventory is padded. Both are build-time reports, not judgement calls.

**S61** is exempt and is scoped against its gate instead, having no rung above it.

---

## 7. Thematic clusters

Defined in `clusters.yml`. Clusters group subjects that genuinely have to be integrated to solve a real problem, cutting across the map's 18 parts — a claim about a food needs measurement, causal and biological reasoning at once, and a claim about a tax needs economics, policy and systems reasoning at once.

Every concept carries one or more cluster keys. This is the composition hook for the interleaving problem sets, which are a **separate exercise** and are not specified here. The only requirement this document places on them is that they reference concepts by `concept_id`, which is why that ID is permanent and never renumbered.

---

## 8. Assembly and the checks the build runs

Records in, booklets out. The build is also the quality gate; these checks are the reason the pipeline exists before the writing does.

**Outputs.** Book 0; one booklet per subject, assembling that subject's rungs in order with a micro-refresher generated from the union of its `ground_floor_deps`; an exercise appendix per booklet with worked answers, never printed beside the prompt; a retrieval-item export; a numbers register; and a review-due report.

**Booklet front matter.** Every booklet carries an edition number and a rung-status line — for example `Rungs 1–2 released · rungs 3–4 in preparation` — so a partially written booklet is releasable rather than permanently unfinished. Institutional content additionally prints its as-of date.

**Blocking checks.** Forward reference inside a subject. Reference `kind` incompatible with `concept_type`. `review.stability` inconsistent with `concept_type`. Missing `locator` on any reference. A citekey, in a reference, in a must-know point or in a practice problem, that is not in `check/references/library.bib`. A concept with no `outcome_refs`. A concept with no must-know points, or with the retired five-slot mapping in place of a list. A prose field authored as a YAML folded scalar. An exercise with no worked answer, or of type `integrative`. **A quantitative concept whose drill set falls outside three to eighteen problems without a `practice_note` saying why, or whose ladder never reaches the mechanical band or the transfer band.** A practice problem with no worked answer. An unknown cluster key. A figure whose file is not in `check/figures/`. **An equation in reader-facing prose whose two sides do not evaluate equal.**

**Warning checks.** A reference with `verified.opened: false` — permitted while drafting, blocking at status `verified`. A bridge presupposition with no `bridge_ref`. A rung skill with no exercise anywhere in the rung. An institutional concept with no `as_of`. A concept past its review trigger. A `ground_floor_deps` entry with no corresponding Book 0 record. More must-know points than the soft cap of nine. A concept with no must-know point tagged `misconception` or `trap`. The sequence-read warnings of the style sheet above §10: an over-long sentence, an over-long paragraph, an illustration that never addresses the reader, and an acronym used in a booklet before anything expands it.

**Renderer.** Record assembly emits plain markdown and is independent of the renderer, so swapping one for another affects no content.

As built, the renderer is **pandoc**, producing **docx and HTML**. Quarto was the intended choice and is not usable here: it conflicts with the pinned pandoc in the shared environment, and the conda-forge build installed into a dedicated environment ships `quarto.cmd` and `quarto.js` with no working runtime, so every invocation fails. `build.py` therefore probes each renderer by running it, not by finding it on `PATH`, and takes Quarto automatically if a working install ever appears.

**Must-know points are not a fixed set of slots.** Every concept carries a list of points, printed as *Must know points for you*, and the length of that list is decided by the concept rather than by a template. Each point declares a `bearing` — `clinical`, `methodological`, `policy`, `teaching` or `public` — naming which capacity of the expert it arms, and a point that changes nothing the reader would do, say, accept or refuse is cut. The five fixed slots of the first draft are retired; the build rejects a record still using them. Full rule in the style sheet above §5.

**The drafting route, decided by blind comparison.** Two drafts of Book 0 section F5 were written from the same record, the same opened statute text and the same standard — one by the session model, one by a Sonnet-class model — and read unlabelled. The reader picked the Sonnet-class draft. So reader-facing prose is **drafted by that model and edited here**: the sourcing, the statute checking, the fact verification, the exercises and every build check stay on this side, and the draft arrives as prose to be corrected rather than prose to be accepted. The comparison also demoted the reading-grade measure, which had preferred the rejected draft; see the style sheet above §11a.

**The sequence read is an editorial commitment.** Read from the top in order, the corpus must be an easy read, and a place where the reader has to go back is a defect with a fix. Mechanically supported by the forward-reference check, the acronym check and the sentence and paragraph warnings; finally established by a human reading the assembled booklet cold, end to end, before release. Full rule in the style sheet above §10.

**PDF is unavailable in this sandbox.** Tectonic installs and reports its version but cannot resolve Windows platform directories inside the container, and no combination of `TECTONIC_CACHE_DIR`, `XDG_CACHE_HOME`, `APPDATA` or `USERPROFILE` overrides it; no other LaTeX engine is present. The build probes for a working engine by compiling a minimal document and, finding none, skips PDF with that explanation rather than emitting a failure per booklet. Two routes to PDF when it is wanted: a working Quarto with TinyTeX, or converting the docx on a normal desktop.
