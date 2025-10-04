"""04/10/2025"""
"""
HR - APP
Nesse app o time RH receberá:
- nome do funcionário
- sobrenome do funcionário
- telefone
- salário bruto

Para o cadastro, deverá ter:
- id pro fucionário
- nome completo
- telefone
- e-mail pro funcionário
- salário líquido
"""
from utils.hr import calcula_salario, formatar_telefone, gerar_email, gerar_id


def main():
    funcionarios = []
    while True:
        nome = input("Nome do funcionário (ou Enter para sair): ").strip()
        if nome:
            sobrenome = input("Sobrenome: ").strip()
            nome_completo = f"{nome.title()} {sobrenome.title()}"
            telefone = input("Telefone (com DDD): ")
            salario_b = float(input("Salário bruto: R$"))
            #Criação do Funcionário
            #gerar um id
            #montar o nome completo
            #formatar telefone
            #gerar email da empresa
            #calcular o salário líquido
            funcionario = {}
            funcionario.update(id = gerar_id())
            funcionario.update(nome_completo = nome_completo)
            funcionario.update(telefone = formatar_telefone(telefone))
            funcionario.update(email = gerar_email(nome, sobrenome))
            funcionario.update(salario = calcula_salario(salario_b))
            funcionarios.append(funcionario)
        else:
            print("Obrigado pela preferência!")
            break
    print(funcionarios)

if __name__ == '__main__':
    main()