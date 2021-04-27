
class Pilha:
    
    def __init__(self):
        self.lista_filmes = []

    def tamanho(self):
        return len(self.lista_filmes)

    def pop(self):
        return self.lista_filmes.pop()

    def push(self, item):
        return self.lista_filmes.append(item)

# instancia o objeto na classe
gisele = Pilha()

# adiciona elemento na lista
gisele.push("A lagoa Azul")
gisele.push('As Panteras')
gisele.push('Velozos e Furiosos')

# exibe a lista com os elementos
print(gisele.lista_filmes)

# exibe o tamanho da lista
print(f'Tamanho: {gisele.tamanho()}')

# remove o ultimo elemento da lista
gisele.pop()

# exibe os elementos da lista
print(gisele.lista_filmes)
print(f'Tamanho: {gisele.tamanho()}')