## Verification Report — Zalando / competitive-intelligence-v3.md

**Output type:** External Research (create-company)

**File verified:** competitive-intelligence-v3.md

**Fact registry:** Found — M-2 run (fact_registry_competitive-intelligence-v3.json)

**Date verified:** 2026-04-26

---

### Machine Verification Results

**Rates (higher = better):**

| Metric | Score | Detail |
|---|---|---|
| Quant Claims Accuracy Rate | 66.7% | 6 confirmed / 9 checkable (0 Inconclusive — 4 previously Inconclusive resolved as Human-confirmed accurate) |
| Link Validity Rate | 80.0% | 20 working / 25 checkable (0 Inconclusive). Broken/inaccessible: SRC:guardian_asos_ai_stylist (human confirmed broken), SRC:zalando_fy25_press_release, SRC:retail_gazette_zalando_about_you, SRC:retailtechhub_zalando_google_ucp, SRC:coupang_farfetch (no URL stored). |
| Citation Coverage Rate | 100.0% | 38 cited / 38 content data-filled fields (labeled gaps, structural metadata sections — Source Registry, Label Legend, Gate Checks Completed — and document header fields — Market, Research date — excluded; citations apply to sections 1–4 only). **0 uncited content fields.** |
| Field Recall Rate (automated) | 100.0% | 40 filled / 40 resolvable fields (24 labeled [UNVERIFIED]/[SEARCH FAILED] excluded from denominator) |
| Field Recall Rate (adjusted for FN) | 97.6% | 40 filled / 41 resolvable fields. 1 false negative: ASOS employee count (~2,800+) was publicly available in ASOS Annual Report PDF but not retrieved. |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 |
| Blocked Source Violations (KNOWN_BAD domain or invalid `source_type`) | 0 | 0 |
| Banned Claim Pattern Instances | 0 | 0 |
| Stale Untagged Source Violations | 0 | 0 |
| Uncited Quoted String Violations | N/A — no User Sentiment section | N/A |
| Competitor Count | 3 direct competitors (ASOS, SHEIN, Vinted) | ≥ 3 |

---

### Quant Claims Accuracy detail (M-1)

| Claim | Stated Value | SRC | Result | Notes | Fix |
|---|---|---|---|---|---|
| Zalando GMV €17.6B, Revenue €12.3B, 62M customers | GMV €17.6B, Revenue €12.3B, 62M customers | SRC:zalando_fy25_press_release | Confirmed — Human-resolved | URL inaccessible but claim confirmed accurate by human reviewer | — |
| ASOS Revenue £2,477.8m, FY2025, −15% YoY | £2,477.8m, −15% | SRC:asos_fy25_rns | Confirmed — Human-resolved | Human confirmed accurate against FY25 RNS PDF | — |
| ASOS 6.5M active customers (cited to HY26 RNS) | 6.5M active customers | SRC:asos_hy26_rns | **Contradicted** | HY26 RNS reports global total of 16.5M customers; 6.5M appears to come from FY25 RNS, not HY26. Citation is incorrect. | Flag — citation needs correcting to SRC:asos_fy25_rns and value needs re-verification |
| ASOS 850+ partner brands, 240 countries / markets | 850+ partner brands, 240 countries | SRC:asos_hy26_rns | **Contradicted** | Human confirmed HY26 RNS states "over 100 markets"; ASOS operates in 200+ markets per other sources. Neither 850+ brands nor 240 countries confirmed by cited source. | Flag — requires re-verification against correct source |
| ASOS "Styled By You" AI stylist, 100,000 curated outfits | 100,000 curated outfits; loyalty programme members | SRC:guardian_asos_ai_stylist | Confirmed — Human-resolved | Human confirmed broken link; claim confirmed accurate by human reviewer | — |
| ASOS sold 75% Topshop/Topman to Heartland for £135M | 75% stake, £135M (~$180M) | SRC:asos_topshop_heartland_jv | Confirmed — Human-resolved | Human confirmed URL works and claim is accurate | — |
| >40% of Zalando orders included at least one pre-owned item | >40% of Zalando orders included ≥1 pre-owned item | SRC:fashionunited_zalando_resale_kidswear | **Contradicted** | FashionUnited source states >40% of orders combined new fashion/beauty with second-hand garments — not that ≥1 pre-owned item was in the order. Wording materially misrepresents the stat. | Auto-fix — reword to match source |
| Zalando acquired About You, July 2025 | July 2025 | SRC:retail_gazette_zalando_about_you | Confirmed — Human-resolved | Link broken but claim confirmed accurate by human reviewer | — |
| Zalando joined Google UCP, January 2026 | January 2026 | SRC:retailtechhub_zalando_google_ucp | Confirmed — Human-resolved | Link broken but claim confirmed accurate by human reviewer | — |

