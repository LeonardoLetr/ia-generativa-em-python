from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Carrega o conteudo do arquivo de texto
with open("texto_exemplo.txt", "r", encoding="utf-8") as file:
    conteudo = file.read()

# Cria um documento com o conteudo lido
document = Document(page_content=conteudo)

# Inicializa o modelo da OpenAI
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Define o prompt que será usado no contexto
template = PromptTemplate.from_template(
    "Use o contexto abaixo para responder a pergunta.\n\n{context}\n\nPergunta: {input}"
)

# Cria a chain com LangChain (modo 'stuff')
chain = create_stuff_documents_chain(llm, template)

# Faz uma pergunta com base no conteudo 
resposta = chain.invoke(
    {"input": "Qual é o tema principal do texto?", "context": [document]}
)

print(resposta)