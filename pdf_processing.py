from pdfminer.high_level import extract_text

def input_pdf_text(uploaded_file):
    return extract_text(uploaded_file)