**Final Quant Claims Accuracy Rate: 66.7%** — 6 Confirmed / 9 checkable (Confirmed + Contradicted). 0 Inconclusive.

---

### Human Evaluation (HHH)

*Raw Yes/No per criterion — aggregated across companies over time, not scored per company.*

**Honesty** — Accuracy and truthfulness

| Criteria | Yes / No |
|---|---|
| H1: Are any citations inaccurate or incomplete? | Yes |
| H2: Are any links inaccessible or unverifiable? | Yes |
| H3: Are any current-state qualitative claims poorly substantiated? | Yes |
| H4: Are any future-state claims presented with over-confidence? | No |

**Helpfulness** — Effectiveness in solving the PM's problem

| Criteria | Yes / No |
|---|---|
| He1: Does the report fail to provide novel information? | No |
| He2: Is the report not useful for framing insights or PM decisions? | Yes |

**Harmlessness** — Safe and appropriately framed

| Criteria | Yes / No |
|---|---|
| Ha1: Negative claims about the company lack sufficient evidence? | No |
| Ha2: Negative claims about competitors lack sufficient evidence? | No |

*He2 note: Freshness filter (2yr) by design excludes historically useful PM signals (e.g., ASOS Thrift+ pilot 2022, now defunct). This is a design constraint, not an accuracy failure.*

---

### Issues Found

#### Auto-fix issues

| ID | Section | Found | Should Be |
|---|---|---|---|
| M-1 #7 | Zalando — Recent news (pre-owned / resale stat) | "more than 40% of Zalando orders included at least one pre-owned item" | "more than 40% of Zalando orders combined new fashion and beauty products with second-hand garments" |

#### Flagged for human review

| ID | Section | Issue | Response |
|---|---|---|---|
| M-1 #3 | ASOS — Customers | Document cites SRC:asos_hy26_rns for 6.5M active customers, but HY26 RNS shows 16.5M global total; 6.5M figure appears to originate from FY25 RNS. Citation is wrong and value needs re-verification. | Correct citation to SRC:asos_fy25_rns and re-verify the 6.5M figure |
| M-1 #4 | ASOS — Product / Market reach | "850+ partner brands, 240 countries" — HY26 RNS confirms neither figure; states "over 100 markets". Human confirms ASOS operates in 200+ markets; 240 and 850+ are unconfirmed. | Remove or replace with confirmed figures from FY25 RNS or ASOS newsroom |
| H3 | ASOS — Product | "targeting 18–30-year-olds" cited to SRC:asos_hy26_rns, but that source does not substantiate this demographic claim. | Add a supporting citation or remove the claim |
| H2 / M-2 | Source Registry — SRC:coupang_farfetch | No retrievable URL stored; registry contains only Zalando's own IR page URL (incorrect source). | Replace with a real Coupang/Farfetch news source URL and update fact_registry |
| H2 / M-2 | Vinted — Recent news 3 | `[UNVERIFIED — Silicon Republic, 2025; URL NOT RETRIEVED]` — no URL stored for this source in the registry. | Locate and add URL or remove the claim |
| M-2 | Source Registry | 3 confirmed broken links: SRC:zalando_fy25_press_release, SRC:retail_gazette_zalando_about_you, SRC:retailtechhub_zalando_google_ucp. Associated claims (Zalando FY25 financials, About You acquisition date, Google UCP partnership date) are currently unverifiable. | Find replacement sources; update fact_registry and inline citations |

