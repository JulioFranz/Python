def conversorhora():
    print('Conversor de tempo')
    escolha_valida = False

    while not escolha_valida:
        print('Escolha a opção desejada!')
        print('1- Segundos para minutos')
        print('2- Minuto para segundos')
        print('3- Minutos em horas')

        # Obter a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3): ")

        # Verificar se a escolha é válida
        if escolha in ['1', '2', '3']:
            escolha = int(escolha)
            escolha_valida = True
        else:
            print("Escolha inválida! Digite um número válido.\n")

    n1=float(input('Informe o numero a ser convertido: '))

    if escolha==1:
        minutos=int(n1//60)
        seg=int(n1%60)
        print(minutos,'minutos e ',seg ,'segundos')

    elif escolha==2:
        resultado=int(n1*60)
        print(resultado, 'Segundos')

    elif escolha==3:
        horas=int(n1//60)
        minutos=int(n1%60)
        print(horas, 'Horas e', minutos,'Minutos')



conversorhora()