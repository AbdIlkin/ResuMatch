import streamlit as st
from pdf_processing import input_pdf_text
from llm_response import get_gemini_response
from prompts import input_prompt1, input_prompt2, input_prompt3, input_prompt4

# Streamlit configuration
st.set_page_config(page_title="Resume Expert")

st.header("ResuMatch")
st.subheader('This Application helps you in your Resume Review with help of AI [LLM]')

# Increase the width of the job description input box
job_description = st.text_area("Job Description: ", key="input", height=150)

uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

# Buttons for different functionalities
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve my Skills")
submit3 = st.button("What are the Keywords That are Missing")
submit4 = st.button("Percentage match")

# Process the PDF and generate responses based on the selected functionality
if uploaded_file is not None:
    pdf_content = input_pdf_text(uploaded_file)
    
    if submit1:
        response = get_gemini_response(input_prompt1, pdf_content, job_description)
        st.subheader("The Response is")
        st.write(response)
        
    elif submit2:
        response = get_gemini_response(input_prompt2, pdf_content, job_description)
        st.subheader("The Response is")
        st.write(response)
        
    elif submit3:
        response = get_gemini_response(input_prompt3, pdf_content, job_description)
        st.subheader("The Response is")
        st.write(response)
        
    elif submit4:
        response = get_gemini_response(input_prompt4, pdf_content, job_description)
        st.subheader("The Response is")
        st.write(response)
else:
    st.write("Please upload a PDF file to proceed.")
