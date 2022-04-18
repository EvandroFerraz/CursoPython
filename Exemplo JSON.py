#Documentação: https://docs.python.org/3/library/json.html

import json

clientes_dicionario = {
    1: {
        'nome': 'Luiz Otávio',
        'sobrenome': 'Miranda',
        'idade': 25,
        'altura': 1.80,
        'peso': 80.53,
    },
    2: {
        'nome': 'Maria',
        'sobrenome': 'Oliveira',
        'idade': 52,
        'altura': 1.67,
        'peso': 57,
    },
    3: {
        'nome': 'Pedro',
        'sobrenome': 'Faria',
        'idade': 32,
        'altura': 1.95,
        'peso': 113,
    },
}

clientes_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""

# Converte um dicionário em JSON, útil para salvar informações de qualquer tipo
dados = json.dumps(clientes_dicionario, indent=4)

# Converte JSON em um dicionário, útil para carregar informações de qualquer tipo
dados = json.loads(clientes_json)
print(dados)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as f:
    json.dump(clientes_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as f:
    data = json.load(f)

print(data)


