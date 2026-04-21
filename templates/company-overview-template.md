# [Company Name] Company Overview

<!-- CLAUDE CODE INSTRUCTIONS
This template is designed for LLM-sourced research via web search (Brave Search API).

RULES:
1. Every cell with a value must have a [SRC:id] citation.
2. If a fact cannot be found, write [DATA UNAVAILABLE — as of date]. Never construct an estimate.
3. Competitor analysis: do not include — covered in competitive-intelligence.md.
4. Pricing: do not include — covered in product-description.md.
5. Strategic priorities and OKRs: only include if explicitly stated in a press release, earnings call, or investor update — not inferred from product announcements.
6. No raw URLs anywhere. Register all sources in fact_registry_company-overview.json and cite by SRC:id.
-->

*Last verified: [YYYY-MM-DD]*

---

## Company Background

<!-- Search: "[Company Name] founded year headquarters employees countries operates"
Source from LinkedIn, Crunchbase, company website, or press releases. -->

| Field | Value |
|---|---|
| Founded | [Year] [SRC:id] |
| Headquarters | [City, Country] [SRC:id] |
| Operates in | [Country 1, Country 2, ... OR N markets] [SRC:id] |
| Stage | [Pre-seed / Seed / Series A / Public — include total raised, e.g., "Series B ($45M raised)"] [SRC:id] |
| Employees | [~X] [SRC:id] |

### Leadership Team

<!-- Search: "[Company Name] CEO CPO leadership team"
Source from LinkedIn or company About page.
List named C-suite leaders only. Do not estimate headcount per department. -->

- [Name] — [Title] [SRC:id]
- [Name] — [Title] [SRC:id]

*(Label [DATA UNAVAILABLE — as of date] if leadership is not publicly listed)*

---

## Company Mission

<!-- Search: "[Company Name] mission vision values"
Source directly from company website. Quote verbatim where possible. -->

**Mission:** [Quote verbatim from company website] [SRC:id]
**Vision:** [Quote verbatim — or DATA UNAVAILABLE] [SRC:id]

