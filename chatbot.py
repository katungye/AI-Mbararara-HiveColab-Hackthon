import os
from dotenv import dotenv_values
from google import genai
from google.genai import types
import pathlib


# Load API key from .env file
config = dotenv_values(".env")
client_model = genai.Client(api_key=config["apiKey"])

# Path to the folder containing PDF files
file_path = pathlib.Path("c:/Users/katun/OneDrive/all staff/Documents/AI-Mbararara-HiveColab-Hackthon/MyDocs")

# Models
embedings_model = "gemini-embedding-exp-03-07"
llm_model = "gemini-1.5-flash"

def process_pdfs(folder_path: str):
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_name}")

            # Generate embeddings for the PDF
            with open(file_path, "rb") as file:
                response = client_model.models.generate_embeddings(
                    model=embedings_model,
                    contents=[
                        types.Part.from_bytes(
                            data=file.read(),
                            mime_type="application/pdf",
                        )
                    ]
                )
                embeddings = response.embeddings
                print(f"Generated embeddings for {file_name}")

            # Use LLM to explain the document
            explanation_response = client_model.models.generate_text(
                model=llm_model,
                prompt=f"Explain the content of the document: {file_name}",
                temperature=0.7,
                max_output_tokens=500
            )
            explanation = explanation_response.text
            print(f"Explanation for {file_name}:\n{explanation}\n")

# Run the function
process_pdfs(file_path)