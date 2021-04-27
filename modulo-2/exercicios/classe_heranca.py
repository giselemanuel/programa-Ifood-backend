"""
Crie uma classe automóvel com os respectivos atributos
tipo; modelo; ano; quilometragem rodada (km).
Aluna: Gisele Manuel
"""


class Automovel:  # classe mãe

    def __init__(self, tipo, modelo, ano, quilometragem):   # inicializa a clase mãe  com os atributos
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def exibir_info(self):  # método que exibe as informação do automóvel
        print(f'''
        \033[32mTipo:\033[m          {self.tipo}
        \033[32mModelo:\033[m        {self.modelo}
        \033[32mAno:\033[m           {self.ano}
        \033[32mQuilometragem:\033[m {self.quilometragem} km
        ''')


class Carro(Automovel):   # classe filha carro

    def __init__(self, tipo, modelo, ano, queilometragem):  # inicializa a clase filha com os atribuitos que herdará da classe mãe
        super().__init__(tipo, modelo, ano, queilometragem)  # permite acesso dos atrtibutos definidos dentro da classe mãe


class Moto(Automovel):  # classe filha moto

    def __init__(self, tipo, modelo, ano, quilometragem):  # inicializa a clase filha com os atribuitos que herdará da classe mãe
        super().__init__(tipo, modelo, ano, quilometragem)  # permite acesso dos atrtibutos definidos dentro da classe mãe


gisele_carro = Carro('HB20', 'Hatch', '2019', 50000)
gisele_carro.exibir_info()

guilherme_moto = Moto('Honda', 'CB500', '2017', 10000)
guilherme_moto.exibir_info()
