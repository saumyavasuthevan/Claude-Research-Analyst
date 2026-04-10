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

Use `mcp__brave-search__brave_web_search` to run all 8 queries below. Use the exact company name provided. Run them in parallel where possible.

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

Use the source tiers from `projects/Legal Graph/05- memory/reference_sources.md` to prioritise which results to trust:
- Tier 1 (trust first): law.com, lawnext.com, artificiallawyer.com, prnewswire.com
- Tier 2: TechCrunch, VentureBeat, Bloomberg
- Tier 3 (reviews/pricing): G2, Capterra, Gartner Peer Insights
- Funding: Crunchbase, PitchBook, Tracxn (label as unverified estimates)

## Step 3b — Handle Search Failures Before Continuing

After all 8 searches complete, count how many returned errors or rate limit responses.

**If 1–2 searches failed:** Retry each failed query once using `mcp__brave-search__brave_web_search` before proceeding. If the retry also fails, mark the affected sections `[SEARCH FAILED — data not retrieved as of [date]]` and continue.

**If 3 or more searches failed:** Stop. Do not proceed to write files. Report to the user:
```
[X] searches failed: [list query numbers and queries]
Retrying before writing. Please wait.
```
Retry all failed queries. Only proceed once at least 6 of 8 queries have returned results. If retries continue to fail, ask the user whether to proceed with partial coverage or try again.

**Never fill a section with inferred content because the search that would have sourced it failed.** Use `[SEARCH FAILED — data not retrieved as of [date]]` instead.

## Step 3c — Run Dedicated Competitor Searches

After the 8 main searches, identify every named competitor you plan to include in `competitive-landscape.md`. For each one, run a direct search using `mcp__brave-search__brave_web_search`:

```
"[Competitor name]" product features pricing 2025
```

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

### Labelling rules — classify before writing, not after

For every statement, determine its type before writing it:

| Type | When to use | Label |
|---|---|---|
| Sourced fact | Directly stated in a named source | Cite inline: `[Source, date]` |
| Inference | Reasoned from multiple sources but not explicitly stated | `[ASSUMPTION — reasoning: ...]` |
| Aggregator figure | From Crunchbase, PitchBook, Getlatka, G2, or similar | `[UNVERIFIED ESTIMATE — Source]` |
| Missing data | Searched but could not find | `[DATA UNAVAILABLE — as of date]` |
| Search failure | Primary search for this section failed or errored | `[SEARCH FAILED — data not retrieved as of date]` |
| Unverified competitor claim | Competitor described only via subject-company sources | `[COMPETITOR NOT INDEPENDENTLY VERIFIED]` |

**Never write plausible-sounding content to fill a gap.** If the data isn't there, use the label.

### Banned claim patterns

Do not generate any of the following without quoting a specific named source that makes the claim:

- "The only [X] that..."
- "No competitor offers..."
- "Unlike any other..."
- "Uniquely positioned to..."
- "The leading / fastest / largest..." (unless citing a named ranking with date)
- "[Company] is stronger / better / more advanced than [Competitor] at [X]"

If a source makes this claim, quote and cite it. Do not generate this language yourself.

### Staleness rule for competitive claims

Any comparative statement (Company A vs Company B) must cite a source dated within **12 months** of today. If your most recent source is older than 12 months, tag it:

`[UNVERIFIED — last confirmed [date], may be outdated]`

### Conflicting figures

If two sources report different figures for the same fact, list both — do not silently pick one:

```
User count: ~200M [Company blog, 2023] vs ~280M [Press release, Feb 2026]
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
Identify 3–5 direct competitors from search results. Fill the competitive matrix and one detailed block per competitor. Every comparative claim must meet the source quality rule above.

**3. `projects/[CompanyName]/01- company context/product-description.md`**
Use `templates/product-description-template.md` as the structure.
Focus on what the product actually does, not marketing language. Be specific about features, limits, and integrations.

**4. `projects/[CompanyName]/01- company context/market-research.md`**
Use `templates/market-research-template.md` as the structure.
Populate market size, growth rate, segments, competitors, trends, and opportunities. Cite all figures with source name and date.

## Step 5b — Pre-Save Integrity Check

Before saving each file, verify:

- [ ] Every market size or growth figure has a named source and date
- [ ] No competitor comparison is sourced only from the subject company's own materials
- [ ] No comparative claim is older than 12 months without a staleness tag
- [ ] No banned claim pattern appears without a direct citation
- [ ] Every `[ASSUMPTION]` tag includes a reasoning note
- [ ] No section has been filled with inferred content where data was unavailable
- [ ] Sections whose primary search failed are marked `[SEARCH FAILED]`, not filled from adjacent searches

Fix any that fail before writing the file.

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

Competitors independently verified: [list]
Competitors NOT independently verified: [list, or "none"]

[ASSUMPTION] tags written: X
[DATA UNAVAILABLE] tags written: X
[UNVERIFIED ESTIMATE] tags written: X
[COMPETITOR NOT INDEPENDENTLY VERIFIED] tags written: X

Key sources used: [list the key sources, grouped by file]

Flags for human review: [list any conflicting figures, claims older than 6 months,
or sections with partial coverage — or "none"]
```

## Error Handling

- **Company not found:** Ask the user to confirm the exact company name or provide a website URL.
- **Limited public data (private company):** Proceed with what is available. Label all gaps clearly. Note at the top of each file: `> ⚠️ Limited public data available — private company. Significant sections below are labelled DATA UNAVAILABLE.`
- **Conflicting figures across sources:** List all reported figures with their sources and dates. Do not silently pick one.
- **No pricing data:** Label `[DATA UNAVAILABLE — as of date]`. Do not guess or use ranges without a source.
- **3+ search failures:** Stop, retry, report to user before writing. See Step 3b.
- **Competitor data only available from subject-company sources:** Write the section with confirmed facts only, tag all comparative claims `[COMPETITOR NOT INDEPENDENTLY VERIFIED]`, and list them in the Step 6 confirmation.
