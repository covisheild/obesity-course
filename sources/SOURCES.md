# What is in `sources/`, and what has been checked in it

Every file here was downloaded from India Code and read. The "verified" column lists the
provisions actually located in the text, not the provisions the file is assumed to contain.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `fss_act_2006.txt` | Food Safety and Standards Act 2006 (Act 34 of 2006), enacted 23 Aug 2006 | 24,104 | s.4 establishes FSSAI; s.23(1) packaged food must be labelled "in the manner as may be specified by regulations"; s.92 power to make regulations; s.93 regulations laid before Parliament |
| `constitution_current.txt` | Constitution of India, consolidated 2026 text (handle 123456789/618394) | 135,907 | Articles 21, 32, 47, 53, 79, 226, 245, 246, 279A |
| `constitution.txt` | **Do not cite.** An older India Code consolidation, latest amendment 2003 | 89,103 | Contains no Article 279A. Kept only because it is the worked example in Book 0 F3 |
| `nfsa_2013.txt` | National Food Security Act 2013 (Act 20 of 2013), 10 Sep 2013 | 7,679 | s.5, mid-day meal entitlement |
| `consumer_prot_2019.txt` | Consumer Protection Act 2019 (Act 35 of 2019), 9 Aug 2019 | 21,568 | Chapter III s.10, the Central Consumer Protection Authority |
| `bipm_si.txt` | BIPM's statement of the SI definition, in force from 20 May 2019 | 407 | The seven defining constants with their exact values; the relations Hz = s-1, J = kg m2 s-2 |
| `nist_sp811.txt` | NIST Guide to the SI, footnotes; page updated 18 Aug 2025 | 394 | calth = 4.184 J exactly; International Table calorie = 4.1868 J; the kilocalorie as the food-energy unit |


Drop the file in, add a row, and fill the verified column only with provisions you have found by
searching the file. An empty verified column is honest. A guessed one is the failure this whole
folder exists to prevent.

## Known missing

- FSSAI Labelling and Display Regulations 2020
- FSSAI draft amendment on front-of-pack labelling, and the comment record
- The notification capping industrial trans fat at 2%
- The Supreme Court order of 10 September 2026
- General Clauses Act 1897
- Government of India (Allocation of Business) Rules 1961

**Needs a person with a browser, and why.** Everything above that is a PDF cannot be obtained
from inside a session: PDFs fetch but yield no extractable text, so there is nothing to store and
nothing a quote can be checked against. CAPTCHA-gated hosts (NCBI Bookshelf, PubChem) and direct
downloads through the proxy fail the same way. Retrieving these is a five-minute job in a browser
and is the one step of this pipeline that still needs a human.

Blocking Book 0 Part B specifically:

| Wanted for | Source | Why it is stuck |
| --- | --- | --- |
| B4, the Indian labelling requirement | FSS (Labelling and Display) Regulations, compendium Version VIII, 09.09.2025, on fssai.gov.in | PDF, no text extraction |
| B5, mg/dL to mmol/L | A molar mass for glucose and cholesterol from IUPAC, PubChem or a clinical chemistry reference | PubChem is gated; needs an HTML or text source |

## Vintage of each copy

Added 2026-09-20 by the Book 0 Part A chat, which needed figures out of two of these files and
found that nothing in the table above records how current any copy is. The column that matters for
an institutional number is not when the Act was passed. It is what the copy in this folder says
about changes made since.

Read by searching each file for every occurrence of `by Act N of YYYY` and taking the newest.

| File | Newest change the copy itself names | What that means for a figure taken out of it |
| --- | --- | --- |
| `fss_act_2006.txt` | **Act 13 of 2008**, with effect from 7 February 2008. One amending Act, cited in three footnotes. Nothing later anywhere in the file | Every penalty figure in it is as at 2008 on the face of this copy. Quote it as what this copy says, not as the penalty in force |
| `nfsa_2013.txt` | **None.** The file carries no amendment footnote at all, so it reads as the Act as enacted in 2013 | Schedule I's prices were fixed for three years from commencement and that window closed in 2016; the file says nothing about what replaced them. Schedule II's nutritional standards carry no such clock in the text |
| `constitution_current.txt` | Consolidated 2026 text, per the row above; contains Article 279A | Usable |
| `constitution.txt` | Latest amendment 2003 | **Do not cite**, per the row above |
| `consumer_prot_2019.txt` | **None.** Checked the same way on 2026-09-20 and the file carries no amendment footnote, so it reads as the Act as enacted in 2019 | Quote s.21, s.34, s.47 and s.58 figures as what this copy says |
| `bipm_si.txt` | The 2019 revision, named on the page itself. BIPM revises the SI by CGPM resolution, so the trigger is the next CGPM | Usable. The defining constants are exact by definition and do not drift |
| `nist_sp811.txt` | Page updated 18 August 2025 | Usable. The calorie definitions are fixed conversions, not measurements |

This does not make any of these files wrong. It makes the date on them knowable, which is the whole
point of Book 0 F3, and it was not knowable from this file before.
