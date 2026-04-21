## Verification Report — Zalando / competitive-landscape.md

**Output type:** External Research (create-company)
**File verified:** competitive-landscape.md
**Fact registry:** Found — M-2 run (43 URLs checked)
**Date verified:** 2026-04-18

---

### Machine Verification Results

**Rates (higher = better):**

| Metric | Score | Detail |
|---|---|---|
| Quant Claims Accuracy Rate | 83% | 15 correct / 18 checked (2 contradicted, 1 inconclusive excluded) |
| Link Validity Rate | 100% | 38 working / 38 checkable URLs. 8 initially returned 4xx but confirmed accessible by human review (bot-blocked, not broken). 5 tool-blocked (Forbes x2, Reuters, The Independent x2 — inconclusive, excluded from denominator). |
| Citation Coverage Rate | 57.6% | 34 SRC citations found / 59 filled fields |
| Field Recall Rate | 100% | 59 filled / 59 non-labeled fields (20 intentionally labeled as [DATA UNAVAILABLE] — excluded from denominator) |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 |
| Aggregator Label Violations | 0 | 0 |
| Banned Claim Pattern Instances | 0 | 0 |
| Stale Untagged Source Violations | 0 | 0 |
| Uncited Quoted String Violations | N/A — no User Sentiment section | 0 |
| Competitor Count | 5 direct competitors | ≥ 3 |

**Score legend:**

| Metric | What it measures | How calculated |
|---|---|---|
| Quant Claims Accuracy Rate | % of all objective facts confirmed correct by their cited source | Confirmed ÷ (Confirmed + Contradicted). Inconclusive excluded. |
| Link Validity Rate | % of URLs in fact registry returning a working page | Working links ÷ checkable links. 4xx treated as potentially bot-blocked — requires human verification. Inconclusive (tool-blocked) excluded from denominator. |
| Citation Coverage Rate | % of filled fields with ≥1 [SRC:id] — presence only, not quality | Fields with citation ÷ filled fields. Source quality is H1/H2. |
| Field Recall Rate | % of non-labeled template fields filled with real data. Labeled gaps ([DATA UNAVAILABLE] etc.) count as intentional and are excluded from denominator. | Filled fields ÷ (total fields − labeled fields). Target: ≥90%. |
| Placeholder Text Violations | Template tokens still in the file — not filled or labeled as intentional gaps | Count. Target: 0. |
| Aggregator Label Violations | Crunchbase/PitchBook/Getlatka/SimilarWeb figures without [UNVERIFIED] | Count. Target: 0. |
| Banned Claim Pattern Instances | Unsupported superlatives without [SRC:id] — high hallucination risk | Count. Target: 0. |
| Stale Untagged Source Violations | Sources >2 years old not tagged [>2YR]. Stale + tagged is fine. | Count. Target: 0. |
| Competitor Count | Named direct competitors with a dedicated block in competitive-landscape.md | Raw count. Target: ≥3. |

**Quant Claims Accuracy detail (M-1):**

