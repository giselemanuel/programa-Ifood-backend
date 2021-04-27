"""
Crie uma classe automóvel com os respectivos atributos
tipo; modelo; ano; quilometragem rodada (km).
Aluna: Gisele Manuel
"""


class Automovel:

    def __init__(self, tipo, modelo, ano, quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem


automovel1 = Automovel('HB20', 'Hatch', 2019, 1000)
automovel2 = Automovel('Fusca', 'Hatch', 1950, 5000)

print(automovel1.tipo)
print(automovel1.modelo)
print(automovel1.ano)
print(automovel1.quilometragem)
