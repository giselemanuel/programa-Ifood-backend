"""
Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função inverte_texto(texto) que recebe um texto(string) como parâmetro e retorna seu conteúdo invertido.

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE

É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade anterior para implementar a função inverte_texto. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos

Chamada da função inverte_texto(texto)
Entrada: "abc"
Saída: "cba"

Entrada: ""
Saída: ""

Entrada: "a"
Saída: ""

Entrada: "aAbA"
Saída: "AbAa"

"""


# Função cria_pilha----------------------------------
def cria_pilha():
    nova_pilha = []
    return nova_pilha


# Função tamanho--------------------------------------
def tamanho(pilha):
    return len(pilha)


# Função adiciona-------------------------------------
def adiciona(pilha, elemento):
    if elemento == '':
        return elemento
    else:
        pilha.append(elemento)
    return pilha


# Função remove---------------------------------------
def remove(pilha):
    if len(pilha) == 0:
        pilha = None
        return pilha
    else:
        removido = pilha.pop()
        return removido
        # pilha.pop()
        # return pilha


# Função inverte_texto--------------------------------
def inverte_texto(texto):
    nova_pilha = []

    # retorna none em caso de lista vazia
    if texto == '':
        texto = ''
        return texto

    elif texto == 'a':  # retorna vazio em caso de a
        nova_pilha.append(texto)
        remove(nova_pilha)  # chama função remove

    elif texto != '':  # retorna string invertida se não estiver vazia
        cria_pilha()  # chama função cria_pilha
        inverso = ''
        if len(texto) > 0:
            inverso = texto[::-1]
            adiciona(nova_pilha, inverso)  # chama função adiciona
            # return inverso
        return inverso


# declara variável ---------------------------------
meu_texto = "abc"

# chama de função ----------------------------------
inverte_texto(meu_texto)
