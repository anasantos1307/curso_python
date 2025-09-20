

"""
Operadores Matemáticos:
+ Soma
- Subtração
* Multiplicação
/ Divisão
// Divisão inteira
% Módulo (resto da divisão)
** Potenciação

Regra de sinais:
+ com + = +
+ com - = -
- com + = -
- com - = +

Prioridades:
Ordem de execução em equações:
**
/ e *
+ e -
"""

#Soma
print(10 + 10)
print(10 + -10)
print(-10 + -10)
print()

#Subtração
print(10 - 10)
print(10 - (-10))
print(-10 - 10)
print(-10 - (-10))
print()

#Multiplicação
print(10 * 2)
print(10 * -2)
print(-10 * -2)
print(10 * 2 + 5)
print(10 * (2 + 5))
print()

#Divisão
print(10 / 2)
print(10 / -2)
print(-10 / -2)
print(10 / 2 + 5)
print(10 / (2 + 5))
print()

#Potenciação
print(10 ** 2)
print(10 ** -2)
print(144 ** .5)
print(10 ** 2 + 5)
print(10 ** (2 + 5))
print()

#Divisão inteira
print(10 / 3)
print(10 // 3)
print(10 // 6)
print(10 // 6 + 4)
print()

#Mod (resto da divisão)
print(10 % 3)
print(10 % 6)

# area = float(input("Digite a área que deseja pintar: "))
# rendimento = 15
#
# litros_necessarios = area / rendimento
# quantidade_latas_18 = litros_necessarios // 18
# quantidade_latas_3_6 = litros_necessarios % 18 // 3.6
#
# print()
# print(f"Área: {area} m²")
# print(f"Quantidade de latas de 18L: {quantidade_latas_18}")
# print(f"Quantidade de latas de 3.6L: {quantidade_latas_3_6}")

area = float(input("Área do terreno (em m²): "))
valor_metro = float(input("Valor por m²: R$"))

valor_terreno = area * valor_metro

print(f"Valor do terreno é: R$ {valor_terreno:,.2f}")
