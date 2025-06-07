import json
from datetime import datetime

def salvar_interacao(prompt, resposta, nome_arquivo='historico.json'):
    interacao = {
        'data': datetime.now().isoformat(),
        'prompt': prompt,
        'resposta': resposta
    }
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            interacoes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        interacoes = []
    
    interacoes.append(interacao)

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(interacoes, arquivo, indent=2, ensure_ascii=False)