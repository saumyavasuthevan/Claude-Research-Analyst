# Create Company Context

Research a company using Brave Search and populate all four context files from the project templates.

## Step 1 — Get Company Name

Ask the user: "What company would you like to research?"

Wait for their response before proceeding.

## Step 2 — Read Templates and Check for Existing Project

Run these two operations before searching:

1. Read all four templates:
   - `templates/company-overview-template.md`
   - `templates/competitive-landscape-template.md`
   - `templates/product-description-template.md`
   - `templates/market-research-template.md`

2. Check whether a project folder already exists:
   ```bash
   ls projects/
   ```
   If `projects/[CompanyName]/` already exists, note its contents before writing so you don't overwrite existing research.

## Step 3 — Run Brave Searches

Use `mcp__brave-search__brave_web_search` to run all 8 queries below. Use the exact company name provided.

**Run searches sequentially — do not batch or parallelise:**
```bash
# Between every mcp__brave-search call, run:
sleep 2
```
This prevents burst rate limiting on the Brave Search API. The 14-second overhead is negligible compared to the cost of failed searches and degraded output.

| # | Query | Sections it covers |
|---|---|---|
| 1 | `"[Company]" founded headquarters funding stage employees` | company-overview.md §Background |
| 2 | `"[Company]" ARR revenue customers growth metrics` | company-overview.md §Metrics |
| 3 | `"[Company]" product features capabilities pricing plans` | product-description.md |
| 4 | `"[Company]" competitors alternatives market positioning` | competitive-landscape.md |
| 5 | `"[Company]" market size TAM growth rate industry trends` | market-research.md |
| 6 | `"[Company]" G2 reviews customer use cases ROI` | product-description.md §Metrics |
| 7 | `"[Company]" tech stack engineering infrastructure` | product-description.md §Tech Stack |
| 8 | `"[Company]" roadmap upcoming features announcements 2025 2026` | product-description.md §Roadmap |

Use the following source tiers to prioritise which results to trust:
- Tier 1 (trust first): official company website, press releases, prnewswire.com, businesswire.com, and authoritative industry-specific publications relevant to the company's sector
- Tier 2: TechCrunch, VentureBeat, Bloomberg, Forbes, Reuters
- Tier 3 (reviews/pricing): G2, Capterra, Gartner Peer Insights
- Funding: Crunchbase, PitchBook, Tracxn (label as unverified estimates)

If a `projects/[CompanyName]/05- memory/reference_sources.md` file exists for the active company, check it first — it may define company-specific trusted sources that override this default list.

## Step 3b — Handle Search Failures Before Continuing

After all 8 searches complete, count how many returned errors or rate limit responses.

**If a rate limit error occurs mid-sequence:**
```bash
sleep 5
# then retry the failed query once
```
If the retry also fails, attempt the same query using the `web_search` tool as a fallback. Label those results `[web_search fallback, date]`. Only mark `[SEARCH FAILED]` if both tools fail for that query.

**If 1–2 searches failed and all retries also failed:** Mark affected sections `[SEARCH FAILED — data not retrieved as of [date]]` and continue to the coverage check.

**If 3 or more searches failed:** Stop. Do not proceed to write files. Report to the user:
```
[X] searches failed: [list query numbers and queries]
Retrying before writing. Please wait.
```
Retry all failed queries with `sleep 5` before each attempt. Only proceed once at least 6 of 8 queries have returned results. If retries continue to fail, ask the user whether to proceed with partial coverage or try again.

**Never fill a section with inferred content because the search that would have sourced it failed.** Use `[SEARCH FAILED — data not retrieved as of [date]]` instead.

## Step 3c — Run Dedicated Competitor Searches

After the 8 main searches, identify every named competitor you plan to include in `competitive-landscape.md`. For each one, run two direct searches sequentially with `sleep 2` between each:

```
"[Competitor name]" product features pricing 2025
"[Competitor name]" users statistics 2025 2026
```

The second query specifically catches updated figures — user counts, market share, and pricing change frequently and the main searches often return stale data on competitors.

**Do not write comparative claims about a competitor based solely on what the subject company's sources say about them.** Sources like annual reports, investor decks, or industry overviews that describe competitors in passing do not count as independent verification.

If a direct search on the competitor returns no usable results, tag every comparative claim about them:
`[COMPETITOR NOT INDEPENDENTLY VERIFIED — sourced from subject-company materials only]`

## Step 3d — Coverage Check Before Writing

Before creating any files, produce this coverage map:

