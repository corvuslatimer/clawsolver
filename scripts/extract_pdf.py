#!/usr/bin/env python3
"""Extract text from a PDF file, page by page."""

import sys
import pdfplumber

def extract(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text and text.strip():
                pages.append(f"--- Page {i} ---\n{text.strip()}")
    return "\n\n".join(pages)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_pdf.py <path/to/file.pdf>")
        sys.exit(1)
    print(extract(sys.argv[1]))
