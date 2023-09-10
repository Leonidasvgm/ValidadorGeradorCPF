while True:

    cpf = input('Digite um CPF: ')
    cpf_9digitos = cpf[:9]
    contador_regressivo1 = 10
    resultado_digito1 = 0
    try:
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

        if cpf == novo_cpf: 
            print(f'O CPF {cpf} é válido')
        else:
            print(f'O CPF {cpf} é inválido')    

    except ValueError: 
        print('Digite seu CPF novamente e sem os pontos.')
        

    