```
Search coverage:
Query 1 (company overview): ✅ / ❌ FAILED
Query 2 (metrics):          ✅ / ❌ FAILED
Query 3 (product):          ✅ / ❌ FAILED
Query 4 (competitors):      ✅ / ❌ FAILED
Query 5 (market):           ✅ / ❌ FAILED
Query 6 (reviews):          ✅ / ❌ FAILED
Query 7 (tech stack):       ✅ / ❌ FAILED
Query 8 (roadmap):          ✅ / ❌ FAILED

Competitor direct searches:
- [Competitor A]: ✅ independently verified / ⚠️ not verified
- [Competitor B]: ✅ independently verified / ⚠️ not verified

Sections with full coverage:    [list]
Sections with partial coverage: [list + reason]
Sections with no coverage:      [list — will be marked SEARCH FAILED]
```

Only proceed to Step 4 after completing this check.

## Step 4 — Create Output Directory

```bash
mkdir -p "projects/[CompanyName]/01- company context"
```

Use the company's official capitalisation (e.g. "Ironclad", "LawGeex", "WorkMotion").

## Step 5 — Fill and Save All Four Files

Using the search results, fill in all four templates and save them to the output folder. Write all four files — do not skip any.

Add this block at the very top of every file, before any other content:

```markdown
> **Research date: [date]. All figures should be re-verified if this document
> is used more than 90 days after this date. Figures tagged [UNVERIFIED]
> require immediate re-checking before use.**
```

### Citation rule — inline at point of writing

Every factual claim must include an inline citation at the moment it is written.

**Format:** `[Source Name, Month Year, URL]` immediately after the claim.

Do not write a paragraph and add citations at the end. Cite each sentence as you write it. If you cannot cite a claim at the moment of writing it, do not write it — use `[DATA UNAVAILABLE]` instead.

**Acceptable citation formats:**
- `[Grand View Research, Apr 2025, https://www.grandviewresearch.com/industry-analysis/digital-health-market]`
- `[HPB newsroom, Nov 2024, https://www.hpb.gov.sg/newsroom/article/...]`
- `[Reddit r/singapore, Nov 2025, https://www.reddit.com/r/singapore/comments/...]`
- `[Strava Year in Sport, Dec 2025, https://press.strava.com/articles/...]`

**Unacceptable:**
- `[Source]` with no date and no URL
- `[Source, date]` with no URL
- Footnotes or a source list at the bottom that does not map to specific claims
- Shortened, reconstructed, or guessed URLs

**URL sourcing rule:** Only use URLs that appeared in your `mcp__brave-search` or `web_search` results during this session. Never construct or recall a URL from training memory. If a source was retrieved but its URL was not returned in the search results, write `[URL NOT RETRIEVED]` in place of the URL — do not guess or approximate it.

Keep each competitor block under 300 words. Beyond that length the model loses reliable track of which search result supports which claim.

### Freshness check — required before writing any figure

Before writing any statistic (user counts, market size, pricing, growth rates):
1. Check **all** retrieved sources for that figure — not just the first one found
2. Use the most recently dated source
3. If sources conflict across dates, list all versions — do not silently pick one:
   ```
   User count: ~135M [Strava Year in Sport, Dec 2024, https://...]
            vs ~180M [Strava Year in Sport, Dec 2025, https://press.strava.com/...]
   ```

If your most recent source for a figure is older than 12 months from today, tag it:
`[UNVERIFIED — last confirmed [date], [URL]]`

### Labelling rules — classify before writing, not after

For every statement, determine its type before writing it:

| Type | When to use | Label |
|---|---|---|
| Sourced fact | Directly stated in a named source | `[Source Name, Month Year, URL]` |
| Inference | Reasoned from multiple sources but not explicitly stated | `[ASSUMPTION — reasoning: ...]` |
| Aggregator figure | From Crunchbase, PitchBook, Getlatka, G2, or similar | `[UNVERIFIED ESTIMATE — Source, date, URL]` |
| Missing data | Searched but could not find | `[DATA UNAVAILABLE — as of date]` |
| Search failure | Primary search for this section failed or errored | `[SEARCH FAILED — data not retrieved as of date]` |
| Unverified competitor claim | Competitor described only via subject-company sources | `[COMPETITOR NOT INDEPENDENTLY VERIFIED]` |
| Stale figure | Most recent source older than 12 months | `[UNVERIFIED — last confirmed date, URL]` |
| URL missing from results | Source retrieved but URL not returned by search | `[URL NOT RETRIEVED]` |

**Never write plausible-sounding content to fill a gap.** If the data isn't there, use the label.

### Banned claim patterns

Do not generate any of the following without quoting a specific named source that makes the claim:

- "The only [X] that..."
- "No competitor offers..."
- "Unlike any other..."
- "Uniquely positioned to..."
- "The leading / fastest / largest..." (unless citing a named ranking with date and URL)
- "[Company] is stronger / better / more advanced than [Competitor] at [X]"

If a source makes this claim, quote and cite it with URL. Do not generate this language yourself.

### Staleness rule for competitive claims

Any comparative statement (Company A vs Company B) must cite a source dated within **12 months** of today. If your most recent source is older than 12 months, tag it:

