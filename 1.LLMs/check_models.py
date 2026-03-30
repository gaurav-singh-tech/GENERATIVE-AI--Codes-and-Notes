import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the library with your key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- Available Models for your API Key ---")
for m in genai.list_models():
    # We only want models that generate content (chat models)
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)