---
name: clawsolver
description: Solve math problems from PDF files. Extract questions, work through them step-by-step, and present clear solutions. Use when a user uploads or provides a path to a PDF containing math problems, homework, exams, worksheets, or exercises of any level (arithmetic through calculus/linear algebra).
---

# ClawSolver

## Setup

Requires `pdfplumber`:
```bash
pip install pdfplumber
```

## Workflow

### 1. Extract
```bash
python3 scripts/extract_pdf.py <path/to/file.pdf>
```
Output is page-labeled plain text. If the output is empty, the PDF is image-based — tell the user it needs to be a text/digital PDF.

### 2. Identify Problems
Scan the extracted text and identify each distinct problem by:
- Numbered items (1., 2., Q1, Q2)
- Lettered parts (a), b), i., ii.)
- Section headers (Part A, Section 2)

Group multi-part problems together. Note page numbers if the PDF spans multiple pages.

### 3. Solve
Work through each problem methodically:
- Show all steps — don't skip algebra
- Use plain text notation by default: `x^2`, `sqrt(x)`, `d/dx`, `integral from a to b`
- Switch to LaTeX only if the user asks
- For word problems: state what's given, what's asked, then solve
- For proofs: state the approach before diving in
- If a problem is ambiguous or missing information, flag it and state your assumption

### 4. Present
Format output as:
```
Problem 1: [brief restatement]
Solution:
[step-by-step working]
Answer: [final answer, clearly marked]

Problem 2: ...
```

## Subject Coverage
Handle all standard math subjects:
- **Arithmetic / Algebra** — equations, inequalities, factoring, systems
- **Geometry** — area, volume, proofs, coordinate geometry
- **Trigonometry** — identities, equations, unit circle
- **Calculus** — limits, derivatives, integrals, series
- **Linear Algebra** — matrices, determinants, eigenvalues
- **Statistics** — probability, distributions, hypothesis testing
- **Discrete Math** — combinatorics, logic, proofs

## Edge Cases
- **Multi-page exams**: Offer to solve one section at a time if the PDF is long
- **Tables / data sets**: pdfplumber extracts them as text rows — re-read carefully before solving stats problems
- **Figures/diagrams**: pdfplumber cannot extract images. If a problem references a diagram, ask the user to describe it
- **Scanned PDFs**: Empty extraction output = image-based PDF. Tell the user and stop
- **Partial credit style**: If unsure of final answer, show working clearly and flag uncertainty rather than guessing
