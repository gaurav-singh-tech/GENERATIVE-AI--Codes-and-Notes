from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 1. Load API key from .env
load_dotenv()

# 2. Initialize the Gemini Chat Model
# We use 'gemini-2.5-flash' based on your available model list.
# It is faster and cheaper (free tier) than GPT-4o while being very capable.
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=2, #temperature controls randomness of output, in simplest terms it means how creative the model should be, higher value means more creative responses
    #its value lies between 0 to 1
    max_completions_tokens=10 #number of tokens(cwn say words) to generate for each input
)

# 3. Invoke the model
# (Only call invoke once to save time and quota)
response = model.invoke("Write a 5 line poem on cricket & football?")

# 4. Print the result
# .content extracts just the string answer, ignoring metadata
print(response.content)