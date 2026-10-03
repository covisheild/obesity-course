# S58-R1 intake, group C1 (figure-design guidance: Rougier 2014, Wilke 2019, Bergstrom and West): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Citekeys were
grepped in `sources/INDEX.yml` and `check/references/library.bib` on 2026-10-02 at the start and again just
before finishing: none exists. Eighteen files: Rougier 2014 (1), Bergstrom and West (1), Wilke's
fifteen chapters named in READY.md (one file and one citekey per chapter), and Wilke's Preface (1,
not in READY.md; added because it bears on C20's tool choice). Log: `books/S58-R1/intake/log-C1.md`.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  rougier_2014_ten_rules_figures:
    file: rougier_2014_ten_rules_figures.txt
    what: >-
      Rougier, Droettboom and Bourne, PLoS Comput Biol 2014;10:e1003833 (PMC4161295; CC0 public domain), publisher
      article page. Whole text: licence, introduction, Rules 1-10, Figure 1-8 captions, Notes; figure titles from the
      PMC XML. References and the figures themselves NOT held
  bergstrom_west_2016_proportional_ink:
    file: bergstrom_west_2016_proportional_ink.txt
    what: >-
      Bergstrom and West, "The principle of proportional ink", Calling Bullshit website, Tools (no licence stated;
      "Copyright © Calling Bullshit 2017-2019"). Whole article (bar charts, line graphs, bubble, donut, changing
      denominator, 3D, perspective, pie, conclusion) and the site footer. Example charts (images) NOT held
  wilke_2019_dataviz_preface:
    file: wilke_2019_dataviz_preface.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), the Preface, whole, with the welcome page's licence statement
  wilke_2019_dataviz_ch03:
    file: wilke_2019_dataviz_ch03.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 3 "Coordinate systems and axes": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch04:
    file: wilke_2019_dataviz_ch04.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 4 "Color scales": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch05:
    file: wilke_2019_dataviz_ch05.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 5 "Directory of visualizations": whole chapter text, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch07:
    file: wilke_2019_dataviz_ch07.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 7 "Visualizing distributions: Histograms and density plots": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch09:
    file: wilke_2019_dataviz_ch09.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 9 "Visualizing many distributions at once": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch17:
    file: wilke_2019_dataviz_ch17.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 17 "The principle of proportional ink": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch19:
    file: wilke_2019_dataviz_ch19.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 19 "Common pitfalls of color use": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch20:
    file: wilke_2019_dataviz_ch20.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 20 "Redundant coding": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch22:
    file: wilke_2019_dataviz_ch22.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 22 "Titles, captions, and tables": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch23:
    file: wilke_2019_dataviz_ch23.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 23 "Balance the data and the context": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch24:
    file: wilke_2019_dataviz_ch24.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 24 "Use larger axis labels": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch26:
    file: wilke_2019_dataviz_ch26.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 26 "Don’t go 3D": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch27:
    file: wilke_2019_dataviz_ch27.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 27 "Understanding the most commonly used image file formats": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch28:
    file: wilke_2019_dataviz_ch28.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 28 "Choosing the right visualization software": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
  wilke_2019_dataviz_ch29:
    file: wilke_2019_dataviz_ch29.txt
    what: >-
      Wilke, Fundamentals of Data Visualization (author's manuscript online; CC BY-NC-ND 4.0, verbatim, not
      adapted), chapter 29 "Telling a story and making a point": whole chapter text and all figure captions, with the welcome page's licence
      statement. Reference list and figures (images) NOT held
```

## 2. `check/references/library.bib` (append)

```bibtex
@article{rougier_2014_ten_rules_figures,
  title        = {Ten simple rules for better figures},
  author       = {Rougier, Nicolas P and Droettboom, Michael and Bourne, Philip E},
  journal      = {PLoS Computational Biology},
  year         = {2014},
  volume       = {10},
  number       = {9},
  pages        = {e1003833},
  doi          = {10.1371/journal.pcbi.1003833},
  note         = {PMID 25210732, PMC4161295. Public domain (Creative Commons CC0 public domain
                  dedication, stated on the article page). Published 11 September 2014. Quoted from
                  the article page; figure titles from the PMC XML},
  url          = {https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833},
  urldate      = {2026-10-02}
}

