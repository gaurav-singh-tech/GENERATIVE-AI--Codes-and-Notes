from langchain_openai import OpenAIEmbeddings #1. It imports the OpenAIEmbeddings class from the langchain_openai module to create embeddings using OpenAI's models.
from dotenv import load_dotenv #2. It imports the load_dotenv function from the dotenv module to load environment variables from a .env file.

load_dotenv() #3. It loads the environment variables from the .env file into the system's environment.

embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32) #4. It initializes the OpenAIEmbeddings class with the specified model "text-embedding-3-small" to create embeddings using that model.
#this model is capable of generating embeddings with 32 dimensions.. Dimensions refer to the size of the vector representation of the text data.
#Higher dimensional embeddings can capture more nuanced information about the text, but they also require more computational resources and cost.
#When you run this code, it will create an instance of OpenAIEmbeddings using the specified model for generating text embeddings.

docs=["Delhi is the capital of India",
      "The capital of France is Paris",
      "Berlin is the capital of Germany"

]
result = embedding.embed_documents(docs) #5. It calls the embed_query method on the embedding instance to generate an embedding for the input text "Delhi is the capital of India".

print(str(result)) #6. It prints the resulting all embedding vector as a string representation to the console.