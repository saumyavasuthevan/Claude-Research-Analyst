# 🔬 PM Operating System Index

### Challenge
* The bar for PM operational efficiency and effectiveness has risen
* Most PMs respond with **fragmented** AI use — faster at isolated tasks, but still siloed
* We know that the future is a **unified system** that connects these workflows together. But unification introduces a harder problem: **hallucinations compound** as AI **flattens qualitative nuance**, human judgment is often replaced, and one agent's output feeds into the next
* The core tension is leveraging the **speed of AI while preserving quality**

### Goal 
* Create a PM operating system that combines the best of human, code, and AI to co-create PM artifacts that minimise OPEX while delivering outputs users can trust

### Approach  
* Break down current PM workflows into their **component tasks**
* Assess the best solution for each task: **deterministic code** for anything rules-based, **AI** for analysis, synthesis, and objective verification, **humans** for implicit problem context and strategic direction, qualitative verification, and conflict resolution. 
* Close the feedback loop with **evals** at every step — so hallucinations don't compound silently across agents and the system benchmarks its own accuracy over time
* Start simple and **add complexity iteratively** — e.g. beginning with an agent producing a report, manually identifying errors, then introducing an eval agent, then deterministic data pipelines to meet accuracy requirements 
* Actively remove tasks LLMs do poorly — e.g. removing SWOT analysis from competitive intelligence reports in favour of qualitative claims that summarise verified sources 

### 🔍 Product Discovery

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Interview Analysis Agent](.claude/agents/interview-analysis.md) | Analyses user research interviews for pain points, bright spots, and project-specific dimensions — one file per participant, with verbatim quotes. No synthesis. |
| **Claude Code** | [Survey Analysis Agent](.claude/agents/survey-analysis.md) | Highlights key themes by user segment; deterministically computes all statistics via Python/pandas so the model only interprets, improving accuracy. |
| **Claude Code** | [Company Context Agent](portfolio/create-company.md) | Conducts automated deep-dives into a company, its competitors, market landscape, and products. Serves as context for other agents (e.g. Interview Analysis Agent, PRD Generator). |
| **Claude Code** | [Customer Support Analysis Agent](.claude/agents/customer-support-analysis.md) | Analyses customer support feedback verbatims for themes by user segment. |
| **OpenClaw** | [Competitive Intel](.claude/agents/competitive-intel.md) | Sends a weekly competitive intelligence report to PMs. |

### 📄 Artifacts

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [PRD Generator](others/01-prd-generator) | **Experiment only:** Creates PRD draft by synthesizing market research and internal company context files.<br>**Caveat:** Aimed to speed up summarization and initial ideation but cannot replace the deep understanding of problem context and strategic direction that a PM must first start with. |

### ✅ Eval / Verification

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Int Research Eval Agent](.claude/agents/int-research-eval.md) | Evaluates internal user research outputs. Combines human and machine evaluations to verify qual claims and quant calculations. Benchmarks Precision and Recall. |
| **Claude Code** | [Ext Research Eval Agent](.claude/agents/ext-research-eval.md) | Evaluates external web-based research outputs. Aggregates human's subjective assessment of Helpfulness, Honesty, and Harmlessness scores across reports to benchmark HHH scores over time. Machine evaluates objective criteria in each report (e.g., link validity, template adherence). |
| **Claude Code** | [Eval Feedback Command](.claude/commands/eval-feedback.md) | Updates the relevant agent or skill based on user's evaluation feedback. |
| **Claude Code** | [Check Agent Command](.claude/commands/check-agent.md) | Reviews and updates agent, skill, and command files to resolve conflicts, avoid template drift, and ensure consistency across files. |

### 👁️ Observability

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Observability Hooks](.claude/hooks/) | Captures tool inputs/outputs via deterministic shell hooks, preventing token consumption and Claude from forgetting instructions. Used by Debug Agent to trace errors and recommend improvements to agents and skills. |

### 🔧 Tooling

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Update Portfolio Command](.claude/commands/update-portfolio.md) | Generates or updates a portfolio README for any agent or skill. Reads the agent file and git history to draft an Iterations list, asks four questions, then writes a complete portfolio file with Mermaid workflow diagram and annual value-saved calculation. |
| **Claude Code** | [Meta Sync Command](.claude/commands/meta-sync.md) | Keeps CLAUDE.md, README.md, MEMORY.md, and .claudeignore up-to-date based on recent changes. |
| **Claude Code** | [Agent Template](.claude/_agent-template.md) | Template for building new Claude Code agents — forces agents to inherit conventions from CLAUDE.md to reuse instructions and prevent drift. |

### 🗂️ Misc. Experiments

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **n8n** | [Agentic RAG Contract Auditor](others/04-agentic-rag) | Enhances retrieval when analyzing legal risks in contracts for lawyers. |
| **n8n** | [Traditional RAG Chatbot](others/05-traditional-rag) | Enables users to overcome context window limits. |