@misc{bergstrom_west_2016_proportional_ink,
  title        = {The principle of proportional ink},
  author       = {Bergstrom, Carl T and West, Jevin},
  year         = {2016},
  howpublished = {Calling Bullshit (course website), Tools},
  note         = {No licence stated; the site footer reads "Copyright (c) Calling Bullshit 2017-2019".
                  The page carries no byline or date: authors from the site footer, year as cited by
                  Wilke, Fundamentals of Data Visualization, ch. 17. Quoted from the web page},
  url          = {https://callingbullshit.org/tools/tools_proportional_ink.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_preface,
  title        = {Preface},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. The whole Preface quoted},
  url          = {https://clauswilke.com/dataviz/preface.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch03,
  title        = {Chapter 3: Coordinate systems and axes},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/coordinate-systems-axes.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch04,
  title        = {Chapter 4: Color scales},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/color-basics.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch05,
  title        = {Chapter 5: Directory of visualizations},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted},
  url          = {https://clauswilke.com/dataviz/directory-of-visualizations.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch07,
  title        = {Chapter 7: Visualizing distributions: Histograms and density plots},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/histograms-density-plots.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch09,
  title        = {Chapter 9: Visualizing many distributions at once},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/boxplots-violins.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch17,
  title        = {Chapter 17: The principle of proportional ink},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/proportional-ink.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch19,
  title        = {Chapter 19: Common pitfalls of color use},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/color-pitfalls.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch20,
  title        = {Chapter 20: Redundant coding},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/redundant-coding.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch22,
  title        = {Chapter 22: Titles, captions, and tables},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/figure-titles-captions.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch23,
  title        = {Chapter 23: Balance the data and the context},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/balance-data-context.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch24,
  title        = {Chapter 24: Use larger axis labels},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/small-axis-labels.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch26,
  title        = {Chapter 26: Don’t go 3D},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/no-3d.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch27,
  title        = {Chapter 27: Understanding the most commonly used image file formats},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/image-file-formats.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch28,
  title        = {Chapter 28: Choosing the right visualization software},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/choosing-visualization-software.html},
  urldate      = {2026-10-02}
}

