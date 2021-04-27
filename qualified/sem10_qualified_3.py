"""
Descrição
Nesta atividade você deve criar uma classe simples chamada Pessoa com o mesmos atributos da atividade anterior Pessoa com Pai e Mãe, mas adicionando mais 3 métodos:

Atributos

nome
rg
pai
mae

Métodos

adiciona_pai - já feito na atividade anterior
adiciona_mae - já feito na atividade anterior
eh_mesma_pessoa
eh_antecessor_direto
eh_irmao
O método eh_mesma_pessoa deve receber um objeto do tipo Pessoa como parâmetro e:

retornar True se as pessoas tiverem o mesmo rg, mesmo nome e mesma mãe
retornar True se uma das pessoas não tiver mãe, mas nome e rg são iguais
retornar False em qualquer outro caso
O método eh_antecessor_direto deve receber um objeto do tipo Pessoa como parâmetro e retornar True se o objeto recebido é pai OU mãe do objeto que invocou o método.

O método eh_irmao deve receber um objeto do tipo Pessoa como parâmetro e retornar True se as pessoas possuem um antecessor em comum. Caso contrário, retornará False.

Exemplos:

p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")

p1.eh_mesma_pessoa(p1) --> True
p1.eh_mesma_pessoa(p2) --> False

p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Verifica se as pessoas são antecessoras de p1
p1.eh_antecessor_direto(p3) --> True
p1.eh_antecessor_direto(p4) --> True
p1.eh_antecessor_direto(p2) --> False

# Adiciona pai e mãe de p2
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

# Verifica se p2 é irmão de p1
p1.eh_irmao(p2) --> True
p1.eh_irmao(p4) --> False
"""


# classe da entidade pessoa -------------------------------------
class Pessoa:
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg
        self.pai = None
        self.mae = None

    # método adiciona pai -------------------------------------------
    def adiciona_pai(self, pai):
        self.pai = pai

    # método adiciona mãe --------------------------------------------
    def adiciona_mae(self, mae):
        self.mae = mae

    # método eh_mesma_pessoa ------------------------------------------
    def eh_mesma_pessoa(self, Pessoa):

        if self.nome == Pessoa.nome and self.mae == Pessoa.mae and self.rg == Pessoa.rg:
            return True
        elif self.nome == Pessoa.nome and self.rg == Pessoa.rg and self.mae == None:
            return True
        else:
            return False

    # método eh_antecessor_direto ---------------------------------------
    def eh_antecessor_direto(self, Pessoa):
        if self.mae == Pessoa or self.pai == Pessoa:
            return True
        else:
            return False

# método eh_irmao ----------------------------------------------------
    
    def eh_irmao(self, Pessoa):
        if self.mae == Pessoa.mae and self.pai == Pessoa.pai:
            return True
        else:
            return False


# instancia objetos da classe pessoa ---------------------------------
p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")
p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Verifica se é a mesma pessoa --------------------------------------
p1.eh_mesma_pessoa(p1)
p1.eh_mesma_pessoa(p2)

# Adiciona pai e mãe de p1 ------------------------------------------
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p2 ------------------------------------------
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

# Verifica se p2 é irmão de p1 --------------------------------------
p1.eh_irmao(p2)
p1.eh_irmao(p4)

# Verifica se as pessoas são antecessoras de p1 ---------------------
p1.eh_antecessor_direto(p3)
p1.eh_antecessor_direto(p4)
p1.eh_antecessor_direto(p2)

# Verifica se p2 é irmão de p1 --------------------------------------
p1.eh_irmao(p2)
p1.eh_irmao(p4)

# Verifica se as pessoas são antecessoras de p1 ---------------------
p1.eh_antecessor_direto(p3) 
p1.eh_antecessor_direto(p4)
p1.eh_antecessor_direto(p2)
