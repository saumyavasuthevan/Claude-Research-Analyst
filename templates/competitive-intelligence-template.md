# [Company Name] Competitive Intelligence

<!-- CLAUDE CODE INSTRUCTIONS
This template is designed for LLM-sourced research via web search (Brave Search API).
Every field maps to a specific findable fact. Synthesis stays with the PM.

RULES:
1. Every cell with a value must have a [SRC:id] citation. Every fact_registry entry must include "source_type": "tier1_official" or "tier2_news".
2. If searched but no tier1_official/tier2_news source found: [UNVERIFIED — no primary source found as of date]. If search returned no results at all: [SEARCH FAILED — as of date]. Never construct an estimate.
3. Pricing: pricing model label (e.g., "subscription tiers", "per seat", "commission %") from company website or G2 only. Never cite aggregator sites (Accio, PriceRunner, etc.).
4. Trend response cells — must cite a specific news article. "No public signal" is valid. Never infer an action from general product knowledge.
5. CAGR and market size figures must be verified against the source page, not taken from memory.
6. No raw URLs anywhere. Register all sources in fact_registry_competitive-intelligence.json and cite by SRC:id.
7. After saving this file, run: python3 scripts/validate.py fact_registry_competitive-intelligence.json && python3 scripts/render.py fact_registry_competitive-intelligence.json >> competitive-intelligence.md
-->

**Market:** [Market name]
**Research date:** [YYYY-MM-DD] — re-verify all figures after 90 days.

---

## 1. Market Overview

**TAM:** $[X]B [Source name, Year, SRC:id]
**CAGR:** [X]% ([start year]–[end year]) [Source name, Year, SRC:id]
**Industry outlook:** [One sentence: growing / stable / contracting and why — sourced from the same analyst report.]

<!-- Search: "[industry] market size CAGR 2025 2026 [analyst firm]"
Source from: Mordor Intelligence, Grand View Research, Gartner, Statista, trade press.
Verify the exact CAGR figure against the source page — do not use a cached or remembered figure. -->

**M&A activity (last 24 months):**
- [Acquirer] acquired [Target], [Month YYYY] — [SRC:id]
- [SEARCH FAILED — no M&A activity retrieved as of date]

**Funding rounds in this space (last 12 months):**
- [Company] raised $[X]m [Series X], [Month YYYY] — [SRC:id]
- [SEARCH FAILED — no funding rounds retrieved as of date]

<!-- Named, cited events only. No editorial conclusions. Each bullet must include a SRC:id. -->

---

## 2. Market Trends

<!-- Search: "[industry] trends 2025 2026" for trend identification.
For each trend, run: "[trend keyword] [Competitor1] OR [Competitor2] 2024 2025" to find named competitor actions.
Each trend table must include at least 2 competitors with a confirmed named action (sourced from a news article or press release). If fewer than 2 confirmed actions are found, keep searching before writing the trend — or drop the trend and replace it with one that has sufficient evidence.
Competitors in each trend table are not limited to the 3 closest competitors in the summary matrix — include any named competitor for whom a relevant action was found.
Trend source: cite [SRC:id] at the end of the body sentence — not in the heading.
Response cell: embed [SRC:id] inline at the end of the named action — no separate Source column.
"No public signal as of [date]" is a valid cell value for additional rows beyond the 2 required confirmed examples. -->

### Trend 1: [Trend name]

[One sentence: what is happening in the market — sourced from analyst report or trade press. [SRC:id]]

| Competitor | Response |
|---|---|
| [Name] | [Specific named action — e.g., "Launched X feature, Month YYYY [SRC:id]"] |
| [Name] | [No public signal as of YYYY-MM-DD] |
| [Name] | [SEARCH FAILED] |

---

### Trend 2: [Trend name]

[One sentence. [SRC:id]]

| Competitor | Response |
|---|---|
| [Name] | [Action [SRC:id]] |
| [Name] | [No public signal as of YYYY-MM-DD] |

---

### Trend 3: [Trend name]

[One sentence. [SRC:id]]

| Competitor | Response |
|---|---|
| [Name] | [Action [SRC:id]] |
| [Name] | [No public signal as of YYYY-MM-DD] |

---

### Trend 4: [Trend name]

[One sentence. [SRC:id]]

| Competitor | Response |
|---|---|
| [Name] | [Action [SRC:id]] |
| [Name] | [No public signal as of YYYY-MM-DD] |

---

### Trend 5: [Trend name]

[One sentence. [SRC:id]]

| Competitor | Response |
|---|---|
| [Name] | [Action [SRC:id]] |
| [Name] | [No public signal as of YYYY-MM-DD] |

---

*(Add Trend 6 if found — otherwise delete this line)*

---

## 3. Competitive Summary Matrix

<!-- 3 closest competitors + subject company. All cells must contain a single findable fact with SRC:id.
"Latest signal" = most recent named news event only (last 12 months).
No synthesis cells. -->

