import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import authorization

api_key = authorization.apikey
os.environ['OPENAI_API_KEY'] = api_key

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt_template = PromptTemplate.from_template(
    'me fale sobre o carro {carro}',
)

runnable_sequence = prompt_template | model #| StrOutputParser()

result = runnable_sequence.invoke({'carro': "Ferrari que foi capa do forza 4"})

print(result)