from langchain_openai import OpenAI #It helps to use OpenAI models
from dotenv import load_dotenv #It helps to load the .env file where we store our API keys

load_dotenv() #Load the .env file

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.7) #Initialize the OpenAI LLM with the desired model and temperature. Temperature controls the randomness of the output.

result= llm.invoke("What is the capital city of India?") #Invoke the LLM with a prompt to get the response

print(result) #Print the result