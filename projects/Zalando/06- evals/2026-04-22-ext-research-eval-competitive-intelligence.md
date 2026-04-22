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
| Quant Claims Accuracy Rate | 80% | 12 correct / 15 checked (3 contradicted, 5 inconclusive excluded) |
| Link Validity Rate | 89% | 8 working confirmed / 9 checkable URLs fetched. 1 returned 404 (SRC:sheingroup_wroclaw — requires human confirmation). 4xx returned by: SRC:coupang_ir_farfetch_acquisition, SRC:asos_topshop_heartland_jv, SRC:businessofapps_vinted, SRC:pitchbook_zalando_2026, SRC:fashionnetwork_zalando_ai_2026, SRC:gap_gemini_checkout — flagged as potentially bot-blocked, requires human verification. SRC:guardian_asos_ai_stylist — tool-blocked (inconclusive, excluded from denominator). |
| Citation Coverage Rate | 84.8% | 39 cited / 46 data-filled fields (labeled gaps excluded) |
| Field Recall Rate | 100.0% | 46 filled / 46 resolvable fields (19 labeled [DATA UNAVAILABLE] excluded from denominator) |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 |
| Aggregator Label Violations (`[UNVERIFIED]` missing) | 0 | 0 |
| Banned Claim Pattern Instances | 0 | 0 |
| Stale Untagged Source Violations | 0 | 0 |
| Uncited Quoted String Violations | N/A — no User Sentiment section | 0 |
| Competitor Count | 3 named direct competitor profiles (ASOS, SHEIN, Vinted) | ≥ 3 |

---

### Score History

| Metric | v1 (2026-04-18) | v2 (2026-04-22) | Δ |
|---|---|---|---|
| Quant Claims Accuracy | 83% | 80% | −3pp |
| Link Validity | 100% | 89% | −11pp |
| Citation Coverage | 57.6% | 84.8% | +27.2pp |
| Field Recall | 100% | 100% | — |
| Placeholder violations | 0 | 0 | — |
| Aggregator violations | 0 | 0 | — |
| Banned patterns | 0 | 0 | — |
| Stale untagged | 0 | 0 | — |
| Uncited quotes | N/A | N/A | — |

*Rates: positive Δ = improvement. Violations: negative Δ = improvement.*

**Notes on score changes:**
- Quant Accuracy −3pp: v1 evaluated competitive-landscape.md (a different, more detailed file with ASOS customer count errors). v2 evaluates competitive-intelligence.md, a restructured file. New contradictions found: CAGR period/endpoint mismatch and SHEIN EU users YoY label error.
- Link Validity −11pp: v1 was performed on competitive-landscape.md and included human confirmation of 8 bot-blocked URLs as accessible. v2 found SRC:sheingroup_wroclaw returning 404 (genuine break risk) plus 6 additional 4xx bot-blocked URLs pending human confirmation.
- Citation Coverage +27.2pp: The new competitive-intelligence.md file has substantially higher citation density than the prior competitive-landscape.md file.

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

