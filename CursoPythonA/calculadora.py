num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = int(input("Digite: 1 para Somar | 2 para Subtrair | 3 para Multiplicar | 4 para Dividir | 5 para Exponenciar: "))

match operacao:
    case 1: print(f"Resultado: {num1 + num2}")
    case 2: print(f"Resultado: {num1 - num2}")
    case 3: print(f"Resultado: {num1 * num2}")
    case 4: print(f"Resultado: {num1 / num2}")
    case 5: print(f"Resultado: {num1 ** num2}")
    case _: print("Erro, tente novamente com uma opção válida")
