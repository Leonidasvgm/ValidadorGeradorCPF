import random


cpf_9digitos = ''
for i in range(9):
        cpf_9digitos += str(random.randint(0,9))

contador_regressivo1 = 10
resultado_digito1 = 0

for digito in cpf_9digitos:
    resultado_digito1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1
    digito = (resultado_digito1 * 10) % 11

digito_1 = digito if digito <= 9 else 0
digito_1 = str(digito_1)

cpf_10digitos = cpf_9digitos + digito_1
contador_regressivo2 = 11
resultado_digito2 = 0

for digito in cpf_10digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
    digito =(resultado_digito2 * 10) % 11

digito_2 = digito if digito <= 9 else 0
digito_2 = str(digito_2)

novo_cpf = f'{cpf_9digitos}{digito_1}{digito_2}'

print(f'O novo CPF gerado é {novo_cpf}')
