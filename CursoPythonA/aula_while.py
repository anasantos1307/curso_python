"""
While: enquanto uma condição for True todo o bloco se repetirá

while condição:
    bloco do while
"""

# i = 0
#
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Fim das repetições;")

# n = int(input("N: "))
#
# while n <= 50:
#     if n == 50: print(f"{n} é igual.")
#     else: print(f"{n} é menor que 50.")
#     n = int(input("N: "))
# print(f"{n} é maior que 50.")

# Exemplo Login

# user = input("Usuário: ")
# if user == "admin":
#     password = input("Senha: ")
#
#     while password != "senha123":
#         print("Senha Incorreta!")
#         password = input("Senha: ")
#
#     else: print("Bem-Vindo!")
#
# else: print("Usuário inválido!")

"""
continue: Retorna até a verificação de condição do while
break: quebra o looping, ou seja, sai do while
"""
import time

tentativas = 0

while True:
    if tentativas < 3:
        user = input("Usuário: ")
        if user == "admin":
            password = input("Senha: ")
            if password == "senha123":
                print("Bem-Vindo!")
                break
            else:
                print("Senha Incorreta!")
                tentativas += 1
                continue
    else:
        print("Tentativas excedidas!")
        for i in range(10, 0, -1):
            print("/r", end=f"espere: {i} segundos.")
            time.sleep(1)
        print()
        tentativas = 0
        continue