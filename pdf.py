from google import genai
from google.genai import types
from PyPDF2 import PdfReader
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
client_model = genai.Client(api_key=config["apiKey"])
model_name="gemini-1.5-flash"
prompt="sometext"
directory_path="c:/Users/katun/OneDrive/all staff/Documents/AI-Mbararara-HiveColab-Hackthon/MyDocs"

def extract_and_embend(directory_path, model_name, prompt):

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, file_name)
            with open(pdf_path, "rb") as file:
                pdf_bytes = file.read()
                reader = PdfReader(file)
                for page in reader.pages:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=[
                            types.Part.from_bytes(
                                data=pdf_bytes,
                                mime_type='application/pdf',
                            ),
                            prompt
                        ]
                    )
                    print(f"Summaryclear  for {file_name}: {response.text}")
