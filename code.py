import ollama
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
import os


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print("Error with PyPDF2:", e)

    if not text.strip():
        print("Performing OCR as fallback ...")
        images = convert_from_path(pdf_path, dpi=300)
        for image in images:
            text += pytesseract.image_to_string(image)

    return text.strip()


def compare_with_ollama(tender_latex_text, proposal_pdf_path):
    proposal_text = extract_text_from_pdf(proposal_pdf_path)

    prompt = f"""
You are a tender evaluation AI. Evaluate how well the following company
proposal matches the tender requirements by only giving the matching score out of 100.

Tender Requirements (LaTeX format):
{tender_latex_text}

Company Proposal (Extracted from PDF):
{proposal_text}

Give a score between 0 and 100, and explain your reasoning.
"""

    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


# --- Main Execution ---
tender_latex_text = r"""
\documentclass{article}
\begin{document}
\section*{System Requirements}
\begin{itemize}
\item Minimum of \textbf{16 GB RAM}
\item Processor with a clock speed of at least \textbf{4 GHz}
\item Operating system must be \textbf{Windows 10 or higher}
\end{itemize}
\end{document}
"""

proposal_pdf_path = "company2m.pdf"

result = compare_with_ollama(tender_latex_text, proposal_pdf_path)
print(result)
