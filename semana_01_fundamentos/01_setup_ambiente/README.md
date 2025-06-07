# 🧪 Dia 1 – Setup e Hello World com Flask + OpenAI

## 🎯 Objetivo
- Configurar o ambiente Python com `venv`
- Criar um `requirements.txt`
- Subir uma API Flask com uma rota `/hello` que retorna um JSON
- Instalar a biblioteca da OpenAI e configurar a chave da API (usando `.env`)
- Fazer uma rota `/gpt` que recebe um prompt e retorna a resposta do ChatGPT

---

## ⚙️ Passos executados

1. Criação do ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
