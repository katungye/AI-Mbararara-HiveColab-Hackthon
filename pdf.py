from google import genai
from google.genai import types
from PyPDF2 import PdfReader
from dotenv import dotenv_values
import os
import streamlit as st

# Load environment variables
config = dotenv_values(".env")
client_model = genai.Client(api_key=config["apiKey"])
model_name = "gemini-1.5-flash"

# Directory containing PDF files
pdf_directory = r"c:/Users/katun/OneDrive/all staff/Documents/AI-Mbararara-HiveColab-Hackthon/MyDocs"

# List all PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

st.sidebar.header("Available PDFs")
selected_pdf = st.sidebar.selectbox("Choose a PDF file", pdf_files)

if selected_pdf:
    # Extract text from the selected PDF
    pdf_path = os.path.join(pdf_directory, selected_pdf)
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()

    st.write("### Extracted Text")
    st.text_area("PDF Content", extracted_text, height=200)

    # Chatbot interaction
    st.write("### Chat with the PDF")
    user_input = st.text_input("Ask a question about the PDF:")
    if user_input:
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        response = client_model.models.generate_content(
            model=model_name,
            contents=[
                types.Part.from_bytes(
                    data=pdf_bytes,
                    mime_type='application/pdf',
                ),
                user_input
            ]
        )
        st.write("#### Response")
        st.write(response.text)
