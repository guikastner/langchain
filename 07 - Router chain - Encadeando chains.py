import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import authorization

api_key = authorization.apikey
os.environ['OPENAI_API_KEY'] = api_key

model = ChatOpenAI(model="gpt-3.5-turbo")

classification_chain = (
    PromptTemplate.from_template(
        '''	
        Classifique a pergunta abaixo em um dos seguintes setores: 
        - Financeiro
        - Suporte Técnico
        - Outras Informações

        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        '''	
        Você é um especialista do setor financeiro.
        Sempre responda as perguntas com "Bem vindo ao setor financeiro".
        Responda a pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        '''	
        Você é um especialista do setor de suporte técnico.
        Sempre responda as perguntas com "Bem vindo ao setor suporte técnico".
        Responda a pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)   

other_info_chain = (
    PromptTemplate.from_template(
        '''	
        Sempre responda as perguntas com "Bem vindo ao setor de informações".
        Responda a pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser() 
)

def route (classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_chain
    elif 'suporte tecnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain
    
pergunta = input("Digite uma pergunta: ")

classification = classification_chain.invoke(
    {'pergunta': pergunta})


print(classification)

chain = route(classification=classification)

result = chain.invoke(pergunta)

print(result)