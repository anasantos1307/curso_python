"""
listas: uma coleção python

Características:
- Representação: [item1, item2, ...., itremN]
- São mutáveis
- Podem ser heterogêneas
- Listas são iteráveis
- Listas não são arrays
- São indexadas em zero (assim como as strings);
"""

# minha_lista = [1, 2, 3, 4, 5]
# print(minha_lista)
# print(type(minha_lista))
#
# lista_2 = [10, 3.14, "oi", True, [1, 2, 3]]
# print(lista_2)
#
# matriz = [[1, 2, 3],
#           [4, 5, 6]]
# for i in lista_2:
#     print(i)

# numeros = list(range(51))
# print(numeros)

#Índice
# print(numeros[0])
# print(numeros[13])
# print(numeros[48])
# print(numeros[-1])

#Slicing
# print(numeros[0:12])
# print(numeros[12:40])
# print(numeros[:26])
# print(numeros[28:])
# print(numeros[::5])
# print(numeros[::-5])

#funções
#listas no geral
# print(len(numeros))

#Listas numéricas
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))

frutas = ["laranja", "maçã", "abacaxi", "melão", "uva"]
print("Nossa lista tem", len(frutas))

#Adicionando itens na lista
frutas.append("banana")
print(frutas)

# for i in range(3):
#     frutas = input("Fruta: ")
#     frutas.append(frutas)

frutas.extend(["morango", "melância", "limão"])
print(frutas)

frutas.insert(1, "maracujá")
print(frutas)

#Removendo itens da lista
ultimo_fruta = frutas.pop()
print(ultimo_fruta)
print(frutas)

frutas.remove("banana")
print(frutas)

#Editar

frutas[0] = "pitaya"

#encontrando elementos na lista

print("Melância está na posição", frutas.index("melância"))
frutas[frutas.index("melância")] = "carambola"
print(frutas)

#Contando quantas vezes um dado elemento aparece na lista
print(f"Carambola aparece {frutas.count("carambola")} na nossa lista")

#Método ordenar uma lista:
frutas.sort()
print(frutas)