class Cachorro:
    def __init__(self, nome, cor, raca, porte, qtde_patas): #  __init__ é um construtor , utilizado para inicializar o objeto desta classe.
        self.nome = nome
        self.raca = raca
        self.porte = porte
        self.qtde_patas = qtde_patas

    def comer(self, racao):
        self.racao = racao

    def dormir(self, lugar):
        self.lugar = lugar

    def latir(self, gatilho):
        self.gatilho = gatilho

    def fazer_coco(self, lugar):
        self.lugar = lugar
        
    def fazer_xixi(self, lugar):
        self.lugar = lugar
