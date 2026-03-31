from langchain_huggingface import HuggingFaceEmbeddings #1. It imports the HuggingFaceEmbeddings class from the langchain_huggingface module to create embeddings using Hugging Face models.
from langchain_huggingface import HuggingFacePipeline #2. It imports the HuggingFacePipeline class from the langchain_huggingface module to create a pipeline for Hugging Face models.

embedding=HuggingFaceEmbeddings( #3. It initializes the HuggingFaceEmbeddings class with a specific model and pipeline configuration to create embeddings.
    model_name="sentence-transformers/all-MiniLM-L6-v2") #It specifies the model name from Hugging Face to be used for generating embeddings.

text="DElhi is the capital of India"
    
vector=embedding.embed_query(text)

print(str(vector)) #4. It prints the resulting embedding vector as a string representation to the console.
#When you run this entire code, it will output the embedding vector for the given text using the specified Hugging Face embedding model.
