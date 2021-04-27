class Pessoa:
    def __init__(self, nome, cpf, tel, rg):
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.rg = rg

    def exibir_info(self):
        print(f'''
        INFORAMAÇÕES DO CLIENTE
        -----------------------
        Nome: {self.nome}
        Telefone: {self.tel}   
        CPF: {self.cpf}
        RG: {self.rg}
        -----------------------
        ''')


# Classe filha Proprietário(Pessoa) ----------------------------------------------------

class Proprietario(Pessoa):
    def __init__(self, nome, cpf, tel, rg, pedido, forma_pagamento):
        super().__init__(nome, cpf, tel, rg)
        self.pedido = pedido
        self.forma_pagamento = forma_pagamento

    def exibir_status_pedido(self, status_pedido):
        self.status_pedido = status_pedido
        return self.status_pedido

# Classe filha Entregador(Pessoa) ----------------------------------------------------

class Entregador(Pessoa):
    def __init__(self, nome, cpf, tel, rg, endereco):
        super().__init__(nome, cpf, tel, rg)
        self.endereco = endereco

    def receber_pedido(self, pedido):
        self.pedido = pedido
        return self.pedido


# Classe filha Cliente(Pessoa) ----------------------------------------------------

class Cliente(Pessoa):
    def __init__(self, nome, cpf, tel, rg, endereco):
        super().__init__(nome, cpf, tel, rg)
        self.endereco = endereco

    def realizar_pedido(self, pedido):
        self.pedido = pedido
        return self.pedido


cliente1 = Cliente('Gisele', '999.999.999-99', '(19)9999-9999', '99.999.999-9', 'Campinas - SP')
cliente2 = Proprietario('Gisele', '999.999.999-99', '(19)9999-9999', '99.999.999-9', 'Hamburger', 'Débito')
cliente2.exibir_info()
print(cliente2.exibir_status_pedido('Pedido envido'))