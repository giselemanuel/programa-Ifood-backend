"""
Descrição
Nesta atividade você deve criar uma classe simples chamada Pessoa, onde o seu construtor deve inicializar os seguintes atributos da classe:

nome: deve ser uma string
rg: deve ser uma string
pai: é um objeto do tipo Pessoa inicializado como None(vazio)
mae: é um objeto do tipo Pessoa inicializado como None(vazio)
Exemplos

p = Pessoa("Naruto", "111111")
p.nome --> "Naruto"
p.rg --> "111111"
p.pai --> None
p.mae --> None
"""

# Definição da classe Pessoa


class Pessoa:
    def __init__(self, nome, rg):  # construtor init
        self.nome = nome
        self.rg = rg
        self.pai = None
        self.mae = None


p = Pessoa("Naruto", "111111")  # instancia o objeto p
