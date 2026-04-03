# Create Company Context

Research a company using Brave Search and populate all four context files from the project templates.

## Step 1 — Get Company Name

Ask the user: "What company would you like to research?"

Wait for their response before proceeding.

## Step 2 — Run Brave Searches

Use `mcp__brave-search__brave_web_search` to run all 8 queries below. Use the exact company name provided. Run them in parallel where possible.

| # | Query |
|---|---|
| 1 | `"[Company]" founded headquarters funding stage employees` |
| 2 | `"[Company]" ARR revenue customers growth metrics` |
| 3 | `"[Company]" product features capabilities pricing plans` |
| 4 | `"[Company]" competitors alternatives market positioning` |
| 5 | `"[Company]" market size TAM growth rate industry trends` |
| 6 | `"[Company]" G2 reviews customer use cases ROI` |
| 7 | `"[Company]" tech stack engineering infrastructure` |
| 8 | `"[Company]" roadmap upcoming features announcements 2025 2026` |

Use the source tiers from `.claude/memory/competitive-intel/reference_sources.md` to prioritise which results to trust:
- Tier 1 (break-first): law.com, lawnext.com, artificiallawyer.com, prnewswire.com
- Tier 2: TechCrunch, VentureBeat, Bloomberg
- Tier 3 (reviews/pricing): G2, Capterra, Gartner Peer Insights
- Funding: Crunchbase, PitchBook, Tracxn (label as unverified estimates)

## Step 3 — Create Output Directory

Create the folder: `context/Company/[CompanyName]/`

Use the company name with spaces replaced by the official capitalisation (e.g. "Ironclad", "LawGeex", "WorkMotion").

## Step 4 — Fill and Save All Four Files

Using the search results, fill in all four templates and save them to the output folder. Write all four files — do not skip any.

### Labelling rules (apply consistently across all files):
- `[ASSUMPTION]` — any inference not directly sourced
- `[DATA UNAVAILABLE — as of research date]` — any field you could not find
- `[UNVERIFIED ESTIMATE — Source]` — figures from Crunchbase, PitchBook, Getlatka, or similar aggregators

### Files to write:

**1. `context/Company/[CompanyName]/company-overview.md`**
Use `templates/company-overview-template.md` as the structure.
Fill every section. Do not leave template placeholder text — replace with data or a label.

**2. `context/Company/[CompanyName]/competitive-landscape.md`**
Use `templates/competitive-landscape-template.md` as the structure.
Identify 3–5 direct competitors from search results. Fill the competitive matrix and one detailed block per competitor.

**3. `context/Company/[CompanyName]/product-description.md`**
Use `templates/product-description-template.md` as the structure.
Focus on what the product actually does, not marketing language. Be specific about features, limits, and integrations.

**4. `context/Company/[CompanyName]/market-research.md`**
Use `templates/market-research-template.md` as the structure.
Populate market size, growth rate, segments, competitors, trends, and opportunities. Cite all figures.

## Step 5 — Confirm

After saving all four files, confirm with:

```
Company context created for [Company Name].

Files saved to context/Company/[CompanyName]/
  - company-overview.md
  - competitive-landscape.md
  - product-description.md
  - market-research.md

Sources used: [list the key sources from your searches]
```

## Error Handling

- **Company not found:** Ask the user to confirm the exact company name or provide a website URL.
- **Limited public data (private company):** Proceed with what is available. Label all gaps clearly. Note at the top of each file: "Limited public data available — private company."
- **Conflicting figures across sources:** List all reported figures with their sources. Do not silently pick one.
- **No pricing data:** Label `[DATA UNAVAILABLE]` — do not guess or use ranges without a source.
