"""
Descrição do Exercício:
Escrever as classes gato, caneta e relogio, atribuindo suas características
e métodos, e colocar o print no Discord.
Aluno: Gisele Manuel
"""

# classe gato


class Gato:
    def __init__(self, cor, sexo, raca, idade):  # construtor  com os atributos
        self.cor = cor
        self.sexo = sexo
        self.raca = raca
        self.idade = idade

    def dormir(self, local_dormir):
        self.local_dormir = local_dormir

    def comer(self, racao):
        self.racao = racao

    def miar(self, situacao):
        self.situacao = situacao

    def vacinar(self, situacao_vacina):
        self.situacao_vacina = situacao_vacina

# classe caneta


class Caneta:
    def __init__(self, cor, marca, tipo):
        self.cor = cor
        self.marca = marca
        self.tipo = tipo

    def escrever(self, local):
        self.local = local

# classe Relógio


class Relogio:
    def __init__(self, tipo, marca, tamanho):
        self.tipo = tipo
        self.marca = marca
        self.tamanho = tamanho

    def exibir_hora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo




