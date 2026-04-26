## Verification Report — Zalando / competitive-intelligence.md

**Output type:** External Research (create-company)

**File verified:** competitive-intelligence.md

**Fact registry:** Found — M-2 run (68 URLs in registry)

**Date verified:** 2026-04-22

---

### Machine Verification Results

**Rates (higher = better):**

| Metric | Score | Detail |
|---|---|---|
| Quant Claims Accuracy Rate | 89% | 16 correct / 18 checked (2 contradicted, 2 inconclusive excluded) |
| Link Validity Rate | 93% | 14 working confirmed / 15 checkable URLs fetched. 1 confirmed broken: SRC:sheingroup_wroclaw (404). 6 previously bot-blocked URLs (SRC:coupang_ir_farfetch_acquisition, SRC:asos_topshop_heartland_jv, SRC:businessofapps_vinted, SRC:pitchbook_zalando_2026, SRC:fashionnetwork_zalando_ai_2026, SRC:gap_gemini_checkout) human-verified as accessible. SRC:guardian_asos_ai_stylist — tool-blocked (inconclusive, excluded from denominator). |
| Citation Coverage Rate | 84.8% | 39 cited / 46 data-filled fields (labeled gaps excluded). **7 uncited fields:** (1) Market Overview — industry outlook narrative sentence; (2–3) Trend 3 — H&M and SHEIN competitor response cells (proximity SRC only); (4–5) Trend 4 — SHEIN and Zalando response cells (proximity SRC only); (6) Competitive Summary Matrix — SHEIN "Latest signal" cell; (7) Vinted Profile — Recent news 3 source cell (auto-fix M-3 proposed) |
| Field Recall Rate | 100.0% | 46 filled / 46 resolvable fields (19 labeled [DATA UNAVAILABLE] excluded from denominator) |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 |
| Aggregator Label Violations (`[UNVERIFIED]` missing) | 0 | 0 |
| Banned Claim Pattern Instances | 0 | 0 |
| Stale Untagged Source Violations | 0 | 0 |
| Uncited Quoted String Violations | N/A — no User Sentiment section | N/A |
| Competitor Count | 3 named direct competitor profiles (ASOS, SHEIN, Vinted) | ≥ 3 |

---

### Score History

| Metric | v1 (2026-04-18) | v2 (2026-04-22) | Δ |
|---|---|---|---|
| Quant Claims Accuracy | 83% | 89% | +6pp |
| Link Validity | 100% | 93% | −7pp |
| Citation Coverage | 57.6% | 84.8% | +27.2pp |
| Field Recall | 100% | 100% | — |
| Placeholder violations | 0 | 0 | — |
| Aggregator violations | 0 | 0 | — |
| Banned patterns | 0 | 0 | — |
| Stale untagged | 0 | 0 | — |
| Uncited quotes | N/A | N/A | — |

*Rates: positive Δ = improvement. Violations: negative Δ = improvement.*

**Notes on score changes:**
- Quant Accuracy +6pp (v1→v2): v1 evaluated competitive-landscape.md. v2 evaluates competitive-intelligence.md; machine check found new contradictions (CAGR mismatch, SHEIN YoY label error) but 3 inconclusives (Coupang Farfetch, ASOS Topshop, ASOS AI stylist) and 1 minor contradiction (ASOS revenue −15% rounding) subsequently human-verified and accepted within the same run.
- Link Validity −7pp (v1→v2): v1 confirmed all bot-blocked URLs as accessible. v2 found SRC:sheingroup_wroclaw returning 404 (confirmed broken); 6 initially bot-blocked URLs human-verified as accessible in browser.
- Citation Coverage +27.2pp (v1→v2): The new competitive-intelligence.md file has substantially higher citation density than the prior competitive-landscape.md file.

---

**Score legend:**

| Metric | What it measures | How calculated |
|---|---|---|
| Quant Claims Accuracy Rate | % of all objective facts confirmed correct by their cited source | Confirmed ÷ (Confirmed + Contradicted). Inconclusive excluded. |
| Link Validity Rate | % of URLs in fact registry returning a working page | Working links ÷ total links. Broken = 4xx/5xx or unresolved redirect. |
| Citation Coverage Rate | % of filled fields with ≥1 [SRC:id] — presence only, not quality | Fields with citation ÷ filled fields. Source quality is H1/H2. |
| Field Recall Rate | % of template fields filled with real data. Labeled gaps count as intentional. | Filled fields ÷ total fields. Target: ≥90%. |
| Placeholder Text Violations | Template tokens still in the file — not filled or labeled as intentional gaps | Count. Target: 0. |
| Aggregator Label Violations | Crunchbase/PitchBook/Getlatka/SimilarWeb figures without [UNVERIFIED] | Count. Target: 0. |
| Banned Claim Pattern Instances | Unsupported superlatives without [SRC:id] — high hallucination risk | Count. Target: 0. |
| Stale Untagged Source Violations | Sources >2 years old not tagged [>2YR]. Stale + tagged is fine. | Count. Target: 0. |
| Uncited Quoted String Violations | Quoted consumer phrases in User Sentiment fields with no [SRC:id] — likely hallucinated from general knowledge | Count. Target: 0. |
| Competitor Count | Named direct competitors with a dedicated block in competitive-landscape.md | Raw count. Target: ≥3. |

---

**Quant Claims Accuracy detail (M-1):**