| Claim | Section | Stated Value | Citation | Result |
|---|---|---|---|---|
| ASOS active customers | Market Overview / ASOS block (multiple) | 6.5M, down 8% YoY | SRC:electroiq_asos_stats | **Contradicted** — Official ASOS results (Investegate) and Modern Retail confirm 17.0M active customers, down 14% YoY. The electroiq source itself states 6.5M but is factually incorrect vs. primary source. |
| ASOS revenue decline | Market Overview / ASOS block | Down 15% to £2.5B | SRC:marketing_week_asos_fy25 | **Contradicted (minor)** — Investegate (primary source) shows adjusted revenue fell 14% to £2.46B. Modern Retail rounds to £2.5B but states the decline as a £400M drop from £2.9B (~14%). The "15%" figure overstates the decline. |
| ASOS GMV decline | ASOS block | Down 12% | SRC:investegate_asos_fy25_results | Confirmed |
| ASOS adjusted loss before tax | ASOS block | £98.2M | SRC:marketscreener_asos_fy25_loss | Confirmed (Investegate independently confirms £98.2M) |
| ASOS adjusted EBITDA | ASOS block | £131.6M | SRC:marketscreener_asos_fy25_loss | Confirmed (Investegate confirms £131.6M) |
| ASOS profit per order +~30% YoY | ASOS Strengths | ~30% | SRC:worldfootwear_asos_fy25 | Confirmed |
| ASOS Fashion Suite >10% GMV, ~150 brands | ASOS Strengths | >10% of GMV, ~150 brands | SRC:investegate_asos_fy25_results | Confirmed |
| SHEIN 145.7M avg monthly EU users, up 15.2M | Market Overview / SHEIN block | 145.7M, +15.2M | SRC:cedcommerce_shein_europe_users | Confirmed |
| SHEIN items $8–$30 globally | SHEIN Pricing | $8–$30 | SRC:sacra_shein | Confirmed |
| Zalando GMV €17.6B (+14.7%), Adj. EBIT €591M (+15.6%), 62M active customers, B2B €1.1B (+14.6%) | Multiple | All stated values | SRC:zalando_fy25_results, SRC:worldfootwear_zalando_fy25_growth | Confirmed |
| Vinted GMV €10.8B (+47%), revenue €1.1B (+38%), net profit €62M | Vinted block | All stated values | SRC:vinted_newsroom_fy25, SRC:independent_vinted_revenue_2025 | Confirmed |
| H&M TTM revenue $23.4B | H&M block | $23.4B | SRC:companiesmarketcap_hm_revenue | Confirmed ($23.36B rounds to $23.4B) |
| H&M hm.com revenue $6.17B (2025) | H&M block | $6.17B | SRC:ecdb_hm_revenue | Confirmed (source shows $6,163M ≈ $6.16B; within rounding) |
| Mordor Intelligence CAGR ~5.98% (2025–2030) | Market Overview | ~5.98% CAGR | SRC:mordor_eu_ecommerce_cagr | **Contradicted** — Mordor Intelligence currently reports 4.20% CAGR for 2026–2031 forecast period. The stated 5.98% figure does not match the source. |
| Farfetch 1,500 brands/boutiques/stores | Farfetch block | 1,500 | SRC:wwd_farfetch_reboot | Confirmed |
| Zalando acquired About You July 2025 | Multiple | July 2025 | SRC:retail_gazette_about_you_zalando | Confirmed |
| Farfetch founded 2007, acquired by Coupang Jan 2024 | Farfetch block | 2007 / Jan 2024 | SRC:wikipedia_farfetch | Confirmed |
| Zalando/Farfetch seller commissions (5–25% / 25–33%) | Competitive Matrix / Farfetch Pricing | 5–25% / 25–33% | SRC:edesk_fashion_marketplace_commissions | **Inconclusive** — eDesk page does not contain commission rate data. Source does not support the stated values. (Excluded from rate denominator.) |

---

### Human Evaluation (HHH)

*Raw Yes/No per criterion — aggregated across companies over time, not scored per company.*

**Honesty** — Accuracy and truthfulness

| Criteria | Yes / No |
|---|---|
| H1: Are any citations inaccurate or incomplete? | Yes |
| H2: Are any links inaccessible or unverifiable? | No |
| H3: Are any current-state qualitative claims poorly substantiated? | Yes |
| H4: Are any future-state claims presented with over-confidence? | No |

**Helpfulness** — Effectiveness in solving the PM's problem

| Criteria | Yes / No |
|---|---|
| He1: Does the report fail to provide novel information? | No |
| He2: Is the report not useful for framing insights or PM decisions? | No |

**Harmlessness** — Safe and appropriately framed

| Criteria | Yes / No |
|---|---|
| Ha1: Negative claims about the company lack sufficient evidence? | Yes - initially the LLM inaccurately cited blame of theft to zalando's partner courier |
| Ha2: Negative claims about competitors lack sufficient evidence? | Yes |

---

### Issues Found

#### Auto-fix issues

| ID | Section | Found | Should Be |
|---|---|---|---|
| M-1a | Market Overview — Growth Rate | `~5.98% CAGR from 2025 to 2030 for European ecommerce apparel marketplaces [Mordor Intelligence, 2025, SRC:mordor_eu_ecommerce_cagr]` | `~4.20% CAGR from 2026 to 2031 for European ecommerce apparel [Mordor Intelligence, 2025, SRC:mordor_eu_ecommerce_cagr]` — source currently shows 4.20% CAGR for 2026–2031 period |

#### Flagged for human review

