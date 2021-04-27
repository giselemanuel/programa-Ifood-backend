"""
Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função insere_par_remove_impar(lista) que recebe uma lista de números inteiros como parâmetro e retorna uma pilha de acordo com a seguinte regra: para cada elemento da lista, se o número for par, deve ser inserido na pilha. Caso contrário, deve ser removido.

0 deve ser considerado par.

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE

É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade Pilha - Funções Básicas para implementar a função insere_par_remove_impar. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos

Chamada da função insere_par_remove_impar(lista)
Entrada: [1, 2, 3]
Saída: []

Entrada: [1, 2, 3, 4]
Saída: [4]

Entrada: []
Saída: []

Entrada: [1]
Saída: []

Entrada: [2, 2, 2, 2, 1, 1, 1]
Saída: [2]

Entrada: [1, 2, 3, 4, 6, 8]
Saída: [4, 6, 8]
"""

# função cria_pilha -------------------------------
def cria_pilha():
    stack = []


# função tamanho ----------------------------------
def tamanho(pilha):
    return len(pilha)


# função cria_pilha -------------------------------
def adiciona(pilha, elemento):
    if len(pilha) != 0:
        pilha.append(elemento)
    else:
        pilha = None
        return pilha


# função remove -----------------------------------
def remove(pilha):
    if len(pilha) != 0:
        remove = pilha.pop()
        return remove
    else:
        pilha = None
        return pilha


# função insere_par_remove_impar -----------------
def insere_par_remove_impar(lista):
    nova_pilha = []
    cria_pilha()

    # se num da lista par , adicionar na pilha LIFO
    for num in range(0, len(lista)):
        if num % 2 == 0:
            adiciona(nova_pilha, num)
        elif num % 2 != 0:  # se num da lista impar
            remove(nova_pilha)
    # retorna None se lista estiver vazia
    if len(lista) == 0:
        lista = None
        return lista


# define variáveis ------------------------------
minha_lista = (1, 2, 30)
cria_pilha()

# chama funções ---------------------------------
insere_par_remove_impar(minha_lista)
