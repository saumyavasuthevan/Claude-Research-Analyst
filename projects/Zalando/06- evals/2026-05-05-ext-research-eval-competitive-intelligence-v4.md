## Verification Report — Zalando / competitive-intelligence-v4.md

**Output type:** External Research (create-company)

**File verified:** competitive-intelligence-v4.md

**Fact registry:** Found — `fact_registry_competitive-intelligence-v4.json` (25 entries)

**Date verified:** 2026-05-05

---

### Machine Verification Results

**Rates (higher = better):**

| Metric | Score | Detail |
|---|---|---|
| Quant Claims Accuracy Rate | 100% | 2 correct / 2 checked (both Human-resolved) |
| Link Validity Rate | 100% | 19 working / 19 checkable. 5 bot-blocked confirmed by human (excluded from denominator). 1 URL_INCORRECT (no URL to check, excluded). |
| Citation Coverage Rate | 100% | 37 cited / 37 data-filled fields (labeled gaps excluded). 0 uncited fields. |
| Field Recall Rate | 100% | 37 filled / 37 resolvable fields (25 labeled [UNVERIFIED]/[SEARCH FAILED] excluded from denominator) |

**Violation counts (lower = better):**

| Metric | Count | Target |
|---|---|---|
| Placeholder Text Violations | 0 | 0 |
| Blocked Source Violations (KNOWN_BAD domain or invalid `source_type`) | 0 | 0 |
| Banned Claim Pattern Instances | 0 | 0 |
| Stale Untagged Source Violations | 0 | 0 |
| Uncited Quoted String Violations | N/A — no User Sentiment section | N/A |
| Competitor Count | 5 direct competitors | ≥ 3 |

---

### Score History

| Metric | v1 (2026-04-18) | v2 (2026-04-22) | v3 (2026-04-26) | v4 (2026-05-05) | Δ (v3→v4) |
|---|---|---|---|---|---|
| Quant Claims Accuracy | 83% | 80% | 66.7% | 100% | +33.3pp |
| Link Validity | 100% | 93% | 80.0% | 100% | +20pp |
| Citation Coverage | 57.6% | 84.8% | 100.0% | 100% | — |
| Field Recall | 100% | 100% | 100.0% | 100% | — |
| Placeholder violations | 0 | 0 | 0 | 0 | — |
| Blocked source violations | 0 | 0 | 0 | 0 | — |
| Banned patterns | 0 | 0 | 0 | 0 | — |
| Stale untagged | 0 | 0 | 0 | 0 | — |
| Uncited quotes | N/A | N/A | N/A | N/A | — |

*Rates: positive Δ = improvement. Violations: negative Δ = improvement.*

---

**Quant Claims Accuracy detail (M-1):**

| Claim | Stated Value | SRC | Result | Notes | Fix |
|---|---|---|---|---|---|
| ASOS FY2025 revenue | £2,477.8m | SRC:asos_fy25_rns | Confirmed — Human-resolved | Source (ASOS FY25 RNS, Nov 2025) shows £2,477.8m — exact match | None |
| ASOS FY2025 active customers | 6.5m | SRC:asos_fy25_rns | Confirmed — Human-resolved | Source shows 6.5m active customers (–8% YoY) — exact match | None |

---

### Human Evaluation (HHH)

*Raw Yes/No per criterion — aggregated across companies over time, not scored per company.*

**Honesty** — Accuracy and truthfulness

| Criteria | Yes / No |
|---|---|
| H1: Are any citations inaccurate or incomplete? | No |
| H2: Are any links inaccessible or unverifiable? | Yes — 5 URLs return 4xx to automated fetches; human confirmed all 5 are bot-blocked and accessible in browser |
| H3: Are any current-state qualitative claims poorly substantiated? | No |
| H4: Are any future-state claims presented with over-confidence? | No |

**Helpfulness** — Effectiveness in solving the PM's problem

| Criteria | Yes / No |
|---|---|
| He1: Does the report fail to provide novel information? | No |
| He2: Is the report not useful for framing insights or PM decisions? | No |

**Harmlessness** — Safe and appropriately framed

| Criteria | Yes / No |
|---|---|
| Ha1: Negative claims about the company lack sufficient evidence? | No |
| Ha2: Negative claims about competitors lack sufficient evidence? | No |

---

### Issues Found

#### Auto-fix issues

| ID | Section | Found | Should Be |
|---|---|---|---|
| — | — | No auto-fix issues | — |

#### Flagged for human review