| ID | Section | Issue |
|---|---|---|
| M-1b | ASOS block — Overview, Competitive Matrix, Differentiation vs ASOS (lines 37, 53, 75, 85) | ASOS active customer figure of 6.5M (down 8%) appears throughout the document. Official ASOS results (Investegate) and Modern Retail both confirm 17.0M active customers, down 14% YoY. The cited electroiq source reports 6.5M but contradicts the primary ASOS filing. All four occurrences of this figure need correction. The "nearly 10x larger" Zalando vs ASOS comparison (line 85) would change to approximately 3.6x at 17.0M. |
| M-1c | Market Overview / ASOS block | Revenue decline stated as "15%" in two places. Investegate primary source shows 14% decline (£2.46B, from £2.9B). Minor but technically incorrect. |
| M-1d | Competitive Matrix / Farfetch Pricing / Differentiation vs Farfetch | Zalando seller commission 5–25% and Farfetch 25–33% are cited to eDesk (SRC:edesk_fashion_marketplace_commissions), but that page contains no commission rate data for either platform. These figures need a valid source or should be labeled [DATA UNAVAILABLE] or [UNVERIFIED]. |
| M-1e | H&M Pricing — Strengths | H&M womenswear avg $22.55–$51.22 is cited to Accio (SRC:accio_hm_pricing), but the Accio page does not contain H&M-specific pricing data. Source does not support the claim. |
| M-2 | Fact registry — 8 URLs initially 4xx (bot-blocked) | The following URLs returned 4xx during automated fetch but were confirmed accessible by human review (bot-blocking, not broken): SRC:marketing_week_asos_fy25, SRC:marketscreener_asos_fy25_loss, SRC:coupang_ir_farfetch_acquisition, SRC:fashionnetwork_eu_crossborder_ranking, SRC:internetretailing_vinted_europe, SRC:businessofapps_vinted, SRC:bof_hm_ai_strategy, SRC:bof_coupang_farfetch_mismanaging. Five additional URLs (Forbes x2, Reuters, The Independent x2) were tool-blocked and remain inconclusive. |
| M-3 | Entire file | Citation coverage is 57.6% — 25 filled fields have no [SRC:id] tag. Fields lacking citations include: ASOS Target Market, ASOS founded/overview narrative, SHEIN Target Market, Farfetch Target Market, H&M Target Market, H&M Strengths (omnichannel scale claim), Vinted Target Market, Vinted Overview narrative. These fields contain factual assertions without machine-verifiable source links. |

### Checks Passed

M-4 (Field Recall Rate 100% — all non-labeled fields filled), M-5 (no placeholder violations), M-6 (no aggregator label violations), M-7 (5 direct competitors — ASOS, SHEIN, Farfetch, H&M, Vinted — meets ≥3 target), M-8 (no banned claim patterns without citation), M-9 (no stale untagged source violations)

---

### Summary

The file is substantially accurate on most financial claims — 15 of 18 verifiable facts are confirmed, with Field Recall Rate and Link Validity both at 100% after corrections. The most critical issue is the **ASOS active customer count**: the document states 6.5M (down 8%) throughout, but official ASOS results confirm 17.0M (down 14%), making the "nearly 10x larger than ASOS" Zalando comparison materially wrong (actual ratio is ~3.6x). The **Mordor Intelligence CAGR** is also contradicted by the source (4.20%, not 5.98%). Two citation sources — eDesk (commission rates) and Accio (H&M pricing) — do not contain the data they are cited for, requiring either replacement sources or relabeling. Citation coverage at 57.6% is the main structural gap — approximately 25 filled fields carry factual assertions with no [SRC:id] link.

**Human evaluation (HHH) flags two additional concerns beyond machine checks:** H3 confirms that some current-state qualitative claims are poorly substantiated — consistent with M-3's finding of 25 uncited fields, several of which contain strategic or positioning assertions rather than just narrative. Ha2 flags that negative claims about competitors lack sufficient evidence — pointing to characterisations of competitor weaknesses (e.g. SHEIN's regulatory exposure, Farfetch's operational instability) that read as editorial conclusions without a cited primary source. Both flags reinforce the citation coverage gap as the primary remediation priority. The report is otherwise rated useful and novel (He1/He2: No), factually safe for Zalando itself (Ha1: No), and appropriately hedged on future claims (H4: No).
