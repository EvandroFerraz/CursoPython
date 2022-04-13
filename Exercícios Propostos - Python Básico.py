"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é 
par ou ímpar. Informe caso o usuário não digite um número inteiro.

numero_inteiro = input("Digite um número inteiro: ")
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    
    if numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} é par.")
    else:
        print(f"{numero_inteiro} é ímpar.")
else:
    print("O valor digitado não é um número inteiro.")

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a 
saudação apropriada: Bom Dia das 00 às 11, Boa Tarde das 12 às 18 e Boa Noite das 19 às 23.

hora = input("Digite um horário entre 0 e 23:")
hora = int(hora)
if hora < 0 or hora > 23:
    print("Horário deve estar entre 0 e 23.")
else:
    if hora <= 11:
        print("Bom Dia")
    elif hora <= 17:
        print("Boa Tarde")
    else:
        print("Boa Noite")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome possuir 4 letras ou menos, 
escreva "Seu nome é curto". Se possuir entre 5 e 6 letras, escreva "Seu nome é médio". 
Se possuir mais do que 6 letras, escreva "Seu nome é grande".
"""
nome = input("Digite seu nome:")
if len(nome) <= 4:
    print("Seu nome é curto.")
elif len(nome) <= 6:
    print("Seu nome é médio.")
else:
    print("Seu nome é grande.")

