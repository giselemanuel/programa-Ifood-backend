"""
Descrição
Crie uma função chamada distinct que recebe uma lista de números inteiros e retorna a mesma lista sem números duplicados.

Importante: A lista final deve estar na mesma ordem da lista original, mas sem os números duplicados.

Exemplos
Entrada: [1, 2, 2, 3, 3, 4]
Saída: [1, 2, 3, 4]

Entrada: [4, 1, 3, 2, 3, 4]
Saída: [4, 1, 3, 2]

Entrada: [4, 1, 1, 1, 4, 2, 2]
Saída: [4, 1, 2]

"""
# função que remove duplicado
def distinct(seq):
    # define uma variável do tipo lista que irá gerar uma nova lista sem duplicados
    nova_lista = []
    # navega pela lista e insere o valor na nova lista caso não existe este elemento
    for dup in seq:
        if dup not in nova_lista:
            nova_lista.append(dup)
    # imprime nova lista
    print(nova_lista)
    return nova_lista

# lista com elementos
lista = [1, 2, 2, 3, 3, 4]
# chama a função
distinct(lista)