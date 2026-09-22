# Book 0 · Part C concept inventory

Sections C1 to C9 of `check/book0/OUTLINE.md`. Produced 22 September 2026 against frozen map
`fc19c8bc-a216-4131-99fb-ebe3f19cec4a`, by the method in the specification §5.

---

## What makes Part C different, and this time it is the shape

Parts A and B are mostly lists. Their sections lean on each other here and there — B2 needs A2's
fractions — but you could write A5 without having written A4, and the sections could be drafted in
almost any order.

**Part C is a chain.** Nothing in it stands alone:

```
C1 variables ──┬── C2 rearranging ─── C3 two equations at once
               │
               └── C4 functions ─── C5 graphs ─── C6 recognising shapes
                                      │
                                      └── C7 rate of change ─── C8 accumulation ─── C9 stocks and flows
```

Two consequences the drafting has to respect. Batches must follow the chain rather than cut across
it, because a drafter writing C5 needs to know exactly what C4 established and in what words. And
the sequence read matters more here than anywhere so far: a term introduced late, or introduced
twice in different words, breaks a chain rather than a single section.

## Where the Part is going, and it is not all nine sections

`check/book0/OUTLINE.md` records what the pilot subjects actually declare against Book 0. From the
whole of Part C, S01 needs **C5 and C9**, and S48 needs nothing at all. The outline is explicit
that an earlier draft guessed C6, C7 and C8 were needed and guessed wrong.

That is not an argument for cutting seven sections. It is the reason to know which two the Part is
*for*. **C9 is the terminus** — energy balance is a stock-and-flow model, and C9 is where a reader
becomes able to think in one. **C5 is the other exit**, because every figure in every subject book
is read with it. The remaining seven exist to make those two possible, and each should be written
knowing which of the two it is feeding.

---

## The terminal requirements, before regression

**1. The outline's own notes.** C6 "lets a reader read a curve before differentiating one"; C7
"the derivative, taught as a rate"; C8 "the integral, taught as a total"; C9 "shared by S01 and
S44; promoted here by the §5 step-4 rule".

**2. What Part B leaves owed.** B6's drill set had to drop a problem that recovered a missing mass
from an index and a height, because rearranging is taught here and not there. **C2 must carry that
problem.** It is a good application of the technique and it closes a real gap rather than inventing
an exercise.

**3. What the subject books presuppose.** S01 reads energy balance as a stock with an inflow and an
outflow. Nothing in Parts A or B lets a reader hold that idea; C9 is the only place it arrives.

---

## The sections

All nine are `derivable`. No new institutional or empirical source is needed anywhere in this Part,
which is why it can be written now: the source gate that held B5 does not apply.

| § | Concept | Anchor | Drill set | Feeds |
| --- | --- | --- | --- | --- |
| C1 | Variables and algebra: what a letter stands for | College Algebra 2e ch. 1–2 | 5–7 | C2, C4 |
| C2 | Rearranging an equation | College Algebra 2e ch. 2 | 10–12 | C3, and Part B's debt |
| C3 | Two equations at once | College Algebra 2e ch. 7 | 8–10 | — |
| C4 | Functions: input, rule, output | College Algebra 2e ch. 3 | 6–8 | C5 |
| C5 | Graphs: axes, scale, slope, intercept | College Algebra 2e ch. 4 | 10–14 | **S01**, C6, C7 |
| C6 | Recognising shapes: linear, exponential, saturating | College Algebra 2e ch. 4–6 | 8–10 | C7 |
| C7 | Rate of change, without the machinery | Calculus Volume 1 | 12–14 | C8 |
| C8 | Accumulation, without the machinery | Calculus Volume 1 | 10–12 | C9 |
| C9 | Stocks and flows | Calculus Volume 1 | 10–12 | **S01**, S44 |

### Where C7 and C8 stop, stated before anyone drafts them

