# A6 · Powers, roots and scientific notation

**Definition.** A power is repeated multiplication of one number by itself. The number being multiplied is the
base and the small raised number is the exponent, which counts how many copies of the base are
multiplied together.

A negative exponent means repeated division by the base rather than repeated multiplication, so
10^-3 is one thousandth. Any base raised to the power zero is one.

Multiplying two powers of the same base adds their exponents, and dividing subtracts them.

A root is the inverse of a power. The square root of a quantity is the number which, multiplied
by itself, yields that quantity. Equivalently it is that quantity raised to the exponent one
half, which is the case that shows an exponent need not be a whole number.

Scientific notation writes a quantity as a number between one and ten multiplied by a power of
ten.

**In plain terms.** Ten to the power three is written 10^3. The ten is the base. The small raised three is the
exponent, and all it does is count how many tens are being multiplied. Ten to the power three is
one thousand.

A quick way to read any power of ten: the exponent is the number of zeros.

A minus sign in the exponent flips it from multiplying to dividing. So 10^-3 is one divided by a
thousand, which is 0.001.

Multiply two powers of ten and you add the exponents. Divide, and you subtract them.

Squaring a number means multiplying it by itself. Three squared is nine.

A square root runs that backwards. The square root of nine is three, because three times three is
nine. Ask it as a question. What number, multiplied by itself, gives me this one?

Some roots come out whole. The square root of 144 is 12. Most do not. The square root of two
starts 1.414 and never stops. Take what the calculator gives you and round it the way the section
on rounding told you to.

There is a second way to write a root, and you need it further on. An exponent of one half means
the square root. So 9^(1/2) is 3, the same answer, written in the language of powers.

That is worth a pause, because it breaks the rule you started with. An exponent does not have to
count copies. Once one half is allowed, so is 1.6, and 10^1.6 is an ordinary number the
calculator gives as about 40. Logarithms, two sections on, are built on exactly that.

Write a quantity as a number between one and ten, times a power of ten. Thirty-five thousand
becomes 3.5 times 10^4.

**Illustration.** Build the ladder of powers of ten yourself, in two columns, with the Indian names on one side
and the international names on the other.

```table
    | power | written out | Indian name | international name |
    | 10^1 | 10 | | |
    | 10^2 | 100 | | |
    | 10^3 | 1,000 | thousand | thousand |
    | 10^4 | 10,000 | | |
    | 10^5 | 1,00,000 | one lakh | |
    | 10^6 | 10,00,000 | | one million |
    | 10^7 | 1,00,00,000 | one crore | |
    | 10^8 | 10,00,00,000 | ten crore | |
    | 10^9 | 1,00,00,00,000 | | one billion |
```

Read the gaps. A lakh is 10^5 and a crore is 10^7, so the Indian ladder steps by two powers of
ten. A million is 10^6 and a billion is 10^9, so the international ladder steps by three.

Now the failure, and it is one of the commonest in real work. A spreadsheet has a column of
grain tonnages in it. The column is narrow, so the spreadsheet prints one cell like this.

```working
    1.5E+06
```

Somebody copies the visible part into a report and writes 1.5 tonnes.

Read what the cell actually said. That E means "times ten to the power", so the cell held 1.5
times 10^6 tonnes.

```working
    1.5 times 10^6
    = 1.5 times 1,000,000
    = 1,500,000
```

Take a lakh and multiply it by a hundred.

```working
    1,00,000 times 100
    = 10^5 times 10^2
    = 10^(5 plus 2)
    = 10^7
    = 1,00,00,000, which is one crore
```

Try the other direction. Divide a crore by a lakh.

```working
    10^7 divided by 10^5
    = 10^(7 minus 5)
    = 10^2
    = 100
```

A crore is a hundred lakh.

**Where this picture breaks.** "The exponent is the number of zeros" is a rule about powers of ten and nothing else. Two to the
power three is eight, and there is no zero anywhere in it.

