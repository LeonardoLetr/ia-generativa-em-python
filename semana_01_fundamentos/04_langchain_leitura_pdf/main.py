from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Carrega o conteúdo do PDF
loader = PyPDFLoader("exemplo.pdf")
documentos  = loader.load()

llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")

template = PromptTemplate.from_template("Use o contexto abaixo para responder a pergunta.\n\n{context}\n\nPergunta: {input}")

chain = create_stuff_documents_chain(llm, template)

resposta = chain.invoke({
    "input": "Qual é a capital do Brasil?",
    "context": documentos
})

print(resposta)