"Without the machinery" is the whole design of these two sections and it needs a boundary somebody
can hold a draft against, or it will drift into a calculus course.

**C7 teaches:** a rate is a change in a quantity divided by the time it took; the difference
between an average rate over an interval and the rate at an instant; that the slope of a line
joining two points on a graph *is* the average rate between them; how to read a rate off a curve by
looking at its steepness; and that a rate carries units, which is B3's check applied here.

**C7 does not teach:** limits, the rules for differentiating anything, or `dy/dx` beyond naming it
once so the reader recognises it on a page somebody else wrote.

**C8 teaches:** that a rate multiplied by a time gives an amount; that adding those amounts across
successive intervals gives a running total; that the area under a rate-versus-time graph is that
total; and that the total is only as good as the assumption that the rate held over each interval.

**C8 does not teach:** antiderivatives, any rule of integration, or `∫` beyond naming it.

The test for both: **a reader should finish able to say what a derivative and an integral are for,
and unable to compute either symbolically.** That is the correct outcome, not a compromise. A
person who can read a dose-response curve and say what its steepness means is better served than
one who can differentiate a polynomial and cannot.

### C9 · Stocks and flows — the section the Part is built to reach

A stock is a quantity that exists at a moment. A flow is a rate that changes it. The stock at any
time is its starting value plus everything that flowed in minus everything that flowed out, which
is C8 applied to a real object rather than a graph.

This is the physical reading of C7 and C8 and it is where S01 begins. It must land the point that
**a stock can be large and stable while both flows are enormous**, because that is the shape of
every energy-balance argument and the intuition most often missing from discussions of weight.

Draw the examples from quantities the course already holds, not from invented ones.

---

## Figures: the first Part where they are not optional

A6 and A7 each earned one figure. Parts A and B needed four between them.

**C5 cannot be taught without pictures.** A section on axes, scale, slope and intercept, delivered
as prose, is a description of something the reader never sees. The same is true of C6, whose entire
content is that three shapes look different and that you can tell which you are looking at.

Expect, and budget for:

- **C5** — one figure showing the same data on two differently scaled axes, because the point that
  a scale can be chosen to flatter or alarm is the one that transfers to every paper the reader
  will read. A second showing slope and intercept read off a line.
- **C6** — one figure putting linear, exponential and saturating curves side by side on the same
  axes, which is the only way the recognition it teaches can be practised.
- **C7** — one figure showing a chord between two points on a curve and the steepness at a single
  point, because that is the distinction the section turns on and prose handles it badly.
- **C8** — one figure showing the area under a rate curve as a stack of rectangles, which is the
  idea, drawn.

That is four to six figures for one Part, against four for the two Parts before it. Every one must
read its numbers out of the record it appears in, as the existing figures do, and the bar is
unchanged: a figure earns its place only when it shows something the prose cannot say in the same
space. For these sections it clears that bar easily, which has not been true before.

---

## Dependencies, declared

| Section | Needs | Why |
| --- | --- | --- |
| C1 | A1 | Place value, before a letter can stand for a number |
| C2 | C1, A2 | Rearranging is done with fractions |
| C3 | C2 | Two equations are solved by rearranging one |
| C4 | C1 | A function takes a variable as its input |
| C5 | C4, A5, B2 | A graph's axes carry units and its slope is a rate |
| C6 | C5, A6, A7 | Exponential shapes need powers; log axes need A7 |
| C7 | C5, A5, B3 | A rate is a ratio with units, and B3's check applies to it |
| C8 | C7, A5 | A running total is built from rates |
| C9 | C7, C8, B4 | Energy balance is the worked case, and it is in joules |

## What is not decided here

Whether C3 earns its place. Two equations at once is standard in an algebra course, and nothing in
the pilot subjects' declared dependencies reaches for it. It is written because the chain in the
outline includes it, but it is the one section of Part C whose necessity should be questioned at
the human read rather than assumed now.
