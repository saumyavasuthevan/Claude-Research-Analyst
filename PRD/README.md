# PRD Generator 

I built this to test Claude’s ability to synthesise and structure a PRD based on provided internal context and external signals. 
What it does: Generates a structured first draft based on provided internal and external research.
What it doesn't do: Replace strategic thinking.
The Goal: I’m a firm believer that you can’t generate a PRD with a click of a button. A great PRD needs deep understanding of internal goals and strategic alignment. This project is my way of testing where AI can speed things up (summarization, structure, initial ideation) while maintaining the role of the PM to evaluate and shape the output.

### Company Context Files (`company-context/`)

These files contain company information as context for PRD:

- `company-overview.md` - Company background, team, metrics, strategy, OKRs
- `user-personas.md` - Three user personas: Jennifer (GC), David (Senior Counsel), Rachel (Legal Ops)
- `product-description.md` - Current product features, roadmap, tech stack
- `competitive-landscape.md` - Competitors and market positioning

### Templates (`templates/`)

Pre-defined output format templates that ensure consistency in your deliverables:

- `market-research-format.md` - Structure for market research deliverables
- `prd-template.md` - Structure for Product Requirements Documents

### Sample Prompts (`sampleprompts/`)

Ready-to-use example prompts for common PM tasks:

- `market-research-prompt.md` - Example prompt for conducting market research
- `prd-prompt.md` - Example prompt for writing PRDs

### Configuration Files

- `CLAUDE.md` - Project-level instructions for Claude Code (defines context and workflows)


