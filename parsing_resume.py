'''
This module would convert the pdf into text so that in can given to the Large Langugae Model.
'''

import PyPDF2


def extract_text_from_pdf(pdf):
    resume_text = ""

    # with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(pdf)

    # Iterate through each page in the PDF
    for page in reader.pages:
        resume_text += page.extract_text()

    return resume_text

# Example usage
# pdf_file_path = 'Nysa_Ginu_Resume_word_1.pdf'
# extracted_text = extract_text_from_pdf(pdf_file_path)
# print(extracted_text)