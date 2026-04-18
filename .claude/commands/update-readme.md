Add a new row to the README.md experiment index for a new skill, agent, or experiment.

## Step 1 — Ask what to document

Ask the user only one question:

> "What skill, agent, or experiment should I add to the README? Tell me what it does and point me to the relevant file or folder in the repo (or I'll try to find it)."

Wait for the user's response before continuing.

## Step 2 — Gather context

Read `README.md` to understand the existing row style (tone, naming convention, description length) and the current group sections.

If the user gave a file or folder path, verify it exists in the repo. If they didn't, search the repo for a likely match based on what they described (check `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, and `projects/`).

## Step 2b — Determine the group

Classify the new entry into one of the existing `###` sections based on its primary function:

- **Product Discovery** — research agents, interview/survey analysis, company intelligence, competitive intel
- **Artifacts** — document generators (PRDs, specs, reports)
- **Eval / Verification** — eval feedback processing, agent/skill quality checks
- **Observability** — hooks, logging, tracing, debug tooling
- **Tooling** — templates, sync commands, structural meta-tooling
- **RAG** — retrieval-augmented generation, chatbots, context window tools

If none of the above fits, propose a new `###` section name to the user before inserting.

## Step 3 — Derive the row automatically

Using the existing rows as style reference, determine:

- **Tool** — always `**Claude Code**`
- **Experiment name** — derive a short, consistent name matching the style of existing entries
- **Link** — find the file or folder on disk first using Glob or Bash `ls`, then construct the GitHub URL from the confirmed local path
  - The repo root is `/Users/saumyavasuthevan/Documents/Dev/GitRepo/AI-Experiments/`
  - Strip the repo root to get the relative path, then build: `https://github.com/saumyavasuthevan/AI-Experiments/blob/main/[relative-path]`
  - Use `/tree/main/` for folders, `/blob/main/` for files
  - **Never construct a GitHub URL without first confirming the file/folder exists on disk. If you cannot find a matching file, tell the user and ask them to provide the path.**
- **Description** — write a concise description matching the tone and structure of existing rows. Rules:
  - Lead with a strong verb: "Analyses...", "Evaluates...", "Reviews...", "Conducts..." — never lead with "Agent that", "Skill that", or "Command that"
  - Use 1–3 short sentences. Preferred structure: **Sentence 1** — what it evaluates/acts on (the object). **Sentence 2** — how it works (the mechanism). **Sentence 3** — the outcome or metric produced. Omit sentences that don't add meaning.
  - No inline code or backtick formatting. No feature checklists or enumeration — describe the purpose, not the feature list. No nested clauses.
  - Match the style of these human-written examples:
    - `Evaluates internal user research outputs. Combines human and machine evaluations to verify qual claims and quant calculations. Benchmarks Precision and Recall.`
    - `Evaluates external web-based research outputs. Aggregates human's subjective assessment of Helpfulness, Honesty, and Harmlessness scores across reports to benchmark HHH scores over time. Machine evaluates objective criteria in each report (e.g., link validity, template adherence).`
    - `Analyses user research interviews for pain points, bright spots, and project-specific dimensions — one file per participant, with verbatim quotes. No synthesis.`
    - `Captures tool inputs/outputs via deterministic shell hooks, preventing token consumption and Claude from forgetting instructions. Used by Debug Agent to trace errors and recommend improvements to agents and skills.`

## Step 4 — Insert into README.md

Read `README.md`. Locate the `###` section matching the group determined in Step 2b. Insert the new row as the **first data row** of that group's table — directly after the header and divider rows (`| :--- |` line), pushing existing rows in that group down.

Save the file, then show the user the row that was added and which group it was placed in.
