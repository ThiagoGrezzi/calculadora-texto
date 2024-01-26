import datetime

opcao = "s"

while opcao != "n":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    calc = int(input("Escolha a operação:\n1 - soma\n2 - sub\n3 - mult\n4 - div\n5 - pot\n6 - Resto\n"))

    # Adicionando mensagem informativa sobre a operação
    if calc == 1:
        print("Realizando a operação de soma.")
    elif calc == 2:
        print("Realizando a operação de subtração.")
    elif calc == 3:
        print("Realizando a operação de multiplicação.")
    elif calc == 4:
        print("Realizando a operação de divisão.")
    elif calc == 5:
        print("Realizando a operação de potência.")
    elif calc == 6:
        print("Calculando o resto da divisão.")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")
        continue

    data = str(datetime.datetime.now())
    data_format = data.replace(':', '_')

    # Executando a operação escolhida
    if calc == 1:
        soma = n1 + n2
        print(n1 + n2)
    elif calc == 2:
        sub = n1 - n2
        print(n1 - n2)
    elif calc == 3:
        mult = n1 * n2
        print(n1 * n2)
    elif calc == 4:
        div = n1 / n2
        print(n1 / n2)
    elif calc == 5:
        pot = n1 ** n2
        print(n1 ** n2)
    elif calc == 6:
        if n1 < n2:
            mod = n2 % n1
            a = n2
            b = n1
            n1 = a
            n2 = b
            print(mod)
        else:
            mod = n1 % n2
            print(mod)

    print(data_format)

    # Salvando o resultado em um arquivo
    nameFile = "operacao_" + str(calc) + "_" + data_format + ".txt"
    file = open(nameFile, "a")
    file.write("O resultado da operação " + str(calc) + " com " + str(n1) + " e " + str(n2) + " é " + str(
        mod if calc == 6 else eval(str(n1) + chr(42 + calc) + str(n2))))
    file.close()

    opcao = input("Deseja usar a calculadora? s ou n ")


