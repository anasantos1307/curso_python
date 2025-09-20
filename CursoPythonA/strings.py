from math import pi

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.5

print(codigo_produto, quantidade_produto, preco_produto)
#print("Código:", codigo_produto, "Quantidade:", quantidade_produto, "Preço: R$", preco_produto)

nome = "Ana"
sobrenome = "Martins"

nome_completo = nome + " " + sobrenome
print(nome_completo)

print("Código: " + codigo_produto + ", Quantidade: " + str(quantidade_produto) + ", Preço: R$" + str(preco_produto))

"""
f-string:
-nos permite compor strings com variáveis sem sair da string
    f"Texto {variável} final do texto."
"""
print()
nome_completo = f"{nome} {sobrenome}"
print(nome_completo)

print(f"Código: {codigo_produto}, Quantidade: {quantidade_produto}, Preço: R${preco_produto:.2f}")

"""
Formatadores:
- Casas decimais: .nf
- Separador de milhares: ,
- Porcentagem: %
"""
#Casas decimais
print()
print(f"{pi:.2f}")
print()

#Separador de milhares
habitantes_sp = 810729
print(f"{habitantes_sp:,}")
capital = 1000000.50
print(f"{capital:,.2f}")
print()

#Porcentagem
valor_compra = 100
desconto = .3
valor_final = valor_compra * (1 - desconto)
print(f"Valor compra: R$ {valor_compra:,.2f}")
print(f"Desconto: {desconto:.2%}")
print(f"Valor com desconto: R$ {valor_final:,.2f}")

