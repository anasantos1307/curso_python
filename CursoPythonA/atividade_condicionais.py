# Atividade 1
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2

if media == 10:
    status = "Aprovado com Distinção"
elif 7 <= media <= 9.9:
    status = "Aprovado"
elif media > 10:
    status = "Algo está incorreto, verifique as notas"
else:
    status = "Reprovado"

print(f"Média: {media:.1f}")
print(f"Status: {status}")
print()

# Atividade 2
lado_1 = float(input("Digite o primeiro lado do triângulo: "))
lado_2 = float(input("Digite o segundo lado do triângulo: "))
lado_3 = float(input("Digite o terceiro lado do triângulo: "))
print()

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print("É possível formar um triângulo com esses valores")
    if lado_1 == lado_2 and lado_1 == lado_3 and lado_2 == lado_3:
        print("Este é um triângulo Equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Este é um triângulo Isósceles")
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print("Este é um triângulo Escaleno")
    else:
        print("Não foi possível definir um triângulo")
else:
    print("Não é possível formar um triângulo com esses valores.")
print()

#Atividade 3

salario = float(input("Digite o seu sálario: "))

if salario <= 2000:
    print("Você está Isento")
elif 2000 <= salario <= 3500:
    print(f"Você deve uma alíquota de 10%, no valor de R${salario * 0.10:.2f}")
elif 3500 <= salario <= 5000:
    print(f"Você deve uma alíquota de 20%, no valor de R${salario * 0.15:.2f}")
else:
    print(f"Você deve uma alíquota de 20%, no valor de R${salario * 0.20:.2f}")
