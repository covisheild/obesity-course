# S47-R1 step 5c, batch r1 (C01 to C06): restore decisions

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` sections 1, 2 and 4,
and `<S>-original.md`, `<S>-prose.yml`, `<S>-pass1-prose.yml` for S47-R1-C01 to C06. Lists are in
`restore-lists/S47-R1-Cnn.txt`, each line commented with the gap it closes. Outputs are
`S47-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. Holes are in `HOLES-r1.md`.

Key: **restored** means original sentences were put back because the reader could not do the
thing without them. **hole** means the original does not fill it either, or it is an error; it
goes to the audit. **not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 865 | 395 | 457 | +62 | 13.47 → 13.07 → 12.27 | OK |
| C02 | 768 | 387 | 442 | +55 | 11.40 → 10.35 → 10.95 | OK |
| C03 | 922 | 442 | 490 | +48 | 14.41 → 14.26 → 14.41 | OK |
| C04 | 803 | 403 | 459 | +56 | 14.34 → 13.90 → 14.34 | OK |
| C05 | 963 | 428 | 562 | +134 | 15.05 → 13.81 → 14.79 | OK |
| C06 | 1027 | 367 | 523 | +156 | 14.88 → 13.11 → 14.53 | OK |
| **Total** | 5348 | 2422 | 2933 | +511 | | 6 OK |

C03 and C04 first failed validation (mean sentence rose to 15.42 and 14.73). Restorations were
dropped, least necessary first, until each passed; the dropped ones are noted below.

**Placeholder corruption in the cut (for the conductor).** `S47-R1-C06-pass1-prose.yml` carries
`{{n:plcpcommentdays}}` (underscores lost), an unknown key the build would block on. The final
file is rebuilt from the original and carries `{{n:plcp_comment_days}}`, so the final is clean.
Any other use of the pass-1 file for C06 should not be trusted on this point.

`python check/build.py --check` / `--subject S47-R1` was not run: it needs the final text written
back into the records, which is outside this brief.

## Gap by gap

### C01
- **C01-1** hole: the original also names no textbook for the four-stage model or the quoted definition.
- **C01-2** restored: "Textbooks draw the life of a policy as four stages." / "A problem gets onto the agenda ..." / "A body decides on one." / "Offices carry it out." / "Someone checks whether it worked." These give enactment = a body decides, so Ex4(2) can be placed.
- **C01-3** restored: "Real decisions skip stages, go back, and happen out of order." This is the reason the reader asked for.
- **C01-4** hole: the original does not say whose release it is, explain the date gap, or define "Cabinet" before C05.
- **C01-5** restored: "Policy is also what offices actually do, and that can differ from what the document says." This defines text versus practice in the bullet itself.
- **C01-6** hole: "collector" and "block" are undefined in the original too, and Ex2(1) and (4) turn on them.
- **C01-7** hole: the original also leaves "government", "a public body" and "an agency" undistinguished.
- **C01-8** not a defect: the passage is labelled "A made-up report", and the exercise asks only for the stage.
- **C01-9** hole: the original says only "Choosing not to act is a policy too". The step to "asked and has not acted" is not shown.

### C02
- **C02-1** hole: the verbless "headings" are in the original too. The reader parsed them, but the fixer should make them sentences.
- **C02-2** restored in part: "Public procurement agencies buy wheat and paddy at MSP." This makes paddy an MSP crop for Ex4. "Kharif" and "marketing season" stay undefined: hole.
- **C02-3** hole. The original names no power for the CCEA, which breaks the section's own rule. C05's restored "Standing Committees of the Cabinet may decide matters referred to them ... (rule 6)" ties a Cabinet committee to the Cabinet. It does not name the CCEA's power in C02.
- **C02-4** hole: the original never says which office acts as "the Central Government". Section 2(a) of the gap report hits the same wall.
- **C02-5** hole: "previous publication" is not explained in the original C02 either, and Ex2 needs it.
- **C02-6** restored: "The State Government appoints a Commissioner of Food Safety for efficient implementation (section 30(1)), and there is a Designated Officer for each district (section 36(2))." This gives the provisions, and Ex3's source for the assignment.
- **C02-7** hole: the original gives no section for the Central Advisory Committee.
- **C02-8** restored: "Under Articles 32 and 226 of the Constitution, the Supreme Court and the High Courts may issue directions, orders or writs." This is the power behind "A court can direct a body to act."
- **C02-9** not a defect: the illustration of the trap is in the first Must-know bullet (CACP recommends, CCEA approves).
- **§1 C02 Ex2** (step order, which clause covers what) not a defect: Ex2 asks the reader to say what the sentence does not tell them. These are that answer.

