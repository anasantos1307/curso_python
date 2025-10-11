"""
Programação Orientada a Objeto

Definição: è um paradigma de programação onde o objeto central do desenvolvimento são as
entidades da aplicação, por exemplo se estamos trabalhando com um sistema de banco as entidades
seriam, Cliente, Gerente, etc.

Sintaxe:
class NomeClass:
    atributos
    métodos

Padrões:
- Nomes das classes são em PascalCase

Conceitos importantes:
-Classe
-Instância
- Atributos
- Métodos
- Herança
- Polimorfismo
- Encapsulamento
"""

class ClienteBanco:
    #Listagem: tipagem dos aributos
    nome: str
    conta: str
    saldo: float

    #Construtor
    def __init__(self, nome: str, conta: str, saldo: float):
        self.nome = nome
        self.conta = conta
        self.saldo  = saldo

    def consultar_saldo(self) -> None:
        print(f"{self.nome}, seu saldo é: R${self.saldo:,.2f}")

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor > self.saldo:
            print("Saldo Insuficiente!")
        else:
            self.saldo -= valor

    #Representação
    def __repr__(self):
        return  f"Cliente= (Nome: {self.nome}, Conta: {self.conta!r}, Saldo:R$ {self.saldo:,.2f})"

class ClientePrata(ClienteBanco):
    pontos: float
    def __init__(self, nome: str, conta: str, saldo: float):
        super().__init__(nome, conta, saldo)
        self.pontos = saldo // 5

    def pegar_emprestimo(self, valor: float):
        if self.saldo > 0:
            self.saldo += valor
        else:
            print("Recusado.")

class ClienteOuro(ClientePrata):
    def __init__(self, nome: str, conta: str, saldo: float):
        super().__init__(nome, conta, saldo)
        self.pontos = saldo // 3

    def investimento(self, investir: float):
        resultado = investir * 0.05
        self.saldo -= investir
        return print(f"Seu investimento terá resultado de R${resultado:,.2f}")




# joao = ClienteBanco("João", "1", 3000)
# print(joao)
# joao.consultar_saldo()
# joao.depositar(1000)
# joao.sacar(5000)
# joao.consultar_saldo()
#
# print()
# ana = ClienteBanco("Ana", "2", 2500)
# print(ana)
# ana.consultar_saldo()
# ana.depositar(1000)
# ana.consultar_saldo()
# print()
#
# maria = ClientePrata("Maria", "3", 10000)
# print(maria)
# print(maria.pontos)
# maria.pegar_emprestimo(2000)
# maria.consultar_saldo()
# print()

daniel = ClienteOuro("Daniel", "4", 20000)
daniel.consultar_saldo()
daniel.investimento(8000)
