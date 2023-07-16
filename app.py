'''
The module for the streamlit app.
'''


import streamlit as st
from custom_cover_llm import generate_cover_letter
import tempfile

st.title('CovrCraft - Create your cover letter effortlessly!')
token = st.secrets["BARD_TOKEN"]

letter_type = ['LinkedIn Connect Message', 'Full length Cover Letter']

def generate_response(url, resume_file, selected_option):

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(resume_file.read())
        resume_path = tmp_file.name

    output = generate_cover_letter(resume_path, url, selected_option, token)
    st.write(output)

with st.form('cover_letter_form'):
    job_url = st.text_area('Enter Public LinkedIn URL for the job posting: ')
    resume_file = st.file_uploader("Upload your resume", type=["pdf"], accept_multiple_files=False)
    letter_type_selected = st.radio("Select the type of letter: ", letter_type)

    submitted = st.form_submit_button('Generate')

    if submitted:
        if job_url.strip() != "" and resume_file is not None:
            generate_response(job_url, resume_file, letter_type_selected)
        else:
            st.write("Please provide both the job URL and the resume file.")