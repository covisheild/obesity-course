# Draft notes — batch b5 (S01-R1-C02)

**Records written:** C02 only. `quantitative: true` per INVENTORY.md; `python check/build.py
--check` gives zero blocking for the file (two issues found and fixed first: a quote crossing
Hall 2008's own `MJ/\nkg` line-wrap needed the wrap's normalised space kept in `quote`; a
level-5 practice arithmetic slip, `39500 / 4.184`, recomputed correctly as 9440.73, not the
9441.69 first written).

**Hall 2008 and Hall 2012, now held:** C02 uses Hall 2008 for the paper's own pure-fat figure
(39.5 MJ/kg), the classic rule's traced-back 87%-fat assumption, the paper's own caution that
adipose composition is "variable", the rule's 32.2 MJ/kg cross-check, and the named-only lean
mass figure (7.6 MJ/kg). Hall 2012 was not needed for this concept (it belongs to C04, C05,
C06, C09) and is not cited here.

**The one judgement call, flagged per your instruction:** Hall 2008 gives no independently
measured lipid fraction for adipose tissue — only the 87% the classic rule assumes, which the
same paper calls variable rather than confirming. So C02 does the lipid-fraction × energy-per-
gram calculation once, explicitly labelled as reproducing the rule's own assumption (cross-
checked against Hall's own "32.2 MJ per kg"), not as a measurement, and a must-know point and
two diagnostic practice problems (levels 7-8) exist specifically to stop a reader treating
7,700 kcal/kg as an established property of adipose tissue. C07's identical figure, reached via
the pound conversion, is flagged as the same assumption reappearing, not independent
confirmation — this is stated in both the definition and a must-know point, to pre-empt double-
counting across the two concepts.

**Practice set:** ten problems, one per level 1-10, reaching both ends of the ladder as
instructed. Chosen because the concept has exactly one technique (lipid fraction × energy per
gram, plus the unit conversions around it) and ten gives one clean diagnostic pair (7-8) and one
transfer pair (9-10) without padding.

**Figures used:** all real and cited — FAO FNP 77's Atwater fat factor (9.0 kcal/g, 37 kJ/g),
Hall 2008's 39.5, 17.6, 19.7 and 7.6 MJ/kg figures, Hall's own 87% and 32.2 MJ/kg, BIPM's mega
prefix, NIST's 4.184 kcal-to-kJ constant. No invented figures used at levels 4-6; bare numbers
only at levels 1-3, 7-8 (arithmetic on a made-up scenario) and 9-10 (a made-up claim built to
test the real distinction).

**Glossary rows proposed** (checked against `prose/GLOSSARY.md`; "adipose tissue" already
listed there and used in its existing sense, not re-added):
- megajoule — a million joules, a thousand kilojoules — `S01-R1-C02`
- lipid fraction — the proportion of a tissue's mass that is fat — `S01-R1-C02`
- energy density — how much energy a fixed mass of something holds — `S01-R1-C02`

**Figure wanted:** none beyond the table already in C02's illustration (pure fat, two sources;
the rule's adipose figure, flagged as an assumption; lean mass, named only).
