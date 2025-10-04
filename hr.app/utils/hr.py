from random import randint

def gerar_id() -> int:
    """
    Função que gera um id aleatório de 4 dígitos.
    :return: id aleatório de 4 dígitos
    """
    return randint(1000, 9999)

def formatar_telefone(numero_telefone: str) -> str:
    """
    Função que recebe o número de telefone e retorna formatado
    :param numero_telefone:
    :return:
    """
    numero_formatado = (numero_telefone.replace("-", "").replace("(", "").replace(")", ""))
    return numero_formatado

def gerar_email(nome: str, sobrenome: str) -> str:
    """
    Gera um email no formato nome.sobrenome@senai.com
    :param nome: primeiro nome
    :param sobrenome: último nome
    :return: nome.sobrenome@senai.com
    """
    return f"{nome}.{sobrenome}@senai.com"

def calcula_salario(salario: float) -> float | str:
    """
    Calcula o salário líquido
    :param salario: salário bruto
    :return: salário líquido
    """
    if 0 <= salario <= 2000:
        return salario
    elif 2000 < salario <= 3500:
        return salario * .9
    elif 3500 < salario <= 5000:
        return salario * .85
    elif salario > 5000:
        return salario * .8
    else:
        return "Salário Inválido!"