| Company | Founded | HQ | Stage / Funding | Revenue or GMV | Customers | Latest signal |
|---|---|---|---|---|---|---|
| **[Company Name] (us)** | [Year] | [City] | [Stage, $Xm raised, SRC:id] | [$X, FYXX, SRC:id] | [X, SRC:id] | [Event, SRC:id] |
| **[Competitor 1]** | [Year] | [City] | [Stage, $Xm raised, SRC:id] | [$X, FYXX, SRC:id] | [X, SRC:id] | [Event, SRC:id] |
| **[Competitor 2]** | [Year] | [City] | [Stage, $Xm raised, SRC:id] | [$X, FYXX, SRC:id] | [X, SRC:id] | [Event, SRC:id] |
| **[Competitor 3]** | [Year] | [City] | [Stage, $Xm raised, SRC:id] | [$X, FYXX, SRC:id] | [X, SRC:id] | [Event, SRC:id] |

---

## 4. Competitor Profiles

<!-- One table per competitor — 3 closest competitors only (matching the summary matrix).
Every row with a value requires a SRC:id.
Recent news = last 12 months only. If nothing found: [SEARCH FAILED — no news retrieved as of date].
Pricing model: subscription tiers, per-seat, commission %, free+premium, etc. — from company website or G2.
  Use [UNVERIFIED — no primary source found] if not stated publicly. Use N/A only if the company has no structured pricing model.
Do not add rows for price range, weaknesses, target market, or differentiation. -->

### [Competitor 1]

| Field | Value | Source |
|---|---|---|
| Founded | [Year], [City] | SRC:id |
| Stage | [e.g., Public / Series C / $Xm raised] | SRC:id |
| Revenue / GMV | [$X, FYXX, ±X% YoY] | SRC:id |
| Customers | [X active / registered — specify which] | SRC:id |
| Employees | [~X] | SRC:id |
| Product | [One sentence from company website] | SRC:id |
| Pricing model | [e.g., "subscription tiers", "per seat, annual", "commission %"] OR [UNVERIFIED — no primary source found as of date] OR N/A | SRC:id or — |
| Recent news 1 | [Named event, Month YYYY] | SRC:id |
| Recent news 2 | [Named event, Month YYYY] | SRC:id |
| Recent news 3 | [Named event, Month YYYY] OR [SEARCH FAILED — no news retrieved as of date] | SRC:id or — |

---

### [Competitor 2]

| Field | Value | Source |
|---|---|---|
| Founded | [Year], [City] | SRC:id |
| Stage | [Stage] | SRC:id |
| Revenue / GMV | [$X, FYXX, ±X% YoY] | SRC:id |
| Customers | [X — specify active / registered] | SRC:id |
| Employees | [~X] | SRC:id |
| Product | [One sentence from company website] | SRC:id |
| Pricing model | [e.g., "subscription tiers", "per seat, annual", "commission %"] OR [UNVERIFIED — no primary source found as of date] OR N/A | SRC:id or — |
| Recent news 1 | [Named event, Month YYYY] | SRC:id |
| Recent news 2 | [Named event, Month YYYY] | SRC:id |
| Recent news 3 | [Named event, Month YYYY] OR [SEARCH FAILED — no news retrieved as of date] | SRC:id or — |

---

### [Competitor 3]

| Field | Value | Source |
|---|---|---|
| Founded | [Year], [City] | SRC:id |
| Stage | [Stage] | SRC:id |
| Revenue / GMV | [$X, FYXX, ±X% YoY] | SRC:id |
| Customers | [X — specify active / registered] | SRC:id |
| Employees | [~X] | SRC:id |
| Product | [One sentence from company website] | SRC:id |
| Pricing model | [e.g., "subscription tiers", "per seat, annual", "commission %"] OR [UNVERIFIED — no primary source found as of date] OR N/A | SRC:id or — |
| Recent news 1 | [Named event, Month YYYY] | SRC:id |
| Recent news 2 | [Named event, Month YYYY] | SRC:id |
| Recent news 3 | [Named event, Month YYYY] OR [SEARCH FAILED — no news retrieved as of date] | SRC:id or — |

---

---

## Label Legend

| Label | Meaning |
|---|---|
| `[UNVERIFIED — no primary source found as of date]` | Searched but no tier1_official or tier2_news source found. Field was actively searched — data is unverifiable, not forgotten. |
| `[UNVERIFIED — sourced from subject-company materials only]` | Competitor claim sourced only from the subject company's own materials. Not independently verified. |
| `[SEARCH FAILED — as of date]` | Search query returned no results for this field. |
| `[>2YR — last confirmed date, SRC:id]` | Most recent source is older than 2 years. Re-verify before use. |
| `[ASSUMPTION — reasoning: ...]` | Inferred from multiple sources but not explicitly stated by any single source. |
| `[URL NOT RETRIEVED]` | Source retrieved but URL was not returned by the search tool. |

*Source Registry appendix (generated by `scripts/render.py`) lists every source with type badge (`tier1_official` / `tier2_news`) and any confidence notes.*

<!-- Last verified: [YYYY-MM-DD] -->
