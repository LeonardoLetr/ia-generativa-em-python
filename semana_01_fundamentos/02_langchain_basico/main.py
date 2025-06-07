from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

print("Chave carregada:", os.getenv("OPENAI_API_KEY"))

load_dotenv()

# Define o modelo da OpenAI
llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")

# Define p prompt template
template = PromptTemplate.from_template("Responda com uma frase curta: {pergunta}")

# Cria a cadeia de LLM
chain = template | llm

# Executa a cadeia com uma pergunta simples
resposta = chain.invoke({"pergunta": "Qual é a capital do Brasil?"})
print(resposta.content)