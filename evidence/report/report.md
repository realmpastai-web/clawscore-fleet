# ClawScore fleet report

## Header

Fleet: clawscore-fleet
Observed at: 2026-10-17T15:54:49Z
Feed newest: 2026-09-11
Feed sha256: 27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034
Tool commit: aed886810063f424e8adece6e74b6880958ce135
Rule: package name casefold equals openclaw and ecosystem npm, or the ghsa_id is a data row in data/non-npm-keep.tsv; rows with withdrawn_at set are excluded

## Fleet summary

Installs: 30. Exact: 26. Range: 4. Unknown: 0. Critical or high: 27. Zero advisory: 3.

This Agent 365 comparison is a local mock: the local mock registry lists 30 rows, of which 14 have a blank or stale mock version.

| id | verdict | version | candidates | advisory_count | critical | high | credential_count | auto_approve | mcp_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claw-01 | exact | 2026.1.29 | 2026.1.29 | 627 | 18 | 249 | 0 | true | 0 |
| claw-02 | exact | 2026.1.29 | 2026.1.29 | 627 | 18 | 249 | 0 | false | 1 |
| claw-03 | exact | 2026.1.29 | 2026.1.29 | 627 | 18 | 249 | 0 | true | 2 |
| claw-04 | exact | 2026.2.14 | 2026.2.14 | 567 | 14 | 210 | 0 | false | 3 |
| claw-05 | exact | 2026.2.14 | 2026.2.14 | 567 | 14 | 210 | 1 | true | 0 |
| claw-06 | exact | 2026.2.14 | 2026.2.14 | 567 | 14 | 210 | 1 | false | 1 |
| claw-07 | exact | 2026.3.28 | 2026.3.28 | 288 | 5 | 110 | 1 | true | 2 |
| claw-08 | exact | 2026.3.28 | 2026.3.28 | 288 | 5 | 110 | 1 | false | 3 |
| claw-09 | exact | 2026.3.28 | 2026.3.28 | 288 | 5 | 110 | 2 | true | 0 |
| claw-10 | range |  | 2026.4.7-1, 2026.4.8 | 222 | 3 | 97 | 2 | false | 1 |
| claw-11 | range |  | 2026.4.7-1, 2026.4.8 | 222 | 3 | 97 | 2 | true | 2 |
| claw-12 | range |  | 2026.4.7-1, 2026.4.8 | 222 | 3 | 97 | 2 | false | 3 |
| claw-13 | range |  | 2026.4.7-1, 2026.4.8 | 222 | 3 | 97 | 3 | true | 0 |
| claw-14 | exact | 2026.4.15 | 2026.4.15 | 169 | 1 | 86 | 3 | false | 1 |
| claw-15 | exact | 2026.4.15 | 2026.4.15 | 169 | 1 | 86 | 3 | true | 2 |
| claw-16 | exact | 2026.4.15 | 2026.4.15 | 169 | 1 | 86 | 3 | false | 3 |
| claw-17 | exact | 2026.4.20 | 2026.4.20 | 157 | 1 | 85 | 0 | true | 0 |
| claw-18 | exact | 2026.4.20 | 2026.4.20 | 157 | 1 | 85 | 0 | false | 1 |
| claw-19 | exact | 2026.4.20 | 2026.4.20 | 157 | 1 | 85 | 0 | true | 2 |
| claw-20 | exact | 2026.4.21 | 2026.4.21 | 157 | 1 | 85 | 0 | false | 3 |
| claw-21 | exact | 2026.4.21 | 2026.4.21 | 157 | 1 | 85 | 1 | true | 0 |
| claw-22 | exact | 2026.4.21 | 2026.4.21 | 157 | 1 | 85 | 1 | false | 1 |
| claw-23 | exact | 2026.4.22 | 2026.4.22 | 148 | 1 | 84 | 1 | true | 2 |
| claw-24 | exact | 2026.4.22 | 2026.4.22 | 148 | 1 | 84 | 1 | false | 3 |
| claw-25 | exact | 2026.4.22 | 2026.4.22 | 148 | 1 | 84 | 2 | true | 0 |
| claw-26 | exact | 2026.4.23 | 2026.4.23 | 146 | 1 | 82 | 2 | false | 1 |
| claw-27 | exact | 2026.4.23 | 2026.4.23 | 146 | 1 | 82 | 2 | true | 2 |
| claw-28 | exact | 2026.10.4 | 2026.10.4 | 0 | 0 | 0 | 2 | false | 3 |
| claw-29 | exact | 2026.10.4 | 2026.10.4 | 0 | 0 | 0 | 3 | true | 0 |
| claw-30 | exact | 2026.10.4 | 2026.10.4 | 0 | 0 | 0 | 3 | false | 1 |

## npm audit comparison

| version | npm query date | feed newest | npm audit | ClawScore | overlap | GitHub-DB-not-returned | repo-only | npm-only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026.1.29 | 2026-10-21 | 2026-09-11 | 555 | 627 | 555 | 2 (GHSA-2j8v-hwgc-x698, GHSA-hggm-x7r9-mm7v) | 70 | 0 |
| 2026.2.14 | 2026-10-21 | 2026-09-11 | 493 | 567 | 493 | 2 (GHSA-2j8v-hwgc-x698, GHSA-hggm-x7r9-mm7v) | 72 | 0 |
| 2026.3.28 | 2026-10-21 | 2026-09-11 | 212 | 288 | 212 | 1 (GHSA-2j8v-hwgc-x698) | 75 | 0 |
| 2026.4.7-1 | 2026-10-21 | 2026-09-11 | 0 | 222 | 0 | 146 (GHSA-24vr-rprv-67rf, GHSA-275c-xpvc-jgfw, GHSA-2767-2q9v-9326, GHSA-2cq5-mf3v-mx44, GHSA-2gvc-4f3c-2855, GHSA-2hfg-4fh4-qp7f, GHSA-2hh7-c75g-qj2r, GHSA-2j8v-hwgc-x698, GHSA-2xcp-x87w-q377, GHSA-3c6j-hq33-3jv4, GHSA-3fv3-6p2v-gxwj, GHSA-3vvq-q2qc-7rmp, GHSA-3wqp-prf6-2m72, GHSA-49cg-279w-m73x, GHSA-4f8g-77mw-3rxc, GHSA-4hpg-mp64-x7xq, GHSA-4m3v-q747-pc6h, GHSA-525j-hqq2-66r4, GHSA-527m-976r-jf79, GHSA-536q-mj95-h29h, GHSA-53vx-pmqw-863c, GHSA-55cf-xx38-4p9p, GHSA-57r2-h2wj-g887, GHSA-5fc7-f62m-8983, GHSA-5gjc-grvm-m88j, GHSA-5h3f-885m-v22w, GHSA-5h3g-6xhh-rg6p, GHSA-5wj5-87vq-39xm, GHSA-66r7-m7xm-v49h, GHSA-67mf-f936-ppxf, GHSA-68x5-xx89-w9mm, GHSA-68xw-r643-9p5w, GHSA-6c4r-g249-wv3c, GHSA-6fvr-66p3-3qj4, GHSA-72fw-cqh5-f324, GHSA-72q8-jcmc-97wx, GHSA-736r-jwj6-4w23, GHSA-7437-7hg8-frrw, GHSA-77pv-3w4q-vrj5, GHSA-77q5-rr5v-x43q, GHSA-7g8c-cfr3-vqqr, GHSA-7hxm-f538-3xp6, GHSA-7jm2-g593-4qrc, GHSA-7jp6-r74r-995q, GHSA-7wv4-cc7p-jhxc, GHSA-82qx-6vj7-p8m2, GHSA-8372-7vhw-cm6q, GHSA-83w9-h5wv-j9xm, GHSA-8c59-hr4w-qg69, GHSA-8j37-5w68-wj2g, GHSA-8mg9-j9cf-54cj, GHSA-8wg3-5mcm-fjq8, GHSA-92jp-89mq-4374, GHSA-939r-rj45-g2rj, GHSA-93rg-2xm5-2p9v, GHSA-985f-72mj-8gf7, GHSA-9c3v-684m-579c, GHSA-9v8j-9c9g-w66c, GHSA-c226-q6fx-6j6c, GHSA-c28g-vh7m-fm7v, GHSA-c29c-2q9c-pc86, GHSA-c4qg-j8jg-42q5, GHSA-c4qm-58hj-j6pj, GHSA-c9h3-5p7r-mrjh, GHSA-ccwh-wwpp-6wg5, GHSA-ccx3-fw7q-rr2r, GHSA-chr9-m4q2-76hw, GHSA-cm8v-2vh9-cxf3, GHSA-cmfr-9m2r-xwhq, GHSA-cqwv-9qjx-vxw2, GHSA-cw4q-gqg5-g38h, GHSA-cwj3-vqpp-pmxr, GHSA-cwpp-5962-q4f6, GHSA-f397-5vjw-v2c2, GHSA-f3h5-h452-vp3j, GHSA-f934-5rqf-xx47, GHSA-fcvx-5cxc-v5p8, GHSA-fq9j-vw4w-fr6v, GHSA-g2hm-779g-vm32, GHSA-g375-h3v6-4873, GHSA-gfg9-5357-hv4c, GHSA-gj9q-8w99-mp8j, GHSA-gp79-m99v-gjmh, GHSA-grc3-2j34-p6gm, GHSA-gxg4-2rrr-jhc7, GHSA-h2vw-ph2c-jvwf, GHSA-hcm3-8f6r-6xwg, GHSA-hw9r-h9mr-4jff, GHSA-hxvm-xjvf-93f3, GHSA-j472-gf56-x589, GHSA-j4c5-89f5-f3pm, GHSA-j6c7-3h5x-99g9, GHSA-jf25-7968-h2h5, GHSA-jvm4-4j77-39p6, GHSA-jwrq-8g5x-5fhm, GHSA-mgq6-vr84-7m2j, GHSA-mhq8-78pj-5j79, GHSA-mj59-h3q9-ghfh, GHSA-mpc8-jxjh-qpgh, GHSA-mr34-9552-qr95, GHSA-p2fh-f5fc-44hr, GHSA-p39j-x9h5-q66m, GHSA-p73f-w79w-jqr5, GHSA-q2gc-xjqw-qp89, GHSA-q3jj-46pq-826r, GHSA-q7q8-3mgw-q67r, GHSA-q8ff-7ffm-m3r9, GHSA-q99w-vh6v-q3v7, GHSA-qh2f-99mv-mrcf, GHSA-qjpc-qf9m-xwmr, GHSA-qmwg-qprg-3j38, GHSA-qqq7-4hxc-x63c, GHSA-qrp5-gfw2-gxv4, GHSA-qx8j-g322-qj6m, GHSA-r39h-4c2p-3jxp, GHSA-r6xh-pqhr-v4xh, GHSA-rggc-m335-3wvj, GHSA-rj2p-j66c-mgqh, GHSA-rj6p-xmxr-qj4h, GHSA-rjxq-qqhf-8hwh, GHSA-rx78-29qr-5hq8, GHSA-v2ww-5rh7-2h5v, GHSA-v6r2-jh58-xx6w, GHSA-v8cx-933x-r976, GHSA-v8qf-fr4g-28p2, GHSA-vc32-h5mq-453v, GHSA-vfp4-8x56-j7c5, GHSA-vr5g-mmx7-h897, GHSA-vxx3-6hc9-7cc3, GHSA-w4v6-g3wm-w36c, GHSA-w5ww-7chg-mxcq, GHSA-w8g9-x8gx-crmm, GHSA-w9hf-3pp7-pvxv, GHSA-w9j9-w4cp-6wgr, GHSA-wc84-j36w-pw4x, GHSA-whf9-3hcx-gq54, GHSA-wppj-c6mr-83jj, GHSA-wv26-j37q-2g7p, GHSA-x3h8-jrgh-p8jx, GHSA-x629-46cc-7xgw, GHSA-xh72-v6v9-mwhc, GHSA-xmxx-7p24-h892, GHSA-xq94-r468-qwgj, GHSA-xr4f-mjxj-w6w5, GHSA-xrq9-jm7v-g9h7, GHSA-xww8-gqvh-92x9) | 76 | 0 |
| 2026.4.8 | 2026-10-21 | 2026-09-11 | 125 | 202 | 125 | 1 (GHSA-2j8v-hwgc-x698) | 76 | 0 |
| 2026.4.15 | 2026-10-21 | 2026-09-11 | 89 | 169 | 89 | 1 (GHSA-2j8v-hwgc-x698) | 79 | 0 |
| 2026.4.20 | 2026-10-21 | 2026-09-11 | 77 | 157 | 77 | 1 (GHSA-2j8v-hwgc-x698) | 79 | 0 |
| 2026.4.21 | 2026-10-21 | 2026-09-11 | 76 | 157 | 76 | 1 (GHSA-2j8v-hwgc-x698) | 80 | 0 |
| 2026.4.22 | 2026-10-21 | 2026-09-11 | 67 | 148 | 67 | 1 (GHSA-2j8v-hwgc-x698) | 80 | 0 |
| 2026.4.23 | 2026-10-21 | 2026-09-11 | 65 | 146 | 65 | 1 (GHSA-2j8v-hwgc-x698) | 80 | 0 |
| 2026.10.4 | 2026-10-21 | 2026-09-11 | 0 | 0 | 0 | 0 | 0 | 0 |

npm audit returned 555 advisories for openclaw@2026.1.29 on 2026-10-21; the maker's repository lists 627 (feed newest 2026-09-11).

npm audit returned 493 advisories for openclaw@2026.2.14 on 2026-10-21; the maker's repository lists 567 (feed newest 2026-09-11).

npm audit returned 212 advisories for openclaw@2026.3.28 on 2026-10-21; the maker's repository lists 288 (feed newest 2026-09-11).

npm audit returned 0 advisories for openclaw@2026.4.7-1 on 2026-10-21; the maker's repository lists 222 (feed newest 2026-09-11).

npm audit returned 125 advisories for openclaw@2026.4.8 on 2026-10-21; the maker's repository lists 202 (feed newest 2026-09-11).

npm audit returned 89 advisories for openclaw@2026.4.15 on 2026-10-21; the maker's repository lists 169 (feed newest 2026-09-11).

npm audit returned 77 advisories for openclaw@2026.4.20 on 2026-10-21; the maker's repository lists 157 (feed newest 2026-09-11).

npm audit returned 76 advisories for openclaw@2026.4.21 on 2026-10-21; the maker's repository lists 157 (feed newest 2026-09-11).

npm audit returned 67 advisories for openclaw@2026.4.22 on 2026-10-21; the maker's repository lists 148 (feed newest 2026-09-11).

npm audit returned 65 advisories for openclaw@2026.4.23 on 2026-10-21; the maker's repository lists 146 (feed newest 2026-09-11).

npm audit returned 0 advisories for openclaw@2026.10.4 on 2026-10-21; the maker's repository lists 0 (feed newest 2026-09-11).

