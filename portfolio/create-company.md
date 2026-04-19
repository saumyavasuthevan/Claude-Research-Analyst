# Company Context Agent

---

## Purpose

Conducts automated deep-dives into a company, its competitors, market landscape, and products. Serves as context for other agents (e.g. Interview Analysis Agent, Survey Analysis Agent).

---

## Workflow

Input a company name → agent researches and generates three context files used by downstream agents.

```mermaid
flowchart LR
    A["Input company name"] --> B["create-company-agent"]
    B --> C["Generate 3 context files<br/><small>company-overview.md<br/>competitive-landscape.md<br/>product-description.md</small>"]
```

---

## Iterations

| Challenge | Fix | Result |
|---|---|---|
| Agent attempted **competitive SWOT analysis**, but search snippets unable to substantiate qual claims — producing hallucinations like "ASOS has weaker EU logistics than Zalando." | **Shifted scope to facts only.** Agent now searches exclusively for data extractable from snippets (founding year, funding, revenue, headcount, named news events). No SWOT, no differentiation, no sentiment. | Every claim is traceable to a specific source. |
| Citations relied on the model generating URLs from memory — a **stochastic process** that produced broken or hallucinated links. | **Shifted to a deterministic citation system.** Every source is logged to a Fact Registry (`fact_registry.json`) at retrieval (URL, title, date, key quote). All output citations use `SRC:id` keys (e.g. `SRC:zalando_fy25_results`) — no raw URLs in any output file. | Every claim is auditable by source, date, and exact quote. |
| Agent wrote **overconfident competitive claims** — e.g. "no other competitor offers X" — sourced only from the subject company's own press releases. | **Banned the subject company's domain from all competitor searches.** Every competitor now requires an independent third-party source. | Reduced error rate on competitive claims. |
| Parallel Brave Search calls hit **rate limits** mid-run, causing the agent to skip queries and hallucinate data to fill the gaps. | **Forced sequential searches with `sleep 2` latency between every call.** | 100% data retrieval; 14-second added latency is a negligible trade-off. |
| **Outdated figures** (revenue, headcount) were presented as current — e.g. a 2022 headcount cited without any date flag. | **Added a staleness rule.** Any figure older than 12 months is auto-tagged `[UNVERIFIED — last confirmed date]`. | All outputs are fully auditable by date. |
| Native web search had **high token consumption** (~95K tokens per run). | **Switched to Brave Search API**, which returns compact structured JSON snippets. | ~50% reduction in search-related token consumption, reducing cost and overcoming context window limits. |

---

## Evals

- **Method:** [`ext-research-eval`](../.claude/agents/ext-research-eval.md) — checks outputs for quantitative claim accuracy, link validity, citation coverage, field recall, placeholder text, aggregator label compliance, banned claim patterns, and stale untagged sources. Includes a human HHH (Honesty, Helpfulness, Harmlessness) scoring component.
- **Coverage:** Run on Zalando competitive landscape output — company-overview.md and product-description.md evals pending.
- **Report:** [2026-04-18 — Zalando competitive landscape verification](../projects/Zalando/06-%20evals/2026-04-18-ext-research-verification-competitive-landscape.md)

---

## Sample Output

- [Zalando — company-overview.md](../projects/Zalando/01-%20company%20context/company-overview.md)
- [Zalando — competitive-landscape.md](../projects/Zalando/01-%20company%20context/competitive-landscape.md)
- [Zalando — product-description.md](../projects/Zalando/01-%20company%20context/product-description.md)

---

## Outcome

**Accuracy / Quality:** Reduced competitive landscape error rate. Every claim is grounded in an independently sourced, date-stamped, auditable citation.

**Cost savings:** ~€750/year — task reduced from 6 hrs to 75 mins (incl. verification)<br/>
*Assumptions: run ~4 times/year · ~4 new companies/year · pegged to PM salary*

---

## Links

- [Agent instructions](../.claude/agents/create-company.md) — prompt Claude uses at runtime
- [Eval report](../projects/Zalando/06-%20evals/2026-04-18-ext-research-verification-competitive-landscape.md) — latest verification run
