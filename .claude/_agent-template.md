---
name: agent-name
description: "One-line description of when to trigger this agent."
model: sonnet
color: teal
---

> **Before saving:** Check each rule you've written against the inheritance table in `CLAUDE.md` → "What Agents & Skills Inherit Automatically". If a rule is listed there, remove it. Only keep rules specific to this agent.

You are a [role]. Your job is to [what you do].

## Step 1 — Resolve Active Company

Follow CLAUDE.md active project resolution to identify the company and set paths.

## Step 2 — Find Input File(s)

[Describe where to look for input files and how to handle missing/multiple files.]

## Step 3 — Read Company Context

Read standard context files per CLAUDE.md before proceeding.

## Step 4 — Confirm Approach Before Proceeding

[Summarise what you found and ask any clarifying questions before doing substantive work.]

## Step 5 — [Core Task]

[Describe the analysis, generation, or processing task.]

## Step 6 — Save Output

> Specify the correct folder for this agent:
> - Research analysis → `04- analysis/`
> - PM deliverables → `05- outputs/[YYYY-MM-DD]-[task-name].md`
> - Company context → `01- company context/`

Save to `projects/[company-name]/[specify-correct-folder]/[filename].md`.

If the output folder does not exist, create it before writing.

Check whether the file already exists — if so, ask the user before overwriting.

## Step 7 — Confirm

After the file is written, confirm with:

```
[Task] complete for [Company Name].

File written: [filename]
Location: [path]
```

## Agent-Specific Rules

- [Only list rules that are not already in CLAUDE.md or CLAUDE.local.md]
