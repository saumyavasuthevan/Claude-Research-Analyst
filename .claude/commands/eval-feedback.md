Process evaluation feedback on an agent or skill output: convert the feedback file to Markdown, analyse it, update the relevant agent or skill, and explain every change made.

## Step 1 — Identify the active company and feedback file

**Identify the active company** using the standard project resolution rules from CLAUDE.md.

Once the company is confirmed, scan `projects/[CompanyName]/06- evals/` for files:
- List all files in the folder.
- If the folder is empty or does not exist, tell the user and stop.
- If there are multiple unprocessed files, list them and ask which to process. Process one at a time.

Once the target file is identified, check its extension:
- If already `.md`: skip to Step 3.
- If `.xlsx`, `.xls`, `.csv`, `.pdf`, `.docx`, or `.doc`: proceed to Step 2.
- If any other format: tell the user it is unsupported and stop.

## Step 2 — Convert the feedback file to Markdown

Follow the `/convert-to-md` command instructions to convert the file. Save the `.md` output in `projects/[CompanyName]/06- evals/` using the same base filename.

Do not ask for confirmation before converting — the user has already initiated this workflow.

After saving, tell the user:
> "Converted [filename] → [filename.md]"

Then offer to delete the original:
> "Would you like me to delete the original [filename]?"

Wait for their response before deleting.

## Step 3 — Identify the target agent or skill

Check whether the user has already specified which agent or skill the feedback relates to (e.g. "update the interview-analysis agent").

If not, infer it from:
1. The feedback file name (e.g. `HPB-interview-analysis-U1` → `interview-analysis` agent)
2. The content of the feedback file (look for references to output structure, section names, or task types that match a known agent or skill)

Known locations to check:
- Agents: `.claude/agents/*.md`
- Commands/skills: `.claude/commands/*.md`

If inference is ambiguous, list candidates and ask the user to confirm before proceeding.

Once identified, read the full target file before continuing.

## Step 4 — Read and analyse the feedback

Read the converted Markdown feedback file in full.

For each row or item in the feedback:
- Identify the **issue type** (e.g. incorrect quote, missing finding, flattened finding, demographic assumption, subjective extraction, quote lacks context)
- Note the specific output it references
- Determine what rule or instruction in the agent/skill caused or failed to prevent this issue

Ignore any rows explicitly flagged by the user as out of scope (e.g. "ignore rows about X").

Group issues by type. If the same root cause appears multiple times, treat it as one change — do not add duplicate rules.

## Step 5 — Update the target agent or skill

For each distinct root cause identified in Step 4, make the minimal targeted edit to the agent or skill that would prevent that class of issue in future runs.

Prefer editing existing rules or instructions over adding new ones. Only add a new rule if no existing instruction covers the gap.

Do not rewrite sections that are unrelated to the feedback.

## Step 6 — Explain every change

After all edits are saved, output a structured explanation:

```
## Changes made to [agent/skill name]

### 1. [Short title of change]
**Feedback that drove this:** [quote the issue type and/or specific row]
**What was changed:** [which section/rule was edited or added]
**Why:** [what failure this prevents]

### 2. [Short title of change]
...
```

Every edit must be accounted for. Do not summarise multiple changes under one entry unless they share an identical root cause.