## Fix order

Patch installs that match at least one critical or high advisory, then rotate credential names ordered by reach. min_clear_release (earliest release from which no critical or high published advisory matches, as of 2026-09-11) is 2026.8.1; it still matches 2 medium advisories.

| install | version | candidates | min_clear_release | credential_count | auto_approve |
| --- | --- | --- | --- | --- | --- |
| claw-13 |  | 2026.4.7-1, 2026.4.8 | 2026.8.1 | 3 | true |
| claw-15 | 2026.4.15 | 2026.4.15 | 2026.8.1 | 3 | true |
| claw-14 | 2026.4.15 | 2026.4.15 | 2026.8.1 | 3 | false |
| claw-16 | 2026.4.15 | 2026.4.15 | 2026.8.1 | 3 | false |
| claw-09 | 2026.3.28 | 2026.3.28 | 2026.8.1 | 2 | true |
| claw-11 |  | 2026.4.7-1, 2026.4.8 | 2026.8.1 | 2 | true |
| claw-25 | 2026.4.22 | 2026.4.22 | 2026.8.1 | 2 | true |
| claw-27 | 2026.4.23 | 2026.4.23 | 2026.8.1 | 2 | true |
| claw-10 |  | 2026.4.7-1, 2026.4.8 | 2026.8.1 | 2 | false |
| claw-12 |  | 2026.4.7-1, 2026.4.8 | 2026.8.1 | 2 | false |
| claw-26 | 2026.4.23 | 2026.4.23 | 2026.8.1 | 2 | false |
| claw-05 | 2026.2.14 | 2026.2.14 | 2026.8.1 | 1 | true |
| claw-07 | 2026.3.28 | 2026.3.28 | 2026.8.1 | 1 | true |
| claw-21 | 2026.4.21 | 2026.4.21 | 2026.8.1 | 1 | true |
| claw-23 | 2026.4.22 | 2026.4.22 | 2026.8.1 | 1 | true |
| claw-06 | 2026.2.14 | 2026.2.14 | 2026.8.1 | 1 | false |
| claw-08 | 2026.3.28 | 2026.3.28 | 2026.8.1 | 1 | false |
| claw-22 | 2026.4.21 | 2026.4.21 | 2026.8.1 | 1 | false |
| claw-24 | 2026.4.22 | 2026.4.22 | 2026.8.1 | 1 | false |
| claw-01 | 2026.1.29 | 2026.1.29 | 2026.8.1 | 0 | true |
| claw-03 | 2026.1.29 | 2026.1.29 | 2026.8.1 | 0 | true |
| claw-17 | 2026.4.20 | 2026.4.20 | 2026.8.1 | 0 | true |
| claw-19 | 2026.4.20 | 2026.4.20 | 2026.8.1 | 0 | true |
| claw-02 | 2026.1.29 | 2026.1.29 | 2026.8.1 | 0 | false |
| claw-04 | 2026.2.14 | 2026.2.14 | 2026.8.1 | 0 | false |
| claw-18 | 2026.4.20 | 2026.4.20 | 2026.8.1 | 0 | false |
| claw-20 | 2026.4.21 | 2026.4.21 | 2026.8.1 | 0 | false |

| credential | reach | installs |
| --- | --- | --- |
| AWS_ACCESS_KEY_ID | 5 | claw-09, claw-10, claw-16, claw-25, claw-26 |
| SLACK_BOT_TOKEN | 5 | claw-07, claw-13, claw-14, claw-15, claw-23 |
| STRIPE_SECRET_KEY | 5 | claw-08, claw-14, claw-15, claw-16, claw-24 |
| ANTHROPIC_API_KEY | 4 | claw-09, claw-15, claw-16, claw-25 |
| AWS_SECRET_ACCESS_KEY | 4 | claw-10, claw-11, claw-26, claw-27 |
| GITHUB_PERSONAL_ACCESS_TOKEN | 4 | claw-05, claw-12, claw-13, claw-21 |
| OPENAI_API_KEY | 4 | claw-06, claw-13, claw-14, claw-22 |
| DISCORD_BOT_TOKEN | 3 | claw-11, claw-12, claw-27 |

## Per-install detail

### claw-01