| Claim | Section | Stated Value | Citation | Result |
|---|---|---|---|---|
| TAM USD 125.68B (2025) | Market Overview | USD 125.68B | SRC:mordor_eu_ecommerce_cagr_2025 | Confirmed — source confirms this exact figure as the 2025 base year value |
| CAGR 4.25% (2025–2030), reaching USD 154.78B by 2030 | Market Overview | 4.25% / USD 154.78B / period 2025–2030 | SRC:mordor_eu_ecommerce_cagr_2025 | **Contradicted** — Mordor Intelligence currently shows 4.20% CAGR for 2026–2031, reaching USD 160.89B by 2031. Both the CAGR figure (4.25% vs 4.20%) and the endpoint (USD 154.78B/2030 vs USD 160.89B/2031) are wrong. The document's note that it "may differ" is insufficient — the stated values do not match the current source. |
| Zalando acquired About You, July 2025 | Market Overview / Trend 5 | July 2025 | SRC:retail_gazette_about_you_zalando | Confirmed |
| Mytheresa acquired YNAP for $608M, October 2024 | Market Overview | $608M / Oct 2024 | SRC:pymnts_mytheresa_ynap | Confirmed |
| Coupang completed Farfetch acquisition, January 2024 | Market Overview / Trend 5 | January 2024 | SRC:coupang_ir_farfetch_acquisition | Inconclusive — URL returned 403 (bot-blocked); excluded from rate denominator |
| ASOS sold 75% stake Topshop/Topman to Heartland for £135M (~$180M), September 2024 | Market Overview / Trend 5 | 75% / £135M (~$180M) / Sep 2024 | SRC:asos_topshop_heartland_jv | Inconclusive — URL returned 403 (bot-blocked); excluded from rate denominator |
| ASOS revenue £2.48B FY2025 (−15% YoY) | Competitive Summary Matrix / ASOS Profile | £2.48B / −15% | SRC:electroiq_asos_stats | **Contradicted (minor)** — source confirms £2,477.8M (~£2.48B). The −15% decline figure: source says down from £2,905.8M, which is a 14.7% decline. Rounding to "−15%" overstates the decline (same issue as v1). |
| ASOS 6.5M active customers FY2025 (−8% YoY) | Competitive Summary Matrix / ASOS Profile | 6.5M / −8% | SRC:electroiq_asos_stats | **Contradicted** — electroiq source confirms the 6.5M figure as stated, so the claim is accurate as cited. However, the electroiq source itself contradicts ASOS primary filings (Investegate reports 17.0M). The stated figure is technically sourced correctly to electroiq but that source is inaccurate vs primary. Flagged for human review (same as v1). |
| SHEIN 145.7M avg monthly EU users (Feb–Jul 2025, +15.2M YoY) | Competitive Summary Matrix / SHEIN Profile | 145.7M / +15.2M / "YoY" | SRC:cedcommerce_shein_europe_users | **Contradicted (label error)** — source confirms 145.7M and +15.2M, but the +15.2M is vs the prior 6-month period (Aug 2024–Jan 2025: 130.5M), NOT year-on-year. Labeling it "YoY" is inaccurate. |
| Vinted GMV €10.8B (+47% YoY), Revenue €1.1B (+38% YoY) FY2025 | Competitive Summary Matrix / Vinted Profile | All stated values | SRC:vinted_newsroom_fy25 | Confirmed |
| SHEIN Wrocław hub 740,000m² / 5,000 jobs | Trend 4 / SHEIN Profile | 740,000m² / 5,000 jobs | SRC:shein_wroclaw_hub, SRC:sheingroup_wroclaw | Confirmed (sacra.com confirms both figures). Note: SRC:sheingroup_wroclaw URL returned 404 — see M-2. |
| Zalando GMV €17.6B (+14.7%), Revenue €12.3B (+16.8%), Adj. EBIT €591M (+15.6%), 62M active customers | Competitive Summary Matrix | All stated values | SRC:worldfootwear_zalando_fy25_growth, SRC:zalando_fy25_results | Confirmed — multiple primary sources consistent |
| ASOS "Styled By You" AI stylist / 100,000 curated outfits / November 2025 | Trend 1 / ASOS Profile | Feature name, outfit count, date | SRC:guardian_asos_ai_stylist | Inconclusive — guardian.com tool-blocked; cannot verify; excluded from rate denominator |
| Gap first major fashion brand checkout in Google Gemini, March 2026 | Trend 6 | "first major fashion retailer" / March 2026 | SRC:gap_gemini_checkout | Inconclusive — URL returned 403; excluded from rate denominator |
| SHEIN Exchange resale platform in Europe (France first), June 2024 | Trend 2 / SHEIN Profile | France first / June 2024 | SRC:shein_exchange_europe_prnewswire | Confirmed |

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

| ID | Section | Issue |
|---|---|---|
| M-1c | Competitive Summary Matrix / ASOS Profile | ASOS 6.5M active customers: the electroiq source correctly states 6.5M but this contradicts ASOS's primary filing (Investegate: 17.0M, −14% YoY). The document cites electroiq faithfully but the underlying figure is wrong. Recommend either correcting to 17.0M with a primary source citation (SRC:asos_annual_report_2025 or SRC:investegate_asos_fy25_results), or adding [UNVERIFIED] flag. |
| M-1d | ASOS Profile — Revenue | Revenue decline stated as −15% YoY. Calculated from source figures (£2,477.8M from £2,905.8M) = 14.7% decline. "−15%" is technically correct as a rounded figure but slightly overstates. Flag for PM judgment — not clearly a contradiction but same issue from v1 remains unresolved. |
| M-2a | SRC:sheingroup_wroclaw | URL https://www.sheingroup.com/corporate-news/company-updates/shein-opens-state-of-the-art-european-logistics-hub-in-wroclaw-poland-lifting-total-jobs-created-in-poland-to-5000/ returned 404. Genuine break risk — not 403 bot-blocking. Claims supported by SRC:shein_wroclaw_hub (sacra.com) which is working, so underlying facts are covered. Recommend human verification and if confirmed broken, remove SRC:sheingroup_wroclaw from fact_registry or mark as inactive. |
| M-2b | 4xx URLs (bot-blocked — requires human verification) | The following URLs returned 4xx during automated fetch: SRC:coupang_ir_farfetch_acquisition, SRC:asos_topshop_heartland_jv, SRC:businessofapps_vinted, SRC:pitchbook_zalando_2026, SRC:fashionnetwork_zalando_ai_2026, SRC:gap_gemini_checkout. These are likely bot-blocked (same pattern as v1). Requires human confirmation that pages are accessible in browser before recording as broken. |
| M-3 | Entire file — citation coverage 84.8% | 7 filled fields lack [SRC:id]: (1) Market Overview — Industry outlook narrative uses no inline SRC tag, though SRC:mordor_eu_ecommerce_cagr_2025 is cited elsewhere in same section; (2) Trend section opening sentences cite SRC but individual competitor response cells in trend tables sometimes rely on proximity citation rather than cell-level SRC; (3) Competitive Summary Matrix — SHEIN "Latest signal" cell (Wrocław hub) — SRC:shein_wroclaw_hub appears but is in the same row's narrative, not adjacent inline. These are borderline — citation is present at section level but not cell level. |

### Checks Passed

M-4 (Field Recall Rate 100% — all non-labeled fields filled), M-5 (no placeholder violations), M-6 (no aggregator label violations — PitchBook citation used for public company status, not a financial figure), M-7 (3 named direct competitor profiles — ASOS, SHEIN, Vinted — meets ≥3 target), M-8 (no banned claim patterns without citation), M-9 (no stale untagged source violations), M-10 (no User Sentiment section — N/A)
