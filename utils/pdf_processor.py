import fitz


def extract_text_from_pdf(pdf_file):
    """
    Extract all text from uploaded PDF.
    """
    text = ""

    try:
        pdf_bytes = pdf_file.read()

        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:
        text = f"Error reading PDF: {e}"

    return text