---

### All Checks — Results Summary

| Check | Result | Detail |
|---|---|---|
| M-1 Quant Claims Accuracy | ⚠ 66.7% — 3 contradicted | See M-1 detail table. 6 confirmed (2 machine + 4 human-resolved), 3 contradicted, 0 inconclusive. |
| M-2 Link Validity | 80.0% — 5 broken/inaccessible | 20 working / 25 checkable. 0 inconclusive. Broken: guardian_asos_ai_stylist (human confirmed), zalando_fy25_press_release, retail_gazette_zalando_about_you, retailtechhub_zalando_google_ucp, coupang_farfetch (no URL). |
| M-3 Citation Coverage | ✓ 100.0% — 0 uncited content fields | 38 cited / 38 content fields. Document header fields (Market, Research date) excluded from scope — citations apply to sections 1–4 only. Structural metadata sections excluded. |
| M-4 Field Recall Rate | ✓ 100.0% (automated) / 97.6% (adjusted) — PASS | 1 FN: ASOS employee count available in Annual Report PDF but not retrieved. Both rates above 90% threshold. |
| M-5 Placeholder Text | 0 violations — PASS | |
| M-6 Blocked Source Compliance | 0 violations — PASS | validate.py: VALIDATION PASSED. No KNOWN_BAD domains. No [VALIDATION_FAILED] tags in document body. |
| M-7 Competitor Count | 3 profiles — PASS | ASOS, SHEIN, Vinted. Meets ≥3 minimum. |
| M-8 Banned Claim Patterns | 0 violations — PASS | 4 regex hits on "only" — all confirmed false positives (Legend text and descriptor language, not unsupported superlative claims). |
| M-9 Stale Untagged Sources | 0 violations — PASS | |
| M-10 Uncited Quoted Strings | N/A — no User Sentiment section | |

---

**Score legend:**

| Metric | What it measures | How calculated |
|---|---|---|
| Quant Claims Accuracy Rate | % of all objective facts confirmed correct by their cited source | Confirmed ÷ (Confirmed + Contradicted). Inconclusive excluded. |
| Link Validity Rate | % of URLs in fact registry returning a working page | Working links ÷ total links. Broken = confirmed 4xx (human-verified) or no URL. 5xx = server error. Bot-blocked 4xx unconfirmed by human = Inconclusive (excluded). |
| Citation Coverage Rate | % of filled fields with ≥1 [SRC:id] — presence only, not quality | Fields with citation ÷ filled fields. Source quality is H1/H2. |
| Field Recall Rate | % of template fields filled with real data. Labeled gaps count as intentional. | Filled fields ÷ total fields. Target: ≥90%. |
| Placeholder Text Violations | Template tokens still in the file — not filled or labeled as intentional gaps | Count. Target: 0. |
| Blocked Source Violations | KNOWN_BAD domain sources in fact registry or report body, or invalid `source_type` values. Each `[VALIDATION_FAILED]` tag also counts. | Count. Target: 0. |
| Banned Claim Pattern Instances | Unsupported superlatives without [SRC:id] — high hallucination risk | Count. Target: 0. |
| Stale Untagged Source Violations | Sources >2 years old not tagged [>2YR]. Stale + tagged is fine. | Count. Target: 0. |
| Uncited Quoted String Violations | Quoted consumer phrases in User Sentiment fields with no [SRC:id] — likely hallucinated from general knowledge | Count. Target: 0. |
| Competitor Count | Named direct competitors with a dedicated block in competitive-landscape.md | Raw count. Target: ≥3. |
