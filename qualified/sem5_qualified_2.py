# função para somar as duas listas
"""
Descrição
Eu sou novo na programação e gostaria da sua ajuda para somar 2 arrays. Na verdade, eu queria somar todos os elementos desses arrays.

P.S. Cada array tem somente numeros inteiros e a saída da função é um numero também.

Crie uma função chamada array_plus_array que recebe dois arrays(listas) de números e some os valores de todos os elementos dos dois arrays.

O resultado deverá ser um número que representa a soma de tudo.

Exemplos
Entrada: [1, 1, 1], [1, 1, 1]
Saída: 6
Entrada: [1, 2, 3], [4, 5, 6]
Saída: 21
"""
# função que soma os valores das duas listas
def array_plus_array(arr1,arr2):
    soma_l1 = 0
    soma_l2 = 0
    total = 0

# soma os elemento da lista 1
    for l1 in list1:
        soma_l1 += l1

# soma os elementos da lista 2
    for l2 in list2:
        soma_l2 += l2

# total da soma das duas listas
    total = soma_l1 + soma_l2
    print(total)

 # difinição das listas   
list1 = [-1, -2, -3]
list2 = [-4, -5, -6]

# chama a função e passa a lista
array_plus_array(list1,list2)