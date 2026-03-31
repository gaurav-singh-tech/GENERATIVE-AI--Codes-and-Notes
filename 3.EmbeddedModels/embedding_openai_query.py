from langchain_openai import OpenAIEmbeddings #1. It imports the OpenAIEmbeddings class from the langchain_openai module to create embeddings using OpenAI's models.
from dotenv import load_dotenv #2. It imports the load_dotenv function from the dotenv module to load environment variables from a .env file.

load_dotenv() #3. It loads the environment variables from the .env file into the system's environment.

embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32) #4. It initializes the OpenAIEmbeddings class with the specified model "text-embedding-3-small" to create embeddings using that model.
#this model is capable of generating embeddings with 32 dimensions.. Dimensions refer to the size of the vector representation of the text data.
#Higher dimensional embeddings can capture more nuanced information about the text, but they also require more computational resources and cost.
#When you run this code, it will create an instance of OpenAIEmbeddings using the specified model for generating text embeddings.

result = embedding.embed_query("Delhi is the capital of India") #5. It calls the embed_query method on the embedding instance to generate an embedding for the input text "Delhi is the capital of India".

print(str(result)) #6. It prints the resulting embedding vector as a string representation to the console.
#When you run this entire code, it will output the embedding vector for the given text using the specified OpenAI embedding model.

#THIS CODE WILL NOT SHOW ANY OUTPUT, BECAUSE MY OPENAI_API_KEY IS EXPIRED.

# If the API key wasn't expired and you had quota, you'd get an output like:
# Code
# [-0.0234375, 0.03125, -0.0078125, ...] # embedding vector
# It's a list of floats representing the embedding vector for "Delhi is the capital of India".
# But since you got a RESOURCE_EXHAUSTED error, it's likely a quota issue 😊.
# Want to double-check your API key and quota?