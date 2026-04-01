from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, parser
from langchain import LLMChain, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
    template= 'Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model=ChatOpenAI(model='gpt-3.5-turbo', temperature=0.9)

parser= StrOutputParser()

chain= prompt | model | parser

results=chain.invoke({'topic': 'space exploration'})

print(results)