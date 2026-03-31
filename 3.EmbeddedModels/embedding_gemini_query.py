from langchain_google_genai import GoogleGenerativeAIEmbeddings #1. It imports the GoogleGenerativeAIEmbeddings class from the langchain_google_genai module to create embeddings using Google's models.
from dotenv import load_dotenv #2. It imports the load_dotenv function from the dotenv module to load environment variables from a .env file.

load_dotenv() #3. It loads the environment variables from the .env file into the system's environment.

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001") #4. It initializes the GoogleGenerativeAIEmbeddings class with the specified model "models/embedding-001" to create embeddings using that model.
#this model is capable of generating embeddings.

result = embedding.embed_query("Delhi is the capital of India") #5. It calls the embed_query method on the embedding instance to generate an embedding for the input text "Delhi is the capital of India".

print(str(result)) #6. It prints the resulting embedding vector as a string representation to the console.
#When you run this entire code, it will output the embedding vector for the given text using the specified Google embedding model.


#THIS CODE WILL NOT SHOW ANY OUTPUT, BECAUSE MY GEMINI KEY IS EXPIRED.

# If the API key wasn't expired and you had quota, you'd get an output like:
# Code
# [-0.0234375, 0.03125, -0.0078125, ...] # embedding vector
# It's a list of floats representing the embedding vector for "Delhi is the capital of India".
# But since you got a RESOURCE_EXHAUSTED error, it's likely a quota issue 😊.
# Want to double-check your API key and quota?