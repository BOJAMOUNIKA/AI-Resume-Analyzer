import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return text

    except Exception as e:
        return f"Error: {e}"