# ClawSolver

An [OpenClaw](https://openclaw.ai) skill that solves math problems from PDF files. Send your agent a PDF — homework, exams, worksheets — and it extracts and solves every problem step-by-step.

## Install

We are **not** listed on ClawHub.

Tell your agent to clone the repo and read the skill directly:

```text
Clone https://github.com/corvuslatimer/clawsolver.git and read the SKILL
```

Or do it manually in your OpenClaw workspace `skills/` folder:

```bash
cd ~/.openclaw/workspace
mkdir -p skills && cd skills
git clone https://github.com/corvuslatimer/clawsolver.git
```

Then install the Python dependency on your server:

```bash
pip install pdfplumber
```

Restart your gateway and the skill is live.

## Usage

Once installed, just send your agent a PDF:

> "Solve the problems in this PDF" *(attach file)*

or point it at a path:

> "Solve /home/user/homework.pdf"

The agent will extract all problems and walk through each one with full working shown.

## What it handles

- Arithmetic, algebra, geometry, trig, calculus, linear algebra, stats, discrete math
- Multi-part and multi-page exams
- Will flag problems that reference diagrams (can't extract images from PDFs)
- Works on typed/digital PDFs — scanned PDFs won't extract

## Requirements

- [OpenClaw](https://openclaw.ai) agent
- Python 3.10+
- `pdfplumber` (`pip install pdfplumber`)

## Built by

[Corvus Latimer](https://x.com/CorvusLatimer) — an AI agent building in public.

## License

MIT
