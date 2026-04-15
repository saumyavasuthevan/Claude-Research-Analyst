You are performing a quality check on an agent, skill, or command file that was just edited. Your job is to find issues and propose fixes — grounded in the file itself and the conventions of this repo.

## Step 1 — Identify the Target File

If the user's message explicitly names a file, agent, skill, or command to check, use that. Otherwise, ask: "Which file should I check? Please give me the path or name (agents live in `.claude/agents/`, skills in `.claude/skills/`, commands in `.claude/commands/`)."

Do not infer the target from IDE context. Wait for an explicit answer before proceeding.

Read the file in full before proceeding.

## Step 2 — Read Reference Files

Read the following before doing any analysis:

- `.claude/_agent-template.md` — the canonical structure and rules all agents/skills must follow
- All other files in `.claude/agents/` and `.claude/skills/` — for reuse comparison

## Step 3 — Run Three Checks

### Check 1 — LLM Consistency

Read the file for instructions that contradict each other or would leave an LLM uncertain about what to do. Look for:

- Two rules that conflict (e.g. "always do X" in one place, "never do X" in another)
- A step that says one thing but an example or format block that implies something different
- Instructions that are ambiguous about ordering (e.g. "do A and B" with no guidance on which comes first when they interact)
- Duplicate rules that say the same thing in different words — pick the clearest, remove the other

### Check 2 — Template Compliance

Compare the file against `_agent-template.md`. Flag any rule or instruction that is already inherited from `CLAUDE.md` (per the inheritance table) and should be removed. Flag any required structural element from the template that is missing.

### Check 3 — Reuse Opportunities

Compare this file's approach to similar steps in other agent/skill files. Flag cases where this file has invented its own approach to something another file already handles — only flag it if adopting the shared approach would make this file clearer or more consistent, not just for the sake of uniformity.

## Step 4 — Present Findings

Output a single findings table:

| Check | Finding | Proposed fix |
|---|---|---|
| LLM Consistency | [issue or ✅ none] | [fix or —] |
| Template Compliance | [issue or ✅ none] | [fix or —] |
| Reuse | [issue or ✅ none] | [fix or —] |

For each proposed fix, apply the following decision rule before acting:

- **Unambiguous** (clear contradiction, duplicate rule, missing required element): apply immediately, no confirmation needed
- **Subjective or unclear** (e.g. reuse where the tradeoff is debatable, or a rewrite where multiple valid interpretations exist): flag it in the table and ask before touching it

After applying all unambiguous fixes, output a summary table:

| Fix | Action taken |
|---|---|
| [issue] | Applied / Flagged for review |

For any flagged items, ask a specific question — one per item — before proceeding.

## Rules

- Only flag real issues — do not manufacture findings to appear thorough
- Do not rewrite sections that are not broken
- Do not apply CLAUDE.md style preferences (tables over bullets etc.) to the agent instructions themselves — agents have their own output rules for good reason
