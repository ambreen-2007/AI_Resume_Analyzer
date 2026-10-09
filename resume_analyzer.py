# resume_analyzer.py

from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    PDF resume se text extract karta hai.
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def analyze_resume(pdf_file):
    """
    Resume PDF ko read karke uska text return karta hai.
    """

    text = extract_text_from_pdf(pdf_file)

    return text