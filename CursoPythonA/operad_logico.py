"""
Operadores Lógicos:
and - E
or - Ou
not - Não

Prioridade:
1ª()
2ª Not
3ª And
4ª Or
"""

# AND

print(False and False)
print(False and True)
print(True and False)
print(True and True)
print()

# Exemplo login
#
# user = input("Username: ")
# password = input("Password: ")
# acesso = user == "admin" and password == "senha123"
# print()
# print(f"Usuário Reconhecido: {user == "admin"}")
# print(f"Senha Reconhecida: {password == "senha123"}")
# print(f"Acesso Liberado: {acesso}")

# OR

print(False or False)
print(False or True)
print(True or False)
print(True or True)
print()

#Exemplo critérios aluno

# media_final = 10
# frequencia = .5
#
# reprova_aluno = media_final < 5 or frequencia < .75
# print()
# print(f"Média final: {media_final:.2f}")
# print(f"Frequência: {frequencia:.2%}")
# print(f"Média final: {reprova_aluno}")

# NOT

print(not False)
print(not True)
print()

print(not 10 > 2 and 10 % 5 == 0)
print(10 > 2 and 10 % 5 == 0)

#Exemplo

C = False
B = True
A = True

situacao_1 = not A and not B and not C
situacao_2 = A and not B and not C
situacao_3 = A and B and not C

bomba = situacao_1 or situacao_2 or situacao_3
print(f"Bomba Ligada: {bomba}")

