class Pilha:
    def __init__(self):
        self.lista = []

    def push(self, item):
        return self.lista.append(item)

    def pop(self):
        return self.lista.pop()

    def tamanho (self):
        return len(self.lista)

nova_lista = Pilha()
nova_lista.push("Gisele")
nova_lista.push("Paulo")
nova_lista.push("Caroline")

nova_lista.lista