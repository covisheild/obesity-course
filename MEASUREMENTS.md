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

---

## The type taxonomy met a Part it did not fit, and what that cost

Added 23 September 2026, when Book 0 Part E was inventoried.

The three concept types were derived from Parts A to D and Part F, and every one of those is
either mathematics or law. `derivable` covers what a reader can rebuild from the floor;
`institutional` covers what a body decided. Part E is the first Part that is neither, and the
taxonomy had no room for it:

| Claim | Rebuildable from the floor? | A finding with an effect size? | Type available before this change |
| --- | --- | --- | --- |
| A cell has a plasma membrane | no | no | none that fits |
| Breaking a bond takes energy in, forming one releases it | no | no | none that fits |
| Atwater's rounded 4, 9 and 4 kcal per gram | no | no — a body adopted them | `institutional`, and it fits |
| Resting metabolic rate in Indian adults | no | yes | `empirical`, and it fits |

Marking the first two `derivable` would have made that word mean two different things in one
corpus, and the reader would meet the second meaning in Part E without warning. Marking them
`empirical` would have demanded a primary study for the existence of the cell.

`empirical` now accepts a `textbook` anchor. The cost is that a mechanical check which used to
separate settled science from contested findings no longer can, so that separation moved to the
audit — a rule that was enforced became a rule that is judged. That is a real loss and it was
taken deliberately: the alternative was a citation class that nobody would ever check, which is
the failure §7b was written against in the first place.

**What to watch for.** The failure this permits is a textbook anchor under a number. If Part E
ships a measured quantity — a rate, a risk, a prevalence — resting on a canonical text rather
than on primary evidence, the widening was too wide and the next revision should carry a fourth
type instead of a looser third.

---

## What a session can actually retrieve, remeasured

`PIPELINE.md`'s source-gate section, written 22 September 2026, records NCBI Bookshelf and
PubChem as CAPTCHA-gated and unreachable. Remeasured on 23 September 2026 while clearing Part E's
source gate, and that is no longer true:

| Host | `curl` through the proxy | WebFetch |
| --- | --- | --- |
| openstax.org | rejected at CONNECT, 403 | works |
| ncbi.nlm.nih.gov (Endotext, Bookshelf) | rejected at CONNECT, 403 | works |
| fao.org | rejected at CONNECT, 403 | works |

Direct downloads are blocked at the proxy for every host, which is probably what the earlier note
measured. The distinction that matters is not the host but the tool.

### Reaching a page and transcribing a page are different problems, and the second one was nearly missed

The first four Part E source files were built with WebFetch, whose extractor is a small model with
a quote-length cap. They looked right. They were then checked passage by passage against raw page
text, and the check is the only reason this is in the file rather than in the corpus:

| Source file | Built with | Passages | Matched the page | Word for word |
| --- | --- | ---: | ---: | ---: |
| `openstax_chemistry_2e.txt` | WebFetch | 60 | 57 | 50 |
| `openstax_biology_2e.txt` | WebFetch | 43 | 43 | 27 |
| `openstax_college_physics_2e.txt` | WebFetch | 35 | 34 | 27 |
| `fao_food_energy.txt` | WebFetch | 7 | 7 | 5 |
| `openstax_anatphys_2e.txt` | **TinyFish** | 106 | 106 | **106** |

**A quarter of WebFetch's "verbatim" passages diverged from the page.** Mostly cosmetic — dropped
`(Figure 4.13)` markers — but not only: whole sentences were deleted mid-paragraph with no
ellipsis, and two passages were sentences that do not exist on the page at all. One was a specific
heat of water "for the liquid", welded out of the front of one sentence and the tail of another.
One was a table row carrying units imported from the column header. Both read as quotations.

`mcp__TinyFish__fetch_content` returns the raw page with no model in the loop. The one file built
that way was perfect first time. After rebuilding the other four from raw text, all five score
281 of 281.

**Why this was close.** The two fabricated passages would have passed the build's quote check,
because the check searches the source *file* — and the file is what had been smoothed. §8 says the
quote field "is the field that makes the audit real". It is, but only as far as the file is a
faithful slice of the page, and nothing in the build establishes that. The gate that caught it was
a separate fetch with a different tool and a script comparing the two.

**The rule this produced**, now in `sources/SOURCES.md`: a source file is transcribed with a tool
that has no model between the page and the file. WebFetch is for reading a page, not for quoting
one.

**What is still unproven.** A quote check against these files shows the words are in the file and
the file is a faithful slice of the page *as fetched on 23 September 2026*. It does not show the
page still says that, and a failed check does not show the passage is absent from the book, since
these are excerpts from named sections. `sources/INDEX.yml` names the sections held, for that
reason.