**Must know points for you.**

- A negative exponent does not make a number negative. It makes it small. Ten to the power minus three is one thousandth, an ordinary positive quantity.
- Whenever a number contains an E, or a small raised number, write it out in full before you use it.
- The Indian ladder steps by two powers of ten: lakh is 10^5 and crore is 10^7. The international ladder steps by three: million is 10^6 and billion is 10^9.
- Write any large figure as a digit or two times a power of ten before you compare it with another.
- Asked to check a colleague's calculation quickly, check the exponents first and the digits second.
- The square root of a sum is not the sum of the square roots. Work out what sits under the root first, then take the root of that one number.
- An exponent does not have to be a whole number. One half means the square root, and a value in between is an ordinary number the calculator will give you.

**Exercise 1** (calculation). Write each of these as a number between one and ten times a power of ten. The list: one lakh,
thirty-five thousand, ten lakh, one crore, one thousandth. Then work out, using the exponent
rules alone, how many lakh there are in a crore and how many thousand there are in a million.

**Exercise 2** (critique). Here is a colleague's note.

> Daily production is 2.4E+05 units, which is about 2.4 lakh. So annual production is roughly
> 8.8E+07, or about 8.8 crore.

Check every step. Say which are right and which are not.

**Exercise 3** (calculation). A square plot of land covers 2,025 square metres. Work out the length of one side.

Then do the same for a second square plot covering 2,000 square metres. Say how many digits of
that answer you would be willing to write down.

**1.** Write each of these out as an ordinary number.

```working
    10^2      10^5      10^0      10^-2      9^(1/2)      144^(1/2)
```

**2.** Work these out using the exponent rules alone, without writing the numbers in full.

```working
    10^4 times 10^3        10^8 divided by 10^5        10^3 times 10^-1
```

**3.** Write each of these in scientific notation, as a number between one and ten times a power of
ten.

```working
    6,200      93,00,000      0.0047      1,00,00,000
```

**4.** Section 34(1) of the Consumer Protection Act, 2019 caps District Commission complaints at one
crore rupees. Section 47 caps State Commission ones at ten crore. Write both in scientific
notation and say, from the exponents alone, how many times larger the second is.

**5.** A district serves 1.8 times 10^5 meals in a year. The second schedule of the National Food
Security Act, 2013 sets each meal at 450 calories. Work out the total calories in scientific
notation, showing the exponent step.

**6.** A square plot covers 8.0 times 10^5 square metres. Write the area out in full, then work out
the length of one side. Give the side to the number of digits the area gives you, and check
your rounded answer by multiplying it back.

**7.** A value is given as 2.5E+04 in a spreadsheet cell and another as 3.0E-02. Write both out in
full, then multiply them and give the answer in scientific notation.

**8.** Here is a worked answer. Find the step that broke.

```working
    10^6 times 10^3
    = 10^(6 times 3)
    = 10^18
```

**9.** Here is a worked answer. Find the step that broke.

```working
    two square plots are to be replaced by one square plot of the same total area
    the first covers 900 square metres and the second 1,600 square metres
    900^(1/2) = 30 and 1,600^(1/2) = 40
    so the new plot has a side of 30 plus 40 = 70 metres
```

**10.** Here is a worked answer. Find the step that broke.

```working
    a concentration is 5 times 10^-3
    a second is 2 times 10^-6
    10^-3 is smaller than 10^-6 because -3 is greater than -6
    so the first is the smaller concentration
```

**11.** Here is a line from a note.

> Annual production is 1.2E+06 tonnes, so at 3 lakh tonnes a quarter the plant is running
> close to capacity.

Decide what to compute, compute it, and say what your answer does not establish.

**12.** In a meeting somebody says this.

> We reach 2 crore people, so a rupee a head is only 2 lakh rupees.

Decide what to compute, compute it, and say what your answer does not establish.