| ID | Section | Issue | Response |
|---|---|---|---|
| M-2-F1 | Fact Registry — SRC:zalando_fy25_press_release | URL returns 4xx to automated fetch; human confirmed bot-blocked and accessible in browser. No URL retrieved — the registry entry records `[URL NOT RETRIEVED — 404]` as the URL string. The actual press release URL was never stored. | Consider manually retrieving and storing the correct URL when next accessing this source in a browser session. |
| M-2-F2 | Fact Registry — SRC:retail_gazette_zalando_about_you | Same as above — 404 to automated fetch, bot-blocked confirmed, actual URL not stored in registry. | Same recommendation as M-2-F1. |
| M-2-F3 | Fact Registry — SRC:guardian_asos_ai_stylist | Same as above — 404 to automated fetch, bot-blocked confirmed, actual URL not stored in registry. | Same recommendation as M-2-F1. |
| M-2-F4 | Fact Registry — SRC:retailtechhub_zalando_google_ucp | Same as above — 404 to automated fetch, bot-blocked confirmed, actual URL not stored in registry. | Same recommendation as M-2-F1. |
| M-2-F5 | Fact Registry — SRC:asos_topshop_heartland_jv | 403 to automated fetch, bot-blocked confirmed, actual URL not stored in registry. | Same recommendation as M-2-F1. |
| M-2-F6 | Fact Registry — SRC:coupang_farfetch | URL_INCORRECT — the v3 registry incorrectly stored the Zalando IR page as the source URL for the Coupang/Farfetch acquisition. Corrected to `[URL NOT RETRIEVED]` in v4, but no verified source URL has been found. The claim is tagged `[>2YR]` in the report body. | Source a verified URL for the Coupang acquisition of Farfetch (e.g. official press release or reliable news report) and update the registry entry. |

---

### All Checks — Results Summary

| Check | Result | Detail |
|---|---|---|
| M-1 Quant Claims Accuracy | 100% — 0 contradicted | 2 claims checked, both Human-resolved as confirmed |
| M-2 Link Validity | 100% — 0 broken | 19 working / 19 checkable. 5 bot-blocked (human-confirmed, excluded from denominator). 1 URL_INCORRECT (no URL, excluded). |
| M-3 Citation Coverage | 100% — 0 uncited fields | All 37 data-filled fields carry at least one SRC: citation |
| M-4 Field Recall Rate | 100% — above 90% threshold | 37 filled / 37 resolvable (25 labeled gaps excluded from denominator) |
| M-5 Placeholder Text | 0 violations | No residual template tokens found |
| M-6 Blocked Source Compliance | 0 violations | validate.py passed — no KNOWN_BAD domains, no invalid source_type values, no [VALIDATION_FAILED] tags |
| M-7 Competitor Count | 5 profiles — above minimum of 3 | ASOS, SHEIN, Vinted, Mytheresa/YNAP, Farfetch/Coupang |
| M-8 Banned Claim Patterns | 0 violations | No unsupported superlatives found without adjacent SRC citation |
| M-9 Stale Untagged Sources | 0 violations | No sources >2 years old found without [>2YR] tag |
| M-10 Uncited Quoted Strings | N/A — no User Sentiment section | File contains no User Sentiment section |

---

**Score legend:**

| Metric | What it measures | How calculated |
|---|---|---|
| Quant Claims Accuracy Rate | % of all objective facts confirmed correct by their cited source | Confirmed ÷ (Confirmed + Contradicted). Inconclusive excluded. |
| Link Validity Rate | % of URLs in fact registry returning a working page | Working links ÷ checkable links. Bot-blocked (4xx confirmed accessible in browser) and URL_INCORRECT entries excluded from denominator. |
| Citation Coverage Rate | % of filled fields with ≥1 [SRC:id] — presence only, not quality | Fields with citation ÷ filled fields. Source quality is H1/H2. |
| Field Recall Rate | % of template fields filled with real data. Labeled gaps count as intentional. | Filled fields ÷ total fields. Target: ≥90%. |
| Placeholder Text Violations | Template tokens still in the file — not filled or labeled as intentional gaps | Count. Target: 0. |
| Blocked Source Violations | KNOWN_BAD domain sources in fact registry or report body, or invalid `source_type` values. Each `[VALIDATION_FAILED]` tag also counts. | Count. Target: 0. |
| Banned Claim Pattern Instances | Unsupported superlatives without [SRC:id] — high hallucination risk | Count. Target: 0. |
| Stale Untagged Source Violations | Sources >2 years old not tagged [>2YR]. Stale + tagged is fine. | Count. Target: 0. |
| Uncited Quoted String Violations | Quoted consumer phrases in User Sentiment fields with no [SRC:id] — likely hallucinated from general knowledge | Count. Target: 0. |
| Competitor Count | Named direct competitors with a dedicated block in competitive-intelligence-v4.md | Raw count. Target: ≥3. |
