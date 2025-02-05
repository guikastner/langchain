from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import authorization
import os


os.environ["OPENAI_API_KEY"] = authorization.apikey
apikey = authorization.apikey

model = ChatOpenAI(model="gpt-3.5-turbo")

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="Você deve responder com base em dados do IBGE Brasil"),
        HumanMessagePromptTemplate.from_template('por favor me fale sobre a a região {regiao} em um parágrafo'),
        AIMessage(content="Claro, vou começar analisando e informações sobre os dados disponíveis"),
        HumanMessage(content='certifique-se de usar dados demográficos e econômicos'),
        AIMessage(content="Entendi, aqui estão os dados:"),
    ]
)

prompt = chat_template.format_messages(regiao="Sudeste")

response = model.invoke(prompt)

print(response.content)