| Claim | Stated Value | Src | Result | Notes |
|---|---|---|---|---|
| TAM USD 125.68B (2025) | USD 125.68B | SRC:mordor_eu_ecommerce_cagr_2025 | Confirmed | |
| CAGR 4.25% (2025–2030), reaching USD 154.78B by 2030 | 4.25% / USD 154.78B / 2025–2030 | SRC:mordor_eu_ecommerce_cagr_2025 | **Contradicted** — source shows 4.20% / USD 160.89B / 2026–2031 | Fixed - cached data issue |
| Zalando acquired About You, July 2025 | July 2025 | SRC:retail_gazette_about_you_zalando | Confirmed | |
| Mytheresa acquired YNAP for $608M, October 2024 | $608M / Oct 2024 | SRC:pymnts_mytheresa_ynap | Confirmed | |
| Coupang completed Farfetch acquisition, January 2024 | January 2024 | SRC:coupang_ir_farfetch_acquisition | Confirmed | Human verified |
| ASOS sold 75% stake Topshop/Topman to Heartland for £135M (~$180M), September 2024 | 75% / £135M / Sep 2024 | SRC:asos_topshop_heartland_jv | Confirmed | Human verified |
| ASOS revenue £2.48B FY2025 (−15% YoY) | £2.48B / −15% | SRC:electroiq_asos_stats | Confirmed | Rounded value accepted |
| ASOS 6.5M active customers FY2025 (−8% YoY) | 6.5M / −8% | SRC:electroiq_asos_stats | **Contradicted** — electroiq confirms 6.5M but primary filing (Investegate) shows 17.0M | Agent updated to not quote aggregator sources|
| SHEIN 145.7M avg monthly EU users (Feb–Jul 2025, +15.2M YoY) | 145.7M / +15.2M / "YoY" | SRC:cedcommerce_shein_europe_users | **Contradicted** — +15.2M is vs prior 6-month period, not year-on-year | Agent updated to check durating of change without assuming YOY|
| Vinted GMV €10.8B (+47% YoY), Revenue €1.1B (+38% YoY) FY2025 | All stated values | SRC:vinted_newsroom_fy25 | Confirmed | |
| SHEIN Wrocław hub 740,000m² / 5,000 jobs | 740,000m² / 5,000 jobs | SRC:shein_wroclaw_hub, SRC:sheingroup_wroclaw | Confirmed — sacra.com confirms both. Note: SRC:sheingroup_wroclaw 404 | |
| Zalando GMV €17.6B (+14.7%), Revenue €12.3B (+16.8%), Adj. EBIT €591M (+15.6%), 62M customers | All stated values | SRC:worldfootwear_zalando_fy25_growth, SRC:zalando_fy25_results | Confirmed | |
| ASOS "Styled By You" AI stylist / 100,000 curated outfits / November 2025 | Feature name, outfit count, date | SRC:guardian_asos_ai_stylist | Confirmed | Human verified |
| Gap first major fashion brand checkout in Google Gemini, March 2026 | "first major" / March 2026 | SRC:gap_gemini_checkout | Inconclusive — 403 bot-blocked | |
| SHEIN Exchange resale platform in Europe (France first), June 2024 | France first / June 2024 | SRC:shein_exchange_europe_prnewswire | Confirmed | |

---

### Human Evaluation (HHH)

*Skipped — per user instruction.*

---

### Issues Found

#### Auto-fix issues

| ID | Section | Found | Should Be |
|---|---|---|---|
| M-1a | Market Overview — CAGR bullet 1 | `4.25% (2025–2030), reaching USD 154.78B by 2030 [Mordor Intelligence, 2025, SRC:mordor_eu_ecommerce_cagr_2025]` | `4.20% (2026–2031), reaching USD 160.89B by 2031 [Mordor Intelligence, 2025, SRC:mordor_eu_ecommerce_cagr_2025]` — source currently shows 4.20% CAGR for 2026–2031 period, USD 160.89B endpoint |
| M-1b | Competitive Summary Matrix — SHEIN row | `+15.2M YoY` | `+15.2M vs prior 6-month period` — source (CedCommerce) compares Feb–Jul 2025 to the prior 6-month period (Aug 2024–Jan 2025), not year-on-year |
| M-3 | Vinted Profile — Recent news 3 | `Exploring share sale at €8B valuation to allow early investors to exit [UNVERIFIED ESTIMATE — Silicon Republic, 2025, URL NOT RETRIEVED] | —` | Add `[SRC:vinted_sacra_2026]` to the source cell — sacra.com/c/vinted mentions €8B valuation/share sale context even though the Silicon Republic URL was not retrieved |

#### Flagged for human review

| ID | Section | Issue | Response |
|---|---|---|---|
| M-1c | Competitive Summary Matrix / ASOS Profile | ASOS 6.5M active customers: electroiq source states 6.5M but contradicts ASOS primary filing (Investegate: 17.0M, −14% YoY). Recommend correcting to 17.0M with primary source, or adding [UNVERIFIED] flag. | Fixed with new tiered searches prioriting pri source|
| M-2a | SRC:sheingroup_wroclaw | URL returned 404 — genuine break risk (not 403 bot-blocking). Underlying facts covered by SRC:shein_wroclaw_hub (sacra.com). If confirmed broken in browser, remove SRC:sheingroup_wroclaw from fact_registry. | Confirmed broken |
| M-3 | Citation coverage 84.8% | 7 fields lack inline [SRC:id] — borderline (citation present at section/row level but not cell level). See Citation Coverage Rate detail above for full list. | |

### Checks Passed

M-4 (Field Recall Rate 100% — all non-labeled fields filled), M-5 (no placeholder violations), M-6 (no aggregator label violations — PitchBook citation used for public company status, not a financial figure), M-7 (3 named direct competitor profiles — ASOS, SHEIN, Vinted — meets ≥3 target), M-8 (no banned claim patterns without citation), M-9 (no stale untagged source violations), M-10 (no User Sentiment section — N/A)
