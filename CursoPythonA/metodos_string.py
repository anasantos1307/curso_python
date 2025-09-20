# Strings

# texto = "Aula de PrOGraMaçãO"
#
# print(texto.upper())
# print(texto.lower())
# print(texto.title())
# print(texto.capitalize())
# print(texto.replace("de", "com"))

# #exemplo 1
# nome = input("Nome: ")
# ultimo_nome = input("Último nome: ")
#
# email = nome.lower() + "." + ultimo_nome.lower() + "@senai.com"
# print(email)
#
# #exemplo 2
# nome = input("Nome e último nome: ")
# email = nome.lower().replace(" ", ".") + "@senai.com"
# print(email)

#Validação

import string

print("Todas as letras", string.ascii_letters)
print("Todos os dígitos", string.digits)
print("Todas as pontuações", string.punctuation)
print()
print("João".isalpha())
print("199989484".isdigit())
print("LED2838".isalnum())

nome_completo = "Ana Martins"
print(nome_completo.split())

print("Quantos char tem a palavra pneumonia?", len("pneumonia"))
print()
print()

"""
String como iteráveis:
-O que é iterável: é tudo valor o qual eu posso 'percorrer'
"""

texto = "Programação em Python"

print("O que está na posição zero da variável texto:", texto[0])

print(texto[0])
print(texto[4])
print(texto[2])
print()

print(texto[0:6])
print(texto[6:12])
print(texto[2:7])



