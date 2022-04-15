"""
#1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.

def saudacao(saudacao, nome):
    print(f"{saudacao} {nome}")

saudacao("Olá","Pessoa X")
saudacao("Hello","Person X")
"""

"""
#2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

def soma(n1, n2, n3):
    print(n1 + n2 + n3)
    
soma(10,11,12)
soma(7,3,2)
"""

"""
#3- Crie uma função que receba 2 núemros. O primeiro é um valor e o segundo um percentual (ex. 10%). 
#Retorne o valor do primeiro número somado à ele mesmo acrescido do aumento de percentual.

def aumento_percentual(numero,percentual):
    return numero + (numero * (percentual / 100))

print(aumento_percentual(10,23))
print(aumento_percentual(200,42))
"""

"""
#4- Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz. Se for divisível por 5, retorna buzz.
#Se o parâmetro da função for divisível por 5 e também por 3, retorne fizzbuzz, caso contrário, retorne o número enviado.

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n

print(fb(15))
"""
    

