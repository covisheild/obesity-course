# What the method cost when it was measured

This file is history, not instruction. Nothing here tells a chat what to do; it records the
numbers the pipeline's design was argued from, so that a later change can be checked against
evidence rather than against memory. `PIPELINE.md` is the operating manual and carries no
measurements, because a chat reading it to run a step should not have to work out which
paragraphs are still live.

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


---

## The practice-count rule, and why it is a range now

The drill set was specified as exactly ten problems, levels one to ten, each used once, and the
build enforced it as an equality. Two days of use showed the cost: a concept with a single move
padded up to ten, and any concept with several moves stopped at ten whether or not the ladder had
been climbed. The count had started driving the teaching.

It is now three to eighteen, with the bands as the real constraint (STYLE.md 7a). The episode is
worth keeping because of how it arose: the number was given in conversation as a rough figure and
written into the contract as a law. When a rule is set mid-flight, the thing to settle before
implementing it is not what the rule says but how strictly it binds.

---

## Book 0 Part A, and what a human read found that the machinery did not

Part A went through Tasks 1 to 5 and came out with a clean build, a compression pass and a gap
report. A person then read it and found seven defects in about twenty minutes, none of which any
automated gate had been capable of seeing:

| Found | Class |
| --- | --- |
| Illustrations told the reader to open `sources/*.txt`, a path only this repository has | contract specified wrongly |
| The drill-set count was rigid where it should have been judged | contract specified wrongly |
| One illustration where the concept needed two | contract specified wrongly |
| Operators spelled out in words for the whole book, so standard notation was never introduced | contract specified wrongly |
| 186 paragraphs of arithmetic typeset as computer source code | renderer |
| Citations inline as author-date with locators, and no per-Part bibliography | renderer |
| Content that should have been tables written as indented pseudo-layout | renderer and content |

The split is the lesson. Four were rules that were followed exactly and were wrong; three were in
the build, where no amount of care in the authoring would have caught them. Neither class is
found by a gate that checks records against sources, which is what the audit does.
