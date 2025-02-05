from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
import authorization
import os


os.environ["OPENAI_API_KEY"] = authorization.apikey


apikey = authorization.apikey

# Create an instance of the chat OpenAI class

model = OpenAI()

set_llm_cache(SQLiteCache(database_path="openai_cache.db"))

prompt = "me diga quem foi albert einstein"

response1 = model.invoke(prompt)
print(f'chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'chamada 2: {response2}')