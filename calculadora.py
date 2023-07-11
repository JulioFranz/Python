def calculadora_menu3():
    print("Bem-vindo à calculadora!")
    escolha_valida = False

    while not escolha_valida:
        print("Escolha uma operação matemática:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        # Obter a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4): ")

        # Verificar se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            escolha = int(escolha)
            escolha_valida = True
        else:
            print("Escolha inválida! Digite um número válido.\n")

    # Obter os números para a operação matemática
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Executar a operação matemática escolhida
    if escolha == 1:
        resultado = num1 + num2
        print("O resultado da soma é: ", round(resultado,2))
    elif escolha == 2:
        resultado = num1 - num2
        print("O resultado da subtração é: ", round(resultado,2))
    elif escolha == 3:
        resultado = num1 * num2
        print("O resultado da multiplicação é: ", round(resultado,2))
    elif escolha == 4:
        if num2 == 0:
            print("Erro: Divisão por zero!")
        else:
            resultado = num1 / num2
            print("O resultado da divisão é: ", round(resultado,2))

                        
calculadora_menu3()