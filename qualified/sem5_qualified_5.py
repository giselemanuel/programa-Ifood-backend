"""
Descrição
Nesta atividade você terá que fazer a soma dos números positivos dentro de um array/lista.

Crie uma função que recebe um array/lista de números inteiros(tanto negativos quanto positivos) e faz a soma apenas dos números positivos.

A função deve retornar a soma desses valores.

IMPORTANTE: Caso o array/lista esteja vazio, a função deve retornar 0.

Exemplos
Entrada: [1,-4,7,12]
Saída: 1 + 7 + 12 = 20

Entrada: [-1, -1, -9, 1]
Saída: 1

Entrada: []
Saída: 0
"""
# função soma número positivo de uma lista
def positive_sum(arr):
    soma = 0
    # pega somente os números positivos da lista
    for positivo in arr:
        if positivo > 0:
            #print(f'{positivo}', end=' ')
            soma = soma + positivo
    #print(soma)
    return soma

# lista
lista = [1,-4,7,12]

# chana função
positive_sum(lista)