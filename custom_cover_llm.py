'''
This module uses the LLM model (BARD by Google) to generate the content.
'''

import os
import streamlit as st
from bardapi import Bard
from parsing_job_desc import get_job_info
from parsing_resume import extract_text_from_pdf

def generate_cover_letter(resume_path, job_url, selected_option):

    role_name, company_name, desc = get_job_info(job_url)

    resume = extract_text_from_pdf(resume_path)

    if selected_option == "LinkedIn Connect Message" :
        prompt = "In less than 60 words, Write message to recruiter using the resume for the role of " + str(role_name) + " at company " + str(company_name)
        input_text = prompt + " [RESUME] " + resume

    elif selected_option == "Full length Cover Letter" :
        prompt = "Write a cover letter for the given job desription using the resume for the role of " + str(role_name) + " at company " + str(company_name)
        input_text = prompt + " [RESUME] " + resume + " [JOB DESCRIPTION] " + desc

    token = st.secrets["BARD_TOKEN"]
    bard = Bard(token=token)
    response = bard.get_answer(input_text)['content']
    
    return response
