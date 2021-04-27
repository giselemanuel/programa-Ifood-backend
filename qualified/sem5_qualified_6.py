"""
Descrição
Crie uma função chamada find_smallest que recebe uma lista de números inteiros e retorna o menor número da lista.

A lista deve conter apenas números inteiros(negativos e positivos) e não deve ser vazia.

Você deve usar uma das estruturas de repetição de sua preferência para implementar a solução.

Exemplos
Entrada: [34, 15, 88, 2]
Saída: 2

Entrada: [1]
Saída: 1

Entrada: [34, -345, -1, 100]
Saída: -345
"""
# função que localiza o menor valor na lista
def find_smallest(numbers):
    # define o primeiro valor da lista como o menor
    menor = numbers[0]
    # percorre a lista
    for n in numbers:
        # valida se existe um menor valor comparado com numebers[0]
        if n < menor :
            menor = n
    # imprime o menor valor
    print(menor)
    return menor

# lista de valores
lista = [[34, -345, -1, 100]]

# chama função
find_smallest(lista)