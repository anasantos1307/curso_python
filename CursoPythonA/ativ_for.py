# Atividade 1
for i in range(1, 50, +2):
    print(i)

# Atividade 2
numero = int(input("Digite o número que deseja ser visto a tabuada: "))

for n in range(1, 11):
    print(f"{numero} x {n} = {numero * n}")

# Atividade 3

n_compras = int(input("Quantas compras foram realizadas: "))
total = float(0)

for compra in range(n_compras):
    valor_compra = float(input(f"Valor da {compra + 1}ª compra: R$ "))
    total += valor_compra

print()
print(f"Você gastou um total de: R$ {total:,.2f}")