# ClawSolver

An OpenClaw skill that extracts and solves math problems from PDF files.

## What it does

Drop a PDF containing math problems — homework, exams, exercises — and ClawSolver extracts the text and walks through each problem step-by-step.

## Requirements

```bash
pip install pdfplumber
```

## Usage

```bash
python3 scripts/extract_pdf.py path/to/problems.pdf
```

Then let the agent solve what's extracted.

## Install as a skill

Copy this folder into your OpenClaw workspace `skills/` directory, or install via [ClawHub](https://clawhub.com).

## Notes

- Works on typed/digital PDFs. Scanned PDFs (image-based) won't extract — use a text-based PDF.
- Built by [Corvus Latimer](https://x.com/CorvusLatimer)

## License

MIT
