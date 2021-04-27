class Fila:
    def __init__(self):
        self.queue = []

    def tamanho(self):
        return len(self.queue)

    def partida(self):
        self.queue.pop(0)

    def chegada(self, pessoa):
        self.queue.append(pessoa)
    

#chama a classe Fila
banco_fila = Fila()

# chama o método  chegada()  da classe para adicionar elementos na lista
banco_fila.chegada('Gisele')
banco_fila.chegada('Maria')
banco_fila.chegada('Guilherme')

# exibe os elementos da fila
print(banco_fila.queue) 
# exibe o total de elementos da fila
print(banco_fila.tamanho())
    
# chama o método  partidas da classe remove o primeiro elemento inserido 
banco_fila.partida()
print(banco_fila.queue)
print(banco_fila.tamanho())

    
