### A7 · Logarithms — what they are for before how they work

*B0-R0-C07 · derivable*

**Definition.** The logarithm of a number to base ten is the power to which ten must be raised to produce that
number. Since 10^3 is one thousand, the logarithm of one thousand is three.

A logarithm therefore answers one question: how many powers of ten is this? It is defined only
for numbers above zero, because no power of ten produces zero or a negative number. The
logarithm of one is zero.

Because multiplying powers of ten adds their exponents, the logarithm of a product is the sum of
the logarithms. A logarithm converts multiplication into addition.

On an axis marked in logarithms, equal distances represent equal multiplications rather than
equal additions. The step from one to ten and the step from one hundred to one thousand occupy
the same distance, and they differ by nine and by nine hundred.

**In plain terms.** Start with what a logarithm is for, because the name puts people off a thing they already half
know.

You have a pile of numbers and they are wildly different sizes. Twenty-five thousand. Three lakh.
Ten lakh. Put them on an ordinary scale and the small ones vanish into the left edge.

So ask a different question of each number. Not how big is it, but how many powers of ten is it?
That question has a short answer, and the short answer is the logarithm.

Ten is 10^1, so its logarithm is 1. A hundred is 10^2, so its logarithm is 2. A thousand is 10^3,
so its logarithm is 3. That is the whole definition: the logarithm is the exponent.

Numbers in between get an answer in between. Five hundred sits between a hundred and a thousand,
so its logarithm sits between 2 and 3. A calculator will tell you it is about 2.7. You do not have
to work that out by hand, and you will not be asked to.

Two things follow, and they are why logarithms are everywhere.

The first is that multiplying turns into adding. A hundred times a thousand is 10^2 times 10^3,
which is 10^5. In logarithms that is 2 plus 3 equals 5.

The second matters more for reading other people's work. Put logarithms on the side of a graph
and equal distances up the page stop meaning equal amounts. They mean equal multiples. One step
is ten times, whether you are stepping from 1 to 10 or from 100 to 1,000. A gap that looks small
on that page can be a factor of a hundred.

**Illustration.** Here is a figure of a kind you will meet constantly. Picture the side of the graph marked like
this, bottom to top.

```
    1     10     100     1,000     10,000
```

The marks are evenly spaced up the page. Somebody looks at it and says this.

> The rise from 100 to 1,000 is the same size as the rise from 1 to 10. You can see it — the
> gaps are equal.

Do the subtraction yourself and watch the claim fall apart.

```
    10 minus 1 = 9
    1,000 minus 100 = 900
```

Nine against nine hundred. The gaps on the page are equal and the amounts are a hundred times
apart.

So what is equal? Do the division instead of the subtraction.

```
    10 divided by 1 = 10
    1,000 divided by 100 = 10
```

Both steps multiply by ten. That is what the axis was built to show, and the person reading it
took equal distance to mean equal amount. Every axis like this one is waiting to catch somebody
the same way.

Now build one for yourself out of real numbers, so you can see why anyone would want it.

Open `sources/fss_act_2006.txt`, the file you opened in section A1, and search inside it for
"twenty-five thousand". One hit this time, in the proviso to section 50: a penalty not exceeding twenty-five thousand rupees for small food
businesses.

For the other three, search the section headings rather than the money. "Three lakh" alone
returns four hits in this Act and only one of them is the section you want. So search for
"Penalty for misbranded food", then "Penalty for sub-standard food", then "Penalty for
misleading advertisement". Each returns the contents list first and the section itself second,
as it did in section A1.

Write the four down and turn each into a power of ten. Use a calculator for the logarithm
column; that is what it is for.

```
    25,000      2.5 times 10^4      logarithm 4.4
    3,00,000    3 times 10^5        logarithm 5.5
    5,00,000    5 times 10^5        logarithm 5.7
    10,00,000   1 times 10^6        logarithm 6.0
```

Look at the last column. The four you wrote down run from 4.4 to 6.0. That is a span of 1.6, and
1.6 powers of ten is a factor of about forty.

Say that out loud, because it is the sentence the logarithms bought you. The heaviest of your
four is about forty times the lightest. On a plain scale the twenty-five thousand would have
been a line you could not see. On a logarithmic one, all four fit and the spacing between them
is readable.

These four are not every penalty in the Act, and you picked them. Say so if you show anybody the
figure.

Last, the multiplying rule, because it is one line and it explains the rest.

```
    100 times 1,000 = 1,00,000
    logarithm 2 plus logarithm 3 = 5
    and 10^5 is indeed 1,00,000
```

Adding the logarithms did the multiplying. Before calculators that was the entire point of
them. It is no longer why anybody computes one, and it is still why the axis behaves as it does.

**Where this picture breaks.** A logarithmic axis makes very different numbers fit on one page, and it does that by squashing
the differences between the large ones. That is a real loss, not just a matter of how it looks.
A tenfold rise and a hundredfold rise look similar on the page. If the size of the effect is
what you are arguing about, this axis is working against you.

It also cannot show zero, and it cannot show anything below it. No power of ten gives zero, so
zero is not on the axis at any position, however far down you go. A figure with a log axis has
therefore silently dropped every zero in the data, and nothing on the page says so.

