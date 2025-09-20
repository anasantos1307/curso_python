"""
2 tipos de Loopings:

- for: Estruturas de repetição contadas;
- while: Estruturas de repetição condicionais;

"""
# numeros = [1, 2, 3, 4, 5]
# for i in numeros:
#     print("oi")
#
# numeros = [1, 2, 3, 4, 5]
# for _ in numeros:
#     nome = input("Nome: ")
#     print(f"Bem-Vindo(a) {nome}!")
#
# for letra in "Olá Mundo!":
#     print(letra.upper())

# range()
# 1ª forma: range(stop)

# sequencia = range(10)
# print(sequencia)
# print(*sequencia)
#
# for i in range(10):
#     print(i)
#
# for n in range(3):
#     nome = input("Nome: ")
#     n1 = float(input("N1: "))
#     n2 = float(input("N2: "))
#     media = (n1 + n2) / 2
#     print(f"{nome}, sua média é de: {media}")
#
# if media == 10:
#     print("A+")
# elif 10 > media >= 7:
#     print("B")
# elif 0 <= media < 7:
#     print("C")

# 2ª forma: range(start, stop)

# for i in range(5, 11):
#     print(f"O quadrado de {i} é {i ** 2}")
#
# idade = int(input("Idade: "))
#
# if idade in range(14, 25):
#     print("Pode fazer o CAI.")
# else:
#     print("Faça um técnico.")

# 3ª forma: range(start, stop, step)

# for n in range(0, 110, 10):
#     print(n)

# Exemplo
print()
n_carros = int(input("Quantos carros você vendeu no mês de Agosto: "))
total = float(0)

for venda in range(n_carros):
    valor_venda = float(input(f"Valor da {venda + 1}ª venda: R$ "))
    total += valor_venda

comissao = total * .07

print()
print(f"Você vendeu um total de: R$ {total:,.2f}")
print(f"A comissão foi de: R$ {comissao:,.2f}")
