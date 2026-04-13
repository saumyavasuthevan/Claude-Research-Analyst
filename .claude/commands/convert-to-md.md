Convert uploaded research files (CSV, XLSX, PDF, DOCX) to Markdown format for a company project.

## Step 1 — Resolve the company

Extract the company name from the user's message. Find the matching folder under `projects/` (case-insensitive). If ambiguous or not found, list available companies and ask.

## Step 2 — Scan for convertible files

Search these folders for non-`.md` files:
- `projects/[CompanyName]/01 - company context/`
- `projects/[CompanyName]/02 - project context/` (including all subfolders recursively)
- `projects/[CompanyName]/03- research/` (including all subfolders recursively)

Target file types: `.csv`, `.xlsx`, `.xls`, `.pdf`, `.docx`, `.doc`

List every file found. If none are found, tell the user and stop.

## Step 3 — Confirm before converting

Show the user the full list of files to convert:

```
Found X files to convert in [CompanyName]:

01 - company context/
  - filename.pdf  →  filename.md
  - ...

02 - project context/
  - filename.docx  →  filename.md
  - ...

03- research/
  - subfolder/filename.csv  →  subfolder/filename.md
  - ...
```

Ask: "Shall I proceed with converting these files?"

Wait for confirmation before continuing.

## Step 4 — Convert each file

For each file, apply the conversion method below. Output the `.md` file in the **same folder** as the source file, with the same base filename.

**Do not truncate or summarise content — preserve all data in full.**

---

### CSV files
Read the file and convert to a Markdown table, preserving all rows and columns. If the file has more than 500 rows, split into multiple tables with a header indicating the row range (e.g. `### Rows 1–500`).

---

### PDF files
Use the Read tool (it supports PDFs natively). Extract all text content and structure it as Markdown:
- Preserve headings, sections, and lists where detectable
- Use `---` horizontal rules to separate major sections
- Preserve tables as Markdown tables where possible
- If the PDF has multiple pages, add a `<!-- Page N -->` comment at each page boundary

---

### DOCX / DOC files
Run the following Bash command to convert using `pandoc` (preferred):

```bash
pandoc -f docx -t markdown "[input_path]" -o "[output_path]"
```

If `pandoc` is not available, try:

```bash
python3 -c "
import docx, sys
doc = docx.Document(sys.argv[1])
for para in doc.paragraphs:
    print(para.text)
" "[input_path]"
```

If neither is available, tell the user which tool is missing and ask them to install it (`brew install pandoc` or `pip install python-docx`), then stop.

---

### XLSX / XLS files
Run the following Bash command:

```bash
python3 -c "
import pandas as pd, sys, os
path = sys.argv[1]
xls = pd.ExcelFile(path)
output = []
for sheet in xls.sheet_names:
    df = pd.read_excel(path, sheet_name=sheet)
    output.append(f'## Sheet: {sheet}\n')
    output.append(df.to_markdown(index=False))
    output.append('\n')
print('\n'.join(output))
" "[input_path]"
```

If `pandas` or `tabulate` is not installed, run:

```bash
pip install pandas tabulate openpyxl
```

Then retry. If it still fails, tell the user what's missing and stop.

---

## Step 5 — Save output

Write each converted file as `[original_filename].md` in the same directory as the source file.

After all conversions, show a summary:

```
Converted X files:
  ✓ path/to/file.pdf  →  path/to/file.md
  ✓ path/to/file.csv  →  path/to/file.md
  ...
```

## Step 6 — Offer to delete originals

Once all files are saved, ask:

> "All X files have been converted. Would you like me to delete the original non-Markdown files? I'll list them one more time before deleting:
>
> [list of original files]
>
> Reply **yes** to delete, or **no** to keep them."

Only delete files if the user explicitly confirms. Delete them one by one using Bash `rm` — do not use wildcards or bulk delete commands.
