# C4 · Functions: input, rule, output

**Definition.** A function is a rule that attaches to every input it accepts exactly one output.

The collection of inputs the rule accepts is its domain. The collection of outputs it can
return is its range.

Two different inputs may share one output, and the rule is still a function. The requirement
runs in one direction only.

A function is written as a name with its input in brackets, so f(x) means the output that the
rule named f gives for the input x. The brackets do not mean multiplication.

**In plain terms.** A function is a machine with one slot in and one slot out.

You drop a number in. One number comes out. Drop the same number in tomorrow and the same number
comes out, because the rule has not changed.

One input may give one output and no more. If the same input gives you 20 today and 35 tomorrow,
you are not holding a rule at all. You are holding something else, and you cannot use it to
answer a question.

There is a short way to write a rule down. Give it a name, say f. Write f(4), said out loud as
"f of 4", for the output the rule gives when you put 4 in. The brackets here do not mean times.

A rule can also be run backwards, from an output to the input that gave it. You undo what the
rule did, the way the section on rearranging undid each step. That gives a single answer only
where no two inputs share an output. Where two inputs do share one, going backwards from that
output leads to both. Nothing in the output tells you which.

Two names, so you recognise them on somebody else's page. The inputs a rule will accept are
called its domain. The outputs it can give back are called its range. Ask a rule what it accepts
and what it does not. That is often the quickest way to catch somebody running it outside what
it was built for. A rule that counts people takes whole numbers from one upwards. Half a person
is not an input it has an answer for.

Be careful with the second of those two words. In statistics, range means something else
entirely, which is the largest value in a set of measurements minus the smallest. The two
meanings have nothing to do with each other and you will meet both. Which one is meant depends
on whether the thing being described is a rule or a set of measurements.

**Illustration.** A block register lands on your desk. It lists four households, how many people are in each, and
the foodgrains each is counted for in a month. The register is made up for this section.

```table
household  people  kilograms a month
A          4       20
B          6       30
C          4       35
D          5       25
```

How many kilograms does it give for a household of four?

You cannot answer. Household A says 20 and household C says 35. One input has two outputs, so
this table is not a function of the number of people.

That is a finding rather than a dead end. Something other than the number of people differs
between A and C, and the register does not say what. Until somebody tells you what, you cannot
work out a single row from the number of people alone.

Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains per person per month.

That sentence is a function. The input is the number of people. The rule is "multiply by five
kilograms a month". The output is kilograms of foodgrains a month.

Put four in.

```working
    5 times 4 = 20
```

Twenty kilograms a month.

Write the rule short. Call it g. Let n stand for the number of people, in the way a letter
stood for a number in the section on variables.

```working
    g(n) = 5 times n
```

Households A, B and D match it. Household C does not.

```working
    5 times 4 = 20
```

One input, one output, and anything that does not match is a question for whoever wrote the
register.

Now run the rule backwards once. A priority household is counted for 30 kilograms a month.
How many people are in it? The rule multiplied by five, so undo it by dividing by five.

```working
    30 divided by 5 = 6
```

Six people. Check it forwards.

```working
    5 times 6 = 30
```

That backwards step is safe here. Each extra person adds five kilograms, so no two household
sizes share an output, and 30 points to one size only.

The section on ratios gives the likely reason for household C. A proviso just below section
3(1) covers households under the Antyodaya Anna Yojana. It entitles them to 35 kilograms a month.
It does so "to such extent as may be specified by the Central Government for each State in the
said scheme". So the Central Government sets how far the scheme reaches in each State. The 35 is
per household, whatever its size.

If C is an Antyodaya household, the register holds two rules, and the row is right. The register
does not say which scheme C is under. So treat this as the likely explanation and ask.

That rule also shows why going backwards can fail. Under it, a household of two and a household
of nine both get 35 kilograms. Given 35, the rule cannot tell you the size.

**Where this picture breaks.** The one-slot machine holds while the rule takes one input. Many real rules take two.

The index you met in the section on body-size units needs a mass and a height together. That is
still a function.

The machine says nothing about whether a rule is true of the world either. A rule can give
exactly one output and still be the wrong rule.

**Must know points for you.**

- When a table lands in front of you, look for one input appearing twice with two different outputs before you compute anything from it.
- Two inputs sharing one output is fine. One input with two outputs is not.
- Outputs that climb for a while and then fall again break nothing. So for this test, look for the repeated input, not for the shape of the outputs.
- When the same inputs give a different answer on a second run, something you did not notice changed. Find what changed before you trust either answer.
- Name the input, the output and the unit of each before you write anybody's rule on a whiteboard.
- A function says the output goes with the input. It never says the input produced it.
- Run a rule backwards only where no two inputs share an output. Where two do, an output points back to more than one input, and a single answer from it is a guess.

**Exercise 1** (critique). A colleague sends you a two-column table of three hundred rows and calls it "the rule we use".
You find that one value in the first column appears twice, with two different values beside it.

Say what that means for the table, and say what you would ask for next.

**Exercise 2** (teaching). A first-year resident says they can never keep formulas straight. You have ten minutes and a
whiteboard.

Teach them what a function is, so that they leave able to check whether something handed to
them is one.

**1.** A rule multiplies the input by 3 and then adds 2.

Work out the output for the inputs 0, 1, 5 and 10.

**2.** Three tables are below. For each one, say whether it is a function of its first column, and say
what told you.

```table
first   second
1       4
2       8
3       12
```

```table
first   second
1       4
2       8
1       9
```

```table
first   second
1       4
2       4
3       4
```

**3.** A rule adds 7 to its input.

The outputs are 12, 19 and 40. Work out the input that produced each one.

**4.** A district office runs this rule to plan its grain lifting. Let n stand for the number of
people in a household. The rule gives the kilograms of foodgrains a month that household is
counted for.

```working
    g(n) = 5 times n
```

Say what the domain of that rule is, in words, and say what its range is. Then say what the
office has done wrong if a row of its planning sheet reads n = 4.5.

**5.** Under section 3(1) of the National Food Security Act, 2013, a person in a priority household is
entitled to five kilograms of foodgrains a month.

Work out the grain for a household of three, and for a household of seven. Give each answer
with its unit. Then work out how many people are in a household counted for 45 kilograms a
month. Say which way round you ran the rule each time.

**6.** Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains a month. So a household of five is counted for 25 kilograms of
foodgrains a month.

Treat the number of months as the input and the total kilograms as the output. Write the rule,
work out the total for four months, and work out how many months it takes to reach
150 kilograms. Give every answer with its unit.

**7.** Here is a worked answer. Find the step that broke.

```working
    a register lists a household of four counted for 20 kilograms
    it lists another household of four counted for 35 kilograms
    the rule for four people is the average of the two
    20 plus 35 = 55
    55 divided by 2 = 27.5
    so four people gives 27.5 kilograms a month
```

**8.** A colleague sends you this line about a block register.

> Our register lists grain per household each month. Divide any row by five and you get the
> number of people. So we can drop the people column and save the data entry.

Decide what to compute, compute it, and say what your answer does not establish.

