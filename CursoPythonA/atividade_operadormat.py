#Atividade 1
raio = float(input("Digite o valor do raio: "))
pi = float(3.14)
area = pi * (raio ** 2)
perimetro = (2 * pi) * raio
diametro = raio * 2

print("--Cálculos--")
print(f"A área com o raio por {raio} é equivalente a {area} m²")
print(f"O perímetro é equivalente a {perimetro}")
print(f"e o diâmetro é equivalente a {diametro}")
print()

#Atividade 2
print("--Conversor de Graus--")
celsius = float(input("Digite o valor em graus Celsius: "))
farenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15

print(f"{celsius} ºC convertidos para Farenheit são iguais a {farenheit}, e convertidos para Kelvin são {kelvin}")
print()

#Atividade 3
print("--Cálculo de Média--")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))
n4 = float(input("Digite a quarta nota do aluno: "))

media = float((n1 + n2 + n3 + n4) / 4)

print(f"A média final do aluno é {media:.1f}")


