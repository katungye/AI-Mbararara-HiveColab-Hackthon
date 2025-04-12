import os
from dotenv import dotenv_values
from google import genai
from PyPDF2 import PdfReader
config = dotenv_values(".env")

client = genai.Client(api_key=config["apiKey"])

file_path = "c:/Users/katun/OneDrive/all staff/Documents/AI-Mbararara-HiveColab-Hackthon/MyDocs"

def extract_embend():
    # Loop through all the PDFs and extract text
for file_name in os.listdir(file_path):
    if file_name.endswith(".pdf"):
        pdf_path = os.path.join(file_path, file_name)
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()

# Pass the extracted text to the model
result = client.models.embed_content(
    model="gemini-embedding-exp-03-07",
    contents=text
)

print(result.embeddings)
    

