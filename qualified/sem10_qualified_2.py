"""
Descrição
Nesta atividade você deve criar uma classe simples chamada Pessoa com o mesmos atributos da atividade anterior Pessoa, mas adicionando 2 métodos:

Atributos

nome
rg
pai
mae

Métodos

adiciona_pai
adiciona_mae
O método adiciona_pai deve receber um objeto do tipo Pessoa e atribuí-lo ao atributo pai do objeto que invocou o método.
O método adiciona_mae deve receber um objeto do tipo Pessoa e atribuí-lo ao atributo mae do objeto que invocou o método.

Exemplos:

p = Pessoa("Naruto", "111111")
p2 = Pessoa("Minato", "010101")
p3 = Pessoa("Kushina", "020202")
p.adiciona_pai(p2)
p.adiciona_mae(p3)

p.pai.nome --> "Minato"
p.mae.nome --> "Kushina"

"""

# classe da entidade Pessoa -------------------------
class Pessoa:
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg
        self.pai = None
        self.mae = None

    # método adiciona pai ----------------------------
    def adiciona_pai(self, pai):
        self.pai = pai
        # return self.pai

    # método adiciona mãe ----------------------------
    def adiciona_mae(self, mae):
        self.mae = mae
        # return self.mae


# instancia os objetos -------------------------------
p = Pessoa("Naruto", "111111")
p_pai = Pessoa("Minato", "010101")
p_mae = Pessoa("Kushina", "020202")

# atribui o objeto invocado pelo método adiciona_pai ao atributo de pai -----------------------------------
p.adiciona_pai(p_pai)

# atribui o objeto invocado pelo método adiciona_pai ao atributo de pai ----------------------------------
p.adiciona_mae(p_mae)

print(f'Pai {p.pai.nome}')
print(f'Mãe {p.mae.nome}')
print(f'Filho {p.nome}')