@incollection{wilke_2019_dataviz_ch29,
  title        = {Chapter 29: Telling a story and making a point},
  author       = {Wilke, Claus O},
  booktitle    = {Fundamentals of Data Visualization},
  publisher    = {O'Reilly Media},
  year         = {2019},
  note         = {Licensed CC BY-NC-ND 4.0 (stated on the book website's welcome page); quoted
                  verbatim, not adapted. Quoted from the author's manuscript on the book website,
                  which it describes as "before final copy-editing"; the year is the print
                  edition's and is not stated on the website. Chapter text quoted with its figure captions},
  url          = {https://clauswilke.com/dataviz/telling-a-story.html},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md` (new section)

```markdown
## Added by the S58-R1 source intake, group C1 (figure design: Rougier, Wilke, Bergstrom and West), 2026-10-02

Every passage was cut by script from the raw text the TinyFish `fetch_content` tool returned
(taken from the tool's own result, not retyped) and re-checked as a whitespace-normalised
substring of that fetch: **57 of 57**. Log in `books/S58-R1/intake/log-C1.md`. Wilke's book is
CC BY-NC-ND 4.0: each Wilke file is a verbatim excerpt held for study and attributed quotation,
never edited or adapted, and its header says so. Bergstrom and West's page states no licence.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `rougier_2014_ten_rules_figures.txt` | Rougier, Droettboom and Bourne, *PLoS Comput Biol* 2014;10:e1003833 (PMC4161295), publisher article page. CC0 public domain. Whole text; no references | 4,928 | Rules 1-10 in full: know your audience; identify your message; adapt to the support medium; "Captions Are Not Optional"; do not trust the defaults; colour (sequential, diverging, qualitative colormaps); do not mislead (Figure 6 caption: values 30, 20, 15, 10 as disc area and radius); "Chartjunk refers to all the unnecessary or confusing visual elements found in a figure that do not improve the message (in the best case) or add confusion (in the worst case)."; message trumps beauty; tools. Figure 1-8 titles from the PMC XML; the Figure 3 caption's inline maths is lost |
| `bergstrom_west_2016_proportional_ink.txt` | Bergstrom and West, "The principle of proportional ink", Calling Bullshit website. No licence stated ("Copyright © Calling Bullshit 2017-2019"); no byline or date on the page. Whole article | 3,821 | The rule: "when a shaded region is used to represent a numerical value, the area of that shaded region should be directly proportional to the corresponding value"; Tennessee jobs bar chart: 2014 "approximately 1.08 times" 2010 but "approximately 2.7 times as much ink"; line graphs need not include zero; filled line chart cut at 28%; bubble radius vs area (26% vs 13%, "one fourth the area"); donut bars; changing denominator; 3D bars and perspective; 3D pie (Android "70% of the pixels") |
| `wilke_2019_dataviz_preface.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0), Preface, whole | 2,449 | "the moment you manually edit a figure, your final figure becomes irreproducible"; "Excel is an interactive plot program as well and is not recommended for figure preparation (or data analysis)" (bears on C20) |
| `wilke_2019_dataviz_ch03.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 3 *Coordinate systems and axes*. Whole chapter text and figure captions; no references | 3,830 | 3.1 Cartesian coordinates (units, aspect ratio), 3.2 nonlinear axes (log and square-root scales), 3.3 curved axes (polar, map projections). "ratios should generally be shown on a log scale"; Figure 3.4 caption: the axis title on a log scale is "the name of the variable shown, not the logarithm of that variable"; Figure 3.6 caption: "ratios should not be displayed on a linear scale" |
| `wilke_2019_dataviz_ch04.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 4 *Color scales*. Whole chapter text and figure captions; no references | 2,262 | 4.1 color to distinguish (qualitative scales), 4.2 color to represent data values (sequential, diverging), 4.3 color to highlight (accent scales). The three use cases: "(i) we can use color to distinguish groups of data from each other; (ii) we can use color to represent data values; and (iii) we can use color to highlight" |
| `wilke_2019_dataviz_ch05.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 5 *Directory of visualizations*. Whole chapter text; no references | 1,833 | 5.1 amounts, 5.2 distributions, 5.3 proportions, 5.4 x-y relationships, 5.5 geospatial data, 5.6 uncertainty. The mark-to-data-shape directory; for amounts, "instead of using bars, we can also place dots at the location where the corresponding bar would end". The chapter's figures have no captions |
| `wilke_2019_dataviz_ch07.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 7 *Visualizing distributions: Histograms and density plots*. Whole chapter text and figure captions; no references | 2,714 | 7.1 a single distribution (histogram, bin width, kernel density), 7.2 multiple distributions. Histograms depend on bin width (Figure 7.2 caption); stacked and overlapping histograms labelled "bad" (Figures 7.6, 7.7) |
| `wilke_2019_dataviz_ch09.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 9 *Visualizing many distributions at once*. Whole chapter text and figure captions; no references | 2,867 | 9.1 along the vertical axis (error bars, boxplots, violins, strip charts, jitter, sina), 9.2 along the horizontal axis (ridgelines). Figure 9.1 caption: error bars of 2 SD labelled "bad" because they "are conventionally used to visualize the uncertainty of an estimate, not the variability in a population"; boxplot anatomy (median, middle 50%, 1.5 times box height fences); strip chart and jitter |
| `wilke_2019_dataviz_ch17.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 17 *The principle of proportional ink*. Whole chapter text and figure captions; no references | 3,118 | 17.1 linear axes, 17.2 logarithmic axes, 17.3 direct area visualizations. Figure 17.1 caption: axis starting at $50,000 "instead of $0" makes bar heights "not proportional to the values shown"; log-scale bars satisfy the principle "in log-transformed coordinates"; Figure 17.8 caption: bars starting at the arbitrary value 10-9 billion USD; pie wedges satisfy the principle |
| `wilke_2019_dataviz_ch19.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 19 *Common pitfalls of color use*. Whole chapter text and figure captions; no references | 3,099 | 19.1 too much or irrelevant information, 19.2 non-monotonic (rainbow) scales, 19.3 colour-vision deficiency, with Table 19.1 (Okabe-Ito palette). "Approximately 8% of males and 0.5% of females suffer from some sort of color-vision deficiency, and deuteranomaly is the most common form whereas tritanomaly is relatively rare."; Figure 19.4 caption: the rainbow scale "is highly non-monotonic", seen by "converting the colors to gray values"; Table 19.1 hex, CMYK and RGB codes |
| `wilke_2019_dataviz_ch20.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 20 *Redundant coding*. Whole chapter text and figure captions; no references | 2,624 | 20.1 legends with redundant coding (colour plus shape), 20.2 figures without legends (direct labeling). "The general strategy we can employ is called direct labeling"; Figure 20.4 caption: with point shapes "even the fully desaturated gray-scale version of the figure is legible" |
| `wilke_2019_dataviz_ch22.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 22 *Titles, captions, and tables*. Whole chapter text and figure captions; no references | 2,987 | Figure titles and captions; Axis and legend titles; Tables (unnumbered in the extraction; 22.1-22.3 in the book). The six table-layout rules (no vertical lines; no horizontal lines between data rows; text left-aligned; numbers right-aligned with the same decimal digits; single characters centred; headers aligned with their data); caption above a table, below a figure; when an axis title may be omitted (Figures 22.4-22.6) |
| `wilke_2019_dataviz_ch23.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 23 *Balance the data and the context*. Whole chapter text and figure captions; no references | 3,925 | 23.1 appropriate amount of context (non-data ink), 23.2 background grids, 23.3 paired data, 23.4 summary. "A common recommendation is to reduce the amount of non-data ink"; the idea of data and non-data ink "was popularized by Edward Tufte"; removing too much (Figure 23.3 caption) |
| `wilke_2019_dataviz_ch24.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 24 *Use larger axis labels*. Whole chapter text and figure captions; no references | 1,690 | the whole chapter (no numbered sections). "If you take away only one single lesson from this book, make it this one: Pay attention to your axis labels, axis tick labels" (opening); Figures 24.1-24.5 captions on text size and balance |
| `wilke_2019_dataviz_ch26.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 26 *Don’t go 3D*. Whole chapter text and figure captions; no references | 2,818 | 26.1 gratuitous 3D, 26.2 3D position scales, 26.3 appropriate use of 3D. "The problem with gratuitous 3D is that the projection of 3D objects into two dimensions for printing or display on a monitor distorts the data."; Figure 26.2 caption: 3D stacked bars misread (totals 322, 279 and 711) |
| `wilke_2019_dataviz_ch27.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 27 *Understanding the most commonly used image file formats*. Whole chapter text and figure captions; no references | 2,494 | 27.1 bitmap and vector graphics (Table 27.1 of formats, one cell per line as extracted), 27.2 lossless and lossy compression, 27.3 converting between formats. Vector graphics "store the geometric arrangement of individual graphical elements in the image"; Figure 27.2 caption: jpeg 432KB to 43KB minor loss, to 25KB visible artifacts |
| `wilke_2019_dataviz_ch28.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 28 *Choosing the right visualization software*. Whole chapter text and figure captions; no references | 3,366 | 28.1 reproducibility and repeatability, 28.2 data exploration versus presentation, 28.3 separation of content and design. Repeat against reproduction (Figure 28.1 caption); "consider taking careful notes on how you make each figure, so that all your work remains reproducible" |
| `wilke_2019_dataviz_ch29.txt` | Wilke, *Fundamentals of Data Visualization* (O'Reilly 2019; author's manuscript online, CC BY-NC-ND 4.0, verbatim, not adapted), ch. 29 *Telling a story and making a point*. Whole chapter text and figure captions; no references | 5,477 | 29.1 what is a story, 29.2 make a figure for the generals, 29.3 build up towards complex figures, 29.4 memorable figures, 29.5 consistent but not repetitive. "making a figure for the generals"; "Most scientists are not trained to make figures for the generals."; Figure 29.3 caption: "This figure is labeled as “bad” because it is overly complex" |
```
