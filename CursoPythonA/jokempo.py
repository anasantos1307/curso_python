import random

while True:
    print("Escolhas: 1- Papel | 2- Pedra | 3- Tesoura")
    usuario = (input("Qual sua escolha? : "))
    maquina = random.choice("1 2 3".split())
    print(f"A máquina escolheu a opção: {maquina}")

    if maquina == usuario:
        print("Empate!")
    elif usuario == "1" and maquina == "2":
        print("Você ganhou!")
    elif usuario == "2" and maquina == "3":
        print("Você ganhou!")
    elif usuario == "3" and maquina == "1":
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    escolha = input("Deseja continuar jogando? ")
    if escolha == "sim":
        continue
    else:
        break