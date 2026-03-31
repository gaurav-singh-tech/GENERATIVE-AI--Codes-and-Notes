from langchain_huggingface import HuggingFaceEmbeddings #1. It imports the HuggingFaceEmbeddings class from the langchain_huggingface module to create embeddings using Hugging Face models.
from dotenv import load_dotenv #2. It imports the load_dotenv function from the dotenv module to load environment variables from a .env file.

from sklearn.metrics.pairwise import cosine_similarity #1. It imports the cosine_similarity function from the sklearn.metrics.pairwise module to compute cosine similarity between vectors.
import numpy as np 
load_dotenv()

embedding=HuggingFaceEmbeddings( #3. It initializes the HuggingFaceEmbeddings class with a specific model and pipeline configuration to create embeddings.
    model_name="sentence-transformers/all-MiniLM-L6-v2") #It specifies the model name from Hugging Face to be used for generating embeddings.

documents=[
    "Virat Kohli is a great cricketer",
    "Sachin Tendulkar is a legendary batsman",
    "The capital of India is New Delhi",
    "The Eiffel Tower is located in Paris",
    "Python is a popular programming language"      
] 

user_query="Who is a legendary batsman?"

documents_embeddings=embedding.embed_documents(documents) #2. It calls the embed_documents method on the embedding instance to generate embeddings for the list of documents.
query_embedding=embedding.embed_query(user_query) #3. It calls the embed_query method on the embedding instance to generate an embedding for the user query.

similarity_score=cosine_similarity([query_embedding], documents_embeddings) #4. It computes the cosine similarity between the query embedding and each of the document embeddings using the cosine_similarity function.  
#Remember both query list and document embeddings should be in 2D array format.

print(list(enumerate(similarity_score[0]))) #5. It prints the similarity scores as a list of tuples, where each tuple contains the index of the document and its corresponding similarity score with the user query.
#When you run this entire code, it will output the similarity scores between the user query
#enumerate() function is used to get index along with similarity score for each document.

sorted_scores = sorted(list(enumerate(similarity_score[0])), key=lambda x:x[1], reverse=True) #lambda function is used to sort based on similarity score which is at index 1 of each tuple.
index = sorted_scores[0][0]
print("Most similar document:", documents[index])
print("Similarity score is :" , sorted_scores[0][1]) #6. It prints the most similar document along with its similarity score to the console.