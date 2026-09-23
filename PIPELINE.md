# How to run the pipeline

Seven prompts and then a read. Copy them as written. A Part runs as four chats, one per phase
(rule 1 below).

This file is instruction only. The measurements the method was designed from, and the record of
which rules changed and why, are in `MEASUREMENTS.md`, and nothing there tells you what to do. A
chat that has to work out which paragraphs of its own operating manual are still live will get
that judgement wrong sooner or later, so the history lives somewhere else.

Tasks 2, 3 and 5 are run by delegating to subagents rather than by doing the work in the main
thread. This is not only for speed. A subagent's work happens in its own context and only its
result comes back, so a Part's eight sections can be drafted, audited and cut inside one task
instead of exhausting one window by the third section. For Task 5 the delegation is also what
makes the method sound, for the reason given there.

---

## Running a Part without waste

Measured on Parts D and E (`MEASUREMENTS.md`, "What Parts D and E cost"): finding and fixing
defects cost more than drafting, and a long main chat cost as much again just re-reading itself.
These rules exist to cut that cost without weakening a single check. Nothing here removes the
independent audit, the quote gate, the arithmetic check or the cold read.

**1. One phase per chat.** A Part runs as four short chats, not one long one:
(a) inventory, source intake and draft; (b) audit; (c) fix and verify; (d) compression. Each
ends by committing a handover file and a bundle; the next starts fresh from the repository and
that file. A chat's history is re-read on every turn, so a chat that lives past its phase pays
for it on every later step.

**2. Model and effort per chat.**

| Chat | Model | Effort | Why |
| --- | --- | --- | --- |
| (a) inventory, sources, draft | drafter: see Task 2; main thread Opus 5.5 | medium | Opus 5.5's default |
| (b) audit | Opus 5.5 | high | the accuracy guard; the one place to spend |
| (c) fix and verify | Opus 5.5 | medium | fixing is correctness work; Sonnet fixers twice reported defects closed that were open |
| (d) compression | Opus 5.5 | low | every cut is checked mechanically by `books/B0/compress/validate.py` |

Never xhigh or max; the evidence is in `MEASUREMENTS.md`.

**3. Read only what the job needs.** Subagents do not read `claude.md` in full; each role reads
the sections listed in its task below. A drafter reads two exemplar records the orchestrator
names, not every finished record. A fixer reads its own section's defect file and its own
record, and its own section of the rendered booklet — never the whole booklet.

**4. Results come back short.** A subagent writes its details to a file in the repository and
returns at most 150 words: what it changed, what is still open, and the file path. The main
thread does not re-read records it has not been told are wrong.

**5. A self-report closes nothing.** "All defects closed" from a fixer is a claim, not a result.
Only Task 4b's verifier closes a defect.

**6. Two fix rounds, then the main thread.** If a defect is still open after two
fix-and-verify rounds, the main thread fixes it directly rather than launching a third fixer
that reloads everything to try again.

**7. Every defect type found twice becomes a check.** When an audit finds a kind of defect that
an earlier Part also had, the handover names it, and the next contract-change chat adds it to
the build or to the drafter's self-check (Task 2, last paragraph). Catching it at draft time is
the cheapest place it will ever be caught.

**8. Sources are taken in once, before drafting.** The main thread of chat (a) fetches and
files every source the inventory needs, to the checklist under the source gate, before any
drafter starts. Drafters and fixers never fetch.

**9. One writing chat at a time on shared files.** `sources/INDEX.yml`,
`check/references/library.bib` and `prose/GLOSSARY.md` are shared registries. Two chats adding
to them at once collide — Part D's odds source had to be renamed on rebase because F2 had taken
its citekey. Parallel chats are fine only when neither adds a source.

---

## Before anything: the source gate

Open `books/<SUBJECT>/READY.md`. If any line says **no**, the pipeline does not start.

This is not a formality and it is not satisfied by intending to find the source later. A record
whose concept is `empirical` or `institutional` and whose source is unopened is now a **blocking**
build failure, so a booklet drafted ahead of its sources cannot be committed clean. Retrieval from inside a
session works, but only up to a boundary that is worth knowing before you plan a Part around it.

**What a session can obtain.** HTML pages on hosts that do not gate robots. BIPM's own SI definition
and the NIST SI guide were both pulled whole on 22 September 2026 and are now in `sources/`. A
primary instrument published as a web page is reachable, and that covers more than it sounds like.

**What a session cannot.** PDFs — they fetch but yield no text, so the FSSAI labelling compendium
is readable by a model summarising it and not storable as a source anyone can quote against.
CAPTCHA-gated hosts, which includes NCBI Bookshelf and PubChem. Anything behind a login. Direct
downloads are blocked at the proxy, so there is no way around this from inside.