*(Label [DATA UNAVAILABLE — as of date] if values aren't publicly stated)*

---

## Company Stage & Traction

### Current Metrics ([Most Recent Quarter/Year Available])

<!-- Search: "[Company Name] ARR revenue customers users growth"
Use press releases, earnings calls (if public), or credible news coverage.
Label [DATA UNAVAILABLE — as of date] for any metric not publicly stated. -->

**Customers:** [X active / registered — specify which] [SRC:id]
**Revenue / GMV:** $[X] [ARR / GMV / revenue — specify which, FYXX] [SRC:id]
**Growth:** [X]% YoY [SRC:id]

### Funding History

<!-- Search: "[Company Name] funding rounds investors Crunchbase"
List each round chronologically. Apply labelling rules per create-company.md for aggregator-sourced figures.
If last round >24 months ago, flag: ⚠️ Last disclosed funding is >24 months old — treat as a material signal. -->

| Round | Year | Amount | Lead investor |
|---|---|---|---|
| [Round name] | [YYYY] | $[X]M | [Investor name] [SRC:id] |

*(Label [DATA UNAVAILABLE — as of date] if round details are unconfirmed)*

---

## Market Position

### Target Market

<!-- Search: "[Company Name] target customers ideal customer profile market segment"
Source from company website, case studies, or sales pages.
Market sizing (TAM, CAGR) is in competitive-intelligence.md — do not duplicate here. -->

**Primary:** [Customer segment — size, industry, role, need] [SRC:id]
**Secondary:** [Secondary segment] [SRC:id]

*(Label [DATA UNAVAILABLE] if not publicly stated)*

---

## Key Risks & Challenges

<!-- Search: "[Company Name] lawsuit regulatory risk churn challenge"
Categorise under the three headings below.
Label [DATA UNAVAILABLE — as of date] for any category with no public signals. -->

### Market Risks
- **[Risk 1]:** [Description — e.g., category commoditisation, macro headwinds] [SRC:id]

### Operational Risks
- **[Risk 1]:** [Description — e.g., key-person dependency, execution capacity] [SRC:id]

### Regulatory & Reputational Risks
- **[Risk 1]:** [Description — e.g., pending litigation, data privacy exposure] [SRC:id]

---

## Customer Sentiment

<!-- METHODOLOGY: Reflexive thematic analysis (Braun & Clarke 2021) — deductive codebook + inductive open coding
     DATA SOURCES: Bright Data MCP (Reddit, Twitter/X, Instagram, Facebook) + search_engine → scrape_as_markdown (G2, Trustpilot)
     TOKEN BUDGET: Collect ≤30 verbatims; single extraction pass; suppress themes with <2 verbatims -->

### Data Collection

<!-- Bright Data MCP tools:
     Reddit:    web_data_reddit_posts — query: "[Company Name]"
     Twitter/X: web_data_x_posts — query: "[Company Name]"
     Instagram: web_data_instagram_posts + web_data_instagram_comments — query: "[Company Name]"
     Facebook:  web_data_facebook_posts + web_data_facebook_company_reviews — query: "[Company Name]"
     Reviews:   search_engine — "[Company Name] reviews site:g2.com OR site:trustpilot.com" → scrape_as_markdown

     Collect: post text + platform + date. Filter to brand/product mentions only. Only include items published within the past 2 years.

     ANTI-HALLUCINATION — verbatim registry:
     Before any analysis, write ALL collected quotes to:
       03- research/quotes_registry.json   ← distinct from fact_registry.json (which stores URLs only)

     Format:
       { "id": "Q001", "text": "exact quote copied verbatim", "platform": "Reddit", "date": "YYYY-MM-DD" }

     IDs: Q001, Q002, ... (Q-prefix distinguishes from fact registry F-IDs)
     Rule: never write quote text directly in analysis. Reference IDs only. Resolve IDs to text at render time. -->

**If B2B:** Collect in priority order. Stop once 30 items collected. Cap: 30 items per platform.

| Priority | Platform | Items collected | Date range |
|---|---|---|---|
| 1 | G2 | [N] | [range] |
| 2 | Trustpilot | [N] | [range] |
| 3 | LinkedIn | [N] | [range] |
| 4 | Reddit | [N] | [range] |


**If B2C:** Collect in priority order. Stop once 30 items collected. Cap: 30 items per platform.

| Priority | Platform | Items collected | Date range |
|---|---|---|---|
| 1 | Trustpilot | [N] | [range] |
| 2 | Reddit | [N] | [range] |
| 3 | Play Store | [N] | [range] |
| 4 | App Store | [N] | [range] |
| 5 | Twitter/X | [N] | [range] |
| 6 | Instagram | [N] | [range] |

*Minimum to proceed with thematic analysis: **30 items** (B2B) / **30 items** (B2C) across all platforms. If below threshold, replace Thematic Analysis section with: `[INSUFFICIENT DATA — fewer than [N] verbatims collected as of [date]. Thematic analysis not conducted.]`*

### Thematic Analysis

<!-- STEP 1 — Sentiment classification (before deriving themes):
     Classify each Q-ID as Positive or Negative from text signal.
     Record split: negative_n, negative_pct, positive_n, positive_pct.

     STEP 2 — Theme derivation within each sentiment group separately:
     Deductive pass: assign each Q-ID to nearest codebook theme.
     Inductive pass: code residuals that don't fit → candidate new themes.
     Suppress themes with <2 verbatims.

     STEP 3 — Sub-theme derivation within each theme (2–4 sub-themes):
     Name sub-themes as specific problem/praise descriptions, not restatements of the theme.
     A sub-theme = one distinct user pain or praise that maps to a distinct fix/action.
     MERGE RULE: if two candidate sub-themes require the same operational fix, merge them into one sub-theme — even if the failure modes look different on the surface.
     SPLIT RULE: only split if the two patterns require genuinely different fixes (e.g. courier-caused non-delivery → fix courier SLA; Zalando dispatch failure → fix warehouse process — these are distinct).
     Do NOT force sub-themes — if all verbatims in a theme point to the same issue, leave it as a single sub-theme or no sub-themes.
     Naming: anchor the sub-theme label on the causal layer (who caused it, what system failed) — not just the symptom. "Courier marks delivery as attempted without attempting" is more actionable than "delivery not received".

     Output format: separate tables for Negative and Positive.
     Quote column: list Q-IDs only (e.g. Q003, Q017). Text and platform resolve from quotes_registry.json at render time.
     NEVER write quote text directly in this file. -->

**Codebook:** Usability · Value · Reliability · Support · Brand · Open (novel patterns)

**Sentiment split:** Negative: [n] ([%]%) / Positive: [n] ([%]%)

#### Negative Feedback (n=[X])

| Theme (n) | Sub-theme (n) | Quote IDs |
|---|---|---|
| **[Theme]** (n=[X]) | [Sub-theme] (n=[X]) | Q001, Q008 |
| **[Theme]** (n=[X]) | [Sub-theme] (n=[X]) | Q014, Q022, Q031 |

*(Repeat theme name on each sub-theme row. 2–3 Q-IDs per sub-theme row. List themes descending by n. Quote text + platform resolved from quotes_registry.json.)*

#### Positive Feedback (n=[X])

| Theme (n) | Sub-theme (n) | Quote IDs |
|---|---|---|
| **[Theme]** (n=[X]) | [Sub-theme] (n=[X]) | Q005, Q019 |

*(Same rules as Negative table above.)*

---

## Label Legend

| Label | Meaning |
|---|---|
| `[DATA UNAVAILABLE — as of date]` | No public information found for this field as of the date shown. |
| `[UNVERIFIED — Source, date, SRC:id]` | Figure from a data aggregator that does not disclose its methodology, or sourced from subject-company materials only. Treat as directional only. |
| `[>2YR — last confirmed date, SRC:id]` | Most recent source is older than 2 years. Verify before use. |
| `[INSUFFICIENT DATA]` | Not enough customer verbatims collected to conduct thematic analysis. |
| `⚠️ Last disclosed funding is >24 months old` | Most recent funding round is older than 24 months — activity since then is unconfirmed. |