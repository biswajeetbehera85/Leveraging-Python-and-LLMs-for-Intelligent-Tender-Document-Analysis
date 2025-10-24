# Leveraging-Python-and-LLMs-for-Intelligent-Tender-Document-Analysis

This project demonstrates how Python, OCR, and Large Language Models (LLMs) can be used to automate tender document evaluation.
It extracts data from PDF tenders, compares them against LaTeX-based tender requirements, and provides a match score with reasoning using the Mistral model via the ollama API.

🚀 Features

🧾 Extract text from digital and scanned PDFs

🔍 Perform OCR using pytesseract when text extraction fails

🧠 Compare extracted text with tender specifications using an LLM (Mistral)

📊 Generate a score and explanation of document compliance

🧩 Supports both structured and unstructured document inputs

⚙️ Modular design for easy integration into larger automation workflows

🏗️ System Architecture
PDF Document ─┬─▶ PyPDF2 (Text Extraction)
               │
               ├─▶ OCR (pytesseract + pdf2image)
               │
               └─▶ Extracted Text ─▶ LLM (ollama) ─▶ Score + Reasoning

📂 Project Structure
📁 Tender-Document-Analyzer/
│
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── sample_tender.tex      # Example LaTeX tender document
├── proposal.pdf           # Example proposal PDF
├── README.md              # Project documentation
└── outputs/               # (Optional) Directory for storing results

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/tender-doc-analysis.git
cd tender-doc-analysis

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install & Configure Tesseract OCR

Windows: Download from Tesseract OCR

Linux (Debian/Ubuntu):

sudo apt install tesseract-ocr


Add Tesseract to your system PATH.

4️⃣ Install Ollama (for LLM access)

Follow the instructions from https://ollama.com/

Then pull the Mistral model:

ollama pull mistral

🧩 Usage
🧠 Run the Tender Evaluation
python main.py


The script will:

Extract text from your input proposal PDF.

Use OCR if the file is scanned or image-based.

Send the extracted text + tender LaTeX spec to the Mistral LLM.

Display a compliance score and reasoning in the terminal.

🧰 Example Output
Performing OCR as fallback ...
LLM Evaluation:
Score: 87/100

Reasoning:
The proposal meets most hardware requirements (16 GB RAM, 4 GHz CPU)
but lacks mention of Windows 10 compliance.

🧾 Example LaTeX Tender Requirements
\documentclass{article}
\begin{document}
\section*{System Requirements}
\begin{itemize}
\item Minimum of \textbf{16 GB RAM}
\item Processor with a clock speed of at least \textbf{4 GHz}
\item Operating system must be \textbf{Windows 10 or higher}
\end{itemize}
\end{document}

🧪 Testing Strategy

Test with native PDFs (digital text)

Test with scanned PDFs (image text)

Validate OCR accuracy using known documents

Verify LLM consistency by rerunning with different wording

🔮 Future Enhancements

Add web-based GUI using Streamlit or Flask

Support batch evaluation of multiple proposals

Integrate semantic vector search for document retrieval

Export comparison reports in PDF/CSV format

📚 Libraries Used
Library	Purpose
PyPDF2	Extract text from text-based PDFs
pytesseract	OCR for scanned/image PDFs
pdf2image	Converts PDF pages to images for OCR
Pillow (PIL)	Image processing and optimization
ollama	Interface to Mistral LLM for text comparison
os	File handling and system operations

License:

This project is intended for academic and research purposes only.
All rights reserved © 2025 DRDO – Integrated Test Range, Chandipur.
