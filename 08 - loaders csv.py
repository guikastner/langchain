import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import authorization
from langchain_community.document_loaders import TextLoader, CSVLoader

api_key = authorization.apikey
os.environ['OPENAI_API_KEY'] = api_key

model = ChatOpenAI(model="gpt-3.5-turbo")

loader = CSVLoader('base_conhecimento.csv')
documents = loader.load()

#print(documents[0].page_content)

prompt_base_conhecimento = PromptTemplate(
    input_varialers=['contexto', 'pergunta'],
    template = '''
    Use o serguinte contexto para responder a pergunta:
    Responda apenas com base no contexto fornecido.
    Não utilize nada mais externo ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}
    '''
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke({
    'contexto': '\n'.join(doc.page_content for doc in documents),
    'pergunta': 'Qual óleo devo usar?'
})

print(response)