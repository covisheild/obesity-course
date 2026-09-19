# How to run the pipeline

Seven prompts and then a read. Copy them as written. Each is one Cowork task, except Task 5, whose
three steps must be three separate tasks for the reason given there.

---

## Before anything: the source gate

Open `books/<SUBJECT>/READY.md`. If any line says **no**, the pipeline does not start. Get that
file, drop it in `sources/`, add a line to `SOURCES.md` saying what it is, then begin.

For S48 three files are missing and they are the three that matter most:

| Needed for | Instrument | Where to get it |
| --- | --- | --- |
| C11 labelling | Food Safety and Standards (Labelling and Display) Regulations, 2020 | fssai.gov.in, Regulations |
| C18 front-of-pack | the draft amendment on front-of-pack labelling, and its comment record | fssai.gov.in, Draft Regulations |
| C19 trans fat | the notification capping industrial trans fat at 2% | egazette.gov.in, or the FSSAI notification page |

Downloading those three is the single highest-value hour available. They cannot be reached from
a sandbox; they can be reached from a browser.

---

## Task 1 — Opus. Structure.

> Read `claude.md` in full. Read `map/subject-map-v3-FROZEN.md` for subject <SUBJECT>, and read
> `plan/INVENTORY-PILOT.md` to see what a finished inventory looks like.
>
> Produce the rung-1 concept inventory for <SUBJECT>, by the method in the specification: collect
> the rung's outcomes, skills, build target and gate, add everything rung 2 presupposes, regress
> each one to the reader floor, and stop only at the floor or at an existing Book 0 section.
>
> Output one table: concept id, name, type (derivable / empirical / institutional), the Book 0
> sections it needs, what it must cover in one line, and the source it will need. No prose.
> Then write `books/<SUBJECT>/READY.md` listing every source, with obtained yes or no, checking
> `sources/` for what is already there.

## Task 2 — Sonnet. Draft.

> Read `claude.md` in full. Read all four records in `done/` before writing a word: they are the
> standard, and matching them matters more than following the rules in the abstract.
>
> Write records for concepts <RANGE> of `books/<SUBJECT>/INVENTORY.md`, one YAML file each, using
> `check/example.concept.yml` as the template and `check/concept.schema.json` as the schema.
>
> For every factual claim, quote the exact words from the file in `sources/` that carry it, and
> put the file and section in the locator. If no file in `sources/` carries it, set
> `opened: false`, say in `verified.note` which instrument is needed, and write the concept so it
> does not depend on the unopened claim.
>
> Prose fields are literal blocks (`|`), never folded (`>`).

## Task 3 — Opus. Audit.

> Read `claude.md`. You are auditing, not rewriting.
>
> For every claim in `books/<SUBJECT>/records/*.yml`: open the file named in the locator inside
> `sources/`, search it for the words the record relies on, and record whether they are there.
> A claim that reads plausibly and is not in the file is the failure you are looking for.
>
> Then check currency: anything with a date, a price, a rate or a cut-point, against the
> instrument in `sources/`, and flag what needs re-checking against a newer one.
>
> Output `books/<SUBJECT>/DEFECTS.md`: a numbered list. For each — the concept id, the field, the
> claim, what the source actually says, and the smallest change that fixes it. Do not edit records.

## Task 4 — Sonnet. Fix.

> Read `claude.md` and `books/<SUBJECT>/DEFECTS.md`. Apply every item. Then run
> `python check/build.py --check` and fix until blocking is zero. Warnings about unopened
> references are expected and stay.
>
> Then run `python check/build.py --subject <SUBJECT>` and read the assembled booklet from the
> first line to the last. Every place you have to read a sentence twice is a defect: fix it.
>
> Write `books/<SUBJECT>/HANDOVER.md`: what was written, what is still unsourced and why, and
> every number that will need re-checking with its trigger.

## Task 5 — the compression pass. Three tasks, not one.

Full rule in `claude.md` §12. The three steps run as three separate Cowork tasks and this is not a
convenience: step 2 only works if the reader doing it has never seen the full-length text. Run them
in one task and the method is gone while still appearing to run.

The model matters less than anything else here. Measured on F4, two different models cutting on the
same brief landed 24 words apart. Use whatever is to hand for steps 1 and 3; step 2 wants a fresh
context, not a particular model.

### Task 5a — cut hard.

