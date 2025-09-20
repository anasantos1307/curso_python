"""
Condicionais em Python:

- if (se)
- else (senão)
- elif (senão se)
"""

# IF
"""
if condição:
    o que o if faz
"""

# Exemplo Farol
# farol = "verde"
#
# if farol == "verde":
#     print("Siga!")

# IF - ELSE
"""
if condição:
    o que o if faz
else:
    o que o else faz
"""

# codigo_produto = "#123"
# quantidade_produto = 500
# preco_produto = 4.5
#
# if quantidade_produto < 1000:
#     print("Quantidade abaixo do mínimo!")
#     print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}.")
# else:
#     print("Quantidade ok!")

# IF - ELIF - ELSE
"""
if condição:
    o que o if faz
elif condição 2:
    o que a condição 2 faz
...
else:
    o que o else faz
"""

# codigo_produto = input("Código do produto: ")
# quantidade_produto = int(input("Quantidade do produto: "))
# preco_produto = 4.5
#
# if codigo_produto == "#123":
#     if 1000 > quantidade_produto >= 0:
#         print("Quantidade abaixo do mínimo!")
#         print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}.")
#     elif 1000 <= quantidade_produto <= 2500:
#         print("Quantidade ok!")
#     elif 2500 < quantidade_produto < 5000:
#         print("Quantidade acima do máximo!")
#         print(f"Vender {quantidade_produto - 2500} unidades de {codigo_produto}.")
#     else:
#         print("Quantidade Inválida!")
#
# elif codigo_produto == "#344":
#     if 700 > quantidade_produto >= 0:
#         print("Quantidade abaixo do mínimo!")
#         print(f"Comprar {700 - quantidade_produto} unidades de {codigo_produto}.")
#     elif 700 <= quantidade_produto <= 1500:
#         print("Quantidade ok!")
#     elif 1500 < quantidade_produto < 3500:
#         print("Quantidade acima do máximo!")
#         print(f"Vender {quantidade_produto - 1500} unidades de {codigo_produto}.")
#     else:
#         print("Quantidade Inválida!")
# else:
#     print("Código de produto inválido")
# print()

# Exemplo Farol

# farol = "verde"
# if farol == "verde": print("Siga!")
# elif farol == "amarelo": print("Reduza!")
# elif farol == "vermelho": print("Pare!")
# else: print("Observe o guarda de trânsito.")

# Operações ternárias

media = 10

status = "Aprovado" if media >= 5 else "Reprovado"
print(f"Média: {media}")
print(f"Status: {status}")

# Match Case

dia_semana = int(input("Digite o número do dia da semana, por exemplo 1 - Domingo: "))

match dia_semana:
    case 1: print("Domingo")
    case 2: print("Segunda-feira")
    case 3: print("Terça-feira")
    case 4: print("Quarta-feira")
    case 5: print("Quinta-feira")
    case 6: print("Sexta-feira")
    case 7: print("Sábado")
    case _: print("Dia inválido")