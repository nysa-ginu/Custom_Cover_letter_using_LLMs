'''
This module would convert the pdf into text so that in can given to the Large Langugae Model.
'''

import pypdf


def extract_text_from_pdf(pdf):
    resume_text = ""

    reader = pypdf.PdfReader(pdf)

    # Iterate through each page in the PDF
    for page in reader.pages:
        resume_text += page.extract_text()

    return resume_text