And watch for the axis that is not what it looks like. An Indian chart may be labelled in lakh:
1 lakh, 2 lakh, 3 lakh. Those steps are equal additions, so it is an ordinary scale wearing
unfamiliar labels. Another may be labelled 1 lakh, 10 lakh, 1 crore, which is equal
multiplication and a log scale. The labels look similar at a glance. Read the steps, not the
words.

One thing about the four figures, as in section A1. They are what this copy of the Act says, and
it names no change to the Act after 2008. A later section of this book teaches you how to check
that for yourself.

**Must know points for you.**

- On a logarithmic axis equal distances are equal multiples, not equal amounts. Reading them as amounts is the standard mistake, and it is made by people who are confident about the figure because they can see it.

- Before reading any figure, look at the axis and decide which kind it is. If the marks go 1, 10, 100, 1,000 the steps are multiplications. If they go 1, 2, 3 they are additions. Everything you then say about the shape of the line depends on which answer you got.

- A logarithmic axis cannot show zero or anything below it, because no power of ten produces them. So a figure on that axis has dropped every zero in the underlying data and says nothing about it. Ask what happened to those observations.

- A log axis makes a large difference look modest. If you are arguing about the size of an effect rather than its presence, that axis is working against you. The same is true when somebody else chose it. Say which axis you are reading from before you quote a figure in public.

- Indian charts are often labelled in lakh or crore, and the labels do not tell you the axis. Steps of one lakh, two lakh, three lakh are an ordinary scale. Steps of one lakh, ten lakh, one crore are a log scale. Read the steps rather than the words.

- Asked in a viva what the logarithm of one is, the answer is zero, because ten to the power zero is one. The question is asked because a candidate who has learnt the button and not the idea will guess one. They will then be unable to say why.

- You will not be asked to compute a logarithm by hand and there is no reason to learn how. What you must be able to do is say what one means and read an axis built from them. And notice when a figure has been drawn on one without saying so.


**Exercise B0-R0-C07-E1** (interpretation). A figure has a vertical axis marked 1, 10, 100, 1,000, 10,000, with the marks evenly spaced. A
line climbs steadily across it, at a constant angle, from the bottom left to the top right. Say
what a straight line on this figure means about the quantity, and say what the same data would
look like on an ordinary scale.

*Record your confidence as a percentage before turning to the answer.*

**Exercise B0-R0-C07-E2** (calculation). Take the four penalty ceilings from the Food Safety and Standards Act, 2006 in the worked
example. Say how many times larger the largest is than the smallest, first by dividing and then
by subtracting the logarithms. Then say what the logarithm of ten crore would be.

**Practice.** Ten problems on this technique, easiest first. Work them on paper. The answers are in the appendix at the back, under these numbers.

**B0-R0-C07-P01.** Give the logarithm to base ten of each of these, without a calculator.

```
    100      10,000      1      10^9
```

**B0-R0-C07-P02.** Each of these logarithms belongs to a number. Say which number.

```
    3      6      0      -2
```

**B0-R0-C07-P03.** Without a calculator, say between which two whole numbers the logarithm of 4,800 lies. Then say
which of the two it is closer to, and why.

**B0-R0-C07-P04.** Section 21(2) of the Consumer Protection Act, 2019 caps a penalty at ten lakh rupees. Sections
34 and 47 cap District and State Commission complaints at one crore and ten crore. Give the
logarithm of each figure.

**B0-R0-C07-P05.** Take the four penalty figures from the Food Safety and Standards Act, 2006: 25,000, 3,00,000,
5,00,000 and 10,00,000. Using a calculator for the logarithms, say how many times larger the
three lakh figure is than the twenty-five thousand one, by subtracting logarithms.

**B0-R0-C07-P06.** A figure has a vertical axis marked 100, 1,000, 10,000 and 1,00,000, evenly spaced. Two points
sit on it: one at 300 and one at 30,000. Say how far apart they are in logarithms, and how many
times larger one value is than the other.

**B0-R0-C07-P07.** Here is a worked answer. Find the step that broke.

```
    logarithm of 200 = 2.3
    logarithm of 300 = 2.5
    2.3 plus 2.5 = 4.8
    so 200 plus 300 = 10^4.8 = about 63,000
```

**B0-R0-C07-P08.** Here is a claim about a figure whose vertical axis runs 1, 10, 100, 1,000 in evenly spaced
marks.

> The line rose one mark between 2015 and 2020, and one mark again between 2020 and 2025, so
> the increase was steady.

Find what is wrong with the word "steady".

**B0-R0-C07-P09.** Here is a caption under a figure in a report.

> Values below the axis minimum are not shown. The vertical axis is logarithmic.

Decide what to work out about the data, and say what the figure cannot establish.

**B0-R0-C07-P10.** A colleague shows you two charts of the same data and asks which to use in a briefing. One has
an ordinary vertical axis, the other a logarithmic one. On the log chart the rise looks modest;
on the ordinary one it looks dramatic. Decide what to work out, and say what your answer does
not settle.
