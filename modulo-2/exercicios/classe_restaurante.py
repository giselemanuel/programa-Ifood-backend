"""
Construir uma classe mãe denoninada Restaurante, deverá conter
atributos e métodos.
cardápio
dias da semana que o restaurante fica aberto.

3 classe filhas, contendo:
nome do restaurante
Formas de pagamento
"""

# Classe mãe


class Restaurante:
    def __init__(self, cardapio, funcionamento, nome, forma_pagamento):
        self.cardapio = cardapio
        self.funcionamento = funcionamento
        self.nome = nome
        self.forma_pagamento = forma_pagamento

    def exibir_info(self):
        print(f'Nome do Restaurante: {self.nome}\nCardápio: {self.cardapio}\n'
              f'Funcionamento:{self.funcionamento}\nForma de Pagamento{self.forma_pagamento}')

    def realizar_pedido(self):
        print('Pedido recebido')

# 1ª Classe filha


class FastFood(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, forma_pagamento):
        super(FastFood, self).__init__(cardapio, funcionamento, nome, forma_pagamento)

# 2ª Classe filha da classe Restaurante


class Pizzaria(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, forma_pagamento):
        super(Pizzaria, self).__init__(cardapio, funcionamento, nome, forma_pagamento)

# 3ª Classe filha da classe Restaurante


class Doceria(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, forma_pagamento):
        super(Doceria, self).__init__(cardapio, funcionamento, nome, forma_pagamento)

# Classe Pessoa da classe Restaurante


class Pessoa(object):
    def __init__(self, nome, cpf, telefone, rg):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rg = rg


# classe 1ª classe filha de pessoa


class Entregador(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, pedido):
        super(Entregador, self).__init__(nome, cpf, telefone, rg)
        self.endereco = endereco
        self.pedido = pedido

    # método entrega pedido

    def entregar(self):
        pass

# classe 1ª classe filha de pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, celular, pedido):
        super(Cliente, self).__init__(nome, cpf, telefone, rg)
        self.celular = celular
        self.pedido = pedido


class Proprietario(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, entregadores):
        super(Proprietario, self).__init__(nome, cpf, telefone, rg)
        self.entregadores = entregadores