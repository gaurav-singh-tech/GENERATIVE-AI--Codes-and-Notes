import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Initialize as a pure LLM (not Chat)
# We add the 'v1beta' version to ensure it recognizes the 2.5 models
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"), #os module is used to access environment variables
    temperature=0.7,
    version="v1beta" 
)

# 3. Execution
# For LLMs, we can use simple string input/output
try:
    # Use .invoke() or just call the llm as a function
    result = llm.invoke("The capital city of India is ")
    print("--- Completion Result ---")
    print(result.strip())
except Exception as e:
    print(f"Error: {e}")