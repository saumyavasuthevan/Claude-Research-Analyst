# 🔬 AI Experiments Index

A growing collection of my experiments with AI / agentic workflows 

| Tool | Agent/ Skill | Description |
| :--- | :--- | :--- |
| **Claude Code** | [Meta Sync Command](.claude/commands/meta-sync.md) | Command that keeps CLAUDE.md, README.md, MEMORY.md, and .claudeignore up-to-date based on recent changes. |
| **Claude Code** | [Customer Support Analysis Agent](.claude/agents/customer-support-analysis.md) | Agent that analyses customer support feedback verbatims for themes by user segment. |
| **Claude Code** | [Agent Template](.claude/_agent-template.md) | Template for building new Claude Code agents — forces agents to inherit conventions from claude.md to prevent drift.|
| **Claude Code** | [Eval Feedback Command](.claude/commands/eval-feedback.md) |Updates the relevant agent or skill based on user's evaluation feedback. |
| **Claude Code** | [Interview Analysis Agent](.claude/agents/interview-analysis.md) | Analyses user research interviews for pain points, bright spots, and project-specific dimensions — one file per participant, with verbatim quotes. No synthesis. |
| **Claude Code** | [Survey Analysis Agent](.claude/agents/survey-analysis.md) | Automatically calculates survey margin of error and highlights key themes by user segment to speed up product discovery|
| **Claude Code** | [Company Context Agent](portfolio/create-company.md) | Conducts automated deep-dives into a company, its competitors, market landscape, and products. Serves as context for other agents (e.g, Interview Analysis agent, PRD Generator)|
| **Claude Code** | [PRD Generator](others/01-prd-generator) | **Experiment only:** Creates PRD draft by synthesizing market research and internal company context files.<br>**Caveat:** Aimed to speed up summarization and initial ideation but cannot replace the deep understanding of problem context and strategic direction that a PM must first start with. |
| **OpenClaw** | [Competitive Intel](.claude/agents/competitive-intel.md) | Sends a weekly competitive intelligence reports to PMs. |
| **n8n** | [Agentic RAG Contract Auditor](others/04-agentic-rag) | Enhances retrieval when analyzing legal risks in contracts for lawyers. |
| **n8n** | [Traditional RAG Chatbot](others/05-traditional-rag) | Enables users to overcome context window limits. |