`[UNVERIFIED — last confirmed [date], [URL]]`

### Conflicting figures

If two sources report different figures for the same fact, list both with dates and URLs — do not silently pick one:

```
User count: ~135M [Strava Year in Sport, Dec 2024, https://...]
         vs ~180M [Strava Year in Sport, Dec 2025, https://press.strava.com/...]
```

### Source quality rule for competitor sections

A comparative claim about a competitor requires either:
- The competitor's own website, press releases, or official docs **(primary)**, or
- A named journalist, analyst report, or study covering the competitor directly **(secondary)**

Anything sourced only from the subject company's materials or a passing mention in a market overview must be tagged `[COMPETITOR NOT INDEPENDENTLY VERIFIED]`.

### Files to write:

**1. `projects/[CompanyName]/01- company context/company-overview.md`**
Use `templates/company-overview-template.md` as the structure.
Fill every section. Do not leave template placeholder text — replace with data or a label.

**2. `projects/[CompanyName]/01- company context/competitive-landscape.md`**
Use `templates/competitive-landscape-template.md` as the structure.
Identify 3–5 direct competitors from search results. Fill the competitive matrix and one detailed block per competitor. Every comparative claim must meet the source quality rule above. Keep each competitor block under 300 words.

**3. `projects/[CompanyName]/01- company context/product-description.md`**
Use `templates/product-description-template.md` as the structure.
Focus on what the product actually does, not marketing language. Be specific about features, limits, and integrations.

**4. `projects/[CompanyName]/01- company context/market-research.md`**
Use `templates/market-research-template.md` as the structure.
Populate market size, growth rate, segments, competitors, trends, and opportunities. Cite all figures with source name, date, and URL.

## Step 5b — Pre-Save Integrity Check

Before saving each file, verify every item below. Fix any that fail before writing the file.

- [ ] Research date block appears at the top of the file
- [ ] Every factual claim has an inline citation with source name, date, and URL (or `[URL NOT RETRIEVED]`)
- [ ] Every market size or growth figure has a named source, date, and URL
- [ ] All figures use the most recently dated source available — not the first found
- [ ] Conflicting figures across sources are listed with both versions and URLs, not silently resolved
- [ ] No competitor comparison is sourced only from the subject company's own materials
- [ ] No comparative claim is older than 12 months without an `[UNVERIFIED]` tag
- [ ] No banned claim pattern appears without a direct citation with URL
- [ ] Every `[ASSUMPTION]` tag includes a reasoning note
- [ ] No section has been filled with inferred content where data was unavailable
- [ ] Sections whose primary search failed are marked `[SEARCH FAILED]`, not filled from adjacent searches
- [ ] No URL has been constructed from memory — all URLs came from search results this session

## Step 6 — Confirm

After saving all four files, confirm with:

```
Company context created for [Company Name].

Files saved to projects/[CompanyName]/01- company context/
  - company-overview.md
  - competitive-landscape.md
  - product-description.md
  - market-research.md

Search coverage: [X]/8 queries successful
Failed/retried queries: [list, or "none"]
Fallback tool used: [web_search for queries X, Y — or "none"]

Competitors independently verified: [list with URLs of primary sources used]
Competitors NOT independently verified: [list, or "none"]

[ASSUMPTION] tags written: X
[DATA UNAVAILABLE] tags written: X
[UNVERIFIED ESTIMATE] tags written: X
[UNVERIFIED — stale figure] tags written: X
[COMPETITOR NOT INDEPENDENTLY VERIFIED] tags written: X
[URL NOT RETRIEVED] tags written: X

Key sources used: [list source name + URL, grouped by file]

Flags for human review: [list any conflicting figures, stale claims,
[URL NOT RETRIEVED] tags, or sections with partial coverage — or "none"]
```

## Error Handling

- **Company not found:** Ask the user to confirm the exact company name or provide a website URL.
- **Limited public data (private company):** Proceed with what is available. Label all gaps clearly. Note at the top of each file: `> ⚠️ Limited public data available — private company. Significant sections below are labelled DATA UNAVAILABLE.`
- **Conflicting figures across sources:** List all reported figures with sources, dates, and URLs. Do not silently pick one.
- **No pricing data:** Label `[DATA UNAVAILABLE — as of date]`. Do not guess or use ranges without a source.
- **3+ search failures:** Stop, retry with `sleep 5` between attempts, report to user before writing. See Step 3b.
- **Rate limit persists after retry:** Attempt query with `web_search` fallback tool. Label results `[web_search fallback, date]`.
- **Competitor data only available from subject-company sources:** Write the section with confirmed facts only, tag all comparative claims `[COMPETITOR NOT INDEPENDENTLY VERIFIED]`, and list them in the Step 6 confirmation.
- **URL not present in search results:** Write `[URL NOT RETRIEVED]` — never construct or guess a URL from memory.
