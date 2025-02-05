from langchain_openai import OpenAI
import authorization
import os


os.environ["OPENAI_API_KEY"] = authorization.apikey


apikey = authorization.apikey
# Create an instance of the OpenAI class


llm = OpenAI()

response = llm.invoke(
    input="Quem foi allan turing?",
    temperature=1,
    max_tokens=500,
)

print(response)