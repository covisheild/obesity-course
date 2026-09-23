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

---

## What Parts D and E cost, and the model evidence of 23 September 2026

Each chat's own usage summary, in weighted tokens (weighted by what each kind of token costs).

**Part E chat, about 87M in total** (this total also covers a Part A compression run):

| Work | Weighted tokens |
| --- | --- |
| Drafting eight sections, 7 subagents | 20.5M |
| Re-reading instructions and history, main chat, every turn | 15.3M |
| Applying 57 audit fixes, 3 subagents | 15.1M |
| Checking and rebuilding sources, 2 subagents | 10.5M |
| Auditing, 3 subagents | 5.7M |
| Compression cutting, 12 subagents | 5.6M |
| Main-chat thinking and replies | 5.1M |
| Fetching source texts, 4 subagents | 3.9M |
| Git, builds and checks | 3.1M |
| Everything else | 2.5M |

**Part D chat, about 57M in total**, nine subagents using about 90% of it: fixers 22.7M, drafters
21.8M, auditors 7.7M, main chat about 5M, sources about 0.4M. One fixer given two sections (D6–D7)
used 9.6M alone. First drafts carried about 150 defects. The two fixers whose work was checked
both reported every defect closed; 27 and 23 were still open.

**What this showed.** Dealing with defects (fixing, verifying, rebuilding sources) cost more than
drafting in both chats. A long main chat cost as much again as all the fixing, just by re-reading
itself. Fixer self-reports could not be trusted. Two chats adding sources at once collided on a
citekey. Hence `PIPELINE.md`'s "Running a Part without waste", `check/SELFCHECK.md`, per-section
defect files, and Task 4b.

**The model evidence**, checked on 23 September 2026 against Artificial Analysis's Claude Opus
5.5 vs Claude Sonnet 5 comparison (Intelligence Index v4.3.2; Opus 5.5 scores marked as
estimates pending independent evaluation) and Anthropic's Opus 5.5 announcement of 22 September:

| Effort | Opus 5.5 index | Opus 5.5 cost/task | Sonnet 5 index | Sonnet 5 cost/task |
| --- | --- | --- | --- | --- |
| low | 42 | $0.55 | 24 | $0.51 |
| medium | 51 | $1.34 | 28 | $1.00 |
| high | 54 | $1.82 | 32 | $1.79 |
| xhigh | 56 | $3.46 | 34 | $2.87 |
| max | 58 | $5.98 | 38 | $5.09 |

Opus 5.5 at low effort outscores Sonnet 5 at max for about a ninth of the cost; there is no
effort level at which Sonnet 5 is the better buy. Max costs about 3.3 times high for four
points. Anthropic reports Opus 5.5 costs 40% less than Opus 5 at default (medium) effort on
typical workloads, with cache reads 60% cheaper, and raised subscription usage limits. Cost per
benchmark task is API pricing, not subscription usage; the two are assumed to move together and
that is not verified. Sonnet 5.5 is announced for the coming weeks, and the drafter question
(`PIPELINE.md` Task 2) should be re-settled then, by blind comparison, not by the index.

---

## Why compression now runs before the audit, and one book per chat (23 September 2026)

Harsh fixed three conditions: the compression pass stays (a 40 per cent cut is 40 per cent more
reading in the same time), no book is dropped, and accuracy is not traded for speed. Within them
the largest available saving was ordering: auditing and fixing the full draft and then cutting
about 40 per cent of it paid to check sentences no reader sees. Compression is deletion-only, so
auditing after it checks every claim the reader will see and none that they will not.

One book per chat replaces one phase per chat because what made long chats expensive was the main
thread doing work in its own context. A conductor that only delegates keeps its history to a few
thousand words of subagent results, while the drafting, auditing and fixing happen in subagent
contexts that are discarded. Book 1 is the test of both changes and records its cost per section
here.

Bundles stay: the GitHub connector writes from Claude Code but only reads from Cowork. One bundle
per book, one pasted command.
