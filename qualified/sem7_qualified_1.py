"""

Descrição
Crie quatro funções básicas para simular uma Pilha:

cria_pilha(): Retorna uma pilha vazia.
tamanho(pilha): Recebe uma pilha como parâmetro e retorna o seu tamanho.
adiciona(pilha, valor): Recebe uma pilha e um valor como parâmetro, adiciona esse valor na pilha e a retorna.
remove(pilha): Recebe uma pilha como parâmetro e retorna o valor no topo da pilha. Se a pilha estiver vazia, deve retornar None.
Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
Exemplos

Função cria_pilha()
Saída: []
Função tamanho(pilha)
# minha_pilha = [9, 1, 2, 3, 100]
Entrada: minha_pilha
Saída: 5
Função adiciona(pilha, valor)
# minha_pilha = [1, 2, 3]
Entrada: minha_pilha, 100
Saída: [1, 2, 3, 100]
Função remove(pilha)
# minha_pilha = [1, 2, 3]
Entrada: minha_pilha
Saída: [1, 2]

# minha_pilha = []
Entrada: minha_pilha
Saída: None
"""


# Função cria_pilha ----------------------------------


def cria_pilha():
    pilha = []
    return pilha

# Função tamanho -------------------------------------


def tamanho(pilha):
    return len(pilha)

# Função adiciona ------------------------------------


def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha

# Função remove --------------------------------------


def remove(pilha):
    if len(pilha) != 0:
        removido = pilha.pop()
        return removido
    else:
        pilha = None
        return pilha


# Define variável -----------------------------------
minha_pilha = [1, 2, 3]

# Chama Funções -------------------------------------
tamanho(minha_pilha)
remove(minha_pilha)
adiciona(minha_pilha, 100)
