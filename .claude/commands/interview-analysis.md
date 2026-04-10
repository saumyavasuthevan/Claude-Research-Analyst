# Interview Analysis Agent

Analyze user research interview transcripts for a given company. Produce one analysis file per interview transcript.

## Step 1 — Get Company Name

If the user has not already specified a company name, ask:
"Which company's interview transcripts should I analyze? (e.g. 'widgets-inc')"

Wait for their response before proceeding.

## Step 2 — Resolve Paths

Set the following paths based on the company name provided:

- **Interviews folder:** `projects/[company-name]/02- research/Interviews/`
- **Context folder:** `projects/[company-name]/01- company context/`
- **Output folder:** `projects/[company-name]/03- analysis/`

List all `.md` files directly inside the interviews folder (non-recursive). If the folder does not exist or contains no `.md` files, stop and report:

```
Error: No interview transcripts found at projects/[company-name]/02- research/Interviews/
Please check the company name and ensure .md transcript files are present in that folder.
```

Do not proceed.

## Step 3 — Check for Already-Analysed Transcripts

List all files in `projects/[company-name]/03- analysis/`. For each transcript file found in Step 2, check whether a corresponding analysis file already exists in the output folder.

- If an analysis file already exists for a transcript, **skip it — do not re-analyse**.
- Only process transcripts that do not yet have a corresponding output file.

If all transcripts already have analysis files, stop and report:

```
All transcripts have already been analysed. No new files created.
```

## Step 4 — Read Company Context

Before reading any transcripts, read the following files (if they exist):

- `projects/[company-name]/01- company context/company-overview.md`
- `projects/[company-name]/01- company context/user-personas.md`
- `projects/[company-name]/01- company context/product-description.md`
- `projects/[company-name]/01- company context/competitive-landscape.md`

Also read all `.md` files inside `projects/[company-name]/02- research/PRDs/` (if the folder exists).

If none of these files exist, note this and proceed.

## Step 5 — Process Each New Transcript

For each transcript not already analysed:

1. Read the full file.
2. If the file is empty or under 100 words, skip it. Log the filename — do not create an output file for it.
3. If the file has 100+ words, extract:

   **Pain Points**
   - Friction, frustration, unmet needs, or workarounds the participant described
   - Each pain point MUST include all relevant verbatim quotes from the transcript (minimum 1, no upper limit — capture every quote that supports or elaborates the point)
   - Example pain point: Users could not find relevant support content (e.g. FAQs, error messages) when they ran into problems.
     > "From FAQ, don't know if [this query] is here, try to search it. There's so many things here! Why spend so much time searching?" — U1

   **Bright Spots**
   - Moments of delight, things working well, positive surprises
   - Each bright spot MUST include all relevant verbatim quotes from the transcript (minimum 1, no upper limit — capture every quote that supports or elaborates the point)
   - Example bright spot: Most email templates were easy for users to understand.
     > "[Did you need help understanding templates?] No, they were easy to understand." — U1

4. Write one output file for this transcript immediately after processing it (do not batch).

## Step 6 — Output File Per Transcript

### Filename convention

Derive the unit identifier from the source filename:
- `U1-john.md` → `[Company-Name]-interview-analysis-U1.md`
- `interview-U4.md` → `[Company-Name]-interview-analysis-U4.md`
- If no number is detectable, use the source filename stem: `[Company-Name]-interview-analysis-john.md`

Save to: `projects/[company-name]/03- analysis/[Company-Name]-interview-analysis-[unit].md`

If the `03- analysis/` folder does not exist, create it before writing the first file.

### Output file structure

```markdown
# [Company Name] Interview Analysis — [Unit]

**Source file:** [source-filename.md]
**Analysis date:** [today's date]

---

## Pain Points

### [Pain Point Title]
- **Description:** [brief description of the friction or unmet need]
- **Supporting quotes** (include ALL relevant quotes from the transcript — minimum 1, no upper limit):
  > "[verbatim quote]" — U1
  > "[verbatim quote]" — U2

[Repeat for each pain point]

---

## Bright Spots

### [Bright Spot Title]
- **Description:** [brief description of the positive finding]
- **Supporting quotes** (include ALL relevant quotes from the transcript — minimum 1, no upper limit):
  > "[verbatim quote]" — U1
  > "[verbatim quote]" — U2

[Repeat for each bright spot]
```

## Step 7 — Confirm

After all files are written, confirm with:

```
Interview analysis complete for [Company Name].

Files written:
  - [filename] (from [source])
  - [filename] (from [source])
  ...

Transcripts skipped (already analysed): [list, or "none"]
Transcripts skipped (too short / empty): [list, or "none"]
```

## Rules

- **Do not synthesise insights or make recommendations.** Summarise only — capture what participants said.
- Every pain point and bright spot must be grounded in at least one verbatim quote.
- Do not read files outside the `02- research/Interviews/` folder (except context files in Step 4).
- **Never edit or paraphrase verbatim quotes — copy the exact words from the transcript, character for character.**
- If an interviewer question is needed to make a quote understandable, include it in square brackets immediately before the participant's response: `[Interviewer question] Participant's answer`.
- Label speakers as U1, U2, U3, etc. — never as "participant" or any generic label. If the transcript includes a speaker name, append it in brackets: `U1 (Shawn Choy)`. If there are multiple speakers with names, always identify the correct speaker per quote (e.g. `U1 (Shawn Choy)` vs `U2 (Amanda Klein)`).
- If a transcript has no clear pain points or bright spots, include a note: "No pain points identified" / "No bright spots identified".
- State assumptions clearly if the transcript format is ambiguous (e.g. no speaker labels).
- Never overwrite an existing analysis file — skip it and note it in the confirmation.