**What that means for planning.** A section resting on a PDF instrument cannot clear the source
gate from a session alone, and the gate now blocks rather than warns. Someone with a browser has to
put the file in `sources/` — which is a five-minute job and is the one part of this pipeline that
still needs a person. Find that out at the gate, before the inventory, not at the audit.

The style sheet §7b lists where to look, and prefers HTML primary sources for exactly this reason. Get that
file, drop it in `sources/`, add a line to `SOURCES.md` saying what it is, then begin.

**The intake checklist**, for every source filed, by the main thread and once. Each of these was
found wrong at audit in Parts E or F2, and each cost a rebuild:

- **Licence** read from the work's own details or copyright page, not assumed from the publisher.
  (All six OpenStax books used so far are CC BY-NC-SA 4.0, not CC BY.)
- **The header says exactly what the file holds**: which sections, and every omission marked in
  place. A header must never call an excerpt complete.
- **The citekey is new**: `grep` `sources/INDEX.yml` and `check/references/library.bib` before choosing it.
- `sources/INDEX.yml`, `check/references/library.bib` and `SOURCES.md` all updated in the same commit.
- No repository path in any reader-facing field of the `.bib` entry.

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
> sections it needs, what it must cover in one line, the source it will need, and whether it is
> **quantitative** — that is, whether the reader has to be able to carry the technique out rather
> than state it. Every quantitative concept owes ten practice problems at step 2 and the build
> blocks without them, so getting this column right here is what stops the drill sets being
> discovered late. No prose.
> Then write `books/<SUBJECT>/READY.md` listing every source, with obtained yes or no, checking
> `sources/` for what is already there.

## Task 2 — Draft. Delegate in batches.

**Which model drafts is an open question, to be settled once at the start of Book 1.** An
earlier blind comparison (`claude.md`, end) preferred a Sonnet-class draft's prose; that was
before Opus 5.5, which on the published index outscores Sonnet 5 at every effort level
(`MEASUREMENTS.md`). Settle it the same way: one
section drafted by each, read unlabelled by Harsh, correctness defects counted by the audit.
Until then drafters run on Sonnet as before.

Split the inventory into batches of two or three concepts and give each batch to its own
subagent, running them together. Each gets the prompt below with its own `<RANGE>`. They write
disjoint files, so they do not collide. The main thread collects the records and checks that the
glossary rows they added agree with each other before anything is written to
`prose/GLOSSARY.md` — two subagents cannot see each other's additions, and that is the one place
a batch can contradict itself.

> Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
> specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar
> records <EXEMPLARS> before writing a word — one of the same concept type, one with a drill
> set: they are the standard, and matching them matters more than following the rules in the
> abstract.
>
> Write records for concepts <RANGE> of `books/<SUBJECT>/INVENTORY.md`, one YAML file each, using
> `check/schema/example.concept.yml` as the template and `check/schema/concept.schema.json` as
> the schema.
>
> For every concept the inventory marks quantitative, write `practice[]` on the ladder in
> `claude.md` §7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with
> its unit, 7-8 diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words.
> **How many is your judgement, between three and eighteen**, and you choose it from the
> technique: one move needs few, several composing moves need many. Levels may repeat and may be
> skipped. The set must reach both ends of the ladder — a drill set with no mechanical problem or
> no transfer problem is a blocking failure — and say in one line, in your handover, why you
> chose the number you chose. Prompts carry no hint of the answer. Answers show every line. A
> problem quoting a real figure names its citekey in `refs`; where no real figure exists, use
> bare numbers rather than inventing one.
>
> For every factual claim, quote the exact words from the file in `sources/` that carry it, and
> put the file and section in the locator. If no file in `sources/` carries it, set
> `opened: false`, say in `verified.note` which instrument is needed, and write the concept so it
> does not depend on the unopened claim.
>
> The locator is for the auditor. **Never tell the reader to open a file in `sources/`** — they
> do not have this repository. Name the instrument by its own title and give the public URL from
> `check/references/library.bib`; the search string and the clause stay exactly as they were.
>
> A `boundary` must-know point names a limit of the technique — when the tool stops being
> trustworthy and what the reader should do then. It never describes the scope of the section.
> A point beginning "This section gets you..." is a table of contents entry and will be rejected.
>
> Prose fields are literal blocks (`|`), never folded (`>`). Anything with columns goes in a
> ```` ```table ```` block, never aligned with spaces inside a working block — a proportional
> face cannot hold the alignment. Set display arithmetic in a
> ```` ```working ```` block, never by indenting it — an indented block used to be typeset as
> computer source code. Write exponents as `10^7` and logarithms as `log10`; the build makes them
> real superscripts and subscripts, so do not write markup. Introduce an operator in words the
> first time beside its symbol, then use the symbol.
>
> Use `illustrations` (a list) where one illustration does not do the teaching, and
> `illustration` where it does. If a figure would show something the prose cannot say in the same
> space, do not draw it here — name it in your handover with the numbers it would use, and the
> main thread will decide.
>
> Before you hand back, check your own work as the auditor will. Run
> `python check/build.py --check` until blocking is zero for your records. Recompute every
> practice answer in Python, not by reading it. For every quote, confirm it is in the source
> file and states the number it is cited for. Check each item of `check/SELFCHECK.md`. Then
> return at most 150 words: records written, anything unsourced, anything you are unsure of.

