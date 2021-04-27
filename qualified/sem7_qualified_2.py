"""
Descrição
Crie quatro funções básicas para simular uma Fila:

cria_fila(): Retorna uma fila vazia.
tamanho(fila): Recebe uma fila como parâmetro e retorna o seu tamanho.
adiciona(fila, valor): Recebe uma fila e um valor como parâmetro, adiciona esse valor na última posição da fila e a retorna.
remove(fila): Recebe uma fila como parâmetro e retorna o valor do início da fila. Se a fila estiver vazia, deve retornar None.
Lembre-se:

A fila funciona seguindo a sequência FIFO(First In First Out) - Primeiro a entrar, primeiro a sair.
Em python, a fila é implementada utilizando a estrutura de uma lista.
Exemplos

Função cria_fila()
Saída: []
Função tamanho(fila)
# minha_fila = [9, 1, 2, 3, 100]
Entrada: minha_fila
Saída: 5
Função adiciona(fila, valor)
# minha_fila = [1, 2, 3]
Entrada: minha_fila, 100
Saída: [1, 2, 3, 100]
Função remove(fila) - exibir o número removido
# minha_fila = [1, 2, 3]
Entrada: minha_fila
Saída: [2, 3]

# minha_fila = []
Entrada: minha_fila
Saída: None

"""


# funçao cria_fila -----------------------------------
def cria_fila():
    fila = []
    return fila


# funçao tamanho---------------------------------------
def tamanho(fila):
    return len(fila)


# funçao adiciona -------------------------------------
def adiciona(fila, valor):
    fila.append(valor)
    return fila


# funçao remove ---------------------------------------
def remove(fila):
    if len(fila) != 0:
        removido = fila.pop(0)
        return removido
    else:
        fila = None
        return fila


# define variável -------------------------------------
minha_fila = [9, 1, 2, 3, 100]

# chama funções ---------------------------------------
cria_fila()
tamanho(minha_fila)
adiciona(minha_fila, 100)
remove(minha_fila)