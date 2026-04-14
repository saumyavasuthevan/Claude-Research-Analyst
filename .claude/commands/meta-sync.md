You are performing a structured meta-file audit. Your job is to detect gaps between what was built and what is documented, then propose and apply updates.

## Step 1 — Check .claudeignore First

Read `.claudeignore`. Note every path listed. Do not read, reference, or act on any of those files at any point in this command.

## Step 2 — Understand Recent Changes

Run:

```bash
git log --oneline -20
git diff HEAD~5 --name-only
```

List the changed files. Use this as the primary signal for what may need documenting.

## Step 3 — Audit Each Meta-File

For each file below, determine: ✅ up to date / ⚠️ needs update. If ⚠️, describe exactly what needs to change before touching anything.

### 3a — CLAUDE.md

Check:
- New agents in `.claude/agents/` not listed under **Available Agents & Skills**
- Removed agents still listed
- New skills in `.claude/skills/` not listed
- New commands in `.claude/commands/` not listed
- Any rule in the Standards Checklist that is stale or missing given recent changes

### 3b — README.md

Check for agents, skills, or commands not yet in the experiment index table, and rows pointing to files that no longer exist.

**If a row needs adding**, follow the row derivation and insertion rules in `.claude/commands/update-readme.md` exactly.

### 3c — MEMORY.md + memory files

Memory location: `~/.claude/projects/-Users-saumyavasuthevan-Documents-Dev-GitRepo-AI-Experiments/memory/`

Check:
- `MEMORY.md` index — does every entry still point to a real file?
- Are there memory files not indexed in `MEMORY.md`?
- Are any memories now stale (e.g. a rule already added to CLAUDE.md doesn't need a separate memory entry)?

### 3d — .claudeignore

Check:
- Entries pointing to files/folders that no longer exist (stale)
- Any new files/folders that match patterns already in `.claudeignore` that should also be ignored

## Step 4 — Present Findings Before Touching Anything

Output a single audit table:

| File | Status | Proposed change |
|---|---|---|
| CLAUDE.md | ✅ / ⚠️ | [what to add/remove/update, or "none"] |
| README.md | ✅ / ⚠️ | [what to add/remove/update, or "none"] |
| MEMORY.md | ✅ / ⚠️ | [what to add/remove/update, or "none"] |
| .claudeignore | ✅ / ⚠️ | [what to add/remove/update, or "none"] |

Then ask:
> "Shall I apply all ⚠️ changes, or would you like to review each one individually?"

**Do not make any edits until the user confirms.**

## Step 5 — Apply Confirmed Changes

Apply only the changes the user approved. After each file is updated, confirm with the filename and a one-line summary of what changed.

## Rules

- Never read or modify files listed in `.claudeignore`
- Never delete content from CLAUDE.md or README.md without explicit user approval
- If a memory entry is stale, propose removal — don't silently delete
- If unsure whether something needs updating, flag it as ⚠️ with a question rather than assuming
