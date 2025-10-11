"""
Tratamento de Exceções

Finalidade: Tratamos as exceções para que nossas aplicações não 'quebrem' durante as experiências dos usuários.

Palavras python:
- try
- except
- finally

Sintaxe:

try:
    código principal
except Exception:
    Tratamento de exception
finally:
    bloco finally
"""
from http import HTTPStatus
from wsgiref.util import request_uri


def soma(a: int, b:int) -> int | str:
    """
    Soma
    :param a: número
    :param b: número
    :return: soma de a e b
    """
    try:
        soma = a + b
        return soma
    except TypeError as e:
        return "Não podemos somar string com int, apenas int e int"

# print(soma(10, 10))
# print(soma(10, "10"))

def divisao(a: int, b: int) -> float | str:
    try:
        res = a / b
        return res
    except TypeError:
        return "Não podemos dividir um número por uma string, apenas um int por um int"
    except ZeroDivisionError:
        return "Não podemos dividir um número por 0 (zero)"

# print(divisao(10, 5))
# print(divisao(10, "3"))
# print(divisao(10, 0))

"""
Exemplo de tratamento de exceções em uma API
@app.route("/user/<int;user_id>")
def get_user_by_id(user_id):
    try:
        user = achar(user_id)
        return {"user": user}, HTTPStatus.OK
    except ValueError as e=
        return {"message": "Não achamos"}, HTTPStatus.NOT_FOUND
"""