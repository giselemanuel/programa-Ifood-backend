"""
Descrição
Utilizando as mesmas 8 funções das atividades Pilha- Funções Básicas e Fila - Funções Básicas:

cria_fila()
tamanho(fila)
adiciona(fila, valor)
remove(fila):
Implemente a função fila_prioridade(lista) que recebe uma lista com números inteiros que representam idades de pessoas. A lista representa a ordem de chegada de cada pessoa. A função deve retornar uma fila que dê prioridade aos idosos.

Pessoas com 65 anos ou mais devem ser colocadas no início da fila, mas respeitando o funcionamento normal da fila (primeiro a entrar, primeiro a sair).

DICA: VOCÊ PODE UTILIZAR MAIS DE UMA FILA PARA RESOLVER O PROBLEMA !

Lembre-se:

A fila funciona seguindo a sequência FIFO(First In First Out) - Primeiro a entrar, primeiro a sair.
IMPORTANTE

É OBRIGATÓRIO utilizar pelo menos as funções cria_fila, adiciona e remove da atividade anterior para implementar a função fila_prioridade. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos

Chamada da função fila_prioridade(lista)
Entrada: [18, 20, 23, 18]
Saída: [18, 20, 23, 18]

Entrada: [18, 23, 65, 89]
Saída: [65, 89, 18, 23]

Entrada: [30, 70]
Saída: [70, 30]

Entrada: []
Saída: []

Entrada: [65, 30, 70, 18, 66]
Saída: [65, 70, 66, 30, 18]

"""


# função cria_fila --------------------------------
def cria_fila():
    nova_fila = []
    return nova_fila


# função tamanho ----------------------------------
def tamanho(fila):
    return len(fila)


# função adiciona ---------------------------------
def adiciona(fila, elemento):
    fila.append(elemento)
    return fila


# função remove ----------------------------------
def remove(fila):
    if len(fila) != 0:
        removido = fila.pop(0)
        return removido
    else:
        fila = None
        return fila


# função fila_prioridade -------------------------
def fila_prioridade(lista):
    nova_fila = []
    lista_preferencial = []
    lista_normal = []
    cria_fila()  # chama função cria_fila()

    # se lista não estiver vazia
    if len(lista) != 0:
        for num in lista:
            if num < 65:  # cria lista normal
                lista_normal.append(num)

            elif num >= 65:  # cria lista preferêncial
                lista_preferencial.append(num)

        lista_preferencial.extend(lista_normal)  # unifica as duas lista
        adiciona(nova_fila, lista_preferencial)

    else:
        return lista


# declara variáveis -----------------------------
nova_lista = [18, 20, 23, 18]
nova_fila = cria_fila()

# chama função ----------------------------------
fila_prioridade(nova_lista)