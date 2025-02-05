from langchain_openai import OpenAI, ChatOpenAI
import authorization
import os


os.environ["OPENAI_API_KEY"] = authorization.apikey


apikey = authorization.apikey

# Create an instance of the chat OpenAI class


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=apikey,
    temperature=1,
    max_tokens=500,
)

messages = [
    {
        "role": "system",
        "content": "você é especializado em história da computação?"
    },
    {
        "role": "system",
        "content": "Quem foi allan turing?"
    }
]

Response = llm.invoke(messages)

print(Response.content)