### C03
- **C03-1** not a defect: the first source is the Constitution-down chain, given in the first paragraph, and the reader found it.
- **C03-2** hole: the original does not expand "G.S.R.", "(E)" or "(22 of 2023)" either.
- **C03-3** restored: "Near the start they say "in exercise of the powers conferred by" and name a section." This closes the dangling "Most notifications tell you their own rung."
- **C03-4** restored: "The proviso to article 73 says it cannot, unless the Constitution or an Act of Parliament expressly provides for it." This removes the apparent contradiction with Article 73. The longer Definition sentence ("On a matter where both may legislate ...") was tried and dropped because it raised the mean sentence length.
- **C03-5** not a defect: the reader's inference ("the power may have conditions or limits") is right, and nothing was blocked. The original's "The chain tells you that a body claims a power ..." was tried and dropped because of the mean.
- **C03-6** hole: the original never says which sections came in at which stage, or whether the DPDP Act covers school health apps, so Ex3's correction cannot be written. "... much of it was still not in force in October 2026" (Must-know) was tried and dropped because of the mean. It would not have named the sections anyway.
- **C03-7** hole: "third proposal" is in the original too, and no list of the department's proposals is given.
- **C03-8** restored: "The words are "has power to make laws", not "has made laws"." This shows executive power rests on Article 73/162, not on an existing Act.

### C04
- **C04-1** hole: the floating "As of 2 October 2026 ..." line is in the original too.
- **C04-2** restored: "Union List entry 52 covers industries whose control by the Union Parliament has declared by law to be expedient in the public interest." / "Section 2 of the Food Safety and Standards Act, 2006 makes that declaration for the food industry." This gives the mechanism, and section 2's content for Ex2.
- **C04-3** restored in part: "Concurrent List entry 25 is education, subject to entries 63 to 66 of the Union List." This is the school entry for Ex2, and section 2 comes in via C04-2. No Eleventh or Twelfth Schedule entry is given in the original: hole.
- **C04-4** hole: the original names no State Act for Chhattisgarh.
- **C04-5** hole (error): Ex4's premise ("why can't we") is not supported by the original either.
- **C04-6** hole: the "33(b)" / "33" switch is in the original too.
- **C04-7** hole. The original's "Under Article 254(2) a State law that was reserved for the President ..." would link to Article 200. It was tried and dropped because it raised the mean sentence length. The fixer should reword "sent" as "reserved".

### C05
- **C05-1** hole: the original also calls the two orders "rules", and they sit under Article 77(3) with no Act. That bends C03's ladder without comment.
- **C05-2** restored: "The rules stand as amended up to Amendment Series no. 386 of 22 July 2026." This shows what an amendment series is.
- **C05-3** restored: "Under rule 7, the cases in the Second Schedule go before the Cabinet." / "They include cases involving legislation, ..." This makes clear it is the Transaction of Business Rules' Second Schedule.
- **C05-4** restored in part: "The Goods and Services Tax Council and the Central Goods and Services Tax Act are with the Department of Revenue (items 18A and 21(a))." This gives the item. The Revenue-to-Ministry-of-Finance link is absent from the original: hole.
- **C05-5** restored: "Its Department of Food and Public Distribution has the public distribution system, grain, sugar and food prices." This names the wrong addressee.
- **C05-6** hole: the original does not separate "packaged commodities" from food labelling.
- **C05-7** restored: "Aerated water and soft drinks, and industries such as biscuits, confectionery and ready-to-eat foods, are with the Ministry of Food Processing Industries (items 6 and 2)."
- **C05-8** not a defect: the reader marked it minor, and nothing was blocked. The Cabinet-committee link it raises is covered by the rule 6 restoration, made for C02-3: "Standing Committees of the Cabinet may decide matters referred to them, and the Cabinet may review their decisions (rule 6)."
- **§1 C05 Ex2** (who has power, the State's role) not a defect: Ex2 asks what the lookup does not tell, and the Must-know states that the rules give no power.
- **§2(b) Chhattisgarh business rules not given** not a defect: the text tells the reader to open them (Article 166(3)).

### C06
- **C06-1** restored: "The Transaction of Business Rules require the Ministry of Law to be consulted on proposals for legislation (rule 4(3)(a)), and send cases involving legislation to the Cabinet (Second Schedule, entry (a))." These are steps two and three.
- **C06-2** restored: "In Parliament, a Bill may start in either House, unless it is a Money Bill (Article 107(1))." / "It is introduced on a motion for leave, the first reading, and published in the Gazette." These give "It may be referred" its antecedent. What a Department-related Standing Committee is remains unexplained: folded into C06-6.
- **C06-3** not a defect: an unfilled placeholder. `plcp_comment_days` = "thirty" (numbers.yml). Both "spellings" are one key, and the cut's corrupted copy is not in the final.
- **C06-4** restored: "It cannot be introduced in the Rajya Sabha (the Council of States)." / "The Rajya Sabha may only recommend amendments, within fourteen days, which the Lok Sabha (the House of the People) may accept or reject (Article 109)." These name the two Houses. "PRS Legislative Research" and "term" stay unexplained: minor hole.
- **C06-5** restored: "A Money Bill is a Bill that contains only provisions on the matters in Article 110(1) ..." / "The Speaker of the Lok Sabha decides whether a Bill is a Money Bill (Article 110(3))."
- **C06-6** hole: the original names no document providing for committee referral or evidence-taking.
- **C06-7** restored: "Your evidence can enter at two sourced points." This is the antecedent of "One is".
- **C06-8** hole: "Governor" and "Committee of Secretaries" are unexplained in the original too.

## Counts
Restored 21 (three of them in part, with the remainder a hole), hole 22, not a defect 9.
