nome = input("Insira seu nome: ").title()
idade = int(input("Insira sua idade: "))
cidade = input("Informe o nome da sua cidade: ").title()
estado = input("Informe o seu estado: ")

print()
print("---Cadastro realizado com sucesso!---")
print(f"Olá {nome}, você tem {idade} anos! Vive em {cidade}, cidade do estado de {estado}!")
