def calculadora():
    while True:
        print("Calculadora simples")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Sair")

        operacao = int(input("Selecione uma opção: "))

        if operacao == 5:
            print("Obrigada por utilizar a calculadora")
            break

        if operacao not in range(1, 5):
            print("Opção invalida. Tente novamente.")
            continue

        numero_1 = int(input("Primeiro numero: "))
        numero_2 = int(input("Segundo numero: "))

        if operacao == 1:
            soma = numero_1 + numero_2
            print("O resultado da soma é: ", soma)
        elif operacao == 2:
            sub = numero_1 - numero_2
            print("O resultado da subtracao é: ", sub)
        elif operacao == 3:
            mult = numero_1 * numero_2
            print("O resultado da multiplicação é: ", mult)
        elif operacao == 4:
            if numero_2 > 0:
                divisao = numero_1 / numero_2
            else:
                print("Divisões por zero não são possíveis. Tente novamente.")
                continue
            print("O resultado da divisão é: ", divisao)

calculadora()