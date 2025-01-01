import streamlit as st
from resume import Resume
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader
from io import BytesIO
from chains import Chain

st.title("📧 Cold Mail Generator")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
url_input = st.text_input("Enter a URL:", placeholder="https://example-job.com/")
submit_button = st.button("Submit")

global resume

if uploaded_file is not None:
    pdf_bytes = BytesIO(uploaded_file.read())
    resume_instance = Resume()
    resume=resume_instance.load_resume(pdf_path=pdf_bytes)

if submit_button:
    if uploaded_file is None and not url_input:
        st.warning("Please upload a resume and enter a URL before submitting.")
    elif uploaded_file is None:
        st.warning("Please upload a resume before submitting.")
    elif not url_input:
        st.warning("Please enter a URL before submitting.")
    else:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            chain = Chain()
            jobs = chain.extract_jobs(data)
            if jobs and resume:
                email = chain.write_mail(resume, jobs)
                st.write("Email:")
                st.code(email, language='markdown')
            elif not resume:
                st.warning("Please upload valid resume")
            elif not jobs:
                st.warning("Can't access the job site.")
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


