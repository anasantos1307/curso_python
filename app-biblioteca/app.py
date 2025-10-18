from traceback import print_tb

from entities.biblioteca import Endereco, Livro, Membro, Biblioteca
from utils.cep import busca_cep

cep = "09751-000"
numero = "100"
informacoes_endereco = busca_cep(cep=cep)

e1 = Endereco(
    logradouro=informacoes_endereco["address"],
    numero=numero,
    bairro=informacoes_endereco["district"],
    cidade=informacoes_endereco["city"],
    estado=informacoes_endereco["state"],
    cep=cep
)

print(e1)
print()

iracema = Livro("Iracema", "José de Alencar", 1865)
revolucao_bichos = Livro("A Revolução dos Bichos", "George Orwell", 1945)
o_pianista = Livro("O Pianista", "Wladyslaw Szpilman", 1946)

print(iracema)
print()

joao = Membro("João", e1)
ana = Membro("Ana", e1)
print(joao)
print(ana)
print()

biblioteca = Biblioteca("Bliblioteca", e1)
biblioteca.receber_livro(iracema)
biblioteca.receber_livro(revolucao_bichos)
biblioteca.receber_livro(o_pianista)
print(biblioteca.acervo)
print()

biblioteca.cadastrar_membro(joao)
biblioteca.cadastrar_membro(ana)
print(joao)
print()

biblioteca.emprestar_livro(iracema, joao)
print("Acervo", biblioteca.acervo)
print("João", joao.livros)
print()

biblioteca.devolver_livro(joao, iracema)
print(joao.livros)
