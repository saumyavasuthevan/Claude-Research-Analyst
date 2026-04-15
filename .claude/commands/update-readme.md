Add a new row to the README.md experiment index for a new skill, agent, or experiment.

## Step 1 — Ask what to document

Ask the user only one question:

> "What skill, agent, or experiment should I add to the README? Tell me what it does and point me to the relevant file or folder in the repo (or I'll try to find it)."

Wait for the user's response before continuing.

## Step 2 — Gather context

Read `README.md` to understand the existing row style (tone, naming convention, description length).

If the user gave a file or folder path, verify it exists in the repo. If they didn't, search the repo for a likely match based on what they described (check `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, and `projects/`).

## Step 3 — Derive the row automatically

Using the existing rows as style reference, determine:

- **Tool** — always `**Claude Code**`
- **Experiment name** — derive a short, consistent name matching the style of existing entries
- **Link** — find the file or folder on disk first using Glob or Bash `ls`, then construct the GitHub URL from the confirmed local path
  - The repo root is `/Users/saumyavasuthevan/Documents/Dev/GitRepo/AI-Experiments/`
  - Strip the repo root to get the relative path, then build: `https://github.com/saumyavasuthevan/AI-Experiments/blob/main/[relative-path]`
  - Use `/tree/main/` for folders, `/blob/main/` for files
  - **Never construct a GitHub URL without first confirming the file/folder exists on disk. If you cannot find a matching file, tell the user and ask them to provide the path.**
- **Description** — write a concise description matching the tone and length of existing rows. Rules:
  - Lead with a strong verb: "Analyses...", "Calculates...", "Reviews...", "Conducts..." — never lead with "Agent that", "Skill that", or "Command that"
  - Use a purpose clause ("to resolve X", "to speed up X", "for Y") to frame the problem being solved — not the mechanics or output
  - The test: does the description explain *why someone would use this*, not just *what it technically does*?
  - Max ~20 words. No nested clauses. No redundant phrases.
  - Match the style of these human-written examples:
    - `Analyses user research interviews for pain points, bright spots, and project-specific dimensions — one file per participant, with verbatim quotes. No synthesis.`
    - `Automatically calculates survey margin of error and highlights key themes by user segment to speed up product discovery`
    - `Reviews and updates agent, skill, and command files to resolve conflicts, avoid template drift, and ensure consistency across files.`

## Step 4 — Insert into README.md

Read `README.md`. Insert the new row as the **first data row** of the table — directly after the header and divider rows (`| :--- |` line), pushing all existing rows down.

Save the file, then show the user the row that was added.
