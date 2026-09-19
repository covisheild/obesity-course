# S48 · verification position, before any prose is written

Plan phase 1, step 5. Stated up front so the scope of what can reach released status is known before the writing starts, rather than discovered at the end.

Checked 19 September 2026.

## What is obtained and read

Four statutes, retrieved from India Code through its DSpace REST API, downloaded as text, and the specific clause located in each by search rather than assumed.

| Source | Enacted | Clause located | Handle |
| --- | --- | --- | --- |
| The Food Safety and Standards Act, 2006 | 23 Aug 2006 | s. 4 establishment of FSSAI; ss. 92–93 regulation-making power and laying before Parliament | 123456789/586348 |
| **The Constitution of India, consolidated text as in force 2026** | — | Articles 21, 32, 47, 53, 79, 226, 245, 246 and **279A** | 123456789/618394 |
| The National Food Security Act, 2013 | 10 Sep 2013 | s. 5, mid-day meal entitlement | 123456789/496105 |
| The Consumer Protection Act, 2019 | 9 Aug 2019 | Chapter III, s. 10, establishment of the CCPA | 123456789/613632 |

All fourteen clause locations above were re-confirmed by search in the retrieved files on 19 September 2026.

**Three retrieval traps, each of which would have produced a confident wrong citation.**

1. The National Food Security Act's first matching item on India Code is the **Hindi** text.
2. The Consumer Protection Act's highest-ranked item has **no attached files at all**.
3. Most seriously: the obvious Constitution item — dated 1949, handle `123456789/492360` — is a **stale consolidation**. Its most recent cited amendment is from 2003; it contains no occurrence of "279A" and none of "Goods and Services", because Article 279A was inserted by the 101st Amendment in 2016. An earlier version of this document asserted that Article 279A was present in the Constitution text already retrieved. **That assertion was wrong**, and wrong in the direction that matters: it would have supported concept C12 with a source that does not contain the provision. The correct source is the consolidated 2026 text at handle `123456789/618394`, in which Article 279A is present and located. The stale item must not be used, and the reference library records that exclusion explicitly.

The first two traps were caught by requiring an expected English phrase in the retrieved text before accepting an item. The third was caught only by searching for the specific provision before writing — the fourth of the four checking acts, and the one that catches what the first three miss.

## What these four cover

Directly or as the governing instrument: **C01–C05, C07, C08, C10, C12, C13, C14, C15, C17** — thirteen of the twenty concepts.

Two qualifications on that tally, so it is not read as stronger than it is.

- **C12 depends entirely on the corrected source.** Article 279A is in the consolidated 2026 Constitution and is absent from the 1949 item. Had the stale copy been used, C12 would have carried a citation to a document that does not contain the provision it cites.
- **C08 is only partly sourced.** Its statute-hierarchy content is verified from FSS Act ss. 92–93, but the General Clauses Act 1897, which supplies the definitions of "rule", "regulation" and "notification", has **not** been obtained. The phrase appears inside other retrieved texts, which is a mention and not a source. C08 therefore carries one verified and one outstanding reference.

## What is not obtained

| Needed for | Source | Status |
| --- | --- | --- |
| C11 labelling, C18 the live dispute, C19 trans fat | FSSAI regulations and notifications | Site reachable but is a JavaScript application with no server-rendered content and a bot-protection layer; no API found in its bundle |
| C18 the Supreme Court directions | sci.gov.in / main.sci.gov.in | 502 at the gateway, then TLS handshake timeout; granted but not responding |
| C19, C20 notification numbers and dates | e-Gazette | HTTP 500 from the server on every attempt |
| C06 allocation of business, C16 NP-NCD and PM-JAY | PIB and scheme documents | Host reachable, not yet mined |
| C09 the draft-and-comment practice | FSSAI | As above |

## What this means for the writing

Thirteen of twenty concepts can be written with a citation that has been opened and located today. Of the remaining seven, C06 and C16 are likely reachable through PIB and scheme documents and are simply not done yet; C11, C18 and C19 depend on FSSAI, and C20 partly on the Gazette.

Three concepts therefore carry real risk of being drafted without a primary source: **C11 labelling, C18 the front-of-pack dispute, C19 trans fat** — which are, uncomfortably, the three most consequential and most time-sensitive in the booklet.

The rule does not bend for them. They will be written with `verified.opened: false`, a note naming the exact instrument required, and the build will refuse to let the booklet claim released status while they remain so. What they must not do is cite news coverage of a regulation as though it were the regulation.
