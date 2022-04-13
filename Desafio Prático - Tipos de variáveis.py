"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings
"""

nome = 'Evandro'
idade = 27
altura = 1.84
peso = 66
imc = peso / altura ** 2 
ano_atual = 2022
ano_nascimento = ano_atual - idade

print(f'{nome} possui {idade} anos, {altura} de altura, {peso} de peso, {imc:.2f} de imc e nasceu em {ano_nascimento}.')