## Task 3 — Opus. Audit. Delegate, and not to whoever drafted it.

One subagent per batch, and none of them may be the subagent that wrote the records it is
auditing. A context that wrote a claim will read its own words back as obviously supported; that
is the same self-consultation §12 describes, arriving at the audit instead of the compression
pass. Fresh contexts, every time.

> Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, and specification §4.
> You are auditing, not rewriting.
>
> For every claim in `books/<SUBJECT>/records/*.yml`: open the file `sources/INDEX.yml` maps
> the citekey to, search it for the words the record relies on, and **write those words into
> the record's `quote` field**. Not into your report — into the record. The build searches the
> source for them and blocks if they are absent, which is what makes this step check anything
> at all rather than assert that it checked.
> A claim that reads plausibly and is not in the file is the failure you are looking for.
>
> Then **recompute every practice answer**, line by line, rather than reading it. Ten problems a
> concept is ten chances to ship a wrong answer into an appendix where the reader has nobody to
> ask, and a reader who disagrees with a worked answer assumes they are the one who erred. Check
> also that each set actually climbs: ten problems at the same difficulty with different numbers
> satisfy the build and fail the reader.
>
> Then check currency: anything with a date, a price, a rate or a cut-point, against the
> instrument in `sources/`, and flag what needs re-checking against a newer one.
>
> Output **one file per section**, `books/<SUBJECT>/defects/<RECORD-ID>.md`: a numbered list.
> For each — the field, the claim, what the source actually says, and the smallest change that
> fixes it. Do not edit records other than their `quote` fields. Mark any defect whose *kind*
> you have seen in an earlier Part's defect files as **recurring**.

## Task 4 — Opus 5.5. Fix. One subagent per section.

Never one fixer for two sections: the one fixer that took two in Part D used as much as a
whole batch of drafters.

> Read `books/<SUBJECT>/defects/<RECORD-ID>.md` and the record it names. Read the parts of
> `claude.md` the defects cite, and nothing else of it. Apply every item. Then run
> `python check/build.py --check` and fix until blocking is zero for this record. The arithmetic
> check runs here: it evaluates both sides of every equation in reader-facing prose, so a
> blocking failure from it is a genuine slip in a worked answer and never a formatting
> complaint. Warnings about unopened references are expected and stay.
>
> Then run `python check/build.py --subject <SUBJECT>` and read **your section only** in the
> rendered output. Every place you have to read a sentence twice is a defect: fix it.
>
> Under each defect in the defects file, write one line: what you changed. Return at most 150
> words.

## Task 4b — Opus 5.5. Verify. A fresh subagent that did not fix.

> For each defect in `books/<SUBJECT>/defects/<RECORD-ID>.md`, read the fixer's line, then read
> the record and check the defect is actually gone — recompute any number, search the source
> for any quote. Check nothing else. Mark each defect **closed** or **open, because …**. Return
> the count of open defects.

Repeat Task 4 and 4b for any section with open defects, at most twice (rule 6 above). Then the
main thread writes `books/<SUBJECT>/HANDOVER.md`: what was written, what is still unsourced and
why, and every number that will need re-checking with its trigger.

## Task 5 — the compression pass. One task, three delegated steps.

Full rule in `claude.md` §12. Step 2 works only if the reader doing it has never seen the
full-length text **and cannot reach it**. Both conditions are load-bearing and they are met
differently.

**The context condition** is met by delegating step 2 to a subagent. A subagent does not inherit
the conversation that cut the text; it starts from the prompt it is handed and nothing else. It is
cold by construction, which a separate session is not automatically — a separate session that
clones the repository still has `_build/` sitting in front of it.

**The reachability condition** is met by the scratch directory. Before step 2 runs, copy the cut
sections somewhere that holds nothing else and hand the subagent that path. The original is then
not something the checker has been asked to avoid; it is something the checker does not have. This
is the part the pass has been running on trust, and it is the part worth fixing.

**The one rule that cannot be delegated away:** the thread that performed the cut must never
perform the cold read. It has the original in its context and cannot un-see it. It orchestrates;
it does not check.

Run all three steps in one task, in this order, delegating 5a and 5b and doing 5c in the main
thread. Delegate 5a and 5c per section or per Part as convenient; delegate 5b **once per Part**,
reading the whole Part's cut text in one sitting — a checker that has not seen the originals is
cold whether it reads one section or eight, and batching turns 3n tasks into 3.