Verdict: exact
Version: 2026.1.29
Candidates: 2026.1.29
Files read: /srv/agents/claw-01/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 627 published advisories (18 critical, 249 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /srv/agents/claw-01/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-33rq-m5x2-fvgf severity high https://github.com/advisories/GHSA-33rq-m5x2-fvgf
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3fqr-4cg8-h96q severity high https://github.com/advisories/GHSA-3fqr-4cg8-h96q
- GHSA-3hcm-ggvf-rch5 severity high https://github.com/advisories/GHSA-3hcm-ggvf-rch5
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4564-pvr2-qq4h severity high https://github.com/advisories/GHSA-4564-pvr2-qq4h
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4hg8-92x6-h2f3 severity high https://github.com/advisories/GHSA-4hg8-92x6-h2f3
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4rj2-gpmh-qq5x severity critical https://github.com/advisories/GHSA-4rj2-gpmh-qq5x
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-56f2-hvwg-5743 severity high https://github.com/advisories/GHSA-56f2-hvwg-5743
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-5xfq-5mr7-426q severity high https://github.com/advisories/GHSA-5xfq-5mr7-426q
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-64qx-vpxx-mvqf severity high https://github.com/advisories/GHSA-64qx-vpxx-mvqf
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xhj-55q9-pc3m severity high https://github.com/advisories/GHSA-7xhj-55q9-pc3m
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8jpq-5h99-ff5r severity high https://github.com/advisories/GHSA-8jpq-5h99-ff5r
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-943q-mwmv-hhvh severity high https://github.com/advisories/GHSA-943q-mwmv-hhvh
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cv7m-c9jx-vg7q severity high https://github.com/advisories/GHSA-cv7m-c9jx-vg7q
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fhvm-j76f-qmjv severity critical https://github.com/advisories/GHSA-fhvm-j76f-qmjv
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g6q9-8fvw-f7rf severity high https://github.com/advisories/GHSA-g6q9-8fvw-f7rf
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-gq9c-wg68-gwj2 severity high https://github.com/advisories/GHSA-gq9c-wg68-gwj2
- GHSA-gv46-4xfq-jv58 severity critical https://github.com/advisories/GHSA-gv46-4xfq-jv58
- GHSA-h3f9-mjwj-w476 severity high https://github.com/advisories/GHSA-h3f9-mjwj-w476
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9g4-589h-68xv severity high https://github.com/advisories/GHSA-h9g4-589h-68xv
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hv93-r4j3-q65f severity high https://github.com/advisories/GHSA-hv93-r4j3-q65f
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j27p-hq53-9wgc severity high https://github.com/advisories/GHSA-j27p-hq53-9wgc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jmm5-fvh5-gf4p severity high https://github.com/advisories/GHSA-jmm5-fvh5-gf4p
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jqpq-mgvm-f9r6 severity high https://github.com/advisories/GHSA-jqpq-mgvm-f9r6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jrvc-8ff5-2f9f severity high https://github.com/advisories/GHSA-jrvc-8ff5-2f9f
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m7x8-2w3w-pr42 severity high https://github.com/advisories/GHSA-m7x8-2w3w-pr42
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mp5h-m6qj-6292 severity high https://github.com/advisories/GHSA-mp5h-m6qj-6292
- GHSA-mqpw-46fh-299h severity high https://github.com/advisories/GHSA-mqpw-46fh-299h
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mr32-vwc2-5j6h severity high https://github.com/advisories/GHSA-mr32-vwc2-5j6h
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p25h-9q54-ffvw severity high https://github.com/advisories/GHSA-p25h-9q54-ffvw
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pchc-86f6-8758 severity high https://github.com/advisories/GHSA-pchc-86f6-8758
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-pv58-549p-qh99 severity high https://github.com/advisories/GHSA-pv58-549p-qh99
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q447-rj3r-2cgh severity high https://github.com/advisories/GHSA-q447-rj3r-2cgh
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qj77-c3c8-9c3q severity high https://github.com/advisories/GHSA-qj77-c3c8-9c3q
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qrq5-wjgg-rvqw severity high https://github.com/advisories/GHSA-qrq5-wjgg-rvqw
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r5fq-947m-xm57 severity high https://github.com/advisories/GHSA-r5fq-947m-xm57
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rq6g-px6m-c248 severity high https://github.com/advisories/GHSA-rq6g-px6m-c248
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rv39-79c4-7459 severity critical https://github.com/advisories/GHSA-rv39-79c4-7459
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rwj8-p9vq-25gv severity high https://github.com/advisories/GHSA-rwj8-p9vq-25gv
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6c6-vqqg-w888 severity high https://github.com/advisories/GHSA-v6c6-vqqg-w888
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v773-r54f-q32w severity high https://github.com/advisories/GHSA-v773-r54f-q32w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5c7-9qqw-6645 severity high https://github.com/advisories/GHSA-w5c7-9qqw-6645
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x22m-j5qq-j49m severity high https://github.com/advisories/GHSA-x22m-j5qq-j49m
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xc7w-v5x6-cc87 severity high https://github.com/advisories/GHSA-xc7w-v5x6-cc87
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xvhf-x56f-2hpp severity high https://github.com/advisories/GHSA-xvhf-x56f-2hpp
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-02

Verdict: exact
Version: 2026.1.29
Candidates: 2026.1.29
Files read: /workspace/claw-02/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 627 published advisories (18 critical, 249 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /workspace/claw-02/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-33rq-m5x2-fvgf severity high https://github.com/advisories/GHSA-33rq-m5x2-fvgf
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3fqr-4cg8-h96q severity high https://github.com/advisories/GHSA-3fqr-4cg8-h96q
- GHSA-3hcm-ggvf-rch5 severity high https://github.com/advisories/GHSA-3hcm-ggvf-rch5
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4564-pvr2-qq4h severity high https://github.com/advisories/GHSA-4564-pvr2-qq4h
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4hg8-92x6-h2f3 severity high https://github.com/advisories/GHSA-4hg8-92x6-h2f3
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4rj2-gpmh-qq5x severity critical https://github.com/advisories/GHSA-4rj2-gpmh-qq5x
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-56f2-hvwg-5743 severity high https://github.com/advisories/GHSA-56f2-hvwg-5743
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-5xfq-5mr7-426q severity high https://github.com/advisories/GHSA-5xfq-5mr7-426q
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-64qx-vpxx-mvqf severity high https://github.com/advisories/GHSA-64qx-vpxx-mvqf
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xhj-55q9-pc3m severity high https://github.com/advisories/GHSA-7xhj-55q9-pc3m
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8jpq-5h99-ff5r severity high https://github.com/advisories/GHSA-8jpq-5h99-ff5r
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-943q-mwmv-hhvh severity high https://github.com/advisories/GHSA-943q-mwmv-hhvh
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cv7m-c9jx-vg7q severity high https://github.com/advisories/GHSA-cv7m-c9jx-vg7q
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fhvm-j76f-qmjv severity critical https://github.com/advisories/GHSA-fhvm-j76f-qmjv
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g6q9-8fvw-f7rf severity high https://github.com/advisories/GHSA-g6q9-8fvw-f7rf
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-gq9c-wg68-gwj2 severity high https://github.com/advisories/GHSA-gq9c-wg68-gwj2
- GHSA-gv46-4xfq-jv58 severity critical https://github.com/advisories/GHSA-gv46-4xfq-jv58
- GHSA-h3f9-mjwj-w476 severity high https://github.com/advisories/GHSA-h3f9-mjwj-w476
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9g4-589h-68xv severity high https://github.com/advisories/GHSA-h9g4-589h-68xv
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hv93-r4j3-q65f severity high https://github.com/advisories/GHSA-hv93-r4j3-q65f
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j27p-hq53-9wgc severity high https://github.com/advisories/GHSA-j27p-hq53-9wgc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jmm5-fvh5-gf4p severity high https://github.com/advisories/GHSA-jmm5-fvh5-gf4p
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jqpq-mgvm-f9r6 severity high https://github.com/advisories/GHSA-jqpq-mgvm-f9r6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jrvc-8ff5-2f9f severity high https://github.com/advisories/GHSA-jrvc-8ff5-2f9f
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m7x8-2w3w-pr42 severity high https://github.com/advisories/GHSA-m7x8-2w3w-pr42
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mp5h-m6qj-6292 severity high https://github.com/advisories/GHSA-mp5h-m6qj-6292
- GHSA-mqpw-46fh-299h severity high https://github.com/advisories/GHSA-mqpw-46fh-299h
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mr32-vwc2-5j6h severity high https://github.com/advisories/GHSA-mr32-vwc2-5j6h
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p25h-9q54-ffvw severity high https://github.com/advisories/GHSA-p25h-9q54-ffvw
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pchc-86f6-8758 severity high https://github.com/advisories/GHSA-pchc-86f6-8758
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-pv58-549p-qh99 severity high https://github.com/advisories/GHSA-pv58-549p-qh99
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q447-rj3r-2cgh severity high https://github.com/advisories/GHSA-q447-rj3r-2cgh
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qj77-c3c8-9c3q severity high https://github.com/advisories/GHSA-qj77-c3c8-9c3q
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qrq5-wjgg-rvqw severity high https://github.com/advisories/GHSA-qrq5-wjgg-rvqw
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r5fq-947m-xm57 severity high https://github.com/advisories/GHSA-r5fq-947m-xm57
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rq6g-px6m-c248 severity high https://github.com/advisories/GHSA-rq6g-px6m-c248
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rv39-79c4-7459 severity critical https://github.com/advisories/GHSA-rv39-79c4-7459
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rwj8-p9vq-25gv severity high https://github.com/advisories/GHSA-rwj8-p9vq-25gv
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6c6-vqqg-w888 severity high https://github.com/advisories/GHSA-v6c6-vqqg-w888
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v773-r54f-q32w severity high https://github.com/advisories/GHSA-v773-r54f-q32w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5c7-9qqw-6645 severity high https://github.com/advisories/GHSA-w5c7-9qqw-6645
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x22m-j5qq-j49m severity high https://github.com/advisories/GHSA-x22m-j5qq-j49m
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xc7w-v5x6-cc87 severity high https://github.com/advisories/GHSA-xc7w-v5x6-cc87
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xvhf-x56f-2hpp severity high https://github.com/advisories/GHSA-xvhf-x56f-2hpp
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-03

Verdict: exact
Version: 2026.1.29
Candidates: 2026.1.29
Files read: /app/claw-03/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 627 published advisories (18 critical, 249 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /app/claw-03/.openclaw/openclaw.json, /app/claw-03/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-33rq-m5x2-fvgf severity high https://github.com/advisories/GHSA-33rq-m5x2-fvgf
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3fqr-4cg8-h96q severity high https://github.com/advisories/GHSA-3fqr-4cg8-h96q
- GHSA-3hcm-ggvf-rch5 severity high https://github.com/advisories/GHSA-3hcm-ggvf-rch5
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4564-pvr2-qq4h severity high https://github.com/advisories/GHSA-4564-pvr2-qq4h
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4hg8-92x6-h2f3 severity high https://github.com/advisories/GHSA-4hg8-92x6-h2f3
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4rj2-gpmh-qq5x severity critical https://github.com/advisories/GHSA-4rj2-gpmh-qq5x
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-56f2-hvwg-5743 severity high https://github.com/advisories/GHSA-56f2-hvwg-5743
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-5xfq-5mr7-426q severity high https://github.com/advisories/GHSA-5xfq-5mr7-426q
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-64qx-vpxx-mvqf severity high https://github.com/advisories/GHSA-64qx-vpxx-mvqf
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xhj-55q9-pc3m severity high https://github.com/advisories/GHSA-7xhj-55q9-pc3m
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8jpq-5h99-ff5r severity high https://github.com/advisories/GHSA-8jpq-5h99-ff5r
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-943q-mwmv-hhvh severity high https://github.com/advisories/GHSA-943q-mwmv-hhvh
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cv7m-c9jx-vg7q severity high https://github.com/advisories/GHSA-cv7m-c9jx-vg7q
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fhvm-j76f-qmjv severity critical https://github.com/advisories/GHSA-fhvm-j76f-qmjv
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g6q9-8fvw-f7rf severity high https://github.com/advisories/GHSA-g6q9-8fvw-f7rf
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-gq9c-wg68-gwj2 severity high https://github.com/advisories/GHSA-gq9c-wg68-gwj2
- GHSA-gv46-4xfq-jv58 severity critical https://github.com/advisories/GHSA-gv46-4xfq-jv58
- GHSA-h3f9-mjwj-w476 severity high https://github.com/advisories/GHSA-h3f9-mjwj-w476
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9g4-589h-68xv severity high https://github.com/advisories/GHSA-h9g4-589h-68xv
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hv93-r4j3-q65f severity high https://github.com/advisories/GHSA-hv93-r4j3-q65f
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j27p-hq53-9wgc severity high https://github.com/advisories/GHSA-j27p-hq53-9wgc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jmm5-fvh5-gf4p severity high https://github.com/advisories/GHSA-jmm5-fvh5-gf4p
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jqpq-mgvm-f9r6 severity high https://github.com/advisories/GHSA-jqpq-mgvm-f9r6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jrvc-8ff5-2f9f severity high https://github.com/advisories/GHSA-jrvc-8ff5-2f9f
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m7x8-2w3w-pr42 severity high https://github.com/advisories/GHSA-m7x8-2w3w-pr42
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mp5h-m6qj-6292 severity high https://github.com/advisories/GHSA-mp5h-m6qj-6292
- GHSA-mqpw-46fh-299h severity high https://github.com/advisories/GHSA-mqpw-46fh-299h
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mr32-vwc2-5j6h severity high https://github.com/advisories/GHSA-mr32-vwc2-5j6h
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p25h-9q54-ffvw severity high https://github.com/advisories/GHSA-p25h-9q54-ffvw
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pchc-86f6-8758 severity high https://github.com/advisories/GHSA-pchc-86f6-8758
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-pv58-549p-qh99 severity high https://github.com/advisories/GHSA-pv58-549p-qh99
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q447-rj3r-2cgh severity high https://github.com/advisories/GHSA-q447-rj3r-2cgh
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qj77-c3c8-9c3q severity high https://github.com/advisories/GHSA-qj77-c3c8-9c3q
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qrq5-wjgg-rvqw severity high https://github.com/advisories/GHSA-qrq5-wjgg-rvqw
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r5fq-947m-xm57 severity high https://github.com/advisories/GHSA-r5fq-947m-xm57
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rq6g-px6m-c248 severity high https://github.com/advisories/GHSA-rq6g-px6m-c248
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rv39-79c4-7459 severity critical https://github.com/advisories/GHSA-rv39-79c4-7459
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rwj8-p9vq-25gv severity high https://github.com/advisories/GHSA-rwj8-p9vq-25gv
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6c6-vqqg-w888 severity high https://github.com/advisories/GHSA-v6c6-vqqg-w888
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v773-r54f-q32w severity high https://github.com/advisories/GHSA-v773-r54f-q32w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5c7-9qqw-6645 severity high https://github.com/advisories/GHSA-w5c7-9qqw-6645
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x22m-j5qq-j49m severity high https://github.com/advisories/GHSA-x22m-j5qq-j49m
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xc7w-v5x6-cc87 severity high https://github.com/advisories/GHSA-xc7w-v5x6-cc87
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xvhf-x56f-2hpp severity high https://github.com/advisories/GHSA-xvhf-x56f-2hpp
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-04

Verdict: exact
Version: 2026.2.14
Candidates: 2026.2.14
Files read: /var/lib/claw/claw-04/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 567 published advisories (14 critical, 210 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /var/lib/claw/claw-04/.openclaw/openclaw.json, /var/lib/claw/claw-04/.openclaw/mcp/extra.json, /var/lib/claw/claw-04/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-05

Verdict: exact
Version: 2026.2.14
Candidates: 2026.2.14
Files read: /opt/apps/claw-05/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 567 published advisories (14 critical, 210 high) as of 2026-09-11

Credential names: GITHUB_PERSONAL_ACCESS_TOKEN. credential reach is lab-tested only. Sources: /opt/apps/claw-05/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-06

Verdict: exact
Version: 2026.2.14
Candidates: 2026.2.14
Files read: /home/node/work/claw-06/node_modules/openclaw/dist/build-info.json
Matched files: dist/build-info.json

matches 567 published advisories (14 critical, 210 high) as of 2026-09-11

Credential names: OPENAI_API_KEY. credential reach is lab-tested only. Sources: /home/node/work/claw-06/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-25gx-x37c-7pph severity high https://github.com/advisories/GHSA-25gx-x37c-7pph
- GHSA-2ch6-x3g4-7759 severity high https://github.com/advisories/GHSA-2ch6-x3g4-7759
- GHSA-2fgq-7j6h-9rm4 severity high https://github.com/advisories/GHSA-2fgq-7j6h-9rm4
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2pr2-hcv6-7gwv severity high https://github.com/advisories/GHSA-2pr2-hcv6-7gwv
- GHSA-2qj5-gwg2-xwc4 severity high https://github.com/advisories/GHSA-2qj5-gwg2-xwc4
- GHSA-2rqg-gjgv-84jm severity high https://github.com/advisories/GHSA-2rqg-gjgv-84jm
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-39pp-xp36-q6mg severity high https://github.com/advisories/GHSA-39pp-xp36-q6mg
- GHSA-3c6h-g97w-fg78 severity high https://github.com/advisories/GHSA-3c6h-g97w-fg78
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3cw3-5vxw-g2h3 severity high https://github.com/advisories/GHSA-3cw3-5vxw-g2h3
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3jx4-q2m7-r496 severity high https://github.com/advisories/GHSA-3jx4-q2m7-r496
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3w6x-gv34-mqpf severity high https://github.com/advisories/GHSA-3w6x-gv34-mqpf
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-474h-prjg-mmw3 severity high https://github.com/advisories/GHSA-474h-prjg-mmw3
- GHSA-48vw-m3qc-wr99 severity high https://github.com/advisories/GHSA-48vw-m3qc-wr99
- GHSA-4jpw-hj22-2xmc severity critical https://github.com/advisories/GHSA-4jpw-hj22-2xmc
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4qwc-c7g9-4xcw severity high https://github.com/advisories/GHSA-4qwc-c7g9-4xcw
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4w7m-58cg-cmff severity high https://github.com/advisories/GHSA-4w7m-58cg-cmff
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5gj7-jf77-q2q2 severity high https://github.com/advisories/GHSA-5gj7-jf77-q2q2
- GHSA-5r8f-96gm-5j6g severity high https://github.com/advisories/GHSA-5r8f-96gm-5j6g
- GHSA-5v6x-rfc3-7qfr severity high https://github.com/advisories/GHSA-5v6x-rfc3-7qfr
- GHSA-5wcw-8jjv-m286 severity high https://github.com/advisories/GHSA-5wcw-8jjv-m286
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-63f5-hhc7-cx6p severity high https://github.com/advisories/GHSA-63f5-hhc7-cx6p
- GHSA-659f-22xc-98f2 severity high https://github.com/advisories/GHSA-659f-22xc-98f2
- GHSA-65h8-27jh-q8wv severity high https://github.com/advisories/GHSA-65h8-27jh-q8wv
- GHSA-65rx-fvh6-r4h2 severity high https://github.com/advisories/GHSA-65rx-fvh6-r4h2
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-6mgf-v5j7-45cr severity high https://github.com/advisories/GHSA-6mgf-v5j7-45cr
- GHSA-6pfc-6m7w-m8fx severity high https://github.com/advisories/GHSA-6pfc-6m7w-m8fx
- GHSA-6xg4-82hv-cp6f severity high https://github.com/advisories/GHSA-6xg4-82hv-cp6f
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-767m-xrhc-fxm7 severity high https://github.com/advisories/GHSA-767m-xrhc-fxm7
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7977-c43c-xpwj severity critical https://github.com/advisories/GHSA-7977-c43c-xpwj
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7fcc-cw49-xm78 severity high https://github.com/advisories/GHSA-7fcc-cw49-xm78
- GHSA-7ff8-xjh3-mgh6 severity high https://github.com/advisories/GHSA-7ff8-xjh3-mgh6
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-7xmq-g46g-f8pv severity high https://github.com/advisories/GHSA-7xmq-g46g-f8pv
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8689-gm9g-jgr6 severity high https://github.com/advisories/GHSA-8689-gm9g-jgr6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8rh7-6779-cjqq severity critical https://github.com/advisories/GHSA-8rh7-6779-cjqq
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-94pw-c6m8-p9p9 severity high https://github.com/advisories/GHSA-94pw-c6m8-p9p9
- GHSA-98hh-7ghg-x6rq severity high https://github.com/advisories/GHSA-98hh-7ghg-x6rq
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-99qw-6mr3-36qr severity high https://github.com/advisories/GHSA-99qw-6mr3-36qr
- GHSA-9f72-qcpw-2hxc severity high https://github.com/advisories/GHSA-9f72-qcpw-2hxc
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9hjh-fr4f-gxc4 severity critical https://github.com/advisories/GHSA-9hjh-fr4f-gxc4
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p38-94jf-hgjj severity high https://github.com/advisories/GHSA-9p38-94jf-hgjj
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9p93-7j67-5pc2 severity high https://github.com/advisories/GHSA-9p93-7j67-5pc2
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cfvj-7rx7-fc7c severity high https://github.com/advisories/GHSA-cfvj-7rx7-fc7c
- GHSA-cg6c-q2hx-69h7 severity high https://github.com/advisories/GHSA-cg6c-q2hx-69h7
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-cxmw-p77q-wchg severity high https://github.com/advisories/GHSA-cxmw-p77q-wchg
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-f6pf-4gjx-c94r severity high https://github.com/advisories/GHSA-f6pf-4gjx-c94r
- GHSA-f7ww-2725-qvw2 severity high https://github.com/advisories/GHSA-f7ww-2725-qvw2
- GHSA-f8mp-vj46-cq8v severity high https://github.com/advisories/GHSA-f8mp-vj46-cq8v
- GHSA-fgvx-58p6-gjwc severity critical https://github.com/advisories/GHSA-fgvx-58p6-gjwc
- GHSA-fh3f-q9qw-93j9 severity high https://github.com/advisories/GHSA-fh3f-q9qw-93j9
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fqcm-97m6-w7rm severity high https://github.com/advisories/GHSA-fqcm-97m6-w7rm
- GHSA-fqw4-mph7-2vr8 severity critical https://github.com/advisories/GHSA-fqw4-mph7-2vr8
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g2f6-pwvx-r275 severity high https://github.com/advisories/GHSA-g2f6-pwvx-r275
- GHSA-g353-mgv3-8pcj severity high https://github.com/advisories/GHSA-g353-mgv3-8pcj
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g75x-8qqm-2vxp severity high https://github.com/advisories/GHSA-g75x-8qqm-2vxp
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-g99v-8hwm-g76g severity high https://github.com/advisories/GHSA-g99v-8hwm-g76g
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-gg9v-mgcp-v6m7 severity high https://github.com/advisories/GHSA-gg9v-mgcp-v6m7
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-gp3q-wpq4-5c5h severity high https://github.com/advisories/GHSA-gp3q-wpq4-5c5h
- GHSA-h5hg-h7rr-gpf3 severity high https://github.com/advisories/GHSA-h5hg-h7rr-gpf3
- GHSA-h9xm-j4qg-fvpg severity high https://github.com/advisories/GHSA-h9xm-j4qg-fvpg
- GHSA-hc5h-pmr3-3497 severity critical https://github.com/advisories/GHSA-hc5h-pmr3-3497
- GHSA-hf68-49fm-59cq severity critical https://github.com/advisories/GHSA-hf68-49fm-59cq
- GHSA-hggm-x7r9-mm7v severity high https://github.com/advisories/GHSA-hggm-x7r9-mm7v
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hr5v-j9h9-xjhg severity high https://github.com/advisories/GHSA-hr5v-j9h9-xjhg
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-j7p2-qcwm-94v4 severity high https://github.com/advisories/GHSA-j7p2-qcwm-94v4
- GHSA-jccr-rrw2-vc8h severity high https://github.com/advisories/GHSA-jccr-rrw2-vc8h
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jj82-76v6-933r severity high https://github.com/advisories/GHSA-jj82-76v6-933r
- GHSA-jq3f-vjww-8rq7 severity high https://github.com/advisories/GHSA-jq3f-vjww-8rq7
- GHSA-jq4x-98m3-ggq6 severity high https://github.com/advisories/GHSA-jq4x-98m3-ggq6
- GHSA-jr6x-2q95-fh2g severity high https://github.com/advisories/GHSA-jr6x-2q95-fh2g
- GHSA-jv6r-27ww-4gw4 severity high https://github.com/advisories/GHSA-jv6r-27ww-4gw4
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-jxrq-8fm4-9p58 severity high https://github.com/advisories/GHSA-jxrq-8fm4-9p58
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-m8v2-6wwh-r4gc severity high https://github.com/advisories/GHSA-m8v2-6wwh-r4gc
- GHSA-mfg5-7q5g-f37j severity high https://github.com/advisories/GHSA-mfg5-7q5g-f37j
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgrq-9f93-wpp5 severity high https://github.com/advisories/GHSA-mgrq-9f93-wpp5
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-mj4p-rc52-m843 severity high https://github.com/advisories/GHSA-mj4p-rc52-m843
- GHSA-mqr9-vqhq-3jxw severity high https://github.com/advisories/GHSA-mqr9-vqhq-3jxw
- GHSA-mwxv-35wr-4vvj severity high https://github.com/advisories/GHSA-mwxv-35wr-4vvj
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p4x4-2r7f-wjxg severity high https://github.com/advisories/GHSA-p4x4-2r7f-wjxg
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pj5x-38rw-6fph severity high https://github.com/advisories/GHSA-pj5x-38rw-6fph
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q399-23r3-hfx4 severity high https://github.com/advisories/GHSA-q399-23r3-hfx4
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qc36-x95h-7j53 severity high https://github.com/advisories/GHSA-qc36-x95h-7j53
- GHSA-qcc4-p59m-p54m severity high https://github.com/advisories/GHSA-qcc4-p59m-p54m
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qj22-xqjr-v83v severity high https://github.com/advisories/GHSA-qj22-xqjr-v83v
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qm2m-28pf-hgjw severity high https://github.com/advisories/GHSA-qm2m-28pf-hgjw
- GHSA-qm9x-v7cx-7rq4 severity high https://github.com/advisories/GHSA-qm9x-v7cx-7rq4
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r54r-wmmq-mh84 severity high https://github.com/advisories/GHSA-r54r-wmmq-mh84
- GHSA-r65x-2hqr-j5hf severity high https://github.com/advisories/GHSA-r65x-2hqr-j5hf
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r7vr-gr74-94p8 severity high https://github.com/advisories/GHSA-r7vr-gr74-94p8
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rchv-x836-w7xp severity high https://github.com/advisories/GHSA-rchv-x836-w7xp
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rhfg-j8jq-7v2h severity high https://github.com/advisories/GHSA-rhfg-j8jq-7v2h
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rqpp-rjj8-7wv8 severity critical https://github.com/advisories/GHSA-rqpp-rjj8-7wv8
- GHSA-rw39-5899-8mxp severity high https://github.com/advisories/GHSA-rw39-5899-8mxp
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-rxxp-482v-7mrh severity high https://github.com/advisories/GHSA-rxxp-482v-7mrh
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v3qc-wrwx-j3pw severity high https://github.com/advisories/GHSA-v3qc-wrwx-j3pw
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v865-p3gq-hw6m severity high https://github.com/advisories/GHSA-v865-p3gq-hw6m
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-v8wv-jg3q-qwpq severity high https://github.com/advisories/GHSA-v8wv-jg3q-qwpq
- GHSA-vffc-f7r7-rx2w severity high https://github.com/advisories/GHSA-vffc-f7r7-rx2w
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vfw7-6rhc-6xxg severity high https://github.com/advisories/GHSA-vfw7-6rhc-6xxg
- GHSA-vmhq-cqm9-6p7q severity high https://github.com/advisories/GHSA-vmhq-cqm9-6p7q
- GHSA-vpj2-69hf-rppw severity high https://github.com/advisories/GHSA-vpj2-69hf-rppw
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vvjh-f6p9-5vcf severity high https://github.com/advisories/GHSA-vvjh-f6p9-5vcf
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w235-x559-36mg severity high https://github.com/advisories/GHSA-w235-x559-36mg
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-w76h-8m22-hpgh severity high https://github.com/advisories/GHSA-w76h-8m22-hpgh
- GHSA-w7j5-j98m-w679 severity high https://github.com/advisories/GHSA-w7j5-j98m-w679
- GHSA-w9cg-v44m-4qv8 severity high https://github.com/advisories/GHSA-w9cg-v44m-4qv8
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wcxr-59v9-rxr8 severity high https://github.com/advisories/GHSA-wcxr-59v9-rxr8
- GHSA-wq58-2pvg-5h4f severity high https://github.com/advisories/GHSA-wq58-2pvg-5h4f
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x2ff-j5c2-ggpr severity high https://github.com/advisories/GHSA-x2ff-j5c2-ggpr
- GHSA-x82f-27x3-q89c severity high https://github.com/advisories/GHSA-x82f-27x3-q89c
- GHSA-x9cf-3w63-rpq9 severity high https://github.com/advisories/GHSA-x9cf-3w63-rpq9
- GHSA-xf99-j42q-5w5p severity high https://github.com/advisories/GHSA-xf99-j42q-5w5p
- GHSA-xgf2-vxv2-rrmg severity high https://github.com/advisories/GHSA-xgf2-vxv2-rrmg
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmv6-r34m-62p4 severity high https://github.com/advisories/GHSA-xmv6-r34m-62p4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xp9r-prpg-373r severity high https://github.com/advisories/GHSA-xp9r-prpg-373r
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-07

Verdict: exact
Version: 2026.3.28
Candidates: 2026.3.28
Files read: /srv/agents/claw-07/node_modules/openclaw/dist/.buildstamp
Matched files: dist/.buildstamp

matches 288 published advisories (5 critical, 110 high) as of 2026-09-11

Credential names: SLACK_BOT_TOKEN. credential reach is lab-tested only. Sources: /srv/agents/claw-07/.openclaw/openclaw.json, /srv/agents/claw-07/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-08

Verdict: exact
Version: 2026.3.28
Candidates: 2026.3.28
Files read: /workspace/claw-08/node_modules/openclaw/dist/.buildstamp
Matched files: dist/.buildstamp

matches 288 published advisories (5 critical, 110 high) as of 2026-09-11

Credential names: STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /workspace/claw-08/.openclaw/openclaw.json, /workspace/claw-08/.openclaw/mcp/extra.json, /workspace/claw-08/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-09

Verdict: exact
Version: 2026.3.28
Candidates: 2026.3.28
Files read: /app/claw-09/node_modules/openclaw/dist/.buildstamp
Matched files: dist/.buildstamp

matches 288 published advisories (5 critical, 110 high) as of 2026-09-11

Credential names: ANTHROPIC_API_KEY, AWS_ACCESS_KEY_ID. credential reach is lab-tested only. Sources: /app/claw-09/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3qpv-xf3v-mm45 severity high https://github.com/advisories/GHSA-3qpv-xf3v-mm45
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-57gh-m6rq-54cf severity high https://github.com/advisories/GHSA-57gh-m6rq-54cf
- GHSA-5cj2-3jr2-5h77 severity high https://github.com/advisories/GHSA-5cj2-3jr2-5h77
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7ggg-pvrf-458v severity high https://github.com/advisories/GHSA-7ggg-pvrf-458v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9jpj-g8vv-j5mf severity high https://github.com/advisories/GHSA-9jpj-g8vv-j5mf
- GHSA-9p3r-hh9g-5cmg severity critical https://github.com/advisories/GHSA-9p3r-hh9g-5cmg
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-cg7q-fg22-4g98 severity high https://github.com/advisories/GHSA-cg7q-fg22-4g98
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwf8-44x6-32c2 severity high https://github.com/advisories/GHSA-cwf8-44x6-32c2
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-fv94-qvg8-xqpw severity high https://github.com/advisories/GHSA-fv94-qvg8-xqpw
- GHSA-g374-mggx-p6xc severity high https://github.com/advisories/GHSA-g374-mggx-p6xc
- GHSA-g5cg-8x5w-7jpm severity critical https://github.com/advisories/GHSA-g5cg-8x5w-7jpm
- GHSA-g8xp-qx39-9jq9 severity high https://github.com/advisories/GHSA-g8xp-qx39-9jq9
- GHSA-gfmx-pph7-g46x severity high https://github.com/advisories/GHSA-gfmx-pph7-g46x
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-gjm7-hw8f-73rq severity high https://github.com/advisories/GHSA-gjm7-hw8f-73rq
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jf56-mccx-5f3f severity high https://github.com/advisories/GHSA-jf56-mccx-5f3f
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p464-m8x6-vhv8 severity high https://github.com/advisories/GHSA-p464-m8x6-vhv8
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-q9w8-cf67-r238 severity high https://github.com/advisories/GHSA-q9w8-cf67-r238
- GHSA-qcj9-wwgw-6gm8 severity high https://github.com/advisories/GHSA-qcj9-wwgw-6gm8
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xj9w-5r6q-x6v4 severity high https://github.com/advisories/GHSA-xj9w-5r6q-x6v4
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-10

Verdict: range
Version: 
Candidates: 2026.4.7-1, 2026.4.8
Files read: /var/lib/claw/claw-10/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 222 published advisories (3 critical, 97 high) as of 2026-09-11

Credential names: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY. credential reach is lab-tested only. Sources: /var/lib/claw/claw-10/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2gvc-4f3c-2855 severity high https://github.com/advisories/GHSA-2gvc-4f3c-2855
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm applies_to 2026.4.7-1
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-736r-jwj6-4w23 severity high https://github.com/advisories/GHSA-736r-jwj6-4w23
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw applies_to 2026.4.7-1
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m applies_to 2026.4.7-1
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-11

Verdict: range
Version: 
Candidates: 2026.4.7-1, 2026.4.8
Files read: /opt/apps/claw-11/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 222 published advisories (3 critical, 97 high) as of 2026-09-11

Credential names: AWS_SECRET_ACCESS_KEY, DISCORD_BOT_TOKEN. credential reach is lab-tested only. Sources: /opt/apps/claw-11/.openclaw/openclaw.json, /opt/apps/claw-11/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2gvc-4f3c-2855 severity high https://github.com/advisories/GHSA-2gvc-4f3c-2855
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm applies_to 2026.4.7-1
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-736r-jwj6-4w23 severity high https://github.com/advisories/GHSA-736r-jwj6-4w23
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw applies_to 2026.4.7-1
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m applies_to 2026.4.7-1
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-12

Verdict: range
Version: 
Candidates: 2026.4.7-1, 2026.4.8
Files read: /home/node/work/claw-12/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 222 published advisories (3 critical, 97 high) as of 2026-09-11

Credential names: DISCORD_BOT_TOKEN, GITHUB_PERSONAL_ACCESS_TOKEN. credential reach is lab-tested only. Sources: /home/node/work/claw-12/.openclaw/openclaw.json, /home/node/work/claw-12/.openclaw/mcp/extra.json, /home/node/work/claw-12/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2gvc-4f3c-2855 severity high https://github.com/advisories/GHSA-2gvc-4f3c-2855
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm applies_to 2026.4.7-1
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-736r-jwj6-4w23 severity high https://github.com/advisories/GHSA-736r-jwj6-4w23
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw applies_to 2026.4.7-1
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m applies_to 2026.4.7-1
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-13

Verdict: range
Version: 
Candidates: 2026.4.7-1, 2026.4.8
Files read: /srv/agents/claw-13/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 222 published advisories (3 critical, 97 high) as of 2026-09-11

Credential names: GITHUB_PERSONAL_ACCESS_TOKEN, OPENAI_API_KEY, SLACK_BOT_TOKEN. credential reach is lab-tested only. Sources: /srv/agents/claw-13/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2cq5-mf3v-mx44 severity high https://github.com/advisories/GHSA-2cq5-mf3v-mx44
- GHSA-2gvc-4f3c-2855 severity high https://github.com/advisories/GHSA-2gvc-4f3c-2855
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-525j-hqq2-66r4 severity high https://github.com/advisories/GHSA-525j-hqq2-66r4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-5wj5-87vq-39xm severity high https://github.com/advisories/GHSA-5wj5-87vq-39xm applies_to 2026.4.7-1
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-66r7-m7xm-v49h severity high https://github.com/advisories/GHSA-66r7-m7xm-v49h
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-736r-jwj6-4w23 severity high https://github.com/advisories/GHSA-736r-jwj6-4w23
- GHSA-7437-7hg8-frrw severity high https://github.com/advisories/GHSA-7437-7hg8-frrw applies_to 2026.4.7-1
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-7jp6-r74r-995q severity high https://github.com/advisories/GHSA-7jp6-r74r-995q
- GHSA-82qx-6vj7-p8m2 severity high https://github.com/advisories/GHSA-82qx-6vj7-p8m2
- GHSA-8372-7vhw-cm6q severity high https://github.com/advisories/GHSA-8372-7vhw-cm6q
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-939r-rj45-g2rj severity high https://github.com/advisories/GHSA-939r-rj45-g2rj
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-qx8j-g322-qj6m severity high https://github.com/advisories/GHSA-qx8j-g322-qj6m applies_to 2026.4.7-1
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vfp4-8x56-j7c5 severity high https://github.com/advisories/GHSA-vfp4-8x56-j7c5
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xh72-v6v9-mwhc severity critical https://github.com/advisories/GHSA-xh72-v6v9-mwhc
- GHSA-xmxx-7p24-h892 severity critical https://github.com/advisories/GHSA-xmxx-7p24-h892
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-14

Verdict: exact
Version: 2026.4.15
Candidates: 2026.4.15
Files read: /workspace/claw-14/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 169 published advisories (1 critical, 86 high) as of 2026-09-11

Credential names: OPENAI_API_KEY, SLACK_BOT_TOKEN, STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /workspace/claw-14/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-15

Verdict: exact
Version: 2026.4.15
Candidates: 2026.4.15
Files read: /app/claw-15/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 169 published advisories (1 critical, 86 high) as of 2026-09-11

Credential names: ANTHROPIC_API_KEY, SLACK_BOT_TOKEN, STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /app/claw-15/.openclaw/openclaw.json, /app/claw-15/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-16

Verdict: exact
Version: 2026.4.15
Candidates: 2026.4.15
Files read: /var/lib/claw/claw-16/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 169 published advisories (1 critical, 86 high) as of 2026-09-11

Credential names: ANTHROPIC_API_KEY, AWS_ACCESS_KEY_ID, STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /var/lib/claw/claw-16/.openclaw/openclaw.json, /var/lib/claw/claw-16/.openclaw/mcp/extra.json, /var/lib/claw/claw-16/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-hxvm-xjvf-93f3 severity high https://github.com/advisories/GHSA-hxvm-xjvf-93f3
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-17

Verdict: exact
Version: 2026.4.20
Candidates: 2026.4.20
Files read: /opt/apps/claw-17/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /opt/apps/claw-17/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-18

Verdict: exact
Version: 2026.4.20
Candidates: 2026.4.20
Files read: /home/node/work/claw-18/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /home/node/work/claw-18/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-19

Verdict: exact
Version: 2026.4.20
Candidates: 2026.4.20
Files read: /srv/agents/claw-19/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /srv/agents/claw-19/.openclaw/openclaw.json, /srv/agents/claw-19/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-20

Verdict: exact
Version: 2026.4.21
Candidates: 2026.4.21
Files read: /workspace/claw-20/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: (none). credential reach is lab-tested only. Sources: /workspace/claw-20/.openclaw/openclaw.json, /workspace/claw-20/.openclaw/mcp/extra.json, /workspace/claw-20/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-21

Verdict: exact
Version: 2026.4.21
Candidates: 2026.4.21
Files read: /app/claw-21/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: GITHUB_PERSONAL_ACCESS_TOKEN. credential reach is lab-tested only. Sources: /app/claw-21/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-22

Verdict: exact
Version: 2026.4.21
Candidates: 2026.4.21
Files read: /var/lib/claw/claw-22/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 157 published advisories (1 critical, 85 high) as of 2026-09-11

Credential names: OPENAI_API_KEY. credential reach is lab-tested only. Sources: /var/lib/claw/claw-22/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r6xh-pqhr-v4xh severity high https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-23

Verdict: exact
Version: 2026.4.22
Candidates: 2026.4.22
Files read: /opt/apps/claw-23/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 148 published advisories (1 critical, 84 high) as of 2026-09-11

Credential names: SLACK_BOT_TOKEN. credential reach is lab-tested only. Sources: /opt/apps/claw-23/.openclaw/openclaw.json, /opt/apps/claw-23/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-24

Verdict: exact
Version: 2026.4.22
Candidates: 2026.4.22
Files read: /home/node/work/claw-24/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 148 published advisories (1 critical, 84 high) as of 2026-09-11

Credential names: STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /home/node/work/claw-24/.openclaw/openclaw.json, /home/node/work/claw-24/.openclaw/mcp/extra.json, /home/node/work/claw-24/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-25

Verdict: exact
Version: 2026.4.22
Candidates: 2026.4.22
Files read: /srv/agents/claw-25/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 148 published advisories (1 critical, 84 high) as of 2026-09-11

Credential names: ANTHROPIC_API_KEY, AWS_ACCESS_KEY_ID. credential reach is lab-tested only. Sources: /srv/agents/claw-25/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-cwj3-vqpp-pmxr severity high https://github.com/advisories/GHSA-cwj3-vqpp-pmxr
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r39h-4c2p-3jxp severity high https://github.com/advisories/GHSA-r39h-4c2p-3jxp
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-26

Verdict: exact
Version: 2026.4.23
Candidates: 2026.4.23
Files read: /workspace/claw-26/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 146 published advisories (1 critical, 82 high) as of 2026-09-11

Credential names: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY. credential reach is lab-tested only. Sources: /workspace/claw-26/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-27

Verdict: exact
Version: 2026.4.23
Candidates: 2026.4.23
Files read: /app/claw-27/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

matches 146 published advisories (1 critical, 82 high) as of 2026-09-11

Credential names: AWS_SECRET_ACCESS_KEY, DISCORD_BOT_TOKEN. credential reach is lab-tested only. Sources: /app/claw-27/.openclaw/openclaw.json, /app/claw-27/.mcp.json.
auto_approve: true
mcp_servers: github, slack

Critical and high advisories:

- GHSA-24vr-rprv-67rf severity high https://github.com/advisories/GHSA-24vr-rprv-67rf
- GHSA-2j8v-hwgc-x698 severity high https://github.com/advisories/GHSA-2j8v-hwgc-x698
- GHSA-2x93-h3hg-2xfp severity high https://github.com/advisories/GHSA-2x93-h3hg-2xfp
- GHSA-34mr-7r3m-gfg7 severity high https://github.com/advisories/GHSA-34mr-7r3m-gfg7
- GHSA-3c6j-hq33-3jv4 severity high https://github.com/advisories/GHSA-3c6j-hq33-3jv4
- GHSA-3fp5-v549-9v66 severity high https://github.com/advisories/GHSA-3fp5-v549-9v66
- GHSA-3mq7-q27j-mq7q severity high https://github.com/advisories/GHSA-3mq7-q27j-mq7q
- GHSA-3x84-qq85-fj65 severity high https://github.com/advisories/GHSA-3x84-qq85-fj65
- GHSA-4pqj-3c56-5fqq severity high https://github.com/advisories/GHSA-4pqj-3c56-5fqq
- GHSA-4r25-35qc-fr6j severity high https://github.com/advisories/GHSA-4r25-35qc-fr6j
- GHSA-4wvr-f35r-f8w4 severity high https://github.com/advisories/GHSA-4wvr-f35r-f8w4
- GHSA-575v-8hfq-m3mc severity high https://github.com/advisories/GHSA-575v-8hfq-m3mc
- GHSA-5mrc-77hj-xjxv severity high https://github.com/advisories/GHSA-5mrc-77hj-xjxv
- GHSA-62qm-6fjj-6g23 severity high https://github.com/advisories/GHSA-62qm-6fjj-6g23
- GHSA-6fvr-66p3-3qj4 severity high https://github.com/advisories/GHSA-6fvr-66p3-3qj4
- GHSA-724r-v4wf-mqc5 severity high https://github.com/advisories/GHSA-724r-v4wf-mqc5
- GHSA-74gc-hg2m-79p9 severity high https://github.com/advisories/GHSA-74gc-hg2m-79p9
- GHSA-77pv-3w4q-vrj5 severity high https://github.com/advisories/GHSA-77pv-3w4q-vrj5
- GHSA-77q5-rr5v-x43q severity high https://github.com/advisories/GHSA-77q5-rr5v-x43q
- GHSA-7cp7-87pj-p32v severity high https://github.com/advisories/GHSA-7cp7-87pj-p32v
- GHSA-7hxm-f538-3xp6 severity high https://github.com/advisories/GHSA-7hxm-f538-3xp6
- GHSA-8c59-hr4w-qg69 severity high https://github.com/advisories/GHSA-8c59-hr4w-qg69
- GHSA-8f46-3xx3-8c9m severity high https://github.com/advisories/GHSA-8f46-3xx3-8c9m
- GHSA-8v95-qqcm-qp9h severity high https://github.com/advisories/GHSA-8v95-qqcm-qp9h
- GHSA-8wg3-5mcm-fjq8 severity high https://github.com/advisories/GHSA-8wg3-5mcm-fjq8
- GHSA-8xxh-v4vc-qvm4 severity high https://github.com/advisories/GHSA-8xxh-v4vc-qvm4
- GHSA-9969-8g9h-rxwm severity high https://github.com/advisories/GHSA-9969-8g9h-rxwm
- GHSA-9f86-pvv5-rxfw severity high https://github.com/advisories/GHSA-9f86-pvv5-rxfw
- GHSA-9p6m-2872-xm7x severity high https://github.com/advisories/GHSA-9p6m-2872-xm7x
- GHSA-9x88-f7rh-4c83 severity high https://github.com/advisories/GHSA-9x88-f7rh-4c83
- GHSA-c29c-2q9c-pc86 severity high https://github.com/advisories/GHSA-c29c-2q9c-pc86
- GHSA-ccwh-wwpp-6wg5 severity high https://github.com/advisories/GHSA-ccwh-wwpp-6wg5
- GHSA-cf2p-f286-mphf severity high https://github.com/advisories/GHSA-cf2p-f286-mphf
- GHSA-chr9-m4q2-76hw severity high https://github.com/advisories/GHSA-chr9-m4q2-76hw
- GHSA-crg9-c62w-j2p5 severity high https://github.com/advisories/GHSA-crg9-c62w-j2p5
- GHSA-cw4q-gqg5-g38h severity high https://github.com/advisories/GHSA-cw4q-gqg5-g38h
- GHSA-f397-5vjw-v2c2 severity high https://github.com/advisories/GHSA-f397-5vjw-v2c2
- GHSA-f6p7-6326-vf7v severity high https://github.com/advisories/GHSA-f6p7-6326-vf7v
- GHSA-fh38-965w-f6c3 severity high https://github.com/advisories/GHSA-fh38-965w-f6c3
- GHSA-fq9j-vw4w-fr6v severity high https://github.com/advisories/GHSA-fq9j-vw4w-fr6v
- GHSA-ghpx-6xwq-2w4w severity high https://github.com/advisories/GHSA-ghpx-6xwq-2w4w
- GHSA-hjr6-g723-hmfm severity high https://github.com/advisories/GHSA-hjr6-g723-hmfm
- GHSA-hpg5-cq3m-phqp severity high https://github.com/advisories/GHSA-hpg5-cq3m-phqp
- GHSA-hw9r-h9mr-4jff severity high https://github.com/advisories/GHSA-hw9r-h9mr-4jff
- GHSA-hx85-fgcw-9vrc severity high https://github.com/advisories/GHSA-hx85-fgcw-9vrc
- GHSA-j472-gf56-x589 severity high https://github.com/advisories/GHSA-j472-gf56-x589
- GHSA-jghr-xp78-995p severity high https://github.com/advisories/GHSA-jghr-xp78-995p
- GHSA-jhfx-v2j8-x3m6 severity high https://github.com/advisories/GHSA-jhfx-v2j8-x3m6
- GHSA-jvm4-4j77-39p6 severity high https://github.com/advisories/GHSA-jvm4-4j77-39p6
- GHSA-m38g-vpwj-mpg9 severity high https://github.com/advisories/GHSA-m38g-vpwj-mpg9
- GHSA-mgq6-vr84-7m2j severity high https://github.com/advisories/GHSA-mgq6-vr84-7m2j
- GHSA-mgvr-6gvw-3rgr severity high https://github.com/advisories/GHSA-mgvr-6gvw-3rgr
- GHSA-mhq8-78pj-5j79 severity high https://github.com/advisories/GHSA-mhq8-78pj-5j79
- GHSA-p3h6-v2h4-36q2 severity high https://github.com/advisories/GHSA-p3h6-v2h4-36q2
- GHSA-p5g8-m35v-7m82 severity high https://github.com/advisories/GHSA-p5g8-m35v-7m82
- GHSA-p5xh-frrh-cmgj severity high https://github.com/advisories/GHSA-p5xh-frrh-cmgj
- GHSA-p73f-w79w-jqr5 severity high https://github.com/advisories/GHSA-p73f-w79w-jqr5
- GHSA-pjjr-5qhr-5w6r severity high https://github.com/advisories/GHSA-pjjr-5qhr-5w6r
- GHSA-q7q8-3mgw-q67r severity high https://github.com/advisories/GHSA-q7q8-3mgw-q67r
- GHSA-q99w-vh6v-q3v7 severity high https://github.com/advisories/GHSA-q99w-vh6v-q3v7
- GHSA-qgj5-6x35-9g6f severity high https://github.com/advisories/GHSA-qgj5-6x35-9g6f
- GHSA-qjpc-qf9m-xwmr severity high https://github.com/advisories/GHSA-qjpc-qf9m-xwmr
- GHSA-qw7m-h363-33qw severity high https://github.com/advisories/GHSA-qw7m-h363-33qw
- GHSA-r88x-r7jj-f2cf severity high https://github.com/advisories/GHSA-r88x-r7jj-f2cf
- GHSA-rggc-m335-3wvj severity high https://github.com/advisories/GHSA-rggc-m335-3wvj
- GHSA-rh6r-vvfc-86jq severity high https://github.com/advisories/GHSA-rh6r-vvfc-86jq
- GHSA-rjxq-qqhf-8hwh severity high https://github.com/advisories/GHSA-rjxq-qqhf-8hwh
- GHSA-rx78-29qr-5hq8 severity high https://github.com/advisories/GHSA-rx78-29qr-5hq8
- GHSA-v2ww-5rh7-2h5v severity high https://github.com/advisories/GHSA-v2ww-5rh7-2h5v
- GHSA-v6r2-jh58-xx6w severity high https://github.com/advisories/GHSA-v6r2-jh58-xx6w
- GHSA-v8cx-933x-r976 severity high https://github.com/advisories/GHSA-v8cx-933x-r976
- GHSA-vr7j-7684-7gm5 severity high https://github.com/advisories/GHSA-vr7j-7684-7gm5
- GHSA-vxx3-6hc9-7cc3 severity high https://github.com/advisories/GHSA-vxx3-6hc9-7cc3
- GHSA-w4v6-g3wm-w36c severity critical https://github.com/advisories/GHSA-w4v6-g3wm-w36c
- GHSA-w5ww-7chg-mxcq severity high https://github.com/advisories/GHSA-w5ww-7chg-mxcq
- GHSA-wc84-j36w-pw4x severity high https://github.com/advisories/GHSA-wc84-j36w-pw4x
- GHSA-wwcw-jfpp-gpxw severity high https://github.com/advisories/GHSA-wwcw-jfpp-gpxw
- GHSA-wwx7-573h-pqwc severity high https://github.com/advisories/GHSA-wwx7-573h-pqwc
- GHSA-wxh3-g47h-q3mc severity high https://github.com/advisories/GHSA-wxh3-g47h-q3mc
- GHSA-wxm8-ghhq-q688 severity high https://github.com/advisories/GHSA-wxm8-ghhq-q688
- GHSA-x863-pqjw-hmgf severity high https://github.com/advisories/GHSA-x863-pqjw-hmgf
- GHSA-xr4f-mjxj-w6w5 severity high https://github.com/advisories/GHSA-xr4f-mjxj-w6w5
- GHSA-xww8-gqvh-92x9 severity high https://github.com/advisories/GHSA-xww8-gqvh-92x9

### claw-28

Verdict: exact
Version: 2026.10.4
Candidates: 2026.10.4
Files read: /var/lib/claw/claw-28/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

no published advisory as of 2026-09-11

Credential names: DISCORD_BOT_TOKEN, GITHUB_PERSONAL_ACCESS_TOKEN. credential reach is lab-tested only. Sources: /var/lib/claw/claw-28/.openclaw/openclaw.json, /var/lib/claw/claw-28/.openclaw/mcp/extra.json, /var/lib/claw/claw-28/.mcp.json.
auto_approve: false
mcp_servers: filesystem, github, slack

Critical and high advisories:

(none)

### claw-29

Verdict: exact
Version: 2026.10.4
Candidates: 2026.10.4
Files read: /opt/apps/claw-29/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

no published advisory as of 2026-09-11

Credential names: GITHUB_PERSONAL_ACCESS_TOKEN, OPENAI_API_KEY, SLACK_BOT_TOKEN. credential reach is lab-tested only. Sources: /opt/apps/claw-29/.openclaw/openclaw.json.
auto_approve: true
mcp_servers: (none)

Critical and high advisories:

(none)

### claw-30

Verdict: exact
Version: 2026.10.4
Candidates: 2026.10.4
Files read: /home/node/work/claw-30/node_modules/openclaw/dist/abort.runtime.js
Matched files: dist/abort.runtime.js

no published advisory as of 2026-09-11

Credential names: OPENAI_API_KEY, SLACK_BOT_TOKEN, STRIPE_SECRET_KEY. credential reach is lab-tested only. Sources: /home/node/work/claw-30/.openclaw/openclaw.json.
auto_approve: false
mcp_servers: github

Critical and high advisories:

(none)

## Method and limits

An install with matches is described as matches N published advisories (C critical, H high) as of the header feed_newest, using that install's advisory_count, critical, and high fields. An install with zero matches uses its advisory_note.

Credential reach is lab-tested only. The names were read from the planted lab paths listed in credential_sources. This report does not measure customer hosts.

This Agent 365 comparison is a local mock, and published-schema limits are cited in inputs/rea-narrower-gap/CLAIMS.md.

## Appendix

### claw-01 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-33rq-m5x2-fvgf
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fqr-4cg8-h96q
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3hcm-ggvf-rch5
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-4564-pvr2-qq4h
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-47q7-97xp-m272
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hg8-92x6-h2f3
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rj2-gpmh-qq5x
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56f2-hvwg-5743
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-5xfq-5mr7-426q
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-64qx-vpxx-mvqf
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-782p-5fr5-7fj8
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7rcp-mxpq-72pj
GHSA-7vwx-582j-j332
GHSA-7wv4-cc7p-jhxc
GHSA-7xhj-55q9-pc3m
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8jpq-5h99-ff5r
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mh7-phf8-xgfm
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-943q-mwmv-hhvh
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c37p-4qqg-3p76
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chm2-m3w2-wcxm
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cv7m-c9jx-vg7q
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fhvm-j76f-qmjv
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g27f-9qjv-22pm
GHSA-g2f6-pwvx-r275
GHSA-g34w-4xqq-h79m
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g6q9-8fvw-f7rf
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-gq9c-wg68-gwj2
GHSA-grc3-2j34-p6gm
GHSA-gv46-4xfq-jv58
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3f9-mjwj-w476
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h89v-j3x9-8wqj
GHSA-h97f-6pqj-q452
GHSA-h9g4-589h-68xv
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hv93-r4j3-q65f
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j27p-hq53-9wgc
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jfv4-h8mc-jcp8
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmm5-fvh5-gf4p
GHSA-jmmg-jqc7-5qf4
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jqpq-mgvm-f9r6
GHSA-jr6x-2q95-fh2g
GHSA-jrvc-8ff5-2f9f
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m7x8-2w3w-pr42
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mj5r-hh7j-4gxf
GHSA-mp5h-m6qj-6292
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqpw-46fh-299h
GHSA-mqr9-vqhq-3jxw
GHSA-mr32-vwc2-5j6h
GHSA-mv9j-6xhh-g383
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p25h-9q54-ffvw
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pchc-86f6-8758
GHSA-pfv7-rr5m-qmv6
GHSA-pg2v-8xwh-qhcc
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pv58-549p-qh99
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q447-rj3r-2cgh
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qj77-c3c8-9c3q
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qrq5-wjgg-rvqw
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qw99-grcx-4pvm
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r5fq-947m-xm57
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r8g4-86fx-92mq
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rmxw-jxxx-4cpc
GHSA-rq6g-px6m-c248
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rv39-79c4-7459
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rwj8-p9vq-25gv
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6c6-vqqg-w888
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v773-r54f-q32w
GHSA-v865-p3gq-hw6m
GHSA-v892-hwpg-jwqp
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w2cg-vxx6-5xjg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5c7-9qqw-6645
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wfp2-v9c7-fh79
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x22m-j5qq-j49m
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xc7w-v5x6-cc87
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvhf-x56f-2hpp
GHSA-xvx8-77m6-gwg6
GHSA-xw4p-pw82-hqr7
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xwjm-j929-xq7c
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-02 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-33rq-m5x2-fvgf
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fqr-4cg8-h96q
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3hcm-ggvf-rch5
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-4564-pvr2-qq4h
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-47q7-97xp-m272
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hg8-92x6-h2f3
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rj2-gpmh-qq5x
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56f2-hvwg-5743
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-5xfq-5mr7-426q
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-64qx-vpxx-mvqf
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-782p-5fr5-7fj8
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7rcp-mxpq-72pj
GHSA-7vwx-582j-j332
GHSA-7wv4-cc7p-jhxc
GHSA-7xhj-55q9-pc3m
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8jpq-5h99-ff5r
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mh7-phf8-xgfm
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-943q-mwmv-hhvh
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c37p-4qqg-3p76
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chm2-m3w2-wcxm
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cv7m-c9jx-vg7q
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fhvm-j76f-qmjv
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g27f-9qjv-22pm
GHSA-g2f6-pwvx-r275
GHSA-g34w-4xqq-h79m
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g6q9-8fvw-f7rf
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-gq9c-wg68-gwj2
GHSA-grc3-2j34-p6gm
GHSA-gv46-4xfq-jv58
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3f9-mjwj-w476
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h89v-j3x9-8wqj
GHSA-h97f-6pqj-q452
GHSA-h9g4-589h-68xv
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hv93-r4j3-q65f
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j27p-hq53-9wgc
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jfv4-h8mc-jcp8
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmm5-fvh5-gf4p
GHSA-jmmg-jqc7-5qf4
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jqpq-mgvm-f9r6
GHSA-jr6x-2q95-fh2g
GHSA-jrvc-8ff5-2f9f
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m7x8-2w3w-pr42
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mj5r-hh7j-4gxf
GHSA-mp5h-m6qj-6292
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqpw-46fh-299h
GHSA-mqr9-vqhq-3jxw
GHSA-mr32-vwc2-5j6h
GHSA-mv9j-6xhh-g383
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p25h-9q54-ffvw
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pchc-86f6-8758
GHSA-pfv7-rr5m-qmv6
GHSA-pg2v-8xwh-qhcc
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pv58-549p-qh99
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q447-rj3r-2cgh
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qj77-c3c8-9c3q
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qrq5-wjgg-rvqw
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qw99-grcx-4pvm
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r5fq-947m-xm57
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r8g4-86fx-92mq
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rmxw-jxxx-4cpc
GHSA-rq6g-px6m-c248
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rv39-79c4-7459
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rwj8-p9vq-25gv
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6c6-vqqg-w888
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v773-r54f-q32w
GHSA-v865-p3gq-hw6m
GHSA-v892-hwpg-jwqp
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w2cg-vxx6-5xjg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5c7-9qqw-6645
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wfp2-v9c7-fh79
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x22m-j5qq-j49m
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xc7w-v5x6-cc87
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvhf-x56f-2hpp
GHSA-xvx8-77m6-gwg6
GHSA-xw4p-pw82-hqr7
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xwjm-j929-xq7c
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-03 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-33rq-m5x2-fvgf
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fqr-4cg8-h96q
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3hcm-ggvf-rch5
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-4564-pvr2-qq4h
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-47q7-97xp-m272
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hg8-92x6-h2f3
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rj2-gpmh-qq5x
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56f2-hvwg-5743
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-5xfq-5mr7-426q
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-64qx-vpxx-mvqf
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-782p-5fr5-7fj8
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7rcp-mxpq-72pj
GHSA-7vwx-582j-j332
GHSA-7wv4-cc7p-jhxc
GHSA-7xhj-55q9-pc3m
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8jpq-5h99-ff5r
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mh7-phf8-xgfm
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-943q-mwmv-hhvh
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c37p-4qqg-3p76
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chm2-m3w2-wcxm
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cv7m-c9jx-vg7q
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fhvm-j76f-qmjv
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g27f-9qjv-22pm
GHSA-g2f6-pwvx-r275
GHSA-g34w-4xqq-h79m
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g6q9-8fvw-f7rf
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-gq9c-wg68-gwj2
GHSA-grc3-2j34-p6gm
GHSA-gv46-4xfq-jv58
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3f9-mjwj-w476
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h89v-j3x9-8wqj
GHSA-h97f-6pqj-q452
GHSA-h9g4-589h-68xv
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hv93-r4j3-q65f
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j27p-hq53-9wgc
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jfv4-h8mc-jcp8
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmm5-fvh5-gf4p
GHSA-jmmg-jqc7-5qf4
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jqpq-mgvm-f9r6
GHSA-jr6x-2q95-fh2g
GHSA-jrvc-8ff5-2f9f
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m7x8-2w3w-pr42
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mj5r-hh7j-4gxf
GHSA-mp5h-m6qj-6292
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqpw-46fh-299h
GHSA-mqr9-vqhq-3jxw
GHSA-mr32-vwc2-5j6h
GHSA-mv9j-6xhh-g383
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p25h-9q54-ffvw
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pchc-86f6-8758
GHSA-pfv7-rr5m-qmv6
GHSA-pg2v-8xwh-qhcc
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pv58-549p-qh99
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q447-rj3r-2cgh
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qj77-c3c8-9c3q
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qrq5-wjgg-rvqw
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qw99-grcx-4pvm
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r5fq-947m-xm57
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r8g4-86fx-92mq
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rmxw-jxxx-4cpc
GHSA-rq6g-px6m-c248
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rv39-79c4-7459
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rwj8-p9vq-25gv
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6c6-vqqg-w888
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v773-r54f-q32w
GHSA-v865-p3gq-hw6m
GHSA-v892-hwpg-jwqp
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w2cg-vxx6-5xjg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5c7-9qqw-6645
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wfp2-v9c7-fh79
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x22m-j5qq-j49m
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xc7w-v5x6-cc87
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvhf-x56f-2hpp
GHSA-xvx8-77m6-gwg6
GHSA-xw4p-pw82-hqr7
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xwjm-j929-xq7c
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-04 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2858-xg23-26fp
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hmj-39m8-jwc7
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7wv4-cc7p-jhxc
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g2f6-pwvx-r275
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-grc3-2j34-p6gm
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h97f-6pqj-q452
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmmg-jqc7-5qf4
GHSA-jp4j-q5fc-58gv
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jr6x-2q95-fh2g
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqr9-vqhq-3jxw
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pfv7-rr5m-qmv6
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qf48-qfv4-jjm9
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v865-p3gq-hw6m
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2g4-7mj7-2hhj
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvx8-77m6-gwg6
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-05 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2858-xg23-26fp
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hmj-39m8-jwc7
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7wv4-cc7p-jhxc
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g2f6-pwvx-r275
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-grc3-2j34-p6gm
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h97f-6pqj-q452
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmmg-jqc7-5qf4
GHSA-jp4j-q5fc-58gv
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jr6x-2q95-fh2g
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqr9-vqhq-3jxw
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pfv7-rr5m-qmv6
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qf48-qfv4-jjm9
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v865-p3gq-hw6m
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2g4-7mj7-2hhj
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvx8-77m6-gwg6
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-06 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25gx-x37c-7pph
GHSA-25pw-4h6w-qwvm
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-27cr-4p5m-74rj
GHSA-2858-xg23-26fp
GHSA-2ch6-x3g4-7759
GHSA-2f7j-rp58-mr42
GHSA-2fgq-7j6h-9rm4
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2hm8-rqrm-xfjq
GHSA-2j8v-hwgc-x698
GHSA-2mc2-g238-722j
GHSA-2pr2-hcv6-7gwv
GHSA-2prf-9cw7-fq62
GHSA-2qj5-gwg2-xwc4
GHSA-2qrv-rc5x-2g2h
GHSA-2rgf-hm63-5qph
GHSA-2rqg-gjgv-84jm
GHSA-2w79-r9g8-wmcr
GHSA-2ww6-868g-2c56
GHSA-2x4x-cc5g-qmmg
GHSA-2xcp-x87w-q377
GHSA-3298-56p6-rpw2
GHSA-33hm-cq8r-wc49
GHSA-34mr-7r3m-gfg7
GHSA-354r-7mfh-7rh2
GHSA-36h3-7c54-j27r
GHSA-37gc-85xm-2ww6
GHSA-37v6-fxx8-xjmx
GHSA-392f-ggf5-fp3c
GHSA-39hf-qg99-f4qv
GHSA-39mp-545q-w789
GHSA-39pp-xp36-q6mg
GHSA-3c6h-g97w-fg78
GHSA-3c6j-hq33-3jv4
GHSA-3cvx-236h-m9fj
GHSA-3cw3-5vxw-g2h3
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3h2q-j2v4-6w5r
GHSA-3h52-cx59-c456
GHSA-3jx4-q2m7-r496
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3pxq-f3cp-jmxp
GHSA-3q42-xmxv-9vfr
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3w6x-gv34-mqpf
GHSA-3wqp-prf6-2m72
GHSA-3x3x-h76w-hp98
GHSA-3x84-qq85-fj65
GHSA-3xfw-4pmr-4xc5
GHSA-3xv9-89fm-7h4r
GHSA-42mx-vp8m-j7qh
GHSA-43x4-g22p-3hrq
GHSA-45cg-2683-gfmq
GHSA-4685-c5cp-vp95
GHSA-474h-prjg-mmw3
GHSA-48vw-m3qc-wr99
GHSA-48wf-g7cp-gr3m
GHSA-49cg-279w-m73x
GHSA-4cqv-h74h-93j4
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4gc7-qcvf-38wg
GHSA-4hmj-39m8-jwc7
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4jpw-hj22-2xmc
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4qwc-c7g9-4xcw
GHSA-4r25-35qc-fr6j
GHSA-4rqq-w8v4-7p47
GHSA-4w7m-58cg-cmff
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-52q4-3xjc-6778
GHSA-534w-2vm4-89xr
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-56pc-6hvp-4gv4
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-5847-rm3g-23mw
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5f9p-f3w2-fwch
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5ghc-98wh-gwwf
GHSA-5gj7-jf77-q2q2
GHSA-5h2c-8v84-qpvr
GHSA-5h2w-qmfp-ggp6
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5jvj-hxmh-6h6j
GHSA-5m4g-88rg-69pj
GHSA-5m9r-p9g7-679c
GHSA-5mx2-2mgw-x8rm
GHSA-5r8f-96gm-5j6g
GHSA-5rx7-34fw-64qg
GHSA-5v6x-rfc3-7qfr
GHSA-5wcw-8jjv-m286
GHSA-5wj5-87vq-39xm
GHSA-62f6-mrcj-v8h5
GHSA-6336-qqw9-v6x6
GHSA-63f5-hhc7-cx6p
GHSA-63mg-xp9j-jfcm
GHSA-659f-22xc-98f2
GHSA-65h8-27jh-q8wv
GHSA-65rx-fvh6-r4h2
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68f8-9mhj-h2mp
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6c9j-x93c-rw6j
GHSA-6fvr-66p3-3qj4
GHSA-6g25-pc82-vfwp
GHSA-6hf3-mhgc-cm65
GHSA-6j27-pc5c-m8w8
GHSA-6mgf-v5j7-45cr
GHSA-6mqc-jqh6-x8fc
GHSA-6p8r-6m93-557f
GHSA-6pfc-6m7w-m8fx
GHSA-6rcp-vxwf-3mfp
GHSA-6rmx-gvvg-vh6j
GHSA-6x2m-hqfw-hvpj
GHSA-6xg4-82hv-cp6f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-74wf-h43j-vvmj
GHSA-74xj-763f-264w
GHSA-767m-xrhc-fxm7
GHSA-77hf-7fqf-f227
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-77w2-crqv-cmv3
GHSA-792q-qw95-f446
GHSA-796m-2973-wc5q
GHSA-7977-c43c-xpwj
GHSA-7cp7-87pj-p32v
GHSA-7f4q-9rqh-x36p
GHSA-7fcc-cw49-xm78
GHSA-7ff8-xjh3-mgh6
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7h7g-x2px-94hj
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7jx5-9fjg-hp4m
GHSA-7qf6-h84j-8fq4
GHSA-7wv4-cc7p-jhxc
GHSA-7xmq-g46g-f8pv
GHSA-7xr2-q9vf-x4r5
GHSA-82g8-464f-2mv7
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-844j-xrrq-wgh4
GHSA-846p-hgpv-vphc
GHSA-8689-gm9g-jgr6
GHSA-877v-w3f5-3pcq
GHSA-8883-9w57-vwv6
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8cp7-rp8r-mg77
GHSA-8f46-3xx3-8c9m
GHSA-8fmp-37rc-p5g7
GHSA-8g75-q649-6pv6
GHSA-8j2w-6fmm-m587
GHSA-8j37-5w68-wj2g
GHSA-8j9w-9pm5-pv8m
GHSA-8jhh-jcqg-mj5p
GHSA-8m9v-xpgf-g99m
GHSA-8mf7-vv8w-hjr2
GHSA-8mg9-j9cf-54cj
GHSA-8mvx-p2r9-r375
GHSA-8rh7-6779-cjqq
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-94pw-c6m8-p9p9
GHSA-9528-x887-j2fp
GHSA-985f-72mj-8gf7
GHSA-9868-vxmx-w862
GHSA-98ch-45wp-ch47
GHSA-98hh-7ghg-x6rq
GHSA-9969-8g9h-rxwm
GHSA-99qw-6mr3-36qr
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f72-qcpw-2hxc
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9hjh-fr4f-gxc4
GHSA-9jpj-g8vv-j5mf
GHSA-9mph-4f7v-fmvh
GHSA-9p38-94jf-hgjj
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9p93-7j67-5pc2
GHSA-9q2p-vc84-2rwm
GHSA-9q36-67vc-rrwg
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9vvh-2768-c8vp
GHSA-9wqx-g2cw-vc7r
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c6hr-w26q-c636
GHSA-ccg8-46r6-9qgj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cfp9-w5v9-3q4h
GHSA-cfvj-7rx7-fc7c
GHSA-cg6c-q2hx-69h7
GHSA-cg7q-fg22-4g98
GHSA-chf7-jq6g-qrwv
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cjv3-m589-v3rx
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-cxmw-p77q-wchg
GHSA-cxpw-2g23-2vgw
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f44p-c7w9-7xr7
GHSA-f5mf-3r52-r83w
GHSA-f693-58pc-2gfr
GHSA-f6h3-846h-2r8w
GHSA-f6p7-6326-vf7v
GHSA-f6pf-4gjx-c94r
GHSA-f7fh-qg34-x2xh
GHSA-f7ww-2725-qvw2
GHSA-f8mp-vj46-cq8v
GHSA-f8r2-vg7x-gh8m
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-ff98-w8hj-qrxf
GHSA-fg3m-vhrr-8gj6
GHSA-fgvx-58p6-gjwc
GHSA-fh32-73r9-rgh5
GHSA-fh3f-q9qw-93j9
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqcm-97m6-w7rm
GHSA-fqw4-mph7-2vr8
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g2f6-pwvx-r275
GHSA-g353-mgv3-8pcj
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g75x-8qqm-2vxp
GHSA-g7cr-9h7q-4qxq
GHSA-g86v-f9qv-rh6m
GHSA-g8xp-qx39-9jq9
GHSA-g99v-8hwm-g76g
GHSA-gcj7-r3hg-m7w6
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-gg9v-mgcp-v6m7
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp3q-wpq4-5c5h
GHSA-gp79-m99v-gjmh
GHSA-gq83-8q7q-9hfx
GHSA-grc3-2j34-p6gm
GHSA-gwqp-86q6-w47g
GHSA-gxg4-2rrr-jhc7
GHSA-h2v7-xc88-xx8c
GHSA-h3x4-hc5v-v2gm
GHSA-h4jx-hjr3-fhgc
GHSA-h5hg-h7rr-gpf3
GHSA-h656-5vcf-cm23
GHSA-h7f7-89mm-pqh6
GHSA-h97f-6pqj-q452
GHSA-h9xm-j4qg-fvpg
GHSA-hc5h-pmr3-3497
GHSA-hcm3-8f6r-6xwg
GHSA-hf68-49fm-59cq
GHSA-hff7-ccv5-52f8
GHSA-hfpr-jhpq-x4rm
GHSA-hggm-x7r9-mm7v
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hjvp-qhm6-wrh2
GHSA-hpg5-cq3m-phqp
GHSA-hr5v-j9h9-xjhg
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hwpq-rrpf-pgcq
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j26j-7qc4-3mrf
GHSA-j425-whc4-4jgc
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4c9-w69r-cw33
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j4xf-96qf-rx69
GHSA-j7p2-qcwm-94v4
GHSA-j9pv-rrcj-6pfx
GHSA-jccr-rrw2-vc8h
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jf6w-m8jw-jfxc
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jj82-76v6-933r
GHSA-jjgj-cpp9-cvpv
GHSA-jjw7-3vjf-fg5j
GHSA-jmmg-jqc7-5qf4
GHSA-jp4j-q5fc-58gv
GHSA-jq3f-vjww-8rq7
GHSA-jq4x-98m3-ggq6
GHSA-jr6x-2q95-fh2g
GHSA-jv6r-27ww-4gw4
GHSA-jvm4-4j77-39p6
GHSA-jwf4-8wf4-jf2m
GHSA-jwrq-8g5x-5fhm
GHSA-jxrq-8fm4-9p58
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m69h-jm2f-2pv8
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-m866-6qv5-p2fg
GHSA-m8v2-6wwh-r4gc
GHSA-mf5g-6r6f-ghhm
GHSA-mfg5-7q5g-f37j
GHSA-mgq6-vr84-7m2j
GHSA-mgrq-9f93-wpp5
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj4p-rc52-m843
GHSA-mj59-h3q9-ghfh
GHSA-mp66-rf4f-mhh8
GHSA-mpc8-jxjh-qpgh
GHSA-mqr9-vqhq-3jxw
GHSA-mw7w-g3mg-xqm7
GHSA-mwcg-wfq3-4gjc
GHSA-mwxv-35wr-4vvj
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p4x4-2r7f-wjxg
GHSA-p536-vvpp-9mc8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-p7gr-f84w-hqg5
GHSA-pfv7-rr5m-qmv6
GHSA-pj5x-38rw-6fph
GHSA-pjjr-5qhr-5w6r
GHSA-pjvx-rx66-r3fg
GHSA-ppwq-6v66-5m6j
GHSA-pw7h-9g6p-c378
GHSA-q2gc-xjqw-qp89
GHSA-q399-23r3-hfx4
GHSA-q3jj-46pq-826r
GHSA-q6qf-4p5j-r25g
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qc36-x95h-7j53
GHSA-qcc3-jqwp-5vh2
GHSA-qcc4-p59m-p54m
GHSA-qcj9-wwgw-6gm8
GHSA-qf48-qfv4-jjm9
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qhrr-grqp-6x2g
GHSA-qj22-xqjr-v83v
GHSA-qjpc-qf9m-xwmr
GHSA-qm2m-28pf-hgjw
GHSA-qm77-8qjp-4vcm
GHSA-qm9x-v7cx-7rq4
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qvr7-g57c-mrc7
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-qxgf-hmcj-3xw3
GHSA-r294-2894-92j3
GHSA-r39h-4c2p-3jxp
GHSA-r54r-wmmq-mh84
GHSA-r65x-2hqr-j5hf
GHSA-r6h2-5gqq-v5v6
GHSA-r6qf-8968-wj9q
GHSA-r6xh-pqhr-v4xh
GHSA-r7vr-gr74-94p8
GHSA-r88x-r7jj-f2cf
GHSA-r9q5-c7qc-p26w
GHSA-rchv-x836-w7xp
GHSA-rf6h-5gpw-qrgq
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rh6r-vvfc-86jq
GHSA-rhfg-j8jq-7v2h
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm2p-j3r7-4x4j
GHSA-rm45-4jx5-2927
GHSA-rm59-992w-x2mv
GHSA-rm5c-4rmf-vvhw
GHSA-rqp8-q22p-5j9q
GHSA-rqpp-rjj8-7wv8
GHSA-rv2q-f2h5-6xmg
GHSA-rvqr-hrcc-j9vv
GHSA-rvvf-6vh3-9j43
GHSA-rw39-5899-8mxp
GHSA-rx3g-mvc3-qfjf
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-rxxp-482v-7mrh
GHSA-v2v2-f783-358j
GHSA-v2ww-5rh7-2h5v
GHSA-v3j7-34xh-6g3w
GHSA-v3qc-wrwx-j3pw
GHSA-v6r2-jh58-xx6w
GHSA-v6x2-2qvm-6gv8
GHSA-v865-p3gq-hw6m
GHSA-v8cg-4474-49v8
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-v8wv-jg3q-qwpq
GHSA-vc32-h5mq-453v
GHSA-vcx4-4qxg-mfp4
GHSA-vffc-f7r7-rx2w
GHSA-vfg3-pqpq-93m4
GHSA-vfp4-8x56-j7c5
GHSA-vfw7-6rhc-6xxg
GHSA-vhpg-cq3w-v8p9
GHSA-vhwf-4x96-vqx2
GHSA-vj3g-5px3-gr46
GHSA-vjp8-wprm-2jw9
GHSA-vjx8-8p7h-82gr
GHSA-vmhq-cqm9-6p7q
GHSA-vmqr-rc7x-3446
GHSA-vpj2-69hf-rppw
GHSA-vqvg-86cc-cg83
GHSA-vqx8-9xxw-f2m7
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vr7j-g7jv-h5mp
GHSA-vvgp-4c28-m3jm
GHSA-vvjh-f6p9-5vcf
GHSA-vxx3-6hc9-7cc3
GHSA-w235-x559-36mg
GHSA-w45g-5746-x9fp
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6m8-cqvj-pg5v
GHSA-w6wx-jq6j-6mcj
GHSA-w76h-8m22-hpgh
GHSA-w7j5-j98m-w679
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9cg-v44m-4qv8
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-wcxr-59v9-rxr8
GHSA-wh94-p5m6-mr7j
GHSA-whf9-3hcx-gq54
GHSA-wj55-88gf-x564
GHSA-wjfv-5qch-m5vj
GHSA-wm8r-w8pf-2v6w
GHSA-wpc6-37g7-8q4w
GHSA-wpg9-4g4v-f9rc
GHSA-wpph-cjgr-7c39
GHSA-wppj-c6mr-83jj
GHSA-wq58-2pvg-5h4f
GHSA-wr6m-jg37-68xh
GHSA-wv26-j37q-2g7p
GHSA-wv46-v6xc-2qhf
GHSA-ww6v-v748-x7g9
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2cm-hg9c-mf5w
GHSA-x2ff-j5c2-ggpr
GHSA-x2g4-7mj7-2hhj
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x4vp-4235-65hg
GHSA-x629-46cc-7xgw
GHSA-x82f-27x3-q89c
GHSA-x9cf-3w63-rpq9
GHSA-xf99-j42q-5w5p
GHSA-xgf2-vxv2-rrmg
GHSA-xh72-v6v9-mwhc
GHSA-xhq5-45pm-2gjr
GHSA-xj9w-5r6q-x6v4
GHSA-xmv6-r34m-62p4
GHSA-xmxx-7p24-h892
GHSA-xp9r-prpg-373r
GHSA-xq8g-hgh6-87hv
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xvx8-77m6-gwg6
GHSA-xw9g-7xvv-gcjc
GHSA-xwcj-hwhf-h378
GHSA-xwcr-v472-8hhr
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h
GHSA-xxvh-5hwj-42pp

### claw-07 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2f7j-rp58-mr42
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2qrv-rc5x-2g2h
GHSA-2w79-r9g8-wmcr
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-35mw-5vvr-vrxc
GHSA-37v6-fxx8-xjmx
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-3xv9-89fm-7h4r
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-6336-qqw9-v6x6
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-6p8r-6m93-557f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-846p-hgpv-vphc
GHSA-877v-w3f5-3pcq
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-98ch-45wp-ch47
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9jpj-g8vv-j5mf
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cg7q-fg22-4g98
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-cr8r-7g2h-6wr6
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f693-58pc-2gfr
GHSA-f6p7-6326-vf7v
GHSA-f7fh-qg34-x2xh
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh32-73r9-rgh5
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqrj-m88p-qf3v
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g8xp-qx39-9jq9
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h43v-27wg-5mf9
GHSA-hcm3-8f6r-6xwg
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-j9pv-rrcj-6pfx
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jjw7-3vjf-fg5j
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qcc3-jqwp-5vh2
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qm77-8qjp-4vcm
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rm5c-4rmf-vvhw
GHSA-rvvf-6vh3-9j43
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vjx8-8p7h-82gr
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6wx-jq6j-6mcj
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wpc6-37g7-8q4w
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwfp-w96m-c6x8
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xj9w-5r6q-x6v4
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-08 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2f7j-rp58-mr42
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2qrv-rc5x-2g2h
GHSA-2w79-r9g8-wmcr
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-35mw-5vvr-vrxc
GHSA-37v6-fxx8-xjmx
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-3xv9-89fm-7h4r
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-6336-qqw9-v6x6
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-6p8r-6m93-557f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-846p-hgpv-vphc
GHSA-877v-w3f5-3pcq
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-98ch-45wp-ch47
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9jpj-g8vv-j5mf
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cg7q-fg22-4g98
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-cr8r-7g2h-6wr6
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f693-58pc-2gfr
GHSA-f6p7-6326-vf7v
GHSA-f7fh-qg34-x2xh
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh32-73r9-rgh5
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqrj-m88p-qf3v
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g8xp-qx39-9jq9
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h43v-27wg-5mf9
GHSA-hcm3-8f6r-6xwg
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-j9pv-rrcj-6pfx
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jjw7-3vjf-fg5j
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qcc3-jqwp-5vh2
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qm77-8qjp-4vcm
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rm5c-4rmf-vvhw
GHSA-rvvf-6vh3-9j43
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vjx8-8p7h-82gr
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6wx-jq6j-6mcj
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wpc6-37g7-8q4w
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwfp-w96m-c6x8
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xj9w-5r6q-x6v4
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-09 advisory ids

GHSA-24vr-rprv-67rf
GHSA-25wv-8phj-8p7r
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2f7j-rp58-mr42
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2qrv-rc5x-2g2h
GHSA-2w79-r9g8-wmcr
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-35mw-5vvr-vrxc
GHSA-37v6-fxx8-xjmx
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3pm9-5j7m-59vc
GHSA-3qpv-xf3v-mm45
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-3xv9-89fm-7h4r
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4g5x-2jfc-xm98
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4p4f-fc8q-84m3
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57gh-m6rq-54cf
GHSA-57r2-h2wj-g887
GHSA-58q2-7r52-jq62
GHSA-5cj2-3jr2-5h77
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5hff-46vh-rxmw
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-6336-qqw9-v6x6
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68v4-hmwv-f43h
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-6p8r-6m93-557f
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7ggg-pvrf-458v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83f3-hh45-vfw9
GHSA-83w9-h5wv-j9xm
GHSA-846p-hgpv-vphc
GHSA-877v-w3f5-3pcq
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-89r3-6x4j-v7wf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-98ch-45wp-ch47
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f4w-67g7-mqwv
GHSA-9f86-pvv5-rxfw
GHSA-9gp8-hjxr-6f34
GHSA-9jpj-g8vv-j5mf
GHSA-9p3r-hh9g-5cmg
GHSA-9p6m-2872-xm7x
GHSA-9q7v-8mr7-g23p
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-cg7q-fg22-4g98
GHSA-chfm-xgc4-47rj
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqgw-44wg-44rf
GHSA-cqwv-9qjx-vxw2
GHSA-cr8r-7g2h-6wr6
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwf8-44x6-32c2
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-cwq8-6f96-g3q4
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f693-58pc-2gfr
GHSA-f6p7-6326-vf7v
GHSA-f7fh-qg34-x2xh
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh32-73r9-rgh5
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fqrj-m88p-qf3v
GHSA-fv94-qvg8-xqpw
GHSA-fvx6-pj3r-5q4q
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwjq-xwfj-gv75
GHSA-g24w-m94m-59qc
GHSA-g374-mggx-p6xc
GHSA-g5cg-8x5w-7jpm
GHSA-g8xp-qx39-9jq9
GHSA-gfg9-5357-hv4c
GHSA-gfmx-pph7-g46x
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gjm7-hw8f-73rq
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h43v-27wg-5mf9
GHSA-hcm3-8f6r-6xwg
GHSA-hhff-fj5f-qg48
GHSA-hhq4-97c2-p447
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hr8g-2q7x-3f4w
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-j9pv-rrcj-6pfx
GHSA-jf25-7968-h2h5
GHSA-jf56-mccx-5f3f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jj6q-rrrf-h66h
GHSA-jjw7-3vjf-fg5j
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m34q-h93w-vg5x
GHSA-m38g-vpwj-mpg9
GHSA-m6fx-m8hc-572m
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhgq-xpfq-6r66
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mhr7-2xmv-4c4q
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p464-m8x6-vhv8
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-q9w8-cf67-r238
GHSA-qcc3-jqwp-5vh2
GHSA-qcj9-wwgw-6gm8
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qm77-8qjp-4vcm
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rfqg-qgf8-xr9x
GHSA-rg8m-3943-vm6q
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rm5c-4rmf-vvhw
GHSA-rvvf-6vh3-9j43
GHSA-rx78-29qr-5hq8
GHSA-rxmx-g7hr-8mx4
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vjx8-8p7h-82gr
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w6wx-jq6j-6mcj
GHSA-w85g-3h6x-4xh2
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wpc6-37g7-8q4w
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwfp-w96m-c6x8
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x2m8-53h4-6hch
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xj9w-5r6q-x6v4
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-10 advisory ids

GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2gvc-4f3c-2855
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5gjc-grvm-m88j
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-736r-jwj6-4w23
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c9h3-5p7r-mrjh
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f6p7-6326-vf7v
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-g2hm-779g-vm32
GHSA-g375-h3v6-4873
GHSA-gfg9-5357-hv4c
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-jf25-7968-h2h5
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-mr34-9552-qr95
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-11 advisory ids

GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2gvc-4f3c-2855
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5gjc-grvm-m88j
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-736r-jwj6-4w23
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c9h3-5p7r-mrjh
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f6p7-6326-vf7v
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-g2hm-779g-vm32
GHSA-g375-h3v6-4873
GHSA-gfg9-5357-hv4c
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-jf25-7968-h2h5
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-mr34-9552-qr95
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-12 advisory ids

GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2gvc-4f3c-2855
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5gjc-grvm-m88j
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-736r-jwj6-4w23
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c9h3-5p7r-mrjh
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f6p7-6326-vf7v
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-g2hm-779g-vm32
GHSA-g375-h3v6-4873
GHSA-gfg9-5357-hv4c
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-jf25-7968-h2h5
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-mr34-9552-qr95
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-13 advisory ids

GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2767-2q9v-9326
GHSA-2cq5-mf3v-mx44
GHSA-2gvc-4f3c-2855
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3fv3-6p2v-gxwj
GHSA-3mq7-q27j-mq7q
GHSA-3vvq-q2qc-7rmp
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-49cg-279w-m73x
GHSA-4f8g-77mw-3rxc
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-525j-hqq2-66r4
GHSA-527m-976r-jf79
GHSA-536q-mj95-h29h
GHSA-53vx-pmqw-863c
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fc7-f62m-8983
GHSA-5fwv-rrvp-8xvr
GHSA-5gjc-grvm-m88j
GHSA-5h3f-885m-v22w
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-5wj5-87vq-39xm
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-66r7-m7xm-v49h
GHSA-67mf-f936-ppxf
GHSA-68x5-xx89-w9mm
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-736r-jwj6-4w23
GHSA-7437-7hg8-frrw
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7g8c-cfr3-vqqr
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-7jp6-r74r-995q
GHSA-7wv4-cc7p-jhxc
GHSA-82qx-6vj7-p8m2
GHSA-8372-7vhw-cm6q
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-92jp-89mq-4374
GHSA-939r-rj45-g2rj
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-c4qm-58hj-j6pj
GHSA-c9h3-5p7r-mrjh
GHSA-ccwh-wwpp-6wg5
GHSA-ccx3-fw7q-rr2r
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cm8v-2vh9-cxf3
GHSA-cmfr-9m2r-xwhq
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f3h5-h452-vp3j
GHSA-f6p7-6326-vf7v
GHSA-f934-5rqf-xx47
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-g2hm-779g-vm32
GHSA-g375-h3v6-4873
GHSA-gfg9-5357-hv4c
GHSA-ghpx-6xwq-2w4w
GHSA-gj9q-8w99-mp8j
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-j6c7-3h5x-99g9
GHSA-jf25-7968-h2h5
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-jwrq-8g5x-5fhm
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-mr34-9552-qr95
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q2gc-xjqw-qp89
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qmwg-qprg-3j38
GHSA-qqq7-4hxc-x63c
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-qx8j-g322-qj6m
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj2p-j66c-mgqh
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vc32-h5mq-453v
GHSA-vfp4-8x56-j7c5
GHSA-vhpg-cq3w-v8p9
GHSA-vr5g-mmx7-h897
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w8g9-x8gx-crmm
GHSA-w9hf-3pp7-pvxv
GHSA-w9j9-w4cp-6wgr
GHSA-wc84-j36w-pw4x
GHSA-whf9-3hcx-gq54
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xh72-v6v9-mwhc
GHSA-xmxx-7p24-h892
GHSA-xq94-r468-qwgj
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-14 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-15 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-16 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-2xcp-x87w-q377
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-57r2-h2wj-g887
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-72q8-jcmc-97wx
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-7jm2-g593-4qrc
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-c4qg-j8jg-42q5
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-h2vw-ph2c-jvwf
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-hxvm-xjvf-93f3
GHSA-j472-gf56-x589
GHSA-j4c5-89f5-f3pm
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mj59-h3q9-ghfh
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qrp5-gfw2-gxv4
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-v8qf-fr4g-28p2
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xrq9-jm7v-g9h7
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-17 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-18 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-19 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c28g-vh7m-fm7v
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-20 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-21 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-22 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-275c-xpvc-jgfw
GHSA-2hfg-4fh4-qp7f
GHSA-2hh7-c75g-qj2r
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-55cf-xx38-4p9p
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5h3g-6xhh-rg6p
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-93rg-2xm5-2p9v
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q3jj-46pq-826r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r6xh-pqhr-v4xh
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wppj-c6mr-83jj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x3h8-jrgh-p8jx
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-23 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-2hfg-4fh4-qp7f
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-24 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-2hfg-4fh4-qp7f
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-25 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-2hfg-4fh4-qp7f
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwj3-vqpp-pmxr
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q7q8-3mgw-q67r
GHSA-q8ff-7ffm-m3r9
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r39h-4c2p-3jxp
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-26 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-2hfg-4fh4-qp7f
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q7q8-3mgw-q67r
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rwp6-7w3q-75fq
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-27 advisory ids

GHSA-22v4-33m3-8p7m
GHSA-24vr-rprv-67rf
GHSA-2hfg-4fh4-qp7f
GHSA-2j8v-hwgc-x698
GHSA-2x93-h3hg-2xfp
GHSA-34mr-7r3m-gfg7
GHSA-39hf-qg99-f4qv
GHSA-3c6j-hq33-3jv4
GHSA-3fp5-v549-9v66
GHSA-3mq7-q27j-mq7q
GHSA-3wqp-prf6-2m72
GHSA-3x84-qq85-fj65
GHSA-4g58-43jr-6738
GHSA-4hpg-mp64-x7xq
GHSA-4hwv-rj92-h7rp
GHSA-4m3v-q747-pc6h
GHSA-4pqj-3c56-5fqq
GHSA-4r25-35qc-fr6j
GHSA-4wvr-f35r-f8w4
GHSA-4xwj-mcc7-x7x5
GHSA-575v-8hfq-m3mc
GHSA-5fwv-rrvp-8xvr
GHSA-5j27-v2pw-cj9m
GHSA-5m4g-88rg-69pj
GHSA-5mrc-77hj-xjxv
GHSA-5p6w-wmh3-frfr
GHSA-5rx7-34fw-64qg
GHSA-62qm-6fjj-6g23
GHSA-66hm-hxq3-5pfh
GHSA-68xw-r643-9p5w
GHSA-6c4r-g249-wv3c
GHSA-6fvr-66p3-3qj4
GHSA-724r-v4wf-mqc5
GHSA-72fw-cqh5-f324
GHSA-72p2-79fg-pvph
GHSA-74gc-hg2m-79p9
GHSA-77pv-3w4q-vrj5
GHSA-77q5-rr5v-x43q
GHSA-7cp7-87pj-p32v
GHSA-7hxm-f538-3xp6
GHSA-7jfq-rmfm-29wp
GHSA-83w9-h5wv-j9xm
GHSA-8938-r7c6-54vq
GHSA-89cw-7452-cfrf
GHSA-8c59-hr4w-qg69
GHSA-8f46-3xx3-8c9m
GHSA-8j37-5w68-wj2g
GHSA-8mg9-j9cf-54cj
GHSA-8v95-qqcm-qp9h
GHSA-8wg3-5mcm-fjq8
GHSA-8xxh-v4vc-qvm4
GHSA-985f-72mj-8gf7
GHSA-9969-8g9h-rxwm
GHSA-9c3v-684m-579c
GHSA-9f86-pvv5-rxfw
GHSA-9p6m-2872-xm7x
GHSA-9v8j-9c9g-w66c
GHSA-9x88-f7rh-4c83
GHSA-c226-q6fx-6j6c
GHSA-c29c-2q9c-pc86
GHSA-ccwh-wwpp-6wg5
GHSA-cf2p-f286-mphf
GHSA-chr6-w4m5-57fv
GHSA-chr9-m4q2-76hw
GHSA-cqwv-9qjx-vxw2
GHSA-crg9-c62w-j2p5
GHSA-cw4q-gqg5-g38h
GHSA-cwpp-5962-q4f6
GHSA-f397-5vjw-v2c2
GHSA-f6p7-6326-vf7v
GHSA-fcvx-5cxc-v5p8
GHSA-fh38-965w-f6c3
GHSA-fphf-69cp-h5xw
GHSA-fq9j-vw4w-fr6v
GHSA-fvxr-9g24-x3hf
GHSA-fw6q-2frm-jxxr
GHSA-fwgr-fpv9-vf5x
GHSA-g24w-m94m-59qc
GHSA-ghpx-6xwq-2w4w
GHSA-gp79-m99v-gjmh
GHSA-grc3-2j34-p6gm
GHSA-gxg4-2rrr-jhc7
GHSA-hcm3-8f6r-6xwg
GHSA-hjr6-g723-hmfm
GHSA-hpg5-cq3m-phqp
GHSA-hw9r-h9mr-4jff
GHSA-hx85-fgcw-9vrc
GHSA-j472-gf56-x589
GHSA-j4cx-jvq7-79vm
GHSA-j4mm-p864-vx7f
GHSA-jghr-xp78-995p
GHSA-jhfx-v2j8-x3m6
GHSA-jvm4-4j77-39p6
GHSA-m38g-vpwj-mpg9
GHSA-m78m-7h3q-q938
GHSA-mgq6-vr84-7m2j
GHSA-mgvr-6gvw-3rgr
GHSA-mhm4-93fw-4qr2
GHSA-mhq8-78pj-5j79
GHSA-mpc8-jxjh-qpgh
GHSA-p2fh-f5fc-44hr
GHSA-p39j-x9h5-q66m
GHSA-p3h6-v2h4-36q2
GHSA-p5g8-m35v-7m82
GHSA-p5xh-frrh-cmgj
GHSA-p73f-w79w-jqr5
GHSA-pjjr-5qhr-5w6r
GHSA-q7q8-3mgw-q67r
GHSA-q99w-vh6v-q3v7
GHSA-q9j5-4xr6-xqqw
GHSA-qgj5-6x35-9g6f
GHSA-qh2f-99mv-mrcf
GHSA-qjpc-qf9m-xwmr
GHSA-qw7m-h363-33qw
GHSA-r88x-r7jj-f2cf
GHSA-rggc-m335-3wvj
GHSA-rgjw-6v73-php6
GHSA-rh6r-vvfc-86jq
GHSA-rj6p-xmxr-qj4h
GHSA-rjxq-qqhf-8hwh
GHSA-rm45-4jx5-2927
GHSA-rwp6-7w3q-75fq
GHSA-rx78-29qr-5hq8
GHSA-v2ww-5rh7-2h5v
GHSA-v6r2-jh58-xx6w
GHSA-v8cx-933x-r976
GHSA-vhpg-cq3w-v8p9
GHSA-vr7j-7684-7gm5
GHSA-vxx3-6hc9-7cc3
GHSA-w4v6-g3wm-w36c
GHSA-w5ww-7chg-mxcq
GHSA-w5x7-c87m-3jpc
GHSA-w9hf-3pp7-pvxv
GHSA-wc84-j36w-pw4x
GHSA-wjfv-5qch-m5vj
GHSA-wv26-j37q-2g7p
GHSA-wwcw-jfpp-gpxw
GHSA-wwx7-573h-pqwc
GHSA-wxh3-g47h-q3mc
GHSA-wxm8-ghhq-q688
GHSA-x629-46cc-7xgw
GHSA-x863-pqjw-hmgf
GHSA-xr4f-mjxj-w6w5
GHSA-xw9g-7xvv-gcjc
GHSA-xww8-gqvh-92x9
GHSA-xx9p-hc9w-6p5h

### claw-28 advisory ids

(none)

### claw-29 advisory ids

(none)

### claw-30 advisory ids

(none)
