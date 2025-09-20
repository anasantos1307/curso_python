while True:
    atleta = input("Digite o nome do atleta: ")
    if atleta == "":
        print("Programa Encerrado")
        break

    salto1 = float(input("Digite a distância do primeiro salto: "))
    salto2 = float(input("Digite a distância do segundo salto: "))
    salto3 = float(input("Digite a distância do terceiro salto: "))
    salto4 = float(input("Digite a distância do quarto salto: "))
    salto5 = float(input("Digite a distância do quinto salto: "))

    saltos = []
    saltos.insert(0, salto1)
    saltos.insert(1, salto2)
    saltos.insert(2, salto3)
    saltos.insert(3, salto4)
    saltos.insert(4, salto5)

    resultado = (salto1 + salto2 + salto3 + salto4 + salto5) / 5
    print()
    print(f"Atleta: {atleta}")
    print()
    print(f"Primeiro Salto: {saltos[0]} m.")
    print(f"Segundo Salto: {saltos[1]} m.")
    print(f"Terceiro Salto: {saltos[2]} m.")
    print(f"Quarto Salto: {saltos[3]} m.")
    print(f"Quinto Salto: {saltos[4]} m.")
    print()
    print("--- Resultado Final ---")
    print(f"Atleta: {atleta}")
    print(f"Saltos: {saltos}")
    print(f"Média dos saltos: {resultado} m.")
