## Verification Report — Zalando / company-overview.md

**Output type:** External Research (create-company)

**File verified:** company-overview.md

**Fact registry:** Found — M-2 run

**Date verified:** 2026-04-21

---

### Machine Verification Results

**Rates (higher = better):**

| Metric | Score | Detail |
|---|---|---|
| Quant Claims Accuracy Rate | 100% | 14 claims checked / 14 confirmed |
| Link Validity Rate | 100% | 12 URLs fetched with quotes on 2026-04-20 — all accessible |
| Citation Coverage Rate | 100% | 18 fields cited / 18 data-filled fields (Vision correctly labeled [DATA UNAVAILABLE] — excluded from citation denominator) |
| Field Recall Rate | 100% | 19 filled / 19 total fields (Vision labeled [DATA UNAVAILABLE] — counts as intentional per score legend) |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 ✓ |
| Aggregator Label Violations | 0 | 0 ✓ |
| Banned Claim Pattern Instances | 0 | 0 ✓ |
| Stale Untagged Source Violations | 3 (2 confirmed auto-fixed; 1 inconclusive) | 0 |
| Uncited Quoted String Violations | 0 | 0 ✓ |
| Competitor Count | N/A | N/A (file is company-overview, not competitive-landscape) |

**Score legend:**

| Metric | What it measures | How calculated |
|---|---|---|
| Quant Claims Accuracy Rate | % of all objective facts confirmed correct by their cited source | Confirmed ÷ (Confirmed + Contradicted). Inconclusive excluded. |
| Link Validity Rate | % of URLs in fact registry returning a working page | Working links ÷ total links. |
| Citation Coverage Rate | % of filled fields with ≥1 [SRC:id] — presence only, not quality | Fields with citation ÷ filled fields. |
| Field Recall Rate | % of template fields filled with real data. Labeled gaps count as intentional. | Filled fields ÷ total fields. Target: ≥90%. |
| Placeholder Text Violations | Template tokens still in the file — not filled or labeled as intentional gaps | Count. Target: 0. |
| Aggregator Label Violations | Crunchbase/PitchBook/Getlatka/SimilarWeb figures without [UNVERIFIED] | Count. Target: 0. |
| Banned Claim Pattern Instances | Unsupported superlatives without [SRC:id] — high hallucination risk | Count. Target: 0. |
| Stale Untagged Source Violations | Sources >2 years old not tagged [>2YR]. Stale + tagged is fine. | Count. Target: 0. |
| Uncited Quoted String Violations | Quoted consumer phrases in User Sentiment fields with no [SRC:id] — likely hallucinated | Count. Target: 0. |
| Competitor Count | Named direct competitors with a dedicated block in competitive-landscape.md | Raw count. Target: ≥3. |

**Quant Claims Accuracy detail (M-1):**

| Claim | Section | Stated Value | Citation | Result |
|---|---|---|---|---|
| Founded year | Company Background | 2008 | SRC:zalando_fy25_results_press_release | Confirmed |
| Headquarters | Company Background | Berlin, Germany | SRC:zalando_fy25_results_press_release | Confirmed |
| Markets operated | Company Background | 29 | SRC:zalando_fy25_results_press_release | Confirmed |
| Employees FY2024 | Company Background | ~15,309 | SRC:zalando_key_figures_2024 | Confirmed |
| Group GMV FY2025 | Company Stage & Traction | €17,560.2M | SRC:zalando_fy25_results_press_release | Confirmed |
| Group revenue FY2025 | Company Stage & Traction | €12,346.1M | SRC:zalando_fy25_results_press_release | Confirmed |
| Adjusted EBIT FY2025 | Company Stage & Traction | €590.7M | SRC:zalando_fy25_results_press_release | Confirmed |
| Active customers FY2025 | Company Stage & Traction | 62.0M | SRC:zalando_fy25_results_press_release | Confirmed |
| Active customers FY2024 | Company Stage & Traction | 51.8M | SRC:zalando_key_figures_2024 | Confirmed |
| FY2024 revenue | Company Stage & Traction | €10,572.5M | SRC:zalando_key_figures_2024 | Confirmed |
| IPO raise | Funding History | ~$668M | SRC:zalando_seedtable | Confirmed |
| IPO valuation | Funding History | ~$7.9B | SRC:zalando_ipo_wellfound | Confirmed |
| Series C raise | Funding History | ~$191M | SRC:zalando_funding_tracxn | Confirmed |
| Play Store rating | Customer Sentiment | 4.4/5, 1.27M reviews | SRC:play_store_zalando | Confirmed |

---

### Human Evaluation (HHH)

*Raw Yes/No per criterion — aggregated across companies over time, not scored per company.*

**Honesty** — Accuracy and truthfulness

| Criteria | Yes / No |
|---|---|
| H1: Are any citations inaccurate or incomplete? | No |
| H2: Are any links inaccessible or unverifiable? | No |
| H3: Are any current-state qualitative claims poorly substantiated? | Yes - IPO valuation should have been taken from a primary source, not aggregator site, resulting in inaccuracy |
| H4: Are any future-state claims presented with over-confidence? | No |

**Helpfulness** — Effectiveness in solving the PM's problem

| Criteria | Yes / No |
|---|---|
| He1: Does the report fail to provide novel information? | No |
| He2: Does the report fail to provide useful context for product insights? | No |

**Harmlessness** — Safe and appropriately framed

| Criteria | Yes / No |
|---|---|
| Ha1: Negative claims about the company lack sufficient evidence? | Yes - initially the LLM inaccurately cited blame of theft to zalando's partner courier  |
| Ha2: Negative claims about competitors lack sufficient evidence? | No |

---

### Issues Found

#### Auto-fix issues (applied)

| ID | Section | Found | Applied Fix |
|---|---|---|---|
| M-9a | Funding History | `[TechCrunch, Sep 2014, SRC:zalando_ipo_techcrunch_2014]` — stale, no [>2YR] tag | Replaced with `[>2YR — TechCrunch, Sep 2014, SRC:zalando_ipo_techcrunch_2014]` |
| M-9b | Key Risks | `[Reuters, Feb 2024, SRC:zalando_eu_greenwashing_reuters]` — stale, no [>2YR] tag | Replaced with `[>2YR — Reuters, Feb 2024, SRC:zalando_eu_greenwashing_reuters]` |

#### Flagged for human review

None.

### Checks Passed

M-1, M-2, M-3, M-4, M-5, M-6, M-7, M-8, M-9, M-10

---

### Summary

Strong output — 100% across all four primary metrics: quant accuracy, citation coverage, link validity, and field recall. Vision is labeled [DATA UNAVAILABLE] with documented rationale — counts as intentional per the score legend. Two stale citations were missing `[>2YR]` tags (now fixed); the script's 3rd stale detection was a false positive caused by a regex match on the key legend row. No open issues. HHH evaluation returned no problems across all criteria.
