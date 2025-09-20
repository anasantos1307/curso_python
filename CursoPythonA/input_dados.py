"""
Input de dados:
-função input()
    input(argumento do tipo string)
"""

codigo_produto = input("Informe o código do produto: ")
quantidade_produto = int(input(f"Quantidade de {codigo_produto}: "))
preco_produto = float(input(f"Preço de {codigo_produto}: R$ "))
print()
#print(codigo_produto)
#print(quantidade_produto * 2)

print(f"Código: {codigo_produto}, Quantidade: {quantidade_produto}, Preço: R${preco_produto:,.2f}")
