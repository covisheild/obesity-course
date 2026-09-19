# Working in more than one chat at once

The corpus is 43 Book 0 sections and 195 subject rungs through a six-step pipeline. That is not a
serial project. But parallel chats fail in a particular way — quietly, by drifting apart — and this
file is what stops that. Read it before opening a second chat.

Every chat is a separate cloud container. Nothing crosses between them except this repository, the
Notion tracker, and the saved skills. Anything a chat learns and does not write to one of those
three is lost when the chat ends.

---

## The order of operations

Fan-out is not a switch. It happens in this order and the order is not negotiable.

**1. Book 0 first, and Book 0 can be parallel now.** Every subject record declares
`ground_floor_deps` against Book 0 sections. Building subject books while the ground floor is still
moving means building all of them against a floor that changes underneath, with no way afterwards
to tell which records leaned on the old version. Book 0's own 43 sections are largely independent
of each other — `check/book0/OUTLINE.md` carries the few chains — so several chats can take
different Parts at once. This is where parallelism starts.

**2. Freeze Book 0.** Tag it. After that its sections change only through a deliberate amendment
that names every subject record built on them.

**3. One subject book, serially, end to end.** The compression pass has been tested on one section
and its bridge constraint has not been tested at all. If something systematic is wrong with the
method, running eight chats finds out after eight books instead of after one. Parallelism
multiplies the cost of a systematic error, and the errors worth catching early are exactly the ones
that look fine from inside any single chat.

**4. Then fan out across subjects**, at a width set by the rule below.

---

## The width limit

Task 6 is one person reading a booklet cold, end to end, in one sitting. That step does not
parallelize. Five chats produce five booklets queueing at one reader, and while they queue, later
work gets built on books whose defects are still undetected.

**Run no more chats than booklets you can actually read.** The compression pass helps triage — the
sections whose gap reports came back longest are the ones to read hardest — but it does not remove
the constraint.

---

## Who owns what

A chat owns exactly one subject and writes only inside it.

| Path | Owner |
| --- | --- |
| `books/<SUBJECT>/**` | the one chat building that subject |
| `done/**` | Book 0 chats only, one Part each |
| `sources/**` | append-only, any chat; never delete or replace another chat's file |
| `prose/GLOSSARY.md` | append-only, any chat; see below |
| `claude.md`, `PIPELINE.md`, `PARALLEL.md`, `check/**`, `map/**` | **nobody, mid-flight** |

The last row is the important one. The contract, the build and the frozen map are changed
deliberately, between rounds, in a chat that is doing nothing else — never by a chat that is in the
middle of a book and finds a rule inconvenient. A chat that thinks a rule is wrong writes that
down in its handover and carries on under the rule.

---

## Branches

One branch per subject: `subject/S48`, or `book0/part-F`. Push it. Merge to `main` only when that
booklet has passed the human read, so `main` is always the released corpus and never a work front.

Two chats never work on the same branch. If a chat needs something another chat is still writing,
it waits or it works around it — it does not reach into the other branch.

---

## Claiming work

The Notion Build Tracker is the lock. Before a chat writes a word it sets that unit's **Stage** to
the step it is starting, and sets it again when the step finishes. A unit already past **Not
started** belongs to someone.

The stages run: Not started, Source gate, Inventory done, Drafted, Audited, Build clean,
Compressed, Reader pass, Released.

A chat that finds a unit in a stage nobody is working on — a half-finished claim from a chat that
ended — reads that unit's Blocker and Notes before touching it, and does not assume the previous
chat got as far as the stage says.

---

## The glossary, and why it exists

`claude.md` §10 requires that a term is introduced once, where the reader first meets it, and
afterwards used in the same words. The build enforces this **within** a booklet. Nothing enforces
it across booklets, and the sequence read is per-booklet so it cannot catch it either.

With one chat this did not matter. With six, subject A and subject B will each "introduce" the same
term, differently, and neither will notice.

So: **before teaching a term of art, check `prose/GLOSSARY.md`.** If it is there, use the plain
words already recorded. If it is not, add it in the same commit that first teaches it. Append only;
changing an existing entry means every booklet that used it has to change too, which is a
between-rounds job, not a mid-flight one.

---

## What every chat reads before writing anything

1. `claude.md` in full. Not the summary, not the section it thinks is relevant.
2. The four records in `done/`. They are the standard, and matching them matters more than
   following the rules in the abstract.
3. `PIPELINE.md` for the step it is running.
4. `prose/GLOSSARY.md`.
5. The Notion tracker row for the unit it is claiming.

The skills carry the procedures, so that every chat runs the identical words rather than whatever
that chat's context happened to hold. If a procedure is worth repeating, it belongs in a skill and
not in a chat.

---

## Handover, every time

A chat that stops — finished, out of context, or interrupted — leaves
`books/<SUBJECT>/HANDOVER.md`: what was written, what is still unsourced and why, every number that
will need re-checking with its trigger, and anything it learned that the next chat would otherwise
learn again the hard way. Commit it. An uncommitted insight does not exist.
