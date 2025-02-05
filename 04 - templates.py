from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
from langchain.prompts import PromptTemplate
import authorization
import os


os.environ["OPENAI_API_KEY"] = authorization.apikey
apikey = authorization.apikey

model = ChatOpenAI(model="gpt-3.5-turbo")

template = '''
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template,
)

prompt = prompt_template.format(
    idioma1="português",
    idioma2="inglês",
    texto="O que é inteligência artificial?"
)

response = model.invoke(
    prompt
)

print(response.content)