> Read `claude.md` §11, §11a and §12. Read `books/<SUBJECT>/_build/<SUBJECT>.md`, section <SECTION>.
>
> Write a deliberately aggressive compression of that section to
> `books/<SUBJECT>/compress/<SECTION>-pass1.md`. Aim at roughly half the reader-facing word count.
> A later step will test your output with a cold reader and restore whatever turns out to be
> load-bearing, so cut hard and let the test catch your mistakes. Do not be cautious.
>
> Remove words by deleting whole sentences and whole paragraphs. Never fuse two sentences into one.
> Never push a second idea into a sentence that had one. Keep every heading in order even where
> almost nothing survives under it. Keep the second person and the physical instructions. Add
> nothing. The exercises stay word for word.
>
> Then say, in under eighty words, the one cut you were least sure about.

### Task 5b — test cold. New task, and it reads nothing else.

> Read ONLY `books/<SUBJECT>/compress/<SECTION>-pass1.md`. Do not open any other file in this
> project, do not look for other versions of this section, and do not use what you already know
> about the subject to fill gaps. If something is not in that file, it was not taught, and I need
> you to notice that rather than supply it.
>
> You are an intelligent adult with no prior background in this subject, who has read this section
> once and nothing before it.
>
> Answer the section's exercises as that reader. <Where the concept has bridge_ref dependents, add:
> Then do this, from the text alone: `<the presupposition the dependent concept discharges here>`.>
> Then list everything the section taught you that would change what you do, say, accept or refuse.
>
> Then — the part that matters — list every place you had to guess, infer, or supply something the
> text did not give you. Quote the sentence that left each gap. Say what a reader without your
> background could not have done at that point. Include anything you read twice, any term used
> before it was explained, any step asserted but never demonstrated. Check hard before saying there
> are none: a fluent read is exactly what hides this.

### Task 5c — restore only what the test proved.

> Read `claude.md` §12, the original section, `<SECTION>-pass1.md`, and the gap report from 5b.
>
> Restore text from the original where, and only where, the gap report shows the reader was
> actually unable to do something. Put the original's own sentences back word for word, in their
> original positions. Write nothing new. Do not restore a passage because it reads well.
>
> Where the gap report names a hole the full-length original did not fill either, you cannot fix it
> here and must not try. Collect those separately and append them to `books/<SUBJECT>/DEFECTS.md`
> under a heading "Found by the compression pass". They go back through the audit. They are the
> defects the audit cannot see on its own.
>
> Then run `python check/build.py --check` and `--subject <SUBJECT>`. The mean sentence length must
> not have risen. If it has, something was compressed rather than deleted, and that is a failure
> whatever the word count says.

## Task 6 — you

Read the booklet. The three questions worth asking, in order: did I have to read anything twice,
is there a point in the must-know list that would not change what I do, and does any claim make
me want to check it myself. The third one is the important one — if it does, check it, because
that is the audit working or failing in front of you.

The compression pass does not replace this and cannot. The defect it is built around is "I had to
read that twice", and re-reading is something a person does, not a property of text. What 5b buys
you is a shortlist: the sections whose gap reports came back longest are the ones to read hardest.

---

## Running it without watching

Cowork's scheduled tasks run in the cloud and do not need your computer awake. Two practical
points. Tasks that touch files on your own machine need the desktop app open, so keep the project
folder in the Cowork project rather than depending on a local path. And schedule the steps
as separate tasks in sequence rather than one long one, so that a failure in the audit stops the
book instead of being written over by the next step. Task 5b has a second reason to stand alone:
it is only worth running in a context that has not seen the full-length text.

## What this actually costs

Measured on the four Book 0 sections written in the pilot:

| | |
| --- | --- |
| Reader-facing prose | about 1,000 words a section, before compression |
| Drafting | four sections in about a minute of model time |
| Editing after the draft | roughly ten sentence-level fixes a section |
| Factual errors found in audit | three across four sections |
| Check warnings, before and after | 54, then 3 |

Measured on F4 when the compression pass was added:

| | |
| --- | --- |
| Reader-facing prose, after compression | 568 words, from 917 |
| Cut by a single judging pass instead | 749 and 773 — the two models 24 words apart |
| Restored by the cold test | 78 words, in two passages |
| Gaps found that the original had too | four, now in `DEFECTS.md` |
| Mean sentence length, before and after | 12.4 words, then 11.6 |

The drafting is not the slow part and never was. The audit is, and it is the part that must not
be skipped. The compression pass is cheap in model time and its real output is the second table's
last row.

## What is not solved by any of this

Retrieval. Thirteen of S48's twenty concepts can cite something already opened. The other seven
cannot, and three of those are the most consequential in the booklet. No pipeline fixes that. A
person with a browser does.
