---
name: clawsolver
description: Solve math problems from PDF files. Extract questions, work through them step-by-step, and present solutions clearly. Use when a user uploads or provides a path to a PDF containing math problems, homework, exams, or exercises.
---

# ClawSolver

## Setup

Requires `pdfplumber`:
```bash
pip install pdfplumber
```

## Workflow

1. **Extract** the PDF text:
   ```bash
   python3 scripts/extract_pdf.py <path/to/file.pdf>
   ```

2. **Parse** — identify each distinct problem (numbered, lettered, or sectioned).

3. **Solve** each problem step-by-step. Show working clearly. Use plain text math notation (`x^2`, `sqrt(x)`, `integral`) unless the user asks for LaTeX.

4. **Present** solutions grouped by problem number/label. Flag ambiguous or incomplete problems.

## Notes
- Works on typed/digital PDFs. Scanned/image PDFs return empty text — ask the user for a text-based PDF.
- For large PDFs, work page by page and confirm which section to focus on.
- Tables (e.g. stats data sets) extract as text and may need manual cleanup.
