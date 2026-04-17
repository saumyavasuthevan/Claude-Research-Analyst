# 🔬 AI Experiments Index

A growing collection of my experiments with AI / agentic workflows 

### Product Discovery

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Interview Analysis Agent](.claude/agents/interview-analysis.md) | Analyses user research interviews for pain points, bright spots, and project-specific dimensions — one file per participant, with verbatim quotes. No synthesis. |
| **Claude Code** | [Survey Analysis Agent](.claude/agents/survey-analysis.md) | Automatically calculates survey margin of error and highlights key themes by user segment to speed up product discovery. |
| **Claude Code** | [Company Context Agent](portfolio/create-company.md) | Conducts automated deep-dives into a company, its competitors, market landscape, and products. Serves as context for other agents (e.g. Interview Analysis Agent, PRD Generator). |
| **Claude Code** | [Customer Support Analysis Agent](.claude/agents/customer-support-analysis.md) | Analyses customer support feedback verbatims for themes by user segment. |
| **OpenClaw** | [Competitive Intel](.claude/agents/competitive-intel.md) | Sends a weekly competitive intelligence report to PMs. |

### Artifacts

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [PRD Generator](others/01-prd-generator) | **Experiment only:** Creates PRD draft by synthesizing market research and internal company context files.<br>**Caveat:** Aimed to speed up summarization and initial ideation but cannot replace the deep understanding of problem context and strategic direction that a PM must first start with. |

### Eval / Verification

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Eval Feedback Command](.claude/commands/eval-feedback.md) | Updates the relevant agent or skill based on user's evaluation feedback. |
| **Claude Code** | [Check Agent Command](.claude/commands/check-agent.md) | Reviews and updates agent, skill, and command files to resolve conflicts, avoid template drift, and ensure consistency across files. |

### Observability

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Observability Hooks](.claude/hooks/) | Captures tool inputs/outputs via deterministic shell hooks, preventing token consumption and Claude from forgetting instructions. Used by Debug Agent to trace errors and recommend improvements to agents and skills. |

### Tooling

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **Claude Code** | [Meta Sync Command](.claude/commands/meta-sync.md) | Keeps CLAUDE.md, README.md, MEMORY.md, and .claudeignore up-to-date based on recent changes. |
| **Claude Code** | [Agent Template](.claude/_agent-template.md) | Template for building new Claude Code agents — forces agents to inherit conventions from CLAUDE.md to reuse instructions and prevent drift. |

### RAG

| Tool | Agent / Skill | Purpose |
| :--- | :--- | :--- |
| **n8n** | [Agentic RAG Contract Auditor](others/04-agentic-rag) | Enhances retrieval when analyzing legal risks in contracts for lawyers. |
| **n8n** | [Traditional RAG Chatbot](others/05-traditional-rag) | Enables users to overcome context window limits. |
