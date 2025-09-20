saldo = 1000
while True:
    print("Opções disponíveis:")
    print("1 - Depósito | 2 - Saque | 3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        deposito = float(input("Informe o valor do depósito: R$"))
        if deposito < 0:
            print("Valor inválido!")
            continue
        else:
            saldo += deposito
            print(f"Seu saldo atual agora é de: R${saldo}")
            continue
    elif opcao == 2:
        saque = float(input("Informe o valor do saque: R$"))
        if saque > saldo:
            print("Saldo insuficiente!")
            continue
        else:
            saldo -= saque
            print(f"Seu saldo atual agora é de: R${saldo}")
            continue
    elif opcao == 3:
        print("Volte sempre!")
        break
    else:
        print("Opção inválida, tente novamente!")
        print()
        continue



