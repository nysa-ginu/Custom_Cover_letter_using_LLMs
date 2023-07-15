import os
from bardapi import Bard

from parsing_job_desc import get_job_info
from parsing_resume import extract_text_from_pdf

def generate_cover_letter(resume_path, job_url):

    role_name, company_name, desc = get_job_info(job_url)

    resume = extract_text_from_pdf(resume_path)
    prompt = "Write a cover letter for the given job desription using the resume for the role of " + str(role_name) + " at company " + str(company_name)

    input_text = prompt + " [RESUME] " + resume + " [JOB DESCRIPTION] " + desc

    token = os.environ.get('BARD_TOKEN')
    bard = Bard(token=token)
    response = bard.get_answer(input_text)['content']
    
    return response


# url = "https://www.linkedin.com/jobs/view/3638577861/?alternateChannel=search&refId=din%2BbPLwmuV0hMnzrJ3Rtw%3D%3D&trackingId=QwSYVyt4PcFEt8yAfF8fNQ%3D%3D"
# path = "Nysa_Ginu_Resume_word_1.pdf"
# role_name, company_name, desc = get_job_info(url)
# resume = extract_text_from_pdf(path)
# prompt = "Write a cover letter for the given job desription using the resume for the role of " + str(role_name) + " at company " + str(company_name)
# Example usage

# Generate the cover letter
# cover_letter = generate_cover_letter(prompt, resume, desc)

# Print the cover letter
# print(cover_letter)
