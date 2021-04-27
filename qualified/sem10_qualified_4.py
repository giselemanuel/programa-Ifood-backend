"""
Descrição
Utilizando a classe Pessoa criada na atividade Parentesco entre Pessoas, crie a função encontre_os_irmaos(lista_pessoas) que recebe uma lista de objetos do tipo Pessoa e retorna uma lista apenas com o nome das pessoas que são irmãos.

Se não houver irmãos na lista, a lista retornada deve ser vazia ([]).

Lembre-se que a mesma pessoa não pode aparecer mais de uma vez na lista final.

Exemplos

p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")
p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p2
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

lista_pessoas = [p1, p2]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
# Exemplo da saída esperada: ["Sasuke", "Itachi"]
p1 = Pessoa("Pessoa 1", "222222")
p2 = Pessoa("Pessoa 2", "202020")
p3 = Pessoa("Pessoa 3", "444444")
p4 = Pessoa("Pessoa 4", "333333")
p5 = Pessoa("Pessoa 5", "555555")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p5
p5.adiciona_mae(p3)
p5.adiciona_pai(p4)

lista_pessoas = [p1, p2, p5]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
# Exemplo da saída esperada: ["Pessoa 1", "Pessoa 5"]
p1 = Pessoa("Pessoa 1", "222222")
p2 = Pessoa("Pessoa 2", "202020")
p3 = Pessoa("Pessoa 3", "444444")
p4 = Pessoa("Pessoa 4", "333333")
p5 = Pessoa("Pessoa 5", "555555")

lista_pessoas = [p1, p2, p3, p4, p5]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
"""


# classe da entidade pessoa ------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg
        self.pai = None
        self.mae = None

    # método adiciona pai -------------------------------------------------------------------
    def adiciona_pai(self, pai):
        self.pai = pai

    # método adiciona mãe -------------------------------------------------------------------
    def adiciona_mae(self, mae):
        self.mae = mae

    # método eh_mesma_pessoa ----------------------------------------------------------------
    def eh_mesma_pessoa(self, Pessoa):

        if self.nome == Pessoa.nome and self.mae == Pessoa.mae and self.rg == Pessoa.rg:
            return True
        elif self.nome == Pessoa.nome and self.rg == Pessoa.rg and self.mae is None:
            return True
        else:
            return False

    # método eh_antecessor_direto -----------------------------------------------------------
    def eh_antecessor_direto(self, Pessoa):
        if self.mae == Pessoa or self.pai == Pessoa:
            return True
        else:
            return False

    # método eh_irmao -----------------------------------------------------------------------
    def eh_irmao(self, Pessoa):
        if self.mae == Pessoa.mae and self.pai == Pessoa.pai:
            return True
        elif self.mae is None and self.pai is None:
            return False
        else:
            return False


# método encontre_os_irmaos -------------------------------------------------------------------------------
def encontre_os_irmaos(lista_pessoas):
    lista_irmao = []  # lista que receberá o atributo nome dos objetos da classe pessoa se forem irmão

    # iteração na lista_pessoas para verificar se os objetos da classe pessoa são irmão
    for p in range(0, len(lista_pessoas)):
        if lista_pessoas[p].eh_irmao(lista_pessoas[p + 1]):
            lista_irmao.append(lista_pessoas[p].nome)  # adiciona o nome da lista_pessoa a lista_irmao
            lista_irmao.append(lista_pessoas[p + 1].nome)  # adiciona o nome da lista_pessoa a lista_irmao
            return lista_irmao
        else:
            lista_irmao = []
            return lista_irmao


# instancia objetos na classe pessoa ----------------------------------------------------------------------
p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")
p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Adiciona pai e mãe de p1 --------------------------------------------------------------------------------
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p2 --------------------------------------------------------------------------------
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

# cria lista variável do tipo lista -----------------------------------------------------------------------
lista_pessoas = [p1, p2]

# Exemplo e chamada da função -----------------------------------------------------------------------------
encontre_os_irmaos(lista_pessoas)