The model matters less than anything else here. Measured on F4, two different models cutting on the
same brief landed 24 words apart. Run this chat at low effort; step 2 wants a clean context and
a clean directory, not a particular model or effort level. The cold reader must be given every
earlier Part's released text as well as the Part being cut, and the figures' captions and alt
text (`books/B0/compress/prepare.py release`).

**Setting up the scratch directory**, before any subagent is launched:

```bash
rm -rf /tmp/coldread && mkdir -p /tmp/coldread
cp books/<SUBJECT>/compress/*-pass1.md /tmp/coldread/
ls /tmp/coldread          # confirm: cut sections only, nothing else
```

### Step 5a — cut hard. Delegate one subagent per section.

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
> nothing. The exercises stay word for word, and so do all ten practice problems: they are what
> the reader can do, not what the reader has to read, and cutting one changes the first.
>
> Then say, in under eighty words, the one cut you were least sure about.

### Step 5b — test cold. One subagent for the whole Part, pointed at the scratch directory.

Launched by the orchestrating thread, never run by it. The prompt below is the whole of what that
subagent receives: it names no repository path, no subject, and no section, because a checker that
knows where the originals live is one helpful impulse away from reading them.

> Read the files in `/tmp/coldread/`. That directory is your entire world. Do not look anywhere
> else on the filesystem, do not search for other versions of this material, and do not use what
> you already know about the subject to fill gaps. If something is not in those files, it was not
> taught, and I need you to notice that rather than supply it.
>
> You are an intelligent adult with no prior background in this subject, who has read these
> sections once, in this order, and nothing before them.
>
> Take each file in turn. Answer its exercises as that reader, and work its ten practice
> problems. The practice set is the sharpest gap detector in this step: a hole in the teaching
> shows up as a problem you cannot start, and it shows up at a known level rather than as a
> vague unease. <Where a concept has bridge_ref
> dependents, add: Then do this, from the text alone: `<the presupposition the dependent concept
> discharges here>`.>
> Then list everything it taught you that would change what you do, say, accept or refuse.
>
> Then — the part that matters — list every place you had to guess, infer, or supply something the
> text did not give you, file by file. Quote the sentence that left each gap. Say what a reader
> without your background could not have done at that point. Include anything you read twice, any
> term used before it was explained, any step asserted but never demonstrated. Check hard before
> saying there are none: a fluent read is exactly what hides this.

Before launching it, confirm `/tmp/coldread/` holds the cut sections and nothing else. A stray
`_build/` copy in that directory silently voids the pass while every step still appears to run —
which is the same failure the old three-session split was written to prevent, arriving by a
different door.

### Step 5c — restore only what the test proved. Main thread.

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

## Task 6 — you. Optional, and not a gate.

*Changed 23 September 2026, on Harsh's instruction.* The course is for Harsh's own learning, not
for publication, so a Part is finished when Task 5 is: it merges to `main` without waiting for a
human read. Reading the booklet is studying it, and that happens anyway — so the read is not
dropped, it moves to where it costs nothing extra.

Where something is merely unclear, look it up or ask; that is the learning, and nothing needs
sending back. Where something looks **wrong** — a claim, a number, a rule the whole book follows —
add one line to `books/<SUBJECT>/READER-NOTES.md`: section, sentence, what is wrong. The next audit
or contract-change chat treats those lines as defects. This matters more than it sounds: the human
read of Part A found seven defects no gate could see, four of them rules followed everywhere
(`MEASUREMENTS.md`).

When you do read, the questions worth asking: The three questions worth asking, in order: did I have to read anything twice,
is there a point in the must-know list that would not change what I do, and does any claim make
me want to check it myself. The third one is the important one — if it does, check it, because
that is the audit working or failing in front of you.

The compression pass does not replace this and cannot. The defect it is built around is "I had to
read that twice", and re-reading is something a person does, not a property of text. What 5b buys
you is a shortlist: the sections whose gap reports came back longest are the ones to study most carefully.

---

## Running it without watching

Cowork's scheduled tasks run in the cloud and do not need your computer awake. Two practical
points. Tasks that touch files on your own machine need the desktop app open, so keep the project
folder in the Cowork project rather than depending on a local path. And schedule the tasks in
sequence rather than as one long one, so that a failure in the audit stops the book instead of
being written over by the next step. Within Task 5 the three steps stay in the one task, because
what makes step 2 sound is the subagent's context and the scratch directory, not a task boundary.

## What is not solved by any of this

Retrieval. Thirteen of S48's twenty concepts can cite something already opened. The other seven
cannot, and three of those are the most consequential in the booklet. No pipeline fixes that. A
person with a browser does.
