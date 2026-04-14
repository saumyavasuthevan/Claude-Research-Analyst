Research a company and generate all context files for it.

## Step 1 — Get Company Name

If the user has not already specified a company name, ask:
"What company would you like to research?"

Wait for their response before proceeding.

## Step 2 — Confirm Output Location

Check whether `projects/[CompanyName]/` already exists:
- If it does, note its contents and confirm with the user before overwriting anything.
- If it doesn't, confirm the company name spelling/capitalisation before proceeding (use the company's official capitalisation).

## Step 3 — Spawn the Agent

Once the company name is confirmed, spawn the `create-company` agent with this brief:

```
Company name: [CompanyName]
Output folder: projects/[CompanyName]/01- company context/
Templates folder: templates/
```

Let the agent handle all research and file writing. Report its summary back to the user when done.
