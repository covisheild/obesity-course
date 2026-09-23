# Book 0 compression defects: round 2 verification (23 Sep 2026)

Task 4b, independent verifier. Checked against check/records/B0/ at commit a9bce48.

| Record | Id | Verdict |
|---|---|---|
| B0-R0-C24 | C24-R2a | closed |
| B0-R0-C25 | C25-R2a | closed |
| B0-R0-C29 | C29-R2a | closed |
| B0-R0-C36 | C36-R2a | closed |
| B0-R0-C38 | C38-R2a | open: "It is also the small store" calls the liver the small store; C36 says the small store is glycogen in the liver and the muscles |
| B0-R0-C38 | C38-R2b | closed |
| B0-R0-C40 | C40-K1 | closed (via C40-R2a) |
| B0-R0-C40 | C40-R2a | closed |
| B0-R0-C41 | C41-R2a | closed |
| B0-R0-C41 | C41-R2b | closed |
| B0-R0-C43 | C43-R2a | closed |

Open: 1 of 11.

Checks run: C25 powers of 0.75 and 1 minus 0.75 recomputed; C29 seed-110 simulation re-run (0.6330, 0.3165) and restored entries byte-identical to 64547ef^; C40 P11 arithmetic recomputed; quotes checked in nfsa_2013, openstax_intro_stats_2e, openstax_anatphys_2e (one "interstitial" occurrence only; none in openstax_biology_2e), fss_act_2006 s.92(1); C36/C38 grep: no 'near store' or 'far store' left.

Outside scope, noted only: C41 illustration says the old copy's newest named amendment is from 2003, but sources/constitution.txt also names the Ninety-third (2005) and Ninety-fourth (2006) Amendment Acts. The round-2 sentence still holds (both are before 2016). C25 P13 has a pre-existing garble: "is not covered or not covered as one draw".
