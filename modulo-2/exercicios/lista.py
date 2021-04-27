lista_compras = ['Café', 'Açucar', 'Filtro para café', 'Chocolate', 'Cerveja']

# exibe o tamanho da lista
print(len(lista_compras))

#adicionar um elemeto na lista no final
lista_compras.append('Frango')
print(lista_compras)

# insere no final da lista a string separando seus caracteres cada um com uma posição dentro ta lista
lista_compras.extend('Frutas')
print(lista_compras)

# insere um elemento na lista no indice informado dentro da função
lista_compras.insert(1, "Arroz")
print(lista_compras)

# remove o último elemento da lista
lista_compras.pop()
print(lista_compras)

# ordena os elementos da lista, string em ordem alfabética, e numeros em ordem crescente
lista_compras.sort()
print(lista_compras)

# exibe a lista invertida elemento do final no começo
lista_compras.reverse()
print(lista_compras)

