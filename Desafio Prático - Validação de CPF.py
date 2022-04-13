#Crie um algoritmo que receba um CPF como entrada e retorne se o CPF é válido ou não.

cpf = input("Digite um CPF, considerando apenas números: ")
aux_cpf = cpf[:-2]
i_reverso = 10
total = 0

for i in range(19):
    if i > 8:
        i -= 9
    
    total += int(aux_cpf[i]) * i_reverso
    
    i_reverso-= 1
    if i_reverso < 2:
        i_reverso = 11
        d = 11 - (total % 11)
        
        if d > 9:
            d = 0
        total = 0
        aux_cpf += str(d)

if cpf == aux_cpf:
    print("CPF Válido.")
else:
    print("CPF Inválido.")       