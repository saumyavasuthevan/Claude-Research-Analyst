# Research Workflow Lab

A structured company research agent powered by Claude Code. Transforms natural-language research requests into rigorous, source-grounded intelligence reports — with a mandatory two-phase workflow that prevents hallucination, enforces analytical objectivity, and produces consistently formatted output.

---

## Features

- **Two-phase gate enforcement** — research never executes without a user-approved structured prompt. No skipping, no shortcuts.
- **Hallucination prevention** — all quantitative claims require a named, credible source. Unverifiable figures are labeled `[DATA UNAVAILABLE]` rather than fabricated.
- **Explicit assumption labeling** — every inference is prefixed `[ASSUMPTION]` and distinguished from confirmed fact.
- **Private company handling** — built-in patterns for research targets with limited public data: funding recency signals, third-party aggregator labeling, conflicting figure reconciliation.
- **Standardized report structure** — eight-section output format applied consistently across all research targets, regardless of company type or industry.
- **Automatic file output** — completed reports are saved automatically to dated Markdown files (`research_[company]_[YYYY-MM-DD].md`).
- **Customer sentiment coverage** — for private companies without analyst coverage, the agent substitutes structured customer review data (G2, Capterra, Trustpilot) and press sentiment summaries.
- **Competitive landscape tables** — standardized competitor tables with consistent columns: Competitor | HQ | Model | Key Differentiator | Scale Indicator.

---

## The Two-Phase Workflow

This agent enforces a strict two-phase process. Research output is never returned in the same turn as the request.

### Phase 1 — Prompt Generation

When you submit a research request, the agent generates a **Structured Research Prompt** and presents it for review. The prompt specifies:

- The research subject and date
- The analyst role and goal
- Detailed instructions for sourcing, labeling, and formatting
- The full eight-section output format
- Guardrails for data quality

The agent then pauses and asks for confirmation. It will not proceed further.

### Phase 2 — Confirmation Gate

You must explicitly approve before research executes. Accepted responses include:

> `confirmed` / `yes` / `approved` / `go ahead` / `looks good`

You can also approve with modifications:

> `yes, but focus more on the competitive landscape`

In that case, the agent revises the prompt, presents it again, and re-confirms before executing.

### Phase 3 — Research Execution

Only after confirmed approval does the agent:

1. Execute research against the approved structured prompt
2. Deliver the formatted report
3. Save output to `research_[company_name]_[YYYY-MM-DD].md`
4. Confirm the saved filename to the user

---

## Report Structure

Every research report follows the same eight-section format:

| # | Section | Description |
|---|---|---|
| 1 | Company Overview | Legal name, HQ, founding year, ownership, headcount, geographic footprint |
| 2 | Business Model & Revenue Streams | Revenue model, key products, customer segments, channels |
| 3 | Financial Snapshot | Revenue, profitability indicators, funding history, funding recency signal |
| 4 | Market Position & Competitive Landscape | Market positioning, standardized competitor table, moats, weaknesses |
| 5 | Recent Strategic Developments | M&A, partnerships, product launches, leadership changes (last 24 months) |
| 6 | Key Risks & Challenges | Market, operational, and regulatory risks |
| 7 | Analyst & Market Sentiment | Analyst coverage (public) or customer reviews + press sentiment (private) |
| 8 | Sources & Data Provenance | All named sources with dates; gaps explicitly flagged |

---

## How to Install and Run

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed and authenticated
- A terminal with access to this project directory

### Setup

1. Clone or download this repository:

   ```bash
   git clone <your-repo-url>
   cd research-workflow-lab
   ```

2. Verify the project structure:

   ```
   research-workflow-lab/
   ├── CLAUDE.md          # Agent configuration — do not delete
   └── README.md          # This file
   ```

   The `CLAUDE.md` file is the agent's system configuration. Claude Code reads it automatically when you open the project.

### Running a Research Session

1. Open the `research-workflow-lab` directory in Claude Code:

   ```bash
   claude
   ```

2. Submit a research request in natural language:

   ```
   Do research on Stripe.
   ```

3. Review the generated Structured Research Prompt. Reply to confirm or request changes:

   ```
   confirmed
   ```

   or

   ```
   confirmed, but add extra focus on their infrastructure products
   ```

4. The agent executes research and saves the output:

   ```
   Research complete. Output has been saved to: research_stripe_2026-02-22.md
   ```

### Output Files

Completed reports are saved as Markdown files in the project root:

```
research_[company_name]_[YYYY-MM-DD].md
```

Examples:
- `research_stripe_2026-02-22.md`
- `research_goldman_sachs_2026-02-22.md`
- `research_openai_2026-02-22.md`

---

## Data Quality Standards

| Standard | How It's Enforced |
|---|---|
| No fabricated figures | Unsourced data is labeled `[DATA UNAVAILABLE]`, never estimated |
| No unconfirmed execution | Hard gate — agent will not research without explicit user approval |
| Assumptions always labeled | `[ASSUMPTION]` prefix required on every inference |
| Aggregator data flagged | Figures from Getlatka, PitchBook, Crunchbase, etc. labeled as unverified estimates |
| Conflicting figures reconciled | All reported values listed with sources; discrepancy explained |
| Funding recency surfaced | Private company funding gaps >24 months flagged as a material risk signal |
| 24-month data window | Data older than 24 months permitted only if labeled as historical context |

---

## Example Interaction

```
User:    Do research on Banxware.

Agent:   I've generated a structured research prompt for your request. Please review before I proceed.

         ---
         ## Structured Research Prompt
         Subject: Banxware GmbH
         Research Date: 2026-02-22
         ...
         [full prompt]
         ---
         Before I proceed, please confirm:
         - Does this research prompt align with what you need?
         - Are there any sections you want to add, remove, or adjust?
         - Any specific angle, time range, or competitor focus you want prioritized?

         Reply "confirmed" (or describe any changes) to begin research execution.
         ---

User:    confirmed

Agent:   Proceeding with research execution...

         [delivers full 8-section report]

         Research complete. Output has been saved to: research_banxware_2026-02-22.md
```

---

## Configuration

The agent's behavior is controlled entirely by `CLAUDE.md`. Editable parameters include:

- **Output format** — section structure and required fields
- **Guardrails** — data quality rules and labeling requirements
- **Confirmation language** — what phrases count as valid approval
- **Edge case handling** — behavior for private companies, vague names, conflicting data, insufficient data, and multi-company requests

Modifying `CLAUDE.md` changes agent behavior for all future research sessions in this project.
