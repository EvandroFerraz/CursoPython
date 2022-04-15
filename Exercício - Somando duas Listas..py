"""
Considerando duas listas de inteiros, some as posições retornando uma nova 
lista:    

Exemplo:
    lista_a = [1,2,3,4,5,6,7]
    lista_b = [1,2,3,4]
Resultado: 
    lista_soma = [2,4,6,8]
"""
from itertools import zip_longest

lista_a = [10, 11, 23, 47, 58, 61, 87, 95]
lista_b = [12 , 2, 3, 6, 50, 60, 70